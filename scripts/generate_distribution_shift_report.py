"""
Script to compute comprehensive TRAIN vs TEST distribution shift metrics.
Outputs: artifacts/forensics/distribution_shift_report.csv
"""
import csv
import re
import math
from pathlib import Path
from collections import Counter

URL_PAT = re.compile(r'\.(com|in|org|net|fr|co|io|biz|info)\b', re.IGNORECASE)
DIGIT_PAT = re.compile(r'\d')
PIN_PAT = re.compile(r'\b\d{5,6}\b')
LEGAL_PAT = re.compile(r'\b(pvt|ltd|llc|inc|corp|co|sarl|sa|gmbh|enterprises|services|technologies)\b', re.IGNORECASE)

splits_sources = [
    ('train', 'source1'),
    ('train', 'source2'),
    ('train', 'source3'),
    ('test', 'source1'),
    ('test', 'source2'),
    ('test', 'source3'),
]

metrics = []

for split, src in splits_sources:
    path = Path(f'student_resource/dataset/{split}/{split}_{src}.tsv')
    print(f"Profiling {split} {src}...")
    
    total = 0
    missing_addr = 0
    missing_country = 0
    name_lens = []
    addr_lens = []
    countries = Counter()
    has_digit_addr = 0
    has_pin_addr = 0
    has_url_name = 0
    has_legal_name = 0
    non_ascii_name = 0
    word_counts = Counter()
    name_counts = Counter()
    
    # We sample if dataset is huge, or stream full
    # For exact stats, stream full dataset
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        hdr = [c.strip().lower() for c in next(reader)]
        name_idx = hdr.index('business_name')
        addr_idx = hdr.index('business_address')
        country_idx = hdr.index('country')
        
        for row in reader:
            if not row or len(row) <= max(name_idx, country_idx):
                continue
            total += 1
            name = row[name_idx].strip()
            addr = row[addr_idx].strip() if addr_idx < len(row) else ''
            country = row[country_idx].strip()
            
            # Country
            c_norm = country.upper()
            if 'UNITED STATES' in c_norm or c_norm == 'US' or c_norm == 'USA':
                c_key = 'US'
            elif 'INDIA' in c_norm or c_norm == 'IN' or c_norm == 'IND':
                c_key = 'INDIA'
            elif 'FRANCE' in c_norm or c_norm == 'FR' or c_norm == 'FRA':
                c_key = 'FRANCE'
            elif not c_norm:
                c_key = 'MISSING'
            else:
                c_key = c_norm
            countries[c_key] += 1
            
            # Missingness
            if not addr:
                missing_addr += 1
            if not country or c_key == 'MISSING':
                missing_country += 1
                
            # Lengths
            name_len = len(name)
            name_lens.append(name_len)
            addr_len = len(addr)
            addr_lens.append(addr_len)
            
            # Name patterns
            if URL_PAT.search(name):
                has_url_name += 1
            if LEGAL_PAT.search(name):
                has_legal_name += 1
            if any(ord(c) > 127 for c in name):
                non_ascii_name += 1
                
            words = name.split()
            w_len = len(words)
            if w_len == 1:
                word_counts['1_word'] += 1
            elif w_len == 2:
                word_counts['2_words'] += 1
            else:
                word_counts['3_plus_words'] += 1
                
            # Duplicate name sample (top 200k)
            if total <= 200000:
                name_counts[name.lower()] += 1
                
            # Address patterns
            if addr:
                if DIGIT_PAT.search(addr):
                    has_digit_addr += 1
                if PIN_PAT.search(addr):
                    has_pin_addr += 1
                    
    # Percentiles
    name_lens.sort()
    addr_lens.sort()
    n_median = name_lens[total // 2] if total else 0
    n_p95 = name_lens[int(total * 0.95)] if total else 0
    n_mean = sum(name_lens) / total if total else 0
    
    a_median = addr_lens[total // 2] if total else 0
    a_p95 = addr_lens[int(total * 0.95)] if total else 0
    a_mean = sum(addr_lens) / total if total else 0
    
    # Duplicate rate in sample
    sample_size = min(total, 200000)
    dup_names = sum(c for c in name_counts.values() if c > 1)
    dup_rate = dup_names / sample_size if sample_size else 0
    
    c_us_pct = countries['US'] / total * 100 if total else 0
    c_in_pct = countries['INDIA'] / total * 100 if total else 0
    c_fr_pct = countries['FRANCE'] / total * 100 if total else 0
    c_other_pct = (total - countries['US'] - countries['INDIA'] - countries['FRANCE']) / total * 100 if total else 0

    metrics.append({
        'split': split,
        'source': src,
        'total_records': total,
        'country_us_pct': f"{c_us_pct:.2f}%",
        'country_india_pct': f"{c_in_pct:.2f}%",
        'country_france_pct': f"{c_fr_pct:.2f}%",
        'country_other_pct': f"{c_other_pct:.2f}%",
        'missing_address_pct': f"{missing_addr / total * 100:.2f}%",
        'missing_country_pct': f"{missing_country / total * 100:.2f}%",
        'name_len_mean': f"{n_mean:.1f}",
        'name_len_median': n_median,
        'name_len_p95': n_p95,
        'addr_len_mean': f"{a_mean:.1f}",
        'addr_len_median': a_median,
        'addr_len_p95': a_p95,
        'has_url_name_pct': f"{has_url_name / total * 100:.2f}%",
        'has_legal_suffix_pct': f"{has_legal_name / total * 100:.2f}%",
        'non_ascii_name_pct': f"{non_ascii_name / total * 100:.2f}%",
        'name_1_word_pct': f"{word_counts['1_word'] / total * 100:.2f}%",
        'name_2_words_pct': f"{word_counts['2_words'] / total * 100:.2f}%",
        'name_3plus_words_pct': f"{word_counts['3_plus_words'] / total * 100:.2f}%",
        'addr_has_digits_pct': f"{has_digit_addr / (total - missing_addr) * 100:.2f}%" if total > missing_addr else "0.00%",
        'addr_has_postal_code_pct': f"{has_pin_addr / (total - missing_addr) * 100:.2f}%" if total > missing_addr else "0.00%",
        'duplicate_name_rate_sample': f"{dup_rate * 100:.2f}%",
    })

out_dir = Path("artifacts/forensics")
out_dir.mkdir(parents=True, exist_ok=True)
out_csv = out_dir / "distribution_shift_report.csv"

fieldnames = list(metrics[0].keys())
with open(out_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in metrics:
        writer.writerow(row)

print(f"Generated {out_csv} successfully!")

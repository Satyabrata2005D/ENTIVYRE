#!/usr/bin/env python3
import hashlib
import os
import zipfile
from pathlib import Path
from datetime import datetime

def sha256_file(path, chunk_size=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def sha256_zip_member(zip_path, member_name):
    h = hashlib.sha256()
    with zipfile.ZipFile(zip_path, 'r') as z:
        if member_name in z.namelist():
            with z.open(member_name) as f:
                while chunk := f.read(65536):
                    h.update(chunk)
            return h.hexdigest()
    return None

def inspect_tsv(path):
    p = Path(path)
    if not p.exists():
        print(f"File {path} does not exist.")
        return
    stat = p.stat()
    size = stat.st_size
    mtime = datetime.fromtimestamp(stat.st_mtime).isoformat()
    print(f"--- File: {path} ---")
    print(f"Size: {size:,} bytes ({size / (1024*1024):.2f} MB)")
    print(f"Modified: {mtime}")
    
    # First 5 lines, last 5 lines, and row count
    row_count = 0
    first_5 = []
    last_5 = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            row_count += 1
            if len(first_5) < 5:
                first_5.append(line.rstrip("\r\n"))
            last_5.append(line.rstrip("\r\n"))
            if len(last_5) > 5:
                last_5.pop(0)

    print(f"Row count: {row_count:,}")
    print("First 5 lines:")
    for l in first_5:
        print(f"  {l}")
    print("Last 5 lines:")
    for l in last_5:
        print(f"  {l}")

    print("Calculating SHA-256 (streaming)...")
    h = sha256_file(p)
    print(f"SHA-256: {h}\n")
    return h

print("==================================================")
print("PHASE 1: AUDITING SUBMISSION ARTIFACTS AND OUTPUTS")
print("==================================================")

m_hash = inspect_tsv("output/backup_challenger_005_old/matching_results.tsv")
# Don't do full sha256 of candidate_pairs if 5.6GB unless needed, but let's do inspect
p_cand = Path("output/backup_challenger_005_old/candidate_pairs.tsv")
if p_cand.exists():
    stat = p_cand.stat()
    print(f"--- File: output/backup_challenger_005_old/candidate_pairs.tsv ---")
    print(f"Size: {stat.st_size:,} bytes ({stat.st_size / (1024*1024):.2f} MB)")
    print(f"Modified: {datetime.fromtimestamp(stat.st_mtime).isoformat()}")
    print("Calculating candidate_pairs.tsv SHA-256...")
    c_hash = sha256_file(p_cand)
    print(f"SHA-256: {c_hash}\n")

print("Checking submission ZIP archives in submission/:")
for z_path in sorted(Path("submission").glob("*.zip")):
    stat = z_path.stat()
    print(f"\nZIP: {z_path.name}")
    print(f"  Size: {stat.st_size:,} bytes")
    print(f"  Modified: {datetime.fromtimestamp(stat.st_mtime).isoformat()}")
    with zipfile.ZipFile(z_path, 'r') as z:
        names = z.namelist()
        print(f"  Members: {names}")
        if "matching_results.tsv" in names:
            info = z.getinfo("matching_results.tsv")
            zh = sha256_zip_member(z_path, "matching_results.tsv")
            print(f"  matching_results.tsv uncompressed size: {info.file_size:,}")
            print(f"  matching_results.tsv SHA-256: {zh}")
            print(f"  Matches 0.784 hash ({m_hash}): {'IDENTICAL (CASE A)' if zh == m_hash else 'DIFFERENT'}")

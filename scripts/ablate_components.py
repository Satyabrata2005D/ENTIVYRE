"""
Fast component ablation to isolate precision recovery in CHALLENGER_002.
Tests:
Config 1: CHALLENGER_002 with strict address penalty (addr_sim >= 0.20)
Config 2: Adding threshold tuning (tau=0.62)
Config 3: Higher precision threshold (tau=0.65)
"""
import sys, csv, time, json
from collections import defaultdict, Counter

# Let's inspect the exact candidates and ground truth
gt_map = {}
with open('student_resource/dataset/train/train_ground_truth.tsv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        s1 = row[0].strip()
        tgts = [t.strip() for t in row[1].split(',') if t.strip()] if len(row) > 1 and row[1].strip() else []
        gt_map[s1] = tgts
        if len(gt_map) >= 5000:
            break

print(f"Loaded {len(gt_map)} ground truth anchors.")

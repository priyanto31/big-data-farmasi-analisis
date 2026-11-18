import os

required_files = [
    "data/Dataset_Farmasi_Priyanto_15240017.csv",
    "output/output_farmasi_parquet.zip"
]

for f in required_files:
    print(f"[{'OK' if os.path.exists(f) else 'MISSING'}] {f}")
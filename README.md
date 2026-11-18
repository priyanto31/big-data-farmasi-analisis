# 💊 Big Data Pharmacy Supply Chain Analytics

Platform analitik dan pipeline ETL data rantai pasok perusahaan farmasi berskala nasional (100.000 baris data sintetis) yang menggabungkan eksplorasi data, pemrosesan terdistribusi dengan **Apache Spark (PySpark)**, penyimpanan data lake terkompresi **Parquet (Snappy)**, serta visualisasi bisnis tingkat lanjut dengan **Matplotlib & Seaborn**.

Proyek ini dirancang agar dapat dijalankan secara fleksibel: baik di komputer lokal (VS Code / Python) maupun di cloud via Google Colab.

---

## 🎯 Tujuan & Cakupan Proyek

1. **Data Profiling & Quality Gates:** Memvalidasi integritas 100.000 transaksi medis, memeriksa *missing value*, dan menyimulasikan pembobotan distribusi berdasarkan kategori produk dan wilayah.
2. **Transformasi PySpark:** Pemrosesan data skala besar untuk menghitung umur simpan (kedaluwarsa) obat dan menerapkan penalti logistik kargo laut lintas pulau.
3. **Visualisasi Business Intelligence:** Menerjemahkan data mentah menjadi 4 metrik KPI utama yang mudah dipahami oleh pemangku kepentingan (Direksi / Manajemen Rumah Sakit).

---

## 💻 Panduan Instalasi di Komputer Lokal

### 1. Prasyarat Sistem
* **Python:** Versi 3.10 ke atas.
* **Java (JDK):** OpenJDK 17 LTS (Wajib agar Apache Spark bisa berjalan di lokal Windows/Mac).
* **VS Code / Jupyter:** Ekstensi Jupyter terinstal untuk menjalankan file `.ipynb`.

### 2. Langkah Instalasi (Clone & Setup)

```bash
# 1. Clone repositori ke komputer lokal
git clone [https://github.com/priyanto31/big-data-farmasi-analisis.git](https://github.com/priyanto31/big-data-farmasi-analisis.git)
cd big-data-farmasi-analisis

# 2. Instalasi pustaka pendukung secara otomatis
pip install -r requirements.txt
```

---

## 📁 Struktur Repositori

```text
big-data-farmasi-analisis/
├── .gitignore                                 # Aturan penyaringan file Git
├── README.md                                  # Dokumentasi utama proyek
├── requirements.txt                           # Daftar pustaka Python (Dependencies)
├── data/
│   └── Dataset_Farmasi_Priyanto_15240017.csv  # Dataset sintetis utama (100k baris)
├── notebooks/
│   ├── 01_exploration.ipynb                   # Tahap 1: EDA & Data Profiling
│   ├── 02_pyspark_transform.ipynb             # Tahap 2: Pipeline ETL & Logika Logistik
│   └── 03_etl_validation.ipynb                # Tahap 3: Analisis Bisnis & Charting
├── sql/
│   └── analysis_queries.sql                   # Kueri SQL agregasi pendapatan & stok
├── scripts/
│   └── validate_outputs.py                    # Skrip otomatis validasi hasil ETL
├── docs/
│   └── panduan_proyek.md                      # Panduan arsitektur & kamus data
└── output/
    ├── output_farmasi_parquet.zip             # Hasil kompresi data Parquet (Snappy)
    └── charts/
        ├── 01_grafik_pendapatan.png           # KPI 1: Pendapatan Lintas Pulau
        ├── 02_grafik_risiko_kedaluwarsa.png   # KPI 2: Risiko Penalti Logistik Laut
        ├── 03_grafik_tren_musiman.png         # KPI 3: Gelombang Musim Hujan
        └── 04_grafik_distribusi_layanan.png   # KPI 4: Proporsi Klinis (IGD, Rawat Inap)
```

---

## 📊 Ringkasan Hasil & Insight Bisnis

Dari analisis 100.000 data transaksi rantai pasok farmasi, ditemukan 4 wawasan strategis:

* **Dominasi Pendapatan (Efek Pareto):** Kategori Antibiotik dan Obat Saluran Cerna di Jakarta (Pusat) adalah tulang punggung perusahaan. *Rekomendasi:* Terapkan kebijakan *Tiered Inventory* (mengamankan 70% anggaran pengadaan untuk *Safety Stock* kategori ini di Jakarta).
* **Peringatan Logistik (Jayapura):** Tingkat obat berisiko tinggi (*expired* < 3 bulan) sangat ekstrem di Papua akibat *lead time* kargo laut yang mencapai 45 hari. *Rekomendasi:* Beralih ke *Air Freight* (Kargo Udara) khusus untuk obat sirup ke Indonesia Timur.
* **Tren Musiman:** Perputaran stok membentuk lonjakan tajam di Q1 dan Q4 bertepatan dengan siklus musim hujan. *Rekomendasi:* Terapkan *Dynamic Replenishment* (genjot pasokan di Agustus-September, rem di pertengahan tahun).
* **Profiling Konsumsi Klinis (OPD vs ER):** Rawat Jalan (OPD) menyerap 60% obat secara massal, sedangkan IGD (ER) menyerap porsi kecil namun butuh perputaran cepat. *Rekomendasi:* Bangun *Satellite Pharmacy* di zona IGD untuk memangkas *bottleneck* antrean perawat.

---

## 🚀 Cara Menjalankan Aplikasi

Jalankan *notebook* secara berurutan di VS Code atau Google Colab:
1. Buka `notebooks/01_exploration.ipynb` untuk melihat profil data awal.
2. Buka `notebooks/02_pyspark_transform.ipynb` untuk memproses *engine* PySpark (menghasilkan Parquet).
3. Buka `notebooks/03_etl_validation.ipynb` untuk mencetak 4 grafik Business Intelligence.
4. Jalankan `python scripts/validate_outputs.py` di terminal untuk memverifikasi kelengkapan file keluaran.

---

## 🔒 Kebijakan Keamanan & Tata Kelola Data

Untuk menjaga standar kepatuhan medis dan performa repositori:
* **Keamanan PII:** Seluruh dataset 100.000 baris yang disertakan adalah **100% data sintetis**. Tidak ada *Personally Identifiable Information* (PII) atau rekam medis pasien asli yang terekspos.
* **Kompresi Big Data:** Format keluaran utama menggunakan **Apache Parquet** dengan kompresi Snappy untuk efisiensi penyimpanan arsitektur data.

---

## 👥 Tim Pengembang (Kelompok)

Proyek Enterprise Big Data Analytics ini dikembangkan secara kolaboratif oleh:
1. **Priyanto** (NIM: 15240017) - *Peran: Data Engineering, ETL Pipeline, dan Konfigurasi GitHub*
2. **[Nama Teman Anda]** (NIM: [NIM Teman]) - *Peran: Business Analytics, Visualisasi, dan Data Profiling*
# 💊 Big Data Pharmacy Supply Chain Analytics

Platform analitik dan pipeline ETL data rantai pasok perusahaan farmasi berskala nasional (100.000 baris data sintetis) yang menggabungkan eksplorasi data, pemrosesan terdistribusi dengan **Apache Spark (PySpark)**, penyimpanan data lake terkompresi **Parquet (Snappy)**, serta visualisasi bisnis tingkat lanjut dengan **Matplotlib & Seaborn**.

Proyek ini dirancang agar dapat dijalankan secara fleksibel: baik di komputer lokal (VS Code / Python) maupun di cloud via Google Colab.

---

## 🎯 Tujuan & Cakupan Proyek

1. **Data Profiling & Quality Gates:**
   Memvalidasi integritas 100.000 transaksi medis, memeriksa *missing value*, dan menyimulasikan pembobotan distribusi berdasarkan kategori produk dan wilayah.
2. **Transformasi PySpark:** 
   Pemrosesan data skala besar untuk menghitung umur simpan (kedaluwarsa) obat dan menerapkan penalti logistik kargo laut lintas pulau.
3. **Visualisasi Business Intelligence:** 
   Menerjemahkan data mentah menjadi 4 metrik KPI utama yang mudah dipahami oleh pemangku kepentingan (Direksi / Manajemen Rumah Sakit).

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

# 2. Instalasi pustaka pendukung (Pandas, PySpark, Matplotlib, Seaborn)
pip install pyspark pandas matplotlib seaborn
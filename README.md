# NBA Player Performance Analytics

**Nama** : Muhammad Miftah Zakki  
**NIM** : 2441036  
**Program Studi** : Sistem Informasi  
**Perguruan Tinggi** : STMIK AMIK Bandung  
**Mata Kuliah** : Machine Learning  

---

## Pendahuluan

NBA Player Performance Analytics merupakan sebuah aplikasi berbasis web yang dikembangkan untuk menganalisis dan memprediksi performa pemain NBA, khususnya dalam hal jumlah poin per pertandingan (Points Per Game / PPG). Sistem ini memanfaatkan metode Machine Learning untuk mempelajari hubungan antara statistik dasar pemain dan performa mencetak poin.

Proyek ini dibuat sebagai bagian dari tugas mata kuliah Machine Learning dengan tujuan menerapkan konsep pembelajaran mesin ke dalam sebuah sistem nyata yang dapat diakses melalui web. Aplikasi ini mengintegrasikan antarmuka pengguna (frontend), backend berbasis API, serta model Machine Learning sebagai inti dari proses prediksi.

Dengan adanya sistem ini, pengguna dapat memahami bagaimana data statistik sederhana dapat digunakan untuk menghasilkan prediksi performa pemain basket profesional secara kuantitatif.

---

## Tujuan dan Manfaat Sistem

Tujuan utama dari pengembangan NBA Player Performance Analytics adalah membangun aplikasi berbasis web yang mampu memprediksi performa pemain NBA menggunakan pendekatan Machine Learning. Sistem ini bertujuan untuk menunjukkan alur lengkap penerapan Machine Learning mulai dari pengolahan data hingga integrasi model ke dalam aplikasi web.

Manfaat dari sistem ini antara lain memberikan gambaran mengenai pengaruh menit bermain, usia pemain, dan jumlah pertandingan terhadap performa mencetak poin. Dari sisi akademik, proyek ini menjadi sarana pembelajaran penerapan Machine Learning secara praktis dan terstruktur.

---

## Fitur Sistem

Aplikasi NBA Player Performance Analytics menyediakan fitur input data statistik pemain melalui antarmuka web yang interaktif. Pengguna dapat memasukkan nilai menit bermain, usia pemain, dan jumlah pertandingan yang dimainkan menggunakan slider yang mudah digunakan.

Sistem akan memproses data tersebut dan menampilkan hasil prediksi berupa jumlah poin per pertandingan. Selain nilai prediksi, sistem juga menampilkan visualisasi grafik untuk membantu pengguna memahami nilai input yang diberikan.

Aplikasi ini dilengkapi dengan penjelasan sederhana mengenai faktor-faktor yang memengaruhi hasil prediksi sehingga pengguna dapat memahami hasil yang ditampilkan. Efek visual dan musik latar juga ditambahkan untuk meningkatkan pengalaman pengguna.

---

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam sistem ini adalah Linear Regression. Algoritma ini dipilih karena memiliki konsep yang sederhana, mudah dipahami, serta sesuai untuk kebutuhan pembelajaran Machine Learning dasar.

Linear Regression bekerja dengan memodelkan hubungan linear antara beberapa variabel input dengan satu variabel output. Dalam sistem ini, algoritma digunakan untuk memprediksi jumlah poin per pertandingan berdasarkan statistik pemain yang dimasukkan.

---

## Dataset dan Variabel

Dataset yang digunakan dalam proyek ini berasal dari file `players_master.csv` yang berisi data statistik pemain NBA. Dataset tersebut disesuaikan agar dapat digunakan dalam proses pelatihan model regresi.

Variabel input yang digunakan meliputi BASE_MIN (menit bermain), BASE_AGE (usia pemain), dan BASE_GP (jumlah pertandingan yang dimainkan). Variabel output atau target dari model adalah BASE_PTS yang merepresentasikan jumlah poin per pertandingan.

Dataset ini digunakan untuk melatih model agar mampu mempelajari pola hubungan antara statistik pemain dan performa mencetak poin.

---

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library Pandas dan Scikit-learn. Dataset dibagi menjadi data latih dan data uji menggunakan metode train-test split.

Data latih digunakan untuk melatih model Linear Regression agar dapat mempelajari hubungan antar variabel. Setelah proses pelatihan selesai, model diuji menggunakan data uji untuk memastikan kestabilan hasil prediksi.

Model yang telah dilatih kemudian disimpan dalam bentuk file agar dapat digunakan kembali pada backend tanpa perlu melakukan pelatihan ulang.

---

## Evaluasi Model

Evaluasi model dilakukan dengan membandingkan hasil prediksi model terhadap data uji yang telah disiapkan. Proses ini bertujuan untuk memastikan bahwa model mampu menghasilkan prediksi yang logis dan konsisten.

Evaluasi dilakukan secara sederhana karena fokus utama proyek ini adalah implementasi konsep Machine Learning dan integrasinya ke dalam aplikasi web.

---

## Arsitektur Sistem

Arsitektur sistem NBA Player Performance Analytics terdiri dari tiga komponen utama, yaitu frontend, backend, dan model Machine Learning. Frontend berfungsi sebagai antarmuka pengguna untuk memasukkan data dan menampilkan hasil prediksi.

Backend berperan sebagai penghubung antara frontend dan model Machine Learning melalui REST API. Model Machine Learning digunakan sebagai inti sistem untuk melakukan proses prediksi performa pemain.

---

## Backend dengan FastAPI

Backend aplikasi dibangun menggunakan framework FastAPI. FastAPI dipilih karena ringan, cepat, dan mudah digunakan dalam pengembangan REST API.

Backend bertugas menerima data input dari frontend, memproses data menggunakan model Machine Learning yang telah dilatih, dan mengembalikan hasil prediksi ke frontend dalam format JSON.

---

## Frontend Aplikasi

Frontend aplikasi dikembangkan menggunakan HTML, Tailwind CSS, dan JavaScript. Antarmuka dirancang dengan tampilan modern dan interaktif agar mudah digunakan oleh pengguna.

Hasil prediksi ditampilkan secara real-time disertai grafik visualisasi untuk membantu pengguna memahami data input dan hasil prediksi.

---

## Alur Penggunaan Aplikasi

Pengguna membuka halaman web aplikasi dan memasukkan data statistik pemain melalui slider yang tersedia. Setelah data diatur, pengguna menekan tombol prediksi untuk memulai proses perhitungan.

Data yang dimasukkan dikirim ke backend melalui API untuk diproses oleh model Machine Learning. Backend kemudian mengembalikan hasil prediksi yang selanjutnya ditampilkan pada halaman web.

---

## Cara Menjalankan Aplikasi

Aplikasi dapat dijalankan secara lokal dengan menjalankan server backend menggunakan FastAPI. Setelah backend aktif, frontend dapat dibuka melalui browser dan dihubungkan ke endpoint API yang tersedia.

Dengan konfigurasi tersebut, aplikasi siap digunakan untuk melakukan prediksi performa pemain NBA.

---

## Keterbatasan Sistem

Sistem ini masih memiliki beberapa keterbatasan, seperti jumlah variabel input yang masih terbatas dan penggunaan metode Machine Learning yang sederhana. Selain itu, hasil prediksi belum sepenuhnya mencerminkan performa pemain secara nyata.

Oleh karena itu, hasil prediksi dari sistem ini tidak dimaksudkan sebagai analisis resmi, melainkan sebagai media pembelajaran.

---

## Pengembangan Sistem ke Depan

Pengembangan selanjutnya dapat dilakukan dengan menambahkan variabel statistik lanjutan serta dataset yang lebih besar. Metode Machine Learning yang lebih kompleks juga dapat digunakan untuk meningkatkan kualitas prediksi.

---

## Kesimpulan

NBA Player Performance Analytics merupakan aplikasi berbasis web yang berhasil mengimplementasikan konsep Machine Learning untuk memprediksi performa pemain NBA. Sistem ini menunjukkan alur lengkap penerapan Machine Learning mulai dari pengolahan data hingga integrasi ke dalam aplikasi web.

Proyek ini diharapkan dapat menjadi sarana pembelajaran dan dasar pengembangan sistem analitik olahraga berbasis Machine Learning di masa mendatang.

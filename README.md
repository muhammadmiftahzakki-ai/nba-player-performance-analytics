# NBA Player Performance Analytics

**Nama** : Muhammad Miftah Zakki  
**NIM** : 2441036  
**Program Studi** : Sistem Informasi  
**Perguruan Tinggi** : STMIK AMIK Bandung  
**Mata Kuliah** : Machine Learning  

---

## Pendahuluan

NBA Player Performance Analytics merupakan sebuah aplikasi berbasis web yang dikembangkan untuk menganalisis dan memprediksi performa pemain NBA, khususnya dalam hal jumlah poin per pertandingan (Points Per Game / PPG). Sistem ini memanfaatkan pendekatan Machine Learning untuk mempelajari hubungan antara statistik dasar pemain dan performa mencetak poin.

Aplikasi ini dibuat sebagai bagian dari tugas mata kuliah Machine Learning dengan tujuan menerapkan konsep pembelajaran mesin ke dalam sistem nyata yang terintegrasi antara frontend, backend, dan model prediksi. Dengan adanya aplikasi ini, pengguna dapat memahami bagaimana data statistik sederhana dapat digunakan untuk menghasilkan prediksi performa pemain basket profesional.

Selain sebagai tugas akademik, sistem ini juga dirancang agar mudah dipahami oleh pengguna umum melalui tampilan antarmuka yang interaktif, visualisasi grafik, serta penjelasan sederhana mengenai hasil prediksi yang dihasilkan.

---

## Tujuan dan Manfaat Sistem

Tujuan utama dari pengembangan sistem ini adalah membangun aplikasi prediksi performa pemain NBA menggunakan metode Machine Learning yang sederhana namun efektif. Sistem ini bertujuan untuk menunjukkan bagaimana proses pengolahan data, pelatihan model, hingga integrasi model ke dalam aplikasi web dapat dilakukan secara utuh.

Manfaat dari sistem ini antara lain membantu pengguna dalam memahami faktor-faktor yang memengaruhi performa pemain NBA, seperti menit bermain, usia pemain, dan jumlah pertandingan yang dimainkan. Dari sisi akademik, proyek ini menjadi sarana pembelajaran implementasi Machine Learning dalam pengembangan aplikasi berbasis web secara end-to-end.

---

## Fitur Sistem

Aplikasi NBA Player Performance Analytics memiliki beberapa fitur utama yang mendukung proses prediksi dan analisis performa pemain. Pengguna dapat memasukkan data statistik pemain melalui antarmuka web yang interaktif. Sistem kemudian memproses data tersebut dan menampilkan hasil prediksi poin per pertandingan secara real-time.

Selain menampilkan nilai prediksi, aplikasi ini juga menyediakan visualisasi grafik untuk membantu pengguna memahami nilai input yang diberikan. Penjelasan singkat mengenai pengaruh masing-masing variabel terhadap hasil prediksi juga ditampilkan agar sistem bersifat lebih transparan dan mudah dipahami.

Fitur tambahan berupa musik latar dan animasi visual disertakan untuk meningkatkan pengalaman pengguna tanpa mengganggu fungsi utama sistem.

---

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam sistem ini adalah Linear Regression. Algoritma ini dipilih karena memiliki konsep yang sederhana, mudah diinterpretasikan, dan sesuai untuk kebutuhan pembelajaran. Linear Regression bekerja dengan memodelkan hubungan linear antara beberapa variabel input dengan satu variabel output.

Dalam konteks sistem ini, Linear Regression digunakan untuk memprediksi jumlah poin per pertandingan berdasarkan variabel menit bermain, usia pemain, dan jumlah pertandingan yang dimainkan. Setiap variabel memiliki kontribusi tertentu terhadap hasil prediksi yang dihasilkan oleh model.

---

## Dataset dan Variabel

Dataset yang digunakan dalam proyek ini berasal dari file `players_master.csv` yang berisi data statistik pemain NBA. Dataset tersebut mencakup beberapa variabel numerik yang relevan dengan performa pemain dalam mencetak poin.

Variabel input yang digunakan dalam sistem ini meliputi BASE_MIN (menit bermain), BASE_AGE (usia pemain), dan BASE_GP (jumlah pertandingan yang dimainkan). Variabel output atau target dari model adalah BASE_PTS yang merepresentasikan jumlah poin per pertandingan.

Dataset dipilih dan disesuaikan agar sesuai dengan kebutuhan model regresi serta mencerminkan kondisi performa pemain secara realistis.

---

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library Pandas dan Scikit-learn. Dataset yang digunakan dibagi menjadi data latih dan data uji menggunakan metode train-test split dengan perbandingan tertentu.

Data latih digunakan untuk melatih model Linear Regression agar mampu mempelajari pola hubungan antar variabel. Setelah proses pelatihan selesai, model diuji menggunakan data uji untuk memastikan bahwa model dapat menghasilkan prediksi yang stabil.

Model yang telah dilatih kemudian disimpan dalam bentuk file `.pkl` menggunakan Joblib agar dapat digunakan kembali pada backend tanpa perlu melakukan proses training ulang.

---

## Evaluasi Model

Evaluasi model dilakukan dengan memisahkan dataset menjadi data latih dan data uji. Proses ini bertujuan untuk mengukur kemampuan model dalam melakukan prediksi terhadap data yang belum pernah dilihat sebelumnya.

Model Linear Regression dievaluasi menggunakan pendekatan regresi dengan memperhatikan selisih antara nilai prediksi dan nilai aktual. Evaluasi ini membantu memastikan bahwa model memiliki performa yang cukup baik untuk digunakan dalam sistem prediksi sederhana.

Meskipun evaluasi dilakukan secara dasar, proses ini sudah cukup untuk kebutuhan pembelajaran dan implementasi awal Machine Learning dalam aplikasi web.

---

## Arsitektur Sistem

Arsitektur sistem terdiri dari tiga komponen utama, yaitu frontend, backend, dan model Machine Learning. Frontend berfungsi sebagai antarmuka pengguna untuk memasukkan data dan menampilkan hasil prediksi. Backend berperan sebagai penghubung antara frontend dan model Machine Learning.

Frontend dan backend berkomunikasi melalui REST API menggunakan format data JSON. Backend memuat model Machine Learning yang telah dilatih dan bertanggung jawab dalam memproses permintaan prediksi dari frontend.

Arsitektur ini dirancang secara modular sehingga setiap komponen dapat dikembangkan atau diperbaiki secara terpisah.

---

## Backend dengan FastAPI

Backend aplikasi dibangun menggunakan framework FastAPI. FastAPI dipilih karena memiliki performa yang cepat, ringan, serta mendukung pembuatan REST API dengan struktur yang jelas.

Backend bertugas menerima data input dari frontend, memproses data tersebut menggunakan model Machine Learning, dan mengembalikan hasil prediksi dalam format JSON. Selain itu, middleware CORS ditambahkan agar backend dapat diakses oleh frontend berbasis web.

---

## Frontend Aplikasi

Frontend aplikasi dikembangkan menggunakan HTML, Tailwind CSS, dan JavaScript. Antarmuka dirancang dengan gaya visual modern dan interaktif agar mudah digunakan oleh pengguna.

Pengguna dapat mengatur nilai input melalui slider, kemudian menjalankan proses prediksi dengan menekan tombol yang tersedia. Hasil prediksi ditampilkan secara langsung disertai grafik visualisasi dan penjelasan sederhana.

---

## Alur Penggunaan Aplikasi

Alur penggunaan aplikasi dimulai ketika pengguna membuka halaman web aplikasi. Pengguna kemudian memasukkan data statistik pemain seperti menit bermain, usia pemain, dan jumlah pertandingan yang dimainkan.

Setelah data dimasukkan, pengguna menekan tombol prediksi. Data tersebut dikirim ke backend melalui API untuk diproses oleh model Machine Learning. Backend kemudian mengembalikan hasil prediksi ke frontend untuk ditampilkan kepada pengguna.

Seluruh proses berlangsung secara real-time tanpa perlu memuat ulang halaman.

---

## Cara Menjalankan Aplikasi

Untuk menjalankan aplikasi ini secara lokal, pengguna perlu memastikan bahwa Python dan library yang dibutuhkan telah terinstal. Backend dapat dijalankan menggunakan perintah uvicorn untuk menjalankan server FastAPI.

Setelah backend aktif, frontend dapat dibuka melalui browser dengan memastikan alamat API sudah sesuai. Aplikasi siap digunakan untuk melakukan prediksi performa pemain NBA.

---

## Keterbatasan Sistem

Sistem ini masih memiliki beberapa keterbatasan, antara lain jumlah variabel input yang digunakan masih terbatas dan model yang digunakan masih sederhana. Selain itu, hasil prediksi belum sepenuhnya mencerminkan performa pemain secara nyata karena keterbatasan dataset.

Oleh karena itu, hasil prediksi dari sistem ini tidak dimaksudkan sebagai analisis resmi, melainkan sebagai media pembelajaran dan simulasi penerapan Machine Learning.

---

## Pengembangan Sistem ke Depan

Pengembangan selanjutnya dapat dilakukan dengan menambahkan variabel input lain seperti akurasi tembakan, posisi pemain, dan statistik lanjutan lainnya. Dataset yang lebih besar dan lebih beragam juga dapat digunakan untuk meningkatkan akurasi model.

Selain itu, algoritma Machine Learning yang lebih kompleks dapat dicoba untuk menghasilkan prediksi yang lebih optimal.

---

## Kesimpulan

NBA Player Performance Analytics merupakan aplikasi berbasis web yang berhasil mengimplementasikan konsep Machine Learning dalam memprediksi performa pemain NBA. Sistem ini menunjukkan bagaimana proses pengolahan data, pelatihan model, hingga integrasi ke dalam aplikasi web dapat dilakukan secara terstruktur.

Proyek ini diharapkan dapat menjadi sarana pembelajaran dan dasar pengembangan sistem Machine Learning yang lebih kompleks di masa depan.

---

## Referensi

Scikit-learn Documentation.  
James, G., Witten, D., Hastie, T., Tibshirani, R. (2013). *An Introduction to Statistical Learning*. Springer.

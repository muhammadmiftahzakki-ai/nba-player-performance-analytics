# NBA Player Performance Analytics

**Nama** : Muhammad Miftah Zakki  
**NIM** : 2441036  
**Program Studi** : Sistem Informasi  
**Perguruan Tinggi** : STMIK AMIK Bandung  
**Mata Kuliah** : Machine Learning  

---

## Pendahuluan

NBA Player Performance Analytics merupakan sebuah aplikasi berbasis web yang dikembangkan untuk menganalisis dan memprediksi performa pemain NBA, khususnya dalam hal jumlah poin per pertandingan atau Points Per Game (PPG). Sistem ini memanfaatkan pendekatan Machine Learning untuk mengolah data statistik pemain dan menghasilkan prediksi yang dapat digunakan sebagai gambaran performa pemain di lapangan.

Aplikasi ini dikembangkan sebagai bagian dari tugas mata kuliah Machine Learning dengan tujuan untuk menerapkan teori pembelajaran mesin ke dalam sebuah sistem nyata yang terintegrasi. Melalui proyek ini, mahasiswa diharapkan dapat memahami alur kerja Machine Learning secara utuh, mulai dari pengolahan data, pelatihan model, hingga implementasi model ke dalam aplikasi web.

Selain sebagai tugas akademik, sistem ini juga dirancang dengan antarmuka yang interaktif dan mudah digunakan. Pengguna dapat memasukkan data statistik pemain dan secara langsung memperoleh hasil prediksi, sehingga konsep Machine Learning dapat dipahami tidak hanya secara teoritis tetapi juga secara praktis.

---

## Tujuan dan Manfaat Sistem

Tujuan utama dari pengembangan sistem ini adalah untuk membangun sebuah aplikasi prediksi performa pemain NBA berbasis web menggunakan metode Machine Learning. Sistem ini bertujuan untuk menunjukkan bagaimana data statistik sederhana dapat digunakan untuk menghasilkan prediksi performa pemain secara kuantitatif.

Manfaat dari sistem ini antara lain memberikan pemahaman praktis mengenai penerapan Machine Learning, khususnya regresi linear, dalam dunia nyata. Selain itu, proyek ini juga melatih kemampuan integrasi antara frontend, backend, dan model Machine Learning dalam satu sistem yang utuh dan terstruktur.

---

## Fitur Utama Sistem

Sistem NBA Player Performance Analytics memiliki beberapa fitur utama yang mendukung proses prediksi dan analisis performa pemain NBA. Fitur-fitur tersebut dirancang agar pengguna dapat berinteraksi langsung dengan sistem dan memahami hasil prediksi dengan mudah.

Fitur pertama adalah **input data statistik pemain secara interaktif**, di mana pengguna dapat memasukkan nilai Minutes Played, Player Age, dan Games Played melalui slider yang tersedia pada halaman web. Penggunaan slider ini memudahkan pengguna dalam melakukan simulasi berbagai kondisi performa pemain.

Fitur kedua adalah **prediksi Points Per Game (PPG)** menggunakan model Machine Learning. Setelah data dimasukkan, sistem akan memproses data tersebut melalui backend dan menghasilkan nilai prediksi PPG secara real-time tanpa perlu memuat ulang halaman.

Fitur berikutnya adalah **visualisasi data dan hasil prediksi**, yang ditampilkan dalam bentuk grafik menggunakan Chart.js. Visualisasi ini membantu pengguna memahami kontribusi masing-masing variabel terhadap performa pemain secara lebih intuitif.

Selain itu, sistem juga menyediakan fitur **Explainable AI**, yaitu penjelasan sederhana mengenai pengaruh setiap variabel input terhadap hasil prediksi. Fitur ini bertujuan agar pengguna tidak hanya melihat hasil prediksi, tetapi juga memahami alasan di balik prediksi tersebut.

Sistem juga dilengkapi dengan **desain antarmuka modern dan responsif**, menggunakan Tailwind CSS, sehingga dapat diakses dengan nyaman melalui berbagai ukuran layar. Ditambahkan pula efek visual dan audio latar untuk meningkatkan pengalaman pengguna saat menggunakan aplikasi.

---

## Metode Machine Learning

Metode Machine Learning yang digunakan dalam proyek ini adalah Linear Regression. Metode ini dipilih karena memiliki konsep yang sederhana, mudah dipahami, dan sangat cocok untuk tujuan pembelajaran. Linear Regression memodelkan hubungan linear antara variabel input dan output, sehingga hasil prediksi dapat dijelaskan secara matematis.

Linear Regression juga memiliki kompleksitas yang rendah dan relatif stabil ketika digunakan pada dataset berukuran kecil hingga menengah. Setiap variabel input memiliki bobot tertentu yang memengaruhi hasil prediksi Points Per Game, sehingga metode ini mudah diinterpretasikan dan dianalisis.

---

## Dataset dan Variabel

Dataset yang digunakan dalam sistem ini berasal dari data statistik pemain NBA yang disimpan dalam file CSV. Dataset tersebut mencakup beberapa variabel utama yang digunakan sebagai input dalam proses prediksi.

Variabel input yang digunakan meliputi Minutes Played, Player Age, dan Games Played. Ketiga variabel ini dipilih karena memiliki pengaruh yang cukup signifikan terhadap performa mencetak poin seorang pemain NBA. Variabel output dari dataset ini adalah Points Per Game (PPG), yang digunakan sebagai target prediksi model.

---

## Proses Training Model

Proses pelatihan model dilakukan menggunakan bahasa pemrograman Python dengan bantuan library Pandas dan Scikit-learn. Dataset dibagi menjadi data latih dan data uji untuk memastikan model dapat mempelajari pola hubungan antar variabel dengan baik.

Model Linear Regression kemudian dilatih menggunakan data latih, dan dilakukan pengujian menggunakan data uji untuk melihat performa prediksi. Setelah model selesai dilatih, model disimpan dalam bentuk file menggunakan joblib agar dapat digunakan kembali oleh backend tanpa perlu melakukan pelatihan ulang.

---

## Arsitektur Sistem

Arsitektur sistem NBA Player Performance Analytics terdiri dari tiga komponen utama, yaitu frontend, backend, dan model Machine Learning. Frontend berfungsi sebagai antarmuka pengguna, backend sebagai penghubung dan pemroses data, serta model Machine Learning sebagai inti dari sistem prediksi.

Frontend dan backend berkomunikasi melalui REST API. Data input dari pengguna dikirim dalam format JSON ke backend, kemudian diproses oleh model Machine Learning, dan hasil prediksi dikirim kembali ke frontend untuk ditampilkan kepada pengguna.

---

## Backend dengan FastAPI

Backend aplikasi dikembangkan menggunakan framework FastAPI. FastAPI dipilih karena memiliki performa yang tinggi, ringan, dan sangat cocok untuk pengembangan REST API. Backend bertanggung jawab untuk menerima data input, memvalidasi data, menjalankan proses prediksi, dan mengembalikan hasil prediksi ke frontend.

---

## Frontend Aplikasi

Frontend aplikasi dibangun menggunakan HTML, Tailwind CSS, dan JavaScript. Antarmuka dirancang agar interaktif dan mudah digunakan, dengan penggunaan slider, animasi, grafik, serta audio latar untuk meningkatkan pengalaman pengguna.

Pengguna dapat langsung melihat hasil prediksi Points Per Game setelah menekan tombol prediksi, tanpa perlu memuat ulang halaman.

---

## Evaluasi dan Keterbatasan Sistem

Sistem ini masih memiliki beberapa keterbatasan, antara lain jumlah variabel input yang masih terbatas serta penggunaan metode Machine Learning yang relatif sederhana. Dataset yang digunakan juga belum mencakup seluruh faktor yang memengaruhi performa pemain NBA.

Oleh karena itu, hasil prediksi yang dihasilkan oleh sistem ini tidak dimaksudkan sebagai prediksi resmi, melainkan sebagai simulasi dan sarana pembelajaran.

---

## Pengembangan Sistem ke Depan

Pengembangan lebih lanjut dapat dilakukan dengan menambahkan variabel input lain, menggunakan dataset yang lebih besar dan lebih kompleks, serta menerapkan algoritma Machine Learning yang lebih canggih. Selain itu, sistem juga dapat dikembangkan dengan fitur perbandingan performa antar pemain atau prediksi untuk beberapa pertandingan sekaligus.

---

## Kesimpulan

NBA Player Performance Analytics merupakan aplikasi berbasis web yang berhasil mengimplementasikan konsep Machine Learning dalam memprediksi performa pemain NBA. Sistem ini menunjukkan bagaimana model Machine Learning dapat diintegrasikan dengan frontend dan backend secara utuh.

Proyek ini diharapkan dapat menjadi media pembelajaran yang bermanfaat dalam memahami penerapan Machine Learning dalam pengembangan aplikasi berbasis web.

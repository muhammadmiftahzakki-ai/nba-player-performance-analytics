# NBA Player Performance Analytics  
Machine Learning–Based Points Per Game Prediction System

## Identitas Pengembang

Nama : Mayta Nohan Griselda  
NIM : 2441044  
Program Studi : Sistem Informasi  
Perguruan Tinggi : STMIK AMIK Bandung  
Mata Kuliah : Machine Learning  

---

## Deskripsi Proyek

NBA Player Performance Analytics merupakan sebuah aplikasi web interaktif yang dirancang untuk memprediksi **Points Per Game (PPG)** pemain NBA menggunakan pendekatan **Machine Learning**, khususnya algoritma **Linear Regression**.  
Aplikasi ini menggabungkan tampilan frontend yang modern dan dinamis dengan backend berbasis FastAPI, serta model machine learning yang telah dilatih menggunakan data statistik pemain NBA.

Tujuan utama dari proyek ini adalah untuk menunjukkan bagaimana data performa pemain seperti **Minutes Played**, **Age**, dan **Games Played** dapat digunakan untuk memprediksi rata-rata poin yang dicetak oleh seorang pemain. Selain itu, proyek ini juga menekankan aspek **Explainable AI**, sehingga hasil prediksi tidak hanya ditampilkan dalam bentuk angka, tetapi juga disertai penjelasan logis yang mudah dipahami.

---

## Latar Belakang

Dalam dunia olahraga profesional seperti NBA, analisis performa pemain sangat penting untuk pengambilan keputusan, baik oleh pelatih, manajemen tim, maupun analis data. Dengan meningkatnya ketersediaan data statistik pemain, pendekatan berbasis Machine Learning menjadi solusi yang efektif untuk memprediksi performa di masa depan.

Linear Regression dipilih dalam proyek ini karena memiliki hubungan yang cukup linear antara variabel input dan output, serta mudah diinterpretasikan. Model ini cocok digunakan untuk dataset berukuran menengah dan mampu memberikan hasil prediksi yang stabil tanpa kompleksitas berlebih.

---

## Arsitektur Sistem

Sistem ini dibangun menggunakan tiga komponen utama, yaitu frontend, backend, dan model machine learning.

Frontend berfungsi sebagai antarmuka pengguna yang memungkinkan pengguna memasukkan data performa pemain dan melihat hasil prediksi secara visual. Backend berperan sebagai penghubung antara frontend dan model machine learning, sedangkan model machine learning bertugas melakukan proses prediksi berdasarkan data yang diterima.

Alur kerja sistem dimulai ketika pengguna mengatur nilai input pada slider di frontend, kemudian data tersebut dikirim ke backend menggunakan metode HTTP POST. Backend memproses data tersebut menggunakan model regresi linear dan mengembalikan hasil prediksi ke frontend untuk ditampilkan.

---

## Frontend (HTML, Tailwind CSS, JavaScript)

Frontend aplikasi ini dibangun menggunakan HTML, Tailwind CSS, dan JavaScript, dengan tampilan visual yang modern dan interaktif.  
Penggunaan Tailwind CSS memudahkan pembuatan desain responsif dan konsisten, sementara JavaScript digunakan untuk mengelola interaksi pengguna, animasi, serta komunikasi dengan backend.

Fitur utama pada frontend meliputi input slider untuk Minutes Played, Age, dan Games Played, tombol untuk menjalankan prediksi, tampilan hasil prediksi poin, grafik visual menggunakan Chart.js, serta efek animasi dan background dinamis yang meningkatkan pengalaman pengguna.  
Selain itu, terdapat fitur musik latar yang dapat diaktifkan atau dinonaktifkan oleh pengguna.

---

## Backend (FastAPI)

Backend pada proyek ini dibangun menggunakan framework **FastAPI** karena memiliki performa tinggi, mudah digunakan, dan sangat cocok untuk pengembangan REST API.  
FastAPI menerima data input dari frontend dalam format JSON, kemudian memproses data tersebut menggunakan model machine learning yang telah dilatih sebelumnya.

Untuk menghindari masalah komunikasi antar domain, backend juga dikonfigurasi menggunakan **CORS Middleware**, sehingga frontend dapat mengakses API tanpa kendala. Endpoint utama pada backend adalah `/predict`, yang berfungsi untuk menerima data pemain dan mengembalikan hasil prediksi Points Per Game.

---

## Model Machine Learning

Model yang digunakan dalam proyek ini adalah **Linear Regression** dari library scikit-learn.  
Dataset yang digunakan berisi data statistik pemain NBA, dengan variabel input berupa **BASE_MIN**, **BASE_AGE**, dan **BASE_GP**, serta variabel target **BASE_PTS**.

Data dibagi menjadi data latih dan data uji menggunakan metode train-test split. Setelah model dilatih, model disimpan menggunakan joblib agar dapat digunakan kembali oleh backend tanpa perlu melatih ulang setiap kali aplikasi dijalankan.

Pemilihan Linear Regression didasarkan pada kemudahan interpretasi, stabilitas model, serta kesesuaian dengan karakteristik data yang memiliki hubungan linier antar variabel.

---

## Alur Prediksi

Proses prediksi dimulai ketika pengguna menekan tombol "RUN PREDICTION" pada halaman web.  
Data input yang dipilih pengguna dikirim ke backend melalui API FastAPI. Backend kemudian memformat data tersebut dan mengirimkannya ke model machine learning untuk diprediksi.

Hasil prediksi berupa nilai Points Per Game dikembalikan ke frontend dan ditampilkan secara visual, lengkap dengan grafik dan penjelasan sederhana mengenai pengaruh masing-masing variabel terhadap hasil prediksi.

---

## Explainable AI

Untuk meningkatkan pemahaman pengguna, aplikasi ini menyediakan penjelasan sederhana mengenai hasil prediksi.  
Penjelasan ini menjelaskan bahwa semakin tinggi Minutes Played, semakin besar peluang pemain mencetak poin, Games Played membantu menstabilkan performa, dan Age mempengaruhi stamina serta efisiensi pemain.

Pendekatan ini bertujuan agar hasil Machine Learning tidak hanya menjadi angka semata, tetapi juga dapat dipahami secara logis oleh pengguna.

---

## Cara Menjalankan Aplikasi

Langkah pertama adalah menjalankan proses training model untuk menghasilkan file model regresi. Setelah model berhasil disimpan, backend FastAPI dijalankan menggunakan perintah uvicorn.  
Selanjutnya, frontend dapat dibuka melalui browser untuk mulai menggunakan aplikasi.

Pastikan backend berjalan terlebih dahulu sebelum menjalankan frontend agar proses prediksi dapat berjalan dengan baik.

---

## Kesimpulan

NBA Player Performance Analytics berhasil mengimplementasikan konsep Machine Learning ke dalam aplikasi web interaktif.  
Dengan menggabungkan Linear Regression, FastAPI, dan frontend modern, aplikasi ini mampu memberikan prediksi performa pemain NBA secara sederhana, cepat, dan mudah dipahami.

Proyek ini diharapkan dapat menjadi contoh penerapan Machine Learning dalam bidang olahraga, serta menjadi dasar untuk pengembangan sistem analitik yang lebih kompleks di masa depan.

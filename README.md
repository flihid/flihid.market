**flihh\_market**

Nama : Mohamad Rafli Hidayat  
NPM : 2306245831  
Kelas : A  
Link Web : 

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**   
1) Membuat Repository Lokal, Repository GitHub, dan Proyek Django Baru.  
   Pertama-tama, untuk memulai proyek Django, saya membuat sebuah repository lokal di komputer. Kemudian, hubungkan repository lokal dengan repository GitHub menggunakan perintah 'git remote add origin https://github.com/flihid/flihh.market.git'. Setelah inisialisasi github selesai, tambahkan .gitignore dan requirements.txt pada repositori lokal. Setelah itu, saya inisiasi virtual environment dan menginstall semua dependency yang diperlukan untuk proyek Django baru saya.  
2) Membuat Aplikasi dengan Nama "main".  
   Selanjutnya, saya membuat proyek flihh.market dengan menjalankan 'django-admin startproject flihh\_market .'. Setelah proyek Django berhasil diinisialisasi, langkah berikutnya adalah membuat aplikasi di dalam proyek tersebut. Buat aplikasi baru dengan nama "main" menggunakan perintah 'python manage.py startapp main'.  
3) Melakukan Routing pada Proyek untuk Menjalankan Aplikasi "main".  
   Untuk memastikan aplikasi "main" dapat diakses melalui web, saya mendaftarkan aplikasi tersebut di dalam proyek dengan cara menambahkan aplikasi "main" ke dalam INSTALLED\_APPS di file settings.py proyek utama. Selanjutnya, di file urls.py di dalam folder proyek, lakukan routing ke aplikasi "main" dengan menambahkan rute baru yang mengarah ke urls.py dari aplikasi tersebut, seperti menambahkan "path('', include('main.urls'))".  
4) Membuat Model "Product" pada Aplikasi "main".  
   Setelah routing selesai, buat model yang diinginkan dalam aplikasi "main". Model adalah representasi dari objek di database, dalam hal ini sebuah produk. Di file models.py dalam aplikasi "main", buat model Product dengan atribut wajib name, price, dan description. Setelah model dibuat, jalankan perintah 'python manage.py makemigrations' dan 'python manage.py migrate' untuk memperbarui database dengan model Product.  
5) Membuat Fungsi pada views.py untuk Mengembalikan ke Template HTML.  
   Selanjutnya, buatlah fungsi di views.py yang akan digunakan untuk menampilkan nama aplikasi dan juga nama serta kelas saya. Fungsi ini akan mengambil data dan menampilkan informasi ke dalam template HTML.  
6) Membuat Routing pada urls.py Aplikasi "main".  
   Selanjutnya saya membuat beberapa fungsi pada views, untuk menghandle beberapa pola url yang diterima, sehingga views dapat menentukan template apa yang akan dipakai dan data apa saja yang perlu difetch agar bisa sampai pada user dalam bentuk yang komplit.  
7) Melakukan Deployment ke PWS.  
   Setelah aplikasi selesai, langkah terakhir adalah melakukan deployment ke website pws agar aplikasi bisa diakses oleh orang lain.  
8) Selanjutnya saya membuat README.md pada github saya untuk menjawab beberapa pertanyaan

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![][image1]

1) User melakukan HTTP request yang akan ditangani oleh Django. Di urls.py, pola URL yang diminta akan menentukan fungsi view mana yang harus dijalankan berdasarkan permintaan tersebut.  
2) Setelah view yang sesuai dipanggil, view akan mengambil data yang diperlukan dari database. Data ini diambil dari field yang didefinisikan dalam models.py.  
3) View kemudian menentukan template HTML yang akan digunakan untuk menampilkan data. Setelah template dipilih dan data dimasukkan, Django akan mengirimkan respons kembali ke user dalam bentuk HTML yang sudah dipopulasikan dengan data tersebut.

3. **Jelaskan fungsi git dalam pengembangan perangkat lunak\!**

Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk melacak setiap perubahan yang dilakukan pada kode sumber, memungkinkan pengembang untuk bekerja secara kolaboratif tanpa mengganggu pekerjaan satu sama lain. Dengan Git, pengembang dapat membuat cabang terpisah untuk fitur baru atau perbaikan bug, dan kemudian menggabungkan perubahan tersebut kembali ke cabang utama dengan aman. Ini membantu menjaga integritas kode dan memudahkan pengelolaan proyek, baik secara individu maupun dalam tim.

4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya, Django adalah framework yang populer karena menggunakan model MVT yang jelas, bahasa Python yang mudah dipahami, dan memiliki banyak fitur bawaan. Dokumentasi yang lengkap dan komunitas yang luas juga membuatnya ideal untuk pemula dalam pengembangan perangkat lunak.

5. **Mengapa model pada Django disebut sebagai ORM?**

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara kode Python dan database relasional. Dengan ORM, pengembang dapat mengelola data dalam database menggunakan objek Python tanpa perlu menulis kueri SQL secara langsung. Ini membuat proses pengelolaan data lebih intuitif dan efisien, karena pengembang dapat bekerja dengan data dalam bentuk objek yang lebih mudah dipahami dan dimanipulasi.

[image1]: <data[image/png;base64,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](https://github.com/flihid/flihh.market/blob/main/bagan/bagan.png)>

Nama : Mohamad Rafli Hidayat
NPM : 2306245831
Kelas : A
Link Web : 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
    1. Membuat Repository Lokal, Repository GitHub, dan Proyek Django Baru. Pertama-tama, untuk memulai proyek Django, saya membuat sebuah repository lokal di komputer. Kemudian, hubungkan repository lokal dengan repository GitHub menggunakan perintah 'git remote add origin https://github.com/flihid/flihh.market.git'. Setelah inisialisasi github selesai, tambahkan .gitignore dan requirements.txt pada repositori lokal. Setelah itu, saya inisiasi virtual environment dan menginstall semua dependency yang diperlukan untuk proyek Django baru saya.
    2. Membuat Aplikasi dengan Nama "main". Selanjutnya, saya membuat proyek flihh.market dengan menjalankan 'django-admin startproject flihh_market .'. Setelah proyek Django berhasil diinisialisasi, langkah berikutnya adalah membuat aplikasi di dalam proyek tersebut. Buat aplikasi baru dengan nama "main" menggunakan perintah 'python manage.py startapp main'.
    3. Melakukan Routing pada Proyek untuk Menjalankan Aplikasi "main". Untuk memastikan aplikasi "main" dapat diakses melalui web, saya mendaftarkan aplikasi tersebut di dalam proyek dengan cara menambahkan aplikasi "main" ke dalam INSTALLED_APPS di file settings.py proyek utama. Selanjutnya, di file urls.py di dalam folder proyek, lakukan routing ke aplikasi "main" dengan menambahkan rute baru yang mengarah ke urls.py dari aplikasi tersebut, seperti menambahkan "path('', include('main.urls'))".
    4. Membuat Model "Product" pada Aplikasi "main". Setelah routing selesai, buat model yang diinginkan dalam aplikasi "main". Model adalah representasi dari objek di database, dalam hal ini sebuah produk. Di file models.py dalam aplikasi "main", buat model Product dengan atribut wajib name, price, dan description. Setelah model dibuat, jalankan perintah 'python manage.py makemigrations' dan 'python manage.py migrate' untuk memperbarui database dengan model Product.
    5. Membuat Fungsi pada views.py untuk Mengembalikan ke Template HTML. Selanjutnya, buatlah fungsi di views.py yang akan digunakan untuk menampilkan nama aplikasi dan juga nama serta kelas saya. Fungsi ini akan mengambil data dan menampilkan informasi ke dalam template HTML.
    6. Membuat Routing pada urls.py Aplikasi "main". Selanjutnya saya membuat beberapa fungsi pada views, untuk menghandle beberapa pola url yang diterima, sehingga views dapat menentukan template apa yang akan dipakai dan data apa saja yang perlu difetch agar bisa sampai pada user dalam bentuk yang komplit.
    7. Melakukan Deployment ke PWS. Setelah aplikasi selesai, langkah terakhir adalah melakukan deployment ke website pws agar aplikasi bisa diakses oleh orang lain.
    8. Selanjutnya saya membuat README.md pada github saya untuk menjawab beberapa pertanyaan

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
        HTTP Request            Give request data
        ------------>           ------------>
Browser                  View                 Model
        <------------    |  ^   <------------
  ^     HTTP Response    |  |    Edit data
                         V  | Give HTML
  |                     Template
User
    1. User melakukan HTTP request yang akan ditangani oleh Django. Di urls.py, pola URL yang diminta akan menentukan fungsi view mana yang harus dijalankan berdasarkan permintaan tersebut.
    2. Setelah view yang sesuai dipanggil, view akan mengambil data yang diperlukan dari database. Data ini diambil dari field yang didefinisikan dalam models.py.
    3. View kemudian menentukan template HTML yang akan digunakan untuk menampilkan data. Setelah template dipilih dan data dimasukkan, Django akan mengirimkan respons kembali ke user dalam bentuk HTML yang sudah dipopulasikan dengan data tersebut.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk melacak setiap perubahan yang dilakukan pada kode sumber, memungkinkan pengembang untuk bekerja secara kolaboratif tanpa mengganggu pekerjaan satu sama lain. Dengan Git, pengembang dapat membuat cabang terpisah untuk fitur baru atau perbaikan bug, dan kemudian menggabungkan perubahan tersebut kembali ke cabang utama dengan aman. Ini membantu menjaga integritas kode dan memudahkan pengelolaan proyek, baik secara individu maupun dalam tim.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django adalah framework yang populer karena menggunakan model MVT yang jelas, bahasa Python yang mudah dipahami, dan memiliki banyak fitur bawaan. Dokumentasi yang lengkap dan komunitas yang luas juga membuatnya ideal untuk pemula dalam pengembangan perangkat lunak.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara kode Python dan database relasional. Dengan ORM, pengembang dapat mengelola data dalam database menggunakan objek Python tanpa perlu menulis kueri SQL secara langsung. Ini membuat proses pengelolaan data lebih intuitif dan efisien, karena pengembang dapat bekerja dengan data dalam bentuk objek yang lebih mudah dipahami dan dimanipulasi.
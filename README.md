**Flihid\_Market**

Nama : Mohamad Rafli Hidayat  
NPM : 2306245831  
Kelas : A  
Link Web : http://mohamad-rafli-flihidmarket.pbp.cs.ui.ac.id/ 

<details>
  <summary><b>Tugas 2</b></summary>

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**   
1) Membuat Repository Lokal, Repository GitHub, dan Proyek Django Baru.  
   Pertama-tama, untuk memulai proyek Django, saya membuat sebuah repository lokal di komputer. Kemudian, hubungkan repository lokal dengan repository GitHub menggunakan perintah 'git remote add origin https://github.com/flihid/flihid.market.git'. Setelah inisialisasi github selesai, tambahkan '.gitignore' dan 'requirements.txt' pada repositori lokal. Setelah itu, saya inisiasi virtual environment dan menginstall semua dependency yang diperlukan untuk proyek Django baru saya.  
2) Membuat Aplikasi dengan Nama "main".  
   Selanjutnya, saya membuat proyek flihid.market dengan menjalankan 'django-admin startproject flihid\_market .'. Setelah proyek Django berhasil diinisialisasi, langkah berikutnya adalah membuat aplikasi di dalam proyek tersebut. Buat aplikasi baru dengan nama "main" menggunakan perintah 'python manage.py startapp main'.  
3) Melakukan Routing pada Proyek untuk Menjalankan Aplikasi "main".  
   Untuk memastikan aplikasi "main" dapat diakses melalui web, saya mendaftarkan aplikasi tersebut di dalam proyek dengan cara menambahkan aplikasi "main" ke dalam "INSTALLED\_APPS" di file 'settings.py' proyek utama. Selanjutnya, di file 'urls.py di dalam folder proyek, lakukan routing ke aplikasi "main" dengan menambahkan rute baru yang mengarah ke 'urls.py' dari aplikasi tersebut, seperti menambahkan "path('', include('main.urls'))".  
4) Membuat Model "Product" pada Aplikasi "main".  
   Setelah routing selesai, buat model yang diinginkan dalam aplikasi "main". Model adalah representasi dari objek di *database*, dalam hal ini sebuah produk. Di file 'models.py' dalam aplikasi "main", buat model Product dengan atribut wajib *name*, *price*, dan *description*. Setelah model dibuat, jalankan perintah 'python manage.py makemigrations' dan 'python manage.py migrate' untuk memperbarui *database* dengan model Product.  
5) Membuat Fungsi pada 'views.py' untuk Mengembalikan ke Template HTML.  
   Selanjutnya, buatlah fungsi di 'views.py' yang akan digunakan untuk menampilkan nama aplikasi dan juga nama serta kelas saya. Fungsi ini akan mengambil data dan menampilkan informasi ke dalam template HTML.  
6) Membuat Routing pada 'urls.py' Aplikasi "main".  
   Selanjutnya saya membuat beberapa fungsi pada views, untuk menghandle beberapa pola url yang diterima, sehingga views dapat menentukan template apa yang akan dipakai dan data apa saja yang perlu difetch agar bisa sampai pada user dalam bentuk yang komplit.  
7) Melakukan Deployment ke PWS.  
   Setelah aplikasi selesai, langkah terakhir adalah melakukan deployment ke website pws agar aplikasi bisa diakses oleh orang lain.  
8) Selanjutnya saya membuat 'README.md' pada github saya untuk menjawab beberapa pertanyaan

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 'urls.py', 'views.py', 'models.py', dan berkas 'html.'**

![bagan](https://github.com/user-attachments/assets/ebedf5f5-df79-4fdf-8621-edbad2f9f5da)

1) User melakukan HTTP request yang akan ditangani oleh Django. Di 'urls.py', pola URL yang diminta akan menentukan fungsi view mana yang harus dijalankan berdasarkan permintaan tersebut.  
2) Setelah view yang sesuai dipanggil, view akan mengambil data yang diperlukan dari *database*. Data ini diambil dari field yang didefinisikan dalam 'models.py'.  
3) View kemudian menentukan template HTML yang akan digunakan untuk menampilkan data. Setelah template dipilih dan data dimasukkan, Django akan mengirimkan respons kembali ke user dalam bentuk HTML yang sudah dipopulasikan dengan data tersebut.

3. **Jelaskan fungsi git dalam pengembangan perangkat lunak\!**

Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk melacak setiap perubahan yang dilakukan pada kode sumber, memungkinkan pengembang untuk bekerja secara kolaboratif tanpa mengganggu pekerjaan satu sama lain. Dengan Git, pengembang dapat membuat cabang terpisah untuk fitur baru atau perbaikan bug, dan kemudian menggabungkan perubahan tersebut kembali ke cabang utama dengan aman. Ini membantu menjaga integritas kode dan memudahkan pengelolaan proyek, baik secara individu maupun dalam tim.

4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya, Django adalah framework yang populer karena menggunakan model MVT yang jelas, bahasa Python yang mudah dipahami, dan memiliki banyak fitur bawaan. Dokumentasi yang lengkap dan komunitas yang luas juga membuatnya ideal untuk pemula dalam pengembangan perangkat lunak.

5. **Mengapa model pada Django disebut sebagai ORM?**

Model pada Django disebut sebagai ORM (*Object-Relational Mapping*) karena berfungsi sebagai penghubung antara kode Python dan *database* relasional. Dengan ORM, pengembang dapat mengelola data dalam *database* menggunakan objek Python tanpa perlu menulis *query* SQL secara langsung. Ini membuat proses pengelolaan data lebih intuitif dan efisien, karena pengembang dapat bekerja dengan data dalam bentuk objek yang lebih mudah dipahami dan dimanipulasi.

</details>

<details>
  <summary><b>Tugas 3</b></summary>

6. **Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?**

*Data delivery* sangat penting dalam pengimplementasian sebuah platform karena memastikan bahwa informasi atau data yang dibutuhkan oleh pengguna dapat diakses dengan cepat, akurat, dan terpercaya. Dalam sebuah platform, banyak elemen yang terhubung, seperti server, *database*, dan aplikasi klien, yang memerlukan transfer data secara efisien. Jika data tidak dikirimkan dengan baik, pengguna dapat mengalami latensi, kehilangan data, atau bahkan kesalahan sistem. Data delivery juga berperan dalam menjaga integritas dan keamanan data, memastikan informasi yang dikirimkan tidak rusak atau terpapar ancaman keamanan selama proses transfer.

7. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Menurut saya, JSON lebih baik dibandingkan XML dalam banyak situasi karena lebih sederhana dan efisien. JSON memiliki sintaks yang lebih ringan, mudah dibaca oleh manusia dan diproses oleh mesin, terutama dalam aplikasi web. JSON menggunakan struktur yang lebih sederhana dengan format *key-value*, sedangkan XML menggunakan elemen dan tag yang bisa lebih panjang dan kompleks. JSON lebih populer karena lebih mudah digunakan dalam bahasa pemrograman modern, terutama JavaScript. Selain itu, ukuran file JSON lebih kecil dibandingkan XML, yang membuatnya lebih cepat diunduh dan lebih efisien dalam transmisi data.

8. **Jelaskan fungsi dari method 'is\_valid()' pada form Django dan mengapa kita membutuhkan method tersebut?**

Method \`is\_valid()\` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah ditentukan di dalam form tersebut. Method ini memeriksa apakah semua field dalam form telah diisi dengan benar dan sesuai tipe data yang diharapkan. Jika data valid, method ini mengembalikan \`True\`; jika tidak valid, mengembalikan \`False\`. Method ini diperlukan untuk memastikan bahwa data yang dikirimkan oleh pengguna aman dan sesuai dengan ekspektasi sebelum diproses lebih lanjut, seperti menyimpan ke *database* atau melakukan operasi lainnya.

9. **Mengapa kita membutuhkan 'csrf\_token' saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan 'csrf\_token' pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

CSRF (*Cross-Site Request Forgery*) adalah serangan di mana penyerang membuat pengguna yang terautentikasi di suatu situs melakukan aksi yang tidak diinginkan tanpa sepengetahuannya. Django menggunakan ‘csrf\_token’ untuk melindungi aplikasi dari serangan ini. Token tersebut adalah nilai unik yang disisipkan ke dalam form dan diverifikasi pada saat pengiriman.

Jika kita tidak menambahkan ‘csrf\_token’ pada form, aplikasi Django menjadi rentan terhadap serangan CSRF. Penyerang dapat memanipulasi pengguna untuk mengirimkan permintaan berbahaya ke server, seperti mengubah data atau melakukan tindakan penting tanpa izin. Dengan kata lain, tanpa ‘csrf\_token’, penyerang dapat "menyamar" sebagai pengguna untuk melakukan aksi yang tidak diinginkan.

Penyerang dapat memanfaatkan celah ini dengan mengirimkan tautan atau skrip berbahaya kepada pengguna yang sudah login. Ketika pengguna tersebut tanpa sengaja mengakses tautan tersebut, permintaan berbahaya dapat dikirim ke server dengan kredensial mereka, karena server menganggap permintaan itu sah.

10. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).**  
1) Membuat Input Form untuk Menambahkan Objek Model  
   Saya menggunakan form Django untuk membuat form input ini. Form akan mengambil data dari user, memvalidasi data tersebut, dan kemudian menyimpannya ke dalam *database* jika valid. Dengan form ini, saya dapat menerima masukan dari pengguna untuk objek model yang ingin mereka tambahkan.  
2) Menambahkan Fungsi Views untuk Menyajikan Objek dalam Format XML dan JSON.  
   Setelah objek ditambahkan ke *database*, saya membuat beberapa views untuk menampilkan objek tersebut dalam format XML dan JSON. Views ini menggunakan serializer untuk mengonversi data objek model ke format yang sesuai. Saya juga menyajikan data berdasarkan ID dalam format XML atau JSON. Ini akan berguna untuk memastikan fleksibilitas dalam penyajian data, baik untuk keseluruhan objek koleksi atau objek individual.  
3) Routing URL untuk Setiap View yang Telah Dibuat.  
   Setiap view yang saya buat memerlukan URL pattern yang sesuai dalam file ‘urls.py’. Saya membuat rute URL untuk masing-masing view tersebut, sehingga aplikasi dapat menavigasi dan menyajikan data dalam format yang diminta ketika URL yang tepat diakses.   
4) Selanjutnya saya mendokumentasi dalam file ‘README.md’ untuk menjawab beberapa pertanyaan tentang diperlukannya data delivery dalam pengimplementasian sebuah platform, JSON lebih populer dibandingkan XML, fungsi ‘is\_valid()’ pada form Django, pentingnya CSRF token.  
5) Pengujian dengan Postman dan Dokumentasi di ‘README.md’.  
   Saya mengakses keempat URL yang telah dibuat (untuk XML dan JSON) menggunakan Postman, yaitu alat yang memungkinkan mengirim permintaan HTTP dan melihat respons dari server. Setelah itu, saya mengambil *screenshot* dari hasil akses URL tersebut dan menambahkannya ke ‘README.md’ sebagai dokumentasi.  
6) Terakhir saya melakukan ‘add’, ‘commit’, dan ‘push’ ke GitHub untuk mengunggah kode dan dokumentasi proyek ke repositori.

**Hasil akses URL pada Postman**

1. Format XML
![xml](https://github.com/user-attachments/assets/1e912408-03e3-4426-b91e-36c5ef2ed198)

2. Format JSON
![json](https://github.com/user-attachments/assets/c5e90035-287b-48eb-b028-d8de665f725f)

3. Format  XML *by ID*
![xmlbyid](https://github.com/user-attachments/assets/104249e0-3afc-4f8e-8e47-c980c15d920d)

4. Format  JSON *by ID*
![jsonbyid](https://github.com/user-attachments/assets/49d3f9fd-a451-407b-87f7-4dcd006ace00)

</details>

<details>
  <summary><b>Tugas 4</b></summary>

11. **Apa perbedaan antara ‘HttpResponseRedirect()’ dan ‘redirect()’**

‘HttpResponseRedirect()’ adalah kelas yang secara langsung mengembalikan respons HTTP untuk mengarahkan pengguna ke URL tertentu secara manual, dan biasanya membutuhkan URL sebagai argumen. ‘redirect()’, adalah *shortcut* fungsi yang lebih fleksibel dan lebih mudah digunakan. Fungsi ini dapat menerima berbagai jenis argumen, seperti URL, nama view, atau objek model, dan secara otomatis menangani konversi argumen tersebut menjadi URL yang valid. 

12. **Jelaskan cara kerja penghubungan model Product dengan User\!**

Penghubungan model Product dengan User dalam Django dilakukan melalui ForeignKey, yang memungkinkan setiap entri produk terhubung dengan satu pengguna tertentu. Dalam model Product, kita mendefinisikan atribut user sebagai ForeignKey yang merujuk ke model User. Dengan demikian, setiap kali kita membuat entri produk baru, kita bisa mengaitkannya dengan pengguna yang membuat entri tersebut. Saat kita ingin mengakses informasi pengguna dari entri produk, kita dapat dengan mudah melakukannya melalui relasi ini. Ini memungkinkan pengelolaan data yang lebih terstruktur dan memudahkan dalam melakukan query berdasarkan pengguna yang bersangkutan. Contohnya, jika saya memiliki model Product dan User, di model Product saya akan menambahkan field seperti ‘user \= models.ForeignKey(User, on\_delete=models.CASCADE)’. Ini memastikan bahwa setiap entri produk terkait dengan satu pengguna dan jika pengguna dihapus, entri produk mereka juga akan dihapus.

13. **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication dan authorization adalah dua konsep berbeda dalam keamanan sistem. Authentication adalah proses memverifikasi identitas pengguna, seperti saat pengguna memasukkan nama pengguna dan kata sandi saat login. Authorization adalah proses menentukan hak akses atau izin yang dimiliki pengguna setelah identitas mereka dikonfirmasi. Saat pengguna login, sistem melakukan authentication untuk memastikan bahwa pengguna adalah siapa yang mereka klaim. Setelah itu, authorization digunakan untuk menentukan apa yang boleh atau tidak boleh dilakukan oleh pengguna dalam sistem, berdasarkan peran atau izin yang diberikan.

Di Django, authentication dilakukan melalui sistem login yang memeriksa kredensial pengguna terhadap data yang tersimpan di basis data. Django menyediakan model ‘User’ dan form login untuk memudahkan proses ini. Authorization di Django dikelola dengan menggunakan sistem permission dan grup, serta decorator seperti ‘@login\_required’ dan ‘@permission\_required’ untuk mengontrol akses ke tampilan atau fitur tertentu berdasarkan hak akses pengguna.

14. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django mengingat pengguna yang telah login dengan menggunakan sistem *session*. Ketika pengguna berhasil login, Django membuat sebuah *session* untuk mereka, yang disimpan di sisi server dan diidentifikasi dengan ID *session* yang disimpan dalam cookies di browser pengguna. Setiap kali pengguna melakukan permintaan, cookies ini dikirim ke server, memungkinkan Django untuk mengidentifikasi pengguna dan mengautentikasi mereka tanpa perlu login ulang.

Cookies juga memiliki kegunaan lain, seperti menyimpan preferensi pengguna, menjaga pesanan produk dalam aplikasi e-commerce, dan melacak aktivitas pengguna untuk analisis dan personalisasi konten. Namun, tidak semua cookies aman digunakan. Beberapa cookies dapat menjadi target serangan, seperti cookies *session* yang tidak dienkripsi, yang bisa disalahgunakan oleh pihak ketiga. 

15. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
1) Mengimplementasikan fungsi registrasi, login, dan logout
   Saya mulai dengan membuat fungsi registrasi, login, dan logout untuk memfasilitasi akses pengguna. Proses registrasi mencakup validasi data yang dimasukkan pengguna, dan jika berhasil, data pengguna disimpan dalam database. Untuk login, saya menerapkan autentikasi yang memastikan pengguna yang memasukkan kredensial yang benar dapat mengakses aplikasi. Fungsi logout, di mana *session* pengguna diakhiri, dan mereka diarahkan kembali ke halaman login.
2) Membuat akun pengguna dan dummy data 
   Setelah autentikasi, saya membuat dua akun pengguna dengan menggunakan model yang telah dibuat sebelumnya. Saya mengisi masing-masing akun dengan tiga dummy data untuk keperluan pengujian dan demonstrasi. 
3) Menghubungkan model Product dengan User
   Selanjutnya, saya menghubungkan model Product dengan User. Ini memungkinkan saya untuk mengaitkan produk yang dibuat atau dimiliki dengan pengguna tertentu. Penghubungan ini dilakukan dengan menambahkan ForeignKey di model Product yang merujuk ke model User, sehingga setiap produk dapat diidentifikasi berdasarkan pemiliknya.
4) Menampilkan detail informasi pengguna
   Setelah pengguna berhasil login, saya menampilkan detail informasi pengguna, seperti username, pada halaman utama aplikasi. Selain itu, saya menerapkan cookies untuk menyimpan informasi tentang waktu login terakhir pengguna. Dengan cara ini, pengguna dapat melihat informasi penting saat menggunakan aplikasi.
5) Selanjutnya saya mendokumentasi dalam file ‘README.md’ untuk menjawab beberapa pertanyaan tentang perbedaan antara HttpResponseRedirect() dan redirect(), cara kerja penghubungan model Product dengan User, perbedaan antara authentication dan authorization, dan cara Django mengingat pengguna yang telah login.  
6) Terakhir saya melakukan ‘add’, ‘commit’, dan ‘push’ ke GitHub untuk mengunggah kode dan dokumentasi proyek ke repositori.

</details>
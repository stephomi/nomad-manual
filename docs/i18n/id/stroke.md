# ![](/icons/pencil.webp) Stroke    

---
![](/images/stroke_overview.webp) 

## Gambaran Umum 

Anda dapat menyesuaikan perilaku goresan (stroke) untuk sebagian besar kuas alat.
Pengaturannya mirip dengan yang ada di aplikasi lukis 2D, namun beberapa opsi khusus untuk pemahatan dan 3D.

Opsi-opsi ini dibagi ke dalam 5 sub-menu:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Mengontrol bagaimana stroke diterapkan ke model                    |
| Alpha    | ![](/icons/alpha.webp)      | Bagaimana tekstur skala abu-abu digunakan untuk cap kuas           |
| Falloff  | ![](/icons/falloff.webp)    | Mengontrol bagaimana kekuatan kuas berubah dari tengah ke tepi     |
| Filter   | ![](/icons/filter.webp)     | Bagaimana kuas dipengaruhi oleh geometri model                     |
| Pressure | ![](/icons/pressure.webp)   | Mengontrol respons tekanan stylus                                  |

::: tip
Tidak semua opsi stroke berlaku untuk semua alat. Opsi stroke yang tidak digunakan oleh alat saat ini akan dinonaktifkan atau disembunyikan. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Share radius

Jika diaktifkan, semua alat akan menggunakan radius yang sama, default-nya adalah setiap alat memiliki radius masing-masing.

#### Size

* Screen - radius diatur dalam satuan layar. Jika Anda membuat radius selebar 100 piksel, radius akan tetap 100 piksel terlepas dari apakah Anda melakukan zoom in atau zoom out.
* Constant (3d) - radius diatur dalam satuan 3D. Misalnya jika Anda membuat sebuah bola dan membuat radius sama dengan ukuran bola, radius akan tetap sama dengan ukuran bola saat Anda zoom in dan out.


### Stroke

![](/images/stroke_strokemode.webp)

Stroke dapat berperilaku dalam beberapa mode:

### ![](/icons/stroke_dot.webp) Dot
Seret seperti goresan cat biasa. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
Alpha kuas akan diputar mengikuti arah stroke, berguna untuk membuat jahitan kain. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
Mencap stroke kuas dengan **_tinggi_** tetap. Seret akan mengatur skala dan rotasi.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Mencap stroke kuas dengan **_radius_** tetap. Seret akan mengatur tinggi dan rotasi.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Alat `Move` dan `Drag` memiliki 3 opsi sendiri:

### ![](/icons/snake.webp) Drag

Akan terus memperbarui apa yang ada di dalam radius kuas selama stroke. Stroke cepat akan meninggalkan permukaan di belakang, sementara stroke lambat akan menahan material, membentuk bentuk yang lebih panjang. Ini adalah mode default untuk alat `Drag`. Dengan `Dynamic Topology` ini dapat digunakan untuk membuat ekstrusi seperti ular. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Akan memilih apa yang ada di dalam radius kuas saat kuas dimulai, dan mempertahankan seleksi tersebut. Ini berguna untuk operasi pemindahan yang lebih presisi, karena Anda dapat dengan hati-hati menyesuaikan jarak perpindahan dan tidak secara tidak sengaja memindahkan lebih banyak dari yang awalnya dipilih. Ini adalah mode default untuk alat `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Radius yang ditentukan pengguna diabaikan, dan diatur secara dinamis berdasarkan seberapa jauh stroke diseret dari titik awal. Jarak kecil = radius kecil, jarak lebih besar = radius lebih besar. Gunakan slider intensitas untuk mengontrol bentuk falloff. Berguna untuk memblokir bentuk organik yang kenyal.
![](/videos/stroke_lockradius_drag.mp4) 



### Adjust spacing intensity
![](/images/stroke_space_smooth.webp)

Stroke dengan jarak rendah (kurang dari 50%) dapat menumpuk dengan cepat, menghasilkan stroke yang lebih intens dibandingkan nilai jarak yang lebih tinggi. Toggle ini akan mengompensasi hal tersebut, sehingga stroke akan memiliki intensitas yang kurang lebih sama terlepas dari jaraknya.

### Stroke spacing
Seberapa jauh jarak antar penerapan setiap cap kuas selama operasi seret. Nilai di bawah 100% akan saling tumpang tindih, memberikan tampilan stroke yang kontinu. Nilai di atas 100% akan mulai meninggalkan celah, berguna untuk memahat detail seperti jahitan atau resleting.

### Lazy rope stabilizer
Stroke akan tertinggal di belakang posisi pointer dengan jarak tertentu. Ini dapat digunakan untuk menggambar garis yang halus.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing
Merata-ratakan beberapa posisi pointer untuk mendapatkan stroke yang lebih halus.
Dengan nilai tinggi, stroke akan tertinggal di belakang pointer tetapi akhirnya akan menyusul.
Ini berguna untuk menggambar garis yang halus.

### Snap radius
Menjepret awal stroke ke ujung stroke sebelumnya. Radius menentukan seberapa jauh mencari ujung stroke sebelumnya. Ini dapat berguna saat menggambar garis panjang yang kontinu, sambil sering berhenti sejenak.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Secara default stroke hanya akan memengaruhi permukaan model di dalam radius kuas. Saat silhouette diaktifkan, stroke akan diproyeksikan menembus seluruh model. Ini sangat berguna saat melakukan blocking awal model, atau untuk bentuk yang mengharuskan sisi-sisinya tetap tegak lurus.

Arah proyeksi dapat diatur secara eksplisit, metode default 'Closest' akan mendeteksi sudut terbaik relatif terhadap tampilan. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

Intensitas, translasi, rotasi, dan skala stroke masing-masing dapat diacak. Ini dapat digunakan untuk membuat berbagai efek, misalnya randomize dengan alat paint dapat membuat warna belang-belang, atau randomize dengan alat crease dapat digunakan untuk membuat detail kulit.

![](/videos/stroke_randomize.mp4) 

### Stroke Offset

Menerapkan offset konstan pada stroke. Ini berguna untuk layar kecil di mana jari Anda akan menutupi stroke. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

`Alpha` adalah tekstur yang akan memodulasi perilaku kuas Anda.
Ini adalah gambar skala abu-abu, di mana piksel hitam berarti tidak ada deformasi dan piksel putih berarti deformasi penuh.

Klik pada gambar alpha untuk mengubahnya.

Klik pada pratinjau material untuk memuat alpha dari preset material. Anda juga dapat menyimpan preset material di sini, dan memilih untuk menyematkan tekstur dengan alat.

::: tip
Tekstur tidak pernah diubah ukurannya, jadi tekstur besar dapat memperlambat performa.
:::

### Invert pixels
Ini akan membalik nilai gambar, sehingga piksel hitam menjadi putih, dan piksel putih menjadi hitam.

::: tip

Alpha bawaan yang disertakan dengan Nomad tidak dapat dibalik.

:::

### Scaling

Ukuran kuas di Nomad adalah lingkaran dengan radius yang ditentukan pengguna. Tekstur sering kali berbentuk persegi atau persegi panjang, parameter `Scaling` memungkinkan Anda memutuskan bagaimana tekstur harus pas di dalam lingkaran. Untuk tekstur persegi, nilai 0.7 akan pas di dalam lingkaran. Nilai 1 akan memperbesar tekstur sehingga lingkaran berada di dalamnya, memotong tepi.

![](/images/alpha_scaling.webp) 

Mengaktifkan `Scaling - Y` akan memungkinkan Anda meregangkan alpha secara vertikal.

![](/images/alpha_scaling_y.webp) 

### Rotation

Tekstur alpha akan diputar mengikuti arah stroke. Anda dapat menambahkan offset rotasi, dan jika ikon kunci diaktifkan, tekstur akan tetap terkunci pada rotasi ini relatif terhadap layar.

### Tiling
![](/images/stroke_tiling.webp) 

Seberapa sering tekstur diulang di dalam profil kuas. Mode tiling memungkinkan Anda membatasi ke satu tekstur di dalam stroke, atau tekstur berulang, atau cermin di mana setiap tekstur kedua dibalik untuk membuat pola atau membantu membuat tekstur tanpa sambungan.

![](/videos/alpha_tiling.mp4) 



### Mid value

Secara default piksel hitam berarti tidak ada deformasi, dan piksel putih berarti deformasi positif penuh, jadi misalnya, kuas clay dengan tekstur alpha batu hanya akan menarik permukaan keluar di mana alpha tidak hitam.

Jika Anda ingin kuas mendorong permukaan ke dalam, atau sekaligus mendorong ke dalam DAN menarik keluar, Anda dapat mengubah nilai tengah. Jadi jika Anda mengatur nilai ke 0.5, abu-abu tengah di alpha tidak akan melakukan apa-apa, nilai hitam akan mendorong ke dalam, putih akan menarik keluar.




## Falloff

![](/images/falloff_menu.webp) 

Ini mirip dengan [Alpha](#alpha), kecuali Anda mengendalikan intensitas dengan satu kurva. Ini digabungkan dengan alpha sehingga Anda dapat menggunakan tekstur untuk detail, dan falloff untuk mengontrol pemudaran tepi dan intensitas di tengah alat.

Saat kurva berada di atas, ini berarti deformasi penuh, saat berada di bawah kuas tidak berpengaruh.

Anda dapat menganggap kurva sebagai penampang melintang ujung kuas. Bagian bawah memberikan pratinjau seperti apa 'cap' tunggal kuas pada permukaan model, dan jika ada tekstur alpha untuk kuas, ini juga akan ditampilkan untuk mempratinjau bagaimana falloff dan alpha akan berinteraksi.

### Preset
Dengan ini dipilih, mengklik grafik kurva akan menampilkan menu preset. Kurva membulat akan memberikan hasil yang lebih lembut, kurva bersudut akan memberikan hasil yang lebih tajam. Tombol `Sub` di toolbar kiri pada dasarnya akan membalik falloff, sehingga bagian atas kurva akan mendorong ke dalam permukaan alih-alih menarik keluar, atau sebaliknya.

### Catmull-Rom
Jika dipilih, pengguna dapat menggambar kurva falloff sendiri. Editor kurva bekerja sama seperti kurva di bagian lain Nomad:

* Klik pada kurva untuk membuat titik baru
* Seret titik untuk memindahkannya
* Klik pada titik untuk beralih antara tajam dan halus
* Seret titik ke titik tetangga untuk menghapusnya

### B-spline
Jika dipilih, pengguna dapat menggambar kurva falloff sendiri. Editor bekerja sama seperti Catmull-Rom, tetapi titik kurva memengaruhi kurva alih-alih berada langsung di atas kurva, yang dapat membantu membuat bentuk kurva yang lebih halus.

Editor kurva memiliki 3 tombol:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Memperluas editor kurva                      |
| Reset    | ![](/icons/reset.webp)     | Mengembalikan kurva ke keadaan default       |
| Symmetry | ![](/icons/symmetric.webp) | Menampilkan kurva sebagai 'ujung kuas' simetris |


### Influence

* Sphere (3d) - Pengaruh dihitung dengan mengambil jarak dari vertex ke pusat kuas.
* Circle (2d) - Vertex terlebih dahulu diproyeksikan ke bidang area, sebelum diambil jaraknya ke pusat kuas. Ini mirip dengan cara alpha di-sample. 
* Cylinder - Pengaruh diproyeksikan melalui area sebagai silinder, digunakan oleh mode Silhouette di bawah.

### Silhouette
Secara default stroke hanya akan memengaruhi permukaan model di dalam radius kuas. Saat silhouette diaktifkan, stroke akan diproyeksikan menembus seluruh model. Ini sangat berguna saat melakukan blocking awal model, atau untuk bentuk yang mengharuskan sisi-sisinya tetap tegak lurus.



## Filter

![](/images/filter_menu.webp) 

### Accumulate stroke
Mengaktifkan tanpa batas seberapa banyak materi dapat ditambah/dihapus per stroke. Misalnya alat `Clay` memiliki ini diaktifkan, sehingga material dapat terus menumpuk, sementara alat `Brush` memiliki ini dinonaktifkan, sehingga stroke akan berhenti menambah material jika Anda terus menggerakkan stroke yang sama di area mesh yang sama. 

### Front-facing vertex only
Opsi ini akan mengabaikan vertex yang menghadap ke belakang.
Ini dapat berguna jika Anda ingin mengecat bagian dari geometri tipis tanpa memengaruhi sisi lainnya.
Ini juga berfungsi untuk pemahatan tetapi Anda mungkin mengalami beberapa artefak.

### Allow dynamic topology
Opsi ini hanya tersedia jika mesh Anda berada dalam mode [Dynamic Topology](topology.md#dynamic-topology). Anda dapat menonaktifkan atau mengaktifkan dynamic topology per alat.

### Connected topology
Mengaktifkan hanya pemahatan pada vertex yang terhubung ke permukaan yang Anda sentuh dengan alat. Misalnya saat digunakan dengan alat `Move`, ini akan memungkinkan Anda memindahkan satu bagian meskipun bersilangan dengan bagian lain.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Opsi-opsi ini akan menghentikan alat memengaruhi bagian mesh Anda dalam berbagai kondisi. 

Opsi 'Auto' berarti jika Anda memiliki hide, atau mask, atau facegroup yang terlihat di menu [Shading](shading), mereka akan dilindungi, tetapi jika dimatikan di menu tersebut, perlindungan dinonaktifkan.

* `All` - Toggle untuk mengatur apakah filter proteksi bersifat global, atau per alat.
* `Hide` - Jika bagian mesh disembunyikan dengan alat hide, atur apakah bagian tersebut harus dilindungi.
* `Mask` - Jika bagian mesh dimask, atur apakah bagian tersebut harus dilindungi.
* `Facegroup` - Mengatur apakah Anda hanya dapat menggunakan alat di dalam facegroup pertama yang disentuh.


### Keep sharp edges
Mengecualikan titik yang normalnya terlalu berbeda dari normal permukaan.

Ini akan mengubah bagaimana bidang area dihitung (Area sampling).

Opsi ini dapat berguna untuk alat berbasis flatten, atau jika Anda ingin mewarnai permukaan yang sebagian besar datar tanpa meluber.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Beberapa kuas atau opsi stroke memerlukan normal bidang dan posisi bidang terhadap permukaan agar dapat bekerja.

Anda dapat mengontrol bagaimana menghitung bidang rata-rata ini dengan mengatur area sampling sebagai rasio dari radius alat.

Pada 100%, setiap titik di dalam lingkaran seleksi diperhitungkan.

Pada 0%, hanya vertex atau segitiga terdekat yang diperhitungkan. Nilai-nilai ini dapat ditautkan untuk `Normal radius` dan `Position radius`, atau dilepas dan diatur secara independen.


### Depth masking
![](/images/stroke_depthmask.webp)

Mengecualikan titik yang berada di atas atau di bawah jarak tertentu dari bidang yang dihitung (Area sampling).

Ini dapat digunakan untuk mengecat hanya pada area yang berbukit, atau hanya pada area cekungan.

Grafik merepresentasikan penampang permukaan; garis horizontal adalah tempat permukaan berada, lingkaran merepresentasikan radius falloff cat relatif di atas dan di bawah permukaan. `Height offset` adalah persentase di atas atau di bawah permukaan untuk memulai perhitungan masking. `Top area` dan `Bottom area` memungkinkan Anda menskalakan falloff di atas dan di bawah titik offset.

#### Contoh: Mengecat di cekungan
Untuk mengecat hanya area cekungan, atur height offset ke -100%, dan sesuaikan slider top area sehingga menjauh dari garis horizontal. Ini berarti klik pertama mengatur kedalaman 'nol', dan kemudian hanya area di bawah kedalaman ini yang akan terpengaruh.

![](/videos/stroke_depth_cavity.mp4)

#### Contoh: Mengecat di tonjolan
Untuk hanya mengecat di area tinggi, atur height offset ke +90%, sehingga bagian bawah lingkaran memotong garis horizontal sedikit. Saat Anda mengklik di puncak zona 'tinggi', ini akan mengatur kedalaman, sehingga apa pun pada kedalaman itu, plus sedikit di bawahnya, dan apa pun yang lebih tinggi darinya, akan dicat. Cekungan dalam akan dilewati.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Mengontrol bagaimana tekanan stylus/pena memengaruhi kuas.

Secara default `Use global settings` diaktifkan, artinya semua kuas akan berbagi nilai tekanan yang sama.

### Pressure - Radius

Kurva ini mengontrol bagaimana radius kuas dipengaruhi oleh tekanan. Default-nya adalah hubungan linear, jadi jika stylus Anda memiliki respons yang halus, maka perubahan radius juga akan terasa halus. Namun, banyak stylus memiliki respons non-linear, yang dapat Anda kompensasi dengan kurva ini. Misalnya, jika radius terasa tidak mencapai nilai maksimum pada tekanan tinggi, gunakan preset kurva seperti 'out-pow3', dengan lengkungan yang mengarah ke atas, untuk meningkatkan radius lebih awal.

Dialog ini mirip dengan tampilan kurva falloff, Anda dapat menggunakan preset dengan mengetuk jendela kurva, atau menggambar kurva sendiri dengan mode Catmull-Rom dan B-Spline.

Jika Anda menginginkan radius konstan, nonaktifkan bagian ini.

### Pressure - Intensity

Mirip dengan slider radius, tetapi untuk mengontrol intensitas. Jika Anda menginginkan intensitas konstan, nonaktifkan bagian ini.

### Pressure smoothing

Merata-ratakan event tekanan stylus untuk hasil yang lebih halus.

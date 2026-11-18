# ![](/icons/symmetry.webp) Simetri {#symmetry}

Menu ini mengatur bagaimana goresan diulang melintasi bidang cermin, secara radial atau sebagai ubin, serta cara untuk mengembalikan simetri pada objek yang tidak simetris.

![](/images/symmetry_overview.webp) 

## Ikhtisar {#overview}
Anda bisa menggunakan simetri dengan beberapa cara:

* Sebagai cermin, membalik hasil kerja Anda melintasi X (kiri/kanan), Y (atas/bawah), Z (belakang/depan), atau kombinasinya. 
* Simetri radial dapat diatur pada X Y Z dengan sejumlah pengulangan, misalnya untuk memahat bintang laut. 
* Ubin mengulang goresan Anda di seluruh objek, sehingga pahatan menyambung tanpa sambungan yang terlihat.
* Cermin dapat bekerja di sekitar titik asal (disebut mode dunia) atau di sekitar titik tengah objek (disebut mode lokal).
* Pahatan yang awalnya tidak simetris dapat dipaksa menjadi simetris.

Pintasan untuk mengaktifkan/menonaktifkan simetri juga tersedia di panel cepat kiri (*"Sim"*). Tanda kecil 'L/W' menunjukkan apakah Nomad berada dalam mode simetri Lokal atau Dunia. Anda juga bisa menekan lama atau menggeser ke tengah layar untuk memunculkan sebuah menu.

![](/images/symmetry_button.webp) 

Pengaturan simetri disimpan bersama setiap objek, dan judul menu menampilkan nama objek yang sedang Anda sunting.
Alat-alat pahat berbagi status aktif/nonaktif yang sama, sedangkan alat transformasi ([Transformasi](tools.md#transform) dan [Gizmo](tools.md#gizmo)) memiliki statusnya sendiri.

::: tip
Menu simetri terutama untuk mengatur simetri goresan. Anda juga bisa mencerminkan dan mengulang objek melalui [pengulang di menu adegan](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Diaktifkan {#enabled}
Mengaktifkan atau menonaktifkan mode cermin, sama dengan tombol `Sim` di panel cepat kiri. Ikon peringatan mengingatkan Anda saat mode ini mati, dan menu juga memberi tahu Anda jika alat yang sedang dipakai mengabaikan simetri.

## Bidang {#planes}

Aktifkan bidang simetri, dan jumlah pengulangan untuk simetri radial. Perhatikan bahwa Anda tidak harus memilih satu bidang saja: Anda bisa mengaktifkan 1, 2, atau ketiga bidang sekaligus untuk simetri yang kompleks.

Baris `Radial` mengatur jumlah pengulangan simetri radial di sekitar setiap sumbu. Ini juga tidak terbatas pada satu sumbu, dan bahkan bisa digabungkan dengan simetri bidang untuk menghasilkan detail dengan sangat cepat. (Jumlah total pengulangan dibatasi hingga 200)

![](/videos/symmetry_demo.mp4) 

## Ubin {#tile}

Mengulang goresan Anda di sepanjang sebuah sumbu, dengan jarak yang teratur, sehingga pahatan menyambung tanpa sambungan yang terlihat. Berguna untuk pola, batu bata, atau tekstur yang ingin Anda ulang.

Aktifkan ubin untuk setiap sumbu dengan tombol `Ubin`, lalu atur `Jumlah` (berapa banyak pengulangan yang membentang di sepanjang objek) atau `Jarak` (ruang antara dua pengulangan). Ketuk sakelar di sebelah kiri untuk beralih di antara keduanya.

## Metode {#method}
Cermin bisa berupa `Lokal`, yang ikut bergerak bersama objek, atau `Dunia`, yang tidak bergerak. Jika Anda tidak yakin mode mana yang Anda butuhkan, perhatikan indikator bidang cermin dan radial yang ditampilkan di atas objek. Dalam mode lokal, jika Anda memakai alat transformasi (`Gizmo` atau `Transformasi`) dan memindahkan model, indikator cermin juga ikut bergerak. Dalam mode dunia, indikator cermin tetap diam, dan objeknya yang bergeser melewatinya.

## Cerminkan {#mirroring}
![](/images/symmetry_mirroring.webp)

Saat memahat di dekat bidang simetri, beberapa kuas akan menghasilkan simetri yang kurang sempurna. Bagian ini memungkinkan Anda mengembalikan simetri dengan menyalin satu sisi pahatan Anda ke sisi lainnya. 

`Arah` - Dua tombol panah di sebelah judul `Cerminkan` menentukan sisi mana yang akan disalin ke sisi lainnya. Nomad menghitungnya dari viewport Anda saat ini, sehingga sisi tersebut tetap sama di layar dari arah mana pun Anda melihat model.

![](/icons/shield.webp) `Topeng` - Tombol topeng memungkinkan Anda membatasi apa yang akan dicerminkan; menopeng sisi tujuan akan melindungi area itu, sedangkan menopeng sisi sumber akan mencegah area tersebut dicerminkan ke sisi tujuan. 

![](/icons/tool_hide.webp) `Sembunyi` - Saat aktif, area yang disembunyikan di sisi sumber tidak akan dicerminkan ke sisi tujuan. 

`Cerminkan` (jaga topologi) akan mencoba mendeteksi apakah topologi di kedua sisi cermin sama, dan jika ya, cukup memindahkan verteks. Ini adalah kasus yang paling umum. Simetri radial diabaikan. Jika topologinya tidak simetris, Nomad menawarkan untuk memaksakan pencerminan dengan `Potong • Cerminkan`.

Tombol-tombol `Potong` memotong objek di sepanjang bidang simetri. Tombol ini mengubah topologi, jadi lebih destruktif daripada `Cerminkan`. Angka di setiap tombol menunjukkan berapa banyak objek yang Anda dapatkan:

* `Potong` - membuang satu sisi objek.
* `Potong • Cerminkan` - memotong objek, menyalin satu sisi, mencerminkannya ke sisi lain, lalu menyatukan verteks di sepanjang cermin. Terkadang cara ini diperlukan jika model sangat berbeda di kedua sisi cermin.
* `Potong • Pisah` - memotong objek dan menyimpan setiap sisi sebagai objek terpisah.
* `Potong • Cerminkan • Pisah` - seperti `Potong • Cerminkan`, tetapi setiap sisi menjadi objek terpisah.

Jika beberapa objek dipilih, `Cerminkan` dan [Balik objek](#flip-object) diterapkan ke semuanya.

### Balik objek {#flip-object}
![](/images/symmetry_flip.webp)
Menjadikan sisi kiri sebagai sisi kanan, dan sebaliknya, di sepanjang `X`, `Y` atau `Z`. Hasilnya tampak serupa dengan jika Anda memakai menu alat gizmo dan mengatur skala menjadi -1 pada X.

## Atur ulang dan Sunting {#reset-and-edit}

![](/images/symmetry_edit.webp)

Posisi dan orientasi simetri bisa disunting (tetapi tidak disarankan!). Jika diperlukan, `Pusat dunia` (`Pusat objek` dalam mode lokal) dan `Orientasi` akan mengatur ulang posisi dan orientasi simetri ke nilai bawaannya.

Nomad biasanya tahu di mana harus meletakkan bidang simetri. Tidak disarankan untuk mengaturnya secara manual, tetapi tombol `Edit Gizmo` memungkinkan hal ini bagi pengguna tingkat lanjut. Saat tombol ini diklik, sebuah gizmo muncul agar Anda bisa menggeser dan memutar bidang simetri. Jika Anda ingin mengembalikan pusat dan orientasi bawaan, gunakan tombol atur ulang di atas.

`Dari poros` meletakkan bidang simetri pada poros alat [Gizmo](tools.md#gizmo). Opsi ini hanya tersedia saat alat `Gizmo` aktif.

Perilaku opsi-opsi ini berubah tergantung pada ruang (*Lokal/Dunia*) yang sedang Anda gunakan.
Jadi jika hasilnya tidak seperti yang Anda harapkan, pastikan untuk memeriksa apakah Anda berada di ruang yang benar.

::: tip
Menyunting bidang simetri dengan gizmo masih agak eksperimental, kemungkinan besar Anda tidak akan membutuhkannya!
:::

## Opsi tampilan {#show-options}
![](/images/symmetry_show.webp)


`Tampilkan garis` dan `Tampilkan bidang` mengaktifkan atau menonaktifkan overlay viewport yang menunjukkan lokasi simetri. Perhatikan bahwa mematikan opsi-opsi ini baru berlaku setelah menu simetri ditutup.

# ![](/icons/camera.webp) Kamera {#camera}

Menu ini memungkinkan Anda membuat dan mengubah kamera, serta mengatur cara Anda berinteraksi dengan kamera.

![](/images/camera_overview2.webp)

Kamera di Nomad punya beberapa kegunaan:

* Menyiapkan tampilan untuk memahat dari sudut yang presisi
* Dipakai seperti kamera foto untuk membingkai objek Anda
* Sebagai kamera sudut pandang orang pertama untuk menjelajahi adegan Anda
* Sebagai kamera ortografis untuk game isometrik atau render bergaya industri.

## Mengendalikan kamera {#control}

### Rotasi {#rotation}
Anda memutar kamera dengan menyeret *satu* jari di latar belakang.
Jika Anda menyeret jari di atas model, yang dimulai justru operasi pahat.

::: tip Bisakah saya memutar kamera jika latar belakang tidak terjangkau?
Bisa, letakkan *dua* jari di layar - seolah-olah Anda ingin memulai gerakan geser/zoom - lalu angkat *satu* jari.
:::

### Fokus / Atur ulang {#focus}
*Ketuk dua kali* pada model untuk memfokuskan kamera ke titik yang diketuk.
Jika Anda *mengetuk dua kali* di latar belakang, kamera akan berfokus pada mesh yang dipilih atau seluruh adegan, lihat [Ketuk dua kali pada latar belakang](#dtap-tap-background).


### Translasi {#translation}
Dengan menggerakkan *dua* jari, Anda bisa menggeser kamera.


### Zoom {#zooming}
Dengan gerakan mencubit, Anda bisa memperbesar/memperkecil zoom.


### Memiringkan {#rolling}
Anda bisa *memiringkan* tampilan dengan memutar *dua* jari.
::: warning
Gerakan ini hanya tersedia untuk mode rotasi `Bola jejak`.
:::

### Kontrol desktop {#desktop}

Di desktop, tombol alt/opt dipakai untuk mengendalikan kamera:

* seret ujung pena di ruang kosong = putar kamera
* alt+seret ujung pena = geser
* alt+seret ujung pena, lalu lepaskan alt = zoom (sama seperti ZBrush)

Dengan tablet Wacom yang penanya memiliki 2 tombol atau lebih, gunakan pengaturan Wacom untuk mengonfigurasi ujung pena dan tombol-tombolnya seperti ini:

* ujung pena = klik kiri
* tombol rocker bawah = klik tengah
* tombol rocker atas = klik kanan

Dengan pengaturan tersebut, Anda bisa mengendalikan kamera sepenuhnya dengan pena:

* tombol rocker atas dan gerakkan pena di atas layar tanpa menyentuh = putar kamera
* tombol rocker bawah dan gerakkan pena di atas layar tanpa menyentuh = geser

## Kontrol kamera {#camera-controls}

![](/images/camera_list.webp)

### Tampilan {#views}
Anda bisa menyimpan sudut pandang kamera dengan `Tambah Tampilan`.
Jika Anda mengklik nama tampilan, kamera akan kembali ke tampilan tersebut.


::: tip
Tampilan yang disimpan juga menyimpan pengaturan [Jenis proyeksi](#projection) dan [Gambar referensi](background.md).  
Ini berguna jika Anda ingin berpindah-pindah antara tampilan referensi depan/kiri/belakang dengan latar belakang yang berbeda.
:::

| Tindakan    | Ikon                          | Deskripsi                                                                   |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilitas | ![](/icons/eye_open.webp)    | Mengaktifkan atau menonaktifkan kamera. Kamera yang disembunyikan akan dilewati oleh tombol sebelumnya/berikutnya |
| Nama        |                               | Memilih kamera                                                              |
| Gambar      | ![](/icons/image.webp)       | Gambar mini dari gambar referensi jika terhubung dengan kamera              |
| Proyeksi    | ![](/icons/perspective.webp) | Proyeksi kamera, beserta bidang pandangnya saat dalam perspektif            |
| Perbarui Tampilan | ![](/icons/update_view.webp) | Memperbarui tampilan yang disimpan dengan sudut pandang saat ini      |
| Sunting Nama | ![](/icons/pencil.webp)     | Menyunting nama kamera                                                      |
| Hapus       | ![](/icons/trash.webp)       | Menghapus kamera                                                            |

### ![](/icons/camera_add.webp) Tambah Tampilan {#add}
Membuat kamera baru berdasarkan tampilan saat ini.

### ![](/icons/camera.webp) Ikon {#icons-test}

Menentukan apakah ikon kamera terlihat di viewport. Tombol ini muncul di sebelah `Tambah Tampilan` setelah Anda memiliki sebuah kamera. Jika sebuah kamera dipilih, ikonnya selalu terlihat.

### Jenis proyeksi {#projection}
Pilih antara `Perspektif` dan `Ortografis`.

Dalam perspektif, Anda bisa mengubah `Bidang Pandang Vertikal` (field of view) kamera Anda. Panjang fokus yang setara pada kamera 35mm ditampilkan di atas penggeser, praktis jika Anda terbiasa dengan fotografi.
Untuk memahat, biasanya disarankan memakai FOV yang rendah, karena membantu menjaga proporsi.  
Mode `Ortografis` kurang lebih sama dengan FOV bernilai 0.

### Orang Pertama {#fps}
Hanya untuk perspektif. Mengaktifkan opsi ini menempatkan poros langsung pada kamera, bukan pada pahatan. Menyeret jari di latar belakang akan mengunci posisi kamera tetapi mengubah rotasinya, mirip dengan cara kerja game orang pertama. Berguna saat memahat lingkungan, bukan objek tunggal.

![](/images/camera_rotation_ortho_view.webp)

### Jenis rotasi {#rotation-type}
Secara bawaan kamera memakai mode rotasi `Meja putar`.
Artinya Anda hanya punya dua derajat kebebasan; ini lebih intuitif, tetapi dalam beberapa kasus Anda membutuhkan fleksibilitas lebih.  
Anda bisa beralih ke `Bola jejak`, sehingga Anda bisa *memiringkan* tampilan dengan memutar *dua* jari di viewport. Ada dua mode `Bola jejak`: yang pertama memutar tampilan seperti bola di bawah jari Anda, sedangkan yang kedua (dengan ikon panah) memutar tampilan berdasarkan gerakan horizontal dan vertikal seretan Anda, yang mungkin lebih familier bagi sebagian pengguna.

### Snap Ortografis {#orthographic}

Jika diaktifkan dan Anda memakai keyboard, menahan Shift sambil memutar tampilan akan menjepretkan kamera ke tampilan depan/belakang/atas/bawah/kiri/kanan terdekat, dan menjadikan kamera ortografis. Kamera juga menjadi ortografis saat navigator diklik untuk menjepret ke depan/belakang/kiri/kanan/atas/bawah.

### Atur Ulang Tampilan {#reset}

Memindahkan kamera ke depan, dan memuat seluruh adegan ke dalam tampilan

### Snap tampilan {#snap}
Menjepret ke tampilan depan/belakang/kiri/kanan/atas/bawah terdekat. Jika Anda sudah berada di salah satu tampilan tersebut, mengklik lagi akan menjepret 180 derajat ke sisi sebaliknya.

### Kecepatan {#speed}

Jika menurut Anda kamera bergerak terlalu lambat atau terlalu cepat, Anda bisa mengatur pengali kecepatan untuk `Rotasi`, `Perbesaran` dan `Translasi`. Berguna jika pahatan Anda sangat besar atau sangat kecil.

### Ikhtisar poros {#pivot}

Saat memutar kamera, Anda bisa melihat titik kecil berwarna merah muda: itulah titik poros kamera Anda.  
Sangat penting untuk memahami di mana poros Anda berada agar Anda tidak tersesat atau frustrasi dengan kamera.

Secara bawaan, poros diperbarui melalui operasi berikut:
- ketuk dua kali pada model
- ketuk dua kali pada latar belakang (poros baru akan berada di tengah mesh Anda)
- meletakkan *dua* jari di layar (geser/zoom/miringkan) akan memperbarui poros ke titik tengah di antara *kedua* jari

### Perbarui pivot... {#update-pivot}

Anda bisa mengatur lebih lanjut kapan poros diperbarui dengan opsi-opsi berikut:

* `Ketika kamera mulai bergerak` - Memperbarui poros saat Anda mulai berinteraksi dengan kamera.
* `Pivot di ruang kosong` - Mengizinkan poros baru meskipun Anda melakukan zoom di luar permukaan objek. Membutuhkan `Ketika kamera mulai bergerak`.
* `Ketika mengetuk dua kali` - Memperbarui poros rotasi saat Anda mengetuk dua kali pada permukaan objek.
* `Memahat (Goresan)` - Memperbarui poros saat Anda memahat.

::: tip
Setelah terbiasa, Anda bisa menyembunyikan titik merah muda (petunjuk) itu melalui menu [Pengaturan](settings.md).
:::

### Pusatkan tampilan saat memperkecil zoom {#center-view-when-zooming-out}
Saat memperkecil zoom, kamera tidak bergeser ke samping: kamera hanya mundur, sehingga tampilan tetap di tengah.

### Ketuk dua kali pada objek {#dtap-object}
Jika diaktifkan, mengetuk dua kali pada sebuah objek akan memfokuskan kamera pada titik yang diketuk.

### Ketuk dua kali pada latar belakang {#dtap-tap-background}
Jika diaktifkan, mengetuk dua kali pada latar belakang akan memfokuskan kamera pada:
* `Seleksi` - Objek yang dipilih.
* `Adegan` - Seluruh adegan.
* `Alihkan` - Beralih di antara keduanya pada setiap ketukan ganda. Ada dua opsi `Alihkan`, yang berbeda dalam urutan mana yang lebih dulu, seperti yang ditunjukkan ikonnya.

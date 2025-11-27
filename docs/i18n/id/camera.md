# ![](/icons/camera.webp) Kamera

Menu ini memungkinkan Anda membuat dan mengubah kamera, serta mengontrol bagaimana Anda berinteraksi dengan kamera.

![](/images/camera_overview2.webp)

Kamera di Nomad memiliki beberapa kegunaan:

* Menyiapkan tampilan untuk memahat dari sudut yang presisi
* Digunakan seperti kamera foto untuk membingkai objek Anda
* Sebagai kamera perspektif orang pertama untuk menavigasi skena Anda
* Sebagai kamera ortografik untuk gim isometrik atau rendering bergaya industrial.

## Mengontrol kamera

### Rotasi
Anda memutar kamera dengan menyeret *satu* jari pada latar belakang.
Jika Anda menyeret jari di atas model, maka itu akan memulai operasi pemahatan.

::: tip Bisakah saya memutar kamera jika saya tidak bisa menyentuh latar belakang?
Ya, Anda bisa meletakkan *dua* jari di layar - seolah ingin memulai gerakan pan/zoom - lalu lepaskan *satu* jari.
:::

### Fokus / Reset
*Ketuk dua kali* pada model untuk memfokuskan titik yang dipilih.
Jika Anda *ketuk dua kali* di latar belakang, kamera akan fokus pada mesh yang terpilih.

### Translasi
Dengan menggerakkan *dua* jari, Anda dapat menggeser (pan) kamera.

### Zoom
Dengan menggunakan gerakan cubit (pinch) Anda dapat memperbesar/memperkecil.

### Rolling
Anda dapat *memutar* (roll) tampilan dengan memutar *dua* jari.
::: warning
Gestur ini hanya tersedia untuk mode rotasi `trackball`.
:::

### Kontrol desktop

Di desktop, tombol alt/opt digunakan untuk mengontrol kamera:

* tip drag di ruang kosong = memutar kamera
* alt+tip drag = pan
* alt+tip drag, lalu lepaskan alt = zoom (sama seperti zbrush)

Dengan tablet Wacom yang memiliki 2 tombol atau lebih pada pena, gunakan pengaturan Wacom untuk mengonfigurasi ujung pena dan tombol seperti ini:

* tip = klik kiri
* rocker bawah = klik tengah
* rocker atas = klik kanan

Dengan pengaturan tersebut, Anda dapat memanipulasi kamera hanya dengan pena:

* rocker atas dan gerakan hover = memutar kamera
* rocker bawah dan gerakan hover = pan

## Kontrol kamera

![](/images/camera_list.webp)

### Views
Anda dapat menyimpan titik pandang kamera dengan menggunakan `Add View`.
Jika Anda mengklik nama view, maka kamera akan mengembalikan tampilan tersebut.

::: tip
Sebuah view yang disimpan akan menyimpan pengaturan [Projection Type](#projection-type) dan juga [Reference image](background.md).  
Ini bisa berguna jika Anda ingin berputar di antara tampilan referensi depan/kiri/belakang dengan latar belakang yang berbeda.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Mengaktifkan/nonaktifkan kamera. Kamera yang disembunyikan akan dilewati oleh tombol sebelumnya/berikutnya |
| Name        |                               | Memilih kamera                                                              |
| Image       | ![](/icons/image.webp)       | Thumbnail gambar referensi jika terhubung ke kamera                         |
| Update View | ![](/icons/update_view.webp) | Memperbarui view yang disimpan dengan titik pandang saat ini               |
| Edit Name   | ![](/icons/pencil.webp)      | Mengubah nama kamera                                                        |
| Delete      | ![](/icons/trash.webp)       | Menghapus kamera                                                            |

### ![](/icons/tool_view.webp) Add View
Membuat kamera baru berdasarkan tampilan saat ini.

### ![](/icons/camera.webp) Icons

Mengaktifkan/nonaktifkan apakah ikon kamera terlihat di viewport. Jika sebuah kamera dipilih, ikonnya akan selalu terlihat.

### Projection Type
Anda dapat mengubah `Field of View` (FOV / panjang fokus) kamera Anda.
Biasanya disarankan menggunakan FOV rendah untuk keperluan pemahatan, karena dapat membantu proporsi.  
Anda juga dapat menggunakan mode `Orthographic`, yang kurang lebih mirip dengan FOV sama dengan 0.

### First Person
Mengaktifkan pengaturan pivot agar berada langsung pada kamera, bukan pada patung. Menyeret jari pada latar belakang akan menjaga posisi kamera tetap terkunci, tetapi mengubah rotasi, mirip dengan cara kerja gim orang pertama. Berguna saat memahat lingkungan daripada objek tunggal.

![](/images/camera_rotation_ortho_view.webp)

### Rotation Type
Secara bawaan kamera menggunakan mode rotasi `Turntable`.
Artinya Anda hanya memiliki dua derajat kebebasan, ini lebih intuitif tetapi dalam beberapa kasus Anda menginginkan fleksibilitas lebih.  
Anda dapat beralih ke `Trackball`, Anda akan dapat *memutar* (roll) tampilan dengan memutar *dua* jari pada viewport. Di desktop ada mode trackball alternatif yang mungkin lebih familier bagi beberapa pengguna.

### Orthographic snap

Saat diaktifkan, jika Anda memiliki keyboard, menahan tombol shift saat memutar tampilan akan menjepret (snap) kamera ke tampilan depan/belakang/atas/bawah/kiri/kanan terdekat, dan membuat kamera menjadi ortografik. Kamera juga akan dibuat ortografik ketika kubus tampilan diklik untuk menjepret ke depan/belakang/kiri/kanan/atas/bawah.

### Reset view

Memindahkan kamera ke depan, dan menyesuaikan skena agar pas di tampilan.

### Snap view
Menjepret ke tampilan depan/belakang/kiri/kanan/atas/bawah terdekat. Jika Anda sudah berada di salah satu tampilan tersebut, mengklik lagi akan menjepret 180 derajat ke sisi yang berlawanan.

### Speed

Jika Anda merasa kamera bergerak terlalu lambat atau terlalu cepat, Anda dapat mengatur pengali kecepatan untuk `rotation`, `translation` dan `zooming`. Berguna jika patung Anda sangat besar atau sangat kecil.

### Gambaran pivot

Saat Anda memutar kamera, Anda dapat melihat titik merah muda kecil, itulah titik pivot kamera Anda.  
Sangat penting untuk memahami di mana pivot Anda agar Anda tidak tersesat atau merasa frustrasi dengan kamera.

Secara bawaan pivot diperbarui melalui operasi berikut:
- ketuk dua kali pada model
- ketuk dua kali pada latar belakang (pivot baru akan berada di tengah mesh Anda)
- meletakkan *dua* jari di layar (pan/zoom/roll) akan memperbarui pivot ke tengah *dua* jari

### Update Pivot...

Anda dapat menyesuaikan lebih lanjut agar pivot diperbarui dengan opsi berikut:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Jika Anda sudah terbiasa, Anda dapat menyembunyikan titik merah muda (petunjuk) jika Anda masuk ke menu [Settings](settings.md).
:::

### Double tap on object
Saat `Focus` diaktifkan, ketuk dua kali akan memindahkan pivot ke objek yang diketuk.

### Double tap on background
Saat diaktifkan, mengatur pivot menjadi salah satu dari Selection, Scene, atau bergantian di antara keduanya.

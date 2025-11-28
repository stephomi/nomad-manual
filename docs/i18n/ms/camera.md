# ![](/icons/camera.webp) Kamera {#camera}

Menu ini membolehkan anda mencipta dan mengubah suai kamera, serta mengawal cara anda berinteraksi dengan kamera.

![](/images/camera_overview2.webp)

Kamera dalam Nomad mempunyai beberapa kegunaan:

* Menyediakan pandangan untuk mengukir dari sudut yang tepat
* Digunakan seperti kamera foto untuk membingkaikan objek anda
* sebagai kamera perspektif orang pertama untuk menavigasi adegan anda
* sebagai kamera ortografik untuk permainan isometrik atau penggambaran gaya industri.

## Mengawal kamera {#control}

### Putaran {#rotation}
Anda memutar kamera dengan menyeret *satu* jari pada latar belakang.
Jika anda menyeret jari pada model anda, ia sebaliknya akan memulakan operasi ukiran.

::: tip Bolehkah saya memutar kamera jika saya tidak dapat mengakses latar belakang?
Ya, anda boleh meletakkan *dua* jari pada skrin - seolah-olah anda ingin memulakan gerak isyarat pan/zoom - dan kemudian lepaskan *satu* jari.
:::

### Fokus / Tetap semula {#focus}
*Dwi ketik* pada model untuk memfokuskan titik yang dipilih.
Jika anda *dwi ketik* pada latar belakang, kamera akan memfokuskan pada mesh yang dipilih.

### Terjemahan {#translation}
Dengan menggerakkan *dua* jari, anda boleh menggerakkan (pan) kamera.

### Zum {#zooming}
Dengan menggunakan gerak cubit anda boleh mengezum masuk/keluar.

### Putaran (roll) {#rolling}
Anda boleh *memutar* pandangan dengan memutarkan *dua* jari.
::: warning
Gerak isyarat ini hanya tersedia untuk mod putaran `trackball`.
:::

### Kawalan desktop {#desktop}

Pada desktop, kekunci alt/opt digunakan untuk mengawal kamera:

* tip seret di ruang kosong = putar kamera
* alt+tip seret = pan
* alt+tip seret, kemudian lepaskan alt = zum (sama seperti zbrush)

Dengan tablet Wacom yang mempunyai 2 atau lebih butang pada pen, gunakan tetapan Wacom untuk mengkonfigurasi hujung dan butang seperti berikut:

* tip = klik kiri
* rocker bawah = klik tengah
* rocker atas = klik kanan

Dengan tetapan tersebut, anda boleh memanipulasi kamera hanya dengan pen:

* rocker atas dan gerakan hover = putar kamera
* rocker bawah dan gerakan hover = pan

## Kawalan kamera {#camera-controls}

![](/images/camera_list.webp)

### Paparan {#views}
Anda boleh menyimpan titik pandangan kamera dengan menggunakan `Add View`.
Jika anda klik pada nama pandangan, kamera akan memulihkan pandangan tersebut.

::: tip
Pandangan yang disimpan akan menyimpan tetapan [Projection Type](#projection-type) dan juga [Reference image](background.md).  
Ia boleh berguna jika anda mahu berulang alik antara pandangan rujukan depan/kiri/belakang dengan latar belakang yang berbeza.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Togol kamera. Kamera tersembunyi akan dilangkau daripada butang sebelumnya/berikutnya |
| Name        |                               | Pilih kamera                                                                |
| Image       | ![](/icons/image.webp)       | Imej kecil bagi imej rujukan jika ia dipautkan kepada kamera               |
| Update View | ![](/icons/update_view.webp) | Kemas kini pandangan yang disimpan dengan titik pandangan semasa           |
| Edit Name   | ![](/icons/pencil.webp)      | Edit nama kamera                                                            |
| Delete      | ![](/icons/trash.webp)       | Padam kamera                                                                |

### ![](/icons/tool_view.webp) Tambah paparan {#add}
Cipta kamera baharu berdasarkan pandangan semasa.

### ![](/icons/camera.webp) Ikon {#icons-test}

Togol sama ada ikon kamera kelihatan dalam viewport. Jika kamera dipilih, ikonnya sentiasa kelihatan.

### Jenis unjuran {#projection}
Anda boleh menukar `Field of View` (FOV / panjang fokus) kamera anda.
Biasanya disarankan untuk menggunakan FOV rendah untuk tujuan mengukir, kerana ia boleh membantu untuk perkadaran.  
Anda juga boleh menggunakan mod `Orthographic`, yang lebih kurang sama dengan FOV bersamaan 0

### Pandang pertama {#fps}
Dayakan tetapan pivot supaya berada terus pada kamera, bukannya pada arca. Menyeret jari pada latar belakang akan mengekalkan kedudukan kamera terkunci, tetapi menukar putaran, serupa dengan cara permainan orang pertama berfungsi. Berguna apabila mengukir persekitaran dan bukannya objek tunggal.

![](/images/camera_rotation_ortho_view.webp)

### Jenis putaran {#rotation-type}
Secara lalai kamera menggunakan mod putaran `Turntable`.
Ini bermakna anda hanya mempunyai dua darjah kebebasan, ia lebih intuitif tetapi dalam beberapa kes anda akan mahukan lebih fleksibiliti.  
Anda boleh menukar kepada `Trackball`, anda akan dapat *memutar* pandangan dengan memutarkan *dua* jari pada viewport. Pada desktop terdapat mod trackball alternatif yang mungkin lebih biasa bagi sesetengah pengguna.

### Lekapan ortografik {#orthographic}

Apabila didayakan, jika anda mempunyai papan kekunci, menahan shift semasa memutar pandangan akan menjentik kamera ke pandangan depan/belakang/atas/bawah/kiri/kanan terdekat, dan menjadikan kamera ortografik. Kamera juga akan dijadikan ortografik apabila kiub pandangan diklik untuk menjentik ke depan/belakang/kiri/kanan/atas/bawah.

### Tetap semula paparan {#reset}

Gerakkan kamera ke hadapan, dan muatkan adegan ke dalam pandangan

### Lekap paparan {#snap}
Jentik ke pandangan depan/belakang/kiri/kanan/atas/bawah terdekat. Jika anda sudah berada dalam salah satu pandangan tersebut, klik sekali lagi akan menjentik 180 darjah ke sisi bertentangan.

### Kelajuan {#speed}

Jika anda rasa kamera bergerak terlalu perlahan atau terlalu laju, anda boleh menetapkan pengganda kelajuan untuk `rotation`, `translation` dan `zooming`. Berguna jika arca anda sangat besar atau sangat kecil.

### Gambaran keseluruhan paksi putar {#pivot}

Apabila anda memutar kamera anda boleh melihat titik merah jambu kecil, ini ialah titik pivot kamera anda.  
Sangat penting untuk memahami di mana pivot anda supaya anda tidak tersesat atau kecewa dengan kamera.

Secara lalai pivot dikemas kini melalui operasi berikut:
- dwi ketik pada model
- dwi ketik pada latar belakang (pivot baharu akan berada di tengah mesh anda)
- meletakkan *dua* jari pada skrin (pan/zoom/roll) akan mengemas kini pivot pada pusat *dua* jari tersebut

### Kemas kini paksi putar... {#update-pivot}

Anda boleh menyesuaikan lagi pivot untuk dikemas kini dengan pilihan berikut:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Apabila anda sudah biasa dengannya, anda boleh menyembunyikan titik merah jambu (petunjuk) jika anda pergi ke menu [Settings](settings.md).
:::

### Dwi ketik pada objek {#dtap-object}
Apabila `Focus` didayakan, dwi ketik akan mengalihkan pivot ke objek yang diketuk.

### Dwi ketik pada latar belakang {#dtap-tap-background}
Apabila didayakan, tetapkan pivot supaya menjadi salah satu daripada Selection, Scene, atau bertogol antara keduanya.
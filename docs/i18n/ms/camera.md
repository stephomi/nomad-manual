# ![](/icons/camera.webp) Kamera {#camera}

Menu ini membolehkan anda mencipta dan mengubah suai kamera, serta mengawal cara anda berinteraksi dengan kamera.

![](/images/camera_overview2.webp)

Kamera dalam Nomad mempunyai beberapa kegunaan:

* Menyediakan pandangan untuk memahat dari sudut yang tepat
* Digunakan seperti kamera foto untuk membingkai objek anda
* Sebagai kamera perspektif orang pertama untuk menjelajah adegan anda
* Sebagai kamera ortografik untuk permainan isometrik atau pemaparan gaya industri.

## Mengawal kamera {#control}

### Putaran {#rotation}
Anda memutar kamera dengan menyeret *satu* jari pada latar belakang.
Jika anda menyeret jari pada model anda, operasi pemahatan akan bermula.

::: tip Bolehkah saya memutar kamera jika saya tidak dapat mencapai latar belakang?
Ya, anda boleh meletakkan *dua* jari pada skrin - seolah-olah anda mahu memulakan gerak isyarat anjak/zum - kemudian angkat *satu* jari.
:::

### Fokus / Tetapkan semula {#focus}
*Ketuk dua kali* pada model untuk memfokus pada titik yang dipilih.
Jika anda *ketuk dua kali* pada latar belakang, kamera akan memfokus pada mesh yang dipilih atau seluruh adegan, lihat [Ketuk dua kali pada latar belakang](#dtap-tap-background).


### Anjakan {#translation}
Dengan menggerakkan *dua* jari, anda boleh menganjak kamera.


### Zum {#zooming}
Dengan menggunakan gerak isyarat cubit, anda boleh mengezum masuk/keluar.


### Menggolek {#rolling}
Anda boleh *menggolekkan* pandangan dengan memutar *dua* jari.
::: warning
Gerak isyarat ini hanya tersedia untuk mod putaran `Bebola jejak`.
:::

### Kawalan desktop {#desktop}

Pada desktop, kekunci alt/opt digunakan untuk mengawal kamera:

* seret hujung pen di ruang kosong = putar kamera
* alt+seret hujung pen = anjak
* alt+seret hujung pen, kemudian lepaskan alt = zum (sama seperti ZBrush)

Bagi tablet Wacom yang mempunyai 2 atau lebih butang pada pen, gunakan tetapan Wacom untuk mengkonfigurasi hujung dan butang seperti berikut:

* hujung = klik kiri
* butang rocker bawah = klik tengah
* butang rocker atas = klik kanan

Dengan tetapan ini, anda boleh mengawal kamera menggunakan pen sahaja:

* butang rocker atas sambil menggerakkan pen tanpa menyentuh = putar kamera
* butang rocker bawah sambil menggerakkan pen tanpa menyentuh = anjak

## Kawalan kamera {#camera-controls}

![](/images/camera_list.webp)

### Pandangan {#views}
Anda boleh menyimpan titik pandangan kamera dengan menggunakan `Tambah Pandangan`.
Jika anda mengklik nama pandangan, kamera akan memulihkan pandangan itu.


::: tip
Pandangan yang disimpan akan menyimpan tetapan [Jenis Projeksi](#projection) dan juga [Imej rujukan](background.md).  
Ini berguna jika anda mahu bertukar-tukar antara pandangan rujukan depan/kiri/belakang dengan latar belakang yang berbeza.
:::

| Tindakan              | Ikon                          | Penerangan                                                                  |
| :-------------------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Keterlihatan          | ![](/icons/eye_open.webp)    | Togol kamera. Kamera tersembunyi akan dilangkau oleh butang sebelum/seterusnya |
| Nama                  |                               | Pilih kamera                                                                |
| Imej                  | ![](/icons/image.webp)       | Lakaran kecil imej rujukan jika ia dipautkan kepada kamera                  |
| Projeksi              | ![](/icons/perspective.webp) | Projeksi kamera, dengan medan pandangannya apabila dalam perspektif         |
| Kemas kini pandangan  | ![](/icons/update_view.webp) | Kemas kini pandangan yang disimpan dengan titik pandangan semasa            |
| Namakan semula        | ![](/icons/pencil.webp)      | Sunting nama kamera                                                         |
| Padam                 | ![](/icons/trash.webp)       | Padam kamera                                                                |

### ![](/icons/camera_add.webp) Tambah Pandangan {#add}
Cipta kamera baharu berdasarkan pandangan semasa.

### ![](/icons/camera.webp) Ikon {#icons-test}

Togol sama ada ikon kamera kelihatan dalam paparan. Butang ini muncul di sebelah `Tambah Pandangan` sebaik sahaja anda mempunyai kamera. Jika kamera dipilih, ikonnya sentiasa kelihatan.

### Jenis Projeksi {#projection}
Pilih antara `Perspektif` dan `Ortografi`.

Dalam perspektif, anda boleh mengubah `Pandangan Vertikal` (medan pandangan) kamera anda. Panjang fokus yang sepadan untuk kamera 35mm dipaparkan di atas peluncur, berguna jika anda biasa dengan fotografi.
Biasanya disarankan untuk menggunakan FOV yang rendah semasa memahat, kerana ia membantu dari segi perkadaran.  
Mod `Ortografi` lebih kurang sama dengan FOV bersamaan 0.

### Pandangan Orang Pertama {#fps}
Perspektif sahaja. Membolehkan pangsi ditetapkan terus pada kamera, bukan pada arca. Menyeret jari pada latar belakang akan mengekalkan kedudukan kamera, tetapi mengubah putarannya, sama seperti permainan orang pertama. Berguna apabila memahat persekitaran dan bukannya objek tunggal.

![](/images/camera_rotation_ortho_view.webp)

### Jenis Putaran {#rotation-type}
Secara lalai, kamera menggunakan mod putaran `Meja Putar`.
Ini bermakna anda hanya mempunyai dua darjah kebebasan; ia lebih intuitif tetapi dalam sesetengah kes anda mahukan lebih fleksibiliti.  
Anda boleh bertukar kepada `Bebola jejak`, dan anda akan dapat *menggolekkan* pandangan dengan memutar *dua* jari pada paparan. Terdapat dua mod `Bebola jejak`: yang pertama menggolekkan pandangan seperti bola di bawah jari anda, manakala yang kedua (dengan ikon anak panah) memusingkan pandangan berdasarkan pergerakan mendatar dan menegak seretan anda, yang mungkin lebih biasa bagi sesetengah pengguna.

### Snap Ortografik {#orthographic}

Apabila didayakan, jika anda mempunyai papan kekunci, menahan shift semasa memutar pandangan akan melekatkan kamera ke pandangan depan/belakang/atas/bawah/kiri/kanan yang terdekat, dan menjadikan kamera ortografik. Kamera juga akan dijadikan ortografik apabila navigator diklik untuk melekat ke depan/belakang/kiri/kanan/atas/bawah.

### Tetapkan semula pandangan {#reset}

Gerakkan kamera ke depan, dan muatkan adegan ke dalam pandangan

### Pandangan Snap {#snap}
Lekat ke pandangan depan/belakang/kiri/kanan/atas/bawah yang terdekat. Jika anda sudah berada dalam salah satu pandangan tersebut, mengklik sekali lagi akan berpusing 180 darjah ke sisi bertentangan.

### Kelajuan {#speed}

Jika anda rasa kamera bergerak terlalu perlahan atau terlalu laju, anda boleh menetapkan pengganda kelajuan untuk `Putaran`, `Zum` dan `Anjakan`. Berguna jika pahatan anda sangat besar atau sangat kecil.

### Gambaran keseluruhan pangsi {#pivot}

Apabila anda memutar kamera, anda dapat melihat titik merah jambu kecil; ini ialah titik pangsi kamera anda.  
Sangat penting untuk memahami di mana pangsi anda berada supaya anda tidak sesat atau kecewa dengan kamera.

Secara lalai, pangsi dikemas kini melalui operasi berikut:
- ketuk dua kali pada model
- ketuk dua kali pada latar belakang (pangsi baharu akan berada di tengah mesh anda)
- meletakkan *dua* jari pada skrin (anjak/zum/golek) akan mengemas kini pangsi di tengah-tengah *dua* jari tersebut

### Kemas kini pangsi... {#update-pivot}

Anda boleh menyesuaikan lagi cara pangsi dikemas kini dengan pilihan berikut:

* `Apabila kamera mula bergerak` - Kemas kini pangsi apabila anda mula berinteraksi dengan kamera.
* `Benarkan pivot udara` - Benarkan pangsi baharu walaupun anda mengezum di luar permukaan objek. Memerlukan `Apabila kamera mula bergerak`.
* `Apabila mengetuk dua kali` - Kemas kini pangsi putaran apabila anda mengetuk dua kali pada permukaan objek.
* `Ukir (Sapuan)` - Kemas kini pangsi apabila anda memahat.

::: tip
Apabila anda sudah biasa, anda boleh menyembunyikan titik (petunjuk) merah jambu itu dalam menu [Tetapan](settings.md).
:::

### Pusatkan pandangan semasa mengezum keluar {#center-view-when-zooming-out}
Apabila mengezum keluar, kamera tidak menganjak ke sisi: ia hanya bergerak ke belakang, jadi pandangan kekal di tengah.

### Ketuk dua kali pada objek {#dtap-object}
Apabila didayakan, mengetuk dua kali pada objek akan memfokuskan kamera pada titik yang diketuk.

### Ketuk dua kali pada latar belakang {#dtap-tap-background}
Apabila didayakan, mengetuk dua kali pada latar belakang akan memfokuskan kamera pada:
* `Pemilihan` - Objek yang dipilih.
* `Adegan` - Seluruh adegan.
* `Tukar` - Bertukar antara kedua-duanya pada setiap ketukan dua kali. Terdapat dua pilihan `Tukar`; perbezaannya ialah yang mana satu didahulukan, seperti yang ditunjukkan oleh ikonnya.

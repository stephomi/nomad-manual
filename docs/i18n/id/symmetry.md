# ![](/icons/symmetry.webp) Simetri

Menu ini mengontrol bagaimana goresan akan diulang melintasi bidang cermin atau secara radial, serta cara memulihkan simetri pada objek yang tidak simetris.

![](/images/symmetry_overview.webp) 

## Gambaran umum
Anda dapat menggunakan simetri dengan beberapa cara:

* Sebagai cermin, membalik pekerjaan melintasi X (kiri/kanan), Y (atas/bawah), Z (belakang/depan), atau kombinasinya. 
* Simetri radial dapat diatur pada X Y Z dengan jumlah pengulangan, misalnya untuk memahat bentuk bintang laut. 
* Cermin dapat beroperasi di sekitar titik asal (disebut mode dunia/world) atau di sekitar pusat objek (disebut mode lokal/local).
* Pahatan yang dimulai tidak simetris dapat dipaksa menjadi simetris.

Jalan pintas untuk mengaktifkan/nonaktifkan simetri juga dapat ditemukan di panel cepat kiri (*"Sym"*). Huruf kecil 'L/W' menunjukkan apakah Nomad berada dalam mode simetri Lokal atau Dunia. Anda juga dapat menekan lama atau menggeser ke tengah layar untuk memunculkan menu.

![](/images/symmetry_button.webp) 

Ini adalah opsi global, jadi statusnya akan terbawa ke berbagai alat.
Satu-satunya pengecualian adalah alat transformasi ([Move](#translate), [Rotate](#rotate), [Scale](#scale) dan [Gizmo](#gizmo)) yang memiliki status simetri masing-masing.

::: tip
Menu simetri terutama untuk mengontrol simetri goresan. Anda juga dapat mencerminkan dan mengulang objek melalui [repeater yang ada di menu scene](scene#repeaters). 
:::

## Enabled
Alihkan mode cermin, ini sama dengan tombol `Sym` di panel cepat kiri. 

## Planes

Aktifkan bidang simetri dan jumlah pengulangan untuk simetri radial. Perhatikan bahwa Anda tidak harus memilih hanya satu bidang, Anda dapat mengaktifkan 1, 2, atau 3 bidang sekaligus untuk simetri yang kompleks.

Sumbu dan jumlah pengulangan untuk simetri radial. Perhatikan bahwa ini juga tidak dibatasi pada satu sumbu, dan bahkan dapat bekerja dalam kombinasi dengan simetri bidang untuk menghasilkan detail dengan sangat cepat. (Jumlah total pengulangan dibatasi hingga 150)

![](/videos/symmetry_demo.mp4) 

## Method
Cermin dapat bersifat 'Local', dan bergerak bersama objek, atau 'World', dan tidak bergerak. Jika Anda tidak yakin mode mana yang Anda perlukan, amati bidang cermin dan indikator radial yang ditumpangkan pada objek. Saat dalam mode lokal, jika Anda menggunakan gizmo transformasi dan memindahkan model, indikator cermin juga akan bergerak. Saat dalam mode dunia, indikator cermin akan tetap diam, dan objek akan bergeser melewatinya.

## Mirroring
![](/images/symmetry_mirroring.webp)

Saat memahat dekat bidang simetri, beberapa kuas akan memiliki perilaku simetri yang tidak sempurna. Bagian ini memungkinkan Anda memulihkan simetri dengan menyalin satu sisi pahatan ke sisi lainnya. 

`Direction` - Tombol `<<` dan `>>` menentukan sisi mana yang akan disalin ke sisi lain. Nomad menghitung ini dari viewport Anda saat ini, jadi mengaturnya ke `<<` misalnya akan selalu menyalin dari kanan layar ke kiri layar.

![](/icons/shield.webp) `Mask` - Tombol mask memungkinkan Anda mengisolasi bagian yang akan dicerminkan; memasker sisi tujuan akan melindungi area tersebut, memasker sisi sumber akan menghentikan area itu untuk dicerminkan ke tujuan. 

![](/icons/tool_hide.webp) `Hide` - Saat aktif, area yang disembunyikan di sisi sumber tidak akan dicerminkan ke sisi tujuan. 

`Mirror` akan mencoba mengidentifikasi apakah topologi sama di kedua sisi cermin, dan jika ya, hanya akan memindahkan verteks. Ini adalah skenario yang lebih umum.

`Split & Mirror` pada dasarnya akan memotong objek sepanjang cermin, menyalin satu sisi, mencerminkannya ke sisi lain, dan mengelas verteks di sepanjang cermin. Ini adalah opsi yang lebih destruktif, dan akan menghapus multiresolusi, tetapi terkadang metode ini diperlukan jika model sangat berbeda di kedua sisi cermin.

### Flip object
![](/images/symmetry_flip.webp)
Membuat sisi kiri menjadi sisi kanan, dan sebaliknya. Mirip tampilannya dengan jika Anda menggunakan menu alat gizmo dan mengatur skala ke -1 pada X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Lokasi dan orientasi simetri dapat diedit (namun tidak direkomendasikan!). Jika diperlukan, `World center` dan `Orientation` akan mengatur ulang lokasi dan orientasi simetri ke nilai defaultnya.

Nomad biasanya tahu di mana harus menempatkan bidang simetri. Tidak disarankan untuk menyesuaikannya secara manual, tetapi tombol `Gizmo (Edit)` memungkinkan hal ini untuk pengguna tingkat lanjut. Saat tombol ini diklik, sebuah gizmo akan ditampilkan untuk memungkinkan Anda mentranslasi dan memutar bidang simetri. Jika Anda ingin mengembalikan pusat dan orientasi default, tombol `object center` dan `orientation` akan melakukannya.

Perilaku opsi-opsi ini akan berubah tergantung pada ruang (*Local/World*) tempat Anda berada.
Jadi jika tidak bekerja seperti yang Anda harapkan, pastikan untuk memeriksa apakah Anda berada di ruang yang benar.

::: tip
Tombol `Gizmo (Edit)` sengaja dibuat abu-abu sebagai pengingat bahwa Anda mungkin sebaiknya tidak menggunakannya!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` dan `Show plane` akan mengaktifkan/menonaktifkan overlay viewport dari lokasi simetri. Perhatikan bahwa mematikan opsi ini hanya akan berlaku ketika menu simetri ditutup.

# ![](/icons/operation.webp) Operasi {#operation}

Menu ini menggunakan satu operasi pada seluruh permukaan objek yang dipilih sekali gus: melicinkan, mengendurkan, menggilap, mengembangkan, melaraskan warna, serta mengaburkan atau menajamkan cat dan topeng.

![](/images/operation_overview.webp)

## Gambaran keseluruhan {#overview}

Berus hanya bertindak di tempat anda membuat sapuan, tetapi operasi bertindak pada setiap verteks objek yang dipilih dalam satu langkah. Tajuk menunjukkan nama objek, atau bilangan objek apabila beberapa objek dipilih.

Setiap operasi ialah satu peluncur: seret ke kanan untuk menggunakan lebih banyak, ke kiri untuk menggunakan kurang (atau operasi yang bertentangan, bagi peluncur yang mempunyai anak panah di kedua-dua belah). Peluncur kembali ke sifar sebaik sahaja anda melepaskannya, dan setiap seretan ialah satu langkah dalam [Sejarah](history.md), jadi anda boleh menggunakan sesuatu operasi beberapa kali dalam dos yang kecil.

::: tip
Operasi ialah cara pantas untuk membersihkan keseluruhan mesh selepas remesh voxel atau boolean: sedikit `Santai` meratakan saiz segi tiga, sedikit `Lancar` membuang hingar, tanpa perlu mencari setiap tempat dengan berus.
:::

## Penapis {#filters}

Butang di bahagian atas mengehadkan kawasan yang terkesan oleh operasi:

* `Topeng` - Kawasan bertopeng dibiarkan tanpa diubah.
* `Sembunyi` - Kawasan tersembunyi dibiarkan tanpa diubah.
* `Ofset` - (Apabila satu [lapisan](layers.md) dipilih) Hanya kawasan yang mengandungi pahatan dalam lapisan aktif terkesan, jadi anda boleh melicinkan atau mengembangkan isi sesuatu lapisan tanpa menyentuh bahagian lain.

## Pelicinan {#smoothing}

* `Kekalkan isipadu` - Melicinkan tanpa mengecutkan permukaan. Butang gear menyimpan nilai `Mengecilkan` dan `Kembang` yang digunakan untuknya.
* `Kekalkan sempadan` - Verteks pada sempadan mesh (tepi sesuatu lubang) tidak bergerak.
* `Melicinkan stabil` - Cuba menjadikan pelicinan tidak bergantung pada topologi. Ia paling berkesan apabila kepadatan poligon sangat berbeza-beza.
* `Lancar` - Melicinkan permukaan. Seret ke kiri untuk `Tajamkan` permukaan sebaliknya.
* ![](/icons/group.webp) `Lancar` - Melicinkan sempadan antara [kumpulan muka](tools.md#facegroup), meluruskan garis luar kumpulan yang bergerigi. Seret ke kiri untuk menajamkannya.
* `Santai` - Menyeragamkan poligon sambil mengekalkan bentuk.
* ![](/icons/group.webp) `Santai` - Mengendurkan poligon di sepanjang sempadan kumpulan muka.
* `Kekalkan penjuru` - Dengan `Lancar` dan `Santai` kumpulan muka, sempadan kekal tetap di tempat ia membelok lebih daripada sudut ini, jadi penjuru kekal tajam manakala sisinya menjadi licin. Gunakan kotak semaknya untuk menghidupkannya.

## Gilap {#polish}

Meratakan permukaan menjadi faset yang kemas, seperti alat [Gilap](tools.md#polish). `Sudut` menentukan muka yang menjadi rata bersama: muka yang melentur kurang daripada sudut ini menjadi satu faset. Sudut yang lebih rendah mengekalkan lebih banyak lipatan dan faset yang lebih kecil.

## Kembang {#inflate}

Menolak permukaan ke luar mengikut normalnya, atau ke dalam apabila anda menyeret ke kiri. `Normal (Santai)` mengendurkan poligon pada masa yang sama supaya ia tidak meregang; gunakan kotak semaknya untuk mematikannya.

## Pelarasan warna {#color-adjustments}

Pilih saluran yang hendak dilaraskan, `Warna`, `Kekasaran`, `Kemetalan`, `Kelegapan`, `Kepadatan` (lukisan kepadatan [Quad Remesher](tools.md#quad-remesher), jika objek mempunyainya) atau `Topeng`, kemudian:

* `Pendedahan` - Mencerahkan atau menggelapkan nilai.
* `Ketepuan` - (`Warna` sahaja) Warna yang lebih atau kurang terang.
* `Kontras` - Menjarakkan nilai, atau mendekatkannya antara satu sama lain.
* `Rona` - Mengalihkan warna di sekeliling roda warna.

## Kabur {#blur}

Mengaburkan saluran yang dipilih di seluruh permukaan: togol `Warna`, `Kekasaran`, `Kemetalan`, `Kelegapan`, `Kepadatan` atau `Topeng`, kemudian seret `Kabur`. Seret ke kiri untuk `Tajamkan` sebaliknya.

Bagi topeng, ini sama seperti peluncur `Kabur` pada alat [Topeng](tools.md#mask). Di sini anda juga boleh mengaburkan saluran cat.

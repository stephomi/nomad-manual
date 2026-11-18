# ![](/icons/image.webp) Latar Belakang {#background}

Menu ini mengawal warna latar belakang Nomad, serta imej rujukan yang anda mahu gunakan.

![](/images/background_overview.webp)

## Jenis {#type}
![](/images/background_selector.webp)

Terdapat tiga pilihan untuk latar belakang port pandangan.

* `Persekitaran` - Paparkan peta persekitaran yang dipilih dalam [Shading](shading.md). Anda boleh melaraskannya lagi dengan gelangsar `Kabur` dan `Pendedahan` (kecerahan). 
* `Warna` - Satu warna rata pilihan anda
* `Kecerunan` - Peralihan antara dua warna. Gelangsar `Faktor` membolehkan anda mengalihkan titik tengah kecerunan.  

### Jenis kecerunan {#gradient-type}
Dengan `Kecerunan`, pilih bentuknya:
* `Linear` - Kecerunan lurus, arahnya ditetapkan oleh gelangsar `Sudut`.
* `Jejari` - Kecerunan bulat yang bermula dari tengah skrin.
* `Langit` - Kecerunan yang berpaut pada ufuk dunia, jadi ia mengikut kamera apabila anda memandang ke atas dan ke bawah.

Setiap warna mempunyai butang set semula dan pemilih warna, untuk mengambil warna daripada skrin.

## ![](/icons/lock.webp) Segerak dengan kunci kamera {#sync-on-camera-lock}
Apabila kamera dikunci dengan [Navigator](settings.md#snap-cube), imej rujukan mengikut pergerakan kamera, supaya ia kekal sejajar dengan arca anda.

* `Benarkan kecondongan kamera (Bebola jejak)` - Benarkan kamera condong apabila anda keluar daripada kunci kamera.
* `Reset semasa buka kunci` - Set semula pandangan apabila anda keluar daripada kunci kamera.

## Imej Rujukan {#reference}

![](/images/background_reference.webp)

Anda boleh menambah imej pilihan anda pada latar belakang untuk dijadikan rujukan. Ketik `Import...` untuk menambahnya, kemudian tandakan `Imej rujukan` untuk memaparkannya.
Anda boleh menukar kedudukan dan skalanya, contohnya jika anda mahu mengalihkannya ke penjuru skrin.

### ![](/icons/tool_transform.webp) Transformasi {#transform}

Butang ini membolehkan anda meletakkan imej rujukan secara interaktif. Gunakan 2 jari untuk menganjak, menskala dan memutar imej rujukan ke tempatnya. `Tetapkan semula` mengembalikan imej ke kedudukan asalnya. Kedudukan akhir akan dipaparkan pada gelangsar di bawah:

* `Tindihan` - pada 0% imej rujukan sentiasa berada di belakang objek anda, pada 100% ia berada di hadapan. 
* `Kelegapan` - Sejauh mana imej itu lut sinar.
* `Pemprosesan Pasca` - Kenakan kesan pemprosesan pasca pada imej rujukan. Matikannya untuk mengekalkan warna asal.
* `Posisi X` / `Posisi Y` - Kedudukan X dan Y imej.
* `Skala` - Skala imej.
* `Putaran` - Putaran imej.


::: tip

Kamera dan imej rujukan saling berkait. 

Ini bermakna jika anda menyediakan imej rujukan supaya sejajar dengan arca anda, kemudian mencipta kamera daripada [menu Kamera](camera.md), kedudukan, putaran dan skala imej rujukan turut disimpan bersama kamera itu. Anda boleh mematikan imej rujukan dan berputar ke pandangan lain. Apabila anda melihat melalui kamera itu semula, imej rujukan akan diaktifkan dengan tetapan yang anda gunakan.

Malah, anda boleh memilih imej yang berbeza untuk kamera yang berbeza!

 ![](/videos/reference_camera.mp4)

:::

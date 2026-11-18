# ![](/icons/postprocess.webp) PascaProses {#post-process}

Menu ini mengatur banyak aspek Nomad yang memengaruhi tampilan render.

![](/images/postprocess_overview_drac.webp)

Pemrosesan pasca bisa mengubah tampilan akhir adegan Anda secara signifikan.

![](/images/postprocess_overview.webp)
*Adegan yang sama sebelum dan sesudah pemrosesan pasca, tanpa tambahan lampu atau perubahan material.*

Pemrosesan pasca bisa sangat memengaruhi performa, tergantung perangkat Anda.
Ada kotak centang global `Pemrosesan pasca` untuk menonaktifkan semua pemrosesan pasca, sehingga Anda bisa cepat kembali memahat/memodelkan tanpa kehilangan preset Anda.
Untuk render PBR, [Oklusi ambien](#ambient-occlusion-ssao), [Refleksi](#reflection-ssr) dan [Pemetaan Nada](#tone-mapping) sebaiknya diaktifkan.

Namun, sebagian besar waktu Anda akan ingin pemrosesan pasca dinonaktifkan saat memahat, agar bisa fokus pada bentuknya sendiri, bukan pada render.


## Kualitas {#quality}

![](/images/postprocess_quality.webp)

Opsi-opsi ini meningkatkan kualitas render, dengan mengorbankan performa.

### Sampel frame maksimum {#max-frame-sampling}
Nomad menghitung sejumlah pemrosesan pasca untuk render satu frame, yang bisa terlihat berbintik (noise). Kontrol ini menentukan berapa banyak frame yang akan dirender, lalu dipadukan untuk menghilangkan sebagian besar artefak noise. Beberapa efek tidak memerlukan sampel tambahan (misalnya grading warna), sedangkan efek lain seperti bayangan lembut dan pencahayaan global bisa memerlukan ratusan sampel agar bebas noise. 

Di viewport, hal ini bisa terlihat setiap kali Nomad dibiarkan diam: kualitas gambar akan meningkat secara bertahap hingga mencapai sampel maksimum, lalu berhenti. Setelah berhenti, Nomad tidak melakukan apa-apa, sehingga menghemat baterai. Jumlah perhitungan ini juga dipakai di bagian render pada [menu File](files) saat 'ekspor png' diklik.

Kotak centang di sebelah penggeser mengaktifkan atau menonaktifkan pengambilan sampel frame.

### Resolusi render {#resolution-multiplier}
Penggeser ini mengatur resolusi render. Nilai x1.0 berarti render dilakukan pada resolusi piksel perangkat. Nilai x0.5 merender pada setengah resolusi, yang cepat tetapi berkualitas rendah. Nilai lebih dari 1 merender pada ukuran yang lebih besar, lalu diperkecil. Hasilnya berkualitas lebih tinggi dengan noise lebih sedikit, tetapi waktu rendernya lebih lama.

Pengaruhnya terhadap performa sangat besar, jadi usahakan tetap di x1.25 atau lebih rendah. Nilai ini tidak disimpan di pengaturan, dan efek [Seni Piksel](#pixel-art) menimpanya.

### ![](/icons/intensity.webp) Sampel maksimum {#max-samples}

Meningkatkan kualitas efek pemrosesan pasca, dengan mengorbankan performa.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Melakukan dithering pada piksel untuk mengurangi artefak banding (misalnya pada gradien atau vinyet). Biasanya opsi ini sebaiknya diaktifkan, tetapi bisa dimatikan untuk operasi tertentu (misalnya mengekspor peta kedalaman atau operasi khusus data lainnya).

### ![](/icons/denoise.webp) Denoiser (oidn) {#oidn}

Menerapkan denoiser pada gambar setelah semua frame terkumpul. Ini memungkinkan Anda memakai jumlah sampel yang jauh lebih rendah. Denoising sangat membebani prosesor, jadi aktifkan hanya jika gambar Anda berbintik. Fitur ini tidak tersedia di semua perangkat.

## Penjelajah preset {#preset-browser}
![](/images/postprocess_presets.webp)
Mengklik gambar di bawah judul `Pemrosesan pasca` akan menampilkan kumpulan preset pemrosesan pasca. Gunakan `Baru` untuk membuat preset dari pengaturan Anda saat ini. Preset bawaan hanya bisa dikloning: untuk membuat preset sendiri, pilih salah satu, klik `Kloning`, lalu lakukan perubahan. Jika sebuah preset memiliki perubahan yang belum disimpan, preset itu menampilkan `Perubahan yang tidak disimpan!`; untuk menyimpan, klik gambar preset, klik lagi di dalam penjelajah preset, lalu pilih `Simpan`.

## Bilah pintasan {#shortcut-bar}
Saat pemrosesan pasca diaktifkan, sebuah bilah di bagian bawah menu mencantumkan setiap efek (`SSR`, `SSGI`, `SSAO`, `DoF`, `Kembang`...). Ketuk salah satunya untuk melompat ke bagiannya. Efek yang dimatikan tampil abu-abu, sehingga bilah ini juga menjadi ringkasan cepat tentang apa yang dilakukan preset saat ini.

## ![](/icons/postprocess_ssr.webp) Refleksi (SSR) {#reflection-ssr}
Dengan opsi ini, objek bisa memantulkan objek lain di adegan, selama objek-objek tersebut terlihat di layar.
Jika ada objek metalik dan mengilap di adegan Anda, opsi ini sebaiknya dipakai.
Opsi ini memerlukan mode shading [Terang (PBR)](shading.md#pbr).


| SSR mati                   | SSR aktif                 |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Pencahayaan Global (SSGI) {#global-illumination-ssgi}

Pencahayaan global menyimulasikan bagaimana cahaya memantul di antara permukaan, misalnya dinding merah akan memantulkan warna merah ke objek putih di dekatnya. Ini bisa sangat meningkatkan realisme render jika dipakai bersama oklusi ambien dan refleksi. Seperti refleksi, efek ini memerlukan mode shading [Terang (PBR)](shading.md#pbr).

`Kekuatan` - Intensitas pencahayaan global. 



| SSGI mati                  | SSGI aktif                |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Sebuah lampu sorot berada di belakang bola, diarahkan ke langit-langit. Dengan SSGI mati, hanya langit-langit yang terang. Dengan SSGI aktif, cahaya memantul dari langit-langit ke dinding lalu ke bola._

## ![](/icons/postprocess_ssao.webp) Oklusi ambien (SSAO) {#ambient-occlusion-ssao}
Oklusi ambien akan menggelapkan area yang lebih sulit dijangkau cahaya (sudut-sudut, dll.).
Efek ini hanya bergantung pada geometri model.

* `Kekuatan`- Intensitas efek.
* `Ukuran`- Seberapa luas sebaran efeknya.
* `Ketebalan` - Seberapa tebal kedalaman yang diasumsikan untuk objek penghalang, sebagai persentase dari `Ukuran`.
* `Warna rona` - Warna yang dikalikan ke oklusi, dipakai untuk efek kreatif.


| SSAO mati                   | SSAO aktif                 |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO paling terlihat di area yang terutama diterangi cahaya lingkungan. Area yang terkena cahaya langsung yang kuat akan menerima efek AO yang jauh lebih lemah.

:::

## ![](/icons/postprocess_dof.webp) Kedalaman bidang {#depth-of-field-dof}
Menambahkan efek buram pada area di luar fokus.

Cukup ketuk model Anda untuk mengubah titik fokus.

* `Mode apertur` - Mengatur keburaman dengan satu apertur kamera, alih-alih dengan dua penggeser keburaman di bawah.
* `Apertur` (_hanya mode apertur_) - Angka f lensa, seperti pada kamera sungguhan. Nilai yang lebih rendah membuka lensa lebih lebar dan membuat lebih buram.
* `Pengaburan jauh` - Jumlah keburaman yang diterapkan di sisi yang lebih jauh dari titik fokus.
* `Pengaburan dekat` - Jumlah keburaman yang diterapkan di antara titik fokus dan kamera.


| DOF mati                  | DOF fokus pada cincin jauh  | DOF fokus pada cincin dekat |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Kembang {#bloom}
Efek bloom membuat area terang di adegan Anda berpendar.

* `Intensitas` - kekuatan efek.
* `Jari-jari` - Sebaran efek.
* `Ambang Batas` - Seberapa terang piksel di adegan harus sebelum mulai berpendar. Pada nilai 0 semuanya berpendar; nilai yang tinggi hanya membuat piksel paling terang yang berpendar.
* `Warna rona` - warna yang bisa ditambahkan ke bloom untuk efek kreatif.

| Bloom mati                   | Bloom dengan jari-jari 0    | Bloom dengan jari-jari 1    |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Pemetaan Nada {#tone-mapping}
Pemetaan nada adalah operasi yang memetakan ulang nilai HDR ke rentang `[0, 1]`.
Jika Anda tidak memakainya (atau memilih `Tidak ada`), setiap komponen warna yang lebih dari 1 akan terpotong.
Variasi warna apa pun di atas rentang ini akan hilang.

* `Tidak ada/Netral/Agx/ACES` - tonemapper yang dipakai. `Tidak ada` tidak melakukan pemetaan ulang (tetapi kontrol lainnya tetap berfungsi). Opsi lainnya mirip dengan memilih jenis film yang berbeda: masing-masing menangani nilai dan warna yang terlalu terang dengan cara berbeda. Ini topik yang sangat dalam, cari tentang tone mapping, Agx, ACES untuk info lebih lanjut!
* `Eksposur` - kecerahan keseluruhan gambar, mirip dengan mengatur apertur pada kamera. Ini bisa menjadi cara cepat untuk mencerahkan atau menggelapkan gambar secara keseluruhan.
* `Kejenuhan` - kekuatan warna. 1 berarti netral, 0 berarti monokrom, nilai di atas 1 semakin jenuh.
* `Kontras` - Membuat bagian gelap lebih gelap dan bagian terang lebih terang. Gunakan dengan hati-hati, nilai yang tinggi bisa memunculkan artefak.

Perhatikan bahwa dengan `Pemetaan Nada` dinonaktifkan, beberapa detail menghilang karena pikselnya terlalu terang.

| Pemetaan Nada mati          | Pemetaan Nada aktif        |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Pemetaan nada bisa memperkuat efek pencahayaan global. Jika Anda menurunkan intensitas peta lingkungan dan menaikkan sumber cahaya utama, Anda bisa menaikkan `Eksposur` pemetaan nada untuk melihat lebih banyak efek cahaya pantulan.
:::

## ![](/icons/postprocess_tone_curve.webp) Grading warna {#color-grading}
Mirip dengan alat kurva di Photoshop, fitur ini memungkinkan Anda mengatur keseimbangan dan sebaran warna dalam gambar. Kontrol `Utama` memengaruhi keseimbangan warna secara keseluruhan, sedangkan kontrol `Merah`/`Hijau`/`Biru` memungkinkan pengaturan yang lebih halus. 

| Grading warna mati            | Grading warna aktif          |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Kelengkungan {#curvature}
Mendeteksi tempat-tempat yang kelengkungannya berubah dengan cepat, lalu memberi warna pada area tersebut.

* `Faktor` - intensitas keseluruhan efek
* `Tonjolan` - seberapa banyak perubahan cembung yang tajam akan dideteksi dan diberi warna yang dipilih (putih secara bawaan)
* `Rongga` - seberapa banyak perubahan cekung yang akan dideteksi dan diberi warna yang dipilih (hitam secara bawaan)
* `Ketebalan` - seberapa lebar tepi yang terdeteksi.

Di sebelah `Tonjolan` dan `Rongga`, sebuah kotak warna memilih warnanya, dan sebuah tombol kecil memilih bagaimana warna itu dipadukan dengan gambar.


| Kelengkungan mati                | Kelengkungan aktif             |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberasi Kromatik {#chromatic-aberration}
Menyimulasikan artefak lensa berupa cahaya yang terurai di sekitar tepi layar.

* `Kekuatan` - seberapa jauh bagian merah/hijau/biru gambar terpisah ke arah tepi layar

| Kromatik mati                 | Kromatik aktif               |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinyet {#vignette}
Menyimulasikan artefak lensa dengan menggelapkan tepi layar.

* `Ukuran` - Ukuran elips terbalik yang diletakkan di atas gambar
* `Kekerasan` - Seberapa buram atau tajam elips itu dipadukan di atas gambar.
* `Warna rona` - Warna vinyet, hitam secara bawaan.


| Vinyet mati                     | Vinyet aktif                   |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Butir {#grain}
Menambahkan efek butiran, yang bisa membantu gambar terlihat sedikit kurang artifisial.

* `Kekuatan` - jumlah butiran/noise yang ditambahkan ke gambar.


| Butir mati                   | Butir aktif                |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Ketajaman {#sharpness}
Efek penajaman yang mirip dengan yang ada di Photoshop atau aplikasi pengolah foto.

* `Kekuatan` - jumlah penajaman yang diterapkan pada gambar.


| Ketajaman mati                 | Ketajaman aktif              |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Seni Piksel {#pixel-art}
Menyimulasikan seni piksel game retro. Efek ini menimpa [Resolusi render](#resolution-multiplier).

* `Penggeser` - ukuran piksel
* `Izinkan pengambilan sampel bingkai` - jika muncul banyak piksel hitam, coba aktifkan opsi ini. Tanpa opsi ini, efek seni piksel mematikan [pengambilan sampel frame](#max-frame-sampling).

| Piksel mati                 | Piksel aktif               |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Garis pindai {#scanline}
Menyimulasikan tampilan monitor CRT lama.

* `Faktor` - kekuatan garis
* `Jarak` - ukuran garis

| Garis pindai mati              | Garis pindai aktif            |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

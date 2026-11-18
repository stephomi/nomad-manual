# ![](/icons/postprocess.webp) Pemprosesan Pasca {#post-process}

Menu ini mengawal banyak aspek Nomad yang mempengaruhi rupa hasil pemaparan.

![](/images/postprocess_overview_drac.webp)

Menggunakan pemprosesan pasca boleh mengubah rupa akhir adegan anda dengan ketara.

![](/images/postprocess_overview.webp)
*Adegan yang sama sebelum dan selepas pemprosesan pasca, tanpa lampu tambahan atau perubahan bahan.*

Pemprosesan pasca boleh menjejaskan prestasi dengan banyak, bergantung pada peranti anda.
Terdapat kotak semak global `Pemprosesan Pasca` untuk menyahdayakan semua pemprosesan pasca, supaya anda boleh kembali memahat/memodel dengan pantas tanpa kehilangan pratetap anda.
Untuk pemaparan PBR, [Oklusi ambien](#ambient-occlusion-ssao), [Pantulan](#reflection-ssr) dan [Pemetaan Nada](#tone-mapping) patut didayakan.

Walau bagaimanapun, selalunya anda mahu pemprosesan pasca dinyahdayakan semasa memahat, supaya anda boleh menumpukan perhatian pada bentuk itu sendiri dan bukannya pemaparan.


## Kualiti {#quality}

![](/images/postprocess_quality.webp)

Pilihan ini meningkatkan kualiti pemaparan, dengan mengorbankan prestasi.

### Sampel Bingkai Maksimum {#max-frame-sampling}
Nomad mengira sejumlah pemprosesan pasca untuk pemaparan satu bingkai, yang mungkin kelihatan berhingar. Kawalan ini menentukan berapa banyak bingkai yang akan dipaparkan, kemudian dicampurkan bersama untuk membuang kebanyakan artifak hingar. Sesetengah kesan tidak memerlukan sampel tambahan (contohnya penggredan warna), manakala kesan lain seperti bayang lembut dan pencahayaan global boleh memerlukan ratusan sampel untuk bebas daripada hingar. 

Dalam paparan, ini dapat dilihat setiap kali Nomad dibiarkan: kualiti imej akan diperhalusi secara beransur-ansur sehingga mencapai sampel maksimum, kemudian berhenti. Sebaik sahaja ia berhenti, Nomad tidak melakukan apa-apa, sekali gus menjimatkan bateri. Bilangan pengiraan ini juga digunakan dalam bahagian render [menu Fail](files) apabila 'eksport png' diklik.

Kotak semak di sebelah peluncur menghidupkan atau mematikan pensampelan bingkai.

### Resolusi Render {#resolution-multiplier}
Peluncur ini mengawal resolusi pemaparan. Nilai x1.0 bermakna pemaparan dilakukan pada resolusi piksel peranti. Nilai x0.5 memapar pada separuh resolusi, yang pantas tetapi berkualiti rendah. Nilai melebihi 1 memapar pada saiz yang lebih besar, kemudian mengecilkannya. Ini menghasilkan kualiti yang lebih tinggi dan kurang hingar, tetapi masa pemaparan yang lebih lama.

Ia memberi kesan besar pada prestasi, jadi cuba kekalkannya pada x1.25 atau lebih rendah. Nilai ini tidak disimpan dalam tetapan, dan kesan [Seni Piksel](#pixel-art) mengatasinya.

### ![](/icons/intensity.webp) Sampel maksimum {#max-samples}

Meningkatkan kualiti kesan pemprosesan pasca, dengan mengorbankan prestasi.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Dither piksel untuk mengurangkan artifak jalur (contohnya dalam kecerunan atau vinyet). Biasanya ini patut didayakan, tetapi boleh dimatikan untuk operasi tertentu (contohnya mengeksport peta kedalaman atau operasi khusus data yang lain).

### ![](/icons/denoise.webp) Pengurang hingar (oidn) {#oidn}

Menggunakan pengurang hingar pada imej sebaik sahaja semua bingkai dikumpulkan. Ini membolehkan anda menggunakan sampel yang jauh lebih rendah. Pengurangan hingar membebankan pemproses, jadi dayakannya hanya jika imej anda berhingar. Ia tidak tersedia pada semua peranti.

## Pelayar pratetap {#preset-browser}
![](/images/postprocess_presets.webp)
Mengklik imej di bawah tajuk `Pemprosesan Pasca` akan memaparkan koleksi pratetap pemprosesan pasca. Gunakan `Baru` untuk mencipta pratetap daripada tetapan semasa anda. Pratetap terbina dalam hanya boleh diklon: untuk mentakrifkan pratetap anda sendiri, pilih satu, klik `Klona`, dan buat perubahan. Apabila pratetap mempunyai perubahan yang belum disimpan, ia memaparkan `Perubahan belum disimpan!`; untuk menyimpan, klik imej pratetap, klik sekali lagi di dalam pelayar pratetap, dan pilih `Simpan`.

## Bar pintasan {#shortcut-bar}
Apabila pemprosesan pasca didayakan, bar di bahagian bawah menu menyenaraikan setiap kesan (`SSR`, `SSGI`, `SSAO`, `DoF`, `Pemekaran`...). Ketuk salah satu untuk melompat ke bahagiannya. Kesan yang dimatikan dikelabukan, jadi bar ini juga merupakan ringkasan pantas tentang apa yang dilakukan oleh pratetap semasa.

## ![](/icons/postprocess_ssr.webp) Pantulan (SSR) {#reflection-ssr}
Dengan pilihan ini, objek boleh memantulkan objek lain dalam adegan, selagi objek tersebut kelihatan pada skrin.
Jika anda mempunyai objek logam dan berkilat dalam adegan, pilihan ini mungkin patut digunakan.
Pilihan ini memerlukan mod shading [Cerah (PBR)](shading.md#pbr).


| SSR mati                   | SSR hidup                 |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Pencahayaan Global (SSGI) {#global-illumination-ssgi}

Pencahayaan global menyimulasikan cara cahaya melantun antara permukaan; contohnya, dinding merah akan memancarkan warna merah ke atas objek putih yang berdekatan. Ini boleh meningkatkan realisme pemaparan dengan sangat ketara apabila digunakan bersama oklusi ambien dan pantulan. Seperti pantulan, ia memerlukan mod shading [Cerah (PBR)](shading.md#pbr).

`Kekuatan` - Keamatan pencahayaan global. 



| SSGI mati                  | SSGI hidup                |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Sebuah lampu sorot berada di belakang sfera, dihalakan ke siling. Dengan SSGI dimatikan, hanya siling yang diterangi. Dengan SSGI dihidupkan, cahaya melantun dari siling ke dinding dan kemudian ke sfera._

## ![](/icons/postprocess_ssao.webp) Oklusi ambien (SSAO) {#ambient-occlusion-ssao}
Oklusi ambien akan menggelapkan kawasan yang kurang berpeluang dicapai cahaya (penjuru, dan sebagainya).
Kesan ini hanya bergantung pada geometri model.

* `Kekuatan` - Keamatan kesan.
* `Saiz` - Sejauh mana kesan itu tersebar.
* `Ketebalan` - Ketebalan kedalaman yang diandaikan bagi objek penghalang, sebagai peratusan daripada `Saiz`.
* `Tona` - Warna yang didarabkan ke dalam oklusi, digunakan untuk kesan kreatif.


| SSAO mati                   | SSAO hidup                 |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO paling ketara di kawasan yang diterangi terutamanya oleh cahaya persekitaran. Kawasan di bawah cahaya langsung yang kuat akan menerima kesan AO yang jauh lebih lemah.

:::

## ![](/icons/postprocess_dof.webp) Kedalaman Medan {#depth-of-field-dof}
Menambah kesan kabur pada kawasan di luar fokus.

Ketuk sahaja pada model anda untuk mengubah titik fokus.

* `Mod apertur` - Mengawal kekaburan dengan satu apertur kamera, dan bukannya dua peluncur kabur di bawah.
* `Apertur` (_mod apertur sahaja_) - Nombor f kanta, seperti pada kamera sebenar. Nilai yang lebih rendah membuka kanta dan menghasilkan lebih banyak kabur.
* `Kabur jauh` - Jumlah kekaburan yang digunakan di sebelah jauh titik fokus.
* `Kabur Berdekatan` - Jumlah kekaburan yang digunakan antara titik fokus dan kamera.


| DOF mati                  | DOF fokus pada gelang jauh  | DOF fokus pada gelang dekat |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Pemekaran {#bloom}
Pemekaran akan membuatkan kawasan terang dalam adegan anda bercahaya.

* `Keamatan` - kekuatan kesan.
* `Radius` - Sebaran kesan.
* `Ambang` - Seberapa terang piksel dalam adegan sebelum ia mula mekar. Pada 0 semuanya mekar; menetapkannya tinggi hanya membenarkan piksel paling terang untuk mekar.
* `Tona` - warna yang boleh ditambah pada pemekaran untuk kesan kreatif.

| Pemekaran mati               | Pemekaran dengan radius 0   | Pemekaran dengan radius 1   |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Pemetaan Nada {#tone-mapping}
Pemetaan Nada ialah operasi yang memetakan semula nilai HDR kepada julat `[0, 1]`.
Jika anda tidak menggunakannya (atau memilih `Tiada`), sebarang komponen warna yang melebihi 1 akan dipotong.
Sebarang variasi warna di atas julat ini akan hilang.

* `Tiada/Neutral/Agx/ACES` - pemeta nada yang hendak digunakan. `Tiada` tidak melakukan pemetaan semula (tetapi kawalan lain masih berfungsi). Pilihan lain sama seperti memilih jenis filem yang berbeza: masing-masing mengendalikan nilai dan warna yang terlebih dedah dengan cara yang berbeza. Ini topik yang sangat mendalam; cari maklumat tentang pemetaan nada, Agx dan ACES untuk mengetahui lebih lanjut!
* `Pendedahan` - kecerahan keseluruhan imej, sama seperti melaraskan apertur pada kamera. Ini boleh menjadi cara pantas untuk mencerahkan atau menggelapkan imej secara global.
* `Ketepuan` - kekuatan warna. 1 ialah neutral, 0 ialah monokrom, nilai melebihi 1 semakin tepu.
* `Kontras` - Menjadikan bahagian gelap lebih gelap dan bahagian terang lebih terang. Gunakan dengan berhati-hati, kerana ia boleh menghasilkan artifak pada nilai yang tinggi.

Perhatikan bahawa apabila `Pemetaan Nada` dinyahdayakan, sesetengah butiran hilang kerana piksel terlalu terang.

| Pemetaan Nada mati          | Pemetaan Nada hidup        |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Pemetaan nada boleh menguatkan kesan pencahayaan global. Jika anda merendahkan keamatan peta persekitaran dan menaikkan sumber cahaya utama, anda boleh meningkatkan `Pendedahan` pemetaan nada untuk melihat lebih banyak kesan cahaya lantunan.
:::

## ![](/icons/postprocess_tone_curve.webp) Penggredan warna {#color-grading}
Sama seperti alat lengkung dalam Photoshop, ini membolehkan anda mengawal keseimbangan dan taburan warna dalam imej. Kawalan `Utama` mempengaruhi keseluruhan keseimbangan warna, manakala kawalan `Merah`/`Hijau`/`Biru` membolehkan kawalan yang lebih halus. 

| Penggredan warna mati         | Penggredan warna hidup       |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Kelengkungan {#curvature}
Mengesan kawasan yang mempunyai perubahan kelengkungan yang mendadak, dan menggunakan warna pada kawasan tersebut.

* `Faktor` - keamatan keseluruhan kesan
* `Benjolan` - sejauh mana ia mengesan perubahan cembung yang tajam, dan meletakkan warna yang dipilih di situ (putih secara lalai)
* `Rongga` - sejauh mana ia mengesan perubahan cekung, dan meletakkan warna yang dipilih di situ (hitam secara lalai)
* `Ketebalan` - selebar mana tepi yang dikesan.

Di sebelah `Benjolan` dan `Rongga`, petak warna memilih warna, dan butang kecil memilih cara warna itu bercampur dengan imej.


| Kelengkungan mati                | Kelengkungan hidup             |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberasi Kromatik {#chromatic-aberration}
Menyimulasikan artifak kanta, iaitu cahaya yang terurai di sekitar tepi skrin.

* `Kekuatan` - sejauh mana bahagian merah/hijau/biru imej terpisah ke arah tepi skrin

| Kromatik mati                 | Kromatik hidup               |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinyet {#vignette}
Menyimulasikan artifak kanta dengan menggelapkan tepi skrin.

* `Saiz` - Saiz elips songsang yang diletakkan di atas imej
* `Kekerasan` - Sejauh mana kabur atau tajamnya elips itu dicampurkan di atas imej.
* `Tona` - Warna vinyet, hitam secara lalai.


| Vinyet mati                     | Vinyet hidup                   |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Bijian {#grain}
Menambah kesan bijian, yang boleh membantu menjadikan imej kurang kelihatan tiruan.

* `Kekuatan` - jumlah bijian/hingar yang ditambah pada imej.


| Bijian mati                  | Bijian hidup               |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Ketajaman {#sharpness}
Kesan penajaman yang serupa dengan yang terdapat dalam Photoshop atau aplikasi pemprosesan foto.

* `Kekuatan` - jumlah penajaman yang digunakan pada imej.


| Ketajaman mati                 | Ketajaman hidup              |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Seni Piksel {#pixel-art}
Menyimulasikan seni piksel permainan retro. Kesan ini mengatasi [Resolusi Render](#resolution-multiplier).

* `Peluncur` - saiz piksel
* `Benarkan pensampelan bingkai` - jika anda mendapat banyak piksel hitam, cuba hidupkan pilihan ini. Tanpanya, kesan seni piksel mematikan [pensampelan bingkai](#max-frame-sampling).

| Piksel mati                 | Piksel hidup               |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Garis Imbas {#scanline}
Menyimulasikan rupa monitor CRT lama.

* `Faktor` - kekuatan garisan
* `Jarak` - saiz garisan

| Garis Imbas mati               | Garis Imbas hidup             |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

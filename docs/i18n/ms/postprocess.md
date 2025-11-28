# ![](/icons/postprocess.webp) Pascasusai {#post-process}

Menu ini mengawal banyak aspek Nomad yang mempengaruhi rupa render.

![](/images/postprocess_overview_drac.webp)

Menggunakan pascaproses boleh mengubah rupa akhir adegan anda dengan ketara.

![](/images/postprocess_overview.webp)
*Adegan yang sama sebelum dan selepas pascaproses, tanpa lampu tambahan atau perubahan bahan.*

Pascaproses boleh memberi impak besar kepada prestasi bergantung pada peranti anda.
Terdapat kotak semak global untuk menyahdayakan semua pascaproses, supaya anda boleh dengan cepat kembali ke pengukiran/pemodelan tanpa kehilangan pratetap anda.
Untuk rendering PBR, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) dan [Tone Mapping](#tone-mapping) patut diaktifkan.

Walau bagaimanapun, kebanyakan masa anda mahu pascaproses dinyahdayakan ketika mengukir, supaya anda boleh fokus pada bentuk render itu sendiri.


## Kualiti {#quality}

![](/images/postprocess_quality.webp)
### Pensampelan bingkai maksimum {#max-frame-sampling}
Nomad akan mengira sejumlah pascaproses untuk satu render bingkai, yang boleh kelihatan berhingar. Kawalan ini menentukan berapa banyak bingkai akan dirender, kemudian digabungkan untuk menghapuskan kebanyakan artifak hingar. Sesetengah kesan tidak memerlukan sampel tambahan (cth gred warna), manakala yang lain seperti pencahayaan global boleh memerlukan ratusan sampel untuk bebas hingar. 

Dalam viewport ini boleh dilihat apabila Nomad dibiarkan sahaja, kualiti imej akan diperhalusi secara beransur-ansur sehingga ke sampel maksimum, kemudian berhenti. Bilangan pengiraan ini juga digunakan dalam bahagian render menu [Files](files) apabila 'export png' diklik.

### Pengganda resolusi {#resolution-multiplier}
Gelangsar ini mengawal resolusi pascaproses. Nilai x1.0 bermaksud render dilakukan pada resolusi piksel peranti. Nilai x0.5 akan merender pada separuh resolusi, yang akan pantas tetapi berkualiti rendah. Nilai lebih besar daripada 1 akan merender pada saiz lebih besar, kemudian diskalakan turun. Ini menghasilkan kualiti lebih tinggi, kurang hingar, tetapi masa render lebih lama.

### Sampel maksimum {#max-samples}

Ini akan meningkatkan kualiti pascaproses, tetapi secara umum `Full resolution` akan memberi lebih banyak impak. 

### Penyahbising (oidn) {#oidn}

Gunakan penyahhingar pada imej. Ini membolehkan anda menggunakan sampel yang jauh lebih rendah. Ini hanya berfungsi jika `Full Resolution` diaktifkan. Perhatikan bahawa penyahhingaran berlaku selepas semua sampel dikira, dan boleh intensif kepada pemproses.

## Pelayar pratetap {#preset-browser}
![](/images/postprocess_presets.webp)
Mengklik pada imej akan memaparkan koleksi pratetap pascaproses. Untuk menentukan pratetap anda sendiri, pilih satu, klik 'clone', buat perubahan. Untuk menyimpan, klik imej pratetap, klik lagi di dalam pelayar pratetap, dan pilih 'save'.


## Pantulan (SSR) {#reflection-ssr}
Dengan pilihan ini, objek boleh memantulkan objek lain dalam adegan, selagi objek tersebut kelihatan pada skrin.
Jika anda mempunyai objek logam dan berkilat dalam adegan anda, maka pilihan ini mungkin patut digunakan.
Pilihan ini hanya berkesan dengan mod PBR.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Pencahayaan Sejagat (SSGI) {#global-illumination-ssgi}

Pencahayaan global mensimulasikan bagaimana cahaya melantun antara permukaan, cth dinding merah akan memancarkan merah ke objek putih berdekatan. Ini boleh meningkatkan realisme render dengan sangat apabila digunakan bersama ambient occlusion dan pantulan. 

`Strength` - Keamatan pencahayaan global. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Sebuah spotlight berada di belakang sfera, dihalakan ke siling. Dengan SSGI off, hanya siling yang diterangi. Dengan SSGI on, cahaya melantun dari siling ke dinding ke sfera._

## Lekukan Sekitar (SSAO) {#ambient-occlusion-ssao}
Ambient occlusion akan menggelapkan kawasan di mana cahaya kurang berpeluang sampai (sudut, dsb).
Kesan ini hanya bergantung pada geometri model.

* `Strength`- Keamatan kesan.
* `Size`- Sejauh mana kesan tersebar.
* `Curvature bias` - Sejauh mana kepekaan kesan berbanding variasi permukaan.
* `Color` - Satu ton yang didarabkan ke dalam occlusion, digunakan untuk kesan kreatif.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO akan paling kelihatan di kawasan yang diterangi terutamanya oleh cahaya persekitaran. Kawasan di bawah cahaya langsung yang kuat akan menerima kesan AO yang jauh lebih lemah.

:::

## Kedalaman Medan (DOF) {#depth-of-field-dof}
Tambah kesan kabur pada kawasan yang berada di luar fokus.

Hanya ketik pada model anda untuk menukar titik fokus.

* `Far blur` - Jumlah pengkaburan yang digunakan pada bahagian jauh dari titik fokus.
* `Near blur` - Jumlah pengkaburan yang digunakan antara titik fokus dan kamera.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Kembang cahaya {#bloom}
Bloom akan membuat kawasan terang dalam adegan anda bersinar.

* `Intensity` - kekuatan kesan.
* `Radius` - Penyebaran kesan.
* `Threshold` - Seberapa terang piksel perlu berada dalam adegan sebelum ia mula bloom. Menetapkan nilai ini rendah akan membuat segala-galanya bloom, menetapkannya tinggi akan membenarkan hanya piksel paling terang untuk bloom.
* `Color` - satu ton yang boleh ditambah pada bloom untuk kesan kreatif.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Pemetaan Ton {#tone-mapping}
Tone Mapping ialah operasi yang akan memetakan semula nilai HDR kepada julat `[0, 1]`.
Jika anda tidak menggunakannya (atau pilih `none`), sebarang komponen warna lebih tinggi daripada 1 akan dipotong.
Sebarang variasi warna di atas julat ini kemudian akan hilang.

* `None/Neutral/Agx/ACES` - pemetaan ton mana yang hendak digunakan. `None` tidak melakukan pemetaan semula (tetapi kawalan lain masih berfungsi). Pilihan lain adalah serupa dengan memilih stok filem yang berbeza, ia akan mengendalikan nilai dan warna terlebih dedah dengan cara yang berbeza. Ini adalah topik yang sangat mendalam, cari maklumat tentang tone mapping, Agx, ACES untuk maklumat lanjut!
* `Exposure` - kecerahan keseluruhan imej, serupa dengan melaras apertur pada kamera. Ini boleh menjadi cara pantas untuk mencerahkan atau menggelapkan imej secara global.
* `Saturation` - kekuatan warna. 1 adalah neutral, 0 adalah monokrom, nilai di atas 1 semakin tepu.
* `Contrast` - Menjadikan bahagian gelap lebih gelap dan bahagian terang lebih terang. Gunakan dengan berhati-hati, ia boleh memperkenalkan artifak pada nilai tinggi.

Perhatikan bahawa dengan `Tone Mapping` dinyahdayakan, beberapa butiran hilang kerana piksel terlalu terang.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping boleh meningkatkan kesan pencahayaan global. Jika anda menurunkan keamatan peta persekitaran, sumber cahaya utama dinaikkan, anda boleh meningkatkan `exposure` tone mapping untuk melihat lebih banyak kesan pantulan cahaya.
:::

## Penggredan Warna {#color-grading}
Serupa dengan alat curves dalam Photoshop, ini membolehkan anda mengawal imbangan dan taburan warna dalam imej. Kawalan `main` mempengaruhi keseluruhan imbangan warna, kawalan `red`/`green`/`blue` membenarkan kawalan halus. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Kelengkungan {#curvature}
Mengesan di mana terdapat perubahan kelengkungan yang pantas, dan gunakan warna pada kawasan tersebut.

* `Factor` - keamatan keseluruhan kesan
* `Bump` - sejauh mana ia akan mencari perubahan cembung tajam, dan meletakkan warna terpilih di sana (putih secara lalai)
* `Cavity` - sejauh mana ia akan mengesan perubahan cekung, dan meletakkan warna terpilih di sana (hitam secara lalai)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Aberasi Kromatik {#chromatic-aberration}
Mensimulasikan artifak kanta dengan cahaya yang diuraikan di sekeliling tepi skrin.

* `Strength` - sejauh mana bahagian merah/hijau/biru imej dipecahkan ke arah tepi skrin

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vinyet {#vignette}
Mensimulasikan artifak kanta dengan menggelapkan tepi skrin.

* `Size` - Saiz elips songsang yang diletakkan di atas imej
* `Hardness` - Sejauh mana kabur atau tajam elips itu dicampur di atas imej.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Biji bunyi {#grain}
Tambah kesan grain, ia boleh membantu menjadikan imej kelihatan kurang artifisial.

* `Strength` - jumlah grain/hingar yang ditambah pada imej.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Ketajaman {#sharpness}
Kesan menajamkan serupa dengan yang terdapat dalam Photoshop atau aplikasi pemprosesan foto.

* `Strength` - jumlah penajaman yang digunakan pada imej.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Seni Piksel {#pixel-art}
Mensimulasikan seni piksel permainan retro.

* `Slider` - saiz piksel
* `Allow frame sampling` - jika anda mendapat banyak piksel hitam, cuba hidupkan ini, yang akan mengetepikan pensampelan lalai.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Garisan Imbas {#scanline}
Mensimulasikan rupa monitor CRT lama.

* `Factor` - kekuatan garis
* `Spacing` - saiz garis

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Penditeran {#dithering}

Dither piksel untuk mengurangkan artifak banding. Biasanya ini patut diaktifkan, tetapi boleh dinyahdayakan untuk operasi khusus (cth mengeksport peta kedalaman atau operasi khusus data lain).
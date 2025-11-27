# ![](/icons/postprocess.webp) Post process 

Menu ini mengontrol banyak aspek Nomad yang memengaruhi tampilan hasil render.

![](/images/postprocess_overview_drac.webp)

Menggunakan post process dapat secara signifikan mengubah tampilan akhir scene Anda.

![](/images/postprocess_overview.webp)
*Scene yang sama sebelum dan sesudah post process, tanpa tambahan lampu atau perubahan material.*

Post process dapat berdampak besar pada performa tergantung perangkat Anda.
Ada sebuah checkbox global untuk menonaktifkan semua postprocess, sehingga Anda bisa dengan cepat kembali ke sculpting/modeling tanpa kehilangan preset Anda.
Untuk rendering PBR, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) dan [Tone Mapping](#tone-mapping) sebaiknya diaktifkan.

Namun, sebagian besar waktu Anda ingin post process dimatikan saat sedang sculpting, agar bisa fokus pada bentuk dari hasil render itu sendiri.


## Quality

![](/images/postprocess_quality.webp)
### Max frame sampling
Nomad akan menghitung sejumlah post process untuk satu frame render, yang bisa terlihat berisik (noisy). Kontrol ini menentukan berapa banyak frame yang akan dirender, lalu dibaurkan (blend) bersama untuk menghilangkan sebagian besar artefak noise. Beberapa efek tidak memerlukan sampel ekstra (misalnya color grading), sementara yang lain seperti global illumination bisa memerlukan ratusan sampel agar bebas noise. 

Di viewport hal ini bisa terlihat ketika Nomad dibiarkan, kualitas gambar akan perlahan membaik hingga mencapai jumlah sampel maksimum, lalu berhenti. Jumlah perhitungan ini juga digunakan di bagian render pada [Files menu](files) ketika 'export png' diklik.

### Resolution multiplier
Slider ini mengontrol resolusi post process. Nilai x1.0 berarti render dilakukan pada resolusi piksel perangkat. Nilai x0.5 akan merender pada setengah resolusi, yang akan cepat tetapi berkualitas rendah. Nilai lebih besar dari 1 akan merender pada ukuran lebih besar, lalu diskalakan turun. Ini menghasilkan kualitas lebih tinggi, noise lebih sedikit, tetapi waktu render lebih lama.

### Max samples

Ini akan meningkatkan kualitas post process, tetapi umumnya `Full resolution` akan memiliki dampak lebih besar. 

### Full resolution
Saat diaktifkan akan memaksa resolution multiplier ke x1.0

### Denoiser (oidn)

Menerapkan denoiser pada gambar. Ini memungkinkan Anda menggunakan jumlah sampel yang jauh lebih rendah. Ini hanya berfungsi jika `Full Resolution` diaktifkan. Perlu dicatat bahwa denoising terjadi setelah semua sampel dihitung, dan bisa cukup membebani prosesor.

## Preset browser
![](/images/postprocess_presets.webp)
Mengklik gambar akan menampilkan kumpulan preset post process. Untuk membuat preset sendiri, pilih salah satu, klik 'clone', lalu lakukan perubahan. Untuk menyimpan, klik gambar preset, klik lagi di dalam preset browser, dan pilih 'save'.


## Reflection (SSR)
Dengan opsi ini, objek dapat memantulkan objek lain di dalam scene, selama objek tersebut terlihat di layar.
Jika Anda memiliki objek metalik dan mengkilap di scene Anda, maka opsi ini sebaiknya digunakan.
Opsi ini hanya efektif pada mode PBR.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Global illumination mensimulasikan bagaimana cahaya memantul antar permukaan, misalnya dinding merah akan memantulkan warna merah ke objek putih di dekatnya. Ini dapat sangat meningkatkan realisme render ketika digunakan bersama ambient occlusion dan reflections. 

`Strength` - Intensitas global illumination. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Sebuah spotlight berada di belakang bola, diarahkan ke langit-langit. Dengan SSGI off, hanya langit-langit yang terkena cahaya. Dengan SSGI on, cahaya memantul dari langit-langit ke dinding lalu ke bola._

## Ambient Occlusion (SSAO)
Ambient occlusion akan menggelapkan area di mana cahaya memiliki kemungkinan lebih kecil untuk mencapai (sudut, dll).
Efek ini hanya bergantung pada geometri model.

* `Strength`- Intensitas efek.
* `Size`- Seberapa luas penyebaran efek.
* `Curvature bias` - Seberapa sensitif efek terhadap variasi permukaan.
* `Color` - Tint yang dikalikan ke dalam occlusion, digunakan untuk efek kreatif.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO akan paling terlihat di area yang terutama diterangi oleh cahaya environment. Area yang berada di bawah cahaya langsung yang kuat akan menerima efek AO yang jauh lebih lemah.

:::

## Depth of Field (DOF)
Menambahkan efek blur pada area yang berada di luar fokus.

Cukup ketuk pada model Anda untuk mengubah titik fokus.

* `Far blur` - Jumlah blur yang diterapkan pada sisi jauh dari titik fokus.
* `Near blur` - Jumlah blur yang diterapkan antara titik fokus dan kamera.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom
Bloom akan membuat area terang di scene Anda tampak menyala (glow).

* `Intensity` - kekuatan efek.
* `Radius` - Luas penyebaran efek.
* `Threshold` - Seberapa terang piksel di scene sebelum mulai mengalami bloom. Mengatur nilai ini rendah akan membuat semuanya bloom, mengaturnya tinggi akan membuat hanya piksel paling terang yang bloom.
* `Color` - tint yang dapat ditambahkan ke bloom untuk efek kreatif.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone Mapping
Tone Mapping adalah operasi yang akan memetakan ulang nilai HDR ke rentang `[0, 1]`.
Jika Anda tidak menggunakannya (atau memilih `none`), komponen warna apa pun yang lebih tinggi dari 1 akan terpotong.
Setiap variasi warna di atas rentang ini kemudian akan hilang.

* `None/Neutral/Agx/ACES` - tonemapper yang digunakan. `None` tidak melakukan pemetaan ulang (tetapi kontrol lainnya tetap berfungsi). Opsi lainnya mirip dengan memilih jenis film yang berbeda, mereka akan menangani nilai dan warna yang overexposed dengan cara berbeda. Ini adalah topik yang sangat dalam, cari informasi tentang tone mapping, Agx, ACES untuk detail lebih lanjut!
* `Exposure` - kecerahan keseluruhan gambar, mirip dengan mengatur aperture pada kamera. Ini bisa menjadi cara cepat untuk mencerahkan atau menggelapkan gambar secara global.
* `Saturation` - kekuatan warna. 1 adalah netral, 0 adalah monokrom, nilai di atas 1 semakin jenuh.
* `Contrast` - Membuat area gelap lebih gelap dan area terang lebih terang. Gunakan dengan hati-hati, karena dapat menimbulkan artefak pada nilai tinggi.

Perhatikan bahwa dengan `Tone Mapping` dimatikan, beberapa detail menghilang karena piksel terlalu terang.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping dapat meningkatkan efek global illumination. Jika Anda menurunkan intensitas environment map, menaikkan sumber cahaya utama, lalu meningkatkan `exposure` pada tone mapping, Anda dapat melihat lebih banyak efek pantulan cahaya (bounce lighting).
:::

## Color Grading
Mirip dengan tool curves di Photoshop, ini memungkinkan Anda mengontrol keseimbangan dan distribusi warna pada gambar. Kontrol `main` memengaruhi keseimbangan warna keseluruhan, sedangkan `red`/`green`/`blue` memungkinkan kontrol yang lebih halus. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Mendeteksi area di mana terdapat perubahan kurvatur yang cepat, dan menerapkan warna pada area tersebut.

* `Factor` - intensitas keseluruhan efek
* `Bump` - seberapa kuat ia akan mencari perubahan cembung tajam, dan menempatkan warna yang dipilih di sana (putih secara default)
* `Cavity` - seberapa kuat ia akan mendeteksi perubahan cekung, dan menempatkan warna yang dipilih di sana (hitam secara default)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatic Aberration
Mensimulasikan artefak lensa dengan cahaya yang terurai di sekitar tepi layar.

* `Strength` - seberapa jauh bagian merah/hijau/biru dari gambar terpisah ke arah tepi layar

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignette
Mensimulasikan artefak lensa dengan menggelapkan tepi layar.

* `Size` - Ukuran elips terbalik yang ditempatkan di atas gambar
* `Hardness` - Seberapa blur atau tajam elips tersebut dicampurkan di atas gambar.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Menambahkan efek grain, yang dapat membantu membuat gambar terasa sedikit kurang artifisial.

* `Strength` - jumlah grain/noise yang ditambahkan ke gambar.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Sharpness
Efek penajaman mirip dengan yang ada di Photoshop atau aplikasi pemrosesan foto.

* `Strength` - jumlah penajaman yang diterapkan pada gambar.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Mensimulasikan pixel art game retro.

* `Slider` - ukuran piksel
* `Allow frame sampling` - jika Anda mendapatkan banyak piksel hitam, coba aktifkan ini, yang akan menimpa sampling default.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Mensimulasikan tampilan monitor CRT lama.

* `Factor` - kekuatan garis
* `Spacing` - ukuran garis

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering

Mendither piksel untuk mengurangi artefak banding. Biasanya ini sebaiknya diaktifkan, tetapi bisa dimatikan untuk operasi tertentu (misalnya mengekspor depth map atau operasi spesifik data lainnya).

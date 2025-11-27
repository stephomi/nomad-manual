# ![](/icons/paint.webp) Mengecat  

Kawal warna, kekasaran, kemetalan sapuan cat, benarkan pengisian menyeluruh (flood fill) atribut cat, dan cara alat cat berinteraksi dengan lapisan, topeng (mask), serta pemilihan tersembunyi.

![](/images/paint_overview.webp)  

## Gambaran keseluruhan

Nomad menggunakan pengecatan verteks PBR. Apa maksudnya?

### PBR
PBR, atau Physically Based Rendering ialah teknik grafik komputer yang popular untuk filem, televisyen, permainan dan mudah alih. Dengan memadankan cahaya pada sifat fizikal, dan mentakrifkan permukaan melalui warna, kekasaran, kemetalan, pelbagai rupa fotorealistik boleh dicapai.

### Pengecatan verteks

Pengecatan verteks bermaksud maklumat cat disimpan dalam verteks model, bukannya dalam tekstur. Oleh kerana Nomad boleh mengendalikan model dengan ratusan ribu, malah berjuta-juta verteks, model anda sepatutnya boleh mempunyai cat permukaan yang sangat terperinci; jika anda boleh mengukir perincian itu, anda juga boleh mengecat perincian tersebut.

Ini juga bermakna mengecat dalam Nomad tidak memerlukan pemetaan UV, yang selalunya proses perlahan dan teknikal dalam aplikasi 3D lain. Banyak aplikasi 3D lain tidak menyokong kiraan verteks tinggi seperti Nomad, namun Nomad juga mempunyai alatan pembakaran tekstur (texture baking) dan pengurangan poligon (decimation) yang baik untuk membantu.

### Tekstur

Nomad menyokong tekstur, tetapi ia perlu wujud dalam model yang diimport, atau melalui pembakaran pengecatan verteks ke tekstur. 

Tekstur hanyalah imej, tetapi dalam konteks 3D ia biasanya merujuk kepada imej yang ditetapkan pada objek.
Untuk membalut imej di sekeliling model, model memerlukan koordinat tekstur (UV).

Nomad boleh mengiranya [secara automatik](topology.md#uv-unwrap) tetapi anda tidak mempunyai banyak kawalan ke atas kualiti keseluruhan.

::: tip
Salah satu contoh aliran kerja:
- Ukir dalam Nomad, kemudian lakukan [UV unwrap](topology.md#uv-unwrap)
- Jika anda sudah mula mengecat dalam Nomad anda boleh [pindahkan pengecatan verteks ke tekstur](topology.md#bake-vertex-colors-to-texture)
- Eksport ke Procreate
- Tekstur dalam Procreate
- Eksport kembali ke Nomad untuk tujuan rendering
:::

Itu gambaran keseluruhan, sekarang mari terokai bahagian-bahagian menu mengecat:


## Pengecatan strok
![](/images/paint_intensity.webp)  

Aktifkan pengecatan untuk alat ini, berguna jika anda perlu mengukir dan mengecat pada masa yang sama.

Untuk alat di mana mengecat ialah fungsi utama (cth Paint, Smudge, Mask), kotak semak ini tidak wujud.

### Keamatan cat

Gelangsar untuk membolehkan anda menggunakan keamatan berbeza daripada keamatan alat utama.

Kotak semak `Alpha`, `Falloff` dan `Randomize` menentukan sama ada ciri tersebut akan mempengaruhi pengecatan. Contohnya anda boleh mengaktifkan randomize untuk alat clay, tetapi warna tidak akan dirandomkan.


## Bahan
![](/images/paint_material.webp) 

Ikon pertama ialah bentuk pratonton bahan. Seret pada pratonton bahan 3D untuk memutarkannya. 

Ikon kedua ialah pratonton sapuan cat dengan pilihan alpha dan falloff yang dipilih.

Butang pratonton di sebelah tajuk Material membolehkan anda bertukar antara none, Material atau Triplanar. Ini menentukan apa yang akan berlaku apabila anda menukar sifat cat secara interaktif:

* `None` - Tiada pratonton akan dipaparkan pada model apabila anda melaras sifat
* `Material` - Nilai bahan akan dipratonton pada objek apabila anda melaras sifat. Jika anda menggunakan tekstur dan model mempunyai UV, UV tersebut akan digunakan.
* `Triplanar` - Bahan akan dipratonton sebagai unjuran Triplanar. 

Pipet boleh digunakan untuk mengambil sampel semua sifat daripada objek dalam adegan anda.

## Praset bahan
Mengetik bentuk pratonton 3D akan memaparkan menu praset bahan, ini boleh diklon untuk mentakrifkan praset anda sendiri.

![](/images/paint_presets.webp) 

Togol `Embed Textures` dan `Alpha` apabila diaktifkan akan menyimpan sebarang tekstur yang digunakan oleh bahan ini di dalam praset. Ini diterangkan dengan lebih lanjut di bawah.

## Gelangsar PBR
![](/images/paint_sliders.webp) 

Pengecatan [PBR](shading.md#pbr) menggunakan 4 saluran:
- `Color` Warna yang akan dicat. Pipet boleh digunakan untuk memilih warna daripada bahagian lain model, atau daripada imej rujukan.
- `Roughness` Menunjukkan betapa "kasar" atau "licin" sesuatu permukaan. Nilai rendah untuk kekasaran bermakna pantulan akan tajam.
- `Metalness` Menunjukkan sama ada permukaan itu logam atau tidak. Nilai sepatutnya sama ada 0% atau 100% kebanyakan masa, nilai di antara sepatutnya luar biasa.
- `Opacity` Sejauh mana bahan boleh dilihat tembus. Secara teknikal ia bukan sebahagian daripada spesifikasi PBR, tetapi ia berguna dalam banyak situasi. 1 ialah legap sepenuhnya, 0 ialah lutsinar. Ambil perhatian bahawa kelegapan dan pembiasan (refraction) adalah perkara berbeza, pembiasan dalam Nomad dikendalikan melalui bahan pembiasan.

Jika anda memilih praset bahan, 3 saluran akan dicat serentak (opacity selalunya sengaja dikecualikan). Ini bermakna bukannya hanya mengecat 'merah', anda boleh mengecat 'logam merah kasar' atau 'plastik putih licin'.

Petak ialah slot tekstur, ketik untuk menggunakan tekstur bagi sifat tersebut dan bukannya nilai pepejal.

Ikon berus di sebelah gelangsar akan mengisi penuh (flood fill) sifat tersebut ke seluruh objek anda.

Kotak semak akan mengaktifkan atau menyahaktifkan sifat tertentu itu, jadi anda boleh hanya mengecat warna, atau hanya mengecat kekasaran dan kelegapan, sebagai contoh. 

Berikut beberapa contoh sifat kekasaran dan kemetalan berbeza:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Hanya warna disokong dalam mod [Matcap rendering](shading.md#matcap), kemetalan dan kekasaran diabaikan.
:::

::: tip
Apabila menggunakan tekstur untuk pengecatan PBR, selalunya berguna untuk bertukar kepada alat seperti `Stamp`, atau gunakan menu stroke untuk menggunakan mod selain dot, yang boleh mengheret (smear) tekstur.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Anda mungkin mahu menghidupkan `Smooth Shading` [secara global](settings.md#smooth-shading) atau [per-objek](material.md#smooth-shading) jika anda mengecat permukaan logam pada objek dengan kiraan poligon rendah.
:::

## Cat semua

![](/images/paint_paint_all.webp)

Gunakan bahan semasa pada objek, sama ada dalam mod standard dengan 'Paint All', atau sebagai unjuran Triplanar.

Kotak semak di sebelah gelangsar color/metalness/roughness/opacity akan diambil kira, sebarang sifat yang dinyahaktif tidak akan diisi.

Butang tambahan mengawal cara paint all boleh dipengaruhi lagi:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Kawasan bertopeng tidak akan terjejas.        |
| ![](/icons/tool_hide.webp) | Kawasan tersembunyi tidak akan terjejas.      |
| ![](/icons/opacity.webp)   | guna faktor pengecatan alat di atas.          |
| ![](/icons/layer.webp)     | Kawasan tidak dicat pada lapisan tidak akan terjejas. |
| ![](/icons/triplanar.webp) | Penunjuk tetapan triplanar                    |
| ![](/icons/cog.webp)       | Buka tetapan Triplanar                        |

### Tetapan Triplanar
![](/images/paint_triplanar_settings.webp)

Serupa dengan [tetapan triplanar dalam menu bahan](material.md#triplanar), anda boleh mengawal pengadunan unjuran, pengjubinan (tiling) dan ofset. 

Gunakan kotak semak pratonton di bahagian atas menu ini untuk mengaktifkan pratonton berterusan semasa melaras nilai.

## Bahan global
Jika pilihan ini diaktifkan, bahan yang dipilih akan sama seperti alat lain. Ambil perhatian bahawa ia hanya mengambil kira tetapan roughness, metalness dan color.

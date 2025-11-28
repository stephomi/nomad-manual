# ![](/icons/paint.webp) Melukis {#painting}

Mengontrol warna, kekasaran, metalness dari sapuan cat, memungkinkan pengisian menyeluruh (flood fill) atribut cat, dan bagaimana alat cat berinteraksi dengan layer, mask, serta seleksi tersembunyi.

![](/images/paint_overview.webp)  

## Ikhtisar {#overview}

Nomad menggunakan pengecatan verteks PBR. Apa artinya ini?

### PBR {#pbr}
PBR, atau Physically Based Rendering adalah teknik grafis komputer populer untuk film, televisi, gim, dan mobile. Dengan mendasarkan cahaya pada properti fisik, dan mendefinisikan permukaan melalui warna, kekasaran, metalness, berbagai tampilan fotorealistik dapat dicapai.

### Melukis verteks {#vertex-painting}

Pengecatan verteks berarti informasi cat disimpan di verteks model, bukan di tekstur. Karena Nomad dapat menangani model dengan ratusan ribu, sering kali jutaan verteks, model Anda seharusnya dapat memiliki pengecatan permukaan yang sangat detail; jika Anda bisa memahat detailnya, Anda juga bisa mengecat detail tersebut.

Ini juga berarti bahwa pengecatan di Nomad tidak memerlukan pemetaan UV, yang sering kali merupakan proses lambat dan teknis di aplikasi 3D lain. Banyak aplikasi 3D lain tidak mendukung jumlah verteks tinggi seperti yang dapat dilakukan Nomad, namun Nomad juga memiliki alat baking tekstur dan decimation yang baik untuk membantu.

### Pemberian tekstur {#texturing}

Nomad mendukung tekstur, tetapi tekstur harus sudah ada di model yang diimpor, atau melalui baking pengecatan verteks ke tekstur. 

Tekstur hanyalah sebuah gambar, tetapi dalam konteks 3D biasanya mengacu pada gambar yang ditetapkan ke sebuah objek.
Untuk membungkus gambar di sekitar model, model memerlukan koordinat tekstur (UV).

Nomad dapat menghitung [koordinat tersebut secara otomatis](topology.md#uv-unwrap) tetapi Anda tidak memiliki banyak kendali atas kualitas keseluruhan.

::: tip
Salah satu contoh alur kerja:
- Memahat di Nomad, lalu [UV unwrap](topology.md#uv-unwrap)
- Jika Anda sudah mulai mengecat di Nomad Anda dapat [mentransfer pengecatan verteks ke tekstur](topology.md#bake-vertex-colors-to-texture)
- Ekspor ke Procreate
- Melakukan teksturing di Procreate
- Ekspor kembali ke Nomad untuk keperluan rendering
:::

Itu ikhtisarnya, sekarang mari jelajahi bagian-bagian dari menu pengecatan:


## Melukis goresan {#stroke-painting}
![](/images/paint_intensity.webp)  

Mengaktifkan pengecatan untuk alat ini, berguna jika Anda perlu memahat dan mengecat pada saat yang sama.

Untuk alat di mana pengecatan adalah fungsi utama (misalnya Paint, Smudge, Mask), kotak centang ini tidak ada.

### Intensitas cat {#paint-intensity}

Slider untuk memungkinkan Anda menggunakan intensitas yang berbeda dari intensitas alat utama.

Kotak centang `Alpha`, `Falloff` dan `Randomize` menentukan apakah fitur-fitur tersebut akan memengaruhi pengecatan. Misalnya Anda dapat mengaktifkan randomize untuk alat clay, tetapi warna tidak akan diacak.

## Material {#material}
![](/images/paint_material.webp) 

Ikon pertama adalah bentuk pratinjau material. Menyeret pada pratinjau material 3D akan memutarnya. 

Ikon kedua adalah pratinjau sapuan cat dengan alpha dan falloff yang dipilih.

Tombol pratinjau di sebelah judul Material memungkinkan Anda beralih antara none, Material atau Triplanar. Ini menentukan apa yang akan terjadi ketika Anda mengubah properti cat secara interaktif:

* `None` - Tidak ada pratinjau yang akan ditampilkan pada model ketika Anda menyesuaikan properti
* `Material` - Nilai material akan dipratinjau pada objek ketika Anda menyesuaikan properti. Jika Anda menggunakan tekstur dan model memiliki UV, UV tersebut akan digunakan.
* `Triplanar` - Material akan dipratinjau sebagai proyeksi Triplanar. 

Eyedropper dapat digunakan untuk mengambil semua properti dari sebuah objek di dalam scene Anda.

## Preset material {#material-presets}
Mengetuk bentuk pratinjau 3D akan menampilkan menu preset material, preset ini dapat diklon untuk mendefinisikan preset Anda sendiri.

![](/images/paint_presets.webp) 

Toggel `Embed Textures` dan `Alpha` ketika diaktifkan akan menyimpan tekstur apa pun yang digunakan oleh material ini di dalam preset. Hal ini dijelaskan lebih lanjut di bawah.

## Penggeser PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Pengecatan [PBR](shading.md#pbr) menggunakan 4 kanal:
- `Color` Warna yang akan dicat. Eyedropper dapat digunakan untuk memilih warna dari bagian lain model, atau dari gambar referensi.
- `Roughness` Menentukan seberapa "kasar" atau "halus" suatu permukaan. Nilai rendah untuk roughness berarti pantulan akan tajam.
- `Metalness` Menentukan apakah permukaan bersifat metalik atau tidak. Nilainya sebaiknya 0% atau 100% sebagian besar waktu, nilai di antaranya sebaiknya hanya dalam kasus khusus.
- `Opacity` Seberapa banyak material dapat dilihat tembus pandang. Secara ketat bukan bagian dari spesifikasi PBR, tetapi berguna dalam banyak situasi. 1 sepenuhnya buram, 0 transparan. Perhatikan bahwa opacity dan refraksi adalah hal yang berbeda, refraksi di Nomad ditangani melalui material refraction. 

Jika Anda memilih preset material, 3 kanal akan dicat secara bersamaan (opacity sering kali sengaja dikecualikan). Ini berarti bahwa alih-alih hanya mengecat 'merah', Anda dapat mengecat 'logam merah kasar' atau 'plastik putih halus'.

Kotak persegi adalah slot tekstur, klik untuk menggunakan tekstur untuk properti tersebut alih-alih nilai solid.

Ikon kuas di sebelah slider akan melakukan flood fill properti tersebut ke seluruh objek Anda.

Kotak centang akan mengaktifkan atau menonaktifkan properti tertentu, sehingga Anda bisa hanya mengecat warna, atau hanya mengecat roughness dan opacity, misalnya. 

Berikut beberapa contoh properti roughness dan metalness yang berbeda:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Hanya warna yang didukung dalam mode [Matcap rendering](shading.md#matcap), metalness dan roughness diabaikan.
:::

::: tip
Saat menggunakan tekstur untuk pengecatan PBR, sering kali berguna untuk beralih ke alat seperti `Stamp`, atau menggunakan menu stroke untuk memakai mode selain dot, yang dapat mengoles (smear) tekstur.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Anda mungkin ingin menyalakan `Smooth Shading` [secara global](settings.md#smooth-shading) atau [per-objek](material.md#smooth-shading) jika Anda mengecat permukaan metalik pada objek dengan jumlah poligon rendah.
:::

## Cat semua {#paint-all}

![](/images/paint_paint_all.webp)

Menerapkan material saat ini ke objek, baik dalam mode standar dengan 'Paint All', atau sebagai proyeksi Triplanar.

Kotak centang di sebelah slider color/metalness/roughness/opacity akan dihormati, properti yang dinonaktifkan tidak akan diisi.

Tombol tambahan mengontrol bagaimana paint all dapat dipengaruhi lebih lanjut:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Area yang termask tidak akan terpengaruh.     |
| ![](/icons/tool_hide.webp) | Area tersembunyi tidak akan terpengaruh.      |
| ![](/icons/opacity.webp)   | gunakan faktor pengecatan alat di atas.       |
| ![](/icons/layer.webp)     | Area yang belum dicat pada layer tidak akan terpengaruh. |
| ![](/icons/triplanar.webp) | Indikator pengaturan triplanar                |
| ![](/icons/cog.webp)       | Membuka pengaturan Triplanar                  |

### Pengaturan triplanar {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Serupa dengan [pengaturan triplanar di menu material](material.md#triplanar), Anda dapat mengontrol blending proyeksi, tiling dan offset. 

Gunakan kotak centang pratinjau di bagian atas menu ini untuk mengaktifkan pratinjau persisten saat menyesuaikan nilai.

## Material global {#global-material}
Jika opsi ini diaktifkan, material yang dipilih akan sama dengan alat lainnya. Perhatikan bahwa ini hanya mempertimbangkan pengaturan roughness, metalness dan color.
# ![](/icons/paint.webp) Cat {#painting}

Kawal warna, kekasaran dan kemetalan sapuan cat, isi penuh atribut cat, dan tentukan cara alat cat berinteraksi dengan lapisan, topeng dan kawasan tersembunyi.

![](/images/paint_overview.webp)  

## Gambaran keseluruhan {#overview}

Nomad menggunakan pengecatan verteks PBR. Apakah maksudnya?

### PBR {#pbr}
PBR, atau Physically Based Rendering (pemaparan berasaskan fizik), ialah teknik grafik komputer yang popular untuk filem, televisyen, permainan dan peranti mudah alih. Dengan mendasarkan pencahayaan pada sifat fizikal, dan mentakrifkan permukaan melalui warna, kekasaran dan kemetalan, pelbagai rupa fotorealistik boleh dicapai.

### Pengecatan verteks {#vertex-painting}

Pengecatan verteks bermaksud maklumat cat disimpan dalam verteks model, bukan dalam tekstur. Oleh sebab Nomad boleh mengendalikan model dengan ratusan ribu, malah selalunya jutaan verteks, model anda boleh mempunyai cat permukaan yang sangat terperinci; jika anda boleh memahat butiran itu, anda juga boleh mengecatnya.

Ini juga bermakna mengecat dalam Nomad tidak memerlukan pemetaan UV, proses yang selalunya lambat dan teknikal dalam aplikasi 3d lain. Banyak aplikasi 3d lain tidak menyokong bilangan verteks setinggi Nomad, namun Nomad juga mempunyai alat yang baik untuk membantu: bake tekstur dan Kurangkan (decimate).

### Penteksturan {#texturing}

Nomad menyokong tekstur, tetapi tekstur mesti sudah ada dalam model yang diimport, atau dihasilkan dengan bake pengecatan verteks ke tekstur. 

Tekstur hanyalah sebuah imej, tetapi dalam konteks 3d ia biasanya merujuk kepada imej yang diberikan kepada sesuatu objek.
Untuk membalut imej di sekeliling model, model memerlukan koordinat tekstur (UV).

Nomad boleh [mengiranya secara automatik](topology.md#uv-unwrap) tetapi anda tidak mempunyai banyak kawalan terhadap kualiti keseluruhannya.

::: tip
Satu contoh aliran kerja:
- Pahat dalam Nomad, kemudian [buka balut UV](topology.md#uv-unwrap)
- Jika anda sudah mula mengecat dalam Nomad, anda boleh [memindahkan cat verteks ke tekstur](topology.md#bake-texture)
- Eksport ke Procreate
- Buat tekstur dalam Procreate
- Eksport semula ke Nomad untuk tujuan pemaparan
:::

Itulah gambaran keseluruhannya; sekarang mari kita terokai bahagian-bahagian menu cat:


## Pewarnaan Goresan {#stroke-painting}
![](/images/paint_intensity.webp)  

Dayakan pengecatan untuk alat ini, berguna jika anda perlu memahat dan mengecat pada masa yang sama. Apabila sesuatu alat boleh mengecat tetapi kotak semak ini dimatikan, ikon amaran di sebelah tajuk akan mengingatkan anda.

Bagi alat yang fungsi utamanya ialah mengecat (contohnya Lukis, Smudge, Topeng), kotak semak ini tidak wujud.

### ![](/icons/opacity.webp) Keamatan cat {#paint-intensity}

Peluncur yang membolehkan anda menggunakan keamatan yang berbeza daripada keamatan utama alat.

Butang peluncur di sebelahnya menambah peluncur keamatan cat pantas pada bar sisi, untuk alat yang memahat dan mengecat pada masa yang sama.

Butang `Alpha`, `Pengurangan` dan `Rawakkan keamatan` menentukan sama ada ciri-ciri tersebut akan mempengaruhi pengecatan. Contohnya, anda boleh mendayakan rawak untuk alat clay, tetapi warnanya tidak akan dirawakkan.

* `Alpha` - apabila dinyahdayakan, pengecatan mengabaikan alpha dan meliputi seluruh kawasan berus. Dengan alat VDM, butang ini digantikan dengan `Bahan cop`, yang menghidupkan atau mematikan bahan yang disimpan dalam cop.
* `Pengurangan` - apabila dinyahdayakan, pengecatan kekal pada keamatan penuh hingga ke tepi berus.
* `Rawakkan keamatan` - sama ada bahagian keamatan dalam perawak sapuan mempengaruhi pengecatan. Perawakan kedudukan, putaran dan skala sentiasa menggerakkan keseluruhan cop.

Pilihan ini diabaikan oleh [Cat semua](#paint-all), tetapi alpha digunakan oleh varian triplanarnya.

### ![](/icons/link.webp) Bahan global {#global-material}
Jika pilihan ini didayakan, bahan yang dipilih akan sama dengan alat-alat lain. Perhatikan bahawa ia hanya mengambil kira tetapan kekasaran, kemetalan dan warna. Nyahdayakannya untuk memberikan alat ini bahannya sendiri.


## Bahan {#material}
![](/images/paint_material.webp) 

Ikon pertama ialah bentuk pratonton bahan. Menyeret pada pratonton bahan 3d akan memutarnya. 

Ikon kedua ialah pratonton sapuan cat dengan pilihan alpha dan pengurangan yang dipilih.

### ![](/icons/falloff.webp) Lengkung {#curves}

Membuka penyunting lengkung untuk slot tekstur [peluncur PBR](#pbr-sliders). Ia memetakan semula nilai tekstur sebelum ia dicat, tanpa menyentuh fail imej. Ikon lengkung kecil pada slot tekstur memberitahu anda bahawa lengkungnya telah disunting.

### ![](/icons/cog.webp) Pilihan bahan {#material-options}

Butang `Bahan` di sebelah tajuk mengandungi dua tetapan.

`Pratonton paparan bahan` menentukan apa yang berlaku pada objek yang dipilih semasa anda mengubah peluncur warna, kekasaran, kemetalan, kelegapan dan keamatan:

* `Tiada` - Tiada pratonton dipaparkan pada model semasa anda melaraskan sifat
* `Bahan` - Nilai bahan dipratonton pada objek semasa anda melaraskan sifat.
* `Triplanar` - Bahan dipratonton sebagai unjuran Triplanar. 

Kotak semak warna, kekasaran, kemetalan dan kelegapan di bawahnya memilih saluran yang digantikan oleh [Pemilih bahan](#material-picker).

### ![](/icons/dropper.webp) Pemilih bahan {#material-picker}

Penitis mata memilih bahan di bawah kursor, daripada mana-mana objek dalam adegan anda. Hanya saluran yang ditanda dalam [Pilihan bahan](#material-options) akan digantikan.

## Pratetap Bahan {#material-presets}
Mengetuk bentuk pratonton 3d akan memaparkan menu pratetap bahan; pratetap ini boleh diklon untuk mentakrifkan pratetap anda sendiri.

![](/images/paint_presets.webp) 

Togol `Benamkan tekstur` menyimpan salinan tekstur yang digunakan oleh bahan ini di dalam pratetap. Tanpanya, pratetap hanya merujuk kepada tekstur dalam folder textures/ Nomad. Hidupkannya apabila anda mahu berkongsi pratetap bertekstur tanpa menghantar teksturnya secara berasingan.

`Sertakan Alfa` turut menyimpan alpha berus dalam pratetap bahan.

## Peluncur PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Pengecatan [PBR](shading.md#pbr) menggunakan 4 saluran:
- `Warna` Warna yang akan dicat. Penitis mata boleh digunakan untuk memilih warna daripada bahagian lain model, atau daripada imej rujukan.
- `Kekasaran` Menunjukkan sejauh mana permukaan itu "kasar" atau "licin". Nilai kekasaran yang rendah bermakna pantulan akan menjadi tajam.
- `Kemetalan` Hanya menunjukkan sama ada permukaan itu logam atau tidak. Nilainya biasanya sama ada 0% atau 100%; nilai di antaranya sepatutnya jarang digunakan.
- `Kelegapan` Sejauh mana bahan boleh dilihat tembus. Secara tegasnya ia bukan sebahagian daripada spesifikasi PBR, tetapi ia berguna dalam banyak situasi. 1 ialah legap sepenuhnya, 0 ialah lut sinar. Perhatikan bahawa kelegapan dan pembiasan ialah dua perkara berbeza; pembiasan dalam Nomad dikendalikan melalui bahan pembiasan. 

Jika anda memilih pratetap bahan, 3 saluran dicat serentak (kelegapan selalunya sengaja dikecualikan). Ini bermakna, daripada hanya mengecat 'merah', anda boleh mengecat 'logam merah yang kasar' atau 'plastik putih yang licin'.

Petak itu ialah slot tekstur; klik padanya untuk menggunakan tekstur bagi sifat tersebut dan bukannya nilai tetap. Tekstur warna mewarnai warna, manakala tekstur kekasaran, kemetalan atau kelegapan menggantikan nilai peluncur (labelnya dipotong garis untuk menunjukkannya). Bagi tekstur kelegapan, `Guna Alfa sebagai Nilai` membaca saluran alpha tekstur dan bukannya nilai skala kelabunya.

Dengan alat VDM, apabila cop mempunyai bahannya sendiri, slot tambahan memaparkannya di sebelah slot tekstur. Ketuk untuk menggunakan atau mengabaikan saluran cop tersebut.

Ikon berus di sebelah peluncur akan mengisi penuh sifat itu pada objek anda.

Kotak semak akan mendayakan atau menyahdayakan sifat tertentu itu, jadi anda boleh mengecat warna sahaja, atau hanya kekasaran dan kelegapan, sebagai contoh. 

Berikut ialah beberapa contoh sifat kekasaran dan kemetalan yang berbeza:

|                | Kemetalan 0%                      | Kemetalan 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Kekasaran 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Kekasaran 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Kekasaran 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Kekasaran dan kemetalan memerlukan mod shading [Cerah (PBR)](shading.md#pbr). Dalam mod [MatCap](shading.md#matcap) atau [Tanpa cahaya](shading.md#unlit), kedua-duanya diabaikan, dan menu memaparkan amaran.
:::

::: tip
Apabila menggunakan tekstur untuk pengecatan PBR, selalunya berguna untuk bertukar kepada alat seperti `Cap`, atau menggunakan menu sapuan untuk memilih mod selain titik, yang boleh mencomotkan tekstur.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Anda mungkin mahu menghidupkan `Shading licin` [secara global](settings.md#smooth-shading) atau [bagi setiap objek](material.md#smooth-shading) jika anda mengecat permukaan logam pada objek dengan bilangan poligon yang lebih rendah.
:::

## ![](/icons/paint.webp) Cat semua {#paint-all}

![](/images/paint_paint_all.webp)

Gunakan bahan semasa pada objek yang dipilih, sama ada dalam mod biasa dengan `Cat semua`, atau sebagai unjuran Triplanar dengan `Cat semua + Triplanar`. Varian triplanar tidak tersedia untuk primitif yang belum disahkan.

Kotak semak di sebelah peluncur warna/kemetalan/kekasaran/kelegapan dipatuhi; sebarang sifat yang dinyahdayakan tidak akan diisi.

Butang tambahan mengawal cara cat semua boleh dipengaruhi lagi. Kebanyakannya memaparkan peratusan, dan ia dikelabukan apabila ia tidak akan memberi kesan:

| Ikon                        | Penerangan                                    |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Kawasan bertopeng tidak akan terjejas.        |
| ![](/icons/tool_hide.webp) | Kawasan tersembunyi tidak akan terjejas.      |
| ![](/icons/opacity.webp)   | Gunakan faktor pengecatan alat di atas.       |
| ![](/icons/layer.webp)     | Kawasan lapisan yang tidak dicat tidak akan terjejas. |
| ![](/icons/triplanar.webp) | `Verteks`: varian triplanar juga mengofset permukaan dengan alpha, mengikut keamatan alat yang dipaparkan. |
| ![](/icons/cog.webp)       | Buka tetapan Triplanar                        |

### ![](/icons/cog.webp) Tetapan Triplanar {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Sama seperti [tetapan triplanar dalam menu bahan](material.md#triplanar), anda boleh mengawal pencampuran unjuran, jubinan dan ofset. 

Gunakan kotak semak pratonton di bahagian atas menu ini untuk mendayakan pratonton berterusan semasa melaraskan nilai.

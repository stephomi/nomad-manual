# ![](/icons/cog.webp) Tetapan {#reset-to-default}

Menu tetapan mengandungi banyak pilihan untuk mengawal rupa dan kelakuan Nomad.

![](/images/settings_overview.webp)

Barisan butang di bahagian atas menu membawa anda terus ke sesuatu bahagian: `Kursor`, `Petunjuk`, `Wayar`, `Grid`, `Dua belah`, `Garis luar`, `Sorotan`, `Snap kiub`, `Statistik`, `Pemegang-pemegang`, `Bentuk`, `Repeater` dan `Pelbagai resolusi`.

## Tetapan paparan {#display-settings}
Bahagian ini mengandungi pintasan pelancaran pantas bagi kebanyakan tetapan yang terdapat di bahagian bawah menu ini.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Shading licin {#smooth-shading}
Togol antara shading licin dan bersegi. Dalam mod bersegi, setiap poligon diberi shading secara berasingan, jadi anda dapat melihat topologi di bawahnya.
Shading bersegi boleh berguna semasa peringkat pemahatan, kemudian tukar kepada shading licin untuk pemaparan.

Menyahdayakan Shading licin meningkatkan prestasi sedikit.

### ![](/icons/outline.webp) Garis luar {#outline-quick}
Togol garis luar pada pilihan semasa anda.

Ini berguna untuk mendapatkan maklum balas visual tentang mesh yang sedang dipilih sekiranya [Gelapkan objek yang tidak dipilih](#darken-unselected-objects) dinyahdayakan.

Dari segi prestasi, menggunakan [Gelapkan objek yang tidak dipilih](#darken-unselected-objects) jauh lebih baik daripada menggunakan garis luar.

### ![](/icons/grid.webp) Grid {#grid-quick}
Togol grid latar belakang, berguna untuk memahami kedudukan dan skala objek.

### ![](/icons/culling.webp) Dua belah {#two-sided-quick}
Togol paparan poligon dua belah. Semua muka menghala ke arah tertentu.
Muka yang dianggap sebagai *muka belakang* ialah muka yang menghala "menjauhi" titik pandangan kamera.

Contohnya, sfera ringkas semasa permulaan mempunyai muka yang menghala ke luar.
Jika anda menggerakkan kamera ke dalam sfera, anda akan melihat bahagian belakang muka-muka ini.

Biasanya anda tidak sepatutnya melihat bahagian belakang muka, jadi mewarnakannya boleh membantu anda mengesan masalah yang berpotensi atau topologi yang salah.

Menyahdayakan pemaparan `Dua belah` boleh meningkatkan prestasi pemaparan sedikit.


### ![](/icons/wireframe.webp) Kerangka dawai {#wireframe-quick}
Togol tindihan kerangka dawai. 

Perhatikan bahawa mendayakan kerangka dawai akan menurunkan prestasi.

### ![](/icons/snap_cube.webp) Snap kiub {#snap-cube-quick}
Togol ikon pembantu di penjuru adegan, berguna untuk mengorientasikan diri anda dalam ruang dan bertukar dengan pantas antara pandangan depan/belakang/kiri/kanan/atas/bawah.

### ![](/icons/palette.webp) Tunjukkan cat {#show-painting}
Togol paparan cat. Apabila dimatikan, objek dipaparkan dengan bahan putih bukan logam, pada kekasaran 25%, dan bukannya catnya.

### ![](/icons/tool_hide.webp) Gunakan Sembunyi {#use-hide}
Togol mod sembunyi. Apabila dimatikan, ia masih ada, cuma dinyahaktifkan. Butang ini dinyahdayakan jika anda sedang menggunakan alat sembunyi.

### ![](/icons/shield.webp) Tunjukkan topeng {#show-mask}
Togol mod topeng. Apabila dimatikan, ia masih ada, cuma dinyahaktifkan. Tekan butang ini sekali lagi untuk mendayakannya semula.

Jika anda perlu menyembunyikan topeng DAN masih mahu ia aktif, gunakan warna topeng di bawah dan tetapkannya kepada putih. Ingat untuk menukarnya kembali kepada kelabu apabila selesai!

Perhatikan bahawa butang ini dinyahdayakan jika anda sedang menggunakan alat topeng. 

### ![](/icons/shield.webp) Topeng → Legap {#mask-opaque}
`Topeng → Legap` akan mengabaikan verteks lut sinar bagi topeng. Ini hanya berkaitan dengan kelegapan verteks dan tekstur; muka yang disembunyikan oleh "sembunyi" akan tetap tersembunyi. Ia hanya tersedia semasa `Tunjukkan topeng` dihidupkan.

### ![](/icons/bang.webp) Sorotan {#highlight-quick}
Togol kilatan sorotan pilihan. Apabila memilih objek, objek yang dipilih akan berkelip seketika selama 500 milisaat. Warna dan tempoh kilatan boleh disesuaikan di bawah.

### ![](/icons/list.webp) Statistik {#stats-quick}
Togol teks paparan status dalam paparan 3d. Ia memaparkan maklumat tentang memori sistem anda, jumlah verteks dalam adegan, dan bilangan verteks dalam pilihan semasa.

----- 

### ![](/icons/cube.webp) Gelapkan objek yang tidak dipilih {#darken-unselected-objects}
Objek yang tidak dipilih akan digelapkan supaya pilihan semasa lebih menonjol.

### ![](/icons/shield.webp) Topeng {#mask}
Warna yang digunakan untuk topeng, secara lalai kelabu sederhana, didarabkan dengan warna objek anda. Tetapkannya kepada putih untuk menjadikan topeng tidak kelihatan, tetapi ingat untuk menukarnya kembali kepada kelabu apabila selesai!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Bulat {#show-circle-while-sculpting}
Bila hendak memaparkan bulatan jejari berus:

* `Auto` - tunjukkan bulatan, tetapi sembunyikannya semasa anda memahat.
* `Tidak` - jangan sesekali tunjukkan bulatan.
* `Ya` - sentiasa tunjukkan bulatan, walaupun semasa memahat.

### Tunjukkan titik kecil {#show-small-dot}
Paparkan titik di tengah sapuan berus semasa memahat, atau apabila pangsi kamera diubah.

### Tunjukkan penstabil tali {#show-rope-stabilizer}
Lukis garisan untuk menunjukkan panjang tali apabila [Penstabil tali lambat](stroke.md#lazy-rope-stabilizer) aktif dalam tetapan sapuan.

### Tunjukkan petunjuk kecondongan {#show-roll-hint}
Tunjukkan panduan arah golek semasa anda menggunakan ikatan kekunci golek.

### ![](/icons/radius.webp) Saiz {#dot-size}
Saiz titik kecil.

### Warna {#cursor-colors}
Kursor berubah warna bergantung pada apa yang sedang anda lakukan: `Ukir`, `Latar belakang` (apabila berada di atas latar belakang), `Topeng`, `Lancar`, `Kamera` dan `Jari-jari`. Setiap warna boleh disesuaikan di sini.

## ![](/icons/cursor.webp) Petunjuk {#indicator}
![](/images/settings_indicator.webp)

Paparkan penunjuk visual untuk tutorial dan rakaman skrin. Tetapkannya kepada `Ya` untuk menghidupkannya (pada iOS terdapat juga pilihan `Auto`).

Butang `Jari`, `Stilus` dan `Tetikus` akan mendayakan paparan ikon apabila jenis input tersebut dikesan.

### Warna {#indicator-color}
Warna penunjuk.

### Saiz/Ikon/Bulatan {#indicator-shape}
Kawalan untuk melaraskan saiz penunjuk, serta kelegapan ikon dan bulatan di dalam penunjuk.

## ![](/icons/wireframe.webp) Kerangka dawai {#wireframe}
![](/images/settings_wireframe.webp)
Aktifkan tindihan kerangka dawai.

### Sasaran {#target}
Tetapkan sama ada objek yang tidak dipilih akan memaparkan kerangka dawai, atau hanya objek yang dipilih, atau semua objek.

### Sembunyi {#hide}
Tetapkan sama ada kerangka dawai masih dipaparkan untuk poligon yang tersembunyi.

### Multiresolusi: Hanya Tahap 0 {#multiresolution-level-0-only}
Multiresolusi memaparkan kerangka dawai tahap 0 dengan lebih gelap, dan tahap yang lebih tinggi semakin cerah. Apabila didayakan, pilihan ini hanya memaparkan kerangka dawai tahap 0.

### Warna {#wireframe-color}
Tetapkan warna dan kelegapan kerangka dawai.

## ![](/icons/grid.webp) Grid {#grid}
![](/images/settings_grid.webp)
Aktifkan grid.

### Snap {#snap}
Pilihan ini membuatkan titik bagi alat berasaskan lengkung dan bentuk (`Larik`, `Tiub`, bentuk poligon dan laluan...) melekat semasa anda melukisnya:

* `Snap ke grid` - melekat pada grid.
* `Snap ke titik (pandangan sejajar)` - melekat pada titik sedia ada yang berdekatan apabila kamera sejajar dengan satu paksi.
* `Snap ke titik (pandangan bebas)` - melekat pada titik sedia ada yang berdekatan apabila kamera tidak sejajar.

### Warna {#grid-color}
Tetapkan warna dan kelegapan grid. Pilihan ini muncul apabila grid kelihatan.

`Vinyet` memudarkan grid ke arah tepinya. `Ambang pembahagian snap` menetapkan, dalam piksel, setakat mana garisan grid boleh menjadi padat pada skrin sebelum grid bertukar ke tahap subbahagian yang lain.

## ![](/icons/culling.webp)Dua belah {#two-sided}
Membolehkan anda melihat muka poligon dari kedua-dua belah.

### Warna permukaan belakang {#backface-color}
`Warna belakang` mendayakan pewarnaan muka belakang, dan `Warna permukaan belakang` menetapkan warnanya.

## ![](/icons/outline.webp)Garis luar {#outline}
Dayakan garis luar di sekeliling objek yang dipilih.

### Warna garis luar, Ketebalan {#outline-color-thickness}
Tetapkan warna dan `Ketebalan` garis luar.


## ![](/icons/bang.webp) Sorotan {#highlight}
Dayakan kilatan singkat apabila pilihan berubah.
### Warna, Jangka masa {#color-duration}
Tetapkan warna dan tempoh kilatan dalam milisaat.

## ![](/icons/snap_cube.webp) Snap kiub {#snap-cube}
![](/images/settings_snapcube.webp)

Paparkan ikon pembantu di penjuru adegan, berguna untuk bertukar dengan pantas antara pandangan depan/belakang/kiri/kanan/atas/bawah. Ketuk pada sisi kiub untuk bertukar antara pandangan ortografik.

### Bentuk {#shape}
Pilih antara bentuk sfera, kiub atau gnomon untuk snap kiub.

### Hadkan penyelarasan {#restrict-alignment}
Selaraskan pandangan snap dengan paksi dunia. Apabila didayakan, hanya 6 pandangan utama yang boleh dipilih. Pada `Auto`, sekatan ini hanya berlaku apabila kamera berada dalam mod `Meja Putar`.

### Saiz {#size}
Tetapkan saiz snap kiub.

### Putar 180° {#flip-180}
Dayakan kelakuan ketuk supaya jika pandangan telah di-snap, mengetuk bahagian tengah kiub akan memutar pandangan 180 darjah. Contohnya, jika pandangan di-snap ke depan, mengetuk kiub pandangan akan memutarnya ke pandangan belakang.

### Tepi & penjuru {#edges-corners}
Tambah pandangan snap pada tepi dan penjuru kiub (zon berwarna ambar). Tidak tersedia untuk bentuk gnomon.

### Seretan meja putar {#turntable-drag}
Menyeret kiub akan memutarnya tanpa menggolekkan kamera, dan berhenti seketika pada setiap pandangan snap. Nyahdayakannya untuk menyeret kiub dengan putaran `Bebola jejak`. Walau apa pun pilihannya, seretan kekal mendatar atau menegak. Dengan kamera `Meja Putar`, kiub sentiasa diseret dengan cara ini.

### Kedudukan {#snap-position}
Tetapkan penjuru tempat snap kiub berada.


## ![](/icons/list.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Paparkan maklumat tentang memori sistem anda, jumlah verteks dalam adegan, dan bilangan verteks dalam pilihan semasa.

### Kedudukan {#stats-position}
Tetapkan penjuru tempat statistik berada.

## ![](/icons/edit_radius.webp) Pemegang {#handle}
Tetapan untuk pemegang yang anda seret dalam paparan, seperti gizmo.

### Input berangka {#gizmo-input}
Benarkan input berangka apabila mengetuk salah satu kawalan gizmo.

### Sembunyi semasa interaksi {#hide-on-interaction}
Memudarkan gizmo semasa anda berinteraksi dengannya, supaya ia tidak menghalang.

### ![](/icons/opacity.webp) Kelegapan {#handle-opacity}
Kelegapan pemegang.

## ![](/icons/shape_lasso.webp) Bentuk {#shape-settings}
Rupa bentuk yang anda lukis dengan sapuan bentuk (laso, segi empat tepat, lengkung...) pada skrin.

### ![](/icons/opacity.webp) Isian, Garis luar {#shape-fill-outline}
Kelegapan bahagian dalam bentuk dan garisan di sekelilingnya.

### Warna {#shape-colors}
Warna bentuk bagi setiap jenis alat: `Topeng`, `Sembunyi`, `Kumpulan muka` dan `Potong`.

## ![](/icons/array.webp) Repeater {#primitive-repeaters}
Had bagi salinan yang dihasilkan oleh [pengulang](scene#repeaters) (tatasusunan, radial, lengkung, permukaan). Had ini memastikan Nomad kekal responsif apabila sesuatu pengulang menjadi tidak terkawal.

### ![](/icons/cube.webp) Salinan maksimum {#repeater-max-copies}
Bilangan salinan paling banyak yang boleh dihasilkan oleh satu pengulang. Nomad bergelut dengan objek yang banyak, tidak kira saiznya.

### ![](/icons/cube.webp) Salinan adegan {#repeater-scene-copies}
Bajet salinan untuk seluruh adegan. Salinan poligon rendah menggunakan sedikit geometri tetapi tetap merupakan objek penuh, jadi inilah had yang dicapai dahulu oleh salinan kecil.

### ![](/icons/triangle.webp) Muka maksimum {#repeater-max-faces}
Bajet muka untuk semua salinan dalam adegan. Apabila melebihinya, objek yang paling berat akan kehilangan salinan dahulu.

## ![](/icons/multires.webp) Multiresolusi {#multires}
### Bilangan verteks maksimum {#multires-lowres-count}
Tetapkan ambang supaya operasi `Perbahagikan` multiresolusi tidak dibenarkan melebihi bilangan verteks ini, kerana ia berkemungkinan besar akan menyebabkan Nomad ranap: Nomad tidak menyemak memori yang tersedia sebelum membahagikan. Nilai lalainya ialah 10 juta.
### Ambang resolusi rendah {#multires-lowres-threshold}
Resolusi mesh yang lebih rendah boleh dipaparkan semasa anda menggerakkan kamera. Anda boleh menaikkan nilai ini jika anda mahu memaparkan resolusi mesh yang lebih tinggi.

## Tetapan {#advanced}
### ![](/icons/reset.webp) Tetap semula kepada asal {#reset}
Tetapkan semula semua tetapan keutamaan aplikasi kepada nilai lalainya.

Sesetengah sumber disimpan secara berasingan dan TIDAK ditetapkan semula: projek, ikatan kekunci, pratetap alat, persekitaran HDR, MatCap, alpha, tekstur berus dan imej rujukan. Semua yang disimpan bersama projek, seperti pencahayaan, pemprosesan pasca atau pandangan kamera, juga kekal utuh.

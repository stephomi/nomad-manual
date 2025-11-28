# ![](/icons/cog.webp) Tetapan {#reset-to-default}

Menu tetapan mengandungi banyak pilihan untuk mengawal rupa dan tingkah laku Nomad.

![](/images/settings_overview.webp)

## Tetapan paparan {#display-settings}
Bahagian ini mengandungi pintasan pelancaran pantas untuk kebanyakan tetapan di bahagian bawah menu ini.

![](/images/settings_display_settings.webp)

### Lorekan licin {#smooth-shading}
Togol lorekan licin dan bersegi. Apabila bersegi, poligon dilorek secara bebas, jadi anda boleh melihat topologi asas.
Ia boleh berguna untuk melihat lorekan bersegi semasa peringkat mengukir, kemudian tukar kepada lorekan licin untuk rendering.

Melumpuhkan Lorekan Licin meningkatkan prestasi sedikit.

### Garis luar {#outline-quick}
Togol garis luar pada pilihan semasa anda.

Ini berguna untuk mendapatkan maklum balas visual pada mesh terpilih anda sekiranya [Gelapkan Tidak Dipilih](#darken-unselected-objects) dilumpuhkan.

Dari sudut prestasi, menggunakan [Gelapkan Tidak Dipilih](#darken-unselected-objects) adalah jauh lebih baik daripada menggunakan penyelesaian garis luar.

### Grid {#grid-quick}
Togol grid latar belakang, berguna untuk memahami penempatan dan skala objek.

### Dua sisi {#two-sided-quick}
Togol paparan poligon dua sisi. Semua permukaan menghala ke arah tertentu.
Permukaan yang dianggap sebagai *backface* ialah yang menghala "menjauhi" sudut pandang kamera.

Sebagai contoh sfera ringkas permulaan akan mempunyai permukaan yang menghala ke luar.
Jika anda menggerakkan kamera ke dalam sfera anda akan melihat backface permukaan ini.

Kebanyakan masa anda tidak sepatutnya melihat bahagian backface permukaan, jadi mewarnakannya boleh membantu anda mengesan potensi masalah atau topologi yang tidak betul.

Melumpuhkan rendering `dua sisi` boleh meningkatkan prestasi rendering sedikit.


### Kerangka wayar {#wireframe-quick}
Togol tindihan rangka dawai. 

Ambil perhatian bahawa mengaktifkan rangka dawai akan menurunkan prestasi.

### Kiub snap {#snap-cube-quick}
Togol ikon pembantu di penjuru paparan, berguna untuk mengorientasikan diri anda dalam ruang dan menukar dengan pantas antara pandangan depan/belakang/kiri/kanan/atas/bawah.

### Tunjuk pengecatan {#show-painting}
Togol paparan cat. Cat lalai yang digunakan ialah bahan putih tidak metalik, pada kekasaran 25%.

### Guna sembunyi {#use-hide}
Togol mod sembunyi. Apabila dimatikan ia masih wujud, cuma dinyahaktifkan. Butang ini dilumpuhkan jika anda sedang menggunakan alat sembunyi.

### Tunjuk topeng {#show-mask}
Togol mod topeng. Apabila dimatikan ia masih wujud, cuma dinyahaktifkan. Tekan butang ini sekali lagi untuk mengaktifkannya semula.

Jika anda perlu menyembunyikan topeng DAN masih mahu ia aktif, gunakan warna topeng di bawah dan tetapkan kepada putih. Ingat untuk menukarnya kembali kepada kelabu apabila anda selesai!

Ambil perhatian bahawa butang ini dilumpuhkan jika anda sedang menggunakan alat topeng. 

### Topeng -> Legap {#mask-opaque}
Topeng -> legap akan mengabaikan verteks lutsinar untuk topeng bertopeng. Ini hanya berkaitan untuk kelegapan verteks dan tekstur, permukaan yang disembunyikan oleh “sembunyi” masih akan kekal tersembunyi.

### Serlahan {#highlight-quick}
Togol kilatan sorotan pemilihan. Apabila memilih objek, kilatkan objek terpilih dengan warna merah jambu terang selama 500 milisaat. Warna dan tempoh kilatan boleh disuaikan di bawah.

### Statistik {#stats-quick}
Togol teks paparan status dalam viewport 3D. Ini memaparkan maklumat tentang memori sistem anda, jumlah kiraan verteks adegan, dan kiraan verteks pilihan semasa.

----- 

### Gelapkan objek tidak dipilih {#darken-unselected-objects}
Objek yang tidak dipilih akan digelapkan supaya pilihan semasa lebih menonjol.

### Topeng {#mask}
Warna yang digunakan untuk topeng, secara lalai kelabu sederhana, didarabkan dengan warna objek anda. Tetapkan ini kepada putih untuk menjadikan topeng tidak kelihatan, tetapi ingat untuk menukarnya kembali kepada kelabu apabila selesai!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Tunjuk bulatan ketika mengukir {#show-circle-while-sculpting}
Terus menunjukkan jejari berus semasa mengukir.

### Tunjuk titik kecil {#show-small-dot}
Paparkan titik di tengah sapuan berus semasa mengukir, atau apabila paksi putar kamera diubah.

### Tunjuk penstabil tali {#show-rope-stabilizer}
Lukis garisan untuk menunjukkan panjang tali apabila penstabil tali malas diaktifkan dalam tetapan strok.

## ![](/icons/cursor.webp) Penunjuk {#indicator}
![](/images/settings_indicator.webp)

Paparkan penunjuk visual untuk tutorial dan rakaman skrin.

Butang `Jari`, `Stylus` dan `Tetikus` akan membolehkan paparan ikon apabila jenis input tersebut dikesan.

### Warna {#indicator-color}
Warna penunjuk.

### Saiz/Ikon/Bulatan {#indicator-shape}
Kawalan untuk melaraskan saiz penunjuk dan bentuk di dalam penunjuk.

## ![](/icons/wireframe.webp) Kerangka wayar {#wireframe}
![](/images/settings_wireframe.webp)
Aktifkan tindihan rangka dawai.

### Sasaran {#target}
Tetapkan sama ada objek tidak dipilih akan menunjukkan rangka dawai, atau hanya objek terpilih, atau semua objek.

### Sembunyi {#hide}
Tetapkan sama ada rangka dawai masih akan ditunjukkan untuk poligon tersembunyi.

### Multiresolusi: Aras 0 sahaja {#multiresolution-level-0-only}
Multiresolution akan menunjukkan rangka dawai untuk tahap 0 lebih gelap, dan tahap lebih tinggi semakin cerah. Apabila diaktifkan, pilihan ini hanya akan menunjukkan rangka dawai tahap 0.

### Warna {#wireframe-color}
Tetapkan warna dan kelegapan untuk rangka dawai.

## ![](/icons/grid.webp) Grid {#grid}
![](/images/settings_grid.webp)
Aktifkan grid.

### Warna {#grid-color}
Tetapkan warna dan kelegapan grid.

### Snap {#snap}
Aktifkan snap untuk alat berasaskan lengkung kepada grid.

## ![](/icons/culling.webp)Dua sisi {#two-sided}
Benarkan melihat permukaan poligon dari kedua-dua sisi.

### Warna belakang muka, Warna belakang muka {#backface-color}
Aktifkan pewarnaan backface, dan warna pewarnaan.

## ![](/icons/outline.webp)Garis luar {#outline}
Aktifkan garis luar di sekeliling objek aktif.

### Warna garis luar, Ketebalan {#outline-color-thickness}
Tetapkan warna dan ketebalan garis luar.


## ![](/icons/bang.webp) Serlahan {#highlight}
Aktifkan kilatan pendek apabila objek aktif ditukar.
### Warna, Tempoh {#color-duration}
Tetapkan warna dan tempoh masa kilatan dalam milisaat.

## ![](/icons/snap_cube.webp) Kiub snap {#snap-cube}
![](/images/settings_snapcube.webp)

Paparkan ikon pembantu di penjuru paparan, berguna untuk menukar dengan pantas antara pandangan depan/belakang/kiri/kanan/atas/bawah. Ketik pada sisi kiub untuk bertukar antara pandangan ortografik.

### Bentuk {#shape}
Pilih antara bentuk kiub, sfera, atau gnomon untuk kiub snap.

### Hadkan penjajaran {#restrict-alignment}
Aktifkan penguncian putaran kamera apabila menyeret pada kiub snap. Apabila aktif, gerakan seretan pada kiub snap hanya akan pergi kiri/kanan atau atas/bawah.

### Saiz {#size}
Tetapkan saiz kiub snap.

### Kalih 180 {#flip-180}
Aktifkan tingkah laku ketikan supaya jika pandangan telah disnap, mengetik pada tengah kiub akan memutar pandangan 180 darjah. Sebagai contoh jika pandangan disnap ke depan, mengetik kiub pandangan akan memutar ke pandangan belakang.

### Kedudukan {#snap-position}
Tetapkan di penjuru mana kiub snap akan berada.


## ![](/icons/edit_radius_n.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Paparkan maklumat tentang memori sistem anda, jumlah kiraan verteks adegan, dan kiraan verteks pilihan semasa.

### Kedudukan {#stats-position}
Tetapkan di penjuru mana statistik akan berada.

## Primitif/Pengulang {#primitive-repeaters}
## Input berangka {#gizmo-input}
Benarkan input berangka apabila mengetik widget gizmo.

## Multiresolusi {#multires}
### Kiraan verteks maksimum {#multires-lowres-count}
Tetapkan ambang untuk tidak membenarkan operasi subdivide multires melebihi kiraan poligon ini, yang berkemungkinan akan menyebabkan Nomad ranap. Lalai ialah 10 juta.
### Ambang resolusi rendah {#multires-lowres-threshold}
Resolusi lebih rendah bagi mesh boleh dipaparkan apabila anda menggerakkan kamera. Anda boleh meningkatkan nilai ini jika anda mahu memaparkan resolusi mesh yang lebih tinggi.

## Tetapan {#advanced}
### Tetap semula ke lalai {#reset}
Tetapkan semula semua tetapan kepada nilai lalai.
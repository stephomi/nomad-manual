# ![](/icons/brush.webp) Sapuan {#stroke}

---
![](/images/stroke_overview.webp) 

## Gambaran keseluruhan {#overview}

Anda boleh menyesuaikan cara sapuan berfungsi bagi kebanyakan berus alat.
Tetapannya hampir sama dengan yang terdapat dalam aplikasi lukisan 2d, tetapi ada beberapa pilihan yang khusus untuk pengukiran dan 3d.

Pilihan-pilihan ini dibahagikan kepada 5 submenu:

| Nama     | Ikon                         | Penerangan                                                         |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Sapuan   | ![](/icons/brush.webp)      | Mengawal cara sapuan dikenakan pada model                          |
| Alpha    | ![](/icons/alpha.webp)      | Cara tekstur skala kelabu digunakan untuk cap berus                |
| Pengurangan | ![](/icons/falloff.webp) | Mengawal cara kekuatan berus berubah dari tengah ke tepi           |
| Penapis  | ![](/icons/filter.webp)     | Cara berus dipengaruhi oleh geometri model                         |
| Tekanan  | ![](/icons/pressure.webp)   | Mengawal tindak balas tekanan stylus                               |

::: tip
Tidak semua pilihan sapuan digunakan oleh setiap alat. Pilihan sapuan yang tidak digunakan oleh alat semasa akan dinyahdayakan atau disembunyikan.
:::


## ![](/icons/brush.webp) Sapuan {#stroke-1}

### ![](/icons/radius.webp) Jejari {#radius}

![](/images/stroke_radius.webp)

Pilihan jejari ialah tetapan global: ia terpakai pada semua alat.

#### Ruang {#size}

* `Skrin` - jejari ditetapkan dalam unit skrin. Jika anda menetapkan jejari selebar 100 piksel, ia akan kekal 100 piksel tidak kira sama ada anda zum masuk atau zum keluar.
* `Dunia (3D)` - jejari ditetapkan dalam unit 3d. Contohnya, jika anda mencipta sfera dan menjadikan jejari sama besar dengan sfera itu, jejari akan kekal sama saiz dengan sfera semasa anda zum masuk dan keluar.

#### ![](/icons/link.webp) Pintasan segerak {#sync-shortcut}

Apabila didayakan, tetapan jejari dan siluet kekal selari apabila anda bertukar ke berus pintasan (`Lancar`, `Topeng` atau `Sembunyi`). Dengan cara ini, sapuan pantas untuk melicinkan atau menopeng menggunakan saiz berus yang sama seperti alat yang sedang anda gunakan.

#### ![](/icons/link.webp) Kongsi jari-jari {#share-radius}

Apabila didayakan, semua alat akan menggunakan jejari yang sama. Secara lalai, setiap alat mempunyai jejarinya sendiri.


### Jenis sapuan {#stroke-type}

![](/images/stroke_strokemode.webp)

Sapuan boleh berfungsi dalam beberapa mod:

### ![](/icons/stroke_dot.webp) Titik {#dot}
Seret seperti sapuan cat biasa.
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Gulung alfa {#roll}
Alfa berus akan diputar mengikut arah sapuan, berguna untuk membuat jahitan pada kain.
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Kunci + jejari {#lock-radius}
Mengecap sapuan berus dengan **_ketinggian_** tetap. Seretan akan menetapkan skala dan putaran.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Kunci + intensiti {#lock-intensity}
Mengecap sapuan berus dengan **_jejari_** tetap. Seretan akan menetapkan ketinggian dan putaran.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Mod `Kunci + jejari` dan `Kunci + intensiti` mengabaikan tetapan [Tekanan](#pressure), kerana seretan itu sendiri sudah menetapkan saiz dan kekuatan.
:::

![](/images/stroke_strokemodemove.webp)

Alat `Alih` dan `Seret` mempunyai 3 pilihan tersendiri:

### ![](/icons/snake.webp) Seret {#drag}

Sentiasa mengemas kini apa yang berada di dalam jejari berus sepanjang sapuan. Sapuan yang laju akan meninggalkan permukaan di belakang, manakala sapuan yang perlahan akan terus memegang bahan, menghasilkan bentuk yang lebih panjang. Ini ialah mod lalai untuk alat `Seret`. Dengan `Topologi dinamik`, mod ini boleh digunakan untuk membuat penyemperitan berbentuk seperti ular.
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Ambil {#grab}
Memilih apa yang berada di dalam jejari berus ketika sapuan bermula, dan mengekalkan pilihan itu. Ini berguna untuk operasi alih yang lebih tepat, kerana anda boleh melaraskan jarak alihan dengan teliti tanpa tersilap mengalihkan lebih daripada apa yang anda pilih pada mulanya. Ini ialah mod lalai untuk alat `Alih`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Kunci + jejari (seret) {#lock-radius-drag}
Jejari yang anda tetapkan diabaikan, dan sebaliknya ditetapkan secara dinamik berdasarkan sejauh mana sapuan diseret dari titik permulaan. Jarak kecil = jejari kecil, jarak lebih jauh = jejari lebih besar. Gunakan gelangsar intensiti untuk mengawal bentuk pengurangan. Berguna untuk membentuk bentuk organik yang kenyal seperti getah.
![](/videos/stroke_lockradius_drag.mp4) 

Sesetengah alat lain menyenaraikan jenis sapuan mereka sendiri di sini, contohnya `Santai`, `Lancar` dan `Smudge` untuk alat pelicin, atau bentuk seperti `Laso` dan `Lengkung` untuk alat berasaskan pemilihan. Semuanya diterangkan bersama setiap [alat](tools.md).


### Sesuaikan intensiti jarak {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Sapuan dengan jarak yang rendah (kurang daripada 50%) boleh terkumpul dengan cepat, menghasilkan sapuan yang lebih kuat berbanding nilai jarak yang lebih tinggi. Togol ini akan mengimbanginya, supaya sapuan mempunyai intensiti yang lebih kurang sama tidak kira berapa jaraknya.

### Jarak sapuan {#stroke-spacing}
Sejauh mana setiap cap berus dijarakkan semasa seretan. Nilai di bawah 100% akan bertindih, memberikan rupa sapuan yang berterusan. Nilai melebihi 100% akan mula meninggalkan ruang kosong, berguna untuk mengukir butiran seperti jahitan atau zip.

### Penstabil tali lambat {#lazy-rope-stabilizer}
Sapuan akan ketinggalan di belakang kedudukan penunjuk pada jarak tertentu. Ini boleh digunakan untuk melukis garisan yang licin.
![](/videos/stroke_lazy_rope.mp4) 

### Pelembutan sapuan {#stroke-smoothing}
Mengambil purata beberapa kedudukan penunjuk untuk mendapatkan sapuan yang lebih licin.
Dengan nilai yang tinggi, sapuan akan ketinggalan di belakang penunjuk tetapi akhirnya akan mengejarnya.
Ini berguna untuk melukis garisan yang licin.

### Jejari snap {#snap-radius}
Melekatkan sapuan pada sapuan sebelumnya apabila penunjuk bermula berhampiran tempat sapuan terakhir berakhir. Jejari ini menentukan sejauh mana untuk mencari hujung sapuan sebelumnya. Ini berguna apabila melukis garisan panjang yang berterusan sambil kerap berhenti seketika.

### ![](/icons/trail.webp) Jejak {#trail}

Apabila didayakan, setiap cap baharu turut mengenakan semula titik-titik terkini sapuan di belakangnya. `Bilangan jejak` menetapkan berapa banyak titik yang dikenakan semula, `Keamatan jejak` menetapkan kekuatannya, dan `Jejari jejak` menetapkan sejauh mana ia membesar.

Jejak hanya berfungsi dengan jenis sapuan `Titik`, dan tidak dengan [pengaruh pengurangan](#influence) `Rabung`.

### ![](/icons/silhouette.webp) Siluet {#silhouette}
![](/images/stroke_silhouette.webp)
Secara lalai, sapuan hanya menjejaskan permukaan model di dalam jejari berus. Apabila siluet didayakan, sapuan akan diunjurkan menembusi keseluruhan model. Ini sangat berguna semasa membentuk asas model pada peringkat awal, atau untuk bentuk yang memerlukan sisinya kekal tegak.

Arah unjuran boleh ditetapkan secara khusus:

* `X`, `Y`, `Z` - unjur mengikut paksi tetap.
* `Paparan` - unjur mengikut arah kamera.
* `Apabila snap` - unjur mengikut arah kamera, tetapi hanya semasa kamera di-snap pada suatu pandangan. Jika tidak, sapuan kekal sebagai sapuan biasa.
* `Paling hampir` - unjur mengikut paksi yang paling hampir dengan arah kamera. Ini ialah tetapan lalai.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Rawakkan {#randomize}

![](/images/stroke_randomize.webp)

`Intensiti`, `Ofset`, `Putaran` dan `Skala` sapuan masing-masing boleh dirawakkan. Gunakan kotak semak pada setiap baris untuk menghidupkan atau mematikannya. Ini boleh digunakan untuk menghasilkan pelbagai kesan, contohnya merawakkan dengan alat cat boleh menghasilkan warna bertompok, atau merawakkan dengan alat alur tajam boleh digunakan untuk membuat butiran kulit.

`Tempoh (lebih perlahan)` menetapkan panjang kitaran rawak: naikkannya untuk variasi yang perlahan dan beralun, turunkannya untuk hingar yang pantas. Butang kecil di sebelah setiap baris menskalakan tempoh untuk baris itu sahaja.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Rawakkan - HSV {#randomize-hsv}

Untuk alat yang mewarnakan, `Rona`, `Ketepuan` dan `Nilai` warna cat juga boleh dirawakkan, dengan tempoh tersendiri. Sangat sesuai untuk menambah variasi warna yang halus pada kulit atau batu.

### Ofset strok {#stroke-offset}

Mengenakan ofset tetap pada sapuan, supaya jari anda tidak menutupnya. Ini berguna pada skrin kecil. Ia ialah tetapan global: dayakan dengan kotak semaknya, dan ia terpakai pada semua alat.


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` ialah tekstur yang memodulasi tingkah laku berus anda.
Ia ialah imej skala kelabu, di mana piksel hitam bermaksud tiada ubah bentuk dan piksel putih bermaksud ubah bentuk penuh.

Klik pada imej alfa untuk menukarnya. Selain alfa terbina dalam dan alfa yang anda import sendiri, senarai alfa juga boleh memuat turun peta anjakan daripada Poly Haven.

Klik pada pratonton bahan untuk memuatkan alfa daripada pra-tetap bahan. Anda juga boleh menyimpan pra-tetap bahan di sini, dan memilih untuk membenamkan tekstur bersama alat.

::: tip
Tekstur tidak pernah diubah saiz, jadi tekstur yang besar boleh memperlahankan prestasi.
:::

### ![](/icons/blend_contrast.webp) Betulkan alfa {#invert-pixels}
Butang `Betulkan...` pada alfa yang diimport membuka tetingkap timbul yang membetulkan imej itu sendiri: nilai pertengahannya, menterbalikkan piksel (hitam menjadi putih dan putih menjadi hitam), putaran 90°, dan balikan mendatar atau menegak. Fail imej itu ditulis semula, jadi aplikasi lain juga akan melihat imej yang telah dibetulkan.

::: tip

Alfa terbina dalam yang disertakan bersama Nomad tidak boleh dibetulkan.

:::

### Projeksi {#projection}

Cara alfa diunjurkan pada model:

* `Permukaan` - alfa terletak pada permukaan di bawah berus, mengikut orientasinya.
* `Skrin` - alfa diunjurkan terus dari pandangan.
* `Jubinan` - alfa diunjurkan dari pandangan dan kekal di tempatnya semasa anda mewarna di atasnya, seperti stensil, jadi corak berulang bercantum dengan lancar. Putaran dikunci, dan tekanan pen tidak mengubah saiz corak.
* `Triplanar` - alfa diunjurkan mengikut 3 paksi. Pilihan penskalaan, putaran dan jubinan di bawah digantikan dengan tetapan tekstur triplanar.

### ![](/icons/diagonal.webp) Penskalaan {#scaling}

Saiz berus dalam Nomad ialah bulatan dengan jejari yang ditetapkan oleh pengguna. Tekstur pula selalunya berbentuk segi empat sama atau segi empat tepat, jadi parameter `Penskalaan` membolehkan anda menentukan cara tekstur dimuatkan di dalam bulatan. Untuk tekstur segi empat sama, nilai 0.7 akan muat di dalam bulatan. Nilai 1 akan membesarkan tekstur supaya bulatan pula muat di dalamnya, dan bahagian tepinya akan terpotong.

![](/images/alpha_scaling.webp) 

Mendayakan `Penskalaan Y` membolehkan anda meregangkan alfa secara menegak. Gelangsar pertama kemudiannya menjadi `Penskalaan X`.

![](/images/alpha_scaling_y.webp) 

`Balik secara mendatar` mencerminkan alfa dari kiri ke kanan.

### Putaran {#rotation}

Tekstur alfa akan diputar mengikut arah sapuan. Anda boleh menambah ofset putaran, dan jika ikon kunci didayakan, tekstur akan kekal terkunci pada putaran ini berbanding skrin.

Butang pen di sebelahnya memutar alfa apabila anda memusingkan stylus anda (barrel roll), dengan sapuan `Kunci + jejari` dan `Kunci + intensiti` semasa putaran tidak dikunci. Ia hanya berfungsi dengan perkakasan stylus yang menyokongnya.

### Jubinan {#tiling}
![](/images/stroke_tiling.webp) 

Berapa kerap tekstur berulang di dalam profil berus. Mod `Jubinan - X` dan `Jubinan - Y` membolehkan anda mengehadkan kepada satu tekstur sahaja di dalam sapuan (`Tiada`), tekstur berulang (`Ulang`), atau tekstur yang dicerminkan di mana setiap tekstur kedua dibalikkan untuk menghasilkan corak atau membantu membuat tekstur yang bersambung tanpa jahitan (`Pantulan`). Mod ini tersedia dengan sapuan `Gulung alfa`, projeksi `Jubinan`, atau `Jubinan` melebihi 1.

`Sesuai rapat (imej bukan empat segi tepat)` hanya penting untuk alfa dan tekstur berus yang bukan segi empat sama. Apabila didayakan, setiap imej berjubin secara tersendiri tanpa sebarang jarak. Nyahdayakannya untuk memastikan alfa dan imej lain kekal selari apabila nisbah aspek mereka berbeza.

![](/videos/alpha_tiling.mp4) 



### Nilai pertengahan {#mid-value}

Secara lalai, piksel hitam bermaksud tiada ubah bentuk, dan piksel putih bermaksud ubah bentuk positif penuh. Jadi contohnya, berus tanah liat dengan tekstur alfa batu-batan hanya akan menarik permukaan keluar di tempat alfa itu tidak hitam.

Jika anda mahu berus menolak permukaan ke dalam, atau menolak ke dalam DAN menarik keluar, anda boleh mengubah nilai pertengahan. Jadi jika anda menetapkan nilai kepada 0.5, warna kelabu pertengahan dalam alfa tidak akan melakukan apa-apa, nilai hitam akan menolak ke dalam, dan putih akan menarik keluar.

Dua butang membantu anda mencari nilai yang betul: butang segi empat sama membaca nilai pertengahan daripada sempadan imej, dan pemilih membolehkan anda memilihnya terus pada alfa itu sendiri.




## ![](/icons/falloff.webp) Pengurangan {#falloff}

![](/images/falloff_menu.webp) 

Ini serupa dengan [Alpha](#alpha), tetapi anda mengawal intensiti dengan satu lengkung sahaja. Ia digabungkan dengan alfa, supaya anda boleh menggunakan tekstur untuk butiran, dan pengurangan untuk mengawal pudaran di tepi serta intensiti di tengah alat.

Apabila lengkung berada di bahagian atas, ubah bentuk adalah penuh. Apabila ia berada di bahagian bawah, berus tidak memberi sebarang kesan.

Anda boleh membayangkan lengkung ini sebagai keratan rentas hujung berus. Bahagian bawah menunjukkan pratonton rupa satu 'cap' berus pada permukaan model, dan jika berus mempunyai tekstur alfa, ia juga akan dipaparkan untuk menunjukkan bagaimana pengurangan dan alfa akan berinteraksi.

### ![](/icons/fx.webp) Pra-tetap {#preset}
Apabila `Pra-tetap...` dipilih, mengklik pada graf lengkung akan membuka menu pra-tetap. Lengkung yang bulat memberikan hasil yang lebih lembut, manakala lengkung yang bersudut memberikan hasil yang lebih tajam. Butang `Tolak` di bar alat kiri pada dasarnya menterbalikkan pengurangan, jadi bahagian atas lengkung akan menolak masuk ke dalam permukaan dan bukannya menarik keluar, atau sebaliknya.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Apabila dipilih, anda boleh melukis lengkung pengurangan anda sendiri. Penyunting lengkung berfungsi sama seperti lengkung di bahagian lain Nomad:

* Klik pada lengkung untuk mencipta titik baharu
* Seret titik untuk mengubah kedudukannya
* Klik pada titik untuk menukar antara tajam dan licin
* Seret titik ke titik jirannya untuk membuangnya

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Apabila dipilih, anda boleh melukis lengkung pengurangan anda sendiri. Penyunting berfungsi sama seperti Catmull-Rom, tetapi titik-titik lengkung mempengaruhi lengkung dan bukannya berada terus di atas lengkung, yang boleh membantu menghasilkan bentuk lengkung yang lebih licin.

### ![](/icons/curve_bevel.webp) Serong {#bevel}
Titik-titik disambungkan dengan garisan lurus, dengan sudut yang dibulatkan mengikut ketajaman setiap titik. Berguna untuk berus berpermukaan rata dengan serong yang kemas di tepinya.

Penyunting lengkung mempunyai 3 butang:

| Item     | Ikon                        | Penerangan                                   |
| :------: | :-------------------------: | :------------------------------------------: |
| Maksimumkan | ![](/icons/maximize.webp) | Membesarkan penyunting lengkung             |
| Tetapkan semula | ![](/icons/reset.webp) | Mengembalikan lengkung kepada keadaan lalai |
| Simetri  | ![](/icons/symmetric.webp) | Memaparkan lengkung sebagai 'hujung berus' yang simetri |


### Pengaruh {#influence}

* `Sfera` (3d) - Pengaruh dikira dengan mengambil jarak dari verteks ke pusat berus.
* `Bulat` (2d) - Verteks diunjurkan dahulu pada satah kawasan, sebelum jaraknya ke pusat berus diambil. Ini serupa dengan cara alfa disampel.
* `Silinder` - Pengaruh diunjurkan menembusi kawasan dalam bentuk silinder. Ini sama seperti mendayakan [Siluet](#silhouette-1) di bawah.
* `Rabung` - Pengurangan diukur merentasi sapuan, jadi lengkung menjadi keratan rentas keseluruhan sapuan. Butang `Sim` kemudiannya mencerminkan profil merentasi sapuan: sunting satu sisi dan sisi yang lain akan mengikut. Apabila ia dimatikan, lengkung bermula dari sisi kiri sapuan hingga ke sisi kanannya. Tidak tersedia untuk alat berasaskan perataan.

### ![](/icons/silhouette.webp) Siluet {#silhouette-1}
Secara lalai, sapuan hanya menjejaskan permukaan model di dalam jejari berus. Apabila siluet didayakan, sapuan akan diunjurkan menembusi keseluruhan model. Ini sangat berguna semasa membentuk asas model pada peringkat awal, atau untuk bentuk yang memerlukan sisinya kekal tegak. Ia mempunyai pilihan unjuran yang sama seperti [Siluet](#silhouette) dalam tab Sapuan.



## ![](/icons/filter.webp) Penapis {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Himpun strok {#accumulate-stroke}
Membuang had berapa banyak bahan yang boleh ditambah/dibuang dalam setiap sapuan. Contohnya, alat `Tanah liat` mendayakan pilihan ini, jadi bahan boleh terus terkumpul, manakala alat `Berus` menyahdayakannya, jadi sapuan akan berhenti menambah bahan jika anda terus menggerakkan sapuan yang sama di atas kawasan mesh yang sama.

### ![](/icons/culling.webp) Hanya verteks menghadap depan {#front-facing-vertex-only}
Pilihan ini akan mengabaikan verteks yang menghadap ke belakang.
Ia berguna jika anda mahu mewarna sebahagian geometri yang nipis tanpa menjejaskan sisi yang satu lagi.
Ia juga berfungsi untuk mengukir, tetapi anda mungkin akan melihat beberapa artifak.

### ![](/icons/eye_open.webp) Hanya bucu kelihatan {#visible-vertex-only}
Mengabaikan verteks yang tersembunyi di belakang permukaan lain, seperti yang dilihat dari kamera. Pilihan ini muncul untuk sapuan bentuk (laso, segi empat tepat...) bagi alat topeng, alat mewarna, `Kumpulan muka` dan `Sembunyi`.

### ![](/icons/dynamic.webp) Benarkan topologi dinamik {#allow-dynamic-topology}
Pilihan ini hanya tersedia jika mesh anda berada dalam mod [Topologi dinamik](topology.md#dynamic-topology). Anda boleh menyahdayakan atau mendayakan topologi dinamik bagi setiap alat.

### ![](/icons/connect.webp) Topologi bersambung {#connected-topology}
Hanya mengukir verteks yang bersambung dengan permukaan yang anda sentuh dengan alat. Contohnya, apabila digunakan dengan alat `Alih`, ini membolehkan anda mengalihkan sesuatu bahagian walaupun ia bersilang dengan bahagian lain.
![](/videos/connected_topology.mp4)

### Lindungi kawasan {#protect-area}
![](/images/filter_protect_area.webp) 

Pilihan-pilihan ini menghalang alat daripada menjejaskan bahagian mesh anda dalam pelbagai keadaan. Setiap satunya boleh ditetapkan kepada `Auto`, `Tidak` atau `Ya`, dan anak panah kecil menunjukkan apa yang sedang dipilih oleh `Auto`.

* `Sembunyi` - Jika sebahagian mesh disembunyikan dengan alat sembunyi, tetapkan sama ada ia perlu dilindungi. Pada `Auto`, muka yang tersembunyi dilindungi, kecuali jika kerangka dawainya kelihatan (lihat tetapan [Kerangka dawai](settings.md#wireframe)).
* `Topeng` - Jika sebahagian mesh ditopeng, tetapkan sama ada ia perlu dilindungi. Pada `Auto`, bahagian yang ditopeng dilindungi selagi topeng kelihatan dalam menu [Shading](shading).
* `Kumpulan muka` - Tetapkan sama ada anda hanya boleh menggunakan alat di dalam kumpulan muka pertama yang disentuh. Pada `Auto`, ini mengikut sama ada kumpulan muka kelihatan dalam menu [Shading](shading).

Butang `(Semua)` menetapkan sama ada perlindungan ini global, dikongsi oleh semua alat, atau ditetapkan bagi setiap alat.


### Pensampelan kawasan {#area-sampling}
Sesetengah berus atau pilihan sapuan memerlukan normal satah dan kedudukan satah pada permukaan untuk berfungsi.

Anda boleh mengawal cara satah purata ini dikira dengan menetapkan kawasan pensampelan sebagai nisbah jejari alat.

Pada 100%, setiap titik di dalam bulatan pemilihan diambil kira.

Pada 0%, hanya verteks atau segi tiga yang paling hampir diambil kira. Nilai-nilai ini boleh dipautkan untuk kedua-dua `Jejari normal` dan `Jejari kedudukan`, atau dinyahkunci dan ditetapkan secara berasingan.

### Penapis Normal Kawasan {#keep-sharp-edges}
Mengecualikan titik yang normalnya terlalu menyimpang daripada normal permukaan.

Ia akan mengubah cara kawasan satah dikira (Pensampelan kawasan), jadi ia paling berguna untuk alat tanah liat atau alat berasaskan perataan, atau jika anda mahu mewarna permukaan yang kebanyakannya rata tanpa warna melimpah keluar.

Sudut `Min` dan `Maks` mengawal peralihan antara titik yang dikecualikan dan titik yang terjejas sepenuhnya, seperti yang ditunjukkan oleh cakera berwarna kecil di sebelahnya.

![](/videos/filter_keep_sharp_edges.mp4)

### Penapis Lenyap Normal {#falloff-normal-filter}
Seperti [Penapis Normal Kawasan](#keep-sharp-edges), ia mengecualikan titik yang normalnya terlalu menyimpang daripada normal permukaan, tetapi ia bertindak pada pengurangan berus dan bukannya pada pengiraan satah. Ia berguna untuk mewarna lekuk atau benjolan.


### Penapis kedalaman {#depth-masking}
![](/images/stroke_depthmask.webp)

Mengecualikan titik yang berada di atas atau di bawah jarak tertentu daripada satah yang dikira (Pensampelan kawasan).

Ini boleh digunakan untuk mewarna hanya pada kawasan yang berbonggol, atau hanya pada kawasan yang berongga.

Graf ini mewakili keratan rentas permukaan; garisan mendatar ialah kedudukan permukaan, dan bulatan mewakili jejari pengurangan cat secara relatif di atas dan di bawah permukaan. `Offset tinggi` ialah peratusan di atas atau di bawah permukaan untuk memulakan pengiraan penopengan. Dengan `Penurunan kedalaman` didayakan, `Kawasan atas` dan `Kawasan bawah` membolehkan anda menskalakan pengurangan di atas dan di bawah titik ofset.

#### Contoh: Mewarna dalam rongga {#example-paint-in-cavities}
Untuk mewarna hanya kawasan rongga, tetapkan ofset tinggi kepada -100%, dan laraskan gelangsar kawasan atas supaya ia menjauhi garisan mendatar. Ini bermakna klik pertama menetapkan kedalaman 'sifar', dan kemudian hanya kawasan di bawah kedalaman ini yang akan terjejas.

![](/videos/stroke_depth_cavity.mp4)

#### Contoh: Mewarna pada bonggol {#example-paint-on-bumps}
Untuk mewarna hanya kawasan yang tinggi, tetapkan ofset tinggi kepada +90%, supaya bahagian bawah bulatan bersilang sedikit dengan garisan mendatar. Apabila anda mengklik di bahagian atas zon yang 'tinggi', ini akan menetapkan kedalaman, supaya apa sahaja pada kedalaman itu, ditambah sedikit di bawahnya, dan apa sahaja yang lebih tinggi daripadanya, akan diwarnakan. Rongga yang dalam akan dilangkau.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Tekanan {#pressure}
![](/images/pressure_menu.webp) 

Mengawal cara tekanan stylus/pen mempengaruhi berus.

### Gunakan tetapan global {#use-global-settings}

Secara lalai, `Gunakan tetapan global` didayakan, bermakna semua berus berkongsi nilai tekanan yang sama. Nyahtandakannya untuk memberikan alat semasa tetapan tekanannya sendiri.

### ![](/icons/radius.webp) Jejari {#pressure-radius}

Lengkung ini mengawal cara jejari berus dipengaruhi oleh tekanan. Tetapan lalainya ialah hubungan linear, jadi jika stylus anda mempunyai tindak balas yang lancar, perubahan jejari juga sepatutnya terasa lancar. Walau bagaimanapun, banyak stylus mempunyai tindak balas yang tidak linear, yang boleh anda imbangi dengan lengkung ini. Contohnya, jika jejari tidak terasa mencapai nilai maksimumnya pada tekanan tinggi, gunakan pra-tetap lengkung seperti 'out-pow3', dengan lengkungan yang menghala ke atas, supaya jejari meningkat lebih awal.

Dialog ini serupa dengan paparan lengkung pengurangan: anda boleh menggunakan pra-tetap dengan mengetik pada tetingkap lengkung, atau melukis lengkung anda sendiri dengan mod `Catmull-Rom`, `B-spline` dan `Serong`.

Jika anda mahukan jejari yang tetap, nyahdayakan bahagian ini.

### ![](/icons/intensity.webp) Keamatan {#pressure-intensity}

Serupa dengan lengkung jejari, tetapi untuk mengawal intensiti. Jika anda mahukan intensiti yang tetap, nyahdayakan bahagian ini.

### Hadkan tekanan pada 100% {#limit-pressure}

Memastikan tekanan stylus tidak pernah melebihi 100%. Ini ialah tetapan global.

### Kelancaran tekanan {#pressure-smoothing}

Mengambil purata peristiwa tekanan stylus untuk hasil yang lebih licin.

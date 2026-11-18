# ![](/icons/symmetry.webp) Simetri {#symmetry}

Menu ini mengawal cara sapuan diulang merentasi satah cermin, secara radial atau sebagai jubin, serta cara untuk memulihkan simetri pada objek yang tidak simetri.

![](/images/symmetry_overview.webp) 

## Gambaran keseluruhan {#overview}
Anda boleh menggunakan simetri dalam beberapa cara:

* Sebagai cermin, membalikkan kerja anda merentasi X (kiri/kanan), Y (atas/bawah), Z (belakang/depan), atau gabungannya. 
* Simetri radial boleh ditetapkan pada X Y Z dengan bilangan ulangan, contohnya untuk memahat bintang laut. 
* Jubinan mengulang sapuan anda di sepanjang objek, supaya pahatan bersambung dengan lancar seperti jubin.
* Cermin boleh beroperasi di sekeliling asalan (dipanggil mod dunia) atau di sekeliling pusat objek (dipanggil mod tempatan).
* Pahatan yang bermula tidak simetri boleh dipaksa menjadi simetri.

Pintasan untuk mendayakan/menyahdayakan simetri juga terdapat pada panel pantas kiri (*"Sim"*). Huruf kecil 'L/W' menunjukkan sama ada Nomad berada dalam mod simetri Tempatan atau Dunia. Anda juga boleh menekan lama atau meleret ke tengah skrin untuk memaparkan menu.

![](/images/symmetry_button.webp) 

Tetapan simetri disimpan bersama setiap objek, dan tajuk menu menunjukkan nama objek yang sedang anda sunting.
Alat pemahatan berkongsi keadaan hidup/mati yang sama, manakala alat transformasi ([Transformasi](tools.md#transform) dan [Gizmo](tools.md#gizmo)) mempunyai keadaan sendiri.

::: tip
Menu simetri terutamanya untuk mengawal simetri sapuan. Anda juga boleh mencerminkan dan mengulang objek melalui [pengulang dalam menu adegan](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Diaktifkan {#enabled}
Togol mod cermin; ini sama seperti butang `Sim` pada panel pantas kiri. Ikon amaran mengingatkan anda apabila ia dimatikan, dan menu juga memberitahu anda apabila alat semasa mengabaikan simetri.

## Satah {#planes}

Dayakan satah simetri, dan bilangan ulangan untuk simetri radial. Perhatikan bahawa anda tidak perlu memilih satu satah sahaja: anda boleh mendayakan 1, 2 atau kesemua 3 satah untuk simetri yang kompleks.

Baris `Radial` menetapkan bilangan ulangan untuk simetri radial di sekeliling setiap paksi. Ini juga tidak terhad kepada satu paksi, malah boleh digabungkan dengan simetri satah untuk menghasilkan keputusan yang terperinci dengan sangat pantas. (Jumlah keseluruhan ulangan dihadkan kepada 200)

![](/videos/symmetry_demo.mp4) 

## Jubinan {#tile}

Ulang sapuan anda di sepanjang satu paksi, pada jarak yang tetap, supaya pahatan bersambung dengan lancar seperti jubin. Berguna untuk corak, bata, atau tekstur yang anda rancang untuk diulang.

Hidupkan jubinan untuk setiap paksi dengan butang `Jubinan`, kemudian tetapkan sama ada `Kiraan` (berapa banyak ulangan merentasi objek) atau `Jarak` (ruang antara dua ulangan). Ketuk togol di sebelah kiri untuk bertukar antara kedua-duanya.

## Kaedah {#method}
Cermin boleh berada dalam mod `Tempatan`, dan bergerak bersama objek, atau mod `Dunia`, dan tidak bergerak. Jika anda tidak pasti mod mana yang anda perlukan, perhatikan penunjuk satah cermin dan radial yang ditindih pada objek. Dalam mod tempatan, jika anda menggunakan alat transformasi (`Gizmo` atau `Transformasi`) untuk menggerakkan model, penunjuk cermin akan turut bergerak. Dalam mod dunia, penunjuk cermin kekal tetap, dan objek akan meluncur melaluinya.

## Cermin {#mirroring}
![](/images/symmetry_mirroring.webp)

Apabila memahat berhampiran satah simetri, sesetengah berus tidak menghasilkan simetri yang sempurna. Bahagian ini membolehkan anda memulihkan simetri dengan menyalin satu sisi pahatan anda ke sisi yang lain. 

`Arah` - Dua butang anak panah di sebelah tajuk `Cermin` menentukan sisi mana yang akan disalin ke sisi yang lain. Nomad mengiranya daripada paparan semasa anda, jadi sisi itu kekal sama pada skrin walau dari arah mana pun anda melihat model.

![](/icons/shield.webp) `Topeng` - Butang topeng membolehkan anda mengasingkan apa yang akan dicerminkan; topeng pada sisi destinasi akan melindungi kawasan itu, manakala topeng pada sisi sumber akan menghalang kawasan itu daripada dicerminkan ke destinasi. 

![](/icons/tool_hide.webp) `Sembunyi` - Apabila aktif, kawasan yang tersembunyi pada sisi sumber tidak akan dicerminkan ke destinasi. 

`Cermin` (simpan topologi) akan cuba mengenal pasti sama ada topologi adalah sama pada kedua-dua sisi cermin, dan jika ya, hanya menggerakkan verteks. Ini senario yang paling biasa. Simetri radial diabaikan. Jika topologi tidak simetri, Nomad menawarkan untuk memaksa pencerminan dengan `Potong • Cermin`.

Butang `Potong` memotong objek di sepanjang satah simetri. Butang ini mengubah topologi, jadi ia lebih merosakkan berbanding `Cermin`. Nombor pada setiap butang ialah bilangan objek yang akan anda peroleh:

* `Potong` - buang satu sisi objek.
* `Potong • Cermin` - potong objek, salin satu sisi, cerminkan ke sisi yang lain, dan cantumkan verteks di sepanjang cermin. Kadangkala kaedah ini diperlukan jika model sangat berbeza merentasi cermin.
* `Potong • Pisahkan` - potong objek dan simpan setiap sisi sebagai objek berasingan.
* `Potong • Cermin • Pisahkan` - seperti `Potong • Cermin`, tetapi setiap sisi menjadi objek berasingan.

Jika beberapa objek dipilih, `Cermin` dan [Balikkan objek](#flip-object) digunakan pada kesemuanya.

### Balikkan objek {#flip-object}
![](/images/symmetry_flip.webp)
Jadikan sisi kiri sebagai sisi kanan, dan sebaliknya, mengikut `X`, `Y` atau `Z`. Hasilnya kelihatan sama seperti jika anda menggunakan menu alat gizmo dan menetapkan skala kepada -1 pada X.

## Tetapkan semula dan Sunting {#reset-and-edit}

![](/images/symmetry_edit.webp)

Anda boleh menyunting lokasi dan orientasi simetri (tetapi ini tidak disyorkan!). Jika perlu, `Pusat dunia` (`Pusat objek` dalam mod tempatan) dan `Orientasi` akan menetapkan semula lokasi dan orientasi simetri kepada nilai lalainya.

Nomad biasanya tahu di mana hendak meletakkan satah simetri. Melaraskannya secara manual tidak disyorkan, tetapi butang `Edit Gizmo` membolehkannya untuk pengguna mahir. Apabila butang ini diklik, gizmo dipaparkan untuk membolehkan anda mengalihkan dan memutar satah simetri. Jika anda mahu memulihkan pusat dan orientasi lalai, gunakan butang tetapkan semula di atas.

`Dari pivot` meletakkan satah simetri pada paksi alat [Gizmo](tools.md#gizmo). Ia hanya tersedia semasa alat `Gizmo` aktif.

Kelakuan pilihan ini berubah bergantung pada ruang (*Tempatan/Dunia*) yang anda gunakan.
Jadi jika ia tidak berfungsi seperti yang anda jangkakan, pastikan anda berada dalam ruang yang betul.

::: tip
Menyunting satah simetri dengan gizmo agak eksperimental, anda mungkin tidak memerlukannya!
:::

## Pilihan paparan {#show-options}
![](/images/symmetry_show.webp)


`Tunjukkan garis` dan `Tunjukkan satah` menogol tindihan paparan bagi lokasi simetri. Perhatikan bahawa mematikan pilihan ini hanya berkesan apabila menu simetri ditutup.

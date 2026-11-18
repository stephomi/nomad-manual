# ![](/icons/manual.webp) Petua {#tips}

[[toc]]

## Cara memulakan model {#how-to-start-a-model}

Pemula dalam pengukiran 3d sering bertanya apakah cara terbaik untuk memulakan model. Sebenarnya tiada cara yang terbaik; setiap orang mempunyai citarasa yang berbeza. Berikut ialah beberapa pendekatan yang lebih biasa.

### Ukir pada sfera, multiresolusi {#sculpt-on-sphere-multires}

Model lalai semasa Nomad dilancarkan ialah cara yang paling biasa. Gunakan alat alih, tanah liat dan alur tajam untuk menolak dan menarik sfera menjadi bentuk yang dikehendaki. Gunakan tahap subbahagian yang lebih rendah apabila anda mahu membuat perubahan besar dengan cepat, dan tahap subbahagian yang lebih tinggi untuk kerja-kerja terperinci.

Masalah yang biasa ialah anda selalunya kehabisan poligon di tempat yang anda perlukan, sedangkan poligon terlalu banyak di tempat lain. Contohnya, jika anda menolak sfera lalai menjadi satu badan penuh, kemungkinan besar anda tidak akan mempunyai butiran yang cukup untuk membuat jari, sedangkan banyak poligon terbazir di bahagian belakang kepala. Namun, untuk bentuk yang kebanyakannya sfera seperti kepala, ini tidak menjadi masalah.

### DynTopo {#dyntopo}

Mendayakan DynTopo akan menambah dan membuang poligon secara adaptif semasa anda mengukir. Poligon ini berbentuk segi tiga, dan pemula selalunya tidak suka susun aturnya yang bersepah berbanding rupa multiresolusi yang kemas. Tetapi berbaloi untuk terus mencuba! Jika anda menghidupkan shading licin, mematikan kerangka dawai dan berhenti merisaukan susun atur, mod ini boleh memberikan rasa seperti bekerja dengan tanah liat. Jangan lupa bahawa jika anda menggunakan berus yang besar, atau berus pelicin, mod ini juga boleh membuang poligon, jadi alat sentiasa terasa pantas dan responsif. Setelah lapisan pertama ukiran anda siap, anda boleh mengklonnya dan menjalankannya melalui Quad Remesher untuk mendapatkan susun atur yang kemas, kemudian mengunjurkan semula butiran asal pada tahap subbahagian yang tinggi.

### Remesh voxel {#voxel-remesh}

Remesh voxel akan mengenakan topologi yang kebanyakannya berasaskan quad pada ukiran anda. Operasi ini pantas pada resolusi rendah, dan boleh digunakan untuk menggantikan poligon yang teregang atau terlalu padat dengan susun atur yang dijarakkan sekata. Ini boleh menjadi cara yang bagus untuk memulakan satu badan penuh daripada sfera; katakan anda bermula dengan kepala, anda boleh meregangkan leher, lakukan remesh voxel. Regangkan badan, remesh voxel, lengan, remesh voxel, dan seterusnya, sehingga anda mendapat bentuk asas.

### Gunakan beberapa objek {#use-multiple-objects}

Banyak panduan anatomi menggambarkan badan menggunakan sfera, silinder dan kiub yang ringkas. Anda juga boleh mengukir dengan cara ini dalam Nomad. Kelebihannya ialah anda boleh menjadikan objek-objek berinduk antara satu sama lain dalam hierarki adegan, jadi contohnya anda boleh memutar leher dan kepala akan mengikut. Keupayaan menggunakan alat gizmo untuk translasi/putaran/skala yang tepat juga sangat berguna, dan anda juga boleh menetapkan pangsi bagi setiap bentuk supaya ia bergerak tepat seperti yang anda jangkakan. Apabila blok-blok asas sudah berada di tempat yang betul, anda boleh memilih kesemuanya dan melakukan remesh voxel atau boolean untuk menjadikannya satu permukaan bagi pengukiran yang lebih terperinci.

Petua berguna untuk cara kerja ini ialah bermula dengan sfera, skalakannya menjadi bentuk sosej yang panjang, tekan pangsi, klik 'bawah', dan tekan pangsi sekali lagi. Kini anda mempunyai satu bahagian badan yang boleh diklon, dianjak sepanjang sfera pertama, diklon, diputar, diklon, digelongsor, diklon dan seterusnya, untuk menyusun badan dengan cepat.

### Tiub {#tubes}

Alat tiub ialah cara yang bagus untuk memulakan ukiran. Ekor reptilia, lengan, kaki, jari, kening, semuanya boleh dilakar dengan cepat menggunakan alat tiub, kemudian disunting dengan mudah selepas itu. Ia juga membolehkan anda mengubah profil keratan rentas, supaya bentuk boleh ditukar dengan pantas. Anda boleh mengesahkan bentuk itu untuk mula mengukir padanya, dan melakukan remesh voxel bersama objek lain untuk mendapatkan mesh satu badan penuh.

### Gunakan aplikasi lain {#use-other-apps}

Sesetengah orang lebih suka memulakan model dalam aplikasi lain, dan itu juga tidak mengapa. Alat seperti Blender atau Valence membolehkan model dimulakan menggunakan teknik poligon rendah, kemudian diimport ke dalam Nomad untuk diukir.

### Gunakan pra-tetap terbina dalam {#use-the-built-in-presets}

Daripada menu [Fail](files.md), klik `Pra-tetap…` di sebelah kiri bahagian projek. Di sini anda akan menemui beberapa pra-tetap bentuk kepala dan badan daripada Blender Foundation. Pilih yang anda suka, ketik sekali lagi, dan tambahkannya ke adegan anda.

### Gunakan model dalam talian {#use-online-models}

Terdapat banyak model percuma dalam talian, contohnya di polyhaven, sketchfab dan turbosquid. Biasanya model-model ini boleh diimport ke dalam Nomad, dan sama ada diukir terus, atau digunakan sebagai rujukan.

### Tiada peraturan! {#no-rules}

Akhirnya, anda boleh menggunakan apa-apa gabungan teknik ini, atau tidak menggunakannya langsung! Nomad sangat fleksibel dalam hal ini. Pengguna mahir mungkin bermula dengan tiub, kemudian DynTopo, kemudian menggabungkannya dengan kaki yang dimuat turun, kemudian melakukan quad remesh pada semuanya, kemudian multiresolusi untuk butiran akhir. Apa sahaja yang sesuai untuk anda.

## Kumpulan muka {#facegroups}

Alat kumpulan muka boleh digunakan untuk pelbagai perkara, seperti yang diterangkan dalam video youtube ini: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Ini ialah ringkasan bertulis tentang ciri-ciri yang dibincangkan dalam video tersebut.

### Mengapa kumpulan muka? {#why-facegroups}

Kumpulan muka membolehkan anda menyusun dan memilih muka ('muka' dan 'poligon' digunakan secara bergantian dalam manual ini). Ia lebih mudah diterangkan jika dibandingkan dengan alat pemilihan dan penyusunan Nomad yang lain. Nomad membolehkan anda mencipta objek, menamakannya dan menjadikannya berinduk, jadi mudah untuk mencipta struktur objek bagi mentakrifkan sebuah bilik yang terdiri daripada lantai, dinding, kerusi, meja dan sebagainya.

Untuk watak, anda mungkin membuat bentuk asas awal menggunakan objek berasingan untuk kepala, lengan dan kaki, tetapi sebaik sahaja anda menggabungkan semua bahagian itu menjadi satu mesh, struktur ini hilang. Anda boleh mengerjakan bahagian-bahagian kecil watak dengan topeng, tetapi lama-kelamaan memenatkan untuk terus melukis topeng bagi tangan, kemudian hidung, kemudian tangan sekali lagi.

Di sinilah kumpulan muka berguna. Ia membolehkan anda menandakan muka poligon dengan warna, kemudian memilih dan memanipulasi poligon yang mempunyai warna yang sama. Ambil perhatian bahawa warna kumpulan muka dan warna verteks adalah dua perkara yang berbeza.

Analogi yang paling hampir ialah mewarnakan peta, kemudian dapat memilih negara atau wilayah berdasarkan warnanya.

Untuk kepala watak, anda boleh mewarnakan zon-zon untuk menandakan soket mata, hidung, bibir, dagu dan telinga, kemudian memilih zon-zon itu dengan mudah kemudian nanti. Untuk pengukiran permukaan keras dan mekanikal, ia berguna untuk mentakrifkan panel dan bahagian.

### Mencipta dan menyunting kumpulan muka {#creating-and-editing-facegroups}

Kumpulan muka boleh dikenakan dengan berus, di mana setiap sapuan baharu mencipta kumpulan muka baharu, atau berus boleh memilih kumpulan muka di bawah kursor dan memanjangkannya. Kumpulan muka juga boleh dicipta menggunakan bentuk.

* Titik, mod lalai - satu seretan akan mentakrifkan warna kumpulan muka baharu dan menetapkannya pada muka yang anda seret. Setiap seretan baharu akan mentakrifkan kumpulan muka baharu. Satu ketikan akan mengisi penuh kumpulan muka baharu.
* Titik, mod `Pilih` - apabila butang `Pilih` pada bar alat kiri aktif, Nomad akan memilih kumpulan muka di bawah kursor, dan mengenakannya sepanjang baki seretan. Ini berguna untuk memperhalusi kumpulan muka tanpa perlu memilihnya secara manual.

### Penopengan {#masking}

Apabila alat topeng aktif, dan butang kumpulan muka aktif pada bar alatnya, mengetik pada sesuatu kumpulan muka akan menopengnya.


### Menyembunyikan {#hiding}

Apabila alat sembunyi aktif, dan butang kumpulan muka aktif pada bar alatnya, mengetik pada sesuatu kumpulan muka akan menyembunyikannya.

### Menyusun {#organizing}

Seperti yang disebut tadi, kumpulan muka boleh digunakan untuk menyusun mesh anda tanpa perlu membuat objek yang berasingan. Anda mungkin tidak mahu memisahkan kepala kepada objek berasingan untuk hidung, dagu dan telinga, tetapi sangat berguna untuk mentakrifkannya melalui kumpulan muka.

### Kawasan UV {#uv-regions}

Alat UV Atlas akan cuba mentakrifkan jahitan secara automatik, tetapi kadangkala akan meletakkan jahitan di tempat yang anda tidak mahu. Jika kumpulan muka wujud pada objek, dan pilihan kumpulan muka aktif dalam pilihan UV Atlas, ia akan menggunakan sempadan kumpulan muka sebagai jahitan UV.

### Quad Remesher {#quad-remesher}

Pemalam Quad Remesher biasanya akan mengalirkan sisi dengan cantik pada model anda, tetapi anda boleh menggunakan kumpulan muka untuk membantu mengemudinya apabila pilihan kumpulan muka didayakan. Ini memudahkan anda mentakrifkan aliran sisi yang kemas di sekitar mata, rabung kening, bibir atau lipatan pipi, sebagai contoh.

### Penapis dengan alat lain {#filter-with-other-tools}

Banyak alat mempunyai pilihan untuk mengambil kira kumpulan muka, sama ada daripada menu alat utamanya, atau melalui menu Sapuan -> Penapis. Contohnya, alat pelicin pada kekuatan melebihi 100% boleh melicinkan butiran secara agresif di dalam kumpulan muka, tetapi mengekalkan sempadan kumpulan muka secara relatifnya.

### Santai dan licinkan sempadan kumpulan muka {#relax-and-smooth-facegroup-borders}

Pilihan `Santai` dalam alat kumpulan muka sangat baik untuk melicinkan sempadan kumpulan muka sambil mengekalkan ciri-ciri lain. Ini boleh menjadi cara yang bagus untuk mentakrifkan kawasan sempadan kumpulan muka yang licin sebelum melakukan quad remesh.

## Had pada tablet/telefon mudah alih {#limitations-on-tabletmobile}

Tablet dan telefon mudah alih masa kini sangat berkuasa, tetapi mempunyai perbezaan penting berbanding komputer desktop dan komputer riba:

### Tiada penyejukan aktif {#no-active-cooling}

Komputer mempunyai kipas dan/atau penyerap haba yang besar untuk menyejukkannya, dan direka untuk berjalan pada suhu tinggi. Perkakasan mudah alih biasanya direka untuk menjadi nipis terlebih dahulu, bukan untuk membantu menyejukkan komponen dalamannya. Jika Nomad dipaksa menggunakan tetapan kualiti tertinggi (mod pencahayaan PBR, bahan yang kompleks, banyak objek, banyak pilihan pemprosesan pasca didayakan), ini boleh menyebabkan peranti terlalu panas dan menghabiskan bateri dengan sangat cepat.

Pendekatan yang lebih baik ialah menggunakan mod pencahayaan matcap, dan menggunakan `Resolusi Render` yang lebih rendah (di bahagian atas menu pemprosesan pasca). Pilihan ini akan memastikan peranti kekal sejuk dan membolehkan anda mengukir lebih lama.

### Memori terhad {#limited-memory}

Nomad boleh mencapai hasil yang setara dengan kebanyakan aplikasi ukiran desktop, tetapi ia tidak boleh melanggar hukum fizik! Kebanyakan komputer desktop mempunyai memori dua kali ganda berbanding peranti mudah alih, dan stesen kerja yang dibina untuk animasi 3d selalunya mempunyai memori 4 atau 8 kali ganda. Oleh sebab itu, adalah baik untuk sedar berapa banyak poligon yang anda gunakan; jalankan beberapa ujian pada peranti anda untuk melihat bila ia mula menjadi perlahan. Hampir semua peranti yang boleh menjalankan Nomad boleh mengendalikan 1 juta poligon dengan agak mudah. iPad Pro M2 boleh mengendalikan 8 juta dengan selesa, dan ada orang yang telah menguji pada iPad terkini dengan jumlah yang jauh melebihi itu.

Walau bagaimanapun, hanya ukiran yang paling terperinci memerlukan lebih daripada 4 juta poligon; jika anda membuat objek yang agak ringkas dan sering mendapati diri anda melebihi 500,000, 1 juta atau 4 juta, anda menggunakan terlalu banyak poligon! Pastikan `Shading licin` didayakan dalam [Tetapan](settings.md).

### OS kurang bertolak ansur dengan aplikasi berat {#os-is-less-forgiving-with-intensive-apps}

Apple dan Android menjangkakan aplikasi menyimpan dan memuatkan fail kecil dengan sangat cepat. Mereka juga menganggap aplikasi boleh bertukar tugas dengan sangat cepat. Sekali lagi, Nomad menggunakan beberapa helah pintar untuk memastikan saiz fail agak kecil dan menyimpannya dengan sangat cepat, tetapi jika OS mudah alih memutuskan bahawa Nomad mengambil masa terlalu lama, ia akan terus menamatkannya sebelum tugasnya selesai. Ini satu lagi sebab untuk memastikan fail bersaiz kecil; memang boleh bekerja dengan ukiran 37 juta poligon seperti yang dilaporkan oleh seorang pengguna di discord, tetapi ia tidak disyorkan!

## Bekerja pada skrin kecil {#working-on-small-screens}

Nomad direka untuk berfungsi pada tablet, tetapi juga berfungsi dengan baik pada telefon. Mengukir pada skrin kecil seperti telefon boleh dipermudahkan dengan beberapa pelarasan UI dan aliran kerja:

* Ketikan 4 jari akan menogol keseluruhan UI, memberikan anda lebih ruang untuk mengukir.
* Seretan 3 jari ke atas dan ke bawah akan menukar jejari berus.
* Skala UI boleh dikecilkan untuk memuatkan lebih banyak butang jika penglihatan anda baik, atau dibesarkan jika penglihatan anda kurang baik!
* Menu yang lebih lebar kadangkala boleh menghalang ukiran; anda boleh menjadikannya lut sinar dan tidak kabur supaya anda dapat melihat ukiran di bawah menu.
* Jika mengukir dengan jari, gunakan pilihan [`Ofset strok`](stroke.md#stroke-offset) untuk mengalihkan pusat berus sedikit menjauhi jari anda.
* Pilihan-pilihan ini dan banyak lagi boleh didapati dalam [menu Antara Muka](./interface.md).


## Pengubah bentuk kembung atau puncak {#inflate-or-peak-deformer}

Banyak aplikasi 3d mempunyai pengubah bentuk kembung, yang akan menolak semua verteks mengikut normalnya dengan jumlah yang boleh dikawal. Walaupun Nomad pada masa ini tidak mempunyai pengubah bentuk, tingkah laku ini boleh ditiru dengan berus kembung:

* Pilih berus kembung
* Daripada [menu Sapuan](./stroke.md#stroke), tukar kaedah sapuan kepada `Kunci + jejari`
* Jadikan jejari berus lebih besar daripada ukiran anda; zum keluar kamera menjauhi ukiran jika perlu.
* Klik kemudian seret satu sapuan pada permukaan objek anda; apabila jejari lebih besar daripada objek, keseluruhan bentuk akan dikembungkan secara sekata dengan jumlah yang tetap.
* Laraskan intensiti berus untuk mengawal jumlah kembungan
* Gunakan penopengan jika perlu untuk melindungi atau mengurangkan kesan kembung di kawasan tertentu.

## Membuang bonjolan atau 'jerawat' daripada operasi remesh voxel {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Remesh voxel sangat bagus untuk menghasilkan poligon yang dijarakkan sekata, tetapi kadangkala ia menghasilkan topologi yang menyebabkan bonjolan kecil atau jerawat apabila dilicinkan. Contohnya:

* Gunakan berus alur tajam pada sfera lalai dan buat satu pusaran
* Lakukan remesh voxel dengan `Bina multiresolusi` pada 3
* Licinkan dengan intensiti tinggi
* artifak muncul (lebih mudah dilihat dengan bahan matcap yang berkontras tinggi):

![](/videos/tip_pimples_before.mp4)

Untuk membaikinya melalui pengukiran, cuba pilihan `Melicinkan stabil` dalam tetapan pelicin. Pilihan ini boleh mengendalikan susun atur topologi remesh voxel yang tidak sekata, dan memberikan hasil yang bersih.

![](/videos/tip_pimples_stable_smooth.mp4)

Untuk membaiki topologi itu sendiri, gunakan primitif baharu, atau alat quad remesh, atau aplikasi pemodelan 3d luaran, dan unjurkan butiran daripada mesh asal ke mesh baharu melalui `Topologi -> Bake -> Unjur semula → Verteks`.

![](/videos/tip_pimples_reproject.mp4)

## Pencahayaan siang {#daylight-lighting}

Render PBR lalai, seperti namanya, adalah berasaskan fizik, dan seperti foto digital yang belum diproses, ia boleh kelihatan sedikit pudar dan mendatar. Lampu dan pemprosesan pasca Nomad boleh digunakan untuk menjadikan render kelihatan lebih bertenaga.

Berikut ialah render lalai; mari kita lihat jika kita boleh menjadikannya lebih cantik:
![](/images/tips_lighting_default.webp)

Mendayakan pemprosesan pasca dan pemetaan nada boleh menambah kecerahan dan kontras:

![](/images/tips_lighting_tonemap.webp)

Beralih kepada lampu pula, lampu persekitaran lalai sesuai untuk mengukir, tetapi boleh diperbaiki untuk render akhir. Satu cara untuk memikirkannya ialah dengan memisahkan cahaya langsung (contohnya matahari) daripada cahaya persekitaran (contohnya cahaya daripada birunya langit dan tanah). Dengan mengurangkan cahaya persekitaran dan memutarnya, kita mula menangkap rupa pencahayaan sekiranya subjek berada di kawasan yang teduh:

![](/images/tips_lighting_env.webp)

Lampu langsung boleh ditambah, dan intensitinya dinaikkan untuk menyimulasikan cahaya matahari yang terik. Mengimbanginya dengan lampu persekitaran akan memberikan hasil yang menyenangkan:

![](/images/tips_lighting_sunlight.webp)

Watak boleh mendapat manfaat dengan menukar bahannya kepada bawah permukaan (subsurface), dan meletakkan lampu spot di belakang watak yang menghala ke telinga supaya telinganya kelihatan bercahaya:

![](/images/tips_lighting_sss.webp)

Kemudian bereksperimenlah dengan tetapan pemprosesan pasca yang lain! Pencahayaan Global dan Oklusi Ambien membantu menghasilkan pencahayaan yang lebih realistik. Kelengkungan dan Tajamkan boleh membantu menonjolkan lebih banyak butiran dalam ukiran. Aberasi Kromatik, Kedalaman Medan, Bijian, Pemekaran dan Vinyet membantu menyimulasikan kesan kamera. Ambil perhatian bahawa apabila lebih banyak ciri didayakan, nilai pencahayaan dan pemprosesan pasca yang lain perlu dilaraskan untuk mengimbanginya.

Berikut ialah render dengan set penuh pelarasan pemprosesan pasca:
![](/images/tips_lighting_final.webp)

# ![](/icons/manual.webp) Petua

[[toc]]

## Cara memulakan model

Pemula dalam pengukiran 3D sering bertanya apakah cara terbaik untuk memulakan model. Tiada cara yang paling baik, setiap orang ada keutamaan berbeza. Berikut beberapa pendekatan yang lebih lazim.

### Mengukir pada sfera, multires

Model lalai apabila Nomad dilancarkan ialah cara yang paling biasa. Gunakan alat move, clay, crease untuk menolak dan menarik sfera menjadi bentuk, gunakan aras subdivisi lebih rendah apabila anda mahu membuat perubahan besar dengan cepat, gunakan aras subdivisi lebih tinggi untuk kerja perincian.

Masalah biasa ialah anda sering kehabisan poligon di tempat yang anda perlukan, sementara anda mempunyai terlalu banyak poligon di tempat lain. Contohnya jika anda menolak sfera lalai menjadi satu badan penuh, besar kemungkinan anda tidak mempunyai cukup perincian untuk membuat jari, sementara anda akan mempunyai banyak poligon terbuang di belakang kepala. Untuk bentuk yang kebanyakannya sfera seperti kepala, ini mungkin memadai.

### Dyntopo

Mengaktifkan Dyntopo akan secara adaptif menambah dan membuang poligon ketika anda mengukir. Poligon ini akan berupa segi tiga, dan pemula selalunya tidak menyukai susun atur yang berselerak berbanding rupa multires yang kemas. Ia berbaloi untuk diteruskan! Jika anda menghidupkan smooth shading, mematikan wireframe dan berhenti risau tentang susun atur, mod ini boleh memberi rasa seperti tanah liat. Jangan lupa jika anda menggunakan berus besar, atau berus smooth, mod ini juga boleh membuang poligon, jadi alat sentiasa terasa pantas dan responsif. Setelah anda menyiapkan laluan pertama ukiran, anda boleh mengklonnya dan menjalankannya melalui quad remesher untuk mendapatkan susun atur yang baik, dan memprojek semula perincian asal ke aras subdivisi tinggi.

### Voxel remesh

Voxel remesh akan mengenakan topologi berasaskan quad pada ukiran anda. Operasi ini pantas pada resolusi rendah, dan boleh digunakan untuk dengan cepat menggantikan poligon yang diregangkan atau terlalu padat dengan susun atur yang jaraknya sekata. Ini boleh menjadi cara yang baik untuk memulakan satu badan penuh daripada sfera; katakan anda bermula dengan kepala, anda boleh meregangkan leher, voxel remesh. Regangkan badan, voxel remesh, lengan, voxel remesh, dan seterusnya, sehingga anda mendapat bentuk asas.

### Guna objek berbilang

Banyak panduan anatomi akan mewakili badan daripada sfera, silinder, kubus ringkas. Anda juga boleh mengukir dengan cara ini dalam Nomad. Ini mempunyai kelebihan membolehkan anda mem‑parent objek bersama dalam hierarki adegan, jadi anda boleh memutar leher dan kepala akan mengikut, sebagai contoh. Keupayaan menggunakan alat gizmo untuk terjemahan/putaran/skala yang tepat juga sangat berguna, dan anda juga boleh menetapkan pivot per bentuk supaya ia bergerak tepat seperti yang anda jangka. Apabila blok asas berada di tempat yang betul, anda boleh memilih semuanya dan voxel remesh atau boolean menjadi satu permukaan tunggal untuk pengukiran lebih terperinci.

Petua berguna untuk cara kerja ini ialah bermula dengan sfera, skala menjadi sosej yang memanjang, tekan pivot, klik 'bottom', tekan pivot lagi. Kini anda mempunyai bahagian badan yang boleh diklon, diterjemah sepanjang panjang sfera pertama, diklon, diputar, diklon, digelincir, diklon dan sebagainya untuk menyusun badan dengan cepat.

### Tubes

Alat tube ialah cara yang hebat untuk memulakan ukiran. Ekor reptilia, lengan, kaki, jari, kening, semuanya boleh dilakar dengan cepat menggunakan alat tube, kemudian mudah disunting selepas itu. Ia juga membolehkan anda mengubah profil keratan rentas, membolehkan perubahan bentuk pantas. Anda boleh memvalidasi bentuk untuk mula mengukir padanya, dan voxel remesh bersama objek lain untuk mendapatkan mesh badan penuh.

### Guna aplikasi lain

Sesetengah orang lebih suka memulakan model dalam aplikasi lain, itu juga tidak mengapa. Alat seperti Blender atau Valence membenarkan model dimulakan menggunakan teknik low poly, kemudian boleh diimport ke dalam Nomad untuk diukir.

### Guna preset terbina dalam

Daripada menu project klik `Preset...` di bahagian kanan atas. Di sini anda akan menemui beberapa preset bentuk kepala dan badan daripada Blender foundation. Pilih satu yang anda suka, ketik sekali lagi, tambah ke adegan anda. 

### Guna model dalam talian

Terdapat banyak model percuma tersedia dalam talian, contohnya polyhaven, sketchfab, turbosquid. Biasanya model ini boleh diimport ke Nomad, dan sama ada diukir terus, atau digunakan sebagai rujukan.

### Tiada peraturan!

Akhirnya anda boleh menggunakan sebarang gabungan teknik ini, atau langsung tiada! Nomad sangat fleksibel dalam hal ini, pengguna mahir mungkin menggunakan tubes untuk bermula, kemudian dyntopo, kemudian gabung dengan kaki yang dimuat turun, kemudian quad remesh semuanya, kemudian multires untuk perincian akhir. Apa sahaja yang berkesan untuk anda.

## Facegroups

Alat facegroup boleh digunakan untuk banyak perkara, seperti yang diterangkan dalam video youtube ini: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Ini ialah ringkasan teks ciri yang diliputi dalam video tersebut.

### Mengapa facegroups?

Facegroups membolehkan anda mengatur dan memilih faces ('faces' dan 'polygons' digunakan silih ganti dalam manual ini). Ini lebih mudah dijelaskan berbanding alat pemilihan dan pengorganisasian lain dalam Nomad. Nomad membenarkan anda mencipta objek, menamakannya, mem‑parent‑kannya, adalah mudah untuk mencipta struktur objek untuk mentakrifkan bilik yang terdiri daripada lantai, dinding, kerusi, meja dan sebagainya.

Untuk watak anda mungkin melakukan block‑out awal menggunakan objek berasingan untuk kepala, lengan, kaki, tetapi sebaik sahaja anda menggabungkan semua bahagian menjadi satu mesh, struktur ini hilang. Anda boleh bekerja pada sub‑bahagian watak dengan mask, tetapi ia boleh menjadi meletihkan untuk sentiasa melukis mask untuk tangan, kemudian hidung, kemudian tangan lagi.

Di sinilah facegroups berguna. Ia membolehkan anda menanda faces poligon dengan warna, dan kemudian dapat memilih dan memanipulasi poli yang mempunyai warna yang sama. Ambil perhatian bahawa warna facegroup dan warna vertex ialah perkara berbeza.

Analogi paling hampir ialah mewarnakan peta, kemudian kemudian dapat memilih negara atau wilayah berdasarkan warna.

Untuk kepala watak anda boleh mewarnakan zon untuk menanda soket mata, hidung, bibir, dagu, telinga, kemudian dengan mudah memilih zon tersebut kemudian. Untuk pengukiran permukaan keras dan mekanikal ia boleh berguna untuk mentakrifkan panel dan seksyen.

### Mencipta dan menyunting facegroups

Facegroups boleh digunakan dengan berus, di mana setiap sapuan baharu mencipta facegroup baharu, atau ia boleh memilih facegroup di bawah kursor dan melanjutkannya. Ia juga boleh dicipta menggunakan bentuk.

* Dot, auto-pick diaktifkan - satu seretan akan mentakrifkan warna facegroup baharu dan menetapkannya kepada faces yang anda seret. Setiap seretan baharu akan mentakrifkan facegroup baharu. Satu ketikan akan memenuhi facegroup baharu.
* Dot, auto-pick dinyahaktifkan - apabila butang auto-pick berada dalam mod 'sub', Nomad akan memilih facegroup di bawah kursor, dan menerapkannya sepanjang baki seretan. Ini berguna untuk memperhalus facegroups tanpa perlu memilihnya secara manual.

### Masking

Apabila alat mask aktif, dan butang facegroup aktif pada toolbar‑nya, mengetik facegroup akan mem‑mask‑kannya.


### Menyembunyikan

Apabila alat hide aktif, dan butang facegroup aktif pada toolbar‑nya, mengetik facegroup akan menyembunyikannya.

### Mengatur

Seperti yang dinyatakan sebelum ini facegroups boleh digunakan untuk mengatur mesh anda tanpa memerlukan anda membuat objek berasingan. Anda mungkin tidak mahu membahagikan kepala kepada objek berasingan untuk hidung, dagu, telinga, tetapi sangat berguna untuk mentakrifkannya melalui facegroups.

### Rantau UV

Alat UV Atlas akan cuba mentakrifkan seam secara automatik, tetapi kadangkala akan meletakkan seam di tempat yang anda tidak mahu. Jika facegroups wujud pada objek, dan pilihan facegroup aktif dalam pilihan UV Atlas, ia akan menggunakan sempadan facegroup sebagai seam UV sebaliknya.

### Quad remesher

Plugin quad remesher biasanya akan mengalirkan edges dengan baik pada model anda, tetapi anda boleh menggunakan facegroups untuk membantu mengarahkannya apabila pilihan facegroup diaktifkan. Ini boleh memudahkan untuk mentakrifkan aliran edge yang bersih di sekeliling mata, rabung kening, bibir, lipatan pipi sebagai contoh.

### Penapis dengan alat lain

Banyak alat akan mempunyai pilihan untuk sedar facegroup, sama ada daripada menu alat utama mereka, atau melalui menu stroke -> filtering. Contohnya alat smooth pada kekuatan melebihi 100% boleh melicinkan secara agresif perincian dalam facegroup, tetapi mengekalkan sempadan facegroup agak utuh.

### Relax dan smooth sempadan facegroup

Pilihan relax dalam alat facegroup melakukan kerja yang sangat baik untuk melicinkan sempadan facegroup sambil mengekalkan ciri lain utuh. Ini boleh menjadi cara yang baik untuk mentakrifkan rantau sempadan facegroup yang licin sebelum quad remeshing.

## Had pada tablet/peranti mudah alih

Tablet dan peranti mudah alih semasa sangat berkuasa, tetapi mempunyai perbezaan penting berbanding komputer desktop dan komputer riba:

### Tiada penyejukan aktif

Komputer mempunyai kipas dan/atau heatsink besar untuk mengekalkannya sejuk, dan direka untuk berjalan pada suhu tinggi. Perkakasan mudah alih biasanya direka untuk ketipisan dahulu, bukan untuk membantu mengekalkan dalaman sejuk. Jika Nomad didorong ke tetapan kualiti tertingginya (mod pencahayaan PBR, bahan kompleks, banyak objek, banyak pilihan post processing diaktifkan), ini boleh menyebabkan peranti terlalu panas dan menghabiskan bateri dengan sangat cepat. 

Pendekatan yang lebih baik ialah menggunakan mod pencahayaan matcap, dan menggunakan render multiplier yang lebih rendah (bahagian atas menu post process). Pilihan ini akan mengekalkan peranti sejuk dan membolehkan anda mengukir lebih lama.

### Memori terhad

Nomad boleh mencapai hasil yang setara dengan kebanyakan aplikasi pengukiran desktop, tetapi ia tidak boleh melanggar hukum fizik! Kebanyakan komputer desktop mempunyai dua kali ganda memori peranti mudah alih, workstation yang dibina untuk animasi 3D selalunya mempunyai 4x atau 8x memori. Oleh sebab itu, adalah baik untuk peka tentang berapa banyak poligon yang anda gunakan, jalankan beberapa ujian pada peranti anda untuk melihat bila ia mula menjadi lembap. Hampir semua peranti yang boleh menjalankan Nomad boleh mengendalikan 1 juta poligon dengan agak mudah. Ipad Pro M2 boleh mengendalikan 8 juta dengan selesa, orang telah menguji pada Ipad terkini jauh melebihi itu.

Walau begitu, hanya ukiran yang paling terperinci memerlukan lebih daripada 4 juta poli; jika anda membuat objek yang agak ringkas dan mendapati diri anda sering melebihi 500,000, 1 juta, 4 juta, anda menggunakan terlalu banyak poligon! Pastikan anda menghidupkan mod smooth shaded dalam pilihan.

### OS kurang bertolak ansur dengan aplikasi intensif

Apple dan Android menjangka aplikasi akan menyimpan dan memuatkan fail kecil dengan sangat cepat. Mereka juga menganggap aplikasi boleh bertukar tugas dengan sangat cepat. Sekali lagi Nomad melakukan beberapa helah bijak untuk mengekalkan saiz fail agak kecil dan menyimpannya dengan sangat cepat, tetapi jika OS mudah alih memutuskan Nomad mengambil masa terlalu lama, ia akan terus membunuhnya sebelum ia menyelesaikan tugasnya. Ini satu lagi sebab untuk mengekalkan fail pada saiz yang lebih kecil; adalah mungkin untuk bekerja dengan ukiran 37 juta poli seperti yang dilaporkan seorang pengguna di discord, tetapi ia tidak digalakkan!

## Bekerja pada skrin kecil

Nomad direka untuk berfungsi pada tablet, tetapi juga berfungsi dengan baik pada telefon. Mengukir pada skrin kecil seperti telefon boleh dipermudah dengan beberapa pelarasan UI dan aliran kerja:

* Ketikan 4 jari akan menogol keseluruhan UI, memberi anda lebih ruang untuk mengukir.
* Seretan 3 jari ke atas dan ke bawah akan menukar radius berus
* Skala UI boleh dikecilkan untuk memuatkan lebih banyak butang jika anda mempunyai penglihatan yang baik, atau dibesarkan jika penglihatan anda kurang baik!
* Menu yang lebih lebar kadangkala boleh menghalang ukiran, anda boleh menjadikannya lutsinar dan tidak blur untuk membolehkan anda melihat ukiran di bawah menu.
* Jika mengukir dengan jari, gunakan pilihan offset untuk mengalihkan pusat berus sedikit jauh dari jari anda.
* Ini dan banyak lagi pilihan boleh ditemui dalam [Interface menu](./interface.md). 


## Inflate atau peak deformer

Banyak aplikasi 3D mempunyai inflate deformer, yang akan menolak semua vertex sepanjang normal masing‑masing dengan jumlah yang boleh dikawal. Walaupun Nomad pada masa ini tiada deformers, adalah mungkin untuk meniru tingkah laku ini dengan berus inflate:

* Pilih berus inflate
* Daripada [Stroke menu](./stroke.md#stroke) tukar kaedah stroke kepada `Lock + Radius'
* Jadikan radius berus lebih besar daripada ukiran anda, zum kamera menjauh dari ukiran jika perlu.
* Klik kemudian seret stroke pada permukaan objek anda; apabila radius lebih besar daripada objek, keseluruhan bentuk akan di‑inflate secara sekata dengan jumlah tetap.
* Laraskan intensiti berus untuk mengawal jumlah inflate
* Gunakan masking jika perlu untuk melindungi atau mengurangkan kesan inflate di kawasan tertentu.

## Menghapuskan bonjolan atau 'jerawat' daripada operasi voxel remesh

Voxel remesh bagus untuk menghasilkan poligon yang jaraknya sekata, tetapi kadangkala mencipta topologi yang akan menyebabkan bonjolan kecil atau jerawat apabila di‑smooth. Contohnya:

* Gunakan berus crease pada sfera lalai dan buat pusaran
* Voxel remesh dengan 'build multiresolution at 3'
* Smooth dengan intensiti tinggi
* artifak muncul (lebih mudah dilihat dengan bahan matcap kontras tinggi):

![](/videos/tip_pimples_before.mp4)

Untuk membaiki melalui pengukiran, cuba pilihan `Stable smoothing` dalam tetapan smooth. Ini boleh menangani susun atur topologi tidak sekata daripada voxel remesh, dan mendapatkan hasil yang bersih.

![](/videos/tip_pimples_stable_smooth.mp4)

Untuk membaiki topologi itu sendiri, gunakan primitif baharu, atau alat quad remesh, atau pemodel 3D luaran, dan projek perincian daripada mesh asal ke mesh baharu melalui `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Pencahayaan siang hari

Render PBR lalai adalah, seperti namanya, berasaskan fizikal, yang seperti foto digital tidak diproses boleh kelihatan sedikit pudar dan rata. Lampu dan post processing Nomad boleh digunakan untuk menjadikan render kelihatan lebih bertenaga.

Berikut ialah render lalai, mari lihat jika kita boleh menjadikannya lebih baik:
![](/images/tips_lighting_default.webp)

Mengaktifkan post processing dan tonemapping boleh menambah kecerahan dan kontras:

![](/images/tips_lighting_tonemap.webp)

Untuk memberi tumpuan pada lampu, lampu persekitaran lalai bagus untuk mengukir, tetapi boleh diperbaiki untuk render akhir. Satu cara untuk memikirkannya ialah memisahkan cahaya langsung (contohnya matahari) vs cahaya persekitaran (contohnya cahaya daripada biru langit, tanah). Dengan mengurangkan cahaya persekitaran dan memutarkannya, ini mula menangkap rupa pencahayaan jika subjek berada di kawasan teduh:

![](/images/tips_lighting_env.webp)

Cahaya langsung boleh ditambah, dan intensitinya dipertingkatkan untuk mensimulasikan cahaya matahari yang terik. Mengimbangi ini dengan cahaya persekitaran akan menghasilkan hasil yang menyenangkan:

![](/images/tips_lighting_sunlight.webp)

Watak boleh mendapat manfaat daripada menukar bahan mereka kepada subsurface, dan meletakkan spotlight di belakang watak menghala ke telinga untuk menjadikannya bercahaya:

![](/images/tips_lighting_sss.webp)

Kemudian bereksperimen dengan selebihnya tetapan post process! Global Illumination dan Ambient Occlusion membantu dengan pencahayaan yang lebih realistik. Curvature dan Sharpen boleh membantu menyerlahkan lebih banyak perincian dalam ukiran. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette membantu mensimulasikan kesan kamera. Ambil perhatian bahawa apabila ciri diaktifkan, pencahayaan dan nilai post processing lain perlu dilaraskan untuk mengimbangi.

Berikut render dengan set penuh pelarasan post processing:
![](/images/tips_lighting_final.webp)

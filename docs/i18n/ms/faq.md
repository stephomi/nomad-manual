# ![](/icons/faq.webp) Soalan Lazim {#faq}

[[toc]]

## Platform {#platform}
### Di manakah projek saya disimpan pada peranti? {#locate}
Projek terletak dalam folder `projects` di dalam folder utama Nomad.

Di iOS, anda boleh mengakses folder Nomad dengan aplikasi Files iOS.

Di Android, folder Nomad berada di `Android/data/com.stephaneginier.nomad/files/`.  
Pada versi Android terkini (10/11), anda tidak lagi mempunyai akses kepada folder `Android/data`.
Anda boleh mengaksesnya melalui aplikasi berasingan, contohnya [aplikasi ini](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Adakah terdapat cara untuk menguji beta? {#beta}
Untuk Windows & MacOS, versi beta mungkin tersedia di [Laman Utama](https://nomadsculpt.com).
<br>
Untuk iOS terdapat TestFlight peribadi, lawati [Discord](https://discord.com/invite/8h7BwpRz29) dalam saluran #beta-ios.
<br>
[Demo Web](https://nomadsculpt.com/demo) biasanya dikemas kini dengan ciri-ciri terkini.

### Mengapa ada percubaan percuma di Android tetapi tidak di iOS? {#android-trial}
Kerana peranti Android lama kurang berkuasa (dan sesetengah yang baharu juga...), dan saya tidak mahu orang membeli aplikasi dan disambut dengan skrin hitam.
Tetapi sebab utama ialah saya rasa aplikasi berbayar di Android bukanlah kebiasaan.

### Apakah tablet terbaik untuk menjalankan Nomad? {#best-tablet}

Ringkasan: iPad.

Jawapan yang sedikit lebih panjang ialah 

> "iPad terbaru _yang anda mampu_, kecuali anda benar-benar tidak suka Apple, dalam kes itu tablet Samsung terbaru yang anda mampu. Selain itu, uji dahulu." 

Orang selalunya mahukan lebih banyak maklumat, jadi berikut ringkasannya.

Nomad berjalan paling baik pada iPad yang lebih baharu:

* iPad dan iPhone boleh mengakses pemalam [Quad Remesher](tools#quad-remesher) daripada [Exoside](https://exoside.com/)
* iPad terkini dengan pensel terbaru menyokong [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), anda boleh memusingkan pensel dalam sesetengah alat di Nomad. 
* prestasi cip siri M terkini sangat pantas. 

iPad paling baharu dan paling mahal akan dapat merender imej akhir dengan sangat pantas, dan membenarkan anda mengukir dengan perincian yang sangat tinggi.

Walau bagaimanapun, penurunan prestasi pada iPad yang lebih murah dan lama tidak seteruk yang dijangka. Mana-mana iPad yang menyokong Apple Pencil menjalankan Nomad dengan agak baik. Sebagai contoh:

* iPad Pro dari 2023 boleh mengendalikan ukiran 5 juta poligon dan masih responsif, imej berkualiti akhir boleh dirender dalam 5 saat.
* iPad Pro dari 2015 boleh mengendalikan objek 1.2 juta poligon dengan sedikit lengah, imej berkualiti akhir boleh dirender dalam 20 saat.

Itu perbezaan prestasi yang besar, tetapi anda juga perlu mengambil kira harga:

* iPad Pro 2025 berharga *$2500 USD* baharu dengan semua pilihan. 
* iPad Pro 2023 kini berharga *$400 USD* di eBay.
* iPad Pro 2015 berharga *$250 USD* di eBay.

Adakah tambahan 4 juta poligon dan jimat 15 saat berbaloi dengan $2100? Itu terpulang kepada anda.

Model bukan Pro boleh jadi lebih murah dan memberikan pelbagai saiz dan prestasi untuk dipilih. iPad Air semasa menyokong Pencil gen 2 dengan barrel roll, dan jauh lebih murah daripada Pro. Pasaran terpakai dan diperbaharui mempunyai lebih banyak pilihan lagi. 

Ini bermakna apa pun bajet anda, anda sepatutnya boleh mencari iPad yang sesuai. Dan ingat bahawa kebanyakan ukiran bukan berjuta-juta poligon! Jika anda boleh kekal di bawah 500,000 poligon, iPad lama sekalipun akan membenarkan anda mengukir dengan pantas.

`Bagaimana dengan Android?`

Prestasi grafik Android adalah di bawah iPad. Menurut pembangun Nomad, "Samsung Galaxy Tab S9 akan menjalankan Nomad kira-kira satu tertib magnitud lebih perlahan daripada iPad Air". Walau begitu ramai pengguna sangat berpuas hati dengan tablet Samsung mereka, Nomad berjalan dengan baik untuk kebanyakan kerja mengukir. 

Untuk tablet Android lain, berhati-hati. Perkakasan Android boleh berbeza jauh dari segi prestasi, tidak mudah untuk meramal bagaimana Nomad akan berjalan.

Sila gunakan versi percuma tanpa fungsi simpan Nomad untuk menguji dahulu. 

`Bagaimana dengan memori dan storan?`

Kebanyakan fail Nomad biasanya 100mb atau kurang. Ini bermakna hampir mana-mana tablet yang anda beli hari ini, iPad atau Android, akan mempunyai ruang yang mencukupi untuk projek Nomad anda.


### Saya membeli Nomad untuk satu peranti, bolehkah saya gunakannya pada peranti lain? {#multi-devices}
Selagi ia menggunakan gedung aplikasi dan akaun yang sama, boleh.

Sebagai contoh jika anda membelinya di App Store iOS, anda boleh menggunakannya pada peranti iOS anda yang lain.

Jika anda membelinya untuk tablet Android anda di Google Play, anda boleh menggunakannya pada peranti Android anda yang lain.

Namun jika anda membeli Nomad di Android, kemudian anda mendapat iPad, anda perlu membelinya sekali lagi.

Ini kerana Nomad tidak mempunyai pelayan lesen sendiri atau model langganan. Tiada perjanjian antara Apple/Google/AppGallery untuk mengendalikan perkongsian lesen. 


### Bagaimana untuk memulihkan pembelian saya? {#restore}
Google Play dan AppGallery kedua-duanya mengendalikan penyegerakan secara automatik.

- Pergi ke menu About (ikon nomad di kiri atas), dan tekan `restore purchase`
- Pastikan anda log masuk ke akaun yang sama yang anda gunakan untuk membeli Nomad (di Google Play).
- Mulakan semula peranti
- Kadangkala anda perlu menunggu beberapa jam
- Pastikan aplikasi Google Play adalah versi terkini
- Pasang semula Nomad (pastikan anda [sandarkan fail anda](#where-are-my-projects-located-on-my-device) jika anda tidak mahu kehilangan apa-apa)
- Anda boleh cuba membeli sekali lagi untuk melihat apa yang berlaku (nota: anda tidak boleh membeli item yang sama dua kali pada akaun yang sama)

:::tip
Anda boleh menghubungi saya di <support@nomadsculpt.com> tetapi *satu-satunya* perkara yang saya boleh lakukan ialah mengesahkan sama ada sesuatu emel mempunyai pembelian yang dikaitkan dengannya.

Perlu diingat bahawa saya kerap menerima laporan berkaitan lesen yang tidak dikemas kini dengan betul selepas memperoleh peranti baharu.
Saya tidak mempunyai sebarang kawalan ke atas pembayaran dan penyegerakan akaun, semuanya dikendalikan oleh Google/AppGallery!

Akhirnya pembelian sentiasa dipulihkan, tetapi langkah yang diperlukan untuk mempercepatkan proses ini tidak jelas.
:::

::: warning
Peranti Huawei terkini tidak mempunyai akses kepada perkhidmatan Google.
Dalam kes itu anda perlu membeli aplikasi sekali lagi di AppGallery (gedung aplikasi Huawei).
:::

### Bolehkah anda menterjemah atau membetulkan [bahasa-saya]? {#locale}
Saya agak mudah untuk menambah bahasa lain, tetapi saya bergantung pada terjemahan AI kerana ia jauh lebih mudah untuk diurus bagi kemas kini berkala.
Fail terjemahan boleh didapati [di sini](https://github.com/stephomi/nomad-translation).

## Ciri {#features}

### Mengapa gizmo tidak bergerak? {#gizmo-not-moving}
Anda mungkin mempunyai [pin diaktifkan dalam bar alat menu kiri](tools#left-menu-toolbar). 

### Bolehkah kita buat animasi dalam Nomad? {#animate}
Buat masa ini tidak. Ciri garis masa yang boleh menganimasikan lapisan mungkin menarik, tetapi belum benar-benar dirancang pada masa ini.  

Saya ingin menyokong rigging/skinning pada masa hadapan, tetapi ia menimbulkan beberapa cabaran (terutamanya interaksi dengan alat mengukir...) jadi belum pasti buat masa ini.


### Bolehkah kita lakukan pemodelan low-poly yang betul? {#lowpoly}
Buat masa ini tidak.
Ini bukan benar-benar skop Nomad *Sculpt*, tetapi mungkin saya akan menyediakan beberapa alat pada masa hadapan.


### Bolehkah kita lakukan UV dan tekstur? {#texturing}
Jawapan ringkas: Ya. Jawapan panjang: Bukan secara langsung, tetapi terdapat beberapa cara untuk menggabungkan alat cat verteks Nomad yang sangat baik dengan uv dan tekstur.

* Nomad membenarkan anda mengecat warna, kekasaran, sifat bahan terus ke verteks ukiran anda.
* Nomad membenarkan kiraan verteks yang sangat tinggi supaya anda boleh mengecat tanpa risau tentang uv.
* Nomad boleh memuatkan tekstur untuk digunakan dalam berus, membolehkan stamping dan mengecat dengan tekstur.
* Nomad boleh memuatkan objek yang telah ditetapkan tekstur, untuk tujuan rendering.
* Nomad boleh [UV unwrap](topology.md#uv-unwrap) objek low-poly.
* Warna/kekasaran/ketulinan logam boleh dipindahkan daripada tekstur ke verteks melalui [pilihan projek](topology.md#reproject-to-vertex).
* Warna/kekasaran/ketulinan logam/normal boleh dibakar daripada verteks ke tekstur melalui [pilihan baking](topology.md#bake-to-texture)
* Baking dan project boleh dikendalikan antara objek tunggal atau banyak objek, atau antara tahap subdivisi tertinggi dan terendah bagi objek tunggal, membolehkan pelbagai aliran kerja bake dan project.
* Selepas baking, mengeksport obj juga akan mengeksport tekstur, yang boleh dibawa ke aplikasi seperti Procreate untuk mengecat terus pada tekstur.

### Bolehkah saya merakam video turntable? {#video}
Tidak dirancang buat masa ini, iOS mempunyai [ciri rakaman video](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) yang sangat mudah digunakan.

Di iOS, ini dilakukan dengan meleret ke bawah dari kiri atas, dan mengetik butang rakam. Ia akan memberikan kiraan undur 3 saat, leret menu ke atas untuk memaparkan Nomad, dan gunakan ciri turntable. Apabila selesai, leret ke bawah sekali lagi dari kanan atas, dan ketik butang rakam sekali lagi. Sunting video dari pustaka foto untuk membuang rakaman berlebihan di awal dan akhir video.

### Bolehkah anda menambah [ciri-kegemaran] sebagai butang aras teratas? {#interface}
Ya, bar alat bawah kini boleh disesuaikan dari menu [interface](interface.md), dan bar alat terapung kini boleh dicipta.

### Apakah ciri seterusnya? {#next-features}
Untuk pelan jangka sederhana/panjang saya mempunyai banyak idea tetapi belum pasti lagi.  

Pembaikan pepijat dan penambahbaikan ciri sedia ada sentiasa mempunyai keutamaan lebih tinggi berbanding menambah ciri baharu.


### Bolehkah kita rig dalam Nomad? {#rigging}
Tidak, tetapi ia dirancang. Buat masa ini anda boleh parent bentuk bersama dan mengubah titik pivot, membolehkan ukiran mudah yang boleh diposisikan.

### Bolehkah kita gunakan lebih daripada 4 lampu? {#lights}
Tidak, ini adalah had enjin render masa nyata dalam Nomad. Adalah mungkin untuk memalsukannya menggunakan objek emissive dan global illumination dalam pasca proses, seperti yang ditunjukkan dalam [tutorial ini](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Bolehkah kita import Zbrush tools? {#zbrush-import}
Tidak, Zbrush menggunakan format proprietari. Anda sepatutnya boleh mengekstrak peta alpha dan menggunakannya dalam Nomad. 

### Mengapa warna tidak sepadan dengan apa yang saya lukis? Mengapa saya tidak boleh dapatkan warna putih dalam render? {#paint-pbr}
Bayangkan mengambil foto sekeping kertas, berbanding foto lampu meja, berbanding foto matahari. Kamera dan skrin lama hanya akan menjadikan semuanya ‘putih’. Sistem yang lebih moden boleh menunjukkan perbezaan antara putih pantulan kertas berbanding cahaya yang dipancarkan lampu, berbanding super terang matahari.

Grafik komputer moden cuba berfungsi dengan cara yang serupa, meniru fizik cahaya dan permukaan. Ini dipanggil `Physically Based Rendering`, atau PBR, dan renderer PBR Nomad berasaskan perkara ini. Ia kelihatan realistik dan seimbang, tetapi selalunya warna terang yang dicat akan kelihatan lebih gelap.

Jika anda perlukan render lebih hampir sepadan dengan warna yang dicat, anda boleh membetulkannya dengan cara bukan fizikal dan fizikal:

Bukan PBR:
* `Gunakan mod 'Unlit' dalam menu pencahayaan`. Warna akan dipaparkan tepat seperti yang dicat, tetapi anda juga kehilangan semua pembayangan. Berguna untuk semakan pantas, dan output yang lebih grafik.
* `Gunakan mod 'Matcap' dalam menu pencahayaan`. Pilih matcap yang lebih cerah yang kebanyakannya putih, tanpa ton warna.

PBR:
* `Gunakan persekitaran neutral`. Anda boleh [menukar persekitaran](shading.md#environment) kepada yang lebih neutral. Elakkan persekitaran dalaman kerana ia cenderung lebih berwarna. Lebih baik gunakan persekitaran luar siang hari atau studio.
* `Tingkatkan pencahayaan`. Jika anda mengambil foto kertas putih dalam bilik gelap, anda hanya akan menambah lebih banyak cahaya. Pada cahaya persekitaran, naikkan peluncur exposure sehingga warna mula terasa betul bagi anda, atau tambah lebih banyak lampu individu dengan intensiti lebih tinggi.
* `Tingkatkan exposure kamera`. Jika bilik gelap itu tidak mempunyai lampu tambahan, anda boleh biarkan kamera membuka shutter lebih lama, atau gunakan ISO yang lebih sensitif. Dalam Nomad anda boleh mencapai hasil serupa dengan pasca proses. Pergi ke post process, aktifkan, turun ke tone mapping, aktifkan, dan naikkan peluncur exposure sehingga warna terasa betul.
* `Gunakan warna emissive`. Dalam menu material, anda boleh mengaktifkan 'emissive' di bawah textures, yang akan menjadikan objek kelihatan seperti sumber cahaya. Jika anda menghidupkan global illumination dalam tetapan post process, ia akan memancarkan cahaya ke objek lain dalam adegan. Anda juga boleh mengaktifkan 'unlit' untuk material tersebut, yang akan mencapai rupa yang serupa tanpa tekstur.

## Ralat & Runtuhan {#crashes}

### Aplikasi ranap apabila saya simpan atau remesh model! {#crash-remesh}
Peranti anda kehabisan memori (RAM).  
Untuk mengurangkan penggunaan memori dalam adegan anda, anda boleh menggunakan beberapa pilihan [Topology](topology.md) untuk mengurangkan bilangan poligon.

::: tip RAM/Storan
Apa yang penting ialah jumlah RAM, bukan storan (yang biasanya jauh lebih besar).
:::


### Aplikasi ranap apabila saya muatkan projek! {#crash-load}
Jika fail kecil, anda boleh menghantarnya kepada saya dan saya akan lihat (melalui emel <support@nomadsculpt.com>).

Jika tidak, peranti mungkin kehabisan memori RAM.

- Pastikan anda menutup mana-mana aplikasi lain yang dibuka pada peranti anda.
- Mulakan projek baharu dalam Nomad dan bukannya mempunyai projek sedang dibuka.
- Jika masih runtuh, satu-satunya penyelesaian ialah memuatkan [fail projek anda](#where-are-my-projects-located-on-my-device) pada peranti dengan lebih banyak memori.

::: tip
Pada pelayar desktop, anda boleh cuba memuatkan fail anda [di url ini](https://nomadsculpt.com/demo_save/) dan kemudian mengeksportnya semula selepas memudahkan adegan anda.

Sesetengah pelayar mengehadkan jumlah RAM yang boleh diambil oleh satu tab, jadi ada kemungkinan teknik ini tidak akan berfungsi.

Jika projek anda menggunakan [Layers](layers.md), anda mungkin mahu squash lapisan untuk mengurangkan penggunaan memori.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Aplikasi ranap apabila saya mula Nomad! {#crash-start}
Jika ia runtuh ketika memuatkan, ini bermakna Nomad bergelut dengan fail tertentu yang terdapat dalam folder Nomad.

Kebanyakan masa, ia berlaku kerana projek terlalu berat dan malangnya akan melebihi had RAM.

Cari lokasi [folder Nomad](#where-are-my-projects-located-on-my-device), kemudian tukar nama atau pindahkan beberapa fail untuk mencari puncanya.

Mula-mula, cuba tukar nama `settings.json`. Dengan itu ia akan berhenti memuatkan projek terakhir.

Jika tidak berjaya, cuba pindahkan beberapa fail terkini keluar dari folder sumber masing-masing (`projects`, `matcaps`, `environments`, dan lain-lain).

Anda juga boleh menukar nama folder itu sendiri supaya Nomad mengabaikannya sepenuhnya.
Jika anda menukar nama atau memindahkan semua fail dalam folder Nomad, ini akan memberikan hasil yang sama seperti pemasangan bersih.

::: tip
Apabila Nomad memuatkan fail semasa permulaan, ia sentiasa memindahkan fail ke folder `can_be_deleted/`.
Jika operasi berjaya, ia kemudian dipindahkan kembali ke folder asalnya.

Jika ia runtuh sebelum pemuatan selesai, maka Nomad akan dilancarkan dengan jayanya pada permulaan seterusnya, kerana ia mengabaikan folder `can_be_deleted/`.

Anda boleh cuba memuatkan fail ini sekali lagi jika anda fikir ia boleh berjaya.
:::
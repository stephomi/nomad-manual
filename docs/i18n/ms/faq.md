# ![](/icons/faq.webp) Soalan Lazim {#faq}

[[toc]]

## Platform {#platform}
### Di manakah projek saya disimpan pada peranti saya? {#locate}
Projek disimpan dalam folder `projects` di dalam folder utama Nomad.

Pada iOS, anda boleh mengakses folder Nomad dengan aplikasi Files iOS.

Pada Android, folder Nomad terletak di `Android/data/com.stephaneginier.nomad/files/`.  
Pada versi Android terkini (10/11), anda tidak lagi mempunyai akses ke folder `Android/data`.
Anda boleh mengaksesnya melalui aplikasi lain, contohnya [yang ini](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Adakah cara untuk menguji versi beta? {#beta}
Untuk Windows & MacOS, versi beta mungkin tersedia di [Laman Utama](https://nomadsculpt.com).
<br>
Untuk iOS, terdapat TestFlight peribadi; kunjungi [Discord](https://discord.com/invite/8h7BwpRz29) di saluran #beta-ios.
<br>
[Demo Web](https://nomadsculpt.com/demo) biasanya dikemas kini dengan ciri-ciri terkini.

### Mengapa ada percubaan percuma pada Android, tetapi tidak pada iOS? {#android-trial}
Kerana peranti Android lama memang teruk (dan ada juga yang baharu...), dan saya tidak mahu orang membeli aplikasi ini lalu disambut dengan skrin hitam.
Tetapi sebab utamanya ialah saya rasa aplikasi Android berbayar bukanlah sesuatu yang biasa.

### Apakah tablet terbaik untuk menjalankan Nomad? {#best-tablet}

Ringkasnya: iPad.

Jawapan yang sedikit lebih panjang ialah

> "iPad terbaharu _yang mampu anda beli_, kecuali jika anda benar-benar bencikan Apple, maka tablet Samsung terbaharu yang mampu anda beli. Selain itu, uji dahulu."

Orang selalu mahukan maklumat lanjut, jadi berikut ialah ringkasannya.

Nomad berjalan paling baik pada iPad yang lebih baharu:

* iPad dan iPhone boleh mengakses pemalam [Quad Remesher](tools#quad-remesher) daripada [Exoside](https://exoside.com/)
* iPad terkini dengan pensel terbaharu menyokong [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), jadi anda boleh memusingkan pensel dalam alat tertentu di Nomad.
* prestasi cip siri M terkini sangat pantas.

iPad terbaharu yang paling mahal akan dapat merender imej akhir dengan sangat cepat, dan membolehkan anda mengukir dengan sangat banyak butiran.

Namun, penurunan prestasi pada iPad yang lebih murah dan lebih lama tidaklah seteruk yang disangka. Mana-mana iPad yang menyokong Apple Pencil menjalankan Nomad dengan agak baik. Contohnya:

* iPad Pro dari tahun 2023 boleh mengendalikan ukiran 5 juta poligon dan kekal responsif, dan imej berkualiti akhir boleh dirender dalam 5 saat.
* iPad Pro dari tahun 2015 boleh mengendalikan objek 1.2 juta poligon dengan sedikit kelambatan, dan imej berkualiti akhir boleh dirender dalam 20 saat.

Itu perbezaan prestasi yang besar, tetapi anda juga perlu mengambil kira harganya:

* iPad Pro 2025 berharga *$2500 USD* baharu dengan semua pilihan.
* iPad Pro 2023 kini berharga *$400 USD* di eBay.
* iPad Pro 2015 berharga *$250 USD* di eBay.

Adakah mendapat tambahan 4 juta poligon dan menjimatkan 15 saat berbaloi dengan $2100? Itu terpulang kepada anda.

Model bukan Pro boleh menjadi lebih murah lagi dan menawarkan pelbagai saiz dan prestasi untuk dipilih. iPad Air semasa menyokong pensel generasi kedua dengan barrel roll, dan jauh lebih murah daripada Pro. Pasaran terpakai dan diperbaharui menawarkan lebih banyak pilihan.

Ini bermakna walau berapa pun bajet anda, anda sepatutnya dapat mencari iPad yang sesuai. Dan ingat, kebanyakan ukiran tidak mencecah jutaan poligon! Jika anda dapat kekal di bawah 500,000 poligon, iPad lama pun akan membolehkan anda mengukir dengan pantas.

`Bagaimana pula dengan Android?`

Prestasi grafik Android adalah lebih rendah daripada iPad. Menurut pembangun Nomad, "Samsung Galaxy Tab S9 akan menjalankan Nomad sepuluh kali ganda lebih perlahan daripada iPad Air". Walau bagaimanapun, ramai pengguna sangat berpuas hati dengan tablet Samsung mereka, dan Nomad berjalan dengan baik untuk kebanyakan kerja mengukir.

Untuk tablet Android yang lain, berhati-hati. Prestasi perkakasan Android boleh berbeza dengan ketara, jadi sukar untuk meramal bagaimana Nomad akan berjalan.

Sila gunakan versi percuma Nomad (dengan fungsi simpan dinyahdayakan) untuk menguji dahulu.

`Bagaimana pula dengan memori dan storan?`

Kebanyakan fail Nomad bersaiz 100mb atau kurang. Ini bermakna hampir mana-mana tablet yang anda beli sekarang, sama ada iPad atau Android, akan mempunyai ruang yang lebih daripada cukup untuk projek Nomad anda.


### Saya membeli Nomad untuk satu peranti, bolehkah saya menggunakannya pada peranti lain? {#multi-devices}
Boleh, asalkan ia menggunakan gedung aplikasi yang sama dan akaun yang sama.

Contohnya, jika anda membelinya di App Store iOS, anda boleh menggunakannya pada peranti iOS anda yang lain.

Jika anda membelinya untuk tablet Android anda di Google Play, anda boleh menggunakannya pada peranti Android anda yang lain.

Namun, jika anda membeli Nomad pada Android, kemudian anda mendapat iPad, anda perlu membelinya sekali lagi.

Ini kerana Nomad tidak mempunyai pelayan lesen atau model langganan sendiri. Tiada perjanjian antara Apple/Google/AppGallery untuk mengendalikan perkongsian lesen.


### Bagaimana untuk memulihkan pembelian saya? {#restore}
Google Play dan AppGallery kedua-duanya mengendalikan penyegerakan secara automatik.

- Pergi ke menu Tentang (ikon Nomad di bahagian atas kiri), dan tekan `Pulihkan pembelian`
- Semak semula bahawa anda telah log masuk ke akaun yang sama yang anda gunakan untuk membeli Nomad (di Google Play).
- Mulakan semula peranti
- Kadangkala anda perlu menunggu beberapa jam
- Pastikan aplikasi Google Play dikemas kini
- Pasang semula Nomad (pastikan anda [membuat sandaran fail anda](#locate) jika anda tidak mahu kehilangan apa-apa)
- Anda boleh cuba membeli sekali lagi untuk melihat apa yang berlaku (nota: anda tidak boleh membeli item yang sama dua kali pada akaun yang sama)

:::tip
Anda boleh menghubungi saya di <support@nomadsculpt.com>, tetapi *satu-satunya* perkara yang dapat saya lakukan ialah mengesahkan sama ada sesuatu e-mel mempunyai pembelian yang dikaitkan dengannya.

Ambil perhatian bahawa saya kerap menerima laporan tentang lesen yang tidak dikemas kini dengan betul selepas mendapatkan peranti baharu.
Saya tidak mempunyai sebarang kawalan ke atas pembayaran dan penyegerakan akaun; semuanya dikendalikan oleh Google/AppGallery!

Akhirnya pembelian sentiasa dipulihkan, tetapi langkah-langkah yang diperlukan untuk mempercepatkan proses ini tidak jelas.
:::

::: warning
Peranti Huawei terkini tidak mempunyai akses kepada perkhidmatan Google.
Dalam kes itu, anda perlu membeli aplikasi ini sekali lagi di AppGallery (gedung aplikasi Huawei).
:::

### Bolehkah anda menterjemah atau membetulkan [bahasa-saya]? {#locale}
Saya boleh menambah bahasa lain dengan agak mudah, tetapi saya bergantung pada terjemahan AI kerana ia jauh lebih mudah diuruskan untuk kemas kini yang kerap.
Fail-fail terjemahan boleh didapati [di sini](https://github.com/stephomi/nomad-translation).

## Ciri-ciri {#features}

### Mengapa gizmo tidak bergerak? {#gizmo-not-moving}
Anda mungkin telah [mendayakan pin dalam bar alat menu kiri](tools#left-menu-toolbar).

### Bolehkah kita membuat animasi dalam Nomad? {#animate}
Belum buat masa ini. Ciri garis masa yang boleh menganimasikan lapisan mungkin menarik, tetapi ia belum dirancang buat masa ini.

Saya ingin menyokong rigging/skinning pada masa hadapan, tetapi ia membawa beberapa cabaran (terutamanya interaksi dengan alat mengukir...) jadi belum ada apa-apa yang pasti buat masa ini.


### Bolehkah kita membuat pemodelan poligon rendah yang sebenar? {#lowpoly}
Belum buat masa ini.
Ini sebenarnya bukan skop Nomad *Sculpt*, tetapi mungkin saya akan menyediakan beberapa alat pada masa hadapan.


### Bolehkah kita membuat UV dan tekstur? {#texturing}
Jawapan ringkas: Ya. Jawapan panjang: Tidak secara langsung, tetapi terdapat beberapa cara untuk menggabungkan alat cat verteks Nomad yang hebat dengan UV dan tekstur.

* Nomad membolehkan anda mewarnakan warna, kekasaran dan sifat bahan terus ke dalam verteks ukiran anda.
* Nomad membenarkan bilangan verteks yang sangat tinggi supaya anda boleh mewarna tanpa perlu risau tentang UV.
* Nomad boleh memuatkan tekstur untuk digunakan dalam berus, membolehkan anda mengecap dan mewarna dengan tekstur.
* Nomad boleh memuatkan objek yang sudah mempunyai tekstur, untuk tujuan render.
* Nomad boleh [membuka balutan UV](topology.md#uv-unwrap-uvatlas) objek berpoligon rendah.
* Warna/kekasaran/kelogaman boleh dipindahkan daripada tekstur ke verteks melalui [pilihan unjuran](topology.md#reproject-to-vertex).
* Warna/kekasaran/kelogaman/normal boleh di-bake daripada verteks ke tekstur melalui [pilihan bake](topology.md#bake-texture)
* Bake dan unjuran boleh dilakukan antara objek tunggal atau banyak objek, atau antara tahap subbahagian tertinggi dan terendah bagi satu objek, membolehkan pelbagai aliran kerja bake dan unjuran.
* Selepas bake, mengeksport OBJ juga akan mengeksport tekstur, yang boleh dibawa ke aplikasi seperti Procreate untuk mewarna terus pada tekstur.

### Bolehkah saya merakam video meja putar? {#video}
Belum dirancang buat masa ini. iOS mempunyai [ciri rakaman video](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) yang sangat mudah digunakan.

Pada iOS, ini dilakukan dengan meleret ke bawah dari bahagian atas kiri, dan mengetik butang rakam. Ia akan memberikan kira detik 3 saat; leret menu itu ke tepi untuk memaparkan Nomad, dan gunakan ciri meja putar. Apabila selesai, leret ke bawah sekali lagi dari bahagian atas kanan, dan ketik butang rakam sekali lagi. Sunting video dalam pustaka foto untuk membuang rakaman berlebihan di awal dan di akhir video.

### Bolehkah anda menambah [ciri-kegemaran-anda] sebagai butang di aras atas? {#interface}
Ya, bar alat bawah kini boleh disesuaikan daripada menu [Antara Muka](interface.md#shortcuts), dan bar alat terapung kini boleh dicipta.

### Apakah ciri-ciri seterusnya? {#next-features}
Untuk pelan hala tuju jangka sederhana/panjang, saya mempunyai banyak idea tetapi belum pasti lagi.

Pembaikan pepijat dan penambahbaikan ciri sedia ada akan sentiasa diberi keutamaan berbanding penambahan ciri baharu.


### Bolehkah kita membuat rig dalam Nomad? {#rigging}
Tidak, tetapi ia dirancang. Buat masa ini, anda boleh menjadikan bentuk-bentuk berinduk antara satu sama lain dan mengubah titik pangsi, membolehkan ukiran ringkas yang boleh digayakan.

### Bolehkah kita menggunakan lebih daripada 4 lampu? {#lights}
Anda boleh menggunakan sehingga 4 lampu pada peranti mudah alih, dan sehingga 6 pada desktop. Ini ialah had enjin render masa nyata dalam Nomad. Anda boleh memalsukannya menggunakan objek yang memancar dan pencahayaan global dalam pemprosesan pasca, seperti yang ditunjukkan dalam [tutorial ini](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Bolehkah kita mengimport alat Zbrush? {#zbrush-import}
Tidak, Zbrush menggunakan format proprietari. Anda sepatutnya boleh mengekstrak peta alfa dan menggunakannya dalam Nomad.

### Mengapa warna tidak sepadan dengan apa yang saya warnakan? Mengapa saya tidak boleh mendapat warna putih dalam render? {#paint-pbr}
Bayangkan mengambil foto sehelai kertas, berbanding foto lampu meja, berbanding foto matahari. Kamera dan skrin yang lebih lama akan menjadikan semuanya 'putih'. Sistem yang lebih moden boleh menunjukkan perbezaan antara putih kertas yang dipantulkan, cahaya yang dipancarkan oleh lampu, dan cahaya matahari yang sangat terang.

Grafik komputer moden cuba berfungsi dengan cara yang serupa, meniru fizik cahaya dan permukaan. Ini dipanggil `Physically Based Rendering`, atau PBR, dan pemapar PBR Nomad berasaskan konsep ini. Hasilnya kelihatan realistik dan seimbang, tetapi warna yang diwarnakan dengan terang selalunya akan kelihatan lebih gelap.

Jika anda perlukan render yang lebih hampir dengan warna yang diwarnakan, anda boleh membetulkannya dengan cara bukan berasaskan fizik dan cara berasaskan fizik:

Bukan PBR:
* `Gunakan mod 'Tanpa cahaya' dalam menu Shading`. Warna akan dipaparkan tepat seperti yang diwarnakan, tetapi anda juga kehilangan semua shading. Berguna untuk semakan pantas, dan untuk hasil yang lebih grafik.
* `Gunakan mod 'MatCap' dalam menu Shading`. Pilih matcap yang lebih terang, kebanyakannya putih, tanpa sebarang warna.

PBR:
* `Gunakan persekitaran yang neutral`. Anda boleh [menukar persekitaran](shading.md#environment) kepada yang lebih neutral. Elakkan persekitaran dalaman kerana ia cenderung lebih berwarna. Sebaliknya, pilih persekitaran luar pada waktu siang atau persekitaran studio.
* `Tingkatkan pencahayaan`. Jika anda mengambil foto kertas putih dalam bilik gelap, anda hanya perlu menambah cahaya. Pada lampu persekitaran, naikkan gelangsar dedahan sehingga warna mula terasa betul bagi anda, atau tambah lebih banyak lampu individu dengan intensiti yang lebih tinggi.
* `Tingkatkan dedahan kamera`. Jika bilik gelap itu tidak mempunyai lampu tambahan, anda boleh membiarkan pengatup kamera terbuka lebih lama, atau menggunakan ISO yang lebih sensitif. Dalam Nomad, anda boleh mencapai hasil yang serupa dengan pemprosesan pasca. Pergi ke pemprosesan pasca, dayakannya, turun ke pemetaan nada, dayakannya, dan naikkan gelangsar pendedahan sehingga warna terasa betul.
* `Gunakan warna pancaran`. Dalam menu bahan, anda boleh mendayakan 'pancaran' di bawah tekstur, yang akan menjadikan objek kelihatan seperti sumber cahaya. Jika anda menghidupkan pencahayaan global dalam tetapan pemprosesan pasca, ia akan memancarkan cahaya ke objek lain dalam adegan. Anda juga boleh mendayakan 'Sentiasa tanpa pencahayaan' untuk bahan itu, yang akan memberikan rupa yang serupa tanpa tekstur.

## Ranap {#crashes}

### Ia ranap apabila saya menyimpan atau melakukan remesh pada model saya! {#crash-remesh}
Peranti anda kehabisan memori (RAM).  
Untuk mengurangkan penggunaan memori dalam adegan anda, anda boleh menggunakan beberapa pilihan [Topologi](topology.md) untuk mengurangkan bilangan poligon.

::: tip RAM/Storan
Yang penting ialah jumlah RAM, bukan storan (yang biasanya jauh lebih besar).
:::


### Ia ranap apabila saya memuatkan projek saya! {#crash-load}
Jika fail itu kecil, anda boleh menghantarnya kepada saya dan saya akan melihatnya (melalui e-mel <support@nomadsculpt.com>).

Jika tidak, peranti anda mungkin kehabisan memori RAM.

- Pastikan anda menutup semua aplikasi lain yang terbuka pada peranti anda.
- Mulakan projek baharu dalam Nomad dan bukannya membiarkan projek sedang dibuka.
- Jika ia masih ranap, satu-satunya penyelesaian ialah memuatkan [fail projek anda](#locate) pada peranti yang mempunyai lebih banyak memori.

::: tip
Jika peranti mudah alih anda tidak dapat memuatkan projek, cuba [versi desktop](https://nomadsculpt.com). Anda boleh menggunakannya secara percuma dalam mod Demo untuk mengimport dan mengeksport projek, walaupun hanya beberapa alat suntingan yang tersedia.

Jika projek anda menggunakan [Lapisan](layers.md), anda mungkin mahu menggabungkannya untuk mengurangkan penggunaan memori.
:::

### Ia ranap apabila saya memulakan Nomad! {#crash-start}
Jika ia ranap semasa memuatkan, ini bermakna Nomad menghadapi masalah dengan fail tertentu yang terdapat dalam folder Nomad.

Kebanyakan masa, ia berlaku kerana projek itu berat dan malangnya ia melebihi had RAM.

Cari [folder Nomad](#locate), kemudian namakan semula atau alihkan beberapa fail untuk mencari puncanya.

Pertama, cuba namakan semula `settings.json`. Dengan cara itu, ia akan berhenti memuatkan projek terakhir.

Jika itu tidak berkesan, cuba alihkan beberapa fail terkini keluar dari folder sumber masing-masing (`projects`, `matcaps`, `environments`, dll.).

Anda juga boleh menamakan semula folder-folder itu sendiri supaya Nomad mengabaikannya sepenuhnya.
Jika anda menamakan semula atau mengalihkan semua fail dalam folder Nomad, hasilnya akan sama seperti pemasangan bersih.

::: tip
Apabila Nomad memuatkan fail semasa permulaan, ia sentiasa mengalihkan fail itu ke folder `can_be_deleted/`.
Jika operasi itu berjaya, fail itu dialihkan semula ke folder asalnya.

Jika ia ranap sebelum pemuatan selesai, Nomad akan dilancarkan dengan jayanya pada permulaan seterusnya, kerana ia mengabaikan folder `can_be_deleted/`.

Anda boleh cuba memuatkan fail ini sekali lagi jika anda rasa ia boleh berjaya.
:::

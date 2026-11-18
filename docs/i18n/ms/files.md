# ![](/icons/open.webp) Fail {#files}

Menu fail membolehkan anda menyimpan dan memuatkan projek Nomad, mengimport dan mengeksport model 3d, mengeksport imej render, dan menyambungkan Nomad dengan aplikasi lain. Ia mempunyai tiga tab: `Fail`, `Render` dan `Pautan`.

![](/images/file_menu.webp)

## Projek {#project}
![](/images/file_project.webp)

Lakaran kecil di bahagian atas menunjukkan projek semasa, dengan saiz failnya, auto simpan dan sejarah yang disimpan di sebelahnya. Ketik lakaran kecil itu untuk membuka pelayar mini projek anda, kemudian ketik sesuatu projek untuk mendapatkan menu bagi membuka, menambah, menimpa, mengklon, menamakan semula atau memadamnya.

Apabila projek mempunyai perubahan yang belum disimpan, `Perubahan belum disimpan!` dipaparkan di bawah lakaran kecil.

### Skop {#scope}
Pada desktop, pilih tempat projek anda disimpan:
* `Dalaman` - Tetapan lalai, sama seperti pada peranti mudah alih. Projek hanya disimpan di dalam folder utama Nomad.
* `Di Tempat` - Apabila anda membuka projek dari luar folder Nomad, menyimpan akan menimpa fail asal. Auto Simpan tidak berfungsi untuk projek luaran ini.

### ![](/icons/nomad.webp) Pra-tetap {#preset}
Akses koleksi demo dan komponen watak. Pilih satu, kemudian pilih sekali lagi untuk memilih sama ada mahu `Buka` atau `Tambah ke adegan`. Anda juga boleh memuat turun model percuma daripada Poly Haven melalui pelayar ini.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Sejarah... {#history}
Akses pantas kepada pilihan sejarah projek, seperti `Simpan sejarah`, yang mengekalkan sejarah buat asal anda apabila projek disimpan. Lencana hijau pada butang menunjukkan bahawa sejarah disimpan bersama projek. Lihat [Sejarah](history.md#save-history) untuk butirannya.

### ![](/icons/save.webp) Simpan {#save}
Menyimpan projek Nomad. Jika projek belum pernah disimpan, anda akan diminta memberikan nama.

### ![](/icons/save_as.webp) Simpan Sebagai... {#save-as}
Menyimpan projek dengan nama baharu, sebagai projek baharu.

### ![](/icons/save_as.webp) Timpa... {#overwrite}
Memaparkan pelayar projek untuk menyimpan adegan semasa di atas projek lain. Dayakan `Hanya sertakan objek terpilih` untuk menyimpan objek yang dipilih sahaja dan bukannya keseluruhan adegan. Pelayar ini juga mempunyai butang `Simpan Sebagai...` untuk menyimpan sebagai projek baharu.

### ![](/icons/pencil.webp) Namakan semula {#rename}
Memaparkan kotak teks untuk menamakan semula projek semasa.

### ![](/icons/open.webp) Buka... {#open}
Memaparkan pelayar projek untuk membuka projek.

### ![](/icons/add_file.webp) Tambah ke adegan... {#add}
Memaparkan pelayar projek. Apabila sesuatu projek dipilih, kandungannya akan digabungkan dengan adegan semasa.

### ![](/icons/trash.webp) Padam... {#delete}
Memaparkan pelayar projek. Mana-mana projek yang dipilih akan dipadam daripada sistem fail.

### ![](/icons/new_file.webp) Baru {#new}
Memulakan projek baharu. Jika terdapat perubahan yang belum disimpan, anda akan diminta untuk mengesahkannya. Pengesahan ini membolehkan anda memilih `Kekalkan` atau `Tetapkan semula` bagi tetapan `Latar belakang`, `Persekitaran`, `MatCap` dan `X-Ray`, serta memilih sama ada projek baharu menggunakan `Simpan sejarah`.

### ![](/icons/autosave.webp) Auto Simpan... {#auto-save}
Menu untuk mengawal pilihan auto simpan. Dayakan `Auto Simpan` untuk menyimpan projek anda dalam fail berasingan pada selang masa yang tetap. Lencana pada butang menunjukkan sama ada ia dihidupkan.

Sebab Nomad tidak menyimpan di latar belakang ialah kerana fail 3d boleh menjadi agak besar, jadi ia boleh menyebabkan kelambatan yang ketara semasa anda mengukir.

Tambahan pula, untuk mengelakkan masalah kehabisan memori, adegan biasanya dimampatkan sebelum operasi simpan.
Pemampatan/penyahmampatan ini juga akan memperlahankan operasi simpan.

### Selang simpan {#timer-pop-up}
Berapa minit Nomad menunggu di antara setiap auto simpan.

### Tunjuk kira detik {#popup-timeout}
Menunjukkan kira detik sebelum setiap auto simpan, supaya anda boleh membatalkannya jika anda sedang sibuk melakukan sesuatu. Apabila dinyahdayakan, Nomad menyimpan sebaik sahaja anda berhenti mengukir.

### ![](/icons/trash.webp) Abaikan Auto Simpan {#discard-autosave}
Jika fail auto simpan wujud untuk sesuatu projek, ia akan dimuatkan secara automatik dan bukannya projek asal. Jika ini tidak diperlukan, butang ini akan memadam fail auto simpan. Memuatkan fail itu kemudiannya akan memuatkan simpanan manual terakhir projek.

### ![](/icons/open.webp) Buka simpanan yang lapuk {#open-outdated-save}
Apabila sesuatu projek mempunyai auto simpan dan simpanan manual, butang ini membuka yang lebih lama antara kedua-duanya (`Buka auto simpanan yang lapuk` atau `Buka simpanan manual yang lapuk`), bersama tarikhnya. Berguna jika simpanan terkini bukan yang anda mahukan.

### ![](/icons/storage.webp) Dipadam baru-baru ini... {#recently-deleted}
Nomad menyimpan data projek yang telah keluar dari folder projek, dan fail yang digantikan oleh import, selama beberapa hari sebelum memadamnya secara kekal. Fail yang gagal diimport kekal sehingga anda memadamnya. Senarai ini menunjukkan fail-fail tersebut bersama saiz dan tarikhnya, supaya anda boleh memadamnya satu demi satu atau dengan `Padam semua`.

## Import {#import}

### ![](/icons/add_file.webp) Import {#import-button}
Untuk mengimport fail 3d yang bukan projek Nomad.

Apabila anda mengimport fail adegan luaran ke dalam Nomad, anda boleh sama ada *menambahnya* atau memulakan projek *baharu* dengannya.

Menambah fail hanya akan menambah objek-objeknya ke dalam adegan semasa.
Memilih `Baru` akan mencipta projek Nomad baharu yang mengandungi objek-objek baharu itu.

Tetingkap import menyenaraikan setiap fail yang anda pilih, masing-masing dengan pilihan importnya sendiri. Imej juga boleh diimport dengan cara ini: pilih untuk setiap imej sama ada ia menjadi `HDRI`, `MatCap`, `Imej rujukan`, `Alpha`, `Tekstur` atau `VDM`.

Nomad boleh mengimport format berikut:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), pada platform yang menyokongnya

### ![](/icons/cog.webp) Tetapan {#advanced}
Butang `Tetapan...` di sebelah lakaran kecil projek menunjukkan pilihan import utama. Tetapan ini tidak disimpan, dan tetingkap import menunjukkan pilihan yang terpakai pada fail yang sedang anda import.

### Semua format {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Kekalkan topologi {#keep-topology}
Secara lalai, Nomad akan cuba membaiki geometri yang bermasalah semasa memuatkan. Mendayakan pilihan ini akan menghalang Nomad daripada menyusun semula verteks/muka, menggabungkan pendua dan membuang verteks yang tidak digunakan.

::: warning
Dengan `Kekalkan topologi`, operasi seperti Boolean, Join, Decimate atau Manifold mungkin tidak menggabungkan verteks pendua.
:::

#### ![](/icons/image.webp) Langkau tekstur {#skip-textures}
Tidak memuatkan tekstur yang dibenamkan dalam fail, bagi format yang menyokongnya seperti glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Muat tetapan UI {#keep-gui-settings}
Semasa membuka atau mengimport fail projek, muatkan semua tetapan antara muka yang disimpan di dalamnya.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Pisahkan OBJ mengikut kumpulan {#split-obj-by-groups}
Memisahkan kumpulan OBJ kepada objek-objek yang berasingan.

#### ![](/icons/vertex.webp) Gabungkan kedudukan pendua {#merge-duplicate-positions}
Menggabungkan verteks yang berkongsi kedudukan yang sama.

#### ![](/icons/uv.webp) Gabungkan UV pendua {#merge-duplicate-uvs}
Menggabungkan koordinat tekstur yang berkongsi UV yang sama.

#### ![](/icons/paint.webp) Ruang Warna {#color-space}
Menetapkan mod warna yang ditafsirkan daripada fail sebagai `Auto`, `Linear` atau `sRGB`. Cuba tukar pilihan ini jika warna kelihatan tidak betul.

#### ![](/icons/image.webp) Format {#normal-format}
Format peta normal bagi tekstur: `Auto`, `OpenGL (+Y)` atau `DirectX (-Y)`. Cuba format yang satu lagi jika butiran peta normal kelihatan terbalik.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Ruang Warna {#color-space-ply}
Menetapkan mod warna yang ditafsirkan daripada fail sebagai `Auto`, `Linear` atau `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Gabungkan UV pendua {#merge-duplicate-uvs-fbx}
Menggabungkan koordinat tekstur yang berkongsi UV yang sama.

#### ![](/icons/paint.webp) Ruang Warna {#color-space-fbx}
Menetapkan mod warna yang ditafsirkan daripada fail sebagai `Auto`, `Linear` atau `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Format peta normal bagi tekstur: `Auto`, `OpenGL (+Y)` atau `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Ruang Warna {#color-space-usd}
Menetapkan mod warna yang ditafsirkan daripada fail sebagai `Auto`, `Linear` atau `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Format peta normal bagi tekstur: `Auto`, `OpenGL (+Y)` atau `DirectX (-Y)`.



## Eksport {#export}
Menyimpan ke format geometri 3d yang boleh digunakan dalam perisian lain.

![](/images/file_export.webp)

Format fail yang berbeza menyokong ciri yang berbeza, jadi pilihan yang tersedia akan berubah mengikut jenis fail yang dipilih.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Warna verteks](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR verteks](#pbr-paint)       | ✅     | Nomad ✅<br>Lain ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Lain ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Lapisan](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objek                           | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Kumpulan muka                   | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarki                        | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lampu                           | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Tekstur                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitif, Pemprosesan Pasca, dll. | ✅   | Nomad ✅<br>Lain ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Butang eksport {#export-button}
Klik butang ini untuk mengeksport geometri menggunakan tetapan yang dipilih. Butang ini menunjukkan format yang dipilih dan anggaran saiz fail. Pada Android, butang `Kongsi` di sebelahnya menghantar fail terus ke aplikasi lain.

### Format fail {#file-format}
Pilih format untuk dieksport: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` atau `USD`. NOMAD ialah format Nomad sendiri dan tidak boleh dimuatkan dalam perisian lain, jadi ia kebanyakannya untuk diimport semula ke dalam Nomad.

### Termasuk {#allvisibleselected}
Pilih objek yang akan dieksport: `Semua`, `Terlihat` atau `Terpilih`. Nombor di sebelah setiap pilihan menunjukkan berapa banyak objek yang akan dieksport.

### Satu fail setiap objek {#one-file-per-object}
Mengeksport setiap objek ke dalam failnya sendiri. Nombor itu menunjukkan berapa banyak fail yang akan ditulis.

### Jenis {#type}
Apabila eksport menghasilkan beberapa fail (satu fail setiap objek, atau OBJ bersama tekstur), simpan fail-fail itu dalam `Folder` atau `Zip`. Sesetengah aplikasi (Google Drive, One Drive, dll.) tidak menyokong import folder, jadi anda boleh menggunakan Zip sebagai gantinya.

### Benamkan sejarah {#embed-history}
NOMAD sahaja. Menyertakan sejarah buat asal di dalam fail, dan ia akan dipulihkan apabila fail dibuka dalam Nomad. Ia menambah saiz fail, dan memerlukan keseluruhan adegan dieksport sebagai satu fail.

### Benamkan aset {#embed-assets}
NOMAD sahaja. Menyertakan matcap, persekitaran dan fon tersuai anda di dalam fail. Aset terbina dalam tidak dibenamkan.

### Warna verteks {#vertex-colors}
Mengeksport warna verteks jika format fail menyokongnya. Sesetengah perisian 3d boleh membacanya, tetapi bukan semua.

Untuk OBJ, anda boleh memilih:
* `Tiada` - Tiada warna.
* `RGB` - Warna dilampirkan selepas verteks.
* `MRGB (ZBrush)` - Cara alternatif untuk mengekod warna, yang juga menyokong data topeng.

### Ruang Warna {#color-space-export}
OBJ sahaja, dengan warna verteks `RGB`. Menulis warna sebagai `Linear` atau `sRGB`.

### Cat PBR {#pbr-paint}
Mengeksport pewarnaan kekasaran, kelogaman dan topeng. Perisian lain mungkin mengabaikan data ini.
Warna verteks PBR dieksport sebagai atribut warna verteks sekunder.
Saluran-salurannya dipadatkan seperti berikut:

|           | Saluran  |
| :-------: | :------: |
| Kekasaran | R        |
| Kelogaman | G        |
| Topeng    | B        |


### Lapisan {#layers}
Lapisan disokong melalui morph target glTF. Ini disokong secara rasmi oleh glTF, jadi ia sepatutnya berfungsi dalam perisian lain juga.
Nomad juga mengeksport warna, kekasaran dan kelogaman bagi setiap lapisan, tetapi data ini akan diabaikan oleh perisian lain.

### Mewarnai lapisan {#layer-painting}
Mengeksport pewarnaan lapisan, yang biasanya diabaikan oleh perisian lain.

### Kumpulan Muka {#face-group}
Mengeksport kumpulan muka. Eksport ini kadangkala boleh mengganggu perisian lain.

### Tulis Objek {#write-objects}
OBJ sahaja. Memastikan objek-objek kekal berasingan. Nyahdayakannya untuk mengeksport semuanya sebagai satu objek, contohnya untuk menggunakan ciri 'Mesh ID / Polygroup' dalam Substance Painter.

### Normal {#normals}
Mengeksport maklumat normal. Ambil perhatian bahawa Nomad akan sentiasa mengira normalnya sendiri apabila mengimport format fail lain.

### Tangen {#tangents}
Mengeksport maklumat tangen, yang digunakan jika model mempunyai peta normal.

### Tekstur {#textures}
Jika tekstur telah ditambah pada bahan, ia akan dieksport. Ambil perhatian bahawa ini tidak akan melakukan bake tekstur; itu dilakukan melalui pilihan bake dalam topologi.

### Format {#fbx-format}
FBX sahaja. `Binari` lebih kecil tetapi mungkin tidak berfungsi dalam setiap aplikasi, manakala `Ascii` ialah fail teks.

### Dimampatkan {#compressed}
FBX sahaja. Mengurangkan saiz fail, tetapi eksport dan import menjadi lebih perlahan.

### Pra-tetap {#usd-preset}
USD sahaja. Pilih aplikasi yang menjadi sasaran eksport anda: `OpenUSD`, `Apple`, `Procreate` atau `Zbrush`. Sesetengah pilihan hanya tersedia untuk pra-tetap tertentu.

### Instans {#instance}
USD sahaja. Mengeksport objek instans sebagai instans, dan bukannya menduplikasi geometrinya.

### Benarkan senget {#allow-skew}
USD sahaja. Membenarkan kesengetan dalam transformasi matriks. Apabila dinyahdayakan, Nomad memecahkan transformasi yang senget kepada transformasi penskalaan dan putaran yang berasingan.

### Pengulang {#repeater}
USD sahaja. Mengeksport salinan yang dibuat oleh pengulang sebagai instans.

### Gabung salinan {#join-copies}
Setiap objek dan salinan pengulangnya menjadi satu objek.

::: tip Petua: Import kekasaran dan kelogaman ke Blender

Blender boleh mengimport glTF/glb, tetapi tidak memahami atribut verteks untuk kelogaman dan kekasaran secara automatik. Untuk menggunakannya, dalam penyunting bahan, cipta nod Vertex Color dan tetapkan sifatnya kepada atribut warna seterusnya (biasanya Col.001). Sambungkan nod 'Separate XYZ', hantar X ke roughness, dan Y ke Metallic.

Video ini menunjukkan prosesnya:

![](/videos/blender_pbr.mp4)

::: 

::: tip Petua: Sokongan ciri USD

USD ialah format yang kompleks. Spesifikasinya menyokong banyak ciri, tetapi bukan semua perisian 3d menyokongnya. Contohnya, OSX/iOS tidak menyokong warna verteks. Mod pra-tetap dalam pengeksport USD cuba membuat tekaan terbaik untuk keserasian dengan OpenUSD, Apple, Procreate dan Zbrush.

::: 

## ![](/icons/screen.webp) Render {#render}

Mengeksport imej yang menggabungkan semua tetapan dalam projek (lampu, bahan, pemprosesan pasca dan sebagainya).

![](/images/file_render.webp)
### ![](/icons/preview.webp) Pratonton {#preview}

Butang `Pratonton` di sebelah tajuk menu menjadikan antara muka lut sinar, untuk membantu anda melihat bingkai hasil akhir.

### ![](/icons/home.webp) Fokus {#focus}
Membingkaikan adegan atau pemilihan supaya ia muat dengan saiz render. Ketik sekali lagi untuk bertukar antara kedua-duanya.

### ![](/icons/map.webp) Peta ketinggian {#heightmap}
Merender adegan sebagai peta ketinggian skala kelabu seperti yang dilihat dari kamera, dengan bahagian yang paling dekat menjadi paling terang. Mendayakannya akan menukar saiz kepada `Segi empat sama` dan membingkaikan pemilihan. Bar kecil dalam port pandangan membolehkan anda melaraskan `Fokus` kecerunan.

Apabila `Peta ketinggian` dihidupkan, butang `Simpan sebagai alfa` muncul di sebelah butang eksport, untuk menyimpan render sebagai alfa berus baharu dan bukannya mengeksport fail.

### ![](/icons/opacity.webp) Latar belakang lut sinar {#transparent-background}
Mendayakan saluran alfa untuk render, berguna untuk menggabungkan render dengan imej lain dalam program 2d. Ambil perhatian bahawa kelutsinaran separa tidak disokong.

### ![](/icons/sliders.webp) Papar antaramuka {#show-interface}
Menyertakan UI Nomad dalam render.

### Saiz akhir {#final-size}
Resolusi yang digunakan untuk render: `Skrin`, `720`, `1080`, `4096`, `Segi empat sama` atau `Tersuai`.

Apabila menu Fail aktif, tindihan bergaris putus-putus akan dilukis dalam port pandangan untuk menunjukkan kawasan render jika ia tidak sepadan dengan resolusi skrin.

### Lebar / Tinggi {#render-ratio}
Dengan `Tersuai`, tetapkan lebar dan tinggi imej. Butang pautan di antara dua gelangsar itu mengekalkan nisbah apabila anda menukar salah satu daripadanya. Dengan `Segi empat sama`, hanya lebar yang boleh ditetapkan.

### ![](/icons/export.webp) Eksport → PNG {#export-png}
Klik butang ini untuk memulakan proses render. Apabila selesai, anda boleh memilih cara untuk menyimpan atau berkongsi imej itu. Saiz yang sangat besar akan meminta pengesahan terlebih dahulu: simpan projek anda sebelum itu, sekiranya peranti anda kehabisan memori.

## ![](/icons/network.webp) Pautan {#link}

Sambungkan Nomad dengan peranti atau aplikasi lain, untuk menghantar dan menerima objek, atau untuk menyegerakkan suntingan anda secara langsung. Satu peranti menjadi hos sesi, dan yang lain menyertainya.

### Dayakan GoZ {#enable-goz}
Desktop sahaja. Bertukar-tukar mesh dengan ZBrush pada komputer ini. `Hantar` mengimportnya ke dalam ZBrush, `Dapatkan` mengimport daripada ZBrush yang sedang berjalan: `Pemilihan` mengambil subtool yang aktif, `Adegan` mengambil semua subtool. Anda juga boleh menekan GoZ dalam ZBrush pada bila-bila masa.

### Mod {#link-mode}
* `Mati` - Tiada pautan.
* `Hos` - Peranti ini menjadi hos sesi dan menunggu peranti lain menyertai.
* `Sertai` - Mencari peranti berdekatan, kemudian ketik nama hos untuk menyertainya.

Untuk memautkan dua Nomad, pilih `Hos` pada satu peranti dan `Sertai` pada peranti yang lain. Untuk memautkan dengan Blender, Nomad perlu menjadi hos: butang bantuan di sebelah tajuk `Pautan` menunjukkan cara memasang sambungan Nomad Blender Link.

### ![](/icons/network.webp) Port rangkaian {#network-port}
Port rangkaian yang digunakan oleh pautan. Tukarnya hanya jika aplikasi lain sudah menggunakannya.

### Hantar / Dapatkan {#send-get}
Setelah disambungkan, `Hantar` `Pemilihan` anda atau keseluruhan `Adegan` ke peranti yang satu lagi, atau `Dapatkan` daripadanya. `Gantikan` memadam adegan semasa, kemudian mendapatkan adegan peranti yang satu lagi.

### ![](/icons/link.webp) Penyegerakan langsung {#live-sync}
Menstrim suntingan anda ke peranti yang satu lagi semasa anda bekerja. `Pandangan kerja` turut menyegerakkan kamera. `Suntingan adegan` menetapkan peranti mana yang menghantar suntingan: `Auto` memberikan arah kepada aktiviti terkini. Kemudian pilih apa yang disegerakkan: `Objek dan geometri`, `Bahan`, `Cahaya`, `Kamera`, dan apabila pihak yang satu lagi menyokongnya, `Shading` dan `Pasca Pemprosesan`.

::: tip
Objek sedia ada perlu `Hantar` atau `Dapatkan` sekali terlebih dahulu, untuk memautkannya sebelum penyegerakan langsung boleh mengemas kininya.
:::

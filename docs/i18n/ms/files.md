# ![](/icons/open.webp) Fail {#files}

Menu fail membolehkan anda menyimpan dan memuat projek Nomad, mengimport dan mengeksport model 3D, serta mengeksport imej terhasil.

![](/images/file_menu.webp)

## Projek {#project}
![](/images/file_project.webp)

Imej kecil (thumbnail) bagi simpanan terakhir dipaparkan di bahagian atas menu ini. Mengetik imej kecil ini akan memaparkan pelayar mini, ketik dua kali pada projek lain untuk memaparkan menu mini bagi membuka, menambah, menyimpan, mengklon, menamakan semula, atau memadam projek tersebut.

### ![](/icons/nomad.webp) Pratetet {#preset}
Akses koleksi demo dan komponen watak. Pilih satu, kemudian pilih sekali lagi untuk memilih sama ada Buka, Tambah ke Adegan atau Klon entri tersebut ke dalam folder projek anda.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Simpan {#save}
Simpan projek Nomad.

### ![](/icons/save_as.webp) Simpan Sebagai... {#save-as}
Paparkan pelayar projek untuk membolehkan anda menyimpan projek Nomad dengan nama baharu.

### ![](/icons/pencil.webp) Namakan Semula {#rename}
Paparkan kotak teks untuk menamakan semula projek semasa.

### ![](/icons/open.webp) Buka... {#open}
Paparkan pelayar projek untuk membuka projek.

### ![](/icons/add_file.webp) Tambah ke adegan... {#add}
Paparkan pelayar projek, apabila sesuatu projek dipilih kandungannya akan digabungkan dengan adegan semasa.

### ![](/icons/trash.webp) Padam... {#delete}
Paparkan pelayar projek, sebarang projek yang dipilih akan dipadam daripada sistem fail.

### ![](/icons/new_file.webp) Baharu {#new}
Mulakan projek baharu, jika terdapat perubahan yang belum disimpan anda akan ditanya sama ada mahu menyimpannya.

### ![](/icons/autosave.webp) Simpan Automatik... {#auto-save}
Menu untuk mengawal pilihan simpan auto.

Jika anda mengaktifkan simpan auto, anda boleh menetapkan pemasa supaya satu tetingkap timbul akan muncul pada sela masa tetap.
Sebab Nomad tidak menyimpan di latar belakang ialah kerana fail 3D boleh menjadi agak besar dan ini boleh menyebabkan lengah ketara semasa anda mengukir.

Selain itu, untuk mengelakkan masalah kehabisan memori, adegan biasanya dimampatkan sebelum operasi menyimpan.
Pemampatan/nyahmampat ini juga akan memperlahankan operasi simpan.

### Pop timbul pemasa {#timer-pop-up}
Seberapa kerap tetingkap timbul pemasa akan muncul.

### Had masa popup {#popup-timeout}
Aktifkan had masa tetingkap timbul.

### Buang autosimpan {#discard-autosave}
Jika fail simpan auto wujud untuk sesuatu projek, ia akan dimuatkan secara automatik dan bukannya projek asal. Jika ini tidak diperlukan, butang ini akan memadam simpan auto tersebut. Memuatkan fail selepas itu akan memuatkan simpanan manual terakhir projek tersebut.


## Import {#import}

### ![](/icons/add_file.webp) Import {#import-button}
Untuk mengimport fail 3D yang bukan projek Nomad.

Apabila anda mengimport fail adegan luaran ke Nomad, anda boleh sama ada *import* atau *tambah* fail tersebut.

Menambah fail akan hanya menambah objek ke dalam adegan semasa.
Mengimport fail akan mencipta projek Nomad baharu dengan objek baharu di dalamnya.

Nomad boleh mengimport format berikut:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, eksperimental)

### ![](/icons/cog.webp) Lanjutan {#advanced}
Paparkan pilihan import lanjutan:

### Projek/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Kekalkan topologi {#keep-topology}
Secara lalai Nomad akan cuba membaiki geometri bermasalah semasa memuat. Mengaktifkan pilihan ini akan menghalang Nomad daripada menyusun semula bucu/muka, membuang pendua bucu/muka, dan membuang bucu yang tidak digunakan.

#### Langkau tekstur {#skip-textures}
Langkau pemuatan tekstur untuk format yang menyokongnya seperti glTF.

### Projek / glTF {#project-gltf}
#### Kekalkan tetapan gui {#keep-gui-settings}
Aktifkan penyimpanan tetapan gui dan projek di dalam fail Nomad .nom atau glTF.

### OBJ {#obj}
#### Pisahkan OBJ mengikut kumpulan {#split-obj-by-groups}
Aktifkan pemisahan kumpulan OBJ kepada objek berasingan.

#### Ruang Warna {#color-space}
Tetapkan mod warna yang ditafsir daripada obj sebagai Linear, sRGB, atau Auto.

### PLY {#ply}
#### Ruang Warna {#color-space-ply}
Tetapkan mod warna yang ditafsir daripada ply sebagai Linear, sRGB, atau Auto.


### FBX {#fbx}
#### Ruang Warna {#color-space-fbx}
Tetapkan mod warna yang ditafsir daripada obj sebagai Linear, sRGB, atau Auto.



## Eksport {#export}
Simpan ke format geometri 3D yang boleh digunakan dalam perisian lain. 

![](/images/file_export.webp)

Format fail yang berbeza menyokong ciri yang berbeza, pilihan yang tersedia akan berubah berdasarkan jenis fail yang dipilih.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Lain ⚠️  | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Lain ⚠️  | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objek                           | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Kumpulan Muka                   | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarki                        | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lampu                           | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Tekstur                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Eksport ❌ |
| Primitif, Pascaproses, dsb.     | ✅     | Nomad ✅<br>Lain ❌  | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Semua/Kelihatan/Dipilih {#allvisibleselected}
Keadaan butang aktif akan menetapkan objek mana yang akan dieksport. Nombor di sebelah ikon menunjukkan berapa banyak objek yang akan dieksport untuk pilihan tersebut.

### Warna verteks {#vertex-colors}
Eksport warna bucu jika disokong oleh format fail.

### PBR Paint {#pbr-paint}
Warna bucu PBR dieksport sebagai atribut warna bucu sekunder.
Saluran dipaketkan seperti berikut:

|           | Saluran |
| :-------: | :-----: |
| Kekasaran | R       |
| Keberlogaman | G    |
| Masking   | B       |


### Lapisan {#layers}
Lapisan disokong melalui sasaran morf glTF.
Nomad juga mengeksport warna, kekasaran dan keberlogaman setiap lapisan tetapi ini akan diabaikan oleh perisian lain.

### Lukisan lapisan {#layer-painting}
Eksport lukisan lapisan, biasanya diabaikan oleh perisian lain.

### Kumpulan Muka {#face-group}
Eksport kumpulan muka, pengeksportan kadangkala boleh mengganggu perisian lain.

### Normal {#normals}
Eksport maklumat normal. Ambil perhatian bahawa Nomad akan sentiasa mengira normalnya sendiri apabila mengimport format fail lain.

### Tangen {#tangents}
Eksport maklumat tangen, digunakan jika model mempunyai peta normal. 

### Tekstur {#textures}
Jika tekstur telah ditambah pada bahan, ia akan dieksport. Ambil perhatian bahawa ini tidak akan membakar (bake) tekstur, itu dilakukan melalui pilihan bake dalam topologi.

### Butang eksport {#export-button}
Klik ini untuk mengeksport geometri menggunakan tetapan yang dipilih.

::: tip Tip: Import kekasaran dan keberlogaman ke Blender

Blender boleh mengimport glTF/glb, tetapi tidak secara automatik memahami atribut bucu untuk keberlogaman dan kekasaran. Untuk menggunakannya, dalam penyunting bahan cipta nod Vertex Color, tetapkan propertinya kepada atribut warna seterusnya (biasanya Col.001). Sambungkan nod 'Separate XYZ', hantar X ke Roughness, dan Y ke Metallic.

Video ini menunjukkan proses tersebut:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Sokongan ciri USD

USD ialah format yang kompleks, spesifikasinya menyokong banyak ciri, tetapi tidak semua perisian 3D akan menyokongnya. OSX/iOS sebagai contoh tidak menyokong warna bucu. Mod praset dalam pengeksport USD cuba membuat anggaran terbaik untuk keserasian dengan OpenUSD, Apple, Procreate, ZBrush.

::: 

## Render {#render}

Eksport imej yang merupakan gabungan semua tetapan dalam projek (lampu, bahan, pascapemprosesan dan sebagainya). 

![](/images/file_render.webp)
### Pratonton {#preview}

Butang pratonton kecil di sebelah tajuk menu akan meredupkan bar alat untuk membantu mempratonton hasil akhir.

### Latar belakang lutsinar {#transparent-background}
Aktifkan saluran alfa untuk render, berguna untuk menggabungkan render dengan imej lain dalam program 2D. Ambil perhatian bahawa ketelusan separa tidak disokong.

### Tunjuk antara muka {#show-interface}
Aktifkan penyertaan UI Nomad dalam render.

### Nisbah render {#render-ratio}
Pengganda pada resolusi imej.

### Saiz akhir {#final-size}
Resolusi yang akan digunakan untuk render. Apabila `Custom` dipilih, peluncur lebar dan tinggi akan diaktifkan. 

Apabila menu Fail aktif, satu garisan putus-putus akan dilukis dalam paparan untuk menunjukkan kawasan render jika ia tidak sepadan dengan resolusi skrin (ambil perhatian bahawa anda mesti berada dalam mod landskap untuk ini menjadi tepat).

### Eksport png {#export-png}
Klik butang ini untuk memulakan proses render. Apabila selesai anda kemudian boleh memilih cara menyimpan atau berkongsi imej.
# ![](/icons/open.webp) Berkas

Menu berkas memungkinkan Anda menyimpan dan memuat proyek Nomad, mengimpor dan mengekspor model 3D, serta mengekspor gambar render.

![](/images/file_menu.webp)

## Proyek
![](/images/file_project.webp)

Sebuah thumbnail dari penyimpanan terakhir ditampilkan di bagian atas menu ini. Mengklik thumbnail ini akan menampilkan mini browser, ketuk dua kali pada proyek lain untuk menampilkan mini menu untuk membuka, menambah, menyimpan, mengkloning, mengganti nama, atau menghapus proyek tersebut.

### ![](/icons/nomad.webp) Preset 
Akses koleksi demo dan komponen karakter. Pilih satu, lalu pilih lagi untuk memilih Buka, Tambah ke Skena atau Klon entri tersebut ke dalam folder proyek Anda.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Save
Simpan proyek Nomad.

### ![](/icons/save_as.webp) Save As...
Tampilkan browser proyek untuk memungkinkan Anda menyimpan proyek Nomad dengan nama baru.

### ![](/icons/pencil.webp) Rename
Tampilkan kotak teks untuk mengganti nama proyek saat ini.

### ![](/icons/open.webp) Open...
Tampilkan browser proyek untuk membuka sebuah proyek.

### ![](/icons/add_file.webp) Add to scene...
Tampilkan browser proyek, ketika sebuah proyek dipilih isinya akan digabungkan dengan skena saat ini.

### ![](/icons/trash.webp) Delete...
Tampilkan browser proyek, proyek apa pun yang dipilih akan dihapus dari sistem berkas.

### ![](/icons/new_file.webp) New
Mulai proyek baru, jika ada perubahan yang belum disimpan Anda akan ditanya apakah ingin menyimpannya.

### ![](/icons/autosave.webp) Auto Save...
Menu untuk mengatur opsi penyimpanan otomatis.

Jika Anda mengaktifkan autosave, Anda dapat mengatur pengatur waktu sehingga popup akan muncul secara berkala.
Alasan Nomad tidak menyimpan di latar belakang adalah karena berkas 3D bisa sangat besar sehingga dapat menyebabkan lag yang signifikan saat Anda sedang memahat.

Selain itu, untuk menghindari masalah kehabisan memori, skena biasanya dikompresi sebelum operasi penyimpanan.
Kompresi/dekompresi ini juga akan memperlambat operasi penyimpanan.

### Timer pop up
Seberapa sering popup pengatur waktu akan muncul.

### Popup timeout
Aktifkan batas waktu popup.

### Discard autosave
Jika berkas auto save ada untuk sebuah proyek, berkas tersebut akan otomatis dimuat sebagai pengganti proyek asli. Jika ini tidak diperlukan, tombol ini akan menghapus autosave. Memuat berkas kemudian akan memuat penyimpanan manual terakhir dari proyek tersebut.


## Import

### ![](/icons/add_file.webp) Import
Untuk mengimpor berkas 3D yang bukan proyek Nomad.

Saat Anda mengimpor berkas skena eksternal ke Nomad, Anda dapat *mengimpor* atau *menambahkannya*.

Menambahkan berkas akan menambahkan objek ke dalam skena saat ini.
Mengimpor berkas akan membuat proyek Nomad baru dengan objek baru di dalamnya.

Nomad dapat mengimpor format berikut:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, eksperimental)

### ![](/icons/cog.webp) Advanced
Tampilkan opsi impor lanjutan:

### Project/ glTF / OBJ / STL / FBX
#### Keep topology
Secara bawaan Nomad akan mencoba memperbaiki geometri bermasalah saat dimuat. Mengaktifkan ini akan menghentikan Nomad dari pengurutan ulang vertex/face, penghapusan duplikat vertex/face, dan penghapusan vertex yang tidak digunakan.

#### Skip textures
Lewati pemuatan tekstur untuk format yang mendukungnya seperti glTF.

### Project / glTF
#### Keep gui settings
Aktifkan penyimpanan pengaturan GUI dan proyek di dalam berkas Nomad .nom atau glTF.

### OBJ
#### Split OBJ by groups
Aktifkan pemisahan grup OBJ menjadi objek terpisah.

#### Color Space
Atur mode warna yang diinterpretasikan dari OBJ sebagai Linear, sRGB, atau Auto.

### PLY
#### Color Space
Atur mode warna yang diinterpretasikan dari PLY sebagai Linear, sRGB, atau Auto.


### FBX
#### Color Space
Atur mode warna yang diinterpretasikan dari OBJ sebagai Linear, sRGB, atau Auto.



## Export
Simpan ke format geometri 3D yang dapat digunakan di perangkat lunak lain. 

![](/images/file_export.webp)

Format berkas yang berbeda mendukung fitur yang berbeda, opsi yang tersedia akan berubah berdasarkan jenis berkas yang dipilih.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Lainnya ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Lainnya ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, dll    | ✅     | Nomad ✅<br>Lainnya ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### All/Visible/Selected
Status tombol aktif akan menentukan objek mana yang akan diekspor. Angka di sebelah ikon menunjukkan berapa banyak objek yang akan diekspor untuk opsi tersebut.

### Vertex colors
Ekspor warna vertex jika didukung oleh format berkas.

### PBR Paint
Warna vertex PBR diekspor sebagai atribut warna vertex sekunder.
Channel dikemas dengan cara berikut:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Layers
Layer didukung melalui glTF morph targets.
Nomad juga mengekspor warna, roughness, dan metalness per-layer tetapi ini akan diabaikan oleh perangkat lunak lain.

### Layer painting
Ekspor pengecatan layer, biasanya diabaikan oleh perangkat lunak lain.

### Face Group
Ekspor facegroup, ekspor terkadang dapat mengganggu perangkat lunak lain.

### Normals
Ekspor informasi normal. Perhatikan bahwa Nomad akan selalu menghitung normalnya sendiri saat mengimpor format berkas lain.

### Tangents
Ekspor informasi tangent, digunakan jika model memiliki normal map. 

### Textures
Jika tekstur telah ditambahkan ke material, tekstur akan diekspor. Perhatikan bahwa ini tidak akan melakukan baking tekstur, hal itu dilakukan melalui opsi bake di topology.

### Export button
Klik ini untuk mengekspor geometri menggunakan pengaturan yang dipilih.

::: tip Tip: Impor roughness dan metalness ke Blender

Blender dapat mengimpor glTF/glb, tetapi tidak secara otomatis memahami atribut vertex untuk metalness dan roughness. Untuk menggunakannya, di editor material buat node Vertex Color, atur propertinya ke atribut warna berikutnya (biasanya Col.001). Hubungkan node 'Separate XYZ', kirim X ke Roughness, dan Y ke Metallic.

Video ini menunjukkan prosesnya:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Dukungan fitur USD

USD adalah format yang kompleks, spesifikasinya mendukung banyak fitur, tetapi tidak semua perangkat lunak 3D akan mendukungnya. OSX/iOS misalnya tidak mendukung warna vertex. Mode preset di dalam eksportir USD mencoba menebak kompatibilitas terbaik dengan OpenUSD, Apple, Procreate, Zbrush.

::: 

## Render

Ekspor gambar yang merupakan kombinasi dari semua pengaturan dalam proyek (lampu, material, post processing, dll). 

![](/images/file_render.webp)
### Preview

Tombol preview kecil di sebelah judul menu akan meredupkan toolbar untuk membantu mempratinjau hasil akhir.

### Transparent background
Aktifkan channel alpha untuk render, berguna untuk menggabungkan render dengan gambar lain di program 2D. Perhatikan bahwa transparansi parsial tidak didukung.

### Show interface
Aktifkan penyertaan UI Nomad dalam render.

### Render ratio
Pengali pada resolusi gambar.

### Final size
Resolusi yang digunakan untuk render. Saat `Custom` dipilih, slider lebar dan tinggi akan diaktifkan. 

Saat menu File aktif, overlay garis putus-putus akan digambar di viewport untuk menunjukkan area render jika tidak cocok dengan resolusi layar (perhatikan bahwa Anda harus dalam mode lanskap agar ini akurat).

### Export png
Klik tombol ini untuk memulai proses render. Setelah selesai Anda dapat memilih bagaimana menyimpan atau membagikan gambar.

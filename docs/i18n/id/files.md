# ![](/icons/open.webp) Berkas {#files}

Menu berkas memungkinkan Anda menyimpan dan memuat proyek Nomad, mengimpor dan mengekspor model 3D, serta mengekspor gambar render.

![](/images/file_menu.webp)

## Proyek {#project}
![](/images/file_project.webp)

Sebuah thumbnail dari penyimpanan terakhir ditampilkan di bagian atas menu ini. Mengklik thumbnail ini akan menampilkan mini browser, ketuk dua kali pada proyek lain untuk menampilkan mini menu untuk membuka, menambah, menyimpan, mengkloning, mengganti nama, atau menghapus proyek tersebut.

### ![](/icons/nomad.webp) Preset {#preset}
Akses koleksi demo dan komponen karakter. Pilih satu, lalu pilih lagi untuk memilih Buka, Tambah ke Skena atau Klon entri tersebut ke dalam folder proyek Anda.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Simpan {#save}
Simpan proyek Nomad.

### ![](/icons/save_as.webp) Simpan Sebagai... {#save-as}
Tampilkan browser proyek untuk memungkinkan Anda menyimpan proyek Nomad dengan nama baru.

### ![](/icons/pencil.webp) Ganti nama {#rename}
Tampilkan kotak teks untuk mengganti nama proyek saat ini.

### ![](/icons/open.webp) Buka... {#open}
Tampilkan browser proyek untuk membuka sebuah proyek.

### ![](/icons/add_file.webp) Tambah ke skena... {#add}
Tampilkan browser proyek, ketika sebuah proyek dipilih isinya akan digabungkan dengan skena saat ini.

### ![](/icons/trash.webp) Hapus... {#delete}
Tampilkan browser proyek, proyek apa pun yang dipilih akan dihapus dari sistem berkas.

### ![](/icons/new_file.webp) Baru {#new}
Mulai proyek baru, jika ada perubahan yang belum disimpan Anda akan ditanya apakah ingin menyimpannya.

### ![](/icons/autosave.webp) Simpan Otomatis... {#auto-save}
Menu untuk mengatur opsi penyimpanan otomatis.

Jika Anda mengaktifkan autosave, Anda dapat mengatur pengatur waktu sehingga popup akan muncul secara berkala.
Alasan Nomad tidak menyimpan di latar belakang adalah karena berkas 3D bisa sangat besar sehingga dapat menyebabkan lag yang signifikan saat Anda sedang memahat.

Selain itu, untuk menghindari masalah kehabisan memori, skena biasanya dikompresi sebelum operasi penyimpanan.
Kompresi/dekompresi ini juga akan memperlambat operasi penyimpanan.

### Jendela munculan pengatur waktu {#timer-pop-up}
Seberapa sering popup pengatur waktu akan muncul.

### Batas waktu munculan {#popup-timeout}
Aktifkan batas waktu popup.

### Abaikan simpan otomatis {#discard-autosave}
Jika berkas auto save ada untuk sebuah proyek, berkas tersebut akan otomatis dimuat sebagai pengganti proyek asli. Jika ini tidak diperlukan, tombol ini akan menghapus autosave. Memuat berkas kemudian akan memuat penyimpanan manual terakhir dari proyek tersebut.


## Impor {#import}

### ![](/icons/add_file.webp) Impor {#import-button}
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

### ![](/icons/cog.webp) Lanjutan {#advanced}
Tampilkan opsi impor lanjutan:

### Proyek/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Pertahankan topologi {#keep-topology}
Secara bawaan Nomad akan mencoba memperbaiki geometri bermasalah saat dimuat. Mengaktifkan ini akan menghentikan Nomad dari pengurutan ulang vertex/face, penghapusan duplikat vertex/face, dan penghapusan vertex yang tidak digunakan.

#### Lewati tekstur {#skip-textures}
Lewati pemuatan tekstur untuk format yang mendukungnya seperti glTF.

### Proyek / glTF {#project-gltf}
#### Pertahankan pengaturan antarmuka {#keep-gui-settings}
Aktifkan penyimpanan pengaturan GUI dan proyek di dalam berkas Nomad .nom atau glTF.

### OBJ {#obj}
#### Pisah OBJ berdasarkan grup {#split-obj-by-groups}
Aktifkan pemisahan grup OBJ menjadi objek terpisah.

#### Ruang Warna {#color-space}
Atur mode warna yang diinterpretasikan dari OBJ sebagai Linear, sRGB, atau Auto.

### PLY {#ply}
#### Ruang Warna {#color-space-ply}
Atur mode warna yang diinterpretasikan dari PLY sebagai Linear, sRGB, atau Auto.


### FBX {#fbx}
#### Ruang Warna {#color-space-fbx}
Atur mode warna yang diinterpretasikan dari OBJ sebagai Linear, sRGB, atau Auto.



## Ekspor {#export}
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


### Semua/Terlihat/Terpilih {#allvisibleselected}
Status tombol aktif akan menentukan objek mana yang akan diekspor. Angka di sebelah ikon menunjukkan berapa banyak objek yang akan diekspor untuk opsi tersebut.

### Warna verteks {#vertex-colors}
Ekspor warna vertex jika didukung oleh format berkas.

### PBR Paint {#pbr-paint}
Warna vertex PBR diekspor sebagai atribut warna vertex sekunder.
Channel dikemas dengan cara berikut:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Layer {#layers}
Layer didukung melalui glTF morph targets.
Nomad juga mengekspor warna, roughness, dan metalness per-layer tetapi ini akan diabaikan oleh perangkat lunak lain.

### Pengecatan layer {#layer-painting}
Ekspor pengecatan layer, biasanya diabaikan oleh perangkat lunak lain.

### Grup Bidang {#face-group}
Ekspor facegroup, ekspor terkadang dapat mengganggu perangkat lunak lain.

### Normal {#normals}
Ekspor informasi normal. Perhatikan bahwa Nomad akan selalu menghitung normalnya sendiri saat mengimpor format berkas lain.

### Tangen {#tangents}
Ekspor informasi tangent, digunakan jika model memiliki normal map. 

### Tekstur {#textures}
Jika tekstur telah ditambahkan ke material, tekstur akan diekspor. Perhatikan bahwa ini tidak akan melakukan baking tekstur, hal itu dilakukan melalui opsi bake di topology.

### Tombol ekspor {#export-button}
Klik ini untuk mengekspor geometri menggunakan pengaturan yang dipilih.

::: tip Tip: Impor roughness dan metalness ke Blender

Blender dapat mengimpor glTF/glb, tetapi tidak secara otomatis memahami atribut vertex untuk metalness dan roughness. Untuk menggunakannya, di editor material buat node Vertex Color, atur propertinya ke atribut warna berikutnya (biasanya Col.001). Hubungkan node 'Separate XYZ', kirim X ke Roughness, dan Y ke Metallic.

Video ini menunjukkan prosesnya:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Dukungan fitur USD

USD adalah format yang kompleks, spesifikasinya mendukung banyak fitur, tetapi tidak semua perangkat lunak 3D akan mendukungnya. OSX/iOS misalnya tidak mendukung warna vertex. Mode preset di dalam eksportir USD mencoba menebak kompatibilitas terbaik dengan OpenUSD, Apple, Procreate, Zbrush.

::: 

## Render {#render}

Ekspor gambar yang merupakan kombinasi dari semua pengaturan dalam proyek (lampu, material, post processing, dll). 

![](/images/file_render.webp)
### Pratinjau {#preview}

Tombol preview kecil di sebelah judul menu akan meredupkan toolbar untuk membantu mempratinjau hasil akhir.

### Latar belakang transparan {#transparent-background}
Aktifkan channel alpha untuk render, berguna untuk menggabungkan render dengan gambar lain di program 2D. Perhatikan bahwa transparansi parsial tidak didukung.

### Tampilkan antarmuka {#show-interface}
Aktifkan penyertaan UI Nomad dalam render.

### Rasio render {#render-ratio}
Pengali pada resolusi gambar.

### Ukuran akhir {#final-size}
Resolusi yang digunakan untuk render. Saat `Custom` dipilih, slider lebar dan tinggi akan diaktifkan. 

Saat menu File aktif, overlay garis putus-putus akan digambar di viewport untuk menunjukkan area render jika tidak cocok dengan resolusi layar (perhatikan bahwa Anda harus dalam mode lanskap agar ini akurat).

### Ekspor png {#export-png}
Klik tombol ini untuk memulai proses render. Setelah selesai Anda dapat memilih bagaimana menyimpan atau membagikan gambar.
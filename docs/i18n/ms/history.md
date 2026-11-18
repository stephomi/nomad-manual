# ![](/icons/history.webp) Sejarah {#history}
![](/images/history_overview.webp)

Seperti kebanyakan alat penciptaan kandungan, anda boleh membuat asal/ulang semula semua suntingan dalam Nomad.
Sejarah boleh menjadi besar, jadi anda yang menentukan berapa banyak yang disimpan dalam memori, berapa banyak yang disimpan dalam storan, dan sama ada ia disimpan bersama projek anda.

::: tip
Anda boleh menggunakan gerak isyarat pantas untuk buat asal/ulang semula:
- Ketik dengan 2 jari untuk buat asal
- Ketik dengan 3 jari untuk ulang semula
:::

## ![](/icons/history.webp) Sejarah {#history-panel}
![](/images/history_history.webp)

Panel ini memaparkan timbunan sejarah: bilangan langkah, nama operasi, objek yang terlibat, dan jumlah memori yang digunakan oleh langkah itu.

Ketik satu entri untuk kembali (atau maju) ke keadaan tersebut. Tekan lama satu entri untuk memadamnya secara kekal bersama semua sejarah yang lebih lama, cara pantas untuk mengosongkan memori apabila anda sudah berpuas hati dengan arca anda.

### ![](/icons/speed.webp) Main semula {#replay}
Butang main di bahagian bawah kiri berundur ke akar, kemudian mengulang semula operasi satu demi satu, cara yang seronok untuk melihat arca anda dibina. Gelangsar menetapkan kelajuan dalam operasi sesaat. Ketik butang itu sekali lagi untuk berhenti; buat asal/ulang semula atau ketikan pada satu entri juga menghentikannya.

Sebelum ia bermula, satu tetingkap timbul membolehkan anda memilih:
* `Terbalikkan` - Buat asal dari keadaan semasa kembali ke akar, bukannya main semula dari akar.
* `Pulihkan Kamera` - Kamera mengikut operasi yang dimainkan semula, walaupun [Pulihkan Kamera](#restore-camera) dimatikan.
* `Pelicinan kamera` - Kamera meluncur di antara pandangan dan bukannya melompat ke setiap satu. Nilai yang lebih tinggi memberikan kamera yang lebih tenang.

::: warning
Main semula masih dalam percubaan.
:::

## Sertakan tindakan {#include-actions}

Ikon di bahagian bawah panel Sejarah memilih jenis suntingan yang direkodkan dalam sejarah:

| Tindakan      | Ikon                          | Penerangan                                                                         |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Lampu      | ![](/icons/light.webp)        | Suntingan lampu. Menggerakkan lampu dengan Gizmo sentiasa direkodkan, kerana ia boleh menjejaskan objek lain dalam hierarki adegan |
| Shading     | ![](/icons/sun.webp)          | Mod PBR, MatCap dan Tanpa cahaya, MatCap dan HDRI                                   |
| Pasca Pemprosesan | ![](/icons/postprocess.webp)  | Suntingan pemprosesan pasca                                                                   |
| Pemilihan   | ![](/icons/tool_lattice.webp) | Suntingan pemilihan Lattice, seperti klik, pemilihan lasso dan nyahpilih          |

## Tetapan {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Pulihkan Kamera {#restore-camera}
Untuk setiap operasi, sudut pandangan kamera disimpan.
Jika anda mengaktifkan pilihan ini, membuat asal atau mengulang semula sesuatu operasi akan mengembalikan kamera ke sudut pandangan yang disimpan.

### ![](/icons/history.webp) Simpan sejarah {#save-history}
Kekalkan sejarah buat asal apabila projek disimpan, supaya ia kekal selepas projek dibuka semula. Matikannya untuk memastikan fail projek anda lebih kecil.

### ![](/icons/ram.webp) Had RAM {#history-limit-mb}
Jumlah maksimum sejarah yang disimpan dalam RAM. Keadaan yang lebih lama dipindahkan ke storan dan dimuatkan semula apabila diperlukan; ia tidak dipadam.

### ![](/icons/save.webp) Had storan {#storage-limit}
Jumlah maksimum storan yang digunakan oleh sejarah projek ini. Apabila had dicapai, operasi yang paling lama dipadam secara kekal.

::: tip
Had baharu berkuat kuasa selepas suntingan, buat asal atau ulang semula yang berikutnya.
:::

### ![](/icons/undo.webp) Amaran buat asal {#maximum-undoable}
Melompat ke belakang lebih daripada bilangan operasi ini sekali gus akan meminta pengesahan terlebih dahulu. Jika anda membuat suntingan selepas itu, semua operasi selepas titik tersebut akan hilang, jadi ini melindungi anda daripada ketikan tidak sengaja jauh di bawah senarai.

## Statistik memori {#memory-stats}

Bahagian ini memberikan pecahan memori yang digunakan oleh Nomad.

# ![](/icons/history.webp) Riwayat {#history}
![](/images/history_overview.webp)

Seperti kebanyakan aplikasi pembuat konten, Anda bisa mengurungkan dan mengulangi semua perubahan di Nomad.
Riwayat bisa menjadi besar, jadi Anda yang menentukan seberapa banyak yang disimpan di memori, seberapa banyak yang disimpan di penyimpanan, dan apakah riwayat ikut disimpan bersama proyek Anda.

::: tip
Anda bisa menggunakan gestur cepat untuk mengurungkan/mengulangi:
- Ketuk dengan 2 jari untuk mengurungkan
- Ketuk dengan 3 jari untuk mengulangi
:::

## ![](/icons/history.webp) Riwayat {#history-panel}
![](/images/history_history.webp)

Panel ini menampilkan tumpukan riwayat: nomor langkah, nama operasi, objek yang terkena, dan jumlah memori yang dipakai langkah tersebut.

Ketuk sebuah entri untuk melompat mundur (atau maju) ke keadaan itu. Tekan lama sebuah entri untuk menghapusnya secara permanen beserta semua riwayat yang lebih lama, cara cepat untuk mengosongkan memori setelah Anda puas dengan pahatan Anda.

### ![](/icons/speed.webp) Putar ulang {#replay}
Tombol putar di kiri bawah memutar mundur ke awal, lalu mengulangi operasi satu per satu, cara yang seru untuk menyaksikan pahatan Anda terbentuk. Penggesernya mengatur kecepatan dalam operasi per detik. Ketuk tombolnya lagi untuk berhenti; urungkan/ulangi atau mengetuk sebuah entri juga akan menghentikannya.

Sebelum dimulai, sebuah popup memungkinkan Anda memilih:
* `Balikkan` - Mengurungkan dari keadaan saat ini kembali ke awal, alih-alih memutar ulang dari awal.
* `Kembalikan kamera` - Kamera mengikuti operasi yang diputar ulang, bahkan saat [Kembalikan kamera](#restore-camera) dimatikan.
* `Penghalusan kamera` - Kamera meluncur mulus di antara sudut pandang alih-alih melompat ke setiap sudut pandang. Nilai yang lebih tinggi membuat kamera lebih tenang.

::: warning
Putar ulang masih bersifat eksperimental.
:::

## Sertakan tindakan {#include-actions}

Ikon di bagian bawah panel Riwayat menentukan jenis perubahan apa saja yang dicatat dalam riwayat:

| Tindakan    | Ikon                          | Deskripsi                                                                           |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Cahaya      | ![](/icons/light.webp)        | Perubahan cahaya. Memindahkan cahaya dengan Gizmo selalu dicatat, karena bisa memengaruhi objek lain dalam hierarki adegan |
| Shading     | ![](/icons/sun.webp)          | Mode PBR, MatCap, dan Unlit, MatCap, serta HDRI                                     |
| Pemrosesan Pasca | ![](/icons/postprocess.webp)  | Perubahan pemrosesan pasca                                                     |
| Seleksi     | ![](/icons/tool_lattice.webp) | Perubahan seleksi Lattice, seperti klik, seleksi laso, dan pembatalan seleksi       |

## Pengaturan {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Kembalikan kamera {#restore-camera}
Untuk setiap operasi, sudut pandang kamera disimpan.
Jika opsi ini diaktifkan, mengurungkan atau mengulangi sebuah operasi akan mengembalikan kamera ke sudut pandang yang tersimpan.

### ![](/icons/history.webp) Simpan riwayat {#save-history}
Menyimpan riwayat urungkan saat proyek disimpan, sehingga riwayat tetap ada ketika proyek dibuka kembali. Matikan agar file proyek Anda lebih kecil.

### ![](/icons/ram.webp) Batas RAM {#history-limit-mb}
Jumlah maksimum riwayat yang disimpan di RAM. Keadaan yang lebih lama dipindahkan ke penyimpanan dan dimuat lagi saat dibutuhkan, jadi tidak dihapus.

### ![](/icons/save.webp) Batas penyimpanan {#storage-limit}
Jumlah maksimum ruang penyimpanan yang dipakai riwayat proyek ini. Saat batasnya tercapai, operasi tertua dihapus secara permanen.

::: tip
Batas baru berlaku setelah perubahan, urungkan, atau ulangi berikutnya.
:::

### ![](/icons/undo.webp) Peringatan urungkan {#maximum-undoable}
Melompat mundur lebih dari sekian operasi sekaligus akan meminta konfirmasi terlebih dahulu. Jika Anda membuat perubahan setelahnya, semua operasi setelah titik itu akan hilang, jadi ini melindungi Anda dari ketukan tidak sengaja jauh di bawah daftar.

## Statistik memori {#memory-stats}

Bagian ini memberikan rincian memori yang dipakai oleh Nomad.

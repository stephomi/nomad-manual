# ![](/icons/history.webp) Riwayat {#history}
![](/images/history_overview.webp)

Seperti kebanyakan alat pembuatan konten, Anda dapat membatalkan/mengulang semua pengeditan di Nomad.
Ada batasan berapa banyak operasi yang dapat dibatalkan, tetapi Anda dapat mengontrol perilaku ini.

::: tip
Anda dapat menggunakan gestur cepat untuk undo/redo:
- Ketuk dengan 2 jari untuk undo
- Ketuk dengan 3 jari untuk redo
:::

## Riwayat {#history-panel}
![](/images/history_history.webp)

Panel ini menampilkan tumpukan riwayat, menunjukkan jumlah langkah, nama operasi, dan jumlah memori yang digunakan oleh langkah tersebut.

## Pengaturan {#settings}
![](/images/history_settings.webp)

### Batas riwayat (Mb) {#history-limit-mb}
Jika tumpukan riwayat melebihi nilai ini, operasi yang lebih lama akan dihapus sehingga penggunaan memori sesuai dengan batas ini.


### Maksimum dapat diurungkan {#maximum-undoable}
Anda dapat mengontrol jumlah maksimum operasi.

## Pulihkan kamera {#restore-camera}
Untuk setiap operasi, sudut pandang kamera disimpan.
Jika Anda mengaktifkan opsi ini, membatalkan atau mengulang suatu operasi akan mengatur ulang kamera ke sudut pandang yang tersimpan.

## Sertakan tindakan {#include-actions}

* `Lights` - Jika dinonaktifkan, operasi lampu (selain perpindahan gizmo) akan diabaikan oleh tumpukan riwayat
* `Matcaps & HDRIs` - Jika dinonaktifkan, perubahan pada matcap dan hdri akan diabaikan oleh tumpukan riwayat
* `PostProcess` - Jika dinonaktifkan, perubahan pada opsi postprocess akan diabaikan oleh tumpukan riwayat

## Statistik memori {#memory-stats}

Bagian ini memberikan rincian penggunaan memori oleh Nomad.
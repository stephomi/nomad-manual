# ![](/icons/history.webp) Sejarah {#history}
![](/images/history_overview.webp)

Seperti kebanyakan alat penciptaan kandungan, anda boleh buat asal/ulang semula semua penyuntingan dalam Nomad.
Terdapat had kepada bilangan operasi yang boleh dibuat asal, tetapi anda boleh mengawal tingkah laku ini.

::: tip
Anda boleh menggunakan gerak isyarat pantas untuk buat asal/ulang semula:
- Ketik dengan 2 jari untuk buat asal
- Ketik dengan 3 jari untuk ulang semula
:::

## Sejarah {#history-panel}
![](/images/history_history.webp)

Panel ini memaparkan timbunan sejarah, menunjukkan bilangan langkah, nama operasi, dan jumlah memori yang digunakan oleh langkah tersebut.

## Tetapan {#settings}
![](/images/history_settings.webp)

### Had sejarah (Mb) {#history-limit-mb}
Jika timbunan sejarah melebihi nilai ini, operasi yang lebih lama akan dibuang supaya penggunaan memori mematuhi had ini.


### Maksimum boleh buat asal {#maximum-undoable}
Anda boleh mengawal bilangan maksimum operasi.

## Pulihkan kamera {#restore-camera}
Untuk setiap operasi, sudut pandang kamera akan disimpan.
Jika anda mengaktifkan pilihan ini, membuat asal atau mengulang semula sesuatu operasi akan menetapkan semula kamera kepada sudut pandang yang disimpan.

## Sertakan tindakan {#include-actions}

* `Lights` - Apabila dinyahdayakan, operasi cahaya (selain pergerakan gizmo) akan diabaikan oleh timbunan sejarah
* `Matcaps & HDRIs` - Apabila dinyahdayakan, perubahan pada matcap dan hdri akan diabaikan oleh timbunan sejarah
* `PostProcess` - Apabila dinyahdayakan, perubahan pada pilihan pascaproses akan diabaikan oleh timbunan sejarah

## Statistik memori {#memory-stats}

Bahagian ini memberikan pecahan penggunaan memori oleh Nomad.
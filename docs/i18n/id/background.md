# ![](/icons/image.webp) Latar Belakang {#background}

Menu ini mengatur warna latar belakang Nomad, serta gambar referensi yang ingin Anda gunakan.

![](/images/background_overview.webp)

## Jenis {#type}
![](/images/background_selector.webp)

Ada tiga pilihan untuk latar belakang viewport.

* `Lingkungan` - Menampilkan peta lingkungan yang dipilih di [Shading](shading.md). Tampilannya bisa diatur lebih lanjut dengan penggeser `Buram` dan `Eksposur` (kecerahan).
* `Warna` - Satu warna datar pilihan Anda
* `Gradien` - Peralihan antara dua warna. Penggeser `Faktor` memungkinkan Anda menggeser titik tengah gradien.

### Jenis gradien {#gradient-type}
Dengan `Gradien`, pilih bentuknya:
* `Linear` - Gradien lurus, arahnya diatur dengan penggeser `Sudut`.
* `Radial` - Gradien melingkar yang berawal dari tengah layar.
* `Langit` - Gradien yang terikat pada cakrawala dunia, sehingga ikut bergerak saat Anda mengarahkan kamera ke atas dan ke bawah.

Setiap warna punya tombol reset dan pemilih warna, untuk mengambil warna langsung dari layar.

## ![](/icons/lock.webp) Sinkronkan dengan kunci kamera {#sync-on-camera-lock}
Saat kamera dikunci dengan [Navigator](settings.md#snap-cube), gambar referensi mengikuti gerakan kamera, sehingga tetap sejajar dengan pahatan Anda.

* `Allow roll (trackball)` - Mengizinkan kamera berguling saat Anda keluar dari kunci kamera.
* `Reset saat buka kunci` - Mereset tampilan saat Anda keluar dari kunci kamera.

## Gambar referensi {#reference}

![](/images/background_reference.webp)

Anda bisa menambahkan gambar pilihan Anda di latar belakang sebagai referensi. Ketuk `Impor...` untuk menambahkannya, lalu centang `Gambar referensi` untuk menampilkannya.
Anda bisa mengubah posisi dan skalanya, misalnya jika ingin memindahkannya ke sudut layar.

### ![](/icons/tool_transform.webp) Transformasi {#transform}

Tombol ini memungkinkan Anda menempatkan gambar referensi secara interaktif. Gunakan 2 jari untuk menggeser, mengubah skala, dan memutar gambar referensi ke posisinya. `Reset pengaturan` mengembalikan gambar ke penempatan awalnya. Penempatan akhirnya akan tercermin pada penggeser di bawah ini:

* `Overlay` - Pada 0%, gambar referensi selalu berada di belakang objek Anda, pada 100% gambar berada di depan.
* `Opasitas` - Seberapa transparan gambarnya.
* `Pemrosesan pasca` - Menerapkan efek pemrosesan pasca pada gambar referensi. Matikan untuk mempertahankan warna aslinya.
* `Posisi X` / `Posisi Y` - Posisi X dan Y gambar.
* `Skala` - Skala gambar.
* `Rotasi` - Rotasi gambar.


::: tip

Kamera dan gambar referensi saling terhubung.

Artinya, jika Anda sudah menyejajarkan gambar referensi dengan pahatan Anda lalu membuat kamera dari [menu Kamera](camera.md), posisi, rotasi, dan skala gambar referensi juga ikut tersimpan bersama kamera itu. Anda bisa mematikan gambar referensi dan memutar ke sudut pandang lain. Saat Anda melihat melalui kamera itu lagi, gambar referensi akan aktif kembali dengan pengaturan yang Anda gunakan.

Anda bahkan bisa memilih gambar yang berbeda untuk setiap kamera!

 ![](/videos/reference_camera.mp4)

:::

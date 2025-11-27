# ![](/icons/image.webp) Latar Belakang

Menu ini mengontrol warna latar belakang Nomad, serta gambar referensi apa pun yang akan digunakan.

![](/images/background_overview.webp)

## Latar Belakang 
![](/images/background_selector.webp)

Ada tiga opsi untuk latar belakang viewport.

* `Environment` - Menampilkan peta lingkungan yang dipilih di [Shading](shading). Ini dapat dikontrol lebih lanjut dengan kontrol Blur dan Exposure (kecerahan). 
* `Color` - Warna datar yang dapat Anda pilih
* `Gradient` - Gradasi warna dari atas ke bawah. Slider Factor memungkinkan Anda menentukan titik tengah gradasi.  

## Gambar Referensi

![](/images/background_reference.webp)

Anda dapat menambahkan gambar pilihan Anda pada latar belakang untuk digunakan sebagai referensi.
Anda dapat mengubah posisi dan skala, misalnya jika Anda ingin memindahkannya ke sudut layar.

### ![](/icons/tool_transform.webp) Transform 

Tombol ini akan memungkinkan Anda menempatkan gambar referensi secara interaktif. Gunakan 2 jari untuk menggeser, menskalakan, dan memutar gambar referensi ke tempatnya. Penempatan akhir akan tercermin pada slider di bawah:

* `Overlay` - pada 0% gambar referensi akan selalu berada di belakang objek Anda, pada 100% berada di depan. 
* `Opacity` - Seberapa transparan gambar tersebut.
* `Position` - Posisi X dan Y gambar.
* `Rotation` - Rotasi gambar.
* `Scale` - Skala gambar.


::: tip

Kamera dan gambar referensi saling terhubung. 

Ini berarti jika Anda mengatur gambar referensi agar sejajar dengan sculpt Anda, jika Anda membuat kamera dari [menu Camera](camera), posisi, rotasi, dan skala gambar referensi juga disimpan bersama kamera. Anda dapat mematikan gambar referensi, memutar ke viewport lain. Jika Anda kembali melihat melalui kamera, gambar referensi akan diaktifkan dengan pengaturan yang Anda gunakan.

Ini bahkan termasuk memilih gambar yang berbeda untuk kamera yang berbeda!

 ![](/videos/reference_camera.mp4)

:::

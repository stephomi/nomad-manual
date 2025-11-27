# ![](/icons/symmetry.webp) Simetri

Menu ini mengawal bagaimana sapuan akan diulang merentasi satah cermin atau secara jejari, dan cara untuk memulihkan simetri pada objek yang tidak simetri.

![](/images/symmetry_overview.webp) 

## Gambaran keseluruhan 
Anda boleh menggunakan simetri dalam beberapa cara:

* Sebagai cermin, membalikkan kerja merentasi X (kiri/kanan), Y (atas/bawah), Z (belakang/hadapan), atau gabungan daripadanya. 
* Simetri jejari boleh ditetapkan pada X Y Z dengan bilangan ulangan, contohnya mengukir bentuk tapak sulaiman. 
* Cermin boleh beroperasi di sekeliling titik asal (dipanggil mod dunia/world mode) atau di sekeliling pusat objek (dipanggil mod setempat/local mode).
* Ukiran yang bermula tanpa simetri boleh dipaksa menjadi simetri.

Pintasan untuk mengaktif/nyahaktifkan simetri juga boleh ditemui pada panel pantas kiri (*"Sym"*). Huruf kecil 'L/W' menunjukkan sama ada Nomad berada dalam mod simetri Setempat (Local) atau Dunia (World). Anda juga boleh tekan lama atau leret ke tengah skrin untuk memaparkan menu.

![](/images/symmetry_button.webp) 

Ini ialah pilihan global, jadi keadaannya akan dibawa merentasi alat yang berbeza.
Satu-satunya pengecualian ialah alat transform ([Move](#translate), [Rotate](#rotate), [Scale](#scale) dan [Gizmo](#gizmo)) yang mempunyai keadaan simetri mereka sendiri.

::: tip
Menu simetri terutamanya untuk mengawal simetri sapuan. Anda juga boleh mencerminkan dan mengulang objek melalui [repeater yang terdapat dalam menu adegan](scene#repeaters). 
:::

## Enabled
Togol mod cermin, ini sama seperti butang `Sym` dalam panel pantas kiri. 

## Planes

Aktifkan satah simetri dan bilangan ulangan untuk simetri jejari. Perhatikan bahawa anda tidak perlu memilih hanya satu satah, anda boleh mengaktifkan 1, 2 atau 3 satah untuk simetri yang kompleks.

Paksi dan kiraan ulangan untuk simetri jejari. Perhatikan bahawa ini juga tidak terhad kepada satu paksi, dan malah boleh berfungsi bersama dengan simetri satah untuk menghasilkan hasil terperinci dengan sangat pantas. (Bilangan ulangan keseluruhan dihadkan kepada 150)

![](/videos/symmetry_demo.mp4) 

## Method
Cermin boleh sama ada 'Local', dan bergerak bersama objek, atau 'World', dan tidak bergerak. Jika anda tidak pasti mod mana yang diperlukan, perhatikan satah cermin dan penunjuk jejari yang ditindih pada objek. Dalam mod setempat, jika anda menggunakan gizmo transform dan menggerakkan model, penunjuk cermin juga akan bergerak. Dalam mod dunia, penunjuk cermin akan kekal tetap, dan objek akan meluncur melaluinya.

## Mirroring
![](/images/symmetry_mirroring.webp)

Apabila mengukir berhampiran satah simetri, sesetengah berus akan mempunyai tingkah laku simetri yang tidak sempurna. Bahagian ini membolehkan anda memulihkan simetri dengan menyalin satu sisi ukiran anda ke sisi yang lain. 


`Direction` - Butang `<<` dan `>>` menentukan sisi mana yang akan disalin ke sisi yang lain. Nomad mengiranya daripada pandangan semasa anda, jadi menetapkannya kepada `<<` sebagai contoh akan sentiasa menyalin dari kanan skrin ke kiri skrin.

![](/icons/shield.webp) `Mask` - Butang mask membolehkan anda mengasingkan bahagian yang akan dicerminkan; memask sisi destinasi akan melindungi kawasan itu, memask sisi sumber akan menghalang kawasan tersebut daripada dicerminkan ke destinasi. 

![](/icons/tool_hide.webp) `Hide` - Apabila aktif, kawasan yang disembunyikan pada sisi sumber tidak akan dicerminkan ke destinasi. 

`Mirror` akan cuba mengenal pasti sama ada topologi adalah sama pada kedua-dua sisi cermin, dan jika ya, hanya menggerakkan verteks. Ini ialah senario yang lebih lazim.

`Split & Mirror` pada asasnya akan memotong objek sepanjang cermin, menyalin satu sisi, mencerminkannya ke sisi lain, dan mengimpal verteks sepanjang cermin. Ia ialah pilihan yang lebih destruktif, dan akan memadam multiresolusi, tetapi kadangkala kaedah ini diperlukan jika model sangat berbeza merentasi cermin.

### Flip object
![](/images/symmetry_flip.webp)
Menjadikan sisi kiri sebagai sisi kanan, dan sebaliknya. Penampilannya serupa seperti jika anda menggunakan menu alat gizmo dan menetapkan skala kepada -1 pada X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Adalah mungkin untuk mengedit lokasi dan orientasi simetri (tetapi tidak digalakkan!). Jika perlu, `World center` dan `Orientation` akan menetapkan semula lokasi dan orientasi simetri kepada nilai lalai.

Nomad biasanya tahu di mana untuk meletakkan satah simetri. Adalah tidak digalakkan untuk melaraskannya secara manual, tetapi butang `Gizmo (Edit)` membenarkan ini untuk pengguna lanjutan. Apabila butang ini diklik, satu gizmo akan dipaparkan untuk membolehkan anda menterjemah dan memutar satah simetri. Jika anda ingin memulihkan pusat dan orientasi lalai, butang `object center` dan `orientation` akan melakukannya.

Tingkah laku pilihan ini akan berubah bergantung pada ruang (*Local/World*) yang anda gunakan.
Jadi jika ia tidak berfungsi seperti yang anda jangkakan, pastikan anda menyemak sama ada anda berada dalam ruang yang betul.

::: tip
Butang `Gizmo (Edit)` sengaja dikelabukan sebagai peringatan bahawa anda mungkin tidak sepatutnya menggunakannya!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` dan `Show plane` akan menogol tindihan paparan pandangan bagi lokasi simetri. Perhatikan bahawa mematikan pilihan ini hanya akan berkuat kuasa apabila menu simetri ditutup.

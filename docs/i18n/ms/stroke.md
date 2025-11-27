# ![](/icons/pencil.webp) Goresan    

---
![](/images/stroke_overview.webp) 

## Gambaran keseluruhan 

Anda boleh menyesuaikan kelakuan goresan bagi kebanyakan berus alat.
Tetapannya adalah serupa dengan yang terdapat dalam aplikasi lukisan 2D, namun beberapa pilihan adalah khusus untuk pengukiran dan 3D.

Pilihan ini dibahagikan kepada 5 sub-menu:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Kawal cara goresan digunakan pada model                            |
| Alpha    | ![](/icons/alpha.webp)      | Cara tekstur skala kelabu digunakan untuk cap berus                |
| Falloff  | ![](/icons/falloff.webp)    | Kawal bagaimana kekuatan berus berubah dari tengah ke tepi         |
| Filter   | ![](/icons/filter.webp)     | Cara berus dipengaruhi oleh geometri model                         |
| Pressure | ![](/icons/pressure.webp)   | Kawal tindak balas tekanan stylus                                  |

::: tip
Tidak semua pilihan goresan terpakai untuk semua alat. Pilihan goresan yang tidak digunakan oleh alat semasa akan dinyahdaya atau disembunyikan. 
:::


## Stroke

### Radius

![](/images/stroke_radius.webp)

#### Share radius

Apabila diaktifkan, semua alat akan menggunakan radius yang sama, lalainya ialah setiap alat mempunyai radius sendiri.

#### Size

* Screen - radius ditetapkan dalam unit skrin. Jika anda menetapkan radius selebar 100 piksel, ia akan kekal 100 piksel tanpa mengira zum masuk atau keluar.
* Constant (3d) - radius ditetapkan dalam unit 3D. Contohnya jika anda mencipta sfera dan menjadikan radius sama besar dengan sfera, radius akan kekal sama besar dengan sfera apabila anda zum masuk dan keluar.


### Stroke

![](/images/stroke_strokemode.webp)

Goresan boleh bertindak dalam beberapa mod:

### ![](/icons/stroke_dot.webp) Dot
Seret seperti goresan cat biasa. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll
Alpha berus akan diputar untuk mengikut arah goresan, berguna untuk membuat jahitan fabrik. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Cap goresan berus dengan **_ketinggian_** tetap. Seretan akan menetapkan skala dan putaran.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Lock + intensity 
Cap goresan berus dengan **_radius_** tetap. Seretan akan menetapkan ketinggian dan putaran.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Alat `Move` dan `Drag` mempunyai 3 pilihan tersendiri:

### ![](/icons/snake.webp) Drag

Akan terus mengemas kini apa yang berada di dalam radius berus semasa goresan. Goresan pantas akan meninggalkan permukaan di belakang, manakala goresan perlahan akan memegang bahan, menghasilkan bentuk yang lebih panjang. Ini ialah mod lalai untuk alat `Drag`. Dengan `Dynamic Topology` ini boleh digunakan untuk membuat ekstrusi seperti ular. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab
Akan memilih apa yang berada di dalam radius berus apabila berus dimulakan, dan mengekalkan pemilihan itu. Ini berguna untuk operasi alih yang lebih tepat, kerana anda boleh melaraskan jarak alihan dengan teliti dan tidak secara tidak sengaja menggerakkan lebih daripada yang anda pilih pada asalnya. Ini ialah mod lalai untuk alat `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) 
Radius pengguna diabaikan, dan ditetapkan secara dinamik berdasarkan sejauh mana goresan diseret dari titik permulaan. Jarak kecil = radius kecil, jarak lebih besar = radius lebih besar. Gunakan peluncur intensiti untuk mengawal bentuk falloff. Berguna untuk menyekat bentuk organik seperti getah.
![](/videos/stroke_lockradius_drag.mp4) 



### Adjust spacing intensity
![](/images/stroke_space_smooth.webp)

Goresan dengan jarak rendah (kurang daripada 50%) boleh terkumpul dengan cepat, menjadikan goresan lebih kuat berbanding nilai jarak yang lebih tinggi. Togol ini akan mengimbangi perkara ini, supaya goresan adalah kira-kira intensiti yang sama tanpa mengira jarak.

### Stroke spacing
Sejauh mana jarak antara setiap cap berus digunakan semasa operasi seretan. Nilai kurang daripada 100% akan bertindih, memberikan rupa goresan berterusan. Nilai lebih besar daripada 100% akan mula meninggalkan jarak, berguna untuk mengukir perincian seperti jahitan atau zip.

### Lazy rope stabilizer
Goresan akan tertinggal di belakang kedudukan penuding dengan jarak tertentu. Ini boleh digunakan untuk melukis garisan licin.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing
Puratakan berbilang kedudukan penuding untuk mendapatkan goresan yang lebih licin.
Dengan nilai tinggi, goresan akan tertinggal di belakang penuding tetapi akhirnya akan mengejar.
Ini berguna untuk melukis garisan licin.

### Snap radius
Petik permulaan goresan ke hujung goresan sebelumnya. Radius menentukan sejauh mana untuk mencari hujung goresan sebelumnya. Ini boleh berguna apabila melukis garisan panjang berterusan, sambil kerap berhenti seketika.

### ![](/icons/silhouette.webp) Silhouette
![](/images/stroke_silhouette.webp)
Secara lalai goresan hanya akan menjejaskan permukaan model dalam radius berus. Apabila siluet diaktifkan, goresan akan diproyeksikan menembusi keseluruhan model. Ini boleh sangat berguna semasa peringkat awal membentuk model, atau untuk bentuk yang memerlukan sisi kekal tegak lurus.

Arah unjuran boleh ditetapkan secara eksplisit, kaedah lalai 'Closest' akan mengesan sudut terbaik relatif kepada pandangan. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize

![](/images/stroke_randomize.webp)

Intensiti, translasi, putaran dan skala goresan masing-masing boleh dijadikan rawak. Ini boleh digunakan untuk mencipta pelbagai kesan, contohnya rawakkan dengan alat cat boleh mencipta warna bertompok, atau rawakkan dengan alat crease boleh digunakan untuk mencipta perincian kulit.

![](/videos/stroke_randomize.mp4) 

### Stroke Offset

Gunakan ofset malar pada goresan. Ini berguna untuk skrin kecil di mana jari anda akan menutupi goresan. 


## ![](/icons/alpha.webp) Alpha
![](/images/stroke_alpha.webp) 

`Alpha` ialah tekstur yang akan memodulasi kelakuan berus anda.
Ia adalah imej skala kelabu, di mana piksel hitam bermaksud tiada deformasi dan piksel putih deformasi penuh.

Klik pada imej alpha untuk menukarnya.

Klik pada pratonton bahan untuk memuatkan alpha daripada pratetap bahan. Anda juga boleh menyimpan pratetap bahan di sini, dan memilih untuk membenamkan tekstur dengan alat.

::: tip
Tekstur tidak pernah diubah saiz, jadi tekstur besar boleh memperlahankan prestasi.
:::

### Invert pixels
Ini akan membalikkan nilai imej, jadi piksel hitam akan menjadi putih, dan piksel putih akan menjadi hitam.

::: tip

Alpha terbina dalam yang disertakan dengan Nomad tidak boleh diterbalikkan.

:::

### Scaling

Saiz berus dalam Nomad ialah bulatan dengan radius yang ditakrifkan pengguna. Tekstur selalunya segi empat sama atau segi empat tepat, parameter `Scaling` membolehkan anda memutuskan bagaimana tekstur harus muat dalam bulatan. Untuk tekstur segi empat sama, nilai 0.7 akan muat dalam bulatan. Nilai 1 akan menskalakan tekstur lebih besar supaya bulatan muat di dalam, memotong bahagian tepi.

![](/images/alpha_scaling.webp) 

Mengaktifkan `Scaling - Y` akan membolehkan anda meregangkan alpha secara menegak.

![](/images/alpha_scaling_y.webp) 

### Rotation

Tekstur alpha akan diputar untuk mengikut arah goresan. Anda boleh menambah ofset putaran, dan jika ikon kunci diaktifkan, tekstur akan kekal terkunci pada putaran ini relatif kepada skrin.

### Tiling
![](/images/stroke_tiling.webp) 

Kekerapan tekstur diulang dalam profil berus. Mod tiling membolehkan anda mengehadkan kepada satu tekstur dalam goresan, atau tekstur berulang, atau cermin di mana setiap tekstur kedua diterbalikkan untuk mencipta corak atau membantu menjadikan tekstur lancar.

![](/videos/alpha_tiling.mp4) 



### Mid value

Secara lalai piksel hitam bermaksud tiada deformasi, dan piksel putih bermaksud deformasi positif penuh, jadi sebagai contoh, berus clay dengan tekstur alpha batu hanya akan menarik permukaan keluar di mana alpha tidak hitam.

Jika anda mahu berus menolak permukaan ke dalam, atau kedua-duanya menolak ke dalam DAN menarik keluar, anda boleh mengubah nilai tengah. Jadi jika anda menetapkan nilai kepada 0.5, kelabu pertengahan dalam alpha tidak akan melakukan apa-apa, nilai hitam akan menolak ke dalam, putih akan menarik keluar.




## Falloff

![](/images/falloff_menu.webp) 

Ini serupa dengan [Alpha](#alpha), kecuali anda memacu intensiti dengan satu lengkung. Ini digabungkan dengan alpha supaya anda boleh menggunakan tekstur untuk perincian, dan falloff untuk mengawal pemudaran tepi dan intensiti di tengah alat.

Apabila lengkung berada di bahagian atas, ini ialah deformasi penuh, apabila ia berada di bahagian bawah berus tidak memberi kesan.

Anda boleh menganggap lengkung sebagai keratan rentas melalui hujung berus. Bahagian bawah memberikan pratonton rupa satu 'cap' berus pada permukaan model, dan jika terdapat tekstur alpha untuk berus, ini juga akan ditunjukkan untuk mempratonton bagaimana falloff dan alpha akan berinteraksi.

### Preset
Dengan ini dipilih, mengklik pada graf lengkung akan memaparkan menu pratetap. Lengkung bulat akan memberikan hasil yang lebih lembut, lengkung bersudut akan memberikan hasil yang lebih tajam. Butang `Sub` dalam bar alat kiri akan secara berkesan membalikkan falloff, jadi bahagian atas lengkung akan menolak ke dalam permukaan dan bukannya menarik keluar, atau sebaliknya.

### Catmull-Rom
Apabila dipilih, pengguna boleh melukis lengkung falloff mereka sendiri. Penyunting lengkung berfungsi sama seperti lengkung di seluruh Nomad:

* Klik pada lengkung untuk mencipta titik baharu
* Seret titik untuk menukar kedudukannya
* Klik pada titik untuk bertukar antara tajam dan licin
* Seret titik ke titik jiran untuk menghapuskannya

### B-spline
Apabila dipilih, pengguna boleh melukis lengkung falloff mereka sendiri. Penyunting berfungsi sama seperti Catmull-Rom, tetapi titik lengkung mempengaruhi lengkung dan bukannya berada terus pada lengkung, yang boleh membantu dalam mencipta bentuk lengkung yang lebih licin.

Penyunting lengkung mempunyai 3 butang:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Kembangkan penyunting lengkung               |
| Reset    | ![](/icons/reset.webp)     | Kembalikan lengkung ke keadaan lalai         |
| Symmetry | ![](/icons/symmetric.webp) | Paparkan lengkung sebagai 'hujung berus' simetri |


### Influence

* Sphere (3d) - Pengaruh dikira dengan mengambil jarak dari verteks ke pusat berus.
* Circle (2d) - Verteks terlebih dahulu diproyeksikan pada satah kawasan, sebelum mengambil jaraknya ke pusat berus. Ini serupa dengan cara alpha disampel. 
* Cylinder - Pengaruh diproyeksikan melalui kawasan sebagai silinder, digunakan oleh mod Silhouette di bawah.

### Silhouette
Secara lalai goresan hanya akan menjejaskan permukaan model dalam radius berus. Apabila siluet diaktifkan, goresan akan diproyeksikan menembusi keseluruhan model. Ini boleh sangat berguna semasa peringkat awal membentuk model, atau untuk bentuk yang memerlukan sisi kekal tegak lurus.



## Filter

![](/images/filter_menu.webp) 

### Accumulate stroke
Benarkan tiada had kepada berapa banyak bahan boleh ditambah/dibuang setiap goresan. Contohnya alat `Clay` mempunyai ini diaktifkan, jadi bahan boleh terus terkumpul, manakala alat `Brush` mempunyai ini dinyahdaya, jadi goresan akan berhenti menambah bahan jika anda terus menggerakkan goresan yang sama di kawasan mesh yang sama. 

### Front-facing vertex only
Pilihan ini akan mengabaikan verteks yang menghadap belakang.
Ia boleh berguna jika anda mahu mengecat sebahagian geometri nipis tanpa menjejaskan bahagian lain.
Ia juga berfungsi untuk pengukiran tetapi anda mungkin mengalami beberapa artifak.

### Allow dynamic topology
Pilihan ini hanya tersedia jika mesh anda berada dalam mod [Dynamic Topology](topology.md#dynamic-topology). Anda boleh menyahdaya atau mengaktifkan dynamic topology bagi setiap alat.

### Connected topology
Aktifkan hanya pengukiran verteks yang dipautkan kepada permukaan yang anda sentuh dengan alat. Sebagai contoh apabila digunakan dengan alat `Move`, ini akan membolehkan anda menggerakkan satu bahagian walaupun ia bersilang dengan bahagian lain.
![](/videos/connected_topology.mp4)

### Protect Area
![](/images/filter_protect_area.webp) 

Pilihan ini akan menghentikan alat daripada menjejaskan bahagian mesh anda di bawah pelbagai keadaan. 

Pilihan 'Auto' bermaksud jika anda mempunyai hide, atau mask, atau facegroup yang kelihatan dalam menu [Shading](shading), ia akan dilindungi, tetapi jika ia dimatikan dalam menu itu, perlindungan dinyahdaya.

* `All` - Togol untuk menetapkan sama ada penapis perlindungan adalah global, atau bagi setiap alat.
* `Hide` - Jika bahagian mesh disembunyikan dengan alat hide, tetapkan sama ada ia perlu dilindungi.
* `Mask` - Jika bahagian mesh dimask, tetapkan sama ada ia perlu dilindungi.
* `Facegroup` - Tetapkan sama ada anda hanya boleh menggunakan alat dalam facegroup pertama yang disentuh.


### Keep sharp edges
Kecualikan titik yang normalnya terlalu berbeza daripada normal permukaan.

Ia akan mengubah cara kawasan satah dikira (Area sampling).

Pilihan ini boleh berguna untuk alat berasaskan flatten, atau jika anda mahu mewarna permukaan yang kebanyakannya rata tanpa tumpahan berlebihan.

![](/videos/filter_keep_sharp_edges.mp4)

### Area sampling
Sesetengah berus atau pilihan goresan memerlukan normal satah dan kedudukan satah pada permukaan untuk berfungsi.

Anda boleh mengawal cara mengira satah purata ini dengan menetapkan kawasan pensampelan sebagai nisbah radius alat.

Pada 100%, setiap titik di dalam bulatan pemilihan diambil kira.

Pada 0%, hanya verteks atau segi tiga terdekat diambil kira. Nilai ini boleh dipautkan untuk kedua-dua `Normal radius` dan `Position radius`, atau dinyahkunci dan ditetapkan secara berasingan.


### Depth masking
![](/images/stroke_depthmask.webp)

Kecualikan titik yang berada di atas atau di bawah jarak tertentu dari satah yang dikira (Area sampling).

Ini boleh digunakan untuk mengecat hanya pada kawasan berbonggol, atau hanya pada kawasan lekuk.

Graf mewakili keratan rentas permukaan; garisan mendatar ialah tempat permukaan berada, bulatan mewakili radius falloff cat relatif di atas dan di bawah permukaan. `Height offset` ialah peratusan di atas atau di bawah permukaan untuk memulakan pengiraan masking. `Top area` dan `Bottom area` membolehkan anda menskalakan falloff di atas dan di bawah titik ofset.

#### Contoh: Cat dalam lekuk
Untuk mengecat hanya kawasan lekuk, tetapkan height offset kepada -100%, dan laraskan peluncur top area supaya ia menjauhi garisan mendatar. Ini bermakna klik pertama menetapkan kedalaman 'sifar', dan kemudian hanya kawasan di bawah kedalaman ini akan terjejas.

![](/videos/stroke_depth_cavity.mp4)

#### Contoh: Cat pada bonggol
Untuk mengecat hanya di kawasan tinggi, tetapkan height offset kepada +90%, supaya bahagian bawah bulatan bersilang dengan garisan mendatar sedikit sahaja. Apabila anda mengklik di bahagian atas zon 'tinggi', ini akan menetapkan kedalaman, supaya apa sahaja pada kedalaman itu, ditambah sedikit di bawahnya, dan apa sahaja yang lebih tinggi daripadanya, akan dicat. Lekuk dalam akan diabaikan.
![](/videos/stroke_depth_bump.mp4)


## Pressure 
![](/images/pressure_menu.webp) 

Kawal cara tekanan stylus/pen mempengaruhi berus.

Secara lalai `Use global settings` diaktifkan, bermakna semua berus akan berkongsi nilai tekanan yang sama.

### Pressure - Radius

Lengkung ini mengawal bagaimana radius berus dipengaruhi oleh tekanan. Lalainya ialah hubungan linear, jadi jika stylus anda mempunyai tindak balas yang licin, maka perubahan radius juga sepatutnya terasa licin. Namun begitu, banyak stylus mempunyai tindak balas tidak linear, yang boleh anda imbangi dengan lengkung ini. Contohnya, jika radius tidak terasa seperti mencapai nilai maksimum pada tekanan tinggi, gunakan pratetap lengkung seperti 'out-pow3', dengan lengkung yang membengkok ke atas, untuk meningkatkan radius lebih awal.

Dialog ini serupa dengan paparan lengkung falloff, anda boleh menggunakan pratetap dengan mengetik pada tetingkap lengkung, atau melukis lengkung anda sendiri dengan mod Catmull-Rom dan B-Spline.

Jika anda mahukan radius malar, nyahdayakan bahagian ini.

### Pressure - Intensity

Serupa dengan peluncur radius, tetapi untuk mengawal intensiti. Jika anda mahukan intensiti malar, nyahdayakan bahagian ini.

### Pressure smoothing

Puratakan peristiwa tekanan stylus untuk hasil yang lebih licin.

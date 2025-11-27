# ![](/icons/open.webp) Dosyalar

Dosyalar menüsü, Nomad projelerini kaydetmenize ve yüklemenize, 3B modelleri içe ve dışa aktarmanıza ve oluşturulmuş görüntüleri dışa aktarmanıza olanak tanır.

![](/images/file_menu.webp)

## Proje
![](/images/file_project.webp)

Bu menünün üst kısmında son kaydın küçük bir önizlemesi gösterilir. Bu küçük resme tıklamak küçük bir tarayıcı açar, başka bir projeye iki kez dokunarak o projeyi açmak, eklemek, kaydetmek, klonlamak, yeniden adlandırmak, silmek için bir mini menü açabilirsiniz.

### ![](/icons/nomad.webp) Hazır Ayar 
Demo ve karakter bileşenlerinden oluşan bir koleksiyona erişin. Birini seçin, ardından tekrar seçerek Projeyi Aç, Sahneye Ekle veya girişin projeler klasörünüze Klonlanmasını seçin.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Kaydet
Nomad projesini kaydedin.

### ![](/icons/save_as.webp) Farklı Kaydet...
Nomad projesini yeni bir adla kaydetmenizi sağlayan proje tarayıcısını gösterir.

### ![](/icons/pencil.webp) Yeniden Adlandır
Geçerli projeyi yeniden adlandırmak için bir metin kutusu gösterir.

### ![](/icons/open.webp) Aç...
Bir projeyi açmak için proje tarayıcısını gösterir.

### ![](/icons/add_file.webp) Sahneye ekle...
Proje tarayıcısını gösterir, bir proje seçildiğinde içeriği mevcut sahneyle birleştirilir.

### ![](/icons/trash.webp) Sil...
Proje tarayıcısını gösterir, seçilen projeler dosya sisteminden silinir.

### ![](/icons/new_file.webp) Yeni
Yeni bir proje başlatır, kaydedilmemiş değişiklikler varsa kaydetmek isteyip istemediğiniz sorulur.

### ![](/icons/autosave.webp) Otomatik Kaydet...
Otomatik kaydetme seçeneklerini kontrol etmek için menü.

Otomatik kaydetmeyi etkinleştirirseniz, düzenli aralıklarla bir açılır pencere görünecek şekilde bir zamanlayıcı ayarlayabilirsiniz.
Nomad'ın arka planda kaydetmemesinin nedeni, 3B dosyaların oldukça büyük olabilmesi ve bu nedenle siz yontarken belirgin bir gecikmeye neden olabilmesidir.

Ek olarak, bellek yetersizliği sorunlarından kaçınmak için sahne genellikle kaydetme işleminden önce sıkıştırılır.
Bu sıkıştırma/açma işlemi de kaydetme işlemini yavaşlatacaktır.

### Zamanlayıcı açılır penceresi
Zamanlayıcı açılır penceresinin ne sıklıkla görüneceği.

### Açılır pencere zaman aşımı
Açılır pencere zaman aşımını etkinleştir.

### Otomatik kaydı sil
Bir proje için otomatik kayıt dosyası varsa, orijinal proje yerine otomatik olarak o dosya yüklenir. Bu istenmiyorsa, bu düğme otomatik kaydı siler. Dosyayı yüklemek daha sonra projenin son manuel kaydını yükleyecektir.


## İçe Aktar

### ![](/icons/add_file.webp) İçe Aktar
Nomad projesi olmayan 3B dosyaları içe aktarmak için.

Harici bir sahne dosyasını Nomad'a aktardığınızda, onu *içe aktarabilir* veya *ekleyebilirsiniz*.

Bir dosyayı eklemek, nesneleri yalnızca mevcut sahneye ekler.
Bir dosyayı içe aktarmak, yeni nesnelerle birlikte yeni bir Nomad projesi oluşturur.

Nomad şu biçimleri içe aktarabilir:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, deneysel)

### ![](/icons/cog.webp) Gelişmiş
Gelişmiş içe aktarma seçeneklerini göster:

### Proje/ glTF / OBJ / STL / FBX
#### Topolojiyi koru
Nomad varsayılan olarak yükleme sırasında sorunlu geometrileri düzeltmeye çalışır. Bunu etkinleştirmek, Nomad'ın tepe/ yüz yeniden sıralamasını, tepe/ yüz kopyalarının kaldırılmasını, kullanılmayan tepelerin kaldırılmasını durdurur.

#### Dokuları atla
glTF gibi destekleyen biçimler için dokuların yüklenmesini atla.

### Proje / glTF
#### Arayüz ayarlarını koru
Nomad .nom veya glTF dosyası içinde arayüz ve proje ayarlarının kaydedilmesini etkinleştir.

### OBJ
#### OBJ'yi gruplara göre böl
OBJ gruplarının ayrı nesnelere bölünmesini etkinleştir.

#### Renk Uzayı
Obj'den yorumlanan renk modunu Linear, sRGB veya Auto olarak ayarla.

### PLY
#### Renk Uzayı
Ply'den yorumlanan renk modunu Linear, sRGB veya Auto olarak ayarla.


### FBX
#### Renk Uzayı
Obj'den yorumlanan renk modunu Linear, sRGB veya Auto olarak ayarla.



## Dışa Aktar
Diğer yazılımlarda kullanılabilecek bir 3B geometri biçimine kaydedin. 

![](/images/file_export.webp)

Farklı dosya biçimleri farklı özellikleri destekler, mevcut seçenekler seçilen dosya türüne göre değişecektir.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Tümü/Görünür/Seçili
Etkin düğme durumu hangi nesnelerin dışa aktarılacağını belirler. Simgelerin yanındaki sayı, o seçenek için kaç nesnenin dışa aktarılacağını gösterir.

### Vertex renkleri
Dosya biçimi destekliyorsa vertex renklerini dışa aktar.

### PBR Boyama
PBR vertex renkleri ikincil vertex renk öznitelikleri olarak dışa aktarılır.
Kanallar şu şekilde paketlenir:

|           | Kanal   |
| :-------: | :-----: |
| Pürüzlülük | R      |
| Metalik   | G       |
| Maskeleme | B       |


### Katmanlar
Katmanlar glTF morph hedefleri aracılığıyla desteklenir.
Nomad ayrıca katman başına renk, pürüzlülük ve metalik değerleri de dışa aktarır, ancak bu diğer yazılımlar tarafından yok sayılacaktır.

### Katman boyama
Katman boyamasını dışa aktar, genellikle diğer yazılımlar tarafından yok sayılır.

### Yüz Grubu
Yüz gruplarını dışa aktar, dışa aktarma bazen diğer yazılımlarla çakışabilir.

### Normaller
Normal bilgilerini dışa aktar. Nomad'ın diğer dosya biçimlerini içe aktarırken her zaman kendi normallerini hesaplayacağını unutmayın.

### Tanjantlar
Normal haritalar varsa kullanılan tanjant bilgilerini dışa aktar. 

### Dokular
Malzemeye dokular eklendiyse dışa aktarılırlar. Bunun dokuları fırınlamayacağını unutmayın, bu topoloji bölümündeki fırınlama seçenekleriyle yapılır.

### Dışa aktar düğmesi
Seçili ayarları kullanarak geometrinin dışa aktarılmasını başlatmak için buna tıklayın.

::: tip İpucu: Blender'a pürüzlülük ve metalik içe aktarma

Blender glTF/glb içe aktarabilir, ancak metalik ve pürüzlülük için vertex özniteliklerini otomatik olarak anlamaz. Bunları kullanmak için, malzeme düzenleyicisinde bir Vertex Color düğümü oluşturun, özelliğini bir sonraki renk özniteliğine ayarlayın (genellikle Col.001). Bir 'Separate XYZ' düğümü bağlayın, X'i pürüzlülüğe, Y'yi Metalik'e gönderin.

Bu video süreci gösterir:

![](/videos/blender_pbr.mp4)

::: 

::: tip İpucu: USD özellik desteği

USD karmaşık bir biçimdir, belirtimi birçok özelliği destekler, ancak tüm 3B yazılımlar bunların hepsini desteklemez. Örneğin OSX/iOS vertex rengi desteklemez. USD dışa aktarıcısı içindeki hazır ayar modları, OpenUSD, Apple, Procreate, Zbrush ile uyumluluk için en iyi tahmini yapmaya çalışır.

::: 

## Render

Projede bulunan tüm ayarların (ışıklar, malzemeler, son işlem vb.) birleşimi olan bir görüntü dışa aktarın. 

![](/images/file_render.webp)
### Önizleme

Menü başlığının yanındaki küçük önizleme düğmesi, son sonucu önizlemeye yardımcı olmak için araç çubuklarını karartır.

### Şeffaf arka plan
Render için alfa kanalını etkinleştirir, 2B programlarda render'ı diğer görüntülerle birleştirmek için kullanışlıdır. Kısmi saydamlığın desteklenmediğini unutmayın.

### Arayüzü göster
Render'a Nomad'ın arayüzünü dahil etmeyi etkinleştir.

### Render oranı
Görüntü çözünürlüğü üzerinde bir çarpan.

### Nihai boyut
Render için kullanılacak çözünürlük. `Custom` seçildiğinde, genişlik ve yükseklik kaydırıcıları etkinleştirilir. 

Dosya menüsü etkin olduğunda, render bölgesi ekran çözünürlüğüyle eşleşmiyorsa görünüm alanında kesikli bir kaplama çizilir (bunun doğru olması için yatay modda olmanız gerektiğini unutmayın).

### png dışa aktar
Render işlemini başlatmak için bu düğmeye tıklayın. Tamamlandığında, görüntüyü nasıl kaydedeceğinizi veya paylaşacağınızı seçebilirsiniz.

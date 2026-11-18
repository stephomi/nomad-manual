# ![](/icons/open.webp) Dosyalar {#files}

Dosyalar menüsü Nomad projelerini kaydetmenizi ve yüklemenizi, 3d modelleri içe ve dışa aktarmanızı, işlenmiş görüntüleri dışa aktarmanızı ve Nomad'ı başka uygulamalara bağlamanızı sağlar. Üç sekmesi vardır: `Dosyalar`, `İşle` ve `Bağlantı`.

![](/images/file_menu.webp)

## Proje {#project}
![](/images/file_project.webp)

En üstteki küçük resim geçerli projeyi gösterir; yanında dosya boyutu, otomatik kayıt ve kaydedilmiş geçmiş bilgisi yer alır. Projelerinizin küçük bir tarayıcısını açmak için küçük resme dokunun; ardından bir projeye dokunarak onu açmak, eklemek, üzerine yazmak, klonlamak, yeniden adlandırmak ya da silmek için bir menü açın.

Projede henüz kaydedilmemiş değişiklikler varsa küçük resmin altında `Kaydedilmemiş değişiklikler!` yazısı görünür.

### Alan {#scope}
Masaüstünde projelerinizin nereye kaydedileceğini seçin:
* `Dahili` - Varsayılan, mobildeki ile aynı. Projeler yalnızca ana Nomad klasörünün içine kaydedilir.
* `Yerinde` - Nomad klasörünün dışından bir proje açtığınızda, kaydetmek orijinal dosyanın üzerine yazar. Otomatik kayıt bu harici projelerde çalışmaz.

### ![](/icons/nomad.webp) Önayar {#preset}
Demolardan ve karakter parçalarından oluşan bir koleksiyona erişin. Birini seçin, ardından `Aç` ya da `Sahneye ekle` seçeneğini görmek için tekrar seçin. Bu tarayıcıdan Poly Haven'daki ücretsiz modelleri de indirebilirsiniz.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Geçmiş... {#history}
Projenin geçmiş seçeneklerine hızlı erişim sağlar; örneğin proje kaydedildiğinde geri alma geçmişinizi saklayan `Geçmişi kaydet` gibi. Düğmedeki yeşil rozet, geçmişin projeyle birlikte kaydedildiğini gösterir. Ayrıntılar için [Geçmiş](history.md#save-history) sayfasına bakın.

### ![](/icons/save.webp) Kaydet {#save}
Nomad projesini kaydeder. Proje daha önce hiç kaydedilmediyse sizden bir ad istenir.

### ![](/icons/save_as.webp) Farklı kaydet... {#save-as}
Projeyi yeni bir adla, yeni bir proje olarak kaydeder.

### ![](/icons/save_as.webp) Üzerine yaz... {#overwrite}
Geçerli sahneyi başka bir projenin üzerine kaydetmek için proje tarayıcısını açar. Sahnenin tamamı yerine yalnızca seçili nesneleri kaydetmek için `Sadece seçili nesneleri dâhil et` seçeneğini etkinleştirin. Tarayıcıda, bunun yerine yeni bir proje olarak kaydetmek için bir `Farklı kaydet...` düğmesi de bulunur.

### ![](/icons/pencil.webp) Yeniden Adlandır {#rename}
Geçerli projeyi yeniden adlandırmak için bir metin kutusu açar.

### ![](/icons/open.webp) Aç... {#open}
Bir proje açmak için proje tarayıcısını açar.

### ![](/icons/add_file.webp) Sahneye ekle... {#add}
Proje tarayıcısını açar; bir proje seçildiğinde içeriği geçerli sahneyle birleştirilir.

### ![](/icons/trash.webp) Sil... {#delete}
Proje tarayıcısını açar; seçilen projeler dosya sisteminden silinir.

### ![](/icons/new_file.webp) Yeni {#new}
Yeni bir proje başlatır; kaydedilmemiş değişiklikler varsa onaylamanız istenir. Onay penceresinde `Arka Plan`, `Ortam`, `MatCap` ve `X-Ray` ayarları için `Koru` ya da `Sıfırla` seçebilir, ayrıca yeni projenin `Geçmişi kaydet` kullanıp kullanmayacağını belirleyebilirsiniz.

### ![](/icons/autosave.webp) Otomatik Kaydet... {#auto-save}
Otomatik kayıt seçeneklerini kontrol eden menü. Projenizi düzenli aralıklarla ayrı bir dosyaya kaydetmek için `Otomatik Kaydet` seçeneğini etkinleştirin. Düğmedeki rozet açık olup olmadığını gösterir.

Nomad'ın arka planda kaydetmemesinin nedeni, 3d dosyaların oldukça büyük olabilmesi ve bu yüzden heykel yaparken ciddi bir takılmaya yol açabilmesidir.

Ayrıca bellek yetersizliği sorunlarını önlemek için sahne genellikle kaydetme işleminden önce sıkıştırılır.
Bu sıkıştırma/açma işlemi de kaydetmeyi yavaşlatır.

### Kayıt aralığı {#timer-pop-up}
Nomad'ın iki otomatik kayıt arasında kaç dakika beklediği.

### Geri sayımı göster {#popup-timeout}
Her otomatik kayıttan önce bir geri sayım gösterir; böylece bir işin ortasındaysanız kaydı iptal edebilirsiniz. Devre dışıyken Nomad, heykel yapmayı bıraktığınız anda kaydeder.

### ![](/icons/trash.webp) Otomatik kaydı sil {#discard-autosave}
Bir proje için otomatik kayıt dosyası varsa, orijinal proje yerine otomatik olarak o yüklenir. Bu istenmiyorsa, bu düğme otomatik kaydı siler. Dosyayı yüklediğinizde projenin son elle yapılmış kaydı yüklenir.

### ![](/icons/open.webp) Eski kaydı aç {#open-outdated-save}
Bir projenin hem otomatik hem de elle yapılmış bir kaydı varsa, bu düğme ikisinden eski olanı tarihiyle birlikte açar (`Eski otomatik kaydı aç` veya `Eski manuel kaydı aç`). En son kayıt istediğiniz kayıt değilse işinize yarar.

### ![](/icons/storage.webp) Son Silinenler... {#recently-deleted}
Nomad, proje klasöründen çıkan projelerin verilerini ve bir içe aktarmayla değiştirilen dosyaları, kalıcı olarak silmeden önce birkaç gün saklar. İçe aktarılamayan dosyalar siz silene kadar kalır. Bu liste onları boyutları ve tarihleriyle gösterir; böylece tek tek ya da `Tümünü sil` ile silebilirsiniz.

## İçe aktar {#import}

### ![](/icons/add_file.webp) İçe aktar {#import-button}
Nomad projesi olmayan 3d dosyaları içe aktarmak için.

Harici bir sahne dosyasını Nomad'a aktardığınızda onu *ekleyebilir* ya da onunla *yeni* bir proje başlatabilirsiniz.

Dosya eklemek, nesneleri yalnızca geçerli sahneye ekler.
`Yeni` seçeneği ise yeni nesneleri içeren yeni bir Nomad projesi oluşturur.

İçe aktarma penceresi seçtiğiniz her dosyayı kendi içe aktarma seçenekleriyle listeler. Görüntüler de bu yoldan içe aktarılabilir: her biri için `HDRI`, `MatCap`, `Referans`, `Alfa`, `Dokular` ya da `VDM` olacağını seçin.

Nomad şu formatları içe aktarabilir:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), destekleyen platformlarda

### ![](/icons/cog.webp) Ayarlar {#advanced}
Proje küçük resminin yanındaki `Ayarlar...` düğmesi ana içe aktarma seçeneklerini gösterir. Bu ayarlar kaydedilmez; içe aktarma penceresi, içe aktardığınız dosyalar için geçerli olan seçenekleri gösterir.

### Tüm formatlar {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Topolojiyi koru {#keep-topology}
Nomad varsayılan olarak yükleme sırasında sorunlu geometriyi düzeltmeye çalışır. Bunu etkinleştirmek, Nomad'ın verteksleri/yüzleri yeniden sıralamasını, kopyaları birleştirmesini ve kullanılmayan verteksleri kaldırmasını engeller.

::: warning
`Topolojiyi koru` açıkken Boolean, Birleştir, Azalt veya Manifold gibi işlemler yinelenen verteksleri birleştirmeyebilir.
:::

#### ![](/icons/image.webp) Dokuları atla {#skip-textures}
glTF gibi bunu destekleyen formatlarda dosyaya gömülü dokuları yüklemez.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Arayüz ayarlarını yükle {#keep-gui-settings}
Bir proje dosyasını açarken ya da içe aktarırken, içine kaydedilmiş tüm arayüz ayarlarını yükler.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) OBJ'leri gruplara ayır {#split-obj-by-groups}
OBJ gruplarını ayrı nesnelere böler.

#### ![](/icons/vertex.webp) Yinelenen konumları birleştir {#merge-duplicate-positions}
Aynı konumu paylaşan verteksleri birleştirir.

#### ![](/icons/uv.webp) Yinelenen UV'leri birleştir {#merge-duplicate-uvs}
Aynı UV'yi paylaşan doku koordinatlarını birleştirir.

#### ![](/icons/paint.webp) Renk Alanı {#color-space}
Dosyadan okunan renk kipini `Otomatik`, `Doğrusal` ya da `sRGB` olarak ayarlar. Renkler yanlış görünüyorsa bu seçeneği değiştirmeyi deneyin.

#### ![](/icons/image.webp) Format {#normal-format}
Dokulardaki normal haritasının formatı: `Otomatik`, `OpenGL (+Y)` ya da `DirectX (-Y)`. Normal haritasının ayrıntıları ters görünüyorsa diğerini deneyin.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Renk Alanı {#color-space-ply}
Dosyadan okunan renk kipini `Otomatik`, `Doğrusal` ya da `sRGB` olarak ayarlar.


### FBX {#fbx}
#### ![](/icons/uv.webp) Yinelenen UV'leri birleştir {#merge-duplicate-uvs-fbx}
Aynı UV'yi paylaşan doku koordinatlarını birleştirir.

#### ![](/icons/paint.webp) Renk Alanı {#color-space-fbx}
Dosyadan okunan renk kipini `Otomatik`, `Doğrusal` ya da `sRGB` olarak ayarlar.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Dokulardaki normal haritasının formatı: `Otomatik`, `OpenGL (+Y)` ya da `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Renk Alanı {#color-space-usd}
Dosyadan okunan renk kipini `Otomatik`, `Doğrusal` ya da `sRGB` olarak ayarlar.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Dokulardaki normal haritasının formatı: `Otomatik`, `OpenGL (+Y)` ya da `DirectX (-Y)`.



## Dışa Aktar {#export}
Diğer yazılımlarda kullanılabilecek bir 3d geometri formatına kaydeder. 

![](/images/file_export.webp)

Farklı dosya formatları farklı özellikleri destekler; kullanılabilen seçenekler seçilen dosya türüne göre değişir.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Verteks renkleri](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Verteks PBR](#pbr-paint)        | ✅     | Nomad ✅<br>Diğer ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Dörtgen (quad)                            | ✅     | Nomad ✅<br>Diğer ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Katmanlar](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Nesneler                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Yüz Grubu                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hiyerarşi                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Işıklar                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Dokular                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitifler, Süreç sonrası işlemler vb.    | ✅     | Nomad ✅<br>Diğer ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Dışa aktarma düğmesi {#export-button}
Geometriyi seçili ayarlarla dışa aktarmak için buna tıklayın. Düğme seçili formatı ve tahmini dosya boyutunu gösterir. Android'de yanındaki `Paylaş` düğmesi dosyayı doğrudan başka bir uygulamaya gönderir.

### Dosya formatı {#file-format}
Dışa aktarılacak formatı seçin: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` ya da `USD`. NOMAD, Nomad'ın kendi formatıdır; başka yazılımlarda açılmaz, bu yüzden çoğunlukla Nomad'a yeniden aktarmak içindir.

### Dâhil et {#allvisibleselected}
Hangi nesnelerin dışa aktarılacağını seçin: `Tümü`, `Görülebilir` ya da `Seçilen`. Her seçeneğin yanındaki sayı kaç nesnenin dışa aktarılacağını gösterir.

### Her nesne için bir dosya {#one-file-per-object}
Her nesneyi kendi dosyasına aktarır. Sayı kaç dosya yazılacağını gösterir.

### Tür {#type}
Dışa aktarma birkaç dosya yazdığında (nesne başına bir dosya ya da dokulu OBJ), bunları bir `Klasör` ya da bir `Zip` içine kaydeder. Bazı uygulamalar (Google Drive, One Drive vb.) klasör içe aktarmayı desteklemez, bu durumda Zip kullanabilirsiniz.

### Geçmişi göm {#embed-history}
Yalnızca NOMAD. Geri alma geçmişini dosyanın içine ekler; dosya Nomad'da açıldığında geri yüklenir. Dosya boyutunu artırır ve sahnenin tamamının tek bir dosya olarak dışa aktarılmasını gerektirir.

### Varlıkları göm {#embed-assets}
Yalnızca NOMAD. Kendi matcap'lerinizi, ortamlarınızı ve yazı tiplerinizi dosyaya ekler. Yerleşik varlıklar gömülmez.

### Verteks renkleri {#vertex-colors}
Dosya formatı destekliyorsa verteks renklerini dışa aktarır. Bazı 3d yazılımlar bunları okuyabilir, ama hepsi değil.

OBJ için şunları seçebilirsiniz:
* `Yok` - Renk yok.
* `RGB` - Renkler verteks bilgilerinin sonuna eklenir.
* `MRGB (ZBrush)` - Rengi kodlamanın başka bir yolu; maske verisini de destekler.

### Renk Alanı {#color-space-export}
Yalnızca OBJ, `RGB` verteks renkleriyle. Renkleri `Doğrusal` ya da `sRGB` olarak yazar.

### PBR boyaması {#pbr-paint}
Pürüzlülük, metaliklik ve maske boyamasını dışa aktarır. Diğer yazılımlar bu veriyi yok sayabilir.
PBR verteks renkleri ikincil verteks rengi öznitelikleri olarak dışa aktarılır.
Kanallar şu şekilde paketlenir:

|           | Kanal  |
| :-------: | :------: |
| Pürüzlülük | R        |
| Metaliklik | G        |
| Maskeleme   | B        |


### Katmanlar {#layers}
Katmanlar glTF morph target'ları aracılığıyla desteklenir. Bu glTF tarafından resmi olarak desteklenir, bu yüzden diğer yazılımlarda da çalışması gerekir.
Nomad katman başına renkleri, pürüzlülüğü ve metalikliği de dışa aktarır, ancak diğer yazılımlar bunları yok sayar.

### Katman boyaması {#layer-painting}
Katman boyamasını dışa aktarır; genellikle diğer yazılımlar tarafından yok sayılır.

### Yüz Grubu {#face-group}
Yüz gruplarını dışa aktarır; bu bazen diğer yazılımlarda sorunlara yol açabilir.

### Nesneleri Yaz {#write-objects}
Yalnızca OBJ. Nesneleri ayrı tutar. Her şeyi tek bir nesne olarak dışa aktarmak için devre dışı bırakın; örneğin Substance Painter'ın 'Mesh ID / Polygroup' özelliğini kullanmak için.

### Normaller {#normals}
Normal bilgisini dışa aktarır. Nomad'ın diğer dosya formatlarını içe aktarırken normalleri her zaman kendisinin hesapladığını unutmayın.

### Teğetler {#tangents}
Teğet bilgisini dışa aktarır; model normal haritaları içeriyorsa kullanılır. 

### Dokular {#textures}
Malzemeye doku eklenmişse dışa aktarılırlar. Bunun doku pişirmediğini unutmayın; pişirme, topolojideki pişirme seçenekleriyle yapılır.

### Format {#fbx-format}
Yalnızca FBX. `İkili` daha küçüktür ama her uygulamada çalışmayabilir, `ASCII` ise bir metin dosyasıdır.

### Sıkıştırılmış {#compressed}
Yalnızca FBX. Dışa ve içe aktarmayı yavaşlatma pahasına dosya boyutunu küçültür.

### Önayar {#usd-preset}
Yalnızca USD. Hangi uygulama için dışa aktardığınızı seçin: `OpenUSD`, `Apple`, `Procreate` ya da `Zbrush`. Bazı seçenekler yalnızca bazı önayarlarda kullanılabilir.

### Örnek {#instance}
Yalnızca USD. Örneklenmiş nesneleri, geometrilerini çoğaltmak yerine örnek (instance) olarak dışa aktarır.

### Kaymayı İzin Ver {#allow-skew}
Yalnızca USD. Matris dönüşümlerinde kaymaya (skew) izin verir. Devre dışıyken Nomad, kaymalı dönüşümleri ayrı ölçekleme ve döndürme dönüşümlerine böler.

### Tekrarlayıcı {#repeater}
Yalnızca USD. Tekrarlayıcıların oluşturduğu kopyaları örnek olarak dışa aktarır.

### Kopyaları birleştir {#join-copies}
Her nesne ve tekrarlayıcı kopyaları tek bir nesne haline gelir.

::: tip İpucu: Pürüzlülük ve metalikliği Blender'a aktarmak

Blender glTF/glb içe aktarabilir, ama metaliklik ve pürüzlülük için verteks özniteliklerini kendiliğinden anlamaz. Bunları kullanmak için malzeme düzenleyicide bir Vertex Color düğümü oluşturun ve özelliğini bir sonraki renk özniteliğine ayarlayın (genellikle Col.001). Bir 'Separate XYZ' düğümü bağlayın, X'i roughness'a, Y'yi Metallic'e gönderin.

Bu video süreci gösteriyor:

![](/videos/blender_pbr.mp4)

::: 

::: tip İpucu: USD özellik desteği

USD karmaşık bir formattır; belirtimi birçok özelliği destekler, ama her 3d yazılım hepsini desteklemez. Örneğin OSX/iOS verteks rengini desteklemez. USD dışa aktarıcısındaki önayar kipleri OpenUSD, Apple, Procreate ve Zbrush ile uyumluluk için en iyi tahmini yapmaya çalışır.

::: 

## ![](/icons/screen.webp) İşle {#render}

Projedeki tüm ayarların (ışıklar, malzemeler, süreç sonrası işlemler vb.) birleşiminden oluşan bir görüntüyü dışa aktarır. 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Önizleme {#preview}

Menü başlığının yanındaki `Önizleme` düğmesi, son sonucun kadrajını önizlemenize yardımcı olmak için arayüzü saydam yapar.

### ![](/icons/home.webp) Odak {#focus}
Sahneyi ya da seçimi işleme boyutuna sığacak şekilde kadrajlar. İkisi arasında geçiş yapmak için tekrar dokunun.

### ![](/icons/map.webp) Yükseklik haritası {#heightmap}
Sahneyi kameradan görüldüğü haliyle gri tonlamalı bir yükseklik haritası olarak işler; en yakın kısımlar en parlak olanlardır. Etkinleştirildiğinde `Kare` boyuta geçer ve seçimi kadrajlar. Görünüm alanındaki küçük bir çubuk, geçişin `Odak` değerini ayarlamanızı sağlar.

`Yükseklik haritası` açıkken dışa aktarma düğmesinin yanında bir `Alfa olarak kaydet` düğmesi belirir; işlemeyi bir dosya olarak dışa aktarmak yerine yeni bir fırça alfası olarak kaydetmek için.

### ![](/icons/opacity.webp) Şeffaf arkaplan {#transparent-background}
İşleme için bir alfa kanalı etkinleştirir; işlemeyi 2d programlarda başka görüntülerle birleştirmek için kullanışlıdır. Kısmi saydamlığın desteklenmediğini unutmayın.

### ![](/icons/sliders.webp) Arayüzü göster {#show-interface}
Nomad'ın arayüzünü işlemeye dâhil eder.

### Son boyut {#final-size}
İşleme için kullanılacak çözünürlük: `Ekran`, `720`, `1080`, `4096`, `Kare` ya da `Özel`.

Dosyalar menüsü etkinken, ekran çözünürlüğüyle eşleşmiyorsa işleme bölgesini belirtmek için görünüm alanına kesikli bir çerçeve çizilir.

### Genişlik / Yükseklik {#render-ratio}
`Özel` ile görüntünün genişliğini ve yüksekliğini ayarlayın. İki kaydırıcının arasındaki bağlantı düğmesi, birini değiştirdiğinizde oranı korur. `Kare` ile yalnızca genişlik ayarlanabilir.

### ![](/icons/export.webp) Dışa Aktar → PNG {#export-png}
İşleme sürecini başlatmak için bu düğmeye tıklayın. Tamamlandığında görüntüyü nasıl kaydedeceğinizi ya da paylaşacağınızı seçebilirsiniz. Çok büyük boyutlar önce onay ister: cihazınızın belleği yetmeyebileceği için önce projenizi kaydedin.

## ![](/icons/network.webp) Bağlantı {#link}

Nesne gönderip almak ya da düzenlemelerinizi canlı olarak eşitlemek için Nomad'ı başka bir cihaza veya uygulamaya bağlayın. Bir cihaz oturumu barındırır, diğerleri ona katılır.

### GoZ’yi etkinleştir {#enable-goz}
Yalnızca masaüstü. Bu bilgisayardaki ZBrush ile ağ örgüsü alışverişi yapar. `Gönder` ağ örgülerini ZBrush'a aktarır, `Al` çalışan ZBrush'tan içe aktarır: `Seçim` etkin alt aracı (subtool), `Sahne` tüm alt araçları alır. ZBrush'ta istediğiniz zaman GoZ'ye de basabilirsiniz.

### Mod {#link-mode}
* `Kapalı` - Bağlantı yok.
* `Ana makine` - Bu cihaz oturumu barındırır ve diğerlerinin katılmasını bekler.
* `Katıl` - Yakındaki cihazları arar; katılmak için ana makinenin adına dokunun.

İki Nomad'ı bağlamak için bir cihazda `Ana makine`, diğerlerinde `Katıl` seçin. Blender'a bağlanmak için Nomad ana makine olmalıdır: `Bağlantı` başlığının yanındaki yardım düğmesi, Nomad Blender Link eklentisinin nasıl kurulacağını gösterir.

### ![](/icons/network.webp) Ağ bağlantı noktası {#network-port}
Bağlantının kullandığı ağ bağlantı noktası. Yalnızca başka bir uygulama onu zaten kullanıyorsa değiştirin.

### Gönder / Al {#send-get}
Bağlandıktan sonra `Seçim` ya da tüm `Sahne` öğesini diğer cihaza `Gönder` veya ondan `Al`. `Değiştir` geçerli sahneyi siler, ardından diğer cihazın sahnesini alır.

### ![](/icons/link.webp) Canlı eşitleme {#live-sync}
Siz çalışırken düzenlemelerinizi diğer cihaza aktarır. `Çalışma görünümü` kamerayı da eşitler. `Sahne düzenlemeleri` düzenlemeleri hangi cihazın göndereceğini belirler: `Otomatik`, yönü en son etkinliğe göre belirler. Ardından nelerin eşitleneceğini seçin: `Nesneler ve geometri`, `Malzemeler`, `Işıklar`, `Kameralar` ve diğer taraf destekliyorsa `Gölgelendirme` ile `Süreç sonrası işlemler`.

::: tip
Var olan nesnelerin, canlı eşitlemenin onları güncelleyebilmesi için önce bir kez `Gönder` ya da `Al` ile bağlanması gerekir.
:::

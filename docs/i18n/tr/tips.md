# ![](/icons/manual.webp) İpuçları {#tips}

[[toc]]

## Bir modele nasıl başlanır {#how-to-start-a-model}

3d heykelde yeni başlayanlar, bir modele başlamanın en iyi yolunun hangisi olduğunu sık sık sorar. En iyi yol diye bir şey yoktur, herkesin tercihi farklıdır. İşte en yaygın yaklaşımlardan bazıları.

### Küre üzerinde heykel, çoklu çözünürlük {#sculpt-on-sphere-multires}

Nomad açıldığında gelen varsayılan model, en yaygın başlangıç yoludur. Küreyi itip çekerek şekil vermek için taşıma, kil ve oluk araçlarını kullanın; büyük değişiklikleri hızlıca yapmak istediğinizde düşük alt bölüm seviyelerini, ayrıntı çalışması için yüksek alt bölüm seviyelerini kullanın.

Sık karşılaşılan bir sorun, poligonların ihtiyaç duyduğunuz yerde yetmemesi, başka yerlerde ise fazla olmasıdır. Örneğin varsayılan küreyi itip çekerek tam bir vücut yaparsanız, büyük olasılıkla parmaklar için yeterli ayrıntınız olmaz, kafanın arkasında ise boşa giden bir sürü poligon olur. Ancak kafa gibi çoğunlukla küresel şekiller için bu sorun olmayabilir.

### Dinamik topoloji {#dyntopo}

Dinamik topolojiyi etkinleştirmek, siz heykel yaptıkça poligonları uyarlamalı olarak ekler ve kaldırır. Bu poligonlar üçgendir ve yeni başlayanlar, çoklu çözünürlüğün temiz görünümüne kıyasla bu dağınık düzeni çoğu zaman sevmez. Ama vazgeçmemeye değer! Yumuşak gölgelendirmeyi açar, tel kafesi kapatır ve düzeni dert etmeyi bırakırsanız, bu kip gerçek bir kil hissi verebilir. Unutmayın, büyük bir fırça ya da pürüzsüzleştirme fırçası kullanırsanız bu kip poligonları kaldırabilir de; böylece araç her zaman hızlı ve akıcı hissettirir. Heykelin ilk geçişini bitirdikten sonra onu klonlayabilir, düzgün bir düzen elde etmek için Quad Remesher'dan geçirebilir ve orijinal ayrıntıları yüksek bir alt bölüm seviyesine yeniden yansıtabilirsiniz.

### Voksel yeniden ağ örgülendirme {#voxel-remesh}

Voksel yeniden ağ örgülendirme, heykelinize çoğunlukla dörtgenlerden oluşan bir topoloji uygular. Düşük çözünürlüklerde hızlı bir işlemdir; gerilmiş ya da aşırı yoğun poligonları hızla eşit aralıklı bir düzenle değiştirmek için kullanılabilir. Bir küreden tam bir vücuda başlamanın harika bir yolu olabilir: diyelim ki bir kafayla başladınız; bir boyun uzatın, voksel yeniden ağ örgülendirin. Bir gövde uzatın, voksel yeniden ağ örgülendirin, kollar, voksel yeniden ağ örgülendirin ve temel formlar oluşana kadar böyle devam edin.

### Birden fazla nesne kullanın {#use-multiple-objects}

Birçok anatomi kılavuzu vücudu basit kürelerden, silindirlerden ve küplerden oluşturarak gösterir. Nomad'da da bu şekilde heykel yapabilirsiniz. Bunun avantajı, nesneleri sahne hiyerarşisinde birbirine bağlayabilmenizdir; örneğin boynu döndürdüğünüzde kafa da onu izler. Hassas taşıma/döndürme/ölçekleme için gizmo aracını kullanabilmek de çok faydalıdır ve her şekil için eksen noktası ayarlayarak tam beklediğiniz gibi hareket etmelerini sağlayabilirsiniz. Temel bloklar doğru yerdeyken hepsini seçip daha ayrıntılı heykel için voksel yeniden ağ örgülendirme ya da boolean ile tek bir yüzeyde birleştirebilirsiniz.

Bu çalışma şekli için kullanışlı bir ipucu: bir küreyle başlayın, onu uzun bir sosis gibi ölçekleyin, eksen düğmesine basın, 'alt' seçeneğine tıklayın, eksen düğmesine yeniden basın. Artık klonlanabilen bir vücut parçanız var: ilk kürenin uzunluğu boyunca taşıyın, klonlayın, döndürün, klonlayın, kaydırın, klonlayın vb. ve böylece hızla bir vücut düzeni oluşturun.

### Tüpler {#tubes}

Tüp aracı bir heykele başlamanın harika bir yoludur. Sürüngen kuyrukları, kollar, bacaklar, parmaklar, kaşlar; hepsi tüp aracıyla hızla taslak olarak çizilip sonradan kolayca düzenlenebilir. Kesit profilini değiştirmenize de olanak tanır, bu da hızlı şekil değişiklikleri sağlar. Üzerinde heykel yapmaya başlamak için şekli onaylayabilir ve tam bir vücut ağ örgüsü elde etmek için diğer nesnelerle birlikte voksel yeniden ağ örgülendirebilirsiniz.

### Başka uygulamalar kullanın {#use-other-apps}

Bazı kişiler bir modele başka uygulamalarda başlamayı tercih eder, bu da gayet iyi. Blender ya da Valence gibi araçlar modellere düşük poligonlu tekniklerle başlamanızı sağlar; modeller daha sonra heykel için Nomad'a aktarılabilir.

### Yerleşik önayarları kullanın {#use-the-built-in-presets}

[Dosyalar](files.md) menüsünde, proje bölümünün solundaki `Önayar…` düğmesine tıklayın. Burada Blender Foundation'dan birkaç kafa ve vücut şekli önayarı bulacaksınız. Beğendiğiniz birini seçin, yeniden dokunun ve sahnenize ekleyin. 

### Çevrimiçi modeller kullanın {#use-online-models}

İnternette polyhaven, sketchfab, turbosquid gibi sitelerde birçok ücretsiz model bulunur. Bu modeller genellikle Nomad'a aktarılabilir ve doğrudan üzerinde heykel yapılabilir ya da referans olarak kullanılabilir.

### Kural yok! {#no-rules}

Sonuçta bu tekniklerin istediğiniz bir birleşimini kullanabilir ya da hiçbirini kullanmayabilirsiniz! Nomad bu açıdan çok esnektir; ileri düzey kullanıcılar tüplerle başlayıp ardından dinamik topoloji kullanabilir, sonra indirilmiş bir ayakla birleştirebilir, ardından hepsini Quad Remesher'dan geçirip son ayrıntılar için çoklu çözünürlük kullanabilir. Sizin için ne işe yarıyorsa.

## Yüz grupları {#facegroups}

Yüz grubu aracı birçok şey için kullanılabilir; bu YouTube videosunda anlatıldığı gibi: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Aşağıda o videoda ele alınan özelliklerin yazılı bir özeti yer alıyor.

### Neden yüz grupları? {#why-facegroups}

Yüz grupları yüzleri düzenlemenizi ve seçmenizi sağlar (bu kılavuzda 'yüz' ve 'poligon' aynı anlamda kullanılır). Bunu Nomad'ın diğer seçim ve düzenleme araçlarıyla karşılaştırarak anlatmak daha kolay. Nomad nesne oluşturmanıza, onları adlandırmanıza ve birbirine bağlamanıza olanak tanır; zemin, duvarlar, sandalye, masa vb.'den oluşan bir odayı tanımlamak için bir nesne yapısı kurmak kolaydır.

Bir karakter için ilk kaba şekillendirmeyi kafa, kol, bacak için ayrı nesneler kullanarak yapabilirsiniz; ama tüm parçaları tek bir ağ örgüsünde birleştirdiğinizde bu yapı kaybolur. Bir karakterin alt bölümleri üzerinde maskelerle çalışabilirsiniz, ancak önce eller, sonra burun, sonra yine eller için tekrar tekrar maske boyamak yorucu olabilir.

İşte yüz grupları burada işe yarar. Poligon yüzlerini bir renkle etiketlemenizi ve sonra aynı renge sahip poligonları seçip üzerlerinde işlem yapabilmenizi sağlar. Yüz grubu rengi ile verteks renginin farklı şeyler olduğunu unutmayın.

En yakın benzetme, bir haritayı renklerle boyayıp daha sonra ülkeleri ya da bölgeleri renklerine göre seçebilmektir.

Karakter kafaları için göz çukurlarını, burnu, dudakları, çeneyi, kulakları işaretleyen bölgeler boyayabilir, sonra bu bölgeleri kolayca seçebilirsiniz. Sert yüzey ve mekanik heykelde paneller ve bölümler tanımlamak için kullanışlı olabilir.

### Yüz grupları oluşturma ve düzenleme {#creating-and-editing-facegroups}

Yüz grupları, her yeni darbenin yeni bir yüz grubu oluşturduğu bir fırçayla uygulanabilir ya da imlecin altındaki yüz grubunu seçip genişletebilirsiniz. Şekiller kullanılarak da oluşturulabilirler.

* Nokta, varsayılan kip - tek bir sürükleme yeni bir yüz grubu rengi tanımlar ve onu üzerinden geçtiğiniz yüzlere atar. Her yeni sürükleme yeni bir yüz grubu tanımlar. Bir dokunuş, yeni bir yüz grubuyla dolgu yapar.
* Nokta, `Seç` kipi - sol araç çubuğundaki `Seç` düğmesi etkinken Nomad imlecin altındaki yüz grubunu seçer ve sürüklemenin geri kalanında onu uygular. Yüz gruplarını elle seçmek zorunda kalmadan onları iyileştirmek için kullanışlıdır.

### Maskeleme {#masking}

Maske aracı etkinken ve araç çubuğundaki yüz grubu düğmesi açıkken, bir yüz grubuna dokunmak onu maskeler.


### Gizleme {#hiding}

Gizleme aracı etkinken ve araç çubuğundaki yüz grubu düğmesi açıkken, bir yüz grubuna dokunmak onu gizler.

### Düzenleme {#organizing}

Daha önce de belirtildiği gibi yüz grupları, ayrı nesneler oluşturmanızı gerektirmeden ağ örgünüzü düzenlemek için kullanılabilir. Bir kafayı burun, çene, kulaklar için ayrı nesnelere bölmek istemeyebilirsiniz, ama bunların yüz gruplarıyla tanımlanmış olması çok işe yarar.

### UV bölgeleri {#uv-regions}

UV Atlas aracı dikişleri otomatik olarak tanımlamaya çalışır, ancak bazen dikişleri istemediğiniz yerlere koyar. Bir nesnede yüz grupları varsa ve UV Atlas seçeneklerinde yüz grubu seçeneği etkinse, bunun yerine yüz grubu sınırlarını UV dikişleri olarak kullanır.

### Quad Remesher {#quad-remesher}

Quad Remesher eklentisi genellikle modelinizde kenarları güzelce akıtır, ama yüz grubu seçeneği etkinken onu yönlendirmeye yardımcı olmak için yüz gruplarını kullanabilirsiniz. Bu, örneğin gözlerin, kaş çıkıntısının, dudakların ya da yanak kıvrımının çevresinde temiz bir kenar akışı tanımlamayı kolaylaştırır.

### Diğer araçlarla filtreleme {#filter-with-other-tools}

Birçok aracın, ya kendi ana araç menüsünde ya da Darbe -> Filtre menüsünde, yüz gruplarını dikkate alan seçenekleri vardır. Örneğin pürüzsüzleştirme aracı %100'ün üzerindeki güçlerde bir yüz grubunun içindeki ayrıntıyı agresif biçimde yumuşatabilir, ama yüz grubu sınırını görece sağlam bırakır.

### Yüz grubu sınırlarını rahatlatma ve yumuşatma {#relax-and-smooth-facegroup-borders}

Yüz grubu aracındaki `Rahatlat` seçeneği, diğer özellikleri koruyarak yüz grubu sınırlarını yumuşatmakta harika iş çıkarır. Quad remesh işleminden önce düzgün yüz grubu sınır bölgeleri tanımlamanın harika bir yolu olabilir.

## Tablet/mobildeki sınırlamalar {#limitations-on-tabletmobile}

Günümüzün tabletleri ve telefonları çok güçlüdür, ancak masaüstü bilgisayarlardan ve dizüstülerden önemli farkları vardır:

### Aktif soğutma yok {#no-active-cooling}

Bilgisayarlarda onları serin tutan fanlar ve/veya büyük soğutucular bulunur ve yüksek sıcaklıklarda çalışacak şekilde tasarlanırlar. Mobil donanım ise genellikle iç bileşenleri serin tutmaya yardımcı olmaktan çok incelik öncelikli tasarlanır. Nomad en yüksek kalite ayarlarına zorlanırsa (PBR aydınlatma kipi, karmaşık malzemeler, çok sayıda nesne, birçok süreç sonrası işlem seçeneği açık), hem cihaz aşırı ısınabilir hem de pil çok hızlı tükenebilir. 

Daha iyi bir yaklaşım, matcap aydınlatma kipini ve daha düşük bir `İşleme Çözünürlüğü` (süreç sonrası işlemler menüsünün en üstünde) kullanmaktır. Bu seçimler cihazı serin tutar ve daha uzun süre heykel yapmanızı sağlar.

### Sınırlı bellek {#limited-memory}

Nomad çoğu masaüstü heykel uygulamasına eşit sonuçlar elde edebilir, ama fizik kurallarını eğip bükemez! Masaüstü bilgisayarların çoğunda mobil cihazların iki katı bellek bulunur; 3d animasyon için yapılmış iş istasyonlarında çoğu zaman 4 ya da 8 katı vardır. Bu yüzden kaç poligon kullandığınızın farkında olmak iyidir; cihazınızda ne zaman takılmaya başladığını görmek için birkaç test yapın. Nomad'ı çalıştırabilen neredeyse tüm cihazlar 1 milyon poligonu rahatlıkla kaldırabilir. M2 iPad Pro 8 milyonu rahatça kaldırabilir; kullanıcılar en yeni iPad'leri bunun çok üzerinde test etti.

Bununla birlikte, yalnızca en ayrıntılı heykeller 4 milyondan fazla poligona ihtiyaç duyar; görece basit nesneler yapıyorsanız ve sık sık 500.000, 1 milyon, 4 milyonu aştığınızı görüyorsanız, çok fazla poligon kullanıyorsunuz demektir! [Ayarlar](settings.md) bölümünde `Yumuşak gölgelendirme` seçeneğinin etkin olduğundan emin olun.

### İşletim sistemi yoğun uygulamalara karşı daha az hoşgörülüdür {#os-is-less-forgiving-with-intensive-apps}

Apple ve Android, uygulamaların küçük dosyaları çok hızlı kaydedip yüklemesini bekler. Ayrıca uygulamaların çok hızlı geçiş yapabileceğini varsayar. Nomad dosya boyutlarını görece küçük tutmak ve onları çok hızlı kaydetmek için bazı akıllıca yöntemler kullanır; ama mobil işletim sistemi Nomad'ın çok uzun sürdüğüne karar verirse, işini bitirmesini beklemeden onu kapatır. Bu da dosyaları küçük tutmak için bir başka neden; bir kullanıcının Discord'da bildirdiği gibi 37 milyon poligonluk heykellerle çalışmak mümkün, ama önerilmez!

## Küçük ekranlarda çalışmak {#working-on-small-screens}

Nomad tabletler için tasarlanmıştır, ama telefonlarda da iyi çalışır. Telefon gibi küçük bir ekranda heykel yapmak, arayüzde ve çalışma şeklinizde birkaç ince ayarla kolaylaşabilir:

* 4 parmakla dokunmak tüm arayüzü açıp kapatır ve heykel için size daha fazla yer bırakır.
* 3 parmakla yukarı ve aşağı sürüklemek fırça yarıçapını değiştirir
* Gözleriniz iyiyse daha fazla düğme sığdırmak için arayüz ölçeği küçültülebilir, iyi değilse büyütülebilir!
* Geniş menüler bazen heykelin önüne geçebilir; menünün altındaki heykeli görebilmek için onları saydam ve bulanıklaştırmasız yapabilirsiniz.
* Parmakla heykel yapıyorsanız, fırça merkezini parmağınızdan biraz uzaklaştırmak için [`Darbe kaydırma`](stroke.md#stroke-offset) seçeneğini kullanın.
* Bu ve daha birçok seçeneği [Arayüz menüsünde](./interface.md) bulabilirsiniz. 


## Şişirme ya da tepe deformörü {#inflate-or-peak-deformer}

Birçok 3d uygulamada, tüm verteksleri normalleri boyunca ayarlanabilir bir miktarda iten bir şişirme deformörü bulunur. Nomad'da şu an deformör olmasa da bu davranışı şişirme fırçasıyla taklit etmek mümkündür:

* Şişirme fırçasını seçin
* [Darbe menüsünden](./stroke.md#stroke) darbe yöntemini `Yakala • dinamik yarıçap` olarak değiştirin
* Fırça yarıçapını heykelinizden büyük yapın; gerekirse kamerayı heykelden uzaklaştırın.
* Nesnenizin yüzeyine tıklayıp bir darbe sürükleyin; yarıçap nesneden büyük olduğunda şeklin tamamı sabit bir miktarda eşit olarak şişer.
* Şişirme miktarını kontrol etmek için fırça yoğunluğunu ayarlayın
* Gerekirse belirli bölgelerde şişirme etkisini engellemek ya da azaltmak için maskeleme kullanın.

## Voksel yeniden ağ örgülendirme sonrasındaki yumruları ya da 'sivilceleri' giderme {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voksel yeniden ağ örgülendirme eşit aralıklı poligonlar oluşturmak için harikadır, ama bazen pürüzsüzleştirildiğinde küçük yumrulara ya da sivilcelere yol açan bir topoloji oluşturur. Örneğin:

* Varsayılan kürede oluk fırçasını kullanıp bir girdap çizin
* `Çoklu çözünürlük oluştur` değeri 3 iken voksel yeniden ağ örgülendirin
* Yüksek yoğunlukla pürüzsüzleştirin
* bozukluklar belirir (yüksek kontrastlı bir matcap malzemesiyle daha kolay görülür):

![](/videos/tip_pimples_before.mp4)

Heykel yaparak düzeltmek için pürüzsüzleştirme ayarlarındaki `Stabil düzleştirme` seçeneğini deneyin. Voksel yeniden ağ örgülendirmenin düzensiz topoloji düzeniyle başa çıkabilir ve temiz sonuçlar verir.

![](/videos/tip_pimples_stable_smooth.mp4)

Topolojinin kendisini düzeltmek için yeni bir primitif, quad remesh araçları ya da harici bir 3d modelleme programı kullanın ve orijinal ağ örgüsündeki ayrıntıyı `Topoloji -> Pişir -> Tekrar Projelendir → Verteks` ile yenisine yansıtın. 

![](/videos/tip_pimples_reproject.mp4)

## Gün ışığı aydınlatması {#daylight-lighting}

Varsayılan PBR işlemesi, adından da anlaşılacağı gibi fiziksel tabanlıdır; işlenmemiş bir dijital fotoğraf gibi biraz soluk ve düz görünebilir. Nomad'ın ışıkları ve süreç sonrası işlemleri, işlemelerin daha canlı görünmesini sağlamak için kullanılabilir.

İşte varsayılan bir işleme, bakalım daha iyi gösterebilecek miyiz:
![](/images/tips_lighting_default.webp)

Süreç sonrası işlemleri ve ton eşleştirmeyi etkinleştirmek parlaklık ve kontrast katabilir:

![](/images/tips_lighting_tonemap.webp)

Işıklara gelirsek, varsayılan ortam ışığı heykel için iyidir, ama son bir işleme için geliştirilebilir. Bunu düşünmenin bir yolu, doğrudan ışığı (örneğin güneş) ortam ışığından (örneğin gökyüzünün mavisinden ve yerden gelen ışık) ayırmaktır. Ortam ışığını azaltıp döndürerek, konu gölgeli bir alanda olsaydı aydınlatmanın nasıl görüneceğini yakalamaya başlarız:

![](/images/tips_lighting_env.webp)

Sert güneş ışığını taklit etmek için bir doğrudan ışık eklenip yoğunluğu artırılabilir. Bunu ortam ışığıyla dengelemek hoş bir sonuç verir:

![](/images/tips_lighting_sunlight.webp)

Karakterler, malzemelerini yüzey altı (subsurface) olarak değiştirmekten ve kulakları parlatmak için karakterin arkasına kulaklara doğru bakan bir spot ışık yerleştirmekten fayda görebilir:

![](/images/tips_lighting_sss.webp)

Ardından süreç sonrası işlemlerin geri kalan ayarlarıyla denemeler yapın! Küresel Aydınlanma ve Ortam Oklüzyonu daha gerçekçi bir aydınlatmaya yardımcı olur. Eğrilik ve Keskinleştir, heykeldeki ayrıntıları daha çok ortaya çıkarmaya yardımcı olabilir. Kromatik aberasyon, Alan Derinliği, Tanecik, Parlama ve Vinyet kamera efektlerini taklit etmeye yardımcı olur. Özellikler etkinleştirildikçe aydınlatmanın ve diğer süreç sonrası işlem değerlerinin bunu telafi edecek şekilde ayarlanması gerektiğini unutmayın.

İşte süreç sonrası işlemlerde tam bir dizi ince ayar yapılmış işleme:
![](/images/tips_lighting_final.webp)

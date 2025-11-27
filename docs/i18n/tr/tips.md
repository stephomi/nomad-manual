# ![](/icons/manual.webp) İpuçları

[[toc]]

## Bir modele nasıl başlanır

3B heykeltraşa yeni başlayanlar sık sık bir modele başlamanın en iyi yolunun ne olduğunu sorar. Tek bir en iyi yol yoktur, farklı insanların farklı tercihleri vardır. İşte en yaygın yaklaşımlardan bazıları.

### Küre üzerinde heykel, multires

Nomad açıldığında gelen varsayılan model en yaygın yoldur. Küreyi şekillendirmek için move, clay, crease araçlarını kullanın; büyük değişiklikleri hızlıca yapmak istediğinizde daha düşük subdivison seviyelerini, detay çalışması için daha yüksek subdivision seviyelerini kullanın.

Yaygın bir sorun, poligonlara ihtiyaç duyduğunuz yerlerde sık sık poligonunuzun bitmesi, başka yerlerde ise çok fazla poligonunuzun olmasıdır. Örneğin varsayılan küreyi tam bir vücuda dönüştürürseniz, parmakları yapmak için yeterli detayınız olmayabilir, buna karşın kafanın arkasında boşa giden çok sayıda poligon olur. Ancak kafa gibi çoğunlukla küresel şekiller için bu yöntem gayet iyi olabilir.

### Dyntopo

Dyntopo’yu etkinleştirmek, heykeltraşlık yaparken poligonları uyarlanabilir şekilde ekleyip kaldırır. Bu poligonlar üçgen olacaktır ve yeni başlayanlar, multires’in temiz görünümüyle karşılaştırıldığında bu dağınık yerleşimi genellikle sevmez. Yine de devam etmeye değer! Smooth shading’i açar, wireframe’i kapatır ve yerleşimle ilgili endişelenmeyi bırakırsanız, bu mod size oldukça kil benzeri bir his verebilir. Büyük bir fırça veya smooth fırça kullanırsanız bu modun poligonları da kaldırabildiğini unutmayın; böylece araç her zaman hızlı ve tepkisel hissedilir. Heykelin ilk geçişini bitirdiğinizde, onu klonlayabilir, quad remesher’dan geçirerek güzel bir yerleşim elde edebilir ve orijinal detayları yüksek subdivision seviyesine yeniden projekte edebilirsiniz.

### Voxel remesh

Voxel remesh, heykeliniz üzerinde çoğunlukla quad tabanlı bir topoloji uygular. Bu işlem düşük çözünürlüklerde hızlıdır ve gerilmiş poligonları veya aşırı yoğun poligonları, eşit aralıklı bir yerleşimle hızlıca değiştirmek için kullanılabilir. Bu, küreden tam bir vücuda başlamanın harika bir yolu olabilir; örneğin bir kafayla başlarsınız, boynu uzatırsınız, voxel remesh. Gövdeyi uzatırsınız, voxel remesh, kollar, voxel remesh, vb. temel formları elde edene kadar devam edersiniz.

### Birden fazla nesne kullanın

Birçok anatomi rehberi, bir vücudu basit küreler, silindirler, küplerle temsil eder. Nomad’de de bu şekilde heykel yapabilirsiniz. Bunun avantajı, sahne hiyerarşisinde nesneleri birbirine bağlamanıza izin vermesidir; örneğin boynu döndürdüğünüzde kafa onu takip eder. Hassas taşıma/döndürme/ölçekleme için gizmo aracını kullanabilmek de çok faydalıdır ve ayrıca her şekil için pivot ayarlayarak tam beklediğiniz gibi hareket etmelerini sağlayabilirsiniz. Temel bloklar doğru yere geldiğinde, hepsini seçip voxel remesh veya boolean ile tek bir yüzeye birleştirerek daha detaylı heykel için hazırlayabilirsiniz.

Bu çalışma şekli için kullanışlı bir ipucu: Bir küreyle başlayın, onu uzatılmış bir sosis gibi ölçekleyin, pivot’a basın, ‘bottom’a tıklayın, tekrar pivot’a basın. Artık klonlanabilen, ilk kürenin uzunluğu boyunca taşınabilen, klonlanıp döndürülebilen, klonlanıp kaydırılabilen vb. bir vücut parçanız var; böylece bir vücudu hızlıca yerleştirebilirsiniz.

### Tüpler

Tube aracı bir heykele başlamak için harika bir yoldur. Sürüngen kuyrukları, kollar, bacaklar, parmaklar, kaşlar; hepsi tube aracıyla hızlıca taslak olarak çizilebilir ve sonrasında kolayca düzenlenebilir. Ayrıca kesit profilini değiştirmenize izin vererek hızlı şekil değişiklikleri sağlar. Şekli doğrulayıp üzerinde heykel yapmaya başlayabilir ve tam bir vücut ağı elde etmek için diğer nesnelerle birlikte voxel remesh uygulayabilirsiniz.

### Diğer uygulamaları kullanın

Bazı insanlar bir modele başka uygulamalarda başlamayı tercih eder, bu da gayet normaldir. Blender veya Valence gibi araçlar, modellere low poly teknikleriyle başlanmasına izin verir; bu modeller daha sonra heykel için Nomad’e aktarılabilir.

### Dahili hazır ayarları kullanın

Proje menüsünden sağ üstteki `Preset...`e tıklayın. Burada Blender Foundation’dan çeşitli kafa ve vücut şekli hazır ayarları bulacaksınız. Beğendiğiniz birini seçin, tekrar dokunun, sahnenize ekleyin. 

### Çevrimiçi modeller kullanın

Çevrimiçi olarak birçok ücretsiz model mevcuttur; örneğin polyhaven, sketchfab, turbosquid. Genellikle bu modeller Nomad’e aktarılabilir ve ya doğrudan üzerinde heykel yapılabilir ya da referans olarak kullanılabilir.

### Kural yok!

Sonuçta bu tekniklerin herhangi bir kombinasyonunu, hatta hiçbirini kullanmayabilirsiniz! Nomad bu açıdan çok esnektir; ileri düzey kullanıcılar önce tüplerle başlayıp, sonra dyntopo kullanıp, ardından indirilen bir ayakla birleştirip, sonra hepsini quad remesh’ten geçirip, son detay için multires kullanabilir. Size ne uyuyorsa onu yapın.

## Facegroup’lar

Facegroup aracı, şu YouTube videosunda açıklandığı gibi birçok şey için kullanılabilir: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Bu, videoda ele alınan özelliklerin metin özetidir.

### Neden facegroup?

Facegroup’lar, yüzleri organize etmenizi ve seçmenizi sağlar (bu kılavuzda ‘faces’ ve ‘polygons’ birbirinin yerine kullanılır). Bu, Nomad’in diğer seçim ve organizasyon araçlarıyla karşılaştırıldığında açıklaması daha kolay bir kavramdır. Nomad, nesneler oluşturmanıza, adlandırmanıza, birbirine bağlamanıza izin verir; zeminden, duvarlardan, sandalyeden, masadan vb. oluşan bir odayı tanımlayan bir nesne yapısı oluşturmak kolaydır.

Bir karakter için, ilk bloklamayı kafa, kol, bacak için ayrı nesneler kullanarak yapabilirsiniz; ancak tüm parçaları tek bir mesh’te birleştirdiğinizde bu yapı kaybolur. Maskelerle bir karakterin alt bölümleri üzerinde çalışabilirsiniz, ancak eller için, sonra burun için, sonra tekrar eller için maske boyamak yorucu hale gelebilir.

İşte facegroup’ların faydalı olduğu yer burasıdır. Poligon yüzlerini bir renkle etiketlemenize ve ardından aynı renge sahip poligonları seçip manipüle etmenize olanak tanır. Facegroup rengi ile vertex renginin farklı şeyler olduğunu unutmayın.

En yakın benzetme, bir haritaya renkler boyayıp, daha sonra ülkeleri veya bölgeleri renge göre seçebilmek olurdu.

Karakter kafaları için göz çukurlarını, burnu, dudakları, çeneyi, kulakları işaretlemek üzere bölgeler boyayabilir, sonra bu bölgeleri kolayca seçebilirsiniz. Sert yüzey ve mekanik heykel için paneller ve bölümler tanımlamak faydalı olabilir.

### Facegroup oluşturma ve düzenleme

Facegroup’lar bir fırçayla uygulanabilir; her yeni darbe yeni bir facegroup oluşturur veya imlecin altındaki facegroup’u seçip genişletebilirler. Ayrıca şekiller kullanılarak da oluşturulabilirler.

* Dot, auto-pick etkin – Tek bir sürükleme, yeni bir facegroup rengi tanımlar ve sürüklediğiniz yüzlere atar. Her yeni sürükleme yeni bir facegroup tanımlar. Bir dokunuş yeni bir facegroup’u taşma doldurur.
* Dot, auto-pick devre dışı – Auto-pick düğmesi ‘sub’ modundayken, Nomad imlecin altındaki facegroup’u seçer ve sürüklemenin geri kalanında onu uygular. Bu, facegroup’ları elle seçmek zorunda kalmadan onları iyileştirmek için kullanışlıdır.

### Maskeleme

Mask aracı etkin olduğunda ve araç çubuğundaki facegroup düğmesi aktifken, bir facegroup’a dokunmak onu maskeleyecektir.

### Gizleme

Hide aracı etkin olduğunda ve araç çubuğundaki facegroup düğmesi aktifken, bir facegroup’a dokunmak onu gizleyecektir.

### Organize etme

Daha önce bahsedildiği gibi, facegroup’lar mesh’inizi ayrı nesneler oluşturmak zorunda kalmadan organize etmek için kullanılabilir. Burnu, çeneyi, kulakları ayrı nesnelere bölmek istemeyebilirsiniz, ancak bunların facegroup’lar aracılığıyla tanımlanmış olması çok faydalıdır.

### UV bölgeleri

UV Atlas aracı, dikişleri otomatik olarak tanımlamaya çalışacaktır, ancak bazen dikişleri istemediğiniz yerlere koyar. Bir nesnede facegroup’lar varsa ve UV Atlas seçeneklerinde facegroup seçeneği etkinse, bunun yerine facegroup sınırlarını UV dikişleri olarak kullanacaktır.

### Quad remesher

Quad remesher eklentisi genellikle modelinizde kenarları güzelce akıtır, ancak facegroup seçeneği etkinleştirildiğinde, facegroup’ları onu yönlendirmeye yardımcı olmak için kullanabilirsiniz. Bu, örneğin gözlerin etrafında, kaş kemiğinde, dudaklarda, yanak kıvrımında temiz bir edge flow tanımlamayı kolaylaştırabilir.

### Diğer araçlarla filtreleme

Birçok aracın, ya birincil araç menüsünden ya da stroke -> filtering menüsünden, facegroup farkındalığına sahip olma seçenekleri vardır. Örneğin smooth aracı, %100’ün üzerindeki güçlerde bir facegroup içindeki detayı agresif şekilde yumuşatabilir, ancak facegroup sınırını nispeten sağlam tutar.

### Facegroup sınırlarını rahatlatma ve yumuşatma

Facegroup aracındaki relax seçeneği, diğer özellikleri korurken facegroup sınırlarını yumuşatma konusunda mükemmel iş çıkarır. Bu, quad remesh’ten önce düzgün facegroup sınır bölgeleri tanımlamanın harika bir yolu olabilir.

## Tablet/mobilde sınırlamalar

Güncel tabletler ve telefonlar çok güçlüdür, ancak masaüstü bilgisayarlar ve dizüstü bilgisayarlardan önemli farkları vardır:

### Aktif soğutma yok

Bilgisayarların serin kalmasını sağlamak için fanları ve/veya büyük soğutucuları vardır ve yüksek sıcaklıklarda çalışacak şekilde tasarlanmışlardır. Mobil donanım genellikle önce incelik için, iç kısımların serin kalmasına yardımcı olmak için değil, tasarlanır. Nomad en yüksek kalite ayarlarına (PBR aydınlatma modu, karmaşık malzemeler, çok sayıda nesne, etkinleştirilmiş çok sayıda post process seçeneği) zorlanırsa, bu hem cihazı aşırı ısıtabilir hem de pili çok hızlı tüketebilir. 

Daha iyi bir yaklaşım, bir matcap aydınlatma modu kullanmak ve daha düşük bir render multiplier kullanmaktır (post process menüsünün üst kısmı). Bu seçimler cihazı serin tutar ve daha uzun süre heykel yapmanıza izin verir.

### Sınırlı bellek

Nomad, çoğu masaüstü heykel uygulamasına eşdeğer sonuçlar elde edebilir, ancak fiziğin yasalarını bükemez! Çoğu masaüstü bilgisayar, mobil cihazların iki katı belleğe sahiptir; 3B animasyon için inşa edilen iş istasyonları genellikle 4x veya 8x bellekle gelir. Bu nedenle, kaç poligon kullandığınızın farkında olmak, cihazınızın ne zaman yavaşlamaya başladığını görmek için bazı testler yapmak iyidir. Nomad’i çalıştırabilen neredeyse tüm cihazlar 1 milyon poligonu oldukça rahat kaldırabilir. Bir M2 iPad Pro 8 milyonu rahatça kaldırabilir; insanlar en yeni iPad’lerde bunun çok üzerine çıktıklarını test ettiler.

Öyle olsa da, yalnızca en detaylı heykeller 4 milyon poligondan fazlasına ihtiyaç duyar; nispeten basit nesneler yapıyorsanız ve kendinizi sık sık 500.000, 1 milyon, 4 milyonun üzerine çıkarken buluyorsanız, çok fazla poligon kullanıyorsunuz demektir! Seçeneklerde smooth shaded modunun etkin olduğundan emin olun.

### İşletim sistemi yoğun uygulamalara karşı daha az hoşgörülü

Apple ve Android, uygulamaların küçük dosyaları çok hızlı kaydedip yüklemesini bekler. Ayrıca uygulamaların çok hızlı görev değiştirebileceğini varsayarlar. Nomad dosya boyutlarını nispeten küçük tutmak ve çok hızlı kaydetmek için bazı akıllı numaralar kullansa da, mobil işletim sistemi Nomad’in çok uzun sürdüğüne karar verirse, görevi bitirmesini beklemeden onu basitçe öldürür. Bu, dosyaları daha küçük tarafta tutmak için başka bir nedendir; bir kullanıcının Discord’da bildirdiği gibi 37 milyon poligonluk heykellerle çalışmak mümkündür, ancak tavsiye edilmez!

## Küçük ekranlarda çalışma

Nomad tabletlerde çalışacak şekilde tasarlanmıştır, ancak telefonlarda da iyi çalışır. Telefon gibi küçük bir ekranda heykel yapmak, birkaç arayüz ve iş akışı ayarıyla kolaylaştırılabilir:

* Dört parmakla dokunmak tüm arayüzü açıp kapatır, size heykel için daha fazla alan verir.
* Üç parmakla yukarı/aşağı sürüklemek fırça yarıçapını değiştirir.
* İyi görüyorsanız daha fazla düğme sığdırmak için, kötü görüyorsanız daha büyük yapmak için arayüz ölçeğini küçültebilir veya büyütebilirsiniz.
* Geniş menüler bazen heykelin önüne geçebilir; menü altındaki heykeli görebilmek için bunları saydam ve bulanıksız yapabilirsiniz.
* Parmakla heykel yapıyorsanız, fırça merkezini parmağınızdan biraz uzağa taşımak için offset seçeneğini kullanın.
* Bunlar ve daha birçok seçenek [Interface menüsünde](./interface.md) bulunabilir. 

## Inflate veya peak deformer

Birçok 3B uygulamada, tüm vertex’leri normal yönünde kontrol edilebilir bir miktarda iten bir inflate deformer bulunur. Nomad şu anda deformer’lara sahip olmasa da, bu davranışı inflate fırçasıyla taklit etmek mümkündür:

* Inflate fırçasını seçin
* [Stroke menüsünden](./stroke.md#stroke) stroke yöntemini `Lock + Radius' olarak değiştirin
* Fırça yarıçapını heykelinizden daha büyük yapın, gerekirse kamerayı heykelden uzaklaştırın.
* Nesnenizin yüzeyinde tıklayıp bir stroke sürükleyin; yarıçap nesneden büyük olduğunda, tüm şekil sabit bir miktarda eşit şekilde şişirilecektir.
* Şişirme miktarını kontrol etmek için fırça yoğunluğunu ayarlayın
* Gerekirse belirli alanlarda inflate etkisini korumak veya azaltmak için maskeleme kullanın.

## Voxel remesh işleminden kaynaklanan yumruları veya ‘sivilceleri’ kaldırma

Voxel remesh, eşit aralıklı poligonlar yapmak için harikadır, ancak bazen yumuşatıldığında küçük yumrulara veya sivilcelere neden olacak topoloji oluşturur. Örneğin:

* Varsayılan kürede crease fırçasını kullanın ve bir girdap yapın
* ‘build multiresolution at 3’ ile voxel remesh yapın
* Yüksek yoğunlukla smooth uygulayın
* Artifaktlar ortaya çıkar (yüksek kontrastlı matcap malzemeyle daha kolay görülür):

![](/videos/tip_pimples_before.mp4)

Heykelle düzelmek için, smooth ayarlarında `Stable smoothing` seçeneğini deneyin. Bu, voxel remesh’in düzensiz topoloji yerleşimiyle başa çıkabilir ve temiz sonuçlar elde edebilir.

![](/videos/tip_pimples_stable_smooth.mp4)

Topolojinin kendisini düzeltmek için yeni bir primitive, quad remesh araçları veya harici bir 3B modelleyici kullanın ve orijinal mesh’ten yeni mesh’e `Topology -> Misc -> Reproject` üzerinden detay projekte edin. 

![](/videos/tip_pimples_reproject.mp4)

## Gün ışığı aydınlatması

Varsayılan PBR render’ı, adından da anlaşılacağı gibi fiziksel tabanlıdır ve işlenmemiş bir dijital fotoğraf gibi biraz soluk ve düz görünebilir. Nomad’in ışıkları ve post process’i, render’ların daha canlı görünmesini sağlamak için kullanılabilir.

İşte varsayılan bir render, bunu daha iyi hale getirip getiremeyeceğimize bakalım:
![](/images/tips_lighting_default.webp)

Post process ve tonemapping’i etkinleştirmek parlaklık ve kontrast ekleyebilir:

![](/images/tips_lighting_tonemap.webp)

Işıklara odaklanmak için, varsayılan environment ışığı heykel için iyidir, ancak son render için iyileştirilebilir. Bunu düşünmenin bir yolu, doğrudan ışığı (örneğin güneş) ve ortam ışığını (örneğin gökyüzünün mavisinden, yerden gelen ışık) ayırmaktır. Environment ışığını azaltıp döndürerek, bu, konunun gölgeli bir alanda olması durumunda aydınlatmanın nasıl görünmesi gerektiğini yakalamaya başlar:

![](/images/tips_lighting_env.webp)

Doğrudan bir ışık eklenebilir ve yoğunluğu sert güneş ışığını simüle etmek için artırılabilir. Bunu environment ışığıyla dengelemek hoş bir sonuç verecektir:

![](/images/tips_lighting_sunlight.webp)

Karakterler, malzemelerini subsurface ile değiştirip, kulakları parlatmak için karakterin arkasına kulaklara doğru bakan bir spotlight yerleştirmekten fayda görebilir:

![](/images/tips_lighting_sss.webp)

Sonra diğer tüm post process ayarlarıyla denemeler yapın! Global Illumination ve Ambient Occlusion daha gerçekçi aydınlatmaya yardımcı olur. Curvature ve Sharpen, heykelde daha fazla detayı ortaya çıkarmaya yardımcı olabilir. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette kamera efektlerini simüle etmeye yardımcı olur. Özellikler etkinleştirildikçe, aydınlatma ve diğer post process değerlerinin telafi için ayarlanması gerektiğini unutmayın.

İşte tam bir post process ince ayar setiyle render:
![](/images/tips_lighting_final.webp)

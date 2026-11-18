# ![](/icons/history.webp) Geçmiş {#history}
![](/images/history_overview.webp)

Çoğu içerik üretim aracında olduğu gibi, Nomad'da yaptığınız tüm düzenlemeleri geri alıp yineleyebilirsiniz.
Geçmiş epey büyüyebilir; bu yüzden ne kadarının bellekte tutulacağına, ne kadarının depolamada saklanacağına ve projenizle birlikte kaydedilip kaydedilmeyeceğine siz karar verirsiniz.

::: tip
Geri almak/yinelemek için hızlı hareketleri kullanabilirsiniz:
- Geri almak için 2 parmakla dokunun
- Yinelemek için 3 parmakla dokunun
:::

## ![](/icons/history.webp) Geçmiş {#history-panel}
![](/images/history_history.webp)

Bu panel geçmiş yığınını gösterir: adım numarasını, işlemin adını, uygulandığı nesneyi ve o adımın kullandığı bellek miktarını.

Bir girişe dokunarak o duruma geri (ya da ileri) atlayabilirsiniz. Bir girişe uzun basmak, o girişi ve ondan eski tüm geçmişi kalıcı olarak siler; heykelinizden memnun kaldığınızda bellek boşaltmanın hızlı bir yoludur.

### ![](/icons/speed.webp) Yeniden oynat {#replay}
Sol alttaki oynat düğmesi önce başlangıca geri sarar, ardından işlemleri tek tek yeniden uygular; heykelinizin adım adım oluşmasını izlemenin eğlenceli bir yolu. Kaydırıcı, hızı saniyedeki işlem sayısı olarak belirler. Durdurmak için düğmeye tekrar dokunun; bir geri alma/yineleme ya da bir girişe dokunmak da oynatmayı durdurur.

Oynatma başlamadan önce bir açılır pencere şunları seçmenizi sağlar:
* `Tersine çevir` - Başlangıçtan yeniden oynatmak yerine, mevcut durumdan başlangıca doğru geri alır.
* `Kamerayı eski durumuna getir` - [Kamerayı eski durumuna getir](#restore-camera) kapalı olsa bile kamera, yeniden oynatılan işlemleri takip eder.
* `Kamera yumuşatma` - Kamera her görünüme atlamak yerine görünümler arasında süzülerek geçer. Yüksek değerler daha sakin bir kamera hareketi verir.

::: warning
Yeniden oynatma deneysel bir özelliktir.
:::

## Eylemleri dâhil et {#include-actions}

Geçmiş panelinin altındaki simgeler, hangi tür düzenlemelerin geçmişe kaydedileceğini seçer:

| Eylem       | Simge                         | Açıklama                                                                            |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Işıklar     | ![](/icons/light.webp)        | Işık düzenlemeleri. Bir ışığın Gizmo ile taşınması her zaman kaydedilir, çünkü sahne hiyerarşisindeki diğer nesneleri etkileyebilir |
| Gölgelendirme | ![](/icons/sun.webp)        | PBR, MatCap ve Unlit modu, MatCap'ler ve HDRI'lar                                   |
| Süreç sonrası işlemler | ![](/icons/postprocess.webp) | Süreç sonrası işlem düzenlemeleri                                     |
| Seçim       | ![](/icons/tool_lattice.webp) | Tıklamalar, kement seçimleri ve seçimi kaldırma gibi Kafes seçim düzenlemeleri      |

## Ayarlar {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Kamerayı eski durumuna getir {#restore-camera}
Her işlem için kameranın bakış açısı kaydedilir.
Bu seçeneği etkinleştirirseniz, bir işlemi geri almak veya yinelemek kamerayı kaydedilen bakış açısına geri getirir.

### ![](/icons/history.webp) Geçmişi kaydet {#save-history}
Proje kaydedildiğinde geri alma geçmişini de saklar, böylece proje yeniden açıldığında geçmiş kaybolmaz. Proje dosyalarınızı daha küçük tutmak için kapatın.

### ![](/icons/ram.webp) RAM sınırı {#history-limit-mb}
RAM'de tutulan en fazla geçmiş miktarı. Daha eski durumlar depolamaya taşınır ve gerektiğinde yeniden yüklenir; silinmezler.

### ![](/icons/save.webp) Depolama sınırı {#storage-limit}
Bu projenin geçmişinin kullanabileceği en fazla depolama alanı. Sınıra ulaşıldığında en eski işlemler kalıcı olarak silinir.

::: tip
Yeni bir sınır, bir sonraki düzenleme, geri alma veya yinelemeden sonra geçerli olur.
:::

### ![](/icons/undo.webp) Geri alma uyarısı {#maximum-undoable}
Tek seferde bu sayıdan fazla işlem geriye atlamak önce onay ister. Ardından bir düzenleme yaparsanız o noktadan sonraki tüm işlemler kaybolur; bu ayar sizi listenin çok aşağısına yanlışlıkla dokunmaya karşı korur.

## Bellek istatistikleri {#memory-stats}

Bu bölüm, Nomad'ın kullandığı belleğin ayrıntılı bir dökümünü verir.

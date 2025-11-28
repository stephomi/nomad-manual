# ![](/icons/history.webp) Geçmiş {#history}
![](/images/history_overview.webp)

Çoğu içerik oluşturma aracında olduğu gibi, Nomad'de de tüm düzenlemeleri geri alabilir/yeniden uygulayabilirsiniz.
Geri alınabilir işlem sayısında bir sınır vardır, ancak bu davranışı kontrol edebilirsiniz.

::: tip
Geri al/yeniden uygula için hızlı hareketler kullanabilirsiniz:
- Geri almak için 2 parmakla dokunma
- Yeniden uygulamak için 3 parmakla dokunma
:::

## Geçmiş {#history-panel}
![](/images/history_history.webp)

Bu panel, adım sayısını, işlem adını ve o adımın kullandığı bellek miktarını gösteren geçmiş yığınını görüntüler.

## Ayarlar {#settings}
![](/images/history_settings.webp)

### Geçmiş sınırı (Mb) {#history-limit-mb}
Geçmiş yığını bu değeri aşarsa, bellek bütçesinin bu sınıra sığması için eski işlemler kaldırılır.


### En fazla geri alınabilir {#maximum-undoable}
Maksimum işlem sayısını kontrol edebilirsiniz.

## Kamerayı geri yükle {#restore-camera}
Her işlem için kameranın bakış açısı kaydedilir.
Bu seçeneği etkinleştirirseniz, bir işlemi geri almak veya yeniden uygulamak kamerayı kaydedilen bakış açısına sıfırlar.

## İşlemleri dahil et {#include-actions}

* `Lights` - Devre dışı bırakıldığında, ışık işlemleri (gizmo hareketleri dışında) geçmiş yığını tarafından yok sayılır
* `Matcaps & HDRIs` - Devre dışı bırakıldığında, matcap ve hdri değişiklikleri geçmiş yığını tarafından yok sayılır
* `PostProcess` - Devre dışı bırakıldığında, postprocess seçeneklerindeki değişiklikler geçmiş yığını tarafından yok sayılır

## Bellek istatistikleri {#memory-stats}

Bu bölüm, Nomad tarafından kullanılan belleğin dökümünü verir.
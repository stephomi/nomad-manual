# ![](/icons/history.webp) Geçmiş
![](/images/history_overview.webp)

Çoğu içerik oluşturma aracında olduğu gibi, Nomad'de de tüm düzenlemeleri geri alabilir/yeniden uygulayabilirsiniz.
Geri alınabilir işlem sayısında bir sınır vardır, ancak bu davranışı kontrol edebilirsiniz.

::: tip
Geri al/yeniden uygula için hızlı hareketler kullanabilirsiniz:
- Geri almak için 2 parmakla dokunma
- Yeniden uygulamak için 3 parmakla dokunma
:::

## Geçmiş
![](/images/history_history.webp)

Bu panel, adım sayısını, işlem adını ve o adımın kullandığı bellek miktarını gösteren geçmiş yığınını görüntüler.

## Ayarlar
![](/images/history_settings.webp)

### Geçmiş sınırı (Mb)
Geçmiş yığını bu değeri aşarsa, bellek bütçesinin bu sınıra sığması için eski işlemler kaldırılır.


### Maksimum geri alınabilir
Maksimum işlem sayısını kontrol edebilirsiniz.

## Kamerayı geri yükle
Her işlem için kameranın bakış açısı kaydedilir.
Bu seçeneği etkinleştirirseniz, bir işlemi geri almak veya yeniden uygulamak kamerayı kaydedilen bakış açısına sıfırlar.

## İşlemleri dahil et

* `Lights` - Devre dışı bırakıldığında, ışık işlemleri (gizmo hareketleri dışında) geçmiş yığını tarafından yok sayılır
* `Matcaps & HDRIs` - Devre dışı bırakıldığında, matcap ve hdri değişiklikleri geçmiş yığını tarafından yok sayılır
* `PostProcess` - Devre dışı bırakıldığında, postprocess seçeneklerindeki değişiklikler geçmiş yığını tarafından yok sayılır

## Bellek istatistikleri

Bu bölüm, Nomad tarafından kullanılan belleğin dökümünü verir.

# ![](/icons/camera.webp) Kamera {#camera}

Tato nabídka umožňuje vytvářet a upravovat kamery a také řídit, jak s kamerami pracujete.

![](/images/camera_overview2.webp)

Kamery v Nomadu mají několik využití:

* nastavení pohledů pro modelování z přesných úhlů
* použití jako fotoaparát pro komponování objektů
* jako kamera z pohledu první osoby pro navigaci ve scéně
* jako ortografická kamera pro izometrické hry nebo průmyslový styl renderování.

## Ovládání kamery {#control}

### Rotace {#rotation}
Kameru otáčíte tažením *jednoho* prstu po pozadí.
Pokud táhnete prstem po modelu, místo toho se spustí operace sochání.

::: tip Mohu otáčet kamerou, i když se nedostanu na pozadí?
Ano, můžete položit na obrazovku *dva* prsty – jako byste chtěli začít gesto posunu/zoomu – a pak *jeden* prst zvednout.
:::

### Zaostření / Reset {#focus}
*Dvojitým klepnutím* na model zaostříte na zvolený bod.
Pokud *dvojitě klepnete* na pozadí, kamera zaostří na vybranou síť (mesh).

### Posun {#translation}
Pohybem *dvou* prstů můžete kameru posouvat (pan).

### Přiblížení {#zooming}
Pomocí gesta sevření (pinch) můžete přibližovat/oddalovat.

### Rolování {#rolling}
Můžete *naklánět* pohled otáčením *dvou* prstů.
::: warning
Toto gesto je dostupné pouze pro rotační režim `trackball`.
:::

### Ovládání na desktopu {#desktop}

Na desktopu se pro ovládání kamery používá klávesa alt/opt:

* tip táhnout v prázdném prostoru = rotace kamery
* alt+tip táhnout = posun
* alt+tip táhnout, pak pustit alt = zoom (stejně jako ve ZBrush)

U Wacom tabletů, které mají na peru 2 nebo více tlačítek, použijte nastavení Wacomu a nakonfigurujte hrot a tlačítka takto:

* tip = levé tlačítko myši
* spodní kolébka = prostřední tlačítko
* horní kolébka = pravé tlačítko

S tímto nastavením můžete kameru ovládat pouze perem:

* horní kolébka a pohyb vznosem = rotace kamery
* spodní kolébka a pohyb vznosem = posun

## Ovládací prvky kamery {#camera-controls}

![](/images/camera_list.webp)

### Pohledy {#views}
Pomocí `Add View` můžete ukládat pohledy kamery.
Pokud kliknete na název pohledu, kamera tento pohled obnoví.

::: tip
Uložený pohled si zapamatuje nastavení [Projection Type](#projection-type) a také [Referenční obrázek](background.md).  
Může to být užitečné, pokud chcete přepínat mezi předním/levým/zadním referenčním pohledem s různými pozadími.
:::

|   Action    |              Icon              | Description                                                                  |
| :---------: | :---------------------------: | :--------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Přepnout kameru. Skryté kamery budou přeskočeny tlačítky předchozí/další    |
| Name        |                               | Vybrat kameru                                                                |
| Image       | ![](/icons/image.webp)       | Náhled referenčního obrázku, pokud je ke kameře připojen                     |
| Update View | ![](/icons/update_view.webp) | Aktualizovat uložený pohled podle aktuálního pohledu                        |
| Edit Name   | ![](/icons/pencil.webp)      | Upravit název kamery                                                         |
| Delete      | ![](/icons/trash.webp)       | Smazat kameru                                                                |

### ![](/icons/tool_view.webp) Přidat pohled {#add}
Vytvoří novou kameru na základě aktuálního pohledu.

### ![](/icons/camera.webp) Ikony {#icons-test}

Přepíná, zda jsou ikony kamer viditelné ve viewportu. Pokud je kamera vybraná, její ikona je vždy viditelná.

### Typ projekce {#projection}
Můžete změnit `Field of View` (FOV / ohniskovou vzdálenost) kamery.
Pro účely sochání se obvykle doporučuje používat nízké FOV, protože to může pomoci s proporcemi.  
Můžete také použít režim `Orthographic`, který je víceméně podobný FOV rovnému 0.

### Pohled z první osoby {#fps}
Zapne nastavení pivotu přímo na kameru místo na sochu. Tažení prstu po pozadí udrží pozici kamery uzamčenou, ale změní rotaci, podobně jako ve hrách z pohledu první osoby. Užitečné při sochání prostředí spíše než jednotlivých objektů.

![](/images/camera_rotation_ortho_view.webp)

### Typ rotace {#rotation-type}
Ve výchozím nastavení používá kamera rotační režim `Turntable`.
To znamená, že máte pouze dva stupně volnosti; je to intuitivnější, ale v některých případech budete chtít větší flexibilitu.  
Můžete přepnout na `Trackball`, a pak budete moci *naklánět* pohled otáčením *dvou* prstů ve viewportu. Na desktopu existuje alternativní režim trackball, který může být některým uživatelům povědomější.

### Ortografické přitáhnutí {#orthographic}

Je-li zapnuto, podržení klávesy Shift při otáčení pohledu na klávesnici přichytí kameru k nejbližšímu přednímu/zadnímu/hornímu/dolnímu/levému/pravému pohledu a přepne kameru do ortografického režimu. Kamera bude také přepnuta do ortografického režimu, když kliknete na kostku pohledu pro přichycení na přední/zadní/levý/pravý/horní/dolní pohled.

### Resetovat pohled {#reset}

Přesune kameru dopředu a přizpůsobí scénu zobrazení.

### Přitáhnout pohled {#snap}
Přichytí k nejbližšímu přednímu/zadnímu/levému/pravému/hornímu/dolnímu pohledu. Pokud už jste v jednom z těchto pohledů, opětovné kliknutí přichytí o 180 stupňů na opačnou stranu.

### Rychlost {#speed}

Pokud máte pocit, že se kamera pohybuje příliš pomalu nebo příliš rychle, můžete nastavit násobitel rychlosti pro `rotation`, `translation` a `zooming`. Užitečné, pokud je vaše socha velmi velká nebo velmi malá.

### Přehled pivotu {#pivot}

Když otáčíte kamerou, můžete vidět malou růžovou tečku – to je pivot kamery.  
Je velmi důležité pochopit, kde se pivot nachází, abyste se v kameře neztratili nebo nebyli frustrovaní.

Ve výchozím nastavení se pivot aktualizuje těmito operacemi:
- dvojité klepnutí na model
- dvojité klepnutí na pozadí (nový pivot bude ve středu vaší sítě)
- položení *dvou* prstů na obrazovku (pan/zoom/roll) aktualizuje pivot do středu *dvou* prstů

### Aktualizovat pivot... {#update-pivot}

Můžete dále přizpůsobit, kdy se pivot aktualizuje, pomocí těchto voleb:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Až si na to zvyknete, můžete růžovou tečku (nápovědu) skrýt v nabídce [Settings](settings.md).
:::

### Dvojité klepnutí na objekt {#dtap-object}
Když je `Focus` zapnutý, dvojité klepnutí přesune pivot na klepnutý objekt.

### Dvojité klepnutí na pozadí {#dtap-tap-background}
Je-li zapnuto, nastaví pivot na jednu z možností Selection, Scene, nebo mezi nimi přepíná.
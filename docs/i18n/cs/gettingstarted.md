# Začínáme

## Vítejte v Nomadu!

Nomad je aplikace pro 3D modelování (sochaření), která funguje na mnoha zařízeních a nejlépe pracuje na tabletech s tlakově citlivým stylusem, např. Apple iPad s Apple Pencil nebo Samsung Galaxy Tab se stylusem.

Je inspirovaný desktopovými aplikacemi pro sochaření jako ZBrush a Blender, se zaměřením na snadno pochopitelné uživatelské rozhraní bez omezení funkcí. Pokud jste už někdy používali 3D sochařské aplikace, Nomad vám bude velmi povědomý.

Pokud s 3D sochařením začínáte, je dobré znát pár základů.

::: tip Preferujete video?
Na YouTube je nyní SPOUSTA video tutoriálů pro začátečníky, zde jsou některé skvělé odkazy:

* [Nomad Sculpt Crash Course od Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial od Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS série od SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Vyplatí se podívat na hlavní kanál těchto tvůrců, často zveřejňují nové tutoriály.
:::

## Váš první model

Když Nomad spustíte poprvé, uvidíte na obrazovce kouli. Jednoduše táhněte stylusem po kouli a začněte modelovat. Symetrie je ve výchozím nastavení zapnutá, aby bylo modelování snazší.

![](/videos/gettingstarted_01.mp4)

Velikost štětce změníte pomocí posuvníku `Radius` vlevo.

![](/videos/gettingstarted_02.mp4)

Sílu štětce změníte pomocí posuvníku `Intensity` vlevo.

![](/videos/gettingstarted_03.mp4)

Výchozím nástrojem je `Clay tool` a ten k povrchu přidává materiál. Pokud chcete materiál odebírat, klepněte vlevo na tlačítko `Sub`. Pro opětovné přidávání materiálu klepněte na tlačítko Sub znovu.

![](/videos/gettingstarted_04.mp4)

Pro vyhlazení povrchu klepněte na tlačítko `Smooth`. Pro návrat k běžnému modelování klepněte na tlačítko Smooth znovu.

![](/videos/gettingstarted_05.mp4)

Pro otáčení kolem modelu táhněte v prázdném prostoru mimo model.

![](/videos/gettingstarted_06.mp4)

Pro přiblížení a oddálení použijte dvouprsté gesto přiblížení/oddálení (pinch).

![](/videos/gettingstarted_07.mp4)

Pro posun kamery (pan) položte na obrazovku dva prsty a táhněte.

![](/videos/gettingstarted_08.mp4)

Pokud uděláte chybu, dvouprsté klepnutí provede krok zpět (undo), nebo použijte tlačítko undo vlevo dole. 

![](/videos/gettingstarted_09.mp4)

::: tip Desktopová verze
Na desktopu se pro ovládání kamery používá klávesa alt/opt:

* tip táhnutí v prázdném prostoru = rotace kamery
* alt+tip táhnutí = posun (pan)
* alt+tip táhnutí, pak puštění alt = zoom (stejně jako v ZBrush)

U Wacom tabletů, které mají na peru 2 nebo více tlačítek, použijte nastavení Wacomu a nakonfigurujte hrot a tlačítka takto:

* tip = levé tlačítko myši
* spodní kolébka = prostřední tlačítko
* horní kolébka = pravé tlačítko

S těmito nastaveními můžete kameru ovládat pouze perem:

* horní kolébka a pohyb vznosem = rotace kamery
* spodní kolébka a pohyb vznosem = posun
:::

## Přidání barvy

Nomad vám umožňuje malovat na povrch vašeho modelu. V nabídce nástrojů vpravo najděte nástroj `Paint` a klepněte na něj. Na levém panelu se objeví barevná koule. Klepněte na ni, zobrazí se výběr barvy. Zvolte barvu a malujte na svůj model.

![](/videos/gettingstarted_10.mp4)

Pro mazání klepněte na tlačítko `Erase` na levém panelu a poté mažte po povrchu. Pro návrat do režimu malování klepněte na tlačítko Erase znovu.

![](/videos/gettingstarted_11.mp4)

Pomocí štětce Clay v režimech add/sub, nástroje Smooth a nástroje Paint zkuste vytvořit jednoduchou kreslenou hlavu:

![](/images/gettingstarted_head1.webp)

## Další nástroje

Paleta nástrojů obsahuje mnoho nástrojů, které pomáhají s modelováním. Zatím jste použili štětec Clay (výchozí nástroj), Smooth a Paint. Protože se Smooth používá často, má navíc zkratku na levém panelu.

Nástroje v Nomadu umí širokou škálu věcí – od sochařských nástrojů jako Move, Crease, Inflate až po nástroje jako Split a Trim, které připomínají spíše truhlářské nebo zámečnické nástroje. Stránka [Tools](tools.md) obsahuje více informací.

Zkuste použít nástroje Move, Crease, Inflate a Smooth k přidání detailů na hlavu a změně jejího tvaru:

![](/images/gettingstarted_head2.webp)

Teď, když znáte základy Nomadu, se podíváme na zbytek rozhraní.

## Rozhraní

![](/images/interface_overview1.webp)

* `Top menus` – Nabídky pro přístup k většině funkcí Nomadu. Nabídky vlevo nahoře se týkají hlavně scény a objektů, nabídky vpravo nahoře souvisejí s nástroji. Na menších obrazovkách se tyto nabídky kvůli úspoře místa sloučí.
* `Stats` – Informace o scéně, aktuálním objektu, stavu masky a využití paměti.
* `Nav Cube` – Pomůcka, která ukazuje, z jaké strany se na model díváte, a zároveň zkratka pro skok na různé pohledy. Klepnutím na kostku skočíte na příslušný pohled. Tažením kostky ji otáčíte. Klepnutím na malé ikony vedle kostky zarámujete aktuální objekt nebo resetujete pohled na výchozí.
* `Toolbox` – Nástroje Nomadu jsou dostupné v této posuvné oblasti.
* `Left toolbar` – Posuvníky pro radius a intensity u většiny nástrojů, kontextově specifická tlačítka pro jiné nástroje a zkratky pro symetrii, alt/sub režim nástroje, maskování, vyhlazování, gizmo a možnosti malování.
* `Bottom toolbar` – Zkratky pro často používané funkce, vysvětlené níže.

::: tip Levák?
Můžete zrcadlově otočit umístění a pořadí všech panelů nástrojů, viz [Mirror top bar](interface.md#mirror-top-bar) a další související volby.
:::

## Spodní panel nástrojů

![](/images/interface_bottom_toolbar.webp)

* `Undo` – vrátí poslední operaci
* `Redo` – obnoví poslední vrácenou operaci
* `History` – přístup k možnostem historie, vysvětleným v nabídce [History](history.md).
* `Solo` – přepíná zobrazení pouze aktuálního objektu nebo všech objektů
* `X-Ray` – všechny ostatní objekty se zobrazí v rentgenovém režimu a aktuální objekt bude plný. Dlouhé podržení nebo gesto přejetí nahoru umožní nastavit barvu a průhlednost rentgenového režimu.
* `Voxel` – zkratka k tlačítku [Voxel Remesher](topology.md#voxel-remesher) pro voxelové remeshování. Dlouhé podržení nebo gesto přejetí nahoru zobrazí zkratky pro nastavení kvality voxel remeshe.
* `Grid` – přepíná zobrazení mřížky. Dlouhé podržení nebo gesto přejetí nahoru zobrazí možnosti mřížky.
* `Wire` – přepíná překryvnou drátěnou síť (wireframe). Dlouhé podržení nebo gesto přejetí nahoru zobrazí možnosti drátěného zobrazení.
* `Inspect` – přepíná zobrazení dodatečných dat o aktuální síti (mesh). Ve výchozím nastavení zobrazuje UV mapy, ale dlouhé podržení nebo gesto přejetí nahoru umožní zkontrolovat i jiné vlastnosti, pokud existují, a nastavit, zda se zobrazují na pozadí nebo přímo na síti.

## Další kroky

Co byste se měli naučit dál, záleží na vás a na tom, co vás zajímá! Zde je pár návrhů:

Chcete se dozvědět více o sochařských nástrojích? Přejděte do sekce [Tools](tools.md).

Chcete exportovat své modely? Nebo importovat modely pro další úpravy? Nebo vytvářet obrázky svých modelů? Přejděte do sekce [Files](files.md).

Chcete se dozvědět více o řízení detailu na vašem modelu? Přejděte do sekce [Topology](topology.md) a zjistěte více o multires a decimation.

Chcete pracovat s více objekty? Kombinovat jednoduché objekty a primitiva do větší scény? Přejděte do sekce [Scene](scene.md).

Chcete se naučit *všechno* o Nomadu? Dobrá volba! Tento manuál pokrývá celý Nomad, obsahuje spoustu tipů a triků a má skvělou funkci vyhledávání nahoře. Použijte navigaci vlevo a zjistěte víc.

Pokud preferujete video, Holger Schönischka vytvořil na YouTube obrovskou sbírku tipů a triků pro Nomad: https://www.youtube.com/@ProcreateFX/videos


## Získání pomoci

Pokud máte po přečtení manuálu a zhlédnutí výukových videí stále otázky, existují tři hlavní způsoby, jak mluvit s ostatními uživateli Nomadu nebo s vývojářem Nomadu:

* Navštivte fórum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Připojte se k Nomad discord chatu: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Kontaktujte vývojáře přímo na support@nomadsculpt.com

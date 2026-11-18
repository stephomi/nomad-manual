# ![](/icons/symmetry.webp) Symetrie {#symmetry}

Tato nabídka určuje, jak se tahy opakují přes zrcadlovou rovinu, radiálně nebo jako dlaždice, a nabízí způsoby, jak obnovit symetrii u nesymetrických objektů.

![](/images/symmetry_overview.webp) 

## Přehled {#overview}
Symetrii můžete využít několika způsoby:

* Jako zrcadlo, které převrací práci přes osu X (vlevo/vpravo), Y (nahoře/dole), Z (vzadu/vpředu) nebo jejich kombinaci. 
* Radiální symetrii lze nastavit na X, Y, Z s počtem opakování, například při modelování hvězdice. 
* Dlaždice opakují vaše tahy po objektu, takže se model plynule opakuje bez švů.
* Zrcadla mohou pracovat kolem počátku (tzv. režim svět) nebo kolem středu objektu (tzv. lokální režim).
* Model, který jste začali nesymetricky, lze dodatečně přinutit k symetrii.

Zkratku pro zapnutí a vypnutí symetrie najdete také v levém rychlém panelu (*„Sym“*). Malé „L/W“ ukazuje, jestli je Nomad v lokálním, nebo světovém režimu symetrie. Dlouhým stiskem nebo potáhnutím směrem ke středu obrazovky také vyvoláte nabídku.

![](/images/symmetry_button.webp) 

Nastavení symetrie se ukládá s každým objektem a v nadpisu nabídky je název objektu, který upravujete.
Modelovací nástroje sdílejí stejný stav zapnuto/vypnuto, zatímco transformační nástroje ([Přeměnit](tools.md#transform) a [Gizmo](tools.md#gizmo)) mají vlastní.

::: tip
Nabídka symetrie slouží hlavně k ovládání symetrie tahů. Objekty můžete zrcadlit a opakovat také pomocí [opakovačů v nabídce scény](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Povoleno {#enabled}
Zapne nebo vypne zrcadlový režim, stejně jako tlačítko `Sym` v levém rychlém panelu. Když je vypnutý, připomene vám to ikona upozornění, a nabídka vám také řekne, když aktuální nástroj symetrii ignoruje.

## Roviny {#planes}

Zapněte rovinu (nebo roviny) symetrie a počet opakování pro radiální symetrii. Nemusíte se omezovat na jedinou rovinu: pro složitou symetrii můžete mít zapnuté 1, 2 nebo všechny 3 roviny.

Řádek `Radiálně` nastavuje počet opakování radiální symetrie kolem každé osy. Ani tady nejste omezeni na jedinou osu a radiální symetrie může dokonce fungovat v kombinaci se zrcadlovou, takže velmi rychle získáte detailní výsledky. (Celkový počet opakování je omezen na 200.)

![](/videos/symmetry_demo.mp4) 

## Dlaždice {#tile}

Opakuje vaše tahy podél osy v pravidelných vzdálenostech, takže se model plynule opakuje bez švů. Hodí se na vzory, cihly nebo texturu, kterou chcete opakovat.

Dlaždice zapnete pro každou osu tlačítky `Dlaždice` a pak nastavte buď `Počet` (kolik opakování pokryje objekt), nebo `Vzdálenost` (mezera mezi dvěma opakováními). Mezi těmito dvěma možnostmi přepnete přepínačem vlevo.

## Metoda {#method}
Zrcadlo může být `Lokální` a pohybovat se s objektem, nebo `Svět` a zůstávat na místě. Pokud si nejste jistí, který režim potřebujete, sledujte indikátory zrcadlové roviny a radiální symetrie zobrazené přes objekt. V lokálním režimu se při posunu modelu transformačními nástroji (`Gizmo` nebo `Přeměnit`) posunou i indikátory zrcadla. V režimu svět zůstanou indikátory pevně na místě a objekt se skrz ně posouvá.

## Zrcadlo {#mirroring}
![](/images/symmetry_mirroring.webp)

Při modelování blízko rovin symetrie se některé štětce nechovají úplně symetricky. Tato část vám umožní symetrii obnovit tím, že zkopíruje jednu stranu modelu na druhou. 

`Směr` - Dvě tlačítka se šipkami vedle nadpisu `Zrcadlo` určují, která strana se zkopíruje na druhou. Nomad to počítá z aktuálního pohledu, takže strana zůstává na obrazovce stejná, ať se na model díváte odkudkoli.

![](/icons/shield.webp) `Maska` - Tlačítkem masky můžete omezit, co se zrcadlí; maskování cílové strany tuto oblast ochrání, maskování zdrojové strany zabrání tomu, aby se oblast zrcadlila na cílovou stranu. 

![](/icons/tool_hide.webp) `Skrýt` - Když je aktivní, skryté oblasti na zdrojové straně se na cílovou stranu nezrcadlí. 

`Zrcadlo` (udržet topologii) se pokusí zjistit, jestli je topologie na obou stranách zrcadla stejná, a pokud ano, jen posune vrcholy. To je nejběžnější případ. Radiální symetrie se ignoruje. Pokud topologie symetrická není, Nomad nabídne vynutit zrcadlení pomocí `Řez • Zrcadlo`.

Tlačítka `Řez` rozříznou objekt podél rovin symetrie. Mění topologii, takže jsou destruktivnější než `Zrcadlo`. Číslo na každém tlačítku udává, kolik objektů získáte:

* `Řez` - odstraní jednu stranu objektu.
* `Řez • Zrcadlo` - rozřízne objekt, zkopíruje jednu stranu, zrcadlí ji na druhou a svaří vrcholy podél zrcadla. Tato metoda je někdy nutná, když se model na obou stranách zrcadla hodně liší.
* `Řez • Rozdělit` - rozřízne objekt a každou stranu ponechá jako samostatný objekt.
* `Řez • Zrcadlo • Rozdělit` - jako `Řez • Zrcadlo`, ale každá strana se stane samostatným objektem.

Pokud je vybraných víc objektů, `Zrcadlo` i [Převrátit objekt](#flip-object) se použijí na všechny.

### Převrátit objekt {#flip-object}
![](/images/symmetry_flip.webp)
Prohodí levou a pravou stranu podél osy `X`, `Y` nebo `Z`. Vzhledově podobné, jako kdybyste v nabídce nástroje gizmo nastavili měřítko na X na -1.

## Resetovat a upravit {#reset-and-edit}

![](/images/symmetry_edit.webp)

Polohu a orientaci symetrie lze upravit (ale nedoporučuje se to!). V případě potřeby vrátí `Centrum světa` (`Centrum objektu` v lokálním režimu) a `Orientace` polohu a orientaci symetrie na výchozí hodnoty.

Nomad obvykle ví, kam rovinu symetrie umístit. Ruční úprava se nedoporučuje, ale pro pokročilé uživatele to umožňuje tlačítko `Gizmo (Upravit)`. Po jeho stisknutí se zobrazí gizmo, kterým můžete rovinu symetrie posouvat a otáčet. Chcete-li vrátit výchozí střed a orientaci, použijte tlačítka pro reset výše.

`Z pivotu` umístí rovinu symetrie na pivot nástroje [Gizmo](tools.md#gizmo). Je dostupné jen tehdy, když je nástroj `Gizmo` aktivní.

Chování těchto možností se mění podle toho, v jakém prostoru (*Lokální/Svět*) se nacházíte.
Pokud tedy nefungují tak, jak čekáte, zkontrolujte, jestli jste ve správném prostoru.

::: tip
Úprava roviny symetrie gizmem je trochu experimentální, pravděpodobně ji nebudete potřebovat!
:::

## Možnosti zobrazení {#show-options}
![](/images/symmetry_show.webp)


`Zobrazit čáru` a `Zobrazit rovinu` zapínají a vypínají překryv s polohou symetrie ve výřezu. Vypnutí těchto možností se projeví až po zavření nabídky symetrie.

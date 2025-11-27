# ![](/icons/symmetry.webp) Symetrie

Tato nabídka ovládá, jak budou tahy opakovány přes zrcadlovou rovinu nebo radiálně, a způsoby, jak obnovit symetrii na nesymetrických objektech.

![](/images/symmetry_overview.webp) 

## Přehled 
Symetrii můžete používat několika způsoby:

* Jako zrcadlo, které převrací práci přes osy X (vlevo/vpravo), Y (nahoře/dole), Z (vzadu/vpředu), nebo jejich kombinaci. 
* Radiální symetrii lze nastavit na osách X Y Z s počtem opakování, např. při modelování hvězdice. 
* Zrcadla mohou fungovat kolem počátku souřadného systému (tzv. režim svět) nebo kolem středu objektu (tzv. lokální režim).
* Sochy, které začaly jako nesymetrické, lze vynutit jako symetrické.

Zkratku pro zapnutí/vypnutí symetrie lze také najít v levém rychlém panelu (*„Sym“*). Malé „L/W“ označuje, zda je Nomad v lokálním nebo světovém režimu symetrie. Dlouhým stiskem nebo přejetím do středu obrazovky můžete také vyvolat nabídku.

![](/images/symmetry_button.webp) 

Jde o globální volbu, takže stav se přenáší mezi různými nástroji.
Jedinými výjimkami jsou transformační nástroje ([Přesunout](#translate), [Otočit](#rotate), [Měřítko](#scale) a [Gizmo](#gizmo)), které mají vlastní stav symetrie.

::: tip
Nabídka symetrie slouží hlavně k ovládání symetrie tahů. Objekty můžete také zrcadlit a opakovat pomocí [repeaterů v nabídce scény](scene#repeaters). 
:::

## Enabled
Přepíná režim zrcadlení, je to totéž jako tlačítko `Sym` v levém rychlém panelu. 

## Planes

Zapnutí roviny/rovin symetrie a nastavení počtu opakování pro radiální symetrii. Nemusíte volit jen jednu rovinu, pro složitou symetrii můžete mít zapnuté 1, 2 nebo 3 roviny.

Osa a počet opakování pro radiální symetrii. Ani tyto volby nejsou omezeny jen na jednu osu a mohou fungovat i v kombinaci s rovinnou symetrií, takže lze velmi rychle generovat detailní výsledky. (Celkový počet opakování je omezen na 150.)

![](/videos/symmetry_demo.mp4) 

## Method
Zrcadlo může být buď „Local“ (lokální) a pohybovat se s objektem, nebo „World“ (světové) a zůstávat nehybné. Pokud si nejste jisti, který režim potřebujete, sledujte rovinu zrcadlení a radiální indikátory překryté přes objekt. V lokálním režimu se při použití transformačního gizma a posunu modelu budou indikátory zrcadla pohybovat spolu s ním. Ve světovém režimu zůstanou indikátory zrcadla na místě a objekt se bude skrz ně posouvat.

## Mirroring
![](/images/symmetry_mirroring.webp)

Při modelování v blízkosti rovin symetrie mohou mít některé štětce nedokonalé symetrické chování. Tato sekce umožňuje obnovit symetrii zkopírováním jedné strany sochy na druhou. 

`Direction` – Tlačítka `<<` a `>>` určují, která strana bude zkopírována na druhou. Nomad to počítá z aktuálního pohledu, takže nastavení na `<<` například vždy zkopíruje z pravé strany obrazovky na levou.

![](/icons/shield.webp) `Mask` – Tlačítko masky vám umožní vymezit, co bude zrcadleno; maskování cílové strany tuto oblast ochrání, maskování zdrojové strany zabrání tomu, aby se tato oblast zrcadlila do cíle. 

![](/icons/tool_hide.webp) `Hide` – Pokud je aktivní, oblasti, které jsou na zdrojové straně skryté, nebudou zrcadleny do cíle. 

`Mirror` se pokusí zjistit, zda je topologie na obou stranách zrcadla stejná, a pokud ano, pouze přesune vrcholy. To je běžnější scénář.

`Split & Mirror` v podstatě objekt podél zrcadla rozřízne, jednu stranu zkopíruje, zrcadlí ji na druhou a svaří vrcholy podél zrcadla. Je to destruktivnější volba a smaže multirezoluci, ale někdy je tato metoda nutná, pokud je model přes zrcadlo velmi odlišný.

### Flip object
![](/images/symmetry_flip.webp)
Přehoďte levou stranu na pravou a naopak. Vzhledově podobné tomu, jako kdybyste v nabídce nástroje gizmo nastavili měřítko na -1 na ose X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Je možné upravit polohu a orientaci symetrie (ale nedoporučuje se to!). V případě potřeby `World center` a `Orientation` obnoví polohu a orientaci symetrie na výchozí hodnoty.

Nomad obvykle ví, kam umístit rovinu symetrie. Nedoporučuje se to nastavovat ručně, ale tlačítko `Gizmo (Edit)` to umožňuje pokročilým uživatelům. Po kliknutí na toto tlačítko se zobrazí gizmo, které umožňuje rovinu symetrie posouvat a otáčet. Pokud chcete obnovit výchozí střed a orientaci, slouží k tomu tlačítka `object center` a `orientation`.

Chování těchto voleb se mění podle toho, v jakém prostoru (*Local/World*) se nacházíte.
Pokud tedy nefungují podle očekávání, zkontrolujte, zda jste ve správném prostoru.

::: tip
Tlačítko `Gizmo (Edit)` je záměrně zašedlé jako připomínka, že byste ho pravděpodobně neměli používat!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` a `Show plane` přepínají překryvné zobrazení polohy symetrie ve výřezu. Všimněte si, že vypnutí těchto voleb se projeví až po zavření nabídky symetrie.

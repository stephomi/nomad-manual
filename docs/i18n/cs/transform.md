# ![](/icons/transform.webp) Přeměnit {#transform}

Tato nabídka ukazuje transformaci vybraného objektu v číslech: kde je, jak je otočený a zvětšený a jak je velký. Můžete zadat přesné hodnoty, vynulovat je nebo je vypéct do sítě.

![](/images/transform_overview.webp)

## Přehled {#overview}

Každý objekt má kromě svých vrcholů i uzel, který uchovává jeho posun, rotaci a měřítko (jeho matici). Nástroje [Gizmo](tools.md#gizmo) a [Přeměnit](tools.md#transform) tuto matici mění, když táhnete ve výřezu; tato nabídka vám ji umožní přečíst a hodnoty zadat ručně. Rozdíl mezi posunem uzlu a posunem vrcholů vysvětluje část [Uzly a vrcholy](tools.md#nodes-and-vertices).

Hodnotu změníte tažením doleva nebo doprava, nebo na ni klepněte a napište číslo. Hodnoty X, Y a Z jsou podbarvené červeně, zeleně a modře, stejně jako osy gizma.

::: tip
Zadávání hodnot se hodí k přesnému umístění objektů, například když chcete dát několik dílů do úplně stejné výšky, nebo vrátit rotaci na kulaté číslo po volném otáčení gizmem.
:::

## Matice {#matrix}

Nadpis říká, v jakém prostoru jsou hodnoty vyjádřené: `Lokální` (vzhledem k rodičovskému objektu) nebo `Svět`.

### Objekt a pivot {#object-pivot}

* `Objekt` - Hodnoty jsou vlastní transformací objektu.
* `Pivot` - Hodnoty ovládají výběr z jeho [pivotu](tools.md#pivot), stejně jako to dělají úchyty gizma: řádky ukazují nulu a jejich změnou výběr posunete, otočíte nebo změníte jeho měřítko kolem pivotu. Zapněte `Upravit` (ikona zámku), chcete-li posunout jen pivot, objekty zůstanou na místě.

### Lokální a svět {#local-world}

Když má objekt rodiče nebo potomky, nebo je vybraných víc objektů, můžete zvolit, v jakém prostoru se hodnoty zobrazí: `Lokální` (vzhledem k rodiči) nebo `Svět`.

### Akce {#actions}

| Akce                 | Ikona                         | Popis |
| :------------------: | :---------------------------: | :---------- |
| Přesunout počátek    | ![](/icons/target.webp)      | Přesune objekt do počátku světa. |
| Vypéct               | ![](/icons/bake.webp)        | Použije matici na vrcholy a matici vynuluje. Vizuálně se nic nezmění, ale počátek objektu je teď v počátku světa. |
| Pivot                | ![](/icons/gizmo.webp)       | Vypeče pivot do objektu: počátek a orientace objektu převezmou počátek a orientaci pivotu. Vizuálně se nic nezmění. |
| Upravit              | ![](/icons/lock.webp)        | (Režim `Pivot`) Posune jen pivot. |
| Resetovat            | ![](/icons/reset.webp)       | Vrátí transformaci na identitu. V režimu `Pivot` místo toho vrátí pivot na místo. |

Když má vybraný objekt instance, vypečení si vyžádá potvrzení s možností `Zrušit instanci`: vypečení mění vrcholy, které instance sdílejí.

### Posun, rotace, měřítko {#translation-rotation-scale}

Poloha, rotace (ve stupních) a měřítko objektu na osách X, Y a Z. Dvě tlačítka na konci každého řádku vypečou do vrcholů jen tuto část transformace, nebo ji vynulují.

Řádek `Klopení` se objeví, když je objekt zkosený, například po nerovnoměrné změně měřítka otočeného rodiče.

### Jednotné měřítko {#uniform-scale}

Když je zapnuté, měřítko je jediná hodnota, stejná na všech třech osách. Vypněte ho, chcete-li měnit měřítko X, Y a Z zvlášť.

## Rozměry {#dimension}

Velikost a střed ohraničujícího kvádru výběru, v jednotkách světa. Při výběru více objektů zahrnuje všechny.

* `Velikost` - Šířka, výška a hloubka. Se zapnutým tlačítkem propojení změna jednoho rozměru stejným poměrem změní i zbylé dva, takže se zachovají proporce.
* `Střed` - Střed ohraničujícího kvádru. Tlačítko s terčem posune výběr tak, aby jeho střed byl v počátku světa.

::: tip
`Velikost` je nejrychlejší způsob, jak dát objektu skutečnou velikost, například před 3d tiskem: nastavte požadovanou výšku a propojení zachová proporce.
:::

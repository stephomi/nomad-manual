# ![](/icons/operation.webp) Operace {#operation}

Tato nabídka použije operaci na celý povrch vybraných objektů najednou: vyhlazení, uvolnění, leštění, zvětšení, úpravu barev, rozmazání nebo zaostření malby a masky.

![](/images/operation_overview.webp)

## Přehled {#overview}

Zatímco štětec působí tam, kudy vedete tah, operace zasáhne naráz každý vrchol vybraných objektů. V nadpisu je název objektu, nebo počet objektů, pokud jich máte vybraných víc.

Každá operace je posuvník: táhněte doprava, abyste ji použili víc, doleva, abyste ji použili méně (nebo opačnou operaci, u posuvníků se šipkou na obou stranách). Po puštění se posuvník vrátí na nulu a každé tažení je jeden krok v [Historii](history.md), takže můžete operaci použít několikrát po malých dávkách.

::: tip
Operace jsou rychlý způsob, jak vyčistit celou síť po voxelovém přesíťování nebo booleovské operaci: trocha `Uvolnit` vyrovná trojúhelníky, trocha `Hladit` odstraní šum, a nemusíte štětcem hledat každé místo zvlášť.
:::

## Filtry {#filters}

Tlačítka nahoře omezují, kde se operace projeví:

* `Maska` - Maskované oblasti zůstanou nedotčené.
* `Skrýt` - Skryté oblasti zůstanou nedotčené.
* `Offset` - (S vybranou [vrstvou](layers.md)) Ovlivní jen oblasti, kde aktivní vrstva obsahuje modelování, takže můžete vyhladit nebo zvětšit obsah vrstvy, aniž byste sáhli na zbytek.

## Vyhlazení {#smoothing}

* `Zachovat objem` - Vyhlazuje, aniž by se povrch zmenšoval. Tlačítko s ozubeným kolem obsahuje hodnoty `Zmenšit` a `Zvětšit`, které k tomu používá.
* `Zachovat hranice` - Vrcholy na hranici sítě (okraj díry) zůstanou na místě.
* `Stabilní vyhlazení` - Snaží se, aby vyhlazení nezáviselo na topologii. Nejlépe funguje, když se hustota polygonů hodně mění.
* `Hladit` - Vyhladí povrch. Tažením doleva ho místo toho `Zaostřit`.
* ![](/icons/group.webp) `Hladit` - Vyhladí hranice mezi [skupinami tváří](tools.md#facegroup) a narovná zubaté obrysy skupin. Tažením doleva je zaostříte.
* `Uvolnit` - Vyrovná polygony a zachová tvar.
* ![](/icons/group.webp) `Uvolnit` - Uvolní polygony podél hranic skupin tváří.
* `Zachovat rohy` - S `Hladit` a `Uvolnit` pro skupiny tváří zůstanou hranice pevné tam, kde se lomí víc než o tento úhel, takže rohy zůstanou ostré, zatímco strany se vyhladí. Zapnete ho zaškrtávacím políčkem.

## Leštění {#polish}

Zploští povrch do čistých plošek, stejně jako nástroj [Leštění](tools.md#polish). `Úhel` určuje, které plochy se zploští společně: plochy ohnuté méně než o tento úhel se spojí do jedné plošky. Menší úhel zachová víc hran a menší plošky.

## Zvětšit {#inflate}

Vytlačí povrch ven podél normál, nebo dovnitř, když táhnete doleva. `Normální (Uvolnit)` zároveň uvolňuje polygony, aby se nenatahovaly; vypnete ho zaškrtávacím políčkem.

## Úpravy barev {#color-adjustments}

Vyberte kanál, který chcete upravit: `Barva`, `Drsnost`, `Kovovost`, `Krytí`, `Hustota` (malování hustoty pro [Quad Remesher](tools.md#quad-remesher), pokud ho objekt má) nebo `Maska`, a pak:

* `Expozice` - Zesvětlí nebo ztmaví hodnoty.
* `Saturace` - (Jen `Barva`) Živější nebo tlumenější barvy.
* `Kontrast` - Hodnoty od sebe oddálí, nebo je přiblíží k sobě.
* `Odstín` - Posune barvy po barevném kruhu.

## Rozmazání {#blur}

Rozmaže vybrané kanály po povrchu: zapněte `Barva`, `Drsnost`, `Kovovost`, `Krytí`, `Hustota` nebo `Maska` a táhněte `Rozmazání`. Tažením doleva místo toho `Zaostřit`.

U masky je to totéž jako posuvník `Rozmazat` nástroje [Maska](tools.md#mask). Tady ale můžete rozmazat i kanály malby.

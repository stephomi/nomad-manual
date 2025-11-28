# ![](/icons/manual.webp) Tipy {#tips}

[[toc]]

## Jak začít model {#how-to-start-a-model}

Začátečníci v 3D sochaření se často ptají, jaký je nejlepší způsob, jak začít model. Žádný „nejlepší“ způsob neexistuje, různí lidé mají různé preference. Zde jsou některé z běžnějších přístupů.

### Sochání na kouli, multires {#sculpt-on-sphere-multires}

Výchozí model po spuštění Nomadu je nejběžnější způsob. Pomocí nástrojů Move, Clay, Crease tvarujte kouli, používejte nižší úrovně subdivize, když chcete rychle dělat velké změny, a vyšší úrovně subdivize pro detailní práci.

Častým problémem je, že vám často dojdou polygony tam, kde je potřebujete, zatímco jinde jich máte příliš mnoho. Například pokud výchozí kouli vytáhnete do celého těla, je pravděpodobné, že nebudete mít dostatek detailu na prsty, zatímco na zadní části hlavy budete mít spoustu zbytečných polygonů. Pro převážně kulovité tvary, jako je hlava, to ale může být v pořádku.

### Dyntopo {#dyntopo}

Zapnutí Dyntopo bude adaptivně přidávat a odebírat polygony během sochaření. Tyto polygony budou trojúhelníky a začátečníkům se často nelíbí „nepořádné“ rozložení ve srovnání s čistým vzhledem multires. Vyplatí se vytrvat! Pokud zapnete smooth shading, vypnete wireframe a přestanete se starat o rozložení, tento režim může působit velmi „jako hlína“. Nezapomeňte, že pokud použijete velký štětec nebo smooth štětec, tento režim může také polygony odebírat, takže nástroj je vždy rychlý a responzivní. Jakmile máte hotový první průchod sochy, můžete ji naklonovat, spustit přes quad remesher pro pěkné rozložení a reprojektovat původní detaily na vysokou úroveň subdivize.

### Voxel remesh {#voxel-remesh}

Voxel remesh aplikuje na vaši sochu převážně quadovou topologii. Tato operace je rychlá při nižším rozlišení a lze ji použít k rychlé náhradě natažených nebo příliš hustých polygonů rovnoměrně rozloženým meshem. Může to být skvělý způsob, jak začít celé tělo z koule; například začnete hlavou, vytáhnete krk, voxel remesh. Vytáhnete tělo, voxel remesh, ruce, voxel remesh atd., dokud nemáte základní tvary.

### Používejte více objektů {#use-multiple-objects}

Mnoho anatomických příruček znázorňuje tělo pomocí jednoduchých koulí, válců, krychlí. Stejným způsobem můžete sochat i v Nomadu. Má to výhodu v tom, že můžete objekty v hierarchii scény parentovat, takže například otočíte krk a hlava ho bude následovat. Možnost používat nástroj Gizmo pro přesné posuny/rotace/škálování je také velmi užitečná a můžete také nastavit pivoty pro jednotlivé tvary tak, aby se pohybovaly přesně tak, jak očekáváte. Když jsou základní bloky na správném místě, můžete je všechny vybrat a pomocí voxel remesh nebo boolean sloučit do jednoho povrchu pro detailnější sochaření.

Užitečný tip pro tento způsob práce: začněte koulí, roztáhněte ji do „párku“, stiskněte Pivot, klikněte na „Bottom“, znovu stiskněte Pivot. Nyní máte část těla, kterou můžete klonovat, posouvat podél délky první koule, klonovat, otáčet, klonovat, posouvat atd., abyste rychle rozložili celé tělo.

### Trubky {#tubes}

Nástroj Tube je skvělý způsob, jak začít sochu. Ocasy plazů, ruce, nohy, prsty, obočí – to vše lze rychle načrtnout pomocí nástroje Tube a pak snadno upravovat. Umožňuje také měnit profil průřezu, což dovoluje rychlé změny tvaru. Tvar můžete „validate“, abyste na něm mohli začít sochat, a společně s ostatními objekty jej voxel remeshnout do jednoho těla.

### Používejte jiné aplikace {#use-other-apps}

Někteří lidé raději začínají model v jiných aplikacích, to je také v pořádku. Nástroje jako Blender nebo Valence umožňují začít model pomocí low-poly technik, poté je lze importovat do Nomadu pro sochaření.

### Používejte vestavěné presety {#use-the-built-in-presets}

V Project menu klikněte vpravo nahoře na `Preset...`. Najdete zde několik presetů tvarů hlavy a těla od Blender Foundation. Vyberte ten, který se vám líbí, klepněte na něj znovu a přidejte ho do scény. 

### Používejte online modely {#use-online-models}

Online je k dispozici mnoho volných modelů, např. Polyhaven, Sketchfab, Turbosquid. Tyto modely lze obvykle importovat do Nomadu a buď na nich přímo sochat, nebo je použít jako referenci.

### Žádná pravidla! {#no-rules}

Nakonec můžete použít libovolnou kombinaci těchto technik, nebo žádnou! Nomad je v tomto ohledu velmi flexibilní, pokročilí uživatelé mohou začít tubami, pak dyntopo, pak zkombinovat se staženou nohou, pak vše quad remeshnout a nakonec použít multires pro finální detaily. Cokoli vám funguje.

## Facegroups {#facegroups}

Nástroj Facegroup lze použít pro mnoho věcí, jak je vysvětleno v tomto videu na YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Toto je textové shrnutí funkcí pokrytých v tomto videu.

### Proč facegroups? {#why-facegroups}

Facegroups vám umožňují organizovat a vybírat faces („faces“ a „polygony“ jsou v tomto manuálu používány zaměnitelně). To se snáze vysvětluje ve srovnání s ostatními výběrovými a organizačními nástroji Nomadu. Nomad vám umožňuje vytvářet objekty, pojmenovávat je, parentovat je, je snadné vytvořit strukturu objektů pro definici místnosti složené z podlahy, stěn, židle, stolu atd.

U postavy můžete udělat počáteční block-out pomocí samostatných objektů pro hlavu, ruku, nohu, ale jakmile všechny části sloučíte do jednoho meshe, tato struktura se ztratí. Na podsekcích postavy můžete pracovat pomocí masek, ale může být únavné neustále malovat masku na ruce, pak na nos, pak zase na ruce.

Zde jsou užitečné facegroups. Umožňují vám označit polygonové faces barvou a pak vybírat a manipulovat s polygony, které mají stejnou barvu. Všimněte si, že barva facegroup a vertex color jsou odlišné věci.

Nejbližší analogií by bylo malování barev na mapu a následná možnost vybírat země nebo regiony podle barvy.

U hlav postav můžete namalovat zóny pro oční důlky, nos, rty, bradu, uši a pak tyto zóny snadno vybírat. U hard-surface a mechanického sochaření může být užitečné definovat panely a sekce.

### Vytváření a úprava facegroups {#creating-and-editing-facegroups}

Facegroups lze aplikovat štětcem, kde každý nový tah vytvoří novou facegroup, nebo mohou vybrat facegroup pod kurzorem a rozšířit ji. Lze je také vytvářet pomocí tvarů.

* Dot, auto-pick zapnutý – jedno tažení definuje novou barvu facegroup a přiřadí ji faces, přes které táhnete. Každé nové tažení definuje novou facegroup. Klepnutí zaplaví novou facegroup.
* Dot, auto-pick vypnutý – když je tlačítko auto-pick v režimu „sub“, Nomad vybere facegroup pod kurzorem a aplikuje ji po zbytek tažení. To je užitečné pro zpřesňování facegroups bez nutnosti je ručně vybírat.

### Maskování {#masking}

Když je aktivní nástroj Mask a tlačítko facegroup je aktivní na jeho toolbaru, klepnutí na facegroup ji zamaskuje.

### Skrývání {#hiding}

Když je aktivní nástroj Hide a tlačítko facegroup je aktivní na jeho toolbaru, klepnutí na facegroup ji skryje.

### Organizace {#organizing}

Jak bylo zmíněno dříve, facegroups lze použít k organizaci vašeho meshe bez nutnosti vytvářet samostatné objekty. Možná nechcete rozdělit hlavu na samostatné objekty pro nos, bradu, uši, ale je velmi užitečné mít je definované pomocí facegroups.

### UV oblasti {#uv-regions}

Nástroj UV Atlas se pokusí definovat švy automaticky, ale někdy je umístí tam, kde je nechcete. Pokud na objektu existují facegroups a v možnostech UV Atlas je aktivní volba facegroup, použije místo toho hranice facegroups jako UV švy.

### Quad remesher {#quad-remesher}

Plugin Quad Remesher obvykle pěkně vede hrany na vašem modelu, ale můžete mu pomoci je řídit pomocí facegroups, pokud je volba facegroup zapnutá. To může usnadnit definici čistého edge flow kolem očí, obočí, rtů, záhybu tváře apod.

### Filtrování s jinými nástroji {#filter-with-other-tools}

Mnoho nástrojů má možnosti, aby si byly vědomy facegroups, buď v hlavním menu nástroje, nebo přes Stroke -> Filtering. Například nástroj Smooth při síle nad 100 % může agresivně vyhlazovat detaily uvnitř facegroup, ale zachovat hranici facegroup relativně neporušenou.

### Uvolnit a vyhladit hranice facegroup {#relax-and-smooth-facegroup-borders}

Volba Relax v nástroji Facegroup výborně vyhlazuje hranice facegroups a přitom zachovává ostatní rysy. Může to být skvělý způsob, jak definovat hladké hraniční oblasti facegroups před quad remeshem.

## Omezení na tabletu/mobilu {#limitations-on-tabletmobile}

Současné tablety a mobily jsou velmi výkonné, ale mají důležité rozdíly oproti stolním počítačům a notebookům:

### Bez aktivního chlazení {#no-active-cooling}

Počítače mají ventilátory a/nebo velké heatsinky pro chlazení a jsou navrženy tak, aby běžely při vysokých teplotách. Mobilní hardware je obvykle navržen primárně pro tenkost, ne pro chlazení vnitřních komponent. Pokud je Nomad tlačen na nejvyšší kvalitu (PBR lighting mode, komplexní materiály, mnoho objektů, mnoho zapnutých post-processing voleb), může to zařízení přehřívat a velmi rychle vybíjet baterii. 

Lepší přístup je použít matcap lighting mode a nižší render multiplier (nahoře v post-process menu). Tyto volby udrží zařízení chladnější a umožní vám sochat déle.

### Omezená paměť {#limited-memory}

Nomad může dosáhnout výsledků srovnatelných s většinou desktopových sochařských aplikací, ale nemůže ohýbat fyzikální zákony! Většina stolních počítačů má dvojnásobek paměti oproti mobilním zařízením, pracovní stanice pro 3D animaci mívají často 4× nebo 8× více paměti. Proto je dobré mít přehled o tom, kolik polygonů používáte, a udělat si na svém zařízení testy, kdy začne být laggové. Téměř všechna zařízení, která zvládnou spustit Nomad, si docela snadno poradí s 1 milionem polygonů. M2 iPad Pro zvládne pohodlně 8 milionů, lidé testovali na nejnovějších iPadech i mnohem víc.

To ale neznamená, že každý model tolik potřebuje – jen ty nejdetailnější sochy potřebují více než 4 miliony polygonů; pokud děláte relativně jednoduché objekty a často se dostáváte nad 500 000, 1 milion, 4 miliony, používáte příliš mnoho polygonů! Ujistěte se, že máte v možnostech zapnutý smooth shaded mode.

### OS je méně shovívavý k náročným aplikacím {#os-is-less-forgiving-with-intensive-apps}

Apple a Android očekávají, že aplikace budou ukládat a načítat malé soubory velmi rychle. Také předpokládají, že aplikace mohou velmi rychle přepínat úlohy. Nomad sice používá chytré triky, aby udržel velikost souborů relativně malou a ukládal je velmi rychle, ale pokud si mobilní OS myslí, že Nomad trvá příliš dlouho, jednoduše ho zabije dřív, než dokončí úlohu. To je další důvod, proč udržovat soubory menší; je možné pracovat se sochami o 37 milionech polygonů, jak jeden uživatel hlásil na Discordu, ale není to doporučeno!

## Práce na malých obrazovkách {#working-on-small-screens}

Nomad je navržen pro práci na tabletech, ale dobře funguje i na telefonech. Sochaření na malé obrazovce, jako je telefon, lze usnadnit několika úpravami UI a workflow:

* Čtyřprsté klepnutí přepíná celé UI, čímž získáte více prostoru pro sochaření.
* Tříprsté tažení nahoru a dolů mění poloměr štětce.
* Měřítko UI lze zmenšit, aby se vešlo více tlačítek, pokud máte dobrý zrak, nebo zvětšit, pokud máte špatný zrak.
* Širší menu mohou někdy překážet soše, můžete je udělat průhledná a bez rozmazání, abyste viděli sochu pod nimi.
* Pokud socháte prstem, použijte volbu Offset pro posunutí středu štětce trochu od prstu.
* Tyto a mnoho dalších voleb najdete v [Interface menu](./interface.md). 

## Deformátor Nafouknout nebo Špička {#inflate-or-peak-deformer}

Mnoho 3D aplikací má inflate deformer, který posune všechny vertexy podél jejich normály o nastavitelnou hodnotu. Nomad sice v současnosti deformery nemá, ale toto chování lze napodobit pomocí štětce Inflate:

* Vyberte štětec Inflate
* V [Stroke menu](./stroke.md#stroke) změňte metodu tahu na `Lock + Radius'
* Nastavte poloměr štětce větší než vaše socha, v případě potřeby oddalte kameru.
* Klikněte a táhněte tah po povrchu objektu; když je poloměr větší než objekt, celý tvar se rovnoměrně nafoukne o pevnou hodnotu.
* Upravte intenzitu štětce pro kontrolu množství „nafouknutí“.
* Použijte maskování, pokud potřebujete chránit nebo omezit efekt Inflate v určitých oblastech.

## Odstranění hrudek nebo „pupínků“ po operaci voxel remesh {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel remesh je skvělý pro vytváření rovnoměrně rozložených polygonů, ale někdy vytvoří topologii, která při vyhlazování způsobí malé hrbolky nebo pupínky. Například:

* Použijte štětec Crease na výchozí kouli a udělejte spirálu
* Voxel remesh s „build multiresolution at 3“
* Smooth s vysokou intenzitou
* objeví se artefakty (snáze viditelné s materiálem s vysokým kontrastem matcap):

![](/videos/tip_pimples_before.mp4)

Pro opravu pomocí sochaření zkuste volbu `Stable smoothing` v nastavení Smooth. Ta si poradí s nerovnoměrným rozložením topologie z voxel remeshe a dá čisté výsledky.

![](/videos/tip_pimples_stable_smooth.mp4)

Pro opravu samotné topologie použijte nový primitiv, nebo nástroje Quad Remesh, nebo externí 3D modeler a přeneste detaily z původního meshe na nový přes `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Denní osvětlení {#daylight-lighting}

Výchozí PBR render je, jak název napovídá, fyzikálně založený, což může podobně jako neupravená digitální fotografie vypadat trochu vybledle a ploše. Světla a post-processing v Nomadu lze použít k tomu, aby rendery vypadaly živěji.

Zde je výchozí render, podívejme se, zda ho můžeme vylepšit:
![](/images/tips_lighting_default.webp)

Zapnutí post-processingu a tonemappingu může přidat jas a kontrast:

![](/images/tips_lighting_tonemap.webp)

Abychom se zaměřili na světla: výchozí environment light je dobré pro sochaření, ale pro finální render lze vylepšit. Jedním ze způsobů, jak o tom přemýšlet, je oddělit přímé světlo (např. slunce) od environment light (např. světlo z modré oblohy, země). Snížením environment light a jeho otočením začneme zachycovat, jak by osvětlení vypadalo, kdyby byl objekt ve stínu:

![](/images/tips_lighting_env.webp)

Lze přidat přímé světlo a zvýšit jeho intenzitu pro simulaci ostrého slunečního světla. Vyvážením tohoto světla s environment light dosáhnete příjemného výsledku:

![](/images/tips_lighting_sunlight.webp)

Postavám může prospět přepnutí materiálu na subsurface a umístění spotlightu za postavu mířícího na uši, aby zářily:

![](/images/tips_lighting_sss.webp)

Pak experimentujte se zbytkem post-process nastavení! Global Illumination a Ambient Occlusion pomáhají s realističtějším osvětlením. Curvature a Sharpen mohou pomoci zvýraznit detaily sochy. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette pomáhají simulovat kamerové efekty. Všimněte si, že jak zapínáte další funkce, je potřeba upravit osvětlení a ostatní post-process hodnoty, aby to kompenzovaly.

Zde je render s plnou sadou post-process úprav:
![](/images/tips_lighting_final.webp)
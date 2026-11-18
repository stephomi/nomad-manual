# ![](/icons/manual.webp) Tipy {#tips}

[[toc]]

## Jak začít model {#how-to-start-a-model}

Začátečníci v 3d sochání se často ptají, jak nejlépe začít model. Žádný nejlepší způsob neexistuje, každému vyhovuje něco jiného. Tady jsou některé z nejběžnějších postupů.

### Sochání na kouli, multirezoluce {#sculpt-on-sphere-multires}

Nejběžnějším způsobem je výchozí model, se kterým se Nomad spustí. Nástroji přesunout, hlína a rýha kouli tlačíte a táhnete do požadovaného tvaru. Nižší úrovně subdivize použijte, když chcete rychle udělat velké změny, vyšší úrovně subdivize na práci s detaily.

Častým problémem je, že vám polygony dojdou tam, kde je potřebujete, zatímco jinde jich máte příliš. Když například z výchozí koule vytvarujete celé tělo, nejspíš nebudete mít dost detailů na prsty, zatímco na zadní straně hlavy bude spousta zbytečných polygonů. U převážně kulovitých tvarů, jako je hlava, to ale může být v pořádku.

### Dyntopo {#dyntopo}

Se zapnutou dynamickou topologií (Dyntopo) se polygony při sochání adaptivně přidávají a odebírají. Tyto polygony jsou trojúhelníky a začátečníkům se jejich neuspořádané rozložení často nelíbí ve srovnání s čistým vzhledem multirezoluce. Vytrvejte, vyplatí se to! Když zapnete hladké stínování, vypnete drátový model a přestanete se rozložením trápit, může tento režim působit velmi podobně jako práce s hlínou. Nezapomeňte, že s velkým štětcem nebo s vyhlazovacím štětcem tento režim polygony také odebírá, takže nástroj zůstává vždy rychlý a pohotový. Až budete mít hotovou první verzi sochy, můžete ji naklonovat, projet ji Quad Remesherem pro pěkné rozložení a původní detaily přeprojektovat na vysokou úroveň subdivize.

### Voxelové přesíťování {#voxel-remesh}

Voxelové přesíťování vytvoří na vaší soše topologii založenou převážně na čtyřúhelnících. Při nižších rozlišeních je tato operace rychlá a můžete s ní rychle nahradit roztažené nebo příliš husté polygony rovnoměrně rozloženými. Je to skvělý způsob, jak z koule začít celé tělo: začnete například hlavou, vytáhnete krk a přesíťujete. Vytáhnete tělo, přesíťujete, paže, přesíťujete a tak dál, dokud nemáte základní tvary.

### Použijte více objektů {#use-multiple-objects}

Mnoho příruček anatomie zobrazuje tělo pomocí jednoduchých koulí, válců a krychlí. Stejně tak můžete sochat i v Nomadu. Výhodou je, že objekty můžete v hierarchii scény vnořit do sebe, takže když například otočíte krkem, hlava ho bude následovat. Velmi užitečné je také přesné posouvání, otáčení a změna měřítka nástrojem gizmo a pro každý tvar můžete nastavit otočný bod, aby se pohyboval přesně podle vašich představ. Až budou základní bloky na správném místě, můžete je všechny vybrat a voxelovým přesíťováním nebo booleovskou operací je spojit do jediného povrchu pro podrobnější sochání.

Šikovný tip pro tento způsob práce: začněte koulí, změňte její měřítko na protáhlou klobásu, stiskněte otočný bod, klepněte na „dole“ a znovu stiskněte otočný bod. Teď máte část těla, kterou můžete naklonovat, posunout po délce první koule, naklonovat, otočit, naklonovat, posunout, naklonovat atd., a rychle tak rozvrhnout tělo.

### Trubky {#tubes}

Nástroj trubka je skvělý způsob, jak začít sochu. Plazí ocasy, paže, nohy, prsty, obočí, to vše můžete nástrojem trubka rychle načrtnout a pak snadno upravit. Umožňuje také měnit profil průřezu, takže tvar změníte rychle. Tvar můžete potvrdit a začít na něm sochat, a spolu s dalšími objekty ho voxelově přesíťovat, abyste získali síť celého těla.

### Použijte jiné aplikace {#use-other-apps}

Někdo raději začíná model v jiných aplikacích, i to je v pořádku. Nástroje jako Blender nebo Valence umožňují začít model technikami low poly a pak ho importovat do Nomadu k sochání.

### Použijte vestavěná přednastavení {#use-the-built-in-presets}

V nabídce [Soubory](files.md) klepněte na `Přednastavení…` vlevo v části projektu. Najdete tu několik přednastavených tvarů hlav a těl od Blender Foundation. Vyberte si jeden, klepněte na něj znovu a přidejte ho do scény. 

### Použijte modely z internetu {#use-online-models}

Na internetu je k dispozici spousta bezplatných modelů, například na polyhaven, sketchfab nebo turbosquid. Tyto modely obvykle můžete importovat do Nomadu a buď na nich přímo sochat, nebo je použít jako referenci.

### Žádná pravidla! {#no-rules}

Nakonec můžete tyto techniky libovolně kombinovat, nebo nepoužít žádnou! Nomad je v tomto ohledu velmi flexibilní. Pokročilí uživatelé mohou začít trubkami, pak přejít na dyntopo, pak přidat stažené chodidlo, pak vše přesíťovat Quad Remesherem a nakonec použít multirezoluci na finální detaily. Cokoli, co vám vyhovuje.

## Skupiny ploch {#facegroups}

Nástroj skupina ploch se dá použít k mnoha věcem, jak vysvětluje toto video na youtube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Toto je textové shrnutí funkcí, o kterých video mluví.

### Proč skupiny ploch? {#why-facegroups}

Skupiny ploch vám umožňují uspořádat a vybírat plochy (v této příručce se „plochy“ a „polygony“ používají jako synonyma). Nejlépe se to vysvětlí ve srovnání s ostatními nástroji Nomadu pro výběr a uspořádání. V Nomadu můžete vytvářet objekty, pojmenovávat je a vnořovat, takže snadno vytvoříte strukturu objektů, která popisuje třeba místnost s podlahou, stěnami, židlí, stolem a tak dál.

U postavy můžete začít hrubým modelem ze samostatných objektů pro hlavu, paži a nohu, ale jakmile všechny části sloučíte do jedné sítě, tato struktura se ztratí. Na dílčích částech postavy můžete pracovat s maskami, ale znovu a znovu malovat masku na ruce, pak na nos, pak zase na ruce může být únavné.

Právě tady se skupiny ploch hodí. Umožňují označit polygony barvou a pak vybírat a upravovat polygony se stejnou barvou. Barva skupiny ploch a barva vrcholů jsou dvě různé věci.

Nejbližším přirovnáním je vybarvování mapy, kde pak můžete podle barvy vybírat státy nebo oblasti.

Na hlavách postav můžete vybarvit zóny, které označí oční důlky, nos, rty, bradu a uši, a později je snadno vybrat. Při hard surface a mechanickém sochání se zase hodí k vymezení panelů a sekcí.

### Vytváření a úprava skupin ploch {#creating-and-editing-facegroups}

Skupiny ploch můžete nanášet štětcem, kdy každý nový tah vytvoří novou skupinu ploch, nebo můžete vybrat skupinu ploch pod kurzorem a rozšířit ji. Vytvářet je lze také pomocí tvarů.

* Bod, výchozí režim - jedno tažení určí novou barvu skupiny ploch a přiřadí ji plochám, přes které táhnete. Každé nové tažení vytvoří novou skupinu ploch. Klepnutí vyplní celou souvislou oblast novou skupinou ploch.
* Bod, režim `Vybrat` - když je aktivní tlačítko `Vybrat` na levém panelu nástrojů, Nomad vybere skupinu ploch pod kurzorem a po zbytek tažení ji nanáší. Hodí se pro doladění skupin ploch, aniž byste je museli ručně vybírat.

### Maskování {#masking}

Když je aktivní nástroj maska a na jeho panelu nástrojů je aktivní tlačítko skupiny ploch, klepnutím na skupinu ploch ji zamaskujete.


### Skrývání {#hiding}

Když je aktivní nástroj skrýt a na jeho panelu nástrojů je aktivní tlačítko skupiny ploch, klepnutím na skupinu ploch ji skryjete.

### Uspořádání {#organizing}

Jak už bylo zmíněno, skupiny ploch můžete použít k uspořádání sítě, aniž byste museli vytvářet samostatné objekty. Hlavu asi nebudete chtít rozdělit na samostatné objekty pro nos, bradu a uši, ale mít je vymezené skupinami ploch je velmi užitečné.

### Oblasti UV {#uv-regions}

Nástroj UV Atlas se pokusí určit švy automaticky, ale někdy je umístí tam, kde je nechcete. Pokud má objekt skupiny ploch a ve volbách UV Atlas je zapnutá volba skupin ploch, použije místo toho jako UV švy hranice skupin ploch.

### Quad Remesher {#quad-remesher}

Plugin Quad Remesher obvykle vede hrany na modelu pěkně, ale když zapnete volbu skupin ploch, můžete ho skupinami ploch usměrnit. Snadno tak například vymezíte čistý tok hran kolem očí, nadočnicového oblouku, rtů nebo lícní rýhy.

### Filtrování s dalšími nástroji {#filter-with-other-tools}

Mnoho nástrojů má volby, se kterými berou ohled na skupiny ploch, buď přímo v nabídce nástroje, nebo v nabídce Tah -> Filtr. Například nástroj hladit při síle nad 100 % dokáže uvnitř skupiny ploch razantně vyhladit detaily, ale hranici skupiny ploch zachová víceméně neporušenou.

### Uvolnění a vyhlazení hranic skupin ploch {#relax-and-smooth-facegroup-borders}

Volba `Uvolnit` v nástroji skupina ploch výborně vyhlazuje hranice skupin ploch a ostatní prvky přitom zachovává. Je to skvělý způsob, jak před přesíťováním Quad Remesherem vymezit hladké hranice skupin ploch.

## Omezení na tabletu a mobilu {#limitations-on-tabletmobile}

Dnešní tablety a mobily jsou velmi výkonné, ale oproti stolním počítačům a notebookům mají důležité rozdíly:

### Žádné aktivní chlazení {#no-active-cooling}

Počítače mají ventilátory nebo velké chladiče, které je udržují v chladu, a jsou navržené pro provoz při vysokých teplotách. Mobilní hardware je obvykle navržený především tak, aby byl tenký, ne aby pomáhal chladit vnitřní součástky. Když Nomad poženete na nejvyšší nastavení kvality (režim osvětlení PBR, složité materiály, mnoho objektů, mnoho zapnutých efektů postprocesu), může se zařízení přehřát a baterie se velmi rychle vybije. 

Lepší je použít režim osvětlení matcap a nižší `Rozlišení vykreslování` (nahoře v nabídce postprocesu). Díky tomu zařízení zůstane chladné a můžete sochat déle.

### Omezená paměť {#limited-memory}

Nomad dosáhne výsledků srovnatelných s většinou desktopových aplikací pro sochání, ale fyzikální zákony neobejde! Většina stolních počítačů má dvakrát víc paměti než mobilní zařízení a pracovní stanice pro 3d animaci mají často 4x nebo 8x víc. Proto je dobré mít přehled, kolik polygonů používáte, a vyzkoušet na svém zařízení, kdy se začne zasekávat. Téměř všechna zařízení, na kterých Nomad běží, celkem snadno zvládnou 1 milion polygonů. M2 iPad Pro pohodlně zvládne 8 milionů a lidé na nejnovějších iPadech testovali i výrazně víc.

Jen ty nejdetailnější sochy ale potřebují víc než 4 miliony polygonů. Pokud vytváříte poměrně jednoduché objekty a často se dostáváte přes 500 000, 1 milion nebo 4 miliony, používáte příliš mnoho polygonů! Zkontrolujte, že máte v [Nastavení](settings.md) zapnuté `Hladké odstíny`.

### Systém je k náročným aplikacím méně shovívavý {#os-is-less-forgiving-with-intensive-apps}

Apple i Android očekávají, že aplikace budou malé soubory ukládat a načítat velmi rychle. Předpokládají také, že aplikace dokážou velmi rychle přepínat úlohy. Nomad sice používá chytré triky, aby soubory zůstaly poměrně malé a ukládaly se velmi rychle, ale pokud mobilní systém usoudí, že to Nomadu trvá příliš dlouho, prostě ho ukončí dřív, než úlohu dokončí. I to je důvod, proč držet soubory spíš menší. Pracovat se sochou o 37 milionech polygonů jde, jak hlásil jeden uživatel na discordu, ale nedoporučujeme to!

## Práce na malých obrazovkách {#working-on-small-screens}

Nomad je navržený pro tablety, ale dobře funguje i na telefonech. Sochání na malé obrazovce, jako je telefon, si můžete usnadnit několika úpravami rozhraní a pracovního postupu:

* Klepnutím 4 prsty skryjete nebo zobrazíte celé rozhraní, takže máte víc místa na sochání.
* Tažením 3 prsty nahoru a dolů změníte poloměr štětce
* Měřítko rozhraní můžete zmenšit, aby se vešlo víc tlačítek, pokud dobře vidíte, nebo zvětšit, pokud vidíte hůř!
* Širší nabídky mohou sochu někdy zakrývat. Můžete je nastavit jako průhledné a bez rozostření, abyste sochu pod nabídkou viděli.
* Pokud socháte prstem, použijte volbu [`Posun tahu`](stroke.md#stroke-offset), která posune střed štětce kousek od prstu.
* Tyto a mnoho dalších voleb najdete v [nabídce Rozhraní](./interface.md). 


## Deformátor nafouknutí nebo zašpičatění {#inflate-or-peak-deformer}

Mnoho 3d aplikací nabízí deformátor nafouknutí, který posune všechny vrcholy podél jejich normály o nastavitelnou vzdálenost. Nomad zatím deformátory nemá, ale toto chování můžete napodobit štětcem zvětšit:

* Vyberte štětec zvětšit
* V [nabídce Tah](./stroke.md#stroke) změňte způsob tahu na `Zámek + poloměr`
* Nastavte poloměr štětce větší, než je vaše socha, a v případě potřeby kameru od sochy oddalte.
* Klepněte na povrch objektu a táhněte tah. Když je poloměr větší než objekt, celý tvar se rovnoměrně nafoukne o pevnou hodnotu.
* Intenzitou štětce řídíte míru nafouknutí
* V případě potřeby použijte maskování, abyste v určitých oblastech účinku nafouknutí zabránili nebo ho zmírnili.

## Odstranění hrbolků a „pupínků“ po voxelovém přesíťování {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxelové přesíťování skvěle vytváří rovnoměrně rozložené polygony, ale někdy vytvoří topologii, na které se při vyhlazování objeví malé hrbolky nebo pupínky. Například:

* Na výchozí kouli udělejte štětcem rýha spirálu
* Proveďte voxelové přesíťování s `Vytvořit multirezoluci` na 3
* Vyhlaďte s vysokou intenzitou
* objeví se artefakty (lépe viditelné s kontrastním matcap materiálem):

![](/videos/tip_pimples_before.mp4)

Pokud to chcete opravit sochařsky, vyzkoušejte v nastavení hlazení volbu `Stabilní vyhlazení`. Ta si poradí s nerovnoměrným rozložením topologie po voxelovém přesíťování a dá čisté výsledky.

![](/videos/tip_pimples_stable_smooth.mp4)

Pokud chcete opravit samotnou topologii, použijte nové primitivum, nástroje quad remesh nebo externí 3d modelář a detaily z původní sítě přeneste na novou pomocí `Topologie -> Péct -> Přeprojektovat → Vrchol`. 

![](/videos/tip_pimples_reproject.mp4)

## Denní osvětlení {#daylight-lighting}

Výchozí PBR render je, jak název napovídá, fyzikálně založený, takže stejně jako neupravená digitální fotka může působit trochu vybledle a plochě. Světly a postprocesem v Nomadu můžete rendery oživit.

Tady je výchozí render, zkusme ho vylepšit:
![](/images/tips_lighting_default.webp)

Zapnutí postprocesu a mapování tónů přidá jas a kontrast:

![](/images/tips_lighting_tonemap.webp)

Co se týče světel, výchozí osvětlení prostředím je dobré na sochání, ale pro finální render se dá vylepšit. Můžete o tom uvažovat tak, že oddělíte přímé světlo (třeba slunce) od světla prostředí (třeba světla z modré oblohy nebo od země). Když světlo prostředí zeslabíte a natočíte, začne vypadat jako osvětlení objektu, který stojí ve stínu:

![](/images/tips_lighting_env.webp)

Můžete přidat přímé světlo a zvýšit jeho intenzitu, aby napodobilo ostré sluneční světlo. Vyvážením se světlem prostředí dosáhnete příjemného výsledku:

![](/images/tips_lighting_sunlight.webp)

Postavám může prospět změna materiálu na podpovrchový a umístění bodového světla s kuželem za postavu, namířeného na uši, aby prosvítaly:

![](/images/tips_lighting_sss.webp)

Pak experimentujte se zbytkem nastavení postprocesu! Globální osvětlení a ambientní okluze pomáhají s realističtějším osvětlením. Zakřivení a zaostření mohou na soše vynést víc detailů. Chromatická aberace, hloubka ostrosti, zrno, bloom a vinětace pomáhají napodobit efekty fotoaparátu. Se zapínáním dalších funkcí je potřeba upravit osvětlení a ostatní hodnoty postprocesu, aby se to vyrovnalo.

Tady je render s kompletní sadou úprav postprocesu:
![](/images/tips_lighting_final.webp)

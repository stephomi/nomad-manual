# ![](/icons/sliders.webp) Gränssnitt {#interface-menu}

I den här menyn finns många alternativ för att anpassa Nomads gränssnitt.

![](/images/interface_overview2.webp)

Nomad går att anpassa på djupet. Menyn är uppdelad i 5 flikar: Gränssnitt, Kortkommandon, Gest, Bindningar och Debug.

![](/images/interface_menu.webp)


::: tip
Den här sidan handlar om menyn Gränssnitt, inte om själva gränssnittet! Gränssnittet i stort beskrivs i [Kom igång](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Gränssnitt {#interface}

Fliken Gränssnitt styr färg, storlek och layout för Nomads användargränssnitt. Den har två underflikar, `Utseende` och `Layout`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Färger {#presets}

![](/images/interface_presets.webp)

Underfliken `Utseende` börjar med en samling färgförval för gränssnittet. Tryck på ett för att använda det och finjustera det sedan med alternativen nedanför.

#### Accent och Bas {#color-widgetcolor-base}
Gränssnittets huvudfärger: `Accent` för valda knappar och skjutreglagens staplar, `Bas` för panelerna.

#### Textopacitet {#text-opacity}
Tonar ner text och ikoner mot panelerna.

#### Växlingsknappar, Kryssruta, Flikar {#high-contrast-button}
Stilen på växlingsknapparna (`Mjuk` eller `Fylld`), på kryssrutorna (`Kontur`, `Accent` eller `Fyllning`) och på flikarna (`Understrykning`, `Mjuk` eller `Fylld`).

#### Färgade verktyg {#colored}
Färgkodar ikonerna efter kategori, till exempel blir alla maskverktyg bruna, delningsverktygen röda, utplattningsverktygen gröna och så vidare.

#### Panelskugga {#material-color-preview}
Panelerna kastar en skugga så att de syns tydligare mot scenen.

#### Genomskinlig panel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
När det här är på dyker fler alternativ upp som styr hur menyer och paneler ser ut i Nomad: `Panelton` anger deras färg, `Suddstyrka` hur mycket scenen bakom dem suddas ut, och `Glas` lägger till ljusbrytning och högdagrar längs kanterna, mest synligt med låg suddighet.

::: tip
På små enheter kan det vara praktiskt att göra panelfärgen nästan vit, genomskinlig och med låg suddstyrka, så att menyerna inte skymmer scenen.
:::

#### ![](/icons/reset.webp) Återställ utseende {#reset-style}
Återställer alla utseendealternativ till standardvärdena.

### ![](/icons/panel_detach.webp) Layout {#layout}

Underfliken `Layout` bestämmer var saker sitter och hur stora de är.

#### Verktygslåda {#toolbox}

Alternativ för verktygsmenyn till höger i Nomads gränssnitt.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Ändra storlek {#ui-resize-corner}

Visar eller döljer ett handtag i verktygslådans nedre hörn för att ändra dess storlek.

##### Dold {#hidden}
Normalt växlar verktygslådans ikon i det övre fältet mellan en lång enkel kolumn och en lista med verktyg i flera kolumner. Med det här alternativet växlar den i stället mellan listan med flera kolumner och att vara dold.

##### Återställ ordning {#reset-order}
Återställer standardverktygen i verktygslådan till standardordningen. Anpassade ikoner finns kvar i verktygslådan, sist i listan.

#### Övre fält {#rows-auto-1}
`Responsiv` väljer vad det övre fältet gör när det inte får plats på skärmen, vilket mest spelar roll på små skärmar: `Flerradig` bryter menyerna på flera rader, `Skrolla` behåller en enda rad som du kan skrolla.

#### Spegelvänd toppfält {#mirror-top-bar}
Vänder på ordningen för menyerna i det övre fältet.

#### Spegelvänd sidofält {#mirror-side-bars}
Byter plats på sidofälten, så att verktygslådan hamnar till vänster och verktygsalternativen till höger.

#### Spegelvänd bottenfält {#mirror-bottom-bar}
Flyttar bottenfältet till det nedre högra hörnet och vänder på knapparnas ordning.

#### ![](/icons/move.webp) Dra panel {#drag-panel}
En flytande panel flyttas alltid genom att du drar i dess list, men det här alternativet låter dig dra i själva panelen också. Med `Auto` flyttar ett finger eller en stylus panelen bara när du drar mer vågrätt än lodrätt, så att ett lodrätt drag fortfarande skrollar innehållet. Ställ in `Ja` för att även kunna dra med musen, åt vilket håll som helst.

#### ![](/icons/pencil.webp) Använd Nomad-dialog {#use-nomad-dialog}
Visar Nomads egen textdialog i stället för systemets när du skriver in ett namn eller ett värde.

#### ![](/icons/stylus.webp) Hover-punkt {#hover-dot}
Visar en liten punkt i gränssnittet när en stylus som hovrar över skärmen upptäcks.

#### ![](/icons/help.webp) Hjälp-popup vid hovrande {#help-popup-on-hover}

På enheter som stödjer hovring väljer du här om den sammanhangsberoende hjälpen i Nomad, som visas med ikonen ![](/icons/help.webp), ska dyka upp när du hovrar eller bara när du klickar.

#### Övergripande skala {#overall-scale}
En storleksfaktor för alla delar av gränssnittet.
#### Panelbredd {#panel-width}
Bredden på menyer och paneler.
#### Teckensnittsskala {#font-scale}
Skalar teckensnitten.
#### Vertikalt mellanrum {#vertical-spacing}
Mellanrummet mellan elementen i menyer och paneler.
#### Vertikalt mellanrum (vänster) {#vertical-spacing-left}
Mellanrummet mellan elementen i det vänstra verktygsfältet.

#### Kantförskjutningar {#edge-offset}
Ändra bara de här värdena om du har problem med att trycka på knapparna vid skärmkanterna. Om reglagen är inaktiverade använder Nomad de värden för säkert område som enheten själv anger.

::: tip
När du flyttar Nomad till en ny enhet (till exempel byter från en iPhone 12 till en iPhone 15), se till att återställa kantalternativen till standardvärdena!
:::

#### ![](/icons/reset.webp) Återställ layout {#reset-layout}
Återställer alla layoutalternativ till standardvärdena.

## ![](/icons/window.webp) Kortkommandon {#shortcuts}

Fliken Kortkommandon väljer vilka snabbknappar som visas runt vyn, och låter dig bygga egna flytande verktygsfält.

### Sidofält {#side-bar}
Snabbknapparna för verktyg längst ner i det vänstra sidofältet: `Jämna ut`, `Mask`, `Dölj`, `Ytgrupp` och `Gizmo`. Dra i dem för att ändra ordningen.

### Bottenfält {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Tryck på ett kortkommando för att lägga till det i bottenfältet, eller för att ta bort det. De här är på som standard:
* `Ångra` - ångrar den senaste åtgärden
* `Gör om` - återställer den senast ångrade åtgärden
* `Solo` - Döljer tillfälligt alla andra objekt så att bara det markerade syns. Tryck igen för att visa alla objekt igen.
* `Röntgen` - Gör tillfälligt alla andra objekt halvgenomskinliga, så att bara det markerade är helt synligt. Tryck igen för att återställa standardmaterialen.
* `Voxel` - Gör en ny omnätning av det aktuella objektet med den senast använda voxelupplösningen. Ett långt tryck eller ett svep uppåt tar fram ett reglage för upplösningen och en knapp för skarpa kanter.
* `Rutnät` - Visar eller döljer rutnätet i vyn. Med ett långt tryck eller ett svep uppåt kan du ändra rutnätets färg och opacitet.
* `Wireframe` - Visar eller döljer ett wireframe-lager ovanpå modellen. Med ett långt tryck eller ett svep uppåt kan du ändra wireframens färg och opacitet.
* `Inspektera` - låter dig se egenskaper för din mesh, som UV:er, bakade texturer och andra egenskaper, ovanpå Nomads bakgrund.
* `Ytgrupp` - Visar eller döljer ytgrupperna, mer information under [Verktyg->Ytgrupp](tools.md#facegroup)

Andra vanliga kortkommandon finns också: `Kontur`, `Projektion` (perspektiv eller ortografisk), `MatCap`, `DynTopo`, samt knapparna `Dela upp`, `Omvänd` och nivåerna för [Multiresolution](topology.md#multiresolution).

#### ![](/icons/more.webp) Bindningar {#bindings-list}

Nästan alla funktioner i Nomad kan läggas till i bottenfältet via knappen för bindningar, som visar hur många kortkommandon fältet innehåller. När du klickar på knappen visas en meny med bindningar:

![](/images/interface_bindings_search.webp)

Du kan söka per kategori med ikonerna högst upp, eller använda sökfältet för att hitta funktioner efter namn. Klicka på en funktion för att lägga till den i verktygsfältet. Klicka igen för att ta bort den.

#### ![](/icons/eye_open.webp) Synlig {#order}

Visar eller döljer hela bottenfältet.

#### ![](/icons/reset.webp) Återställ {#reset}

Återställer bottenfältet till standardinställningarna.

### Flytande fönster {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Klicka på + för att lägga till ett flytande verktygsfält. Det syns inte förrän du klickat på knappen för bindningar och lagt till några kortkommandon i det, sedan kan du göra det synligt.

Du kan skapa många verktygsfält, och vart och ett har en rad med de här alternativen:

* Dra i handtaget till vänster på en rad för att ändra verktygsfältens ordning.
* `Namn` - Verktygsfältets namn.
* `Synlig` - Visar eller döljer verktygsfältet.
* `List` - Visar en titellist på verktygsfältet.
* `Minimerat` - Behåller verktygsfältet på skärmen när gränssnittet är minimerat.
* `Bindningar` - Öppnar fönstret med bindningar, där du väljer vilka funktioner som ska läggas till i eller tas bort från verktygsfältet.
* `Radera` - Raderar verktygsfältet.

## ![](/icons/gesture.webp) Gest {#gesture}
Menyn Gest styr hur ditt finger, din stylus, mus och styrplatta styr Nomad.

![](/images/interface_gesture.webp)

### Gestalternativ {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad kan begränsa åtgärder beroende på vilken inmatningsenhet du använder. Ett drag med fingret kan till exempel bara flytta kameran, medan ett drag med stylusen bara skulpterar. Har du en mus eller styrplatta kan den också tilldelas vissa åtgärder.

Varje rad är en åtgärd: slå på `Finger`, `Stylus` och `Mus` för att välja vilka enheter som kan utföra den.

* `Kamera` - Flyttar kameran.
* `Nodredigering` - Drar i handtagen som ritas i vyn, till exempel för att redigera en primitiv, en kurva, en repeterare eller ett ljus.
* `Skulptera` - Skulpterar med penslarna. Verktyg som har en egen rad nedanför följer den raden i stället.
* `Markera objekt` - Tryck på ett objekt för att markera det.
* `Materialval` - Håll intryckt i vyn för att hämta färgen eller materialet under markören. Det fungerar bara om den aktuella penseln har målning aktiverad.
* `På tryck` - Tryckgenvägarna för verktyg som Mask, Dölj och Ytgrupp (se nedan).
* `Måla` - Verktygen Måla och Smeta ut.
* `Mask` - Verktyget Mask.
* `Yta` - Verktygen Dölj och Ytgrupp.
* `Skapa` - Verktygen Rör, Svarv och Infoga.
* `Klipp` - Verktygen Beskär, Dela och Projekt.
* `Välj` - Verktygen Välj och Mät.
* `Gizmo` - Verktygen Gizmo och Galler.
* `Transformera` - Verktygen Transformera och Ordna.

::: tip
En vanlig inställning på en surfplatta är att bara låta stylusen skulptera och måla, och använda fingrarna till kameran. Då lämnar handflatan eller ett vilset finger aldrig ett penseldrag på modellen.
:::

### ![](/icons/tool_smooth.webp) Fingret slätar alltid ut {#finger-always-smooths}
När det här är på jämnar fingret alltid ut när ett skulpteringsverktyg är aktivt, oavsett pensel. Om du slår på det tas `Finger` bort från raden `Skulptera`, så att stylusen skulpterar och fingret jämnar ut.

### Tillåt drag utanför objekt {#allow-air-stroke}
Låter ett penseldrag börja även om markören först hamnar utanför meshen. Välj vilka verktyg det gäller: `Verktyg` (alla andra penslar), `Jämna ut`, `Mask` och `Dölj`. Det fungerar bara för enheter som kan skulptera men inte flytta kameran, så de här knapparna är inaktiverade tills någon av dina enheter är inställd så.

### ![](/icons/stroke.webp) Fäst penseldrag {#stroke-snap}
Håll pekaren stilla i slutet av ett penseldrag för att räta ut det till en rak linje eller en mjuk kurva. Fortsätt dra för att rotera och skala det fästa penseldraget runt dess startpunkt.

`Hålltid` anger hur länge du måste hålla stilla innan penseldraget fästs, eller innan en form växlar till redigering.

### ![](/icons/stylus.webp) Använd extra indatasamplingar {#use-extra-input-samples}
Använder de extra inmatningspunkter som enheten rapporterar. Stäng av det om dina penseldrag blir hackiga eller om trycket beter sig konstigt. Alternativet visas inte på iOS.

### ![](/icons/tool_mask.webp) Mask {#mask}

![](/images/interface_gesture_mask.webp)

`Enkeltapp kortkommandon` - Aktiverar de här kortkommandona med ett enda tryck, utan att du behöver hålla in maskknappen. Följande gester blir tillgängliga:
* tryck på bakgrunden för att invertera masken
* tryck på ett maskerat område för att göra masken suddigare
* tryck på ett omaskerat område för att göra masken skarpare

#### Håll intryckt {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Ett långt tryck med verktyget Mask växlar mellan maskpenseln och lassot (SelMask):
* `Håll intryckt - Skulptera` - Håll intryckt och fortsätt sedan dra: penseldraget ritas med det andra läget, och det föregående kommer tillbaka när penseldraget är klart.
* `Håll intryckt - Växla` - Håll intryckt och släpp utan att röra dig för att växla mellan de två.

### ![](/icons/tool_smooth.webp) Jämna ut {#smooth}
`Håll intryckt - Lasso` - Ett långt tryck med verktyget Jämna ut växlar till verktyget Välj så länge markeringsdraget pågår.

### ![](/icons/tool_hide.webp) Dölj {#hide}
![](/images/interface_gesture_hide.webp)

`Enkeltapp kortkommandon` aktiverar de här kortkommandona med verktyget Dölj:
* Tryck på en ytgrupp för att dölja den
* Tryck på en tom yta för att invertera de dolda polygonerna

### ![](/icons/finger3.webp) Tre fingrar {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Om din enhet stödjer gester med 3 fingrar kan du ställa in kortkommandon för den gesten här.

I alternativmatrisen kan du ge lodräta och vågräta drag olika kortkommandon, eller välja `Nej` för att stänga av dem. Observera att om samma gest väljs för 2 alternativ inaktiveras det ena, och dess namn stryks över.

* `Rotera belysning` - Roterar miljön, ljusen och matcap.
* `Verktygsradie` - Ändrar verktygets radie.
* `Verktygsintensitet` - Ändrar verktygets intensitet.

### ![](/icons/fingerprint.webp) Historik 2/3 {#history-23}
`Historikgenvägar` - när det här är på är följande gester aktiva:
* Ångra - tryck med 2 fingrar
* Gör om - tryck med 3 fingrar

`Håll intryckt` - när det här är på ångrar respektive gör du om snabbt i följd genom att hålla ner 2/3 fingrar.

### ![](/icons/mouse.webp) Mus hjul {#mouse-wheel}
`Hastighet (3d zoom)` anger hur snabbt hjulet zoomar vyn, och `Hastighet (2d gränssnitt)` hur snabbt det skrollar menyer och paneler. Minusknappen bredvid varje reglage vänder på riktningen.

### ![](/icons/fingerprint.webp) Styrplatta {#trackpad}
På en Mac väljer `Två fingrar` vad två fingrar på styrplattan gör. Att nypa zoomar alltid och att vrida rullar alltid vyn.
* `Av` - Att skrolla med två fingrar zoomar, som mushjulet. Fingrarna läses inte av var för sig.
* `Panorera` - Två fingrar panorerar vyn, och om du lyfter det ena roterar du runt. Samma som på en surfplatta.
* `Rotera` - Två fingrar roterar runt vyn, och om du lyfter det ena panorerar du.

### Tillgänglighet {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Hjälpfönster` tar fram ett flytande verktygsfält för att styra dra, nypa, rulla och kameraåtgärder.

### Kamera {#camera}
En genväg till menyn `Kamera` (kameraalternativen låg tidigare här men har flyttats till kameramenyn).

### Pennans dubbeltryck -> Bindningar {#pencil-tap}

En genväg till menyn `Bindningar`, där du ställer in vad dubbeltrycket på Pencil gör. Utanför iOS står det `Pennknapp → Bindningar`, för stylusens knapp.

### Handflatsavvisning {#palm-rejection}
På telefoner och surfplattor ignoreras beröringar vars kontaktyta är större än `Maxstorleksgräns`, som handflatan när den vilar mot skärmen. Det fungerar kanske inte på alla enheter, så stäng av det om du har svårt att arbeta i vyn.


## ![](/icons/keyboard.webp) Bindningar {#bindings}
Kortkommandon för tangenter och knappar ställs in i menyn Bindningar:

![](/images/interface_bindings.webp)
Nästan alla funktioner i Nomad kan kopplas till kortkommandon om din enhet har ett tangentbord, eller till extra knappar på din stylus, eller till och med till handkontroller.

Skapa en bindning genom att klicka på rektangeln bredvid funktionen och trycka på tangenten eller knappen.

Hitta funktioner med kategoriikonerna högst upp, eller sök efter namn i sökfältet.

Enskilda bindningar kan inaktiveras med kryssrutan bredvid bindningens namn. Håll intryckt på kryssrutan och dra för att ändra ordningen i listan.

När två aktiva bindningar använder samma kortkommando visas en ![](/icons/help.webp)-ikon bredvid dem, med en lista över funktionerna som krockar.

### ![](/icons/more.webp) Snabbmeny {#context-menu}
Ikonen ![](/icons/more.webp) efter varje bindning öppnar en snabbmeny:

![](/images/interface_bindings_context.webp)

* `Klona` - Klonar bindningen, till exempel för att ge en funktion ett andra kortkommando.
* `Återställ` - Återställer bindningen
* `Radera` - Raderar bindningen. Går bara när funktionen har mer än en bindning.

Under dem har vissa bindningar extra alternativ:

* `Låsta tangenter` - För verktygsgenvägar och snabbgenvägarna (Mask, Jämna ut, Gizmo, Dölj, Ytgrupp, Lägg till/Subtrahera) väljer du hur ett tangenttryck byter verktyg. `Auto` använder standardvärdet som är inställt bland de [avancerade](#advanced) alternativen.
  * `Håll` - Håll ner tangenten för att använda verktyget, släpp den för att gå tillbaka till föregående verktyg.
  * `Växla` - Tryck en gång för att byta verktyg.
  * `Snabbtryck` - Håll ner för att använda verktyget tillfälligt, eller tryck snabbt för att byta till det.
* `Återgå vid släpp` - För snabbgenvägar väljer du om du alltid går tillbaka till föregående verktyg när du släpper en nedhållen tangent, även när det verktyget redan var aktivt.
* `Växla föregående verktyg` - För verktygsgenvägar: trycker du på kortkommandot för det aktuella verktyget byter du tillbaka till det senaste verktyget. Kräver att `Låsta tangenter` står på `Växla` eller `Snabbtryck`.
* `Position` - För kortkommandon till flytande fönster: öppna fönstret där det var (`Behåll tidigare`) eller under markören (`På markören`).
* `Förflyttning (vid släpp)` / `Zoomning (vid släpp)` - För kamerans bindningar för zoom och panorering: byt till den andra när du släpper tangenten.
* Dragriktning - För `Rotera belysning`, `Verktygsradie` och `Verktygsintensitet` väljer du ett vågrätt eller lodrätt drag.
* `Synka` - För funktioner som lägger till, klonar eller instansierar objekt väljer du om resultatet ska synkas. Som standard används synkvärdet som är inställt i menyn Scen.
* `På bakgrund` - För snabbgenvägarna Jämna ut och Mask: dra på bakgrunden medan du håller ner tangenten för att rita ett lasso, ett markeringslasso för Jämna ut och ett masklasso för Mask.
* `Tvinga kamera` - För kamerabindningarna: flytta kameran även om samma kortkommando också används av en annan bindning, oftast ett verktygskortkommando eller Lägg till/Subtrahera.
* `Linjär rullning` - För bindningen som rullar vyn: rulla med ett vågrätt, lodrätt eller diagonalt drag i stället för att röra dig runt pivoten.

::: tip
Med `Snabbtryck` gör en enda tangent båda sakerna: håll den nere för att snabbt jämna ut eller maskera, så är du tillbaka på din pensel när du släpper, eller tryck snabbt för att stanna kvar i det verktyget.
:::

### ![](/icons/cog.webp) Avancerat {#advanced}
Längst ner i menyn Bindningar finns en kugghjulsmeny med avancerade alternativ:

![](/images/interface_bindings_advanced.webp)

* `Snabba genvägar` - Standardvärdena för `Låsta tangenter` och `Återgå vid släpp` för kortkommandona Mask, Jämna ut, Gizmo, Dölj, Ytgrupp och Lägg till/Subtrahera.
* `Verktygsgenvägar` - Standardvärdena för `Låsta tangenter` och `Växla föregående verktyg` för verktygsgenvägarna. Med `Växla föregående verktyg` kan du hela tiden växla mellan två verktyg med samma snabbtangent.
* `Genvägsfönster` - Läget för `Låsta tangenter` för de kortkommandon som visar de flytande fönstren.
* `Vänd zoom Y` - Inverterar den lodräta dragriktningen när du zoomar med en bindning.
* `Linjär rullning` - Rullar vyn med ett vågrätt, lodrätt eller diagonalt drag i stället för att röra dig runt pivoten.
* `SpaceMouse` - Aktiverar stöd för 3Dconnexion SpaceMouse. På vissa system dyker extra alternativ upp: vad den flyttar (`Objekt`, `Kamera`, `Första person`, `Drönare`), `Uppdatera pivot automatiskt` för att flytta pivoten till ytan under markören när den börjar röra sig, samt hastigheterna för `Förflyttning`, `Zoomning` och `Rotation`.
* `Dödzoner (drift)` - För kontrollerna `Gamepad`, `Joystick` och `Knapp`. Höj de här värdena om kameran rör sig när kontrollen ligger orörd.
* `Verktygsradie` - Hur ett drag med radiebindningen ändrar penselns storlek (`Cirkel`, `Mitten` eller `dx`), och sedan hur mycket radiebindningarna lägger till (i pixlar) eller multiplicerar med vid varje tryck.
* `Verktygsintensitet` - Hur mycket intensitetsbindningarna lägger till eller multiplicerar med vid varje tryck.
* `Kamera - Hastighet` - Hastigheten för `Förflyttning` och `Rotation` för de bindningar som panorerar och roterar vyn.
* `Återställ bindningar` - återställer alla bindningar till standardvärdena.
* `Återställ ordning` - återställer standardordningen i listan med bindningar.


## Visa kortkommandon med ⌘ på iOS {#ios-keyboard-shortcuts-display}

På iOS-enheter med tangentbord håller du ner ⌘ (cmd) för att visa en lista med kortkommandon.

Tangentbordsstödet på Android är fortfarande lite experimentellt.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
Här finns några experimentella alternativ och felsökningsalternativ. Många av dem bör stå kvar på standardvärdena och bara ändras efter kontakt med Nomads support. Ikonerna högst upp hoppar till respektive avsnitt.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalisera UVs` - Nomad normaliserar UV:erna för den markerade meshen så att de hamnar inom rutan [0-1].

### ![](/icons/sun.webp) Skuggning {#render}
* `Skriv brytningsdjup (baksida)` - Baksidan av meshar med ljusbrytning skrivs till djupbufferten.
* `Vinkelviktade mjuka normaler` - En justering av hur mjuk skuggning fungerar, som i vissa fall kan undvika veck.

### ![](/icons/speed.webp) Mål FPS {#target-fps}
När det här är av synkar Nomad antalet bilder per sekund med skärmens uppdateringsfrekvens.

När det är på kan du själv ställa in hur många bilder per sekund Nomad ska rendera.

### ![](/icons/window.webp) Gränssnitt {#debug-interface}
* `Verktygslåda: visa alla` - Nomad döljer verktyg som inte är relevanta för den aktuella markeringen, till exempel döljs alla skulpteringspenslar på primitiver som inte är slutförda. Med det här alternativet tonas inaktiverade verktyg ner i stället för att döljas.

De andra gränssnittsalternativen som låg här tidigare finns nu i fliken [Gränssnitt](#interface).

### ![](/icons/turntable.webp) Vridbord {#gif-turntable}
Nomad kan exportera ett vridbord som animerad gif. Observera att kvaliteten blir låg på grund av gif-formatets begränsningar. Skärminspelning är oftast ett bättre sätt.

* `Varaktighet` - hur många sekunder vridbordet ska vara
* `Maximal bildprovering` - Många av Nomads renderingseffekter av hög kvalitet kommer från att flera bildrutor kombineras. Det här reglaget anger hur många bildrutor som ska kombineras, och kryssrutan slår på eller av det.
* `Rotationscenter` - vad kameran roterar runt: `Behåll nuvarande` behåller den aktuella pivoten, `(0, 0, 0)` använder världens mittpunkt, `Scen` scenens mittpunkt.
* `Transparent bakgrund` - Använder genomskinlighet för gif-filen. Observera att gif bara stödjer 1 bits genomskinlighet, så kanterna kan bli kraftigt hackiga.
* `Exportera (GIF)` - startar exporten av gif-filen.

### ![](/icons/postprocess.webp) Efterbehandling {#post-process}
* `Filtrering` - Felsökningsalternativ
* `Format` - Felsökningsalternativ
* `Återanvänd buffertar` - Felsökningsalternativ

### ![](/icons/ram.webp) Prestanda {#performance}
* `Flertrådat: allmänt` - Felsökningsalternativ
* `Flertrådat: skulptering` - Felsökningsalternativ
* `Rita upprepningar som instanser` - Ritar alla kopior från en repeterare i ett enda ritanrop. Felsökningsalternativ.

### ![](/icons/star.webp) Funktion {#feature}
* `nom: komprimera multires` - Minskar storleken på projekt och Nomad-exporter som använder multiresolution. De här filerna kan inte öppnas i äldre versioner av Nomad. Alternativet kan komma att tas bort och vara på som standard i framtiden.
* `Vänd fyrhörningens diagonal (vid tryck)` - Felsökningsalternativ

### ![](/icons/bug.webp) Debug {#dev}
* `Loggar` - Öppnar en loggvy
* `Log events` - Skriver dina pekarhändelser (finger, stylus, mus) till loggvyn, för att felsöka problem med inmatningen.
* `FPS` - lägger till en räknare för bilder per sekund i vyns statistik.
* `Appbetygsruta` - Felsökningsalternativ, på iOS och Android.

### ![](/icons/image.webp) Anpassade ikoner {#custom-icons}
Ersätt Nomads ikoner med dina egna png-filer.
* `Importera ikoner` - Importerar png-filer till `tmp_session/icons`. Var och en ersätter grundikonen med samma namn. De försvinner när Nomad startas om.
* `Exportera verktygsikoner` - Kopierar grundikonerna `tool_<tool>.png` till `tmp_session/icons`, utan att skriva över något. Där kan du redigera dem och sedan använda dem med `Ladda om ikoner`.
* `Ladda om ikoner` - Använder ikonerna från `tmp_session/icons`.

### Quad-omnätning {#quad-remesh}
Alternativen för quad-omnätning finns inte längre i den här menyn: se [Quad-omnätning](topology.md#quad-remesh-instant) i menyn Topologi och verktyget [Quad Remesher](tools.md#quad-remesher).

### Skapa butikens miniatyrer {#make-store-thumbnails}
Renderar skärmbilder i storlekar som passar App Store för iOS.

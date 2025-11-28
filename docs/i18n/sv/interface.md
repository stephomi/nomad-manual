# ![](/icons/interface.webp) Meny för gränssnitt {#interface-menu}

Den här menyn styr många alternativ för att anpassa Nomads gränssnitt. 

![](/images/interface_overview2.webp)

Nomad kan anpassas på en ganska djup nivå, den här menyn är uppdelad i 4 sektioner: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Den här sidan handlar om gränssnittsmenyn, inte själva gränssnittet! Det övergripande gränssnittet beskrivs i [Komma igång](gettingstarted.md).
:::

## Gränssnitt {#interface}

Interface-sektionen låter dig lägga till genvägar, skapa flytande verktygsfält och styra färg, storlek och utseende på Nomads användargränssnitt.

![](/images/interface_overview3.webp)

### Lägg till genvägar (botten)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Det nedre verktygsfältet har dessa genvägar aktiverade som standard:
* `Undo` - ångra föregående åtgärd
* `Redo` - återställ den senast ångrade åtgärden
* `Solo` - Dölj tillfälligt alla andra objekt, så att endast det valda är synligt. Tryck igen för att återställa alla objekt.
* `X-ray` - Gör tillfälligt alla andra objekt halvtransparenta, så att endast det valda är solitt. Tryck igen för att återställa standardmaterialen.
* `Voxel remesh` - Remesha det aktuella objektet med den senast använda voxelupplösningen. En lång tryckning eller en svepning uppåt visar en reglage för upplösning och en växel för skarpa kanter.
* `Grid` - Växla visningsrutnätet. En lång tryckning eller en svepning uppåt låter dig ändra färg och opacitet på rutnätet.
* `Wireframe` - Växla en wireframe-overlay. En lång tryckning eller svepning uppåt låter dig ändra färg och opacitet på wireframen.
* `Inspector` - låter dig visa egenskaper för ditt mesh som uv:n, bakade texturer och andra egenskaper, överlagrade på Nomads bakgrund.
* `Face Group` - Växla facegroup-overlay, mer info under [Tools->FaceGroup](tools.md#facegroup) 

Andra vanliga genvägar finns tillgängliga från den här menyn, många fler finns i bindings-knappen.

#### ![](/icons/more.webp) Bindningar {#bindings-list}

Nästan varje funktion i Nomad kan läggas till i genvägsfältet via bindings-knappen. En bindings-meny visas när knappen klickas:

![](/images/interface_bindings_search.webp)

Du kan söka efter kategori via ikonerna högst upp, eller använda sökfältet för att hitta funktioner efter namn. Klicka på en funktion för att lägga till den i verktygsfältet. Klicka igen för att ta bort den.

#### ![](/icons/list.webp) Ordning {#order}

Detta visar en lista över genvägarna. Håll ned länge och dra för att ändra ordningen på genvägarna.

#### ![](/icons/reset.webp) Återställ {#reset}

Reset återställer det nedre verktygsfältet till standardinställningarna.

### Lägg till genvägar (fönster)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Genom att klicka på + lägger du till ett flytande verktygsfält. Det kommer inte att vara synligt förrän du klickar på bindings-knappen och lägger till några genvägar till det, sedan kan du göra det synligt. 

Du kan skapa många verktygsfält, varje verktygsfält har följande alternativ i den här menyn:

* ![](/icons/checked.webp) `Visible` - Växla synlighet för verktygsfältet
* ![](/icons/more.webp)`Bindings` - Visa bindings-fönstret för att välja funktioner att lägga till eller ta bort från verktygsfältet.
* ![](/icons/list.webp)`Order` - Visa en meny för att ändra ordningen på verktygsfältet.
* ![](/icons/reset.webp) `Reset` - Återställ verktygsfältet till dess standardläge.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Växla ett storleksändringshandtag i verktygsfältets nedre högra hörn.
* ![](/icons/sort_down.webp) `Collapsable` - Växla ett kollapshandtag i det övre högra hörnet.
* ![](/icons/trash.webp) `Delete` - Ta bort verktygsfältet.

### Verktygslåda {#toolbox}

Alternativ för verktygsmenyn till höger i Nomads gränssnitt.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Hörn för UI‑storlek {#ui-resize-corner}

Växla ett storleksändringshandtag i verktygsfältets nedre hörn.

#### Dold {#hidden}
Normalt växlar toolbox-ikonen i toppraden mellan en lång enkel kolumn eller en flerkolumnslista med verktyg. Det här alternativet växlar mellan flerkolumnslistan eller att vara dold.

#### Färgad {#colored}
Färgkoda ikonerna efter kategori, t.ex. alla mask-verktyg är bruna, split-verktyg är röda, flatten-verktyg gröna osv.

#### Rader: Auto (>1) {#rows-auto-1}

#### Återställ ordning {#reset-order}
Återställ standardverktygen i toolboxen till standardordningen. Anpassade ikoner finns kvar i toolboxen i slutet av listan.


### Förval {#presets}

![](/images/interface_presets.webp)

En samling färgförinställningar för gränssnittet.

#### Högkontrastknapp {#high-contrast-button}
En alternativ stil för knappar som gör dem mer synliga när de är aktiverade. Om den är inställd på Auto använder Nomad det här läget när UI-färgkontrasten mellan aktiverad/inaktiverad är låg.

#### Färgkontroll/Färgbas {#color-widgetcolor-base}
De primära färgerna som används i gränssnittet.

#### Transparent panel, Färgpanel, Oskärpestyrka {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
När detta är aktiverat visas extra alternativ för att styra hur menyer och paneler ser ut i Nomad. Deras färg, transparens och oskärpemängd kan justeras.

::: tip
På små enheter kan det vara användbart att göra färgpanelen nästan vit, transparent och med låg blur strength, så att menyer inte skymmer scenen.
:::

----

### Spegla översta raden {#mirror-top-bar}
Vänd ordningen på menyerna i toppraden.

### Spegla sidopaneler {#mirror-side-bars}
Byt sidofält så att toolboxen är till vänster och verktygsalternativen till höger.

### Spegla nedersta raden {#mirror-bottom-bar}
Flytta den nedre raden till det nedre högra hörnet och vänd knappordningen

### Förhandsvisning av materialfärg {#material-color-preview}
När du väljer en färg för ett material visas en förhandsvisning av detta material på det markerade objektet.

----
### Hjälpruta vid hovring {#help-popup-on-hover}

För enheter som stöder hover, styr om kontexthjälpen i Nomad, representerad med ikonen ![](/icons/help.webp), ska visas vid hover eller endast när den klickas.

----

### Total skala {#overall-scale}
En storleksmultiplikator för alla UI-element.
### Panelbredd {#panel-width}
Bredden på menyer och paneler.
### Teckenstorlek {#font-scale}
Skala typsnitten.
### Vertikalt avstånd {#vertical-spacing}
Avståndet mellan element i menyer och paneler.
### Vertikalt avstånd (vänster) {#vertical-spacing-left}
Avståndet mellan element i det vänstra verktygsfältet.

----

### Kantmarginal {#edge-offset}
Du bör bara ändra dessa värden om du har problem med att interagera med knapparna vid skärmens kanter. Om dessa reglage är inaktiverade använder Nomad de säkerhetsmarginaler (safe area) som enheten själv rapporterar.

::: tip
När du migrerar Nomad till en ny enhet (t.ex. byter en iPhone 12 mot en iPhone 15), se till att återställa edge-alternativen till standard!
:::

### Återställ stil {#reset-style}
Återställ alla UI-element till deras standardvärden.


## Gester {#gesture}
Gesture-menyn styr hur penna- och fingertryckningar styr Nomad.

![](/images/interface_gesture.webp)

### Gestalternativ {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad kan begränsa åtgärder baserat på inmatningsenhet. Till exempel kan en fingerdragning bara flytta kameran, medan en penn-dragning bara kan skulptera. Om du har en mus eller styrplatta kan den också tilldelas att styra specifika åtgärder.

Nomad låter dig för närvarande ställa in dessa lägen att styras av valfri kombination av finger-, penna- eller musgester:

* Camera
* Sculpt
* Gizmo
* Material picking (via en lång tryckning)
* Select object


`Finger always smooths` - Smooth kan ställas in att bara fungera med en fingerdragning.

### ![](/icons/tool_mask.webp) Mask {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Aktivera följande one-tap-genvägar utan att behöva hålla mask-knappen nedtryckt. Det möjliggör följande gester:
* tryck på bakgrunden för att invertera masken
* tryck på ett maskat område för att sudda (blur) masken
* tryck på ett omaskat område för att skärpa masken

### Växla Mask <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Lång tryckning växlar mellan Mask och SelMask och startar ett nytt penseldrag. I slutet av draget återväljs det föregående verktyget. 
* `Tool` - Lång tryckning och släpp utan att röra sig för att växla mellan Mask och SelMask. 

### ![](/icons/tool_hide.webp) Dölj {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` aktiverar följande genvägar med hide-verktyget:
* Tryck på en face group för att dölja den
* Tryck i tomt utrymme för att invertera de dolda polygonerna

### ![](/icons/finger3.webp) Tre fingrar {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Om din enhet stöder 3-fingersgester kan du konfigurera genvägar för den gesten. 

Alternativmatrisen låter dig definiera vertikala och horisontella dragningar som separata genvägar. Observera att om samma gest väljs för 2 alternativ kommer ett av dem att inaktiveras.

* `Rotate lighting` - Rotera environment, ljus och Matcap.
* `Tool Radius` - Ändra verktygsradien.
* `Tool Intensity` - Ändra verktygsintensiteten. 

### ![](/icons/fingerprint.webp) Historik 2/3 {#history-23}
`History shortcuts` - när detta är aktiverat är följande gester aktiva:
* Undo - tryck med 2 fingrar
* Redo - tryck med 3 fingrar

`Long press` - när detta är aktiverat kommer att hålla 2/3 fingrar nedtryckta snabbt att ångra/göra om.

### Tillgänglighet {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` visar ett flytande verktygsfält för att styra drag, nyp (pinch), rullning och kamerarörelser.

### Kamera {#camera}
En genväg för att gå till `Camera`-menyn (kameraalternativ fanns tidigare här, men har flyttats till kameramenyn).

### Dubbeltapp med Pencil -> Bindningar {#pencil-tap}

En genväg för att gå till `Bindings`-menyn (alternativ för Pencil-tap och double tap fanns tidigare här, men har flyttats till bindings-menyn).


## Bindningar {#bindings}
Tangentbords- och knappgenvägar kan definieras från bindings-menyn:

![](/images/interface_bindings.webp)
Nästan alla funktioner i Nomad kan bindas till tangentbordsgenvägar om din enhet har ett tangentbord, eller till extra knappar på din penna, eller till och med spelkontroller.

För att skapa en binding, klicka på rektangeln bredvid funktionen och tryck på tangenten/knappen. 

Hitta funktioner via kategoriikonerna högst upp, eller via sökfältet för att hitta efter namn. 

Enskilda bindings kan inaktiveras via kryssrutan bredvid binding-namnet.

### ![](/icons/more.webp) Snabbmeny {#context-menu}
Ikonen ![](/icons/more.webp) efter varje binding visar en snabbmeny:

![](/images/interface_bindings_context.webp)

* `Clone` - Klona bindingen
* `Reset` - Återställ bindingen
* `Delete` - Ta bort bindingen
* `Toggle shortcut on key tap` - Konfigurera om ett tryck kontra en lång tryckning ska behandlas olika. När detta är aktiverat kommer ett tryck att aktivera verktyget. En lång tryckning aktiverar verktyget endast medan tangenten hålls ned, när den släpps återgår det till föregående verktyg. Kallas ibland ”sticky keys” i andra 3D-appar.

### Avancerat {#advanced}
Längst ned i bindings-menyn finns en kugghjulsmeny för avancerade alternativ:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Ett tryck på standardgenvägarna för mask, smooth, gizmo, hide, sub växlar till det läget, men att hålla tangenten nedtryckt växlar till det läget och när tangenten släpps återgår läget till föregående läge. Kallas ibland ”sticky keys” i andra 3D-appar.
* `Toggle tool shortcuts` - När du använder en av verktygsgenvägarna, om samma genväg trycks två gånger, växlar den till föregående verktyg. På så sätt kan du växla mellan två verktyg med samma snabbtangent.
* `Invert Y (Zooming)` - Inverterar zoomen
* `Reset bindings` - återställ alla bindings till standardvärdena.


## iOS ⌘ Tangentbordsgenvägar {#ios-keyboard-shortcuts-display}

På iOS-enheter med tangentbord, håll ned ⌘ (cmd)-tangenten för att visa en lista över genvägar.

Android-tangentbordsstöd är lite experimentellt.

![](/images/shortcuts.webp)


## Felsökning {#debug}
Vissa experimentella och debug-alternativ finns i den här menyn. Många av dessa alternativ bör lämnas på sina standardvärden och endast ändras efter kontakt med Nomad-support.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad normaliserar UV:erna inuti [0-1]-tilen.

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Aktivera instant remesh-algoritmen
* `Quadriflow` - En alternativ quad remesh-metod.

### Rendering {#render}
* `Heightmap` - Ändra viewporten till att rendera scenens djup. Detta kan användas för att skapa alpha maps att använda för penslar.
* `Refraction write depth (back)` - Baksidan av refraktionsmesh kommer att skrivas till depth-buffern.
* `Flip Y (normal map)` - Invertera y-kanalen vid bakning av normal maps, krävs för vissa spel- och render-motorer.
* `Angle weighted smooth normals` - En justering av hur smooth shading fungerar som kan undvika veck i vissa fall.

### Mål‑FPS {#target-fps}
När detta är inaktiverat synkar Nomad sina bilder per sekund med din skärms uppdateringsfrekvens.

När detta är aktiverat kan du ställa in hur många bilder per sekund Nomad ska rendera.

### Gränssnitt {#debug-interface}
* `Top: layout` 
  * Collapse: På små enheter kommer toppraden att kollapsa till fler undermenyer. 
  * Scroll: Om du är van vid Nomad på stora skärmar och föredrar den normala layouten, använder detta alternativ den vanliga breda toppraden, och den kan scrollas.
  * Multiline: Visa hela toppmenyn över flera rader.
* `Bottom: draggable popup` - Det nedre verktygsfältet har flera knappar som visar en dialogruta. Om detta alternativ är aktiverat kan dessa dialoger flyttas till andra ställen på skärmen.  
* `Toolbox: show all` - Nomad döljer verktyg som inte är relevanta för den aktuella markeringen, t.ex. döljs alla sculpt-penslar på primitiver som inte är validerade. Detta alternativ tonar ned inaktiverade verktyg istället för att dölja dem.
* `Toolbox: colored` - Färgkoda toolbox-ikonerna baserat på deras typ.
* `Panel: Drop shadows` - Rita skuggor runt menyer och paneler. På vissa äldre enheter kan detta påverka prestandan.
* `Panel: Blending` - Debug-alternativ
* `Pointer: hovering dot` - För enheter som stöder pen-hover, visa en punkt när pennan hovrar över menyer och paneler.

### Gif‑turntable {#gif-turntable}
Nomad kan exportera en animerad gif-turntable. Observera att på grund av begränsningar i gif-formatet är kvaliteten låg. Skärminspelning är vanligtvis en bättre metod.

* `Duration` - hur lång turntablen ska vara i sekunder
* `Rotation center` - var kamerapivoten är, alltså vilken del av scenen kameran roterar runt
* `Transparent background` - Använd transparent bakgrund för gifs. Observera att gifs bara stöder 1-bitars transparens, så kanter kan bli kraftigt kantiga (aliasing).
* `Max frame sampling` - Många av Nomads högkvalitativa rendereffekter kommer från att kombinera flera bildrutor. Den här reglaget anger hur många bildrutor som ska kombineras.
* `Export (GIF)` - starta gif-exportprocessen.

### Efterbehandling {#post-process}
* `Filtering` - Debug-alternativ
* `Format` - Debug-alternativ
* `Buffer reuse` - Debug-alternativ

### Prestanda {#performance}
* `Multicore general` - Debug-alternativ
* `Multicore sculpting` - Debug-alternativ
* `Partial Drawing` - Experimentell funktion! Använd om du skulpterar en relativt liten del av ett högupplöst mesh. Det bör göra skulpteringen mjukare, men du bör inte aktivera wireframe! Det kan också ge visuella artefakter under penseldrag.

### Funktion {#feature}
* `Flip quad split (on tap)` -  Debug-alternativ
* `Join: merge radius` - Vertices kommer automatiskt att svetsas om de är tillräckligt nära när mesh sammanfogas. Du kan justera radien med detta reglage.

### Felsökning {#dev}
* `Logs` - Visa ett logg-fönster
* `App review popup` - Debug-alternativ
* `FPS` - lägg till en frames-per-second-räknare i viewport-statistiken.
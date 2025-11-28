# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plattform {#platform}
### Var finns mina projekt lagrade på min enhet? {#locate}
Projekten finns i mappen `projects` inuti huvudmappen Nomad.

På iOS kan du komma åt Nomad-mappen via appen Filer.

På Android finns Nomad-mappen i `Android/data/com.stephaneginier.nomad/files/`.  
På de senaste Android-versionerna (10/11) har du inte längre åtkomst till mappen `Android/data`.
Du kan komma åt den via en separat app, till exempel [den här](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Finns det något sätt att beta‑testa? {#beta}
För Windows & MacOS kan en beta finnas tillgänglig på [hemsidan](https://nomadsculpt.com).
<br>
För iOS finns en privat TestFlight, besök [Discord](https://discord.com/invite/8h7BwpRz29) i kanalen #beta-ios.
<br>
[Webbdemon](https://nomadsculpt.com/demo) uppdateras vanligtvis med de senaste funktionerna.

### Varför finns det en gratis provversion på Android men inte på iOS? {#android-trial}
För att gamla Android-enheter är dåliga (och vissa nyare också...), och jag ville inte att folk skulle köpa appen och mötas av en svart skärm.
Men huvudorsaken är att jag upplever att betalda Android-appar inte riktigt är normen.

### Vilken är den bästa surfplattan för att köra Nomad? {#best-tablet}

TLDR: En iPad.

Det lite längre svaret är 

> "Den nyaste iPad du _har råd med_, om du inte verkligen hatar Apple, i så fall den nyaste Samsung-plattan du har råd med. Allt annat, testa först." 

Folk vill alltid ha mer information, så här är en sammanfattning.

Nomad fungerar bäst på nyare iPads:

* iPads och iPhones kan använda pluginet [Quad Remesher](tools#quad-remesher) från [Exoside](https://exoside.com/)
* nyare iPads med senaste pennstödet har [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), du kan vrida pennan i vissa verktyg i Nomad. 
* prestandan hos de senaste M-serie-chipen är mycket hög. 

Den nyaste och dyraste iPaden som finns kommer att kunna rendera slutbilder mycket snabbt och låta dig skulptera mycket detalj.

Men prestandafallet med billigare och äldre iPads är inte så stort som folk tror. Alla iPads som stöder Apple Pencil kör Nomad ganska bra. Till exempel:

* En iPad Pro från 2023 kan hantera skulpturer på 5 miljoner polygoner och ändå vara responsiv, en slutkvalitetsbild kan renderas på 5 sekunder.
* En iPad Pro från 2015 kan hantera ett objekt på 1,2 miljoner polygoner med lite fördröjning, en slutkvalitetsbild kan renderas på 20 sekunder.

Det är en stor prestandaskillnad, men du måste också ta hänsyn till priset:

* iPad Pro 2025 kostar *2500 USD* ny med alla tillval. 
* iPad Pro 2023 kostar för närvarande *400 USD* på eBay.
* iPad Pro 2015 kostar *250 USD* på eBay.

Är det värt 2100 dollar extra för 4 miljoner fler polys och att spara 15 sekunder? Det är upp till dig.

Icke-Pro-modeller kan vara ännu billigare och ge ett brett urval av storlekar och prestanda. Nuvarande iPad Air stöder gen 2-pennan med barrel roll och är avsevärt billigare än Pro. Andrahands- och renoveringsmarknaden har ännu fler alternativ. 

Detta innebär att oavsett budget bör du kunna hitta en iPad som passar dig. Och kom ihåg att de flesta skulpturer inte är på miljoner polys! Om du kan hålla dig under 500 000 polys kommer även gamla iPads låta dig skulptera snabbt.

`Hur är det med Android?`

Grafikprestandan på Android ligger under iPads. Enligt Nomads utvecklare kommer "en Samsung Galaxy Tab S9 köra Nomad en storleksordning långsammare än en iPad Air". Med det sagt är många användare mycket nöjda med sina Samsung-plattor, Nomad fungerar bra för de flesta skulpteringsuppgifter. 

För andra Android-plattor, var försiktig. Android-hårdvara kan variera mycket i prestanda, det är inte lätt att förutse hur Nomad kommer att fungera.

Använd den gratis, spar-inaktiverade versionen av Nomad för att testa först. 

`Hur är det med minne och lagring?`

De flesta Nomad-filer tenderar att vara 100 MB eller mindre. Det innebär att nästan vilken surfplatta du än köper idag, iPad eller Android, kommer ha gott om utrymme för dina Nomad-projekt.


### Jag köpte Nomad för en enhet, kan jag använda den på en annan enhet? {#multi-devices}
Så länge den använder samma appbutik och samma konto, ja.

Till exempel om du köpte den i iOS App Store kan du använda den på dina andra iOS-enheter.

Om du köpte den till din Android-platta på Google Play kan du använda den på dina andra Android-enheter.

Men om du köpte Nomad på Android och sedan skaffar en iPad måste du köpa den igen.

Detta beror på att Nomad inte har någon egen licensserver eller prenumerationsmodell. Det finns ingen överenskommelse mellan Apple/Google/AppGallery om att hantera licensdelning. 


### Hur återställer jag mitt köp? {#restore}
Google Play och AppGallery hanterar synkroniseringen automatiskt.

- Gå till About-menyn (Nomad-ikonen uppe till vänster) och tryck på `restore purchase`
- Kontrollera att du är inloggad på samma konto som du använde för att köpa Nomad (på Google Play).
- Starta om enheten
- Ibland måste du vänta ett par timmar
- Se till att Google Play-appen är uppdaterad
- Installera om Nomad (se till att [säkerhetskopiera dina filer](#where-are-my-projects-located-on-my-device) om du inte vill förlora något)
- Du kan försöka köpa igen för att se vad som händer (obs: du kan inte köpa samma artikel två gånger på samma konto)

:::tip
Du kan kontakta mig på <support@nomadsculpt.com> men det *enda* jag kan göra är att bekräfta om ett e-postkonto har ett köp kopplat till sig.

Observera att jag regelbundet får rapporter om licenser som inte uppdateras korrekt efter att man skaffat en ny enhet.
Jag har ingen kontroll över betalning och kontosynkronisering, allt hanteras av Google/AppGallery!

Till slut återställs köpet alltid, men vilka steg som krävs för att påskynda processen är oklart.
:::

::: warning
Nyare Huawei-enheter har inte tillgång till Googles tjänster.
I så fall måste du köpa appen igen på AppGallery (Huaweis appbutik).
:::

### Kan ni översätta eller fixa [mitt‑språk]? {#locale}
Jag kan relativt enkelt lägga till ett nytt språk, men jag förlitar mig på AI-översättning eftersom det är mycket enklare att hantera för regelbundna uppdateringar.
Översättningsfilerna finns [här](https://github.com/stephomi/nomad-translation).

## Funktioner {#features}

### Varför rör sig inte gizmon? {#gizmo-not-moving}
Du kan ha [pin aktiverad i vänstra menyverktygsfältet](tools#left-menu-toolbar). 

### Kan vi animera i Nomad? {#animate}
Inte just nu. En tidslinjefunktion som kan animera lager skulle kunna vara intressant, men är inte direkt planerad för tillfället.  

Jag skulle vilja stödja riggning/skinning i framtiden, men det innebär några utmaningar (framför allt interaktionen med skulpteringsverktygen...) så inget är säkert än.


### Kan vi göra riktig low‑poly‑modellering? {#lowpoly}
Inte just nu.
Detta är inte riktigt inom Nomad *Sculpts* område, men kanske kommer jag att tillhandahålla några verktyg i framtiden.


### Kan vi göra uv och texturering? {#texturing}
Kort svar: Ja. Långt svar: Inte direkt, men det finns flera sätt att kombinera Nomads utmärkta vertex-målningsverktyg med uv:n och texturer.

* Nomad låter dig måla färg, roughness, materialegenskaper direkt i vertexarna på din skulptur.
* Nomad tillåter mycket höga vertexantal så att du kan måla utan att bry dig om uv:n.
* Nomad kan ladda texturer för användning i penslar, vilket möjliggör stämpling och målning med texturer.
* Nomad kan ladda objekt som redan har texturer tilldelade, för renderingsändamål.
* Nomad kan [UV-unwrappa](topology.md#uv-unwrap) objekt med lägre polygonantal.
* Färg/roughness/metalness kan överföras från texturer till vertexar via [projektinställningarna](topology.md#reproject-to-vertex).
* Färg/roughness/metalness/normals kan bakas från vertexar till texturer via [bake-inställningarna](topology.md#bake-to-texture)
* Baking och projicering kan hanteras mellan enskilda objekt eller många objekt, eller mellan högsta och lägsta subdivisionsnivåerna på ett enskilt objekt, vilket möjliggör en mängd olika bake- och projektarbetsflöden.
* Efter baking kommer export av en obj även exportera texturer, som kan tas till en app som Procreate för att måla direkt på texturer.

### Kan jag spela in en turntable‑video? {#video}
Inte planerat för nu, iOS har en [videoinspelningsfunktion](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) som är mycket enkel att använda.

På iOS görs detta genom att svepa ned från övre vänstra hörnet och trycka på inspelningsknappen. Du får en nedräkning på 3 sekunder, svep bort menyn för att visa Nomad och använd turntable-funktionen. När du är klar, svep ned igen från övre högra hörnet och tryck på inspelningsknappen igen. Redigera filmen i bildbiblioteket för att ta bort överflödig film i början och slutet av videon.

### Kan du lägga till [infoga‑favorit‑funktion] som en toppnivåknapp? {#interface}
Ja, det nedre verktygsfältet kan nu anpassas från menyn [interface](interface.md), och flytande verktygsfält kan nu skapas.

### Vilka är de kommande funktionerna? {#next-features}
För den medellånga/långa planen har jag många idéer men jag vet inte än.  

Buggrättningar och förbättring av befintliga funktioner kommer alltid ha högre prioritet än att lägga till nya.


### Kan vi rigga i Nomad? {#rigging}
Nej, men det är planerat. För närvarande kan du föräldrakoppla former till varandra och ändra pivotpunkter, vilket möjliggör enkla poserbara skulpturer.

### Kan vi använda fler än 4 ljus? {#lights}
Nej, detta är en begränsning i Nomads realtidsrenderingsmotor. Det är möjligt att fejka detta med emissiva objekt och global illumination i efterbearbetning, som visas i [den här handledningen](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Kan vi importera ZBrush‑verktyg? {#zbrush-import}
Nej, Zbrush använder ett proprietärt format. Du bör kunna extrahera alpha-kartorna och använda dem i Nomad. 

### Varför stämmer inte färgerna med det jag målade? Varför kan jag inte få vitt i renderingen? {#paint-pbr}
Föreställ dig att ta ett foto av ett pappersark, jämfört med ett foto av en skrivbordslampa, jämfört med ett foto av solen. Äldre kameror och skärmar gör dem bara alla ”vita”. Mer moderna system kan visa en skillnad mellan reflekterat vitt från papper, utsänt ljus från en lampa och det superljusa från solen.

Modern datorgrafik försöker arbeta på ett liknande sätt, genom att efterlikna fysiken hos ljus och ytor. Detta kallas `Physically Based Rendering`, eller PBR, och Nomads PBR-renderare bygger på detta. Det ser realistiskt och balanserat ut, men ofta kommer starkt målade färger att se mörkare ut.

Om du behöver att renderingen ska stämma bättre med de målade färgerna kan du fixa detta både på icke-fysikaliskt baserade och fysikaliskt baserade sätt:

Icke PBR:
* `Använd läget 'Unlit' i ljusmenyn`. Färger visas exakt som de målats, men du förlorar också all skuggning. Praktiskt för snabba kontroller och mer grafisk output.
* `Använd läget 'Matcap' i ljusmenyn`. Välj en ljusare matcap som mestadels är vit, utan färgton.

PBR:
* `Använd en neutral miljö`. Du kan [ändra miljön](shading.md#environment) till en mer neutral. Undvik inomhusmiljöer eftersom de tenderar att vara mer färgade. Föredra istället dagsljus utomhus eller studiomiljö.
* `Öka belysningen`. Om du tog ett foto av vitt papper i ett mörkt rum skulle du helt enkelt lägga till mer ljus. På miljöljuset, höj exposure-reglaget tills färgerna börjar kännas rätt för dig, eller lägg till fler individuella ljus med högre intensitet.
* `Öka kamerans exponering`. Om det mörka rummet inte hade några extra lampor kunde du låta kameran ha slutaren öppen längre eller använda högre ISO-känslighet. I Nomad kan du uppnå ett liknande resultat med efterbearbetning. Gå till post process, aktivera, ner till tone mapping, aktivera och höj exposure-reglaget tills färgerna känns rätt.
* `Använd emissiv färg`. I materialmenyn kan du aktivera ”emissive” under textures, vilket får ett objekt att se ut som en ljuskälla. Om du slår på global illumination i inställningarna för post process kommer det kasta ljus på andra objekt i scenen. Du kan också aktivera ”unlit” för det materialet, vilket ger ett liknande utseende utan textur.

## Kraschproblem {#crashes}

### Det kraschar när jag sparar eller remeshar min modell! {#crash-remesh}
Din enhet får slut på minne (RAM).  
För att minska minnesanvändningen i din scen kan du använda några av alternativen i [Topology](topology.md) för att minska antalet polygoner.

::: tip RAM/Lagring
Det som spelar roll är mängden RAM, inte lagringen (som vanligtvis är mycket större).
:::


### Det kraschar när jag laddar mitt projekt! {#crash-load}
Om filen är liten kan du skicka den till mig så tittar jag på den (via e-post <support@nomadsculpt.com>).

Annars får enheten troligen slut på RAM-minne.

- Se till att du stänger alla andra öppna appar på din enhet.
- Starta ett nytt projekt i Nomad istället för att ha ett projekt öppet.
- Om det fortfarande kraschar är den enda lösningen att ladda [din projektfil](#where-are-my-projects-located-on-my-device) på en enhet med mer minne.

::: tip
På en skrivbordswebbläsare kan du försöka ladda din fil [på den här url:en](https://nomadsculpt.com/demo_save/) och sedan exportera den igen efter att du förenklat din scen.

Vissa webbläsare begränsar mängden RAM en enskild flik kan använda, så det är möjligt att den här tekniken inte fungerar.

Om ditt projekt använder [Layers](layers.md) kan du vilja platta ihop dem för att minska minnesanvändningen.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Det kraschar när jag startar Nomad! {#crash-start}
Om det kraschar vid uppstart betyder det att Nomad har problem med en viss fil som finns i Nomad-mappen.

För det mesta händer det för att projektet är tungt och tyvärr överskrider RAM-gränsen.

Leta upp [Nomad-mappen](#where-are-my-projects-located-on-my-device) och byt sedan namn på eller flytta några filer för att hitta boven.

Försök först att byta namn på `settings.json`. På så sätt slutar den ladda det senaste projektet.

Om det inte fungerar, försök att flytta några senaste filer utanför deras respektive resursmappar (`projects`, `matcaps`, `environments`, etc).

Du kan också byta namn på mapparna själva så att Nomad helt ignorerar dem.
Om du byter namn på eller flyttar alla filer i Nomad-mappen får du samma resultat som en ren installation.

::: tip
När Nomad laddar en fil vid uppstart flyttar den alltid filen till mappen `can_be_deleted/`.
Om åtgärden lyckas flyttas den sedan tillbaka till sin ursprungliga mapp.

Om det kraschar innan inläsningen är klar kommer Nomad att starta utan problem nästa gång, eftersom den ignorerar mappen `can_be_deleted/`.

Du kan helt enkelt försöka ladda den här filen igen om du tror att det kan lyckas.
:::
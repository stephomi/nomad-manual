# ![](/icons/faq.webp) Vanliga frågor {#faq}

[[toc]]

## Plattform {#platform}
### Var finns mina projekt på min enhet? {#locate}
Projekten finns i mappen `projects` i Nomads huvudmapp.

På iOS kommer du åt Nomad-mappen med appen Filer.

På Android ligger Nomad-mappen i `Android/data/com.stephaneginier.nomad/files/`.  
I de senaste Android-versionerna (10/11) har du inte längre tillgång till mappen `Android/data`.
Du kan komma åt den via en separat app, till exempel [den här](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Kan jag betatesta? {#beta}
För Windows och MacOS kan det finnas en betaversion på [hemsidan](https://nomadsculpt.com).
<br>
För iOS finns en privat TestFlight: gå till kanalen #beta-ios på [Discord](https://discord.com/invite/8h7BwpRz29).
<br>
[Webbdemon](https://nomadsculpt.com/demo) uppdateras oftast med de senaste funktionerna.

### Varför finns det en gratis provperiod på Android, men inte på iOS? {#android-trial}
För att gamla Android-enheter är usla (och en del nya också...), och jag ville inte att folk skulle köpa appen och mötas av en svart skärm.
Men huvudskälet är att jag upplevde att betalappar inte riktigt är normen på Android.

### Vilken är den bästa surfplattan för Nomad? {#best-tablet}

Kort svar: en iPad.

Det lite längre svaret är

> "Den nyaste iPaden _du har råd med_, om du inte verkligen hatar Apple, i så fall den nyaste Samsung-plattan du har råd med. Allt annat: testa först."

Folk vill alltid ha mer information, så här kommer en sammanfattning.

Nomad fungerar bäst på nyare iPads:

* iPads och iPhones har tillgång till insticksprogrammet [Quad Remesher](tools#quad-remesher) från [Exoside](https://exoside.com/)
* nya iPads med den senaste pennan har stöd för [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0): du kan vrida pennan i vissa verktyg i Nomad.
* prestandan hos de senaste chippen i M-serien är mycket hög.

Den nyaste och dyraste iPaden kan rendera slutliga bilder mycket snabbt och låter dig skulptera många detaljer.

Men prestandan sjunker inte så mycket som folk tror med billigare och äldre iPads. Alla iPads som har stöd för Apple Pencil kör Nomad riktigt bra. Till exempel:

* En iPad Pro från 2023 klarar skulpturer på 5 miljoner polygoner och är fortfarande följsam, och en bild i slutlig kvalitet renderas på 5 sekunder.
* En iPad Pro från 2015 klarar ett objekt på 1,2 miljoner polygoner med lite fördröjning, och en bild i slutlig kvalitet renderas på 20 sekunder.

Det är en stor skillnad i prestanda, men du måste också ta hänsyn till priset:

* iPad Pro från 2025 kostar *2500 USD* ny med alla tillval.
* iPad Pro från 2023 kostar just nu *400 USD* på eBay.
* iPad Pro från 2015 kostar *250 USD* på eBay.

Är 4 miljoner extra polygoner och 15 sparade sekunder värda 2100 dollar? Det får du avgöra själv.

Modeller som inte är Pro kan vara ännu billigare och finns i många olika storlekar och prestandanivåer. Den nuvarande iPad Air har stöd för andra generationens penna med barrel roll och är betydligt billigare än Pro. På andrahandsmarknaden och bland renoverade enheter finns ännu fler alternativ.

Det betyder att du bör kunna hitta en iPad som passar dig, oavsett budget. Och kom ihåg att de flesta skulpturer inte har miljontals polygoner! Om du kan hålla dig under 500 000 polygoner låter även gamla iPads dig skulptera snabbt.

`Hur är det med Android?`

Grafikprestandan på Android ligger under iPads. Enligt Nomads utvecklare "kör en Samsung Galaxy Tab S9 Nomad en storleksordning långsammare än en iPad Air". Med det sagt är många användare mycket nöjda med sina Samsung-plattor, och Nomad fungerar bra för det mesta skulpterandet.

Var försiktig med andra Android-plattor. Prestandan hos Android-hårdvara varierar mycket, och det är inte lätt att förutsäga hur Nomad kommer att fungera.

Använd den kostnadsfria versionen av Nomad, där sparning är avaktiverad, för att testa först.

`Hur är det med minne och lagring?`

De flesta Nomad-filer är 100 MB eller mindre. Det betyder att nästan alla surfplattor du köper i dag, iPad eller Android, har gott om plats för dina Nomad-projekt.


### Jag köpte Nomad till en enhet, kan jag använda den på en annan? {#multi-devices}
Ja, så länge den använder samma appbutik och samma konto.

Om du till exempel köpte den i iOS App Store kan du använda den på dina andra iOS-enheter.

Om du köpte den till din Android-platta på Google Play kan du använda den på dina andra Android-enheter.

Men om du köpte Nomad på Android och sedan skaffar en iPad behöver du köpa den igen.

Det beror på att Nomad inte har en egen licensserver eller prenumerationsmodell. Det finns inget avtal mellan Apple/Google/AppGallery för att dela licenser.


### Hur återställer jag mitt köp? {#restore}
Google Play och AppGallery sköter båda synkroniseringen automatiskt.

- Gå till menyn Om (Nomad-ikonen uppe till vänster) och tryck på `Återställ köp`
- Dubbelkolla att du är inloggad med samma konto som du köpte Nomad med (på Google Play).
- Starta om enheten
- Ibland behöver du vänta ett par timmar
- Se till att appen Google Play är uppdaterad
- Installera om Nomad (se till att [säkerhetskopiera dina filer](#locate) om du inte vill förlora något)
- Du kan försöka köpa igen för att se vad som händer (obs: du kan inte köpa samma sak två gånger med samma konto)

:::tip
Du kan kontakta mig på <support@nomadsculpt.com>, men det *enda* jag kan göra är att bekräfta om en e-postadress har ett köp kopplat till sig.

Observera att jag regelbundet får rapporter om licenser som inte uppdateras korrekt efter att någon skaffat en ny enhet.
Jag har ingen kontroll över betalningar och synkronisering av konton, allt sköts av Google/AppGallery!

Till slut återställs köpet alltid, men det är oklart vad man kan göra för att påskynda processen.
:::

::: warning
Nya Huawei-enheter har inte tillgång till Googles tjänster.
I så fall behöver du köpa appen igen på AppGallery (Huaweis appbutik).
:::

### Kan du översätta eller rätta [mitt-språk]? {#locale}
Jag kan relativt enkelt lägga till ett nytt språk, men jag förlitar mig på AI-översättning eftersom det är mycket enklare att hantera vid regelbundna uppdateringar.
Översättningsfilerna finns [här](https://github.com/stephomi/nomad-translation).

## Funktioner {#features}

### Varför rör sig inte gizmon? {#gizmo-not-moving}
Du kanske har aktiverat [fäst i det vänstra menyfältet](tools#left-menu-toolbar).

### Kan man animera i Nomad? {#animate}
Inte just nu. En tidslinje som kan animera lagren vore intressant, men det är inte riktigt planerat för tillfället.

Jag skulle vilja ha stöd för rigging/skinning i framtiden, men det innebär en del utmaningar (särskilt samspelet med skulpteringsverktygen...), så inget är säkert ännu.


### Kan man göra riktig lågpolymodellering? {#lowpoly}
Inte just nu.
Det ligger egentligen utanför vad Nomad *Sculpt* är tänkt för, men jag kanske lägger till några verktyg i framtiden.


### Kan man arbeta med UV och texturer? {#texturing}
Kort svar: Ja. Långt svar: Inte direkt, men det finns flera sätt att kombinera Nomads utmärkta verktyg för vertexmålning med UV och texturer.

* I Nomad kan du måla färg, grovhet och materialegenskaper direkt i skulpturens vertices.
* Nomad klarar väldigt många vertices, så att du kan måla utan att bry dig om UV.
* Nomad kan läsa in texturer att använda i penslar, så att du kan stämpla och måla med texturer.
* Nomad kan läsa in objekt som redan har texturer tilldelade, för rendering.
* Nomad kan göra [UV-uppackning](topology.md#uv-unwrap-uvatlas) av objekt med färre polygoner.
* Färg/grovhet/metallitet kan överföras från texturer till vertices via [projiceringsalternativen](topology.md#reproject-to-vertex).
* Färg/grovhet/metallitet/normaler kan bakas från vertices till texturer via [bakningsalternativen](topology.md#bake-texture)
* Bakning och projicering kan göras mellan enskilda objekt eller många objekt, eller mellan den högsta och lägsta subdivisionsnivån för ett och samma objekt, vilket ger många olika arbetsflöden för bakning och projicering.
* Efter bakningen exporteras även texturerna när du exporterar en OBJ, och de kan tas vidare till en app som Procreate för att måla direkt på texturerna.

### Kan jag spela in en vridbordsvideo? {#video}
Det är inte planerat just nu, men iOS har en [skärminspelningsfunktion](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) som är väldigt enkel att använda.

På iOS sveper du nedåt från övre vänstra hörnet och trycker på inspelningsknappen. Du får en nedräkning på 3 sekunder: svep bort menyn så att Nomad syns och använd vridbordsfunktionen. När du är klar sveper du nedåt igen från övre högra hörnet och trycker på inspelningsknappen igen. Redigera filmen i bildbiblioteket för att ta bort överflödigt material i början och slutet av videon.

### Kan du lägga till [favoritfunktion] som en knapp på toppnivå? {#interface}
Ja, det nedre verktygsfältet kan nu anpassas från menyn [Gränssnitt](interface.md#shortcuts), och du kan nu skapa flytande verktygsfält.

### Vilka blir nästa funktioner? {#next-features}
För färdplanen på medellång och lång sikt har jag många idéer, men jag vet inte än.

Buggfixar och förbättringar av befintliga funktioner har alltid högre prioritet än nya funktioner.


### Kan man rigga i Nomad? {#rigging}
Nej, men det är planerat. Just nu kan du koppla ihop former och ändra pivotpunkter, vilket ger enkla skulpturer som går att posera.

### Kan man använda fler än 4 ljuskällor? {#lights}
Du kan använda upp till 4 ljuskällor på mobilen och upp till 6 på datorn. Det är en begränsning i Nomads renderingsmotor för realtid. Det går att fejka fler med självlysande objekt och global belysning i efterbehandlingen, som visas i [den här guiden](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Kan man importera verktyg från Zbrush? {#zbrush-import}
Nej, Zbrush använder ett eget, slutet format. Du bör dock kunna extrahera alfabilderna och använda dem i Nomad.

### Varför stämmer inte färgerna med det jag målade? Varför kan jag inte få vitt i renderingen? {#paint-pbr}
Tänk dig att du fotograferar ett papper, en skrivbordslampa och solen. Äldre kameror och skärmar gör helt enkelt alla tre "vita". Modernare system kan visa skillnaden mellan det reflekterade vita från papperet, det utsända ljuset från en lampa och solens extrema ljusstyrka.

Modern datorgrafik försöker fungera på liknande sätt, genom att efterlikna fysiken hos ljus och ytor. Det kallas `Physically Based Rendering` (fysikaliskt baserad rendering), eller PBR, och Nomads PBR-rendering bygger på det. Det ser realistiskt och balanserat ut, men starkt målade färger ser ofta mörkare ut.

Om du vill att renderingen ska ligga närmare de målade färgerna kan du åtgärda det både på icke fysikaliskt baserade och på fysikaliskt baserade sätt:

Utan PBR:
* `Använd läget Obelyst i menyn Skuggning`. Färgerna visas exakt som de målades, men du förlorar också all skuggning. Praktiskt för snabba kontroller och för ett mer grafiskt resultat.
* `Använd läget MatCap i menyn Skuggning`. Välj en ljusare matcap som är mestadels vit, utan färgton.

Med PBR:
* `Använd en neutral miljö`. Du kan [byta miljö](shading.md#environment) till en mer neutral. Undvik inomhusmiljöer eftersom de ofta är mer färgade. Välj hellre en utomhusmiljö i dagsljus eller en studiomiljö.
* `Förstärk belysningen`. Om du fotograferade ett vitt papper i ett mörkt rum skulle du helt enkelt lägga till mer ljus. Höj exponeringsreglaget för miljöljuset tills färgerna börjar kännas rätt, eller lägg till fler enskilda ljuskällor med högre intensitet.
* `Höj kamerans exponering`. Om det mörka rummet inte hade några extra lampor skulle du kunna låta kamerans slutare vara öppen längre, eller använda ett känsligare ISO. I Nomad får du ett liknande resultat med efterbehandling. Gå till Efterbehandling, aktivera den, gå ner till Tonkartläggning, aktivera den och höj exponeringsreglaget tills färgerna känns rätt.
* `Använd emissiv färg`. I menyn Material kan du aktivera "Emissiv" under texturer, vilket får ett objekt att se ut som en ljuskälla. Om du slår på global belysning i inställningarna för efterbehandling kastar det ljus på andra objekt i scenen. Du kan också aktivera "Alltid utan belysning" för materialet, vilket ger ett liknande utseende utan textur.

## Krascher {#crashes}

### Det kraschar när jag sparar eller gör en omnätning av min modell! {#crash-remesh}
Din enhet får slut på minne (RAM).  
För att minska minnesanvändningen i scenen kan du använda några av alternativen under [Topologi](topology.md) för att minska antalet polygoner.

::: tip RAM/lagring
Det som spelar roll är mängden RAM, inte lagringsutrymmet (som oftast är mycket större).
:::


### Det kraschar när jag öppnar mitt projekt! {#crash-load}
Om filen är liten kan du skicka den till mig så tittar jag på den (via e-post <support@nomadsculpt.com>).

Annars får enheten troligen slut på RAM-minne.

- Se till att stänga alla andra öppna appar på enheten.
- Starta ett nytt projekt i Nomad i stället för att ha ett projekt öppet.
- Om det fortfarande kraschar är den enda lösningen att öppna [din projektfil](#locate) på en enhet med mer minne.

::: tip
Om din mobila enhet inte kan öppna projektet, prova [datorversionen](https://nomadsculpt.com). Du kan använda den gratis i demoläge för att importera och exportera projekt, även om bara ett fåtal redigeringsverktyg finns tillgängliga.

Om ditt projekt använder [Lager](layers.md) kan du slå ihop dem för att minska minnesanvändningen.
:::

### Det kraschar när jag startar Nomad! {#crash-start}
Om det kraschar vid inläsningen betyder det att Nomad har problem med en viss fil i Nomad-mappen.

Oftast händer det för att projektet är tungt och tyvärr överskrider gränsen för RAM.

Leta upp [Nomad-mappen](#locate) och byt sedan namn på eller flytta några filer för att hitta den skyldiga.

Prova först att byta namn på `settings.json`. Då slutar Nomad att läsa in det senaste projektet.

Om det inte fungerar, prova att flytta några nya filer ut ur sina respektive resursmappar (`projects`, `matcaps`, `environments` osv.).

Du kan också byta namn på själva mapparna så att Nomad ignorerar dem helt.
Om du byter namn på eller flyttar alla filer i Nomad-mappen får du samma resultat som vid en ren installation.

::: tip
När Nomad läser in en fil vid start flyttar den alltid filen till mappen `can_be_deleted/`.
Om inläsningen lyckas flyttas filen tillbaka till sin ursprungliga mapp.

Om det kraschar innan inläsningen är klar startar Nomad utan problem nästa gång, eftersom den ignorerar mappen `can_be_deleted/`.

Du kan helt enkelt försöka läsa in filen igen om du tror att det kan lyckas.
:::

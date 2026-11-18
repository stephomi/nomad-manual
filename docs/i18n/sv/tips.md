# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Hur du börjar en modell {#how-to-start-a-model}

Nybörjare inom 3d-skulptering frågar ofta vilket som är det bästa sättet att börja en modell. Det finns inget bästa sätt, olika personer föredrar olika saker. Här är några av de vanligaste metoderna.

### Skulptera på en sfär, multiresolution {#sculpt-on-sphere-multires}

Standardmodellen när Nomad startar är det vanligaste sättet. Använd verktyg som flytta, lera och veck för att trycka och dra sfären till rätt form. Använd de lägre subdivisionsnivåerna när du vill göra stora ändringar snabbt, och högre subdivisionsnivåer för detaljarbete.

Ett vanligt problem är att du ofta får slut på polygoner där du behöver dem, samtidigt som du har för många på andra ställen. Om du till exempel drar ut standardsfären till en hel kropp har du troligen inte tillräckligt med detaljer för fingrarna, medan massor av polygoner går till spillo på bakhuvudet. För mestadels sfäriska former, som ett huvud, kan det dock fungera bra.

### Dyntopo {#dyntopo}

När du aktiverar Dyntopo läggs polygoner till och tas bort efter behov medan du skulpterar. De här polygonerna är trianglar, och nybörjare tycker ofta att den röriga strukturen är sämre än det rena utseendet med multiresolution. Men det är värt att hålla ut! Om du slår på jämn skuggning, stänger av wireframe och slutar oroa dig för strukturen kan det här läget ge en känsla som påminner mycket om lera. Glöm inte att det här läget också kan ta bort polygoner om du använder en stor pensel eller en utjämningspensel, så verktyget känns alltid snabbt och följsamt. När du har ett första utkast av skulpturen klart kan du klona den, köra den genom Quad Remesher för att få en snygg struktur och projicera om de ursprungliga detaljerna på en hög subdivisionsnivå.

### Voxel-omnätning {#voxel-remesh}

Voxel-omnätning ger din skulptur en topologi som till största delen består av quads. Operationen är snabb vid lägre upplösningar och kan användas för att snabbt ersätta utsträckta eller alltför täta polygoner med en jämnt fördelad struktur. Det kan vara ett utmärkt sätt att börja en hel kropp från en sfär: säg att du börjar med ett huvud, då kan du dra ut en hals och göra en voxel-omnätning. Dra ut en kropp, voxel-omnätning, armar, voxel-omnätning, och så vidare, tills du har grundformerna.

### Använd flera objekt {#use-multiple-objects}

Många anatomiguider bygger upp en kropp av enkla sfärer, cylindrar och kuber. Du kan skulptera på samma sätt i Nomad. Fördelen är att du kan koppla ihop objekt i scenhierarkin, så att huvudet till exempel följer med när du roterar halsen. Att kunna använda gizmo-verktyget för exakt förflyttning, rotation och skalning är också mycket användbart, och du kan ställa in en pivot per form så att de rör sig precis som du tänkt dig. När grundblocken är på rätt plats kan du markera alla och göra en voxel-omnätning eller en boolean av dem till en enda yta för mer detaljerad skulptering.

Ett praktiskt tips för det här arbetssättet är att börja med en sfär, skala den till en utdragen korv, trycka på pivot, klicka på "botten" och trycka på pivot igen. Nu har du en kroppsdel som kan klonas, flyttas längs den första sfärens längd, klonas, roteras, klonas, skjutas, klonas osv. för att snabbt lägga upp en kropp.

### Rör {#tubes}

Rörverktyget är ett utmärkt sätt att börja en skulptur. Reptilsvansar, armar, ben, fingrar, ögonbryn: allt kan snabbt skissas upp med rörverktyget och sedan enkelt redigeras i efterhand. Du kan också ändra tvärsnittsprofilen, vilket ger snabba formändringar. Du kan validera formen för att börja skulptera på den, och göra en voxel-omnätning av den tillsammans med andra objekt för att få en mesh av hela kroppen.

### Använd andra appar {#use-other-apps}

En del föredrar att börja en modell i andra appar, och det går också bra. Med verktyg som Blender eller Valence kan du börja modeller med lågpolytekniker och sedan importera dem i Nomad för att skulptera.

### Använd de inbyggda förinställningarna {#use-the-built-in-presets}

I menyn [Filer](files.md), klicka på `Förinställning…` till vänster i projektavsnittet. Här hittar du flera förinställda huvud- och kroppsformer från Blender Foundation. Välj en du gillar, tryck på den igen och lägg till den i din scen.

### Använd modeller från nätet {#use-online-models}

Det finns många gratis modeller på nätet, till exempel på Poly Haven, Sketchfab och TurboSquid. Oftast kan de här modellerna importeras i Nomad och antingen skulpteras på direkt eller användas som referens.

### Inga regler! {#no-rules}

I slutändan kan du använda vilken kombination av de här teknikerna som helst, eller ingen alls! Nomad är mycket flexibelt i det avseendet. Avancerade användare kanske börjar med rör, går vidare med dyntopo, kombinerar med en nedladdad fot, kör Quad Remesher på alltihop och sedan använder multiresolution för de sista detaljerna. Det som fungerar för dig.

## Ytgrupper {#facegroups}

Verktyget Ytgrupp kan användas till mycket, som förklaras i den här YouTube-videon: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Det här är en sammanfattning i text av funktionerna som tas upp i videon.

### Varför ytgrupper? {#why-facegroups}

Med ytgrupper kan du organisera och markera ytor ("ytor" och "polygoner" betyder samma sak i den här manualen). Det är lättare att förklara jämfört med Nomads andra verktyg för markering och organisering. I Nomad kan du skapa objekt, namnge dem och koppla ihop dem, så det är lätt att bygga upp en struktur av objekt för att till exempel definiera ett rum med golv, väggar, stol, bord och så vidare.

För en karaktär kanske du gör en första utblockning med separata objekt för huvud, armar och ben, men när du slår ihop alla delar till en enda mesh försvinner den strukturen. Du kan arbeta med delar av en karaktär med hjälp av masker, men det blir tröttsamt att måla en mask för händerna, sedan näsan, sedan händerna igen.

Det är här ytgrupper kommer till nytta. Du kan märka polygonytor med en färg och sedan markera och bearbeta polygoner som har samma färg. Observera att ytgruppsfärg och vertexfärg är två olika saker.

Den närmaste jämförelsen är att måla färger på en karta och senare kunna markera länder eller regioner utifrån färgen.

För huvuden kan du måla zoner som markerar ögonhålor, näsa, läppar, haka och öron, och sedan enkelt markera de zonerna senare. För hard surface och mekanisk skulptering kan det vara användbart för att definiera paneler och sektioner.

### Skapa och redigera ytgrupper {#creating-and-editing-facegroups}

Ytgrupper kan läggas på med en pensel, där varje nytt penseldrag skapar en ny ytgrupp, eller så kan de välja ytgruppen under markören och utöka den. De kan också skapas med hjälp av former.

* Punkt, standardläget - en enda dragning definierar en ny ytgruppsfärg och tilldelar den till ytorna du drar över. Varje ny dragning definierar en ny ytgrupp. Ett tryck fyller en ny ytgrupp.
* Punkt, läget `Välj` - när knappen `Välj` i det vänstra verktygsfältet är aktiv väljer Nomad ytgruppen under markören och lägger på den under resten av dragningen. Det är användbart för att förfina ytgrupper utan att behöva välja dem manuellt.

### Maskering {#masking}

När maskverktyget är aktivt och ytgruppsknappen är aktiv i dess verktygsfält maskerar du en ytgrupp genom att trycka på den.


### Dölja {#hiding}

När döljverktyget är aktivt och ytgruppsknappen är aktiv i dess verktygsfält döljer du en ytgrupp genom att trycka på den.

### Organisera {#organizing}

Som nämnts tidigare kan ytgrupper användas för att organisera din mesh utan att du behöver skapa separata objekt. Du kanske inte vill dela upp ett huvud i separata objekt för näsa, haka och öron, men det är mycket användbart att ha dem definierade med ytgrupper.

### UV-regioner {#uv-regions}

Verktyget UV Atlas försöker definiera sömmar automatiskt, men lägger ibland sömmar där du inte vill ha dem. Om ett objekt har ytgrupper och ytgruppsalternativet är aktivt i inställningarna för UV Atlas används ytgruppernas gränser som UV-sömmar i stället.

### Quad Remesher {#quad-remesher}

Insticksprogrammet Quad Remesher får oftast kanterna att flyta fint över modellen, men du kan använda ytgrupper för att styra det när ytgruppsalternativet är aktiverat. Det gör det lätt att till exempel definiera ett rent kantflöde runt ögon, en ögonbrynsbåge, läppar eller ett kindveck.

### Filtrera med andra verktyg {#filter-with-other-tools}

Många verktyg har alternativ för att ta hänsyn till ytgrupper, antingen i verktygets egen meny eller via menyn Penseldrag -> Filter. Utjämningsverktyget kan till exempel, med en styrka över 100 %, jämna ut detaljer kraftigt inom en ytgrupp men hålla ytgruppens gräns någorlunda intakt.

### Slappna av och jämna ut ytgruppernas gränser {#relax-and-smooth-facegroup-borders}

Alternativet `Slappna av` i verktyget Ytgrupp gör ett utmärkt jobb med att jämna ut ytgruppernas gränser och samtidigt hålla andra detaljer intakta. Det kan vara ett bra sätt att definiera mjuka gränser mellan ytgrupper innan du kör Quad Remesher.

## Begränsningar på surfplatta/mobil {#limitations-on-tabletmobile}

Dagens surfplattor och mobiler är mycket kraftfulla, men skiljer sig på viktiga punkter från stationära och bärbara datorer:

### Ingen aktiv kylning {#no-active-cooling}

Datorer har fläktar och/eller stora kylflänsar som håller dem svala, och är byggda för att klara höga temperaturer. Mobil hårdvara är oftast byggd för att vara tunn i första hand, inte för att hålla insidan sval. Om du pressar Nomad till de högsta kvalitetsinställningarna (belysningsläget PBR, komplexa material, många objekt, många efterbehandlingseffekter aktiverade) kan enheten både bli överhettad och tömma batteriet mycket snabbt.

Ett bättre sätt är att använda belysningsläget matcap och en lägre `Renderupplösning` (högst upp i menyn Efterbehandling). De här valen håller enheten sval och låter dig skulptera längre.

### Begränsat minne {#limited-memory}

Nomad kan nå resultat i nivå med de flesta skulpteringsprogram för datorer, men kan inte böja fysikens lagar! De flesta datorer har dubbelt så mycket minne som mobila enheter, och arbetsstationer byggda för 3d-animation har ofta 4 eller 8 gånger så mycket. Därför är det bra att hålla koll på hur många polygoner du använder: testa på din enhet för att se när den börjar bli trög. Nästan alla enheter som kan köra Nomad klarar 1 miljon polygoner ganska lätt. En iPad Pro med M2 klarar 8 miljoner utan problem, och användare har testat de senaste iPad-modellerna med långt mer än så.

Med det sagt behöver bara de allra mest detaljerade skulpturerna mer än 4 miljoner polygoner. Om du gör relativt enkla objekt och ofta märker att du går över 500 000, 1 miljon eller 4 miljoner, så använder du för många polygoner! Se till att du har `Jämn skuggning` aktiverat i [Inställningar](settings.md).

### Operativsystemet är mindre förlåtande mot krävande appar {#os-is-less-forgiving-with-intensive-apps}

Apple och Android förväntar sig att appar sparar och läser in små filer mycket snabbt. De utgår också från att appar kan växla mellan uppgifter mycket snabbt. Nomad använder smarta knep för att hålla filstorlekarna relativt små och spara dem mycket snabbt, men om mobilens operativsystem tycker att Nomad tar för lång tid stänger det helt enkelt av appen innan den är klar. Det är ytterligare ett skäl att hålla filerna i den mindre storleken. Det går att arbeta med skulpturer på 37 miljoner polygoner, som en användare rapporterade på Discord, men det rekommenderas inte!

## Arbeta på små skärmar {#working-on-small-screens}

Nomad är gjort för surfplattor, men fungerar bra på telefoner också. Det kan bli lättare att skulptera på en liten skärm som en telefon med några justeringar av gränssnittet och arbetssättet:

* Ett tryck med 4 fingrar döljer eller visar hela gränssnittet, så att du får mer utrymme att skulptera.
* En dragning upp och ner med 3 fingrar ändrar penselns radie.
* Gränssnittets skala kan göras mindre för att få plats med fler knappar om du har bra syn, eller större om du har sämre syn!
* De bredare menyerna kan ibland vara i vägen för skulpturen. Du kan göra dem genomskinliga och utan oskärpa så att du ser skulpturen under menyn.
* Om du skulpterar med fingret, använd alternativet [`Penseldragsförskjutning`](stroke.md#stroke-offset) för att flytta penselns mitt en bit från fingret.
* De här och många fler alternativ hittar du i menyn [Gränssnitt](./interface.md).


## Uppblåsnings- eller toppdeformerare {#inflate-or-peak-deformer}

Många 3d-appar har en uppblåsningsdeformerare (inflate), som trycker ut alla vertices längs deras normal med en mängd du kan styra. Nomad saknar deformerare just nu, men det går att efterlikna det här beteendet med penseln Blås upp:

* Välj penseln Blås upp
* I menyn [Penseldrag](./stroke.md#stroke), ändra penseldragsmetoden till `Lås + radie`
* Gör penselns radie större än din skulptur, och zooma ut kameran från skulpturen om det behövs.
* Klicka och dra ett penseldrag på objektets yta. När radien är större än objektet blåses hela formen upp jämnt med en fast mängd.
* Justera penselns intensitet för att styra hur mycket den blåses upp
* Använd maskering vid behov för att skydda vissa områden eller minska effekten där.

## Ta bort knölar eller "finnar" efter en voxel-omnätning {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel-omnätning är utmärkt för att få jämnt fördelade polygoner, men skapar ibland en topologi som ger små knölar eller finnar när den jämnas ut. Till exempel:

* Använd veckpenseln på standardsfären och gör en virvel
* Gör en voxel-omnätning med `Bygg multiresolution` på 3
* Jämna ut med hög intensitet
* artefakter dyker upp (lättare att se med ett matcap-material med hög kontrast):

![](/videos/tip_pimples_before.mp4)

För att åtgärda det genom att skulptera, prova alternativet `Stabil utjämning` i utjämningsinställningarna. Det klarar den ojämna topologin från voxel-omnätningen och ger rena resultat.

![](/videos/tip_pimples_stable_smooth.mp4)

För att åtgärda själva topologin, använd en ny primitiv, Quad Remesher-verktygen eller ett externt 3d-modelleringsprogram, och projicera detaljerna från den ursprungliga meshen till den nya via `Topologi -> Baka -> Projektera om → Vertex`.

![](/videos/tip_pimples_reproject.mp4)

## Dagsljusbelysning {#daylight-lighting}

Standardrenderingen i PBR är, som namnet antyder, fysikaliskt baserad, vilket precis som ett obehandlat digitalfoto kan se lite blekt och platt ut. Nomads ljuskällor och efterbehandling kan användas för att ge renderingarna mer liv.

Här är en standardrendering. Låt oss se om vi kan få den att se bättre ut:
![](/images/tips_lighting_default.webp)

Om du aktiverar efterbehandling och tonmappning kan du få mer ljusstyrka och kontrast:

![](/images/tips_lighting_tonemap.webp)

Om vi tittar på ljuset är standardmiljöljuset bra för att skulptera, men kan förbättras för en slutlig rendering. Ett sätt att tänka är att skilja på direkt ljus (till exempel solen) och miljöljus (till exempel ljuset från den blå himlen och marken). Genom att minska miljöljuset och rotera det börjar du fånga hur belysningen borde se ut om motivet stod i skuggan:

![](/images/tips_lighting_env.webp)

Du kan lägga till ett direkt ljus och höja dess intensitet för att simulera skarpt solljus. Om du balanserar det mot miljöljuset får du ett tilltalande resultat:

![](/images/tips_lighting_sunlight.webp)

Karaktärer kan bli bättre om du byter deras material till subsurface och placerar en spotlight bakom karaktären, riktad mot öronen, så att de lyser igenom:

![](/images/tips_lighting_sss.webp)

Experimentera sedan med resten av efterbehandlingsinställningarna! Global belysning och ambient occlusion bidrar till en mer realistisk belysning. Krökning och skärpa kan hjälpa till att lyfta fram fler detaljer i skulpturen. Kromatisk aberration, skärpedjup, brus, bloom och vinjettering simulerar kameraeffekter. Observera att när du aktiverar fler effekter behöver belysningen och övriga efterbehandlingsvärden justeras för att kompensera.

Här är renderingen med en hel uppsättning justeringar i efterbehandlingen:
![](/images/tips_lighting_final.webp)

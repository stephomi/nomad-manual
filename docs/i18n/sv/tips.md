# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Hur man startar en modell {#how-to-start-a-model}

Nybörjare inom 3D‑skulptering frågar ofta vilket som är det bästa sättet att starta en modell. Det finns inget bästa sätt, olika personer har olika preferenser. Här är några av de vanligaste tillvägagångssätten.

### Skulptera på sfär, multires {#sculpt-on-sphere-multires}

Standardmodellen när Nomad startar är det vanligaste sättet. Använd verktygen Move, Clay, Crease för att trycka och dra sfären i form, använd de lägre subdivisionsnivåerna när du vill göra stora ändringar snabbt, använd högre subdivisionsnivåer för detaljarbete.

Ett vanligt problem är att du ofta får slut på polygoner där du behöver dem, medan du har för många polygoner på andra ställen. T.ex. om du trycker ut standardsfären till en hel kropp är det troligt att du inte har tillräckligt med detalj för att göra fingrarna, medan du har massor av bortslösade polygoner på baksidan av huvudet. För mestadels sfäriska former som ett huvud kan detta dock fungera bra.

### Dyntopo {#dyntopo}

Om du aktiverar Dyntopo kommer polygoner adaptivt att läggas till och tas bort medan du skulpterar. Dessa polygoner blir trianglar, och nybörjare gillar ofta inte den röriga layouten jämfört med det rena utseendet hos multires. Det är värt att hålla ut! Om du slår på smooth shading, stänger av wireframe och slutar oroa dig för layouten kan detta läge ge en väldigt lerlik känsla. Glöm inte att om du använder en stor pensel, eller en smooth‑pensel, kan detta läge också ta bort polygoner, så verktyget känns alltid snabbt och responsivt. När du har gjort ett första pass av skulpten kan du klona den och köra den genom quad remesher för att få en fin layout, och reprojicera originaldetaljerna på en hög subdivisionsnivå.

### Voxel-remesh {#voxel-remesh}

Voxel remesh kommer att applicera en huvudsakligen quad‑baserad topologi på din skulpt. Denna operation är snabb vid lägre upplösningar och kan användas för att snabbt ersätta utdragna polygoner eller alltför täta polygoner med en jämnt fördelad layout. Detta kan vara ett utmärkt sätt att starta en hel kropp från en sfär; säg att du börjar med ett huvud, du kan dra ut en hals, voxel remesh. Dra ut en kropp, voxel remesh, armar, voxel remesh, och så vidare tills du har de grundläggande formerna.

### Använd flera objekt {#use-multiple-objects}

Många anatomiguider representerar en kropp med enkla sfärer, cylindrar, kuber. Du kan också skulptera på detta sätt i Nomad. Detta har fördelen att du kan föräldrakoppla objekt i scenhierarkin, så att du till exempel kan rotera nacken och huvudet följer med. Att kunna använda gizmo‑verktyget för exakt förflyttning/rotation/skala är också väldigt användbart, och du kan även sätta pivoter per form så att de rör sig exakt som du förväntar dig. När de grundläggande blocken är på rätt plats kan du markera alla och voxel‑remesha eller boola ihop dem till en enda yta för mer detaljerad skulptering.

Ett praktiskt tips för detta arbetssätt är att börja med en sfär, skala den till en utdragen korv, tryck på Pivot, klicka på ”bottom”, tryck på Pivot igen. Du har nu en kroppsdel som kan klonas, flyttas längs längden på den första sfären, klonas, roteras, klonas, skjutas, klonas osv. för att snabbt lägga ut en kropp.

### Tubes {#tubes}

Tube‑verktyget är ett utmärkt sätt att starta en skulpt. Reptilsvansar, armar, ben, fingrar, ögonbryn – allt detta kan snabbt skissas upp med tube‑verktyget och sedan enkelt redigeras i efterhand. Det låter dig också ändra tvärsnittsprofilen, vilket möjliggör snabba formändringar. Du kan validera formen för att börja skulptera på den, och voxel‑remesha den tillsammans med andra objekt för att få ett helt kroppsnät.

### Använd andra appar {#use-other-apps}

Vissa föredrar att starta en modell i andra appar, det är också helt okej. Verktyg som Blender eller Valence låter dig starta modeller med low‑poly‑tekniker, som sedan kan importeras till Nomad för skulptering.

### Använd de inbyggda förinställningarna {#use-the-built-in-presets}

Från projektmenyn klickar du på `Preset...` uppe till höger. Här hittar du flera huvud‑ och kroppsformspresets från Blender Foundation. Välj en du gillar, tryck på den igen och lägg till den i din scen. 

### Använd modeller online {#use-online-models}

Det finns många gratis modeller tillgängliga online, t.ex. Polyhaven, Sketchfab, Turbosquid. Vanligtvis kan dessa modeller importeras till Nomad och antingen skulpteras på direkt eller användas som referens.

### Inga regler! {#no-rules}

I slutändan kan du använda vilken kombination som helst av dessa tekniker, eller inga alls! Nomad är väldigt flexibelt i detta avseende, avancerade användare kan börja med tubes, sedan dyntopo, sedan kombinera med en nedladdad fot, sedan quad‑remesha allt, sedan multires för slutdetaljer. Vad som än fungerar för dig.

## Facegroups {#facegroups}

Facegroup‑verktyget kan användas till många saker, som förklaras i denna YouTube‑video: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Detta är en textöversikt av funktionerna som täcks i videon.

### Varför facegroups? {#why-facegroups}

Facegroups låter dig organisera och välja faces (”faces” och ”polygons” används omväxlande i denna manual). Detta är lättare att förklara jämfört med Nomads andra urvals‑ och organisationsverktyg. Nomad låter dig skapa objekt, namnge dem, föräldrakoppla dem; det är enkelt att skapa en struktur av objekt för att definiera ett rum bestående av golv, väggar, stol, bord och så vidare.

För en karaktär kanske du gör en första block‑out med separata objekt för huvud, arm, ben, men när du väl slår ihop alla delar till ett enda mesh försvinner denna struktur. Du kan arbeta på undersektioner av en karaktär med masker, men det kan bli tröttsamt att hela tiden måla en mask för händerna, sedan näsan, sedan händerna igen.

Det är här facegroups är användbara. De låter dig tagga polygonfaces med en färg och sedan kunna välja och manipulera polys som har samma färg. Observera att facegroup‑färg och vertex‑färg är olika saker.

Den närmaste analogin vore att måla färger på en karta och senare kunna välja länder eller regioner baserat på färg.

För karaktärshuvuden kan du måla zoner för att markera ögonhålor, näsa, läppar, haka, öron och sedan enkelt välja dessa zoner senare. För hårdvara och mekanisk skulptering kan det vara användbart att definiera paneler och sektioner.

### Skapa och redigera facegroups {#creating-and-editing-facegroups}

Facegroups kan appliceras med en pensel, där varje nytt drag skapar en ny facegroup, eller så kan de välja facegruppen under markören och utöka den. De kan också skapas med hjälp av former.

* Dot, auto‑pick aktiverad – en enda dragning definierar en ny facegroup‑färg och tilldelar den till de faces du drar över. Varje nytt drag definierar en ny facegroup. En tryckning fyllnadsfärgar en ny facegroup.
* Dot, auto‑pick inaktiverad – när auto‑pick‑knappen är i sitt ”sub”-läge kommer Nomad att välja facegruppen under markören och applicera den under resten av draget. Detta är användbart för att förfina facegroups utan att behöva välja dem manuellt.

### Maskning {#masking}

När maskverktyget är aktivt och facegroup‑knappen är aktiv på dess verktygsrad kommer ett tryck på en facegroup att maskera den.

### Dölj {#hiding}

När hide‑verktyget är aktivt och facegroup‑knappen är aktiv på dess verktygsrad kommer ett tryck på en facegroup att dölja den.

### Organisera {#organizing}

Som nämnts tidigare kan facegroups användas för att organisera ditt mesh utan att du behöver skapa separata objekt. Du kanske inte vill dela upp ett huvud i separata objekt för näsa, haka, öron, men det är väldigt användbart att ha dem definierade via facegroups.

### UV-regioner {#uv-regions}

UV Atlas‑verktyget kommer att försöka definiera sömmar automatiskt, men kommer ibland att lägga sömmar där du inte vill ha dem. Om facegroups finns på ett objekt, och facegroup‑alternativet är aktivt i UV Atlas‑alternativen, kommer det istället att använda facegroup‑gränserna som UV‑sömmar.

### Quad-remesher {#quad-remesher}

Quad remesher‑pluginet kommer vanligtvis att lägga kanter snyggt på din modell, men du kan använda facegroups för att hjälpa styra det när facegroup‑alternativet är aktiverat. Detta kan göra det enkelt att definiera ett rent edge‑flow runt ögon, en ögonbrynsås, läppar, kindveck till exempel.

### Filtrera med andra verktyg {#filter-with-other-tools}

Många verktyg har alternativ för att vara facegroup‑medvetna, antingen från deras primära verktygsmeny eller via Stroke -> Filtering‑menyn. Till exempel kan smooth‑verktyget vid styrkor över 100 % aggressivt jämna ut detaljer inom en facegroup men behålla facegroup‑gränsen relativt intakt.

### Mjuka upp och jämna ut facegroup-gränser {#relax-and-smooth-facegroup-borders}

Relax‑alternativet i facegroup‑verktyget gör ett utmärkt jobb med att jämna facegroup‑gränser samtidigt som andra detaljer bevaras. Detta kan vara ett bra sätt att definiera släta facegroup‑gränsregioner innan quad‑remeshing.

## Begränsningar på surfplatta/mobil {#limitations-on-tabletmobile}

Dagens surfplattor och mobiler är mycket kraftfulla, men har viktiga skillnader jämfört med stationära datorer och laptops:

### Ingen aktiv kylning {#no-active-cooling}

Datorer har fläktar och/eller stora kylflänsar för att hålla sig svala och är designade för att köras vid höga temperaturer. Mobil hårdvara är vanligtvis designad för tunnhet i första hand, inte för att hjälpa till att hålla insidan sval. Om Nomad pressas till sina högsta kvalitetsinställningar (PBR‑ljusläge, komplexa material, många objekt, många efterbehandlingsalternativ aktiverade) kan detta både överhetta enheten och tömma batteriet mycket snabbt. 

Ett bättre tillvägagångssätt är att använda ett matcap‑ljusläge och använda en lägre render multiplier (överst i post process‑menyn). Dessa val håller enheten sval och låter dig skulptera längre.

### Begränsat minne {#limited-memory}

Nomad kan uppnå resultat som motsvarar de flesta desktop‑skulpteringsappar, men den kan inte bryta mot fysikens lagar! De flesta stationära datorer har dubbelt så mycket minne som mobila enheter, arbetsstationer byggda för 3D‑animation har ofta 4x eller 8x så mycket minne. På grund av detta är det bra att vara medveten om hur många polygoner du använder, köra några tester på din enhet för att se när den börjar bli seg. Nästan alla enheter som kan köra Nomad klarar 1 miljon polygoner ganska lätt. En M2 Ipad Pro klarar 8 miljoner bekvämt, folk har testat på de senaste Ipads långt över det.

Det sagt, bara de mest detaljerade skulpturerna behöver mer än 4 miljoner polys; om du gör relativt enkla objekt och ofta hamnar över 500 000, 1 miljon, 4 miljoner använder du för många polygoner! Se till att du har smooth shaded‑läge aktiverat i alternativen.

### OS är mindre förlåtande med krävande appar {#os-is-less-forgiving-with-intensive-apps}

Apple och Android förväntar sig att appar sparar och laddar små filer väldigt snabbt. De antar också att appar kan växla uppgifter väldigt snabbt. Återigen gör Nomad några smarta trick för att hålla filstorlekarna relativt små och spara dem väldigt snabbt, men om mobil‑OS:et tycker att Nomad tar för lång tid kommer det helt enkelt att döda appen innan den är klar med sin uppgift. Detta är ytterligare en anledning att hålla filer på den mindre sidan; det är möjligt att arbeta med skulpturer på 37 miljoner polys som en användare rapporterade på Discord, men det rekommenderas inte!

## Att arbeta på små skärmar {#working-on-small-screens}

Nomad är designat för att fungera på surfplattor, men fungerar också bra på telefoner. Skulptering på en liten skärm som en telefon kan göras enklare med några UI‑ och arbetsflödesjusteringar:

* En fyrfingers‑tryckning växlar hela UI:t, vilket ger dig mer utrymme att skulptera.
* En trefingers‑dragning upp och ner ändrar penselradien.
* UI‑skalan kan göras mindre för att få plats med fler knappar om du har bra syn, eller större om du har dålig syn.
* De bredare menyerna kan ibland hamna i vägen för skulpten; du kan göra dem transparenta och icke‑suddiga för att kunna se skulpten under menyn.
* Om du skulpterar med ett finger, använd offset‑alternativet för att flytta penselns centrum en bit bort från ditt finger.
* Dessa och många fler alternativ finns i [Interface‑menyn](./interface.md). 

## Inflate- eller peak-deformer {#inflate-or-peak-deformer}

Många 3D‑appar har en inflate‑deformer som trycker alla vertices längs deras normal med en kontrollerbar mängd. Även om Nomad för närvarande saknar deformers är det möjligt att efterlikna detta beteende med inflate‑penseln:

* Välj inflate‑penseln
* Ändra stroke‑metoden till `Lock + Radius' från [Stroke‑menyn](./stroke.md#stroke)
* Gör penselradien större än din skulpt, zooma kameran bort från skulpten om det behövs.
* Klicka och dra ett stroke på ytan av ditt objekt; när radien är större än objektet kommer hela formen att blåsas upp jämnt med en fast mängd.
* Justera penselintensiteten för att kontrollera mängden uppblåsning.
* Använd maskning vid behov för att skydda eller minska effekten av inflate i vissa områden.

## Ta bort knölar eller "finnar" från en voxel-remesh-operation {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel remesh är bra för att skapa jämnt fördelade polygoner, men skapar ibland topologi som orsakar små klumpar eller finnar när man jämnar. Till exempel:

* Använd crease‑penseln på standardsfären och gör en virvel
* Voxel remesh med ”build multiresolution at 3”
* Jämna med hög intensitet
* artefakter dyker upp (lättare att se med ett högkontrast‑matcap‑material):

![](/videos/tip_pimples_before.mp4)

För att fixa via skulptering, prova alternativet `Stable smoothing` i smooth‑inställningarna. Detta kan hantera den ojämna topologilayouten från voxel remesh och ge rena resultat.

![](/videos/tip_pimples_stable_smooth.mp4)

För att fixa själva topologin, använd en ny primitiv, eller quad remesh‑verktygen, eller en extern 3D‑modellerare, och projicera detaljer från det ursprungliga meshet till det nya via `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Dagsljusbelysning {#daylight-lighting}

Standard‑PBR‑rendern är, som namnet antyder, fysikaliskt baserad, vilket likt ett obehandlat digitalfoto kan se lite urvattnat och platt ut. Nomads ljus och efterbehandling kan användas för att få renderingar att se mer livfulla ut.

Här är en standardrender, låt oss se om vi kan få den att se bättre ut:
![](/images/tips_lighting_default.webp)

Att aktivera post processing och tonemapping kan lägga till ljusstyrka och kontrast:

![](/images/tips_lighting_tonemap.webp)

För att fokusera på ljusen: standardmiljöljuset är bra för skulptering, men kan förbättras för en slutrender. Ett sätt att tänka på detta är att separera direkt ljus (t.ex. solen) från miljöljus (t.ex. ljus från himlens blåhet, marken). Genom att minska miljöljuset och rotera det börjar man fånga hur ljuset borde se ut om motivet befann sig i skugga:

![](/images/tips_lighting_env.webp)

Ett direkt ljus kan läggas till och dess intensitet höjas för att simulera starkt solljus. Genom att balansera detta med miljöljuset uppnås ett tilltalande resultat:

![](/images/tips_lighting_sunlight.webp)

Karaktärer kan dra nytta av att byta sitt material till subsurface och placera en spotlight bakom karaktären riktad mot öronen för att få dem att glöda:

![](/images/tips_lighting_sss.webp)

Experimentera sedan med resten av post process‑inställningarna! Global Illumination och Ambient Occlusion hjälper till med mer realistisk belysning. Curvature och Sharpen kan hjälpa till att lyfta fram mer detaljer i skulpten. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette hjälper till att simulera kameraeffekter. Observera att när funktioner aktiveras måste belysning och andra efterbehandlingsvärden justeras för att kompensera.

Här är rendern med ett komplett set av efterbehandlingsjusteringar:
![](/images/tips_lighting_final.webp)
# ![](/icons/play.webp) Kom igång {#getting-started}

## Välkommen till Nomad! {#welcome-to-nomad}

Nomad är en app för 3d-skulptering som fungerar på många enheter, och allra bäst på surfplattor med en tryckkänslig penna, t.ex. en Apple iPad med Pencil eller en Samsung Galaxy Tab med penna.

Den är inspirerad av skulpteringsprogram för datorn som Zbrush och Blender, med fokus på ett gränssnitt som är lätt att förstå, utan att snåla på funktionerna. Om du har använt 3d-skulpteringsappar förut kommer Nomad att kännas väldigt bekant.

Om det här är första gången du skulpterar i 3d är det bra att känna till några grunder.

::: tip Föredrar du video?
Det finns nu MASSOR av nybörjarvideor på Youtube, här är några riktigt bra länkar:

* [Nomad Sculpt Crash Course av Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial av Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Serien NOMAD FOR BEGINNERS av SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Det är värt att kolla in de här skaparnas kanaler, de lägger ofta upp nya guider.
:::

## Din första skulptur {#your-first-sculpt}

När du startar Nomad första gången ser du en sfär på skärmen. Dra bara pennan över sfären för att börja skulptera. Symmetri är aktiverat som standard för att göra skulpteringen enklare.

![](/videos/gettingstarted_01.mp4)

För att göra penseln större eller mindre använder du radiereglaget till vänster.

![](/videos/gettingstarted_02.mp4)

För att göra penseln starkare eller svagare använder du intensitetsreglaget till vänster.

![](/videos/gettingstarted_03.mp4)

Standardverktyget är verktyget `Lera`, och det bygger på ytan. För att ta bort från ytan trycker du på knappen `Sub` till vänster. För att bygga på ytan igen trycker du på Sub-knappen en gång till.

![](/videos/gettingstarted_04.mp4)

För att jämna ut ytan trycker du på knappen `Jämna ut`. För att gå tillbaka till vanlig skulptering trycker du på Jämna ut-knappen igen.

![](/videos/gettingstarted_05.mp4)

För att rotera runt modellen drar du på den tomma ytan utanför modellen.

![](/videos/gettingstarted_06.mp4)

För att zooma använder du nypgesten med två fingrar.

![](/videos/gettingstarted_07.mp4)

För att panorera kameran sätter du 2 fingrar på skärmen och drar.

![](/videos/gettingstarted_08.mp4)

Om du gör ett misstag ångrar du med ett tryck med 2 fingrar, eller med ångraknappen nere till vänster.

![](/videos/gettingstarted_09.mp4)

::: tip Datorversionen
På datorn används alt/opt-tangenten för att styra kameran:

* dra med spetsen på tom yta = rotera kameran
* alt+dra med spetsen = panorera
* alt+dra med spetsen, släpp sedan alt = zooma (som i zbrush)

Med Wacom-plattor som har 2 eller fler knappar på pennan kan du ställa in spets och knappar så här i Wacoms inställningar:

* spets = vänsterklick
* nedre vippknapp = mittenklick
* övre vippknapp = högerklick

Med de inställningarna kan du styra kameran helt med pennan:

* övre vippknapp och svävande rörelse = rotera kameran
* nedre vippknapp och svävande rörelse = panorera
:::

## Lägg till färg {#add-color}

I Nomad kan du måla på skulpturens yta. Leta upp verktyget `Måla` i verktygsmenyn till höger och klicka på det. I verktygsfältet till vänster dyker en färgad sfär upp. Klicka på den så öppnas en färgväljare. Välj en färg och måla på din modell.

![](/videos/gettingstarted_10.mp4)

För att sudda ut trycker du på knappen `Radera` i verktygsfältet till vänster och suddar sedan på ytan. Tryck på raderingsknappen igen för att gå tillbaka till målningsläget.

![](/videos/gettingstarted_11.mp4)

Försök göra ett enkelt tecknat huvud med lerpenseln i lägena för att bygga på och ta bort, utjämning och målning:

![](/images/gettingstarted_head1.webp)

## Andra verktyg {#other-tools}

Verktygspaletten har många verktyg som hjälper dig att skulptera. Hittills har du använt lerpenseln (startverktyget), utjämning och målning. Eftersom utjämning används så ofta har den en extra genväg i verktygsfältet till vänster.

Verktygen i Nomad kan göra väldigt olika saker, från skulpteringsverktyg som flytta, veck och blås upp, till verktyg som dela och beskär som mer liknar snickar- eller metallverktyg. Sidan [Verktyg](tools.md) har mer information.

Försök använda verktygen flytta, veck, blås upp och jämna ut för att lägga till fler detaljer på huvudet och ändra dess form:

![](/images/gettingstarted_head2.webp)

Nu när du kan grunderna i Nomad, låt oss titta på resten av gränssnittet.

## Gränssnitt {#interface}

![](/images/interface_overview1.webp)

* `Toppmenyer` - Menyerna som ger tillgång till de flesta av Nomads funktioner. Menyerna uppe till vänster handlar främst om scenen och objekten, menyerna uppe till höger hör till verktygen. På mindre skärmar slås de här menyerna ihop för att spara plats.
* `Statistik` - Information om scenen, det aktuella objektet, maskens status och minnesanvändningen.
* `Navigeringskub` - En hjälp som visar vilken sida av skulpturen du tittar på, och en genväg för att hoppa mellan olika vyer. Om du trycker på kuben hoppar vyn till den sidan du tryckte på. Om du drar i kuben roterar vyn. Tryck på de små ikonerna bredvid kuben för att rama in det aktuella objektet, återgå till standardvyn, låsa kameran eller slå på/av rutnätet. I appen heter den `Snap-kub`, och dess utseende och placering kan ändras i [Inställningar](settings.md#snap-cube).
* `Verktygslåda` - Nomads verktyg finns i det här rullningsbara området.
* `Vänster verktygsfält` - Reglage för radie och intensitet för de flesta verktyg, knappar som beror på verktyget för andra, och genvägar för symmetri, verktygets alt/sub-läge, utjämning, maskering, döljning, ytgrupper, gizmon och målningsalternativ. Du kan ändra ordningen på genvägarna i menyn [Gränssnitt](interface.md#side-bar).
* `Nedre verktygsfält` - Genvägar till funktioner som används ofta, förklarade nedan.

::: tip Vänsterhänt?
Du kan spegelvända placeringen och ordningen på alla verktygsfält, se [Spegelvänd toppfält](interface.md#mirror-top-bar) och andra relaterade alternativ.
:::

## Nedre verktygsfält {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Ångra` - ångrar den senaste åtgärden
* `Gör om` - återställer det senast ångrade
* `Historik` - ger tillgång till historikalternativen, som förklaras i menyn [Historik](history.md).
* `Solo` - Växlar mellan att bara visa det aktuella objektet och att visa alla objekt
* `Röntgen` - Visar alla andra objekt i röntgenläge och det aktuella objektet som solitt. Med ett långt tryck eller ett svep uppåt kan du välja röntgenläget matcap och färg, och vilka objekt det gäller.
* `Voxel` - En genväg till voxel-omnätningsknappen i [Voxel-omnätning](topology.md#voxel-remesher). Ett långt tryck eller ett svep uppåt visar alternativen för voxel-omnätningen, som upplösningen.
* `Rutnät` - Slår på/av visningen av rutnätet. Ett långt tryck eller ett svep uppåt visar rutnätets alternativ, som dess färg och fästning.
* `Wireframe` - Slår på/av en wireframe-överlagring. Ett långt tryck eller ett svep uppåt visar alternativen för wireframe.
* `Inspektör` - Slår på/av visningen av extra data om det aktuella nätet. Som standard visas UV, men med ett långt tryck eller ett svep uppåt kan du granska andra egenskaper om de finns, och välja om de visas i bakgrunden eller på nätet.
* `Loggar` - Visar eller döljer ett fönster med Nomads felsökningsloggar.
* `Ytgrupp` - Slår på/av överlagringen för ytgrupper, se verktyget [Ytgrupp](tools.md#facegroup).

Du kan lägga till, ta bort och ändra ordningen på de här genvägarna i menyn [Gränssnitt](interface.md#add-shortcuts-bottom).

## Nästa steg {#next-steps}

Vad du lär dig härnäst är upp till dig och vad du tycker är intressant! Här är några förslag:

Vill du lära dig mer om skulpteringsverktygen? Gå till avsnittet [Verktyg](tools.md).

Vill du exportera dina modeller? Eller importera modeller att skulptera på? Eller skapa bilder av dina skulpturer? Gå till avsnittet [Filer](files.md).

Vill du lära dig mer om att styra detaljnivån på din skulptur? Gå till avsnittet [Topologi](topology.md) och lär dig om multiresolution och decimering.

Vill du arbeta med fler objekt? Kombinera enkla objekt och grundformer till en större scen? Gå till avsnittet [Scen](scene.md).

Vill du lära dig *allt* om Nomad? Bra val! Den här manualen täcker hela Nomad, innehåller massor av tips och tricks, och har en bra sökfunktion högst upp. Använd navigeringen till vänster för att lära dig mer.

Om du föredrar video har Holger Schönischka gjort en enorm samling tips och tricks för Nomad på Youtube: https://www.youtube.com/@ProcreateFX/videos


## Få hjälp {#getting-help}

Om du fortfarande har frågor efter att ha läst manualen och tittat på videoguiderna finns det tre huvudsakliga sätt att prata med andra Nomad-användare eller med Nomads utvecklare:

* Besök forumet: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Gå med i Nomads discord-chatt: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Kontakta utvecklaren direkt på support@nomadsculpt.com

# Kom igång {#getting-started}

## Välkommen till Nomad! {#welcome-to-nomad}

Nomad är en 3D‑skulptapp som fungerar på många enheter, och fungerar bäst på surfplattor med tryckkänslig penna, t.ex. en Apple iPad med Pencil, eller en Samsung Galaxy Tab med stylus.

Den är inspirerad av skrivbordsappar för skulptering som ZBrush och Blender, med fokus på ett lättbegripligt gränssnitt utan att kompromissa med funktioner. Om du har använt 3D‑skulptappar tidigare kommer Nomad att kännas mycket bekant.

Om detta är första gången du skulpterar i 3D är det bra att känna till några grunder.

::: tip Föredrar du video?
Youtube har nu MÅNGA videoguider för nybörjare, här är några bra länkar:

* [Nomad Sculpt Crash Course av Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial av Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS‑serie av SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Det är värt att kolla huvudkanalen för dessa skapare, de lägger ofta upp nya guider.
:::

## Din första skulptur {#your-first-sculpt}

När du startar Nomad första gången ser du en sfär på skärmen. Dra helt enkelt med pennan på sfären för att börja skulptera. Symmetri är aktiverat som standard för att göra skulpteringen enklare.

![](/videos/gettingstarted_01.mp4)

För att göra penseln större eller mindre använder du reglaget för radie till vänster.

![](/videos/gettingstarted_02.mp4)

För att göra penseln starkare eller svagare använder du reglaget för intensitet till vänster.

![](/videos/gettingstarted_03.mp4)

Standardverktyget är `Clay tool`, och det lägger till material på ytan. För att ta bort material från ytan, tryck på knappen `Sub` till vänster. För att lägga till material igen, tryck på Sub‑knappen en gång till.

![](/videos/gettingstarted_04.mp4)

För att jämna ut ytan, tryck på knappen `Smooth`. För att gå tillbaka till vanlig skulptering, tryck på Smooth‑knappen igen.

![](/videos/gettingstarted_05.mp4)

För att rotera runt modellen, dra i tomt utrymme utanför modellen.

![](/videos/gettingstarted_06.mp4)

För att zooma, använd nypgesten med två fingrar.

![](/videos/gettingstarted_07.mp4)

För att panorera kameran, placera två fingrar på skärmen och dra.

![](/videos/gettingstarted_08.mp4)

Om du gör ett misstag kan du ångra med ett tvåfingertapp, eller använda ångraknappen nere till vänster. 

![](/videos/gettingstarted_09.mp4)

::: tip Skrivbordsversion
På dator används alt/opt‑tangenten för att styra kameran:

* tip‑drag i tomt utrymme = rotera kameran
* alt+tip‑drag = panorera
* alt+tip‑drag, släpp sedan alt = zooma (samma som i ZBrush)

Med Wacom‑plattor som har två eller fler knappar på pennan använder du Wacom‑inställningarna för att konfigurera spets och knappar så här:

* tip = vänsterklick
* nedre vippknapp = mittenklick
* övre vippknapp = högerklick

Med dessa inställningar kan du styra kameran enbart med pennan:

* övre vippknapp och hovrande rörelse = rotera kameran
* nedre vippknapp och hovrande rörelse = panorera
:::

## Lägg till färg {#add-color}

Nomad låter dig måla på ytan av din skulpt. I verktygsmenyn till höger hittar du verktyget `Paint` och klickar på det. På verktygsfältet till vänster visas då en färgad sfär. Klicka på den för att öppna färgväljaren. Välj en färg och måla på din modell.

![](/videos/gettingstarted_10.mp4)

För att sudda, tryck på knappen `Erase` på verktygsfältet till vänster och sudda sedan på ytan. Tryck på erase‑knappen igen för att gå tillbaka till målningsläge.

![](/videos/gettingstarted_11.mp4)

Använd clay‑penseln i add/sub‑lägen, smooth och paint, och se om du kan göra ett enkelt tecknat huvud:

![](/images/gettingstarted_head1.webp)

## Andra verktyg {#other-tools}

Verktygspaletten har många verktyg som hjälper till med skulptering. Hittills har du använt clay‑penseln (standardverktyget), smooth och paint. Eftersom smooth används ofta har det en extra genväg i verktygsfältet till vänster.

Verktygen i Nomad kan göra en mängd olika saker, från skulpteringsrelaterade verktyg som move, crease, inflate, till verktyg som split och trim som mer liknar snickeri‑ eller metallbearbetningsverktyg. Sidan [Tools](tools.md) har mer information.

Se om du kan använda verktygen move, crease, inflate och smooth för att lägga till mer detaljer i ditt huvud och ändra dess form:

![](/images/gettingstarted_head2.webp)

Nu när du kan grunderna i Nomad, låt oss titta på resten av gränssnittet.

## Gränssnitt {#interface}

![](/images/interface_overview1.webp)

* `Top menus` - Menyerna för att komma åt de flesta av Nomads funktioner. Menyerna uppe till vänster täcker främst scen‑ och objektfunktioner, menyerna uppe till höger är relaterade till verktyg. På mindre skärmar slås dessa menyer ihop för att spara utrymme.
* `Stats` - Information om scenen, det aktuella objektet, maskstatus och minnesanvändning.
* `Nav Cube` - En hjälpare som visar vilken sida av skulpten du tittar på, samt en genväg för att hoppa till olika vyer. Genom att trycka på kuben hoppar vyn till den sida du trycker på. Genom att dra på kuben roterar du. Tryck på de små ikonerna vid sidan av kuben för att rama in det aktuella objektet eller återställa till standardvyn.
* `Toolbox` - Nomads verktyg finns i detta rullbara område.
* `Left toolbar` - Reglar för radie och intensitet för de flesta verktyg, kontextspecifika knappar för andra verktyg, samt genvägar för symmetri, verktygets alt/sub‑läge, maskning, smoothing, gizmo och målningsalternativ.
* `Bottom toolbar` - Genvägar till ofta använda funktioner, förklaras nedan.

::: tip Vänsterhänt?
Du kan spegelvända placering och ordning för alla verktygsfält, se [Mirror top bar](interface.md#mirror-top-bar) och andra relaterade alternativ.
:::

## Nedre verktygsrad {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Undo` - ångra den senaste åtgärden
* `Redo` - återställ den senast ångrade åtgärden
* `History` - få åtkomst till historikalternativ, förklaras i menyn [History](history.md).
* `Solo` - Växla mellan att bara visa det aktuella objektet eller alla objekt
* `X-Ray` - Gör alla andra objekt genomskinliga i röntgenläge och det aktuella objektet solitt. Ett långt tryck eller en uppåtsvepning låter dig ställa in färg och opacitet för röntgenläget.
* `Voxel` - En genväg till knappen för [Voxel Remesher](topology.md#voxel-remesher). Ett långt tryck eller en uppåtsvepning visar genvägar för att ställa in kvaliteten på voxel‑remesh.
* `Grid` - Växla visning av rutnätet. Ett långt tryck eller en uppåtsvepning visar alternativ för rutnätet.
* `Wire` - Växla en wireframe‑overlay. Ett långt tryck eller en uppåtsvepning visar alternativ för wireframe.
* `Inspect` - Växla visning av extra data om det aktuella nätet. Som standard visas UV:er, men ett långt tryck eller en uppåtsvepning låter dig inspektera andra egenskaper om de finns, och om detta visas i bakgrunden eller på själva nätet.

## Nästa steg {#next-steps}

Vad du bör lära dig härnäst beror på dig och vad du tycker är intressant! Här är några förslag:

Vill du lära dig mer om skulpteringsverktygen? Gå till avsnittet [Tools](tools.md).

Vill du exportera dina modeller? Eller importera modeller att skulptera på? Eller skapa bilder av dina skulpturer? Gå till avsnittet [Files](files.md).

Vill du lära dig mer om hur du kontrollerar detaljnivån på din skulpt? Gå till avsnittet [Topology](topology.md) och lär dig om multires och decimation.

Vill du arbeta med fler objekt? Kombinera enkla objekt och primitivformer till en större scen? Gå till avsnittet [Scene](scene.md).

Vill du lära dig *allt* om Nomad? Bra val! Den här manualen täcker hela Nomad, innehåller många tips och tricks och har en utmärkt sökfunktion högst upp. Använd navigeringen till vänster för att lära dig mer.

Om du föredrar video har Holger Schönischka gjort en stor samling tips och tricks för Nomad på Youtube: https://www.youtube.com/@ProcreateFX/videos


## Få hjälp {#getting-help}

Om du fortfarande har frågor efter att ha läst manualen och tittat på instruktionsvideorna finns det tre huvudsakliga sätt att prata med andra Nomad‑användare eller utvecklaren av Nomad:

* Besök forumet: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Gå med i Nomads Discord‑chatt: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Kontakta utvecklaren direkt på support@nomadsculpt.com
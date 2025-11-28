# ![](/icons/symmetry.webp) Symmetri {#symmetry}

Den här menyn styr hur penseldrag upprepas över ett spegelplan eller radiellt, samt sätt att återställa symmetri på icke-symmetriska objekt.

![](/images/symmetry_overview.webp) 

## Översikt {#overview}
Du kan använda symmetri på flera sätt:

* Som en spegel, som speglar arbete över X (vänster/höger), Y (topp/botten), Z (bak/framsida), eller en kombination. 
* Radiell symmetri kan ställas in på X Y Z med ett antal upprepningar, t.ex. för att skulptera en sjöstjärna. 
* Speglar kan fungera runt origo (kallat världs-läge, *world mode*) eller runt mitten av ett objekt (kallat lokalt läge, *local mode*).
* Skulpturer som började icke-symmetriska kan tvingas att bli symmetriska.

En genväg för att aktivera/inaktivera symmetri finns också i den vänstra snabbpanelen (*"Sym"*). Det lilla ”L/W” indikerar om Nomad är i lokalt eller världs-symmetriläge. Du kan också långttrycka eller svepa till mitten av skärmen för att få fram en meny.

![](/images/symmetry_button.webp) 

Detta är ett globalt alternativ, så läget följer med mellan olika verktyg.
De enda undantagen är transformverktygen ([Flytta](#translate), [Rotera](#rotate), [Skala](#scale) och [Gizmo](#gizmo)) som har egna symmetrilägen.

::: tip
Symmetrimenyn är främst till för att styra penseldragssymmetri. Du kan också spegla och upprepa objekt via [repeatrar som finns i scenmenyn](scene#repeaters). 
:::

## Aktiverad {#enabled}
Växla spegelläge, detta är samma som knappen `Sym` i den vänstra snabbpanelen. 

## Plan {#planes}

Aktivera symmetriplan och antal upprepningar för radiell symmetri. Observera att du inte behöver välja bara ett plan; du kan ha 1, 2 eller alla 3 plan aktiverade för komplex symmetri.

Axeln och upprepningsantalet för radiell symmetri. Observera att dessa inte heller är begränsade till en enda axel, och kan till och med fungera i kombination med plansymmetri för att generera detaljerade resultat mycket snabbt. (Det totala antalet upprepningar är begränsat till 150)

![](/videos/symmetry_demo.mp4) 

## Metod {#method}
Spegeln kan antingen vara ”Local” och röra sig med objektet, eller vara ”World” och inte röra sig. Om du är osäker på vilket läge du behöver, titta på spegelplanet och de radiella indikatorerna som visas över objektet. I lokalt läge, om du använder transform-gizmon och flyttar modellen, kommer spegelindikatorerna också att flyttas. I världs-läge kommer spegelindikatorerna att ligga fast, och objektet glider genom dem.

## Spegling {#mirroring}
![](/images/symmetry_mirroring.webp)

När du skulpterar nära symmetriplanen kommer vissa penslar att ha ett ofullkomligt symmetribeteende. Den här sektionen låter dig återställa symmetri genom att kopiera ena sidan av din skulptur till den andra. 


`Direction` - Knapparna `<<` och `>>` avgör vilken sida som kopieras till den andra. Nomad beräknar detta från din aktuella vy, så om du t.ex. ställer in den på `<<` kommer den alltid att kopiera från skärmens högra sida till skärmens vänstra sida.

![](/icons/shield.webp) `Mask` - Maskknappen låter dig isolera vad som ska speglas; maskering av målsidan skyddar det området, maskering av källsidan hindrar det området från att speglas till målet. 

![](/icons/tool_hide.webp) `Hide` - När detta är aktivt kommer områden som är dolda på källsidan inte att speglas till målsidan. 

`Mirror` försöker identifiera om topologin är densamma på båda sidor om spegeln, och om så är fallet flyttas bara vertexar. Detta är det vanligaste scenariot.

`Split & Mirror` kommer i princip att skära objektet längs spegeln, kopiera ena sidan, spegla den till den andra och svetsa vertexar längs spegeln. Det är ett mer destruktivt alternativ och kommer att ta bort multiresolution, men ibland krävs den här metoden om modellen är mycket olika på var sida om spegeln.

### Vänd objekt {#flip-object}
![](/images/symmetry_flip.webp)
Gör vänster sida till höger sida och vice versa. Liknar till utseendet om du använde gizmo-verktygsmenyn och satte skalan till -1 på X.

## Återställ och redigera {#reset-and-edit}

![](/images/symmetry_edit.webp)

Det är möjligt att redigera symmetrins position och orientering (men inte rekommenderat!). Vid behov kommer `World center` och `Orientation` att återställa symmetrins position och orientering till standardvärdena.

Nomad vet vanligtvis var symmetriplanet ska placeras. Det rekommenderas inte att justera detta manuellt, men knappen `Gizmo (Edit)` tillåter detta för avancerade användare. När denna knapp klickas visas en gizmo som låter dig translatera och rotera symmetriplanet. Om du vill återställa standardcentrum och standardorientering gör knapparna `object center` och `orientation` detta.

Beteendet för dessa alternativ ändras beroende på vilket utrymme (*Local/World*) du befinner dig i.
Så om det inte fungerar som du förväntar dig, kontrollera att du är i rätt utrymme.

::: tip
Knappen `Gizmo (Edit)` är medvetet gråmarkerad som en påminnelse om att du förmodligen inte borde använda den!
:::

## Visa alternativ {#show-options}
![](/images/symmetry_show.webp)


`Show line` och `Show plane` växlar en vy-överlagring av symmetrins positioner. Observera att avstängning av dessa alternativ bara får effekt när symmetrimenyn är stängd.
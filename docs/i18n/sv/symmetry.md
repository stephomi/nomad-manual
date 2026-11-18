# ![](/icons/symmetry.webp) Symmetri {#symmetry}

Den här menyn styr hur penseldrag upprepas över ett spegelplan, radiellt eller som plattor, och erbjuder sätt att återställa symmetrin på objekt som inte är symmetriska.

![](/images/symmetry_overview.webp) 

## Översikt {#overview}
Du kan använda symmetri på flera sätt:

* Som en spegel, som vänder arbetet över X (vänster/höger), Y (upp/ner), Z (bak/fram), eller en kombination.
* Radiell symmetri kan ställas in på X Y Z med ett antal upprepningar, t.ex. när du skulpterar en sjöstjärna.
* Plattsättning upprepar dina penseldrag över objektet, så att skulpturen går ihop sömlöst.
* Speglar kan verka runt origo (kallat världsläge) eller runt ett objekts mitt (kallat lokalt läge).
* Skulpturer som började osymmetriska kan tvingas bli symmetriska.

En genväg för att slå på/av symmetrin finns också i den vänstra snabbpanelen (*"Sym"*). Det lilla 'L/W' visar om Nomad är i lokalt eller globalt symmetriläge. Du kan också trycka länge eller svepa mot mitten av skärmen för att ta fram en meny.

![](/images/symmetry_button.webp) 

Symmetriinställningarna sparas med varje objekt, och menyns rubrik visar namnet på objektet du redigerar.
Skulpteringsverktygen delar samma på/av-läge, medan transformeringsverktygen ([Transformera](tools.md#transform) och [Gizmo](tools.md#gizmo)) har sitt eget.

::: tip
Symmetrimenyn är främst till för att styra penseldragens symmetri. Du kan också spegla och upprepa objekt med [repeterarna i scenmenyn](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Aktiverad {#enabled}
Slår på/av spegelläget, samma sak som knappen `Sym` i den vänstra snabbpanelen. En varningsikon påminner dig när det är avstängt, och menyn säger också till när det aktuella verktyget ignorerar symmetrin.

## Plan {#planes}

Aktivera symmetriplan och antal upprepningar för radiell symmetri. Du behöver inte välja bara ett plan: du kan ha 1, 2 eller alla 3 plan aktiverade för mer komplex symmetri.

Raden `Radiell` ställer in antalet upprepningar för radiell symmetri runt varje axel. Inte heller de är begränsade till en enda axel, och de kan till och med kombineras med plansymmetri för att mycket snabbt ge detaljrika resultat. (Det totala antalet upprepningar är begränsat till 200)

![](/videos/symmetry_demo.mp4) 

## Platta {#tile}

Upprepa dina penseldrag längs en axel, med jämna mellanrum, så att skulpturen går ihop sömlöst. Praktiskt för mönster, tegelstenar eller en textur som du tänker upprepa.

Slå på plattsättning för varje axel med knapparna `Platta`, och ställ sedan in antingen ett `Antal` (hur många upprepningar som täcker objektet) eller ett `Avstånd` (utrymmet mellan två upprepningar). Tryck på reglaget till vänster för att växla mellan de två.

## Metod {#method}
Spegeln kan antingen vara `Lokal` och följa med objektet, eller `Värld` och stå still. Om du är osäker på vilket läge du behöver, titta på spegelplanet och de radiella indikatorerna som visas ovanpå objektet. I lokalt läge flyttas spegelindikatorerna med när du flyttar modellen med transformeringsverktygen (`Gizmo` eller `Transformera`). I världsläge står spegelindikatorerna still och objektet glider igenom dem.

## Spegla {#mirroring}
![](/images/symmetry_mirroring.webp)

När du skulpterar nära symmetriplanen får vissa penslar en ofullständig symmetri. I den här delen kan du återställa symmetrin genom att kopiera ena sidan av skulpturen till den andra.

`Riktning` - De två pilknapparna bredvid rubriken `Spegla` bestämmer vilken sida som kopieras till den andra. Nomad räknar ut det från din aktuella vy, så sidan förblir densamma på skärmen oavsett från vilket håll du tittar på modellen.

![](/icons/shield.webp) `Mask` - Maskknappen låter dig avgränsa vad som speglas: att maskera målsidan skyddar det området, att maskera källsidan hindrar det området från att speglas till målsidan.

![](/icons/tool_hide.webp) `Dölj` - När den är aktiv speglas inte områden som är dolda på källsidan till målsidan.

`Spegla` (behåll topologi) försöker avgöra om topologin är densamma på båda sidor om spegeln, och i så fall flyttas bara vertexarna. Det är det vanligaste fallet. Radiell symmetri ignoreras. Om topologin inte är symmetrisk erbjuder Nomad att tvinga fram speglingen med `Klipp • Spegla` i stället.

Knapparna `Klipp` skär objektet längs symmetriplanet/-planen. De ändrar topologin, så de är mer destruktiva än `Spegla`. Siffran på varje knapp är hur många objekt du får:

* `Klipp` - tar bort ena sidan av objektet.
* `Klipp • Spegla` - skär objektet, kopierar ena sidan, speglar den till den andra och svetsar ihop vertexarna längs spegeln. Ibland krävs den här metoden om modellen skiljer sig mycket mellan sidorna.
* `Klipp • Dela` - skär objektet och behåller varje sida som ett separat objekt.
* `Klipp • Spegla • Dela` - som `Klipp • Spegla`, men varje sida blir ett separat objekt.

Om flera objekt är valda gäller `Spegla` och [Vänd objekt](#flip-object) för alla.

### Vänd objekt {#flip-object}
![](/images/symmetry_flip.webp)
Gör vänster sida till höger och tvärtom, längs `X`, `Y` eller `Z`. Ser ut ungefär som om du använde gizmoverktygets meny och satte skalan till -1 på X.

## Återställ och redigera {#reset-and-edit}

![](/images/symmetry_edit.webp)

Det går att redigera symmetrins position och orientering (men det rekommenderas inte!). Vid behov återställer `Världscentrum` (`Objekt centrum` i lokalt läge) och `Orientering` symmetrins position och orientering till standardvärdena.

Nomad vet oftast var symmetriplanet ska ligga. Det rekommenderas inte att justera det för hand, men knappen `Gizmo (Redigera)` gör det möjligt för avancerade användare. När du trycker på den knappen visas en gizmo som låter dig flytta och rotera symmetriplanet. Om du vill återställa standardcentrum och -orientering använder du återställningsknapparna ovan.

`Från pivot` lägger symmetriplanet på pivoten för verktyget [Gizmo](tools.md#gizmo). Det är bara tillgängligt medan verktyget `Gizmo` är aktivt.

Hur de här alternativen beter sig beror på vilket rum (*Lokal/Värld*) du är i.
Så om det inte fungerar som du väntar dig, kontrollera att du är i rätt rum.

::: tip
Att redigera symmetriplanet med gizmon är lite experimentellt, du borde nog inte behöva det!
:::

## Visningsalternativ {#show-options}
![](/images/symmetry_show.webp)


`Visa linje` och `Visa plan` slår på/av en överlagring i vyn som visar var symmetrin ligger. Observera att avstängningen av de här alternativen bara får effekt när symmetrimenyn är stängd.

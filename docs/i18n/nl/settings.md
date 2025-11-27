# ![](/icons/cog.webp) Instellingen 

Het instellingenmenu bevat veel opties om het uiterlijk en gedrag van Nomad te regelen.

![](/images/settings_overview.webp)

## Weergave-instellingen
Deze sectie bevat snelkoppelingen voor de meeste instellingen verderop in dit menu.

![](/images/settings_display_settings.webp)

### Gladde arcering 
Schakel tussen gladde en gefacetteerde arcering. Bij gefacetteerde arcering worden de polygonen onafhankelijk van elkaar gearceerd, zodat je de onderliggende topologie kunt zien.
Het kan nuttig zijn om gefacetteerde arcering te gebruiken tijdens het beeldhouwen en daarna over te schakelen naar gladde arcering voor het renderen.

Het uitschakelen van gladde arcering verbetert de prestaties een beetje.

### Omtrek
Schakel een omtreklijn in op je huidige selectie.

Dit is handig om visuele feedback te krijgen over je huidige geselecteerde mesh(es) in het geval dat [Donker niet-geselecteerd](#darken-unselected-objects) is uitgeschakeld.

Vanuit prestatie-oogpunt is [Donker niet-geselecteerd](#darken-unselected-objects) veel beter dan de omtrekoplossing.

### Raster
Schakel een achtergrondraster in, handig om de plaatsing en schaal van objecten te begrijpen.

### Tweeledig
Schakel tweezijdige polygonweergave in. Alle vlakken wijzen in een bepaalde richting.
Vlakken die als *achterzijde* worden beschouwd, zijn de vlakken die "van" het camerastandpunt af wijzen.

Bijvoorbeeld: de eenvoudige bol bij het opstarten heeft zijn vlakken naar buiten gericht.
Als je de camera in de bol verplaatst, zie je vervolgens de achterzijde van deze vlakken.

Meestal zou je de achterzijde van vlakken niet moeten zien, dus het inkleuren ervan kan je helpen om mogelijke problemen of onjuiste topologie te detecteren.

Het uitschakelen van `tweeledig` renderen kan de renderprestaties een beetje verbeteren.


### Draadmodel
Schakel een draadmodel-overlay in. 

Merk op dat het inschakelen van het draadmodel de prestaties verlaagt.

### Snap-cube
Schakel een hulppictogram in de hoek van de scène in, handig om je te oriënteren in de ruimte en snel te wisselen tussen voor-/achter-/links-/rechts-/boven-/onderaanzichten.

### Schildering tonen
Schakel de verfweergave in. De standaardverf is een wit niet-metallisch materiaal, met 25% ruwheid.

### Verbergen gebruiken
Schakel de verbergmodus in. Wanneer deze is uitgeschakeld, bestaat hij nog steeds, maar is gedeactiveerd. Deze knop is uitgeschakeld als je momenteel de verbergtool gebruikt.

### Masker tonen
Schakel de maskermodus in. Wanneer deze is uitgeschakeld, bestaat hij nog steeds, maar is gedeactiveerd. Druk nogmaals op deze knop om hem opnieuw in te schakelen.

Als je het masker moet verbergen EN het toch actief wilt houden, gebruik dan de maskerkleur hieronder en stel deze in op wit. Vergeet niet om hem weer naar grijs te zetten als je klaar bent!

Merk op dat deze knop is uitgeschakeld als je momenteel een masker-tool gebruikt. 

### Masker -> Opaak
Masker -> opaak zal transparante vertices negeren voor gemaskeerde maskers. Dit is alleen relevant voor vertex- en textuuropaciteit; vlakken die door “verbergen” verborgen zijn, blijven verborgen.

### Highlight
Schakel de selectie-highlightflits in. Wanneer je objecten selecteert, wordt het geselecteerde object tijdelijk felroze weergegeven gedurende 500 milliseconden. De kleur en duur van de flits kunnen hieronder worden aangepast.

### Statistieken
Schakel de statusweergavetekst in het 3D-viewport in. Dit toont informatie over je systeemgeheugen, het totale aantal vertices in de scène en het aantal vertices van de huidige selectie.

----- 

### Donker niet-geselecteerde objecten
De objecten die niet zijn geselecteerd, worden donkerder gemaakt zodat de huidige selectie beter opvalt.

### Masker
De kleur die wordt gebruikt voor maskering, standaard een middengrijs, vermenigvuldigd met je objectkleur. Stel dit in op wit om het masker onzichtbaar te maken, maar vergeet niet om het weer naar grijs te zetten als je klaar bent!

## ![](/icons/cursor.webp) Cursor

### Cirkel tonen tijdens beeldhouwen
Blijf de straal van de penseel tonen tijdens het beeldhouwen.

### Kleine stip tonen
Toon een stip in het midden van de penseelstreek tijdens het beeldhouwen, of wanneer het camerapunt wordt gewijzigd.

### Touw-stabilisator tonen
Teken een lijn om de touwlengte aan te geven wanneer de lazy rope-stabilisator actief is in de streekinstellingen.

## ![](/icons/cursor.webp) Indicator
![](/images/settings_indicator.webp)

Toon visuele indicator(en) voor tutorials en schermopnames.

De knoppen `Vinger`, `Stylus` en `Muis` schakelen het weergeven van een pictogram in wanneer dat type invoer wordt gedetecteerd.

### Kleur
De kleur van de indicator.

### Grootte/Pictogram/Cirkel
Regelaars om de grootte van de indicator en de vormen binnen de indicator aan te passen.

## ![](/icons/wireframe.webp) Draadmodel
![](/images/settings_wireframe.webp)
Activeer de draadmodel-overlay.

### Doel
Stel in of niet-geselecteerde objecten het draadmodel tonen, of alleen geselecteerde objecten, of alle objecten.

### Verbergen
Stel in of het draadmodel nog steeds wordt weergegeven voor verborgen polygonen.

### Multiresolution: Alleen niveau 0
Multiresolution toont draadmodellen voor niveau 0 donkerder en hogere niveaus geleidelijk lichter. Wanneer deze optie is ingeschakeld, wordt alleen het draadmodel van niveau 0 weergegeven.

### Kleur
Stel de kleur en opaciteit van het draadmodel in.

## ![](/icons/grid.webp) Raster
![](/images/settings_grid.webp)
Activeer het raster.

### Kleur
Stel de rasterkleur en opaciteit in.

### Snappen
Schakel snappen naar het raster in voor curve-gebaseerde tools.

## ![](/icons/culling.webp)Tweeledig
Schakel het zien van polygonvlakken vanaf beide zijden in.

### Achterzijde kleuren, Achterzijde-kleur
Schakel het tinten van de achterzijden in en stel de tintkleur in.

## ![](/icons/outline.webp)Omtrek
Schakel een omtrek rond het actieve object in.

### Omtrekkleur, Dikte
Stel de kleur en dikte van de omtrek in.


## ![](/icons/bang.webp) Highlight
Schakel een korte flits in wanneer het actieve object wordt gewijzigd.
### Kleur, Duur
Stel de kleur en duur van de flits in milliseconden in.

## ![](/icons/snap_cube.webp) Snap-cube
![](/images/settings_snapcube.webp)

Toon een hulppictogram in de hoek van de scène, handig om snel te wisselen tussen voor-/achter-/links-/rechts-/boven-/onderaanzichten. Tik op de zijden van de cube om tussen orthografische aanzichten te wisselen.

### Vorm
Kies tussen een cube, een bol of een gnomon-vorm voor de snap-cube.

### Uitlijning beperken
Schakel vergrendeling van cameradraaien in bij slepen op de snap-cube. Wanneer actief, zal een sleepbeweging op de snap-cube alleen naar links/rechts of omhoog/omlaag gaan.

### Grootte
Stel de grootte van de snap-cube in.

### 180 graden draaien
Schakel een tikgedrag in zodat, als het aanzicht is vastgeklikt, tikken op het midden van de cube het aanzicht 180 graden draait. Als het aanzicht bijvoorbeeld op “voor” is vastgeklikt, zal tikken op de view-cube naar het achteraanzicht draaien.

### Positie
Stel in in welke hoek de snap-cube zal staan.


## ![](/icons/edit_radius_n.webp) Statistieken
![](/images/settings_stats.webp)

Toon informatie over je systeemgeheugen, het totale aantal vertices in de scène en het aantal vertices van de huidige selectie.

### Positie
Stel in in welke hoek de statistieken zullen staan.

## Primtive/Repeaters
## Numerieke invoer
Sta numerieke invoer toe wanneer je op de gizmo-widgets tikt.

## Multiresolution
### Maximaal aantal vertices
Stel een drempel in om niet toe te staan dat een multires-subdivide-bewerking hoger gaat dan deze polycount, wat Nomad waarschijnlijk zou laten crashen. De standaardwaarde is 10 miljoen.
### Drempel lage resolutie
Een lagere resolutie van de mesh kan worden weergegeven wanneer je de camera verplaatst. Je kunt deze waarde verhogen als je een hogere resolutie van de mesh wilt weergeven.

## Instellingen
### Terugzetten naar standaard
Zet alle instellingen terug naar hun standaardwaarden.

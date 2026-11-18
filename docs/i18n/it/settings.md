# ![](/icons/cog.webp) Impostazioni {#reset-to-default}

Il menu Impostazioni contiene molte opzioni per controllare l'aspetto e il comportamento di Nomad.

![](/images/settings_overview.webp)

La fila di pulsanti in cima al menu porta direttamente a una sezione: `Cursore`, `Indicatore`, `Wire`, `Griglia`, `Dai due lati`, `Bordato`, `Evidenziazione`, `Navigatore`, `Statistiche`, `Maniglie`, `Forma`, `Ripetitori` e `Multires`.

## Impostazioni visualizzazione {#display-settings}
Questa sezione contiene scorciatoie rapide per la maggior parte delle impostazioni che trovi più in basso in questo menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Ombreggiatura uniforme {#smooth-shading}
Passa dall'ombreggiatura uniforme a quella sfaccettata e viceversa. Con l'ombreggiatura sfaccettata i poligoni sono ombreggiati in modo indipendente, così puoi vedere la topologia sottostante.
Può essere utile vedere l'ombreggiatura sfaccettata mentre scolpisci, per poi passare all'ombreggiatura uniforme per il rendering.

Disattivare l'ombreggiatura uniforme migliora un po' le prestazioni.

### ![](/icons/outline.webp) Bordato {#outline-quick}
Attiva o disattiva un contorno attorno alla selezione attuale.

È utile per avere un riscontro visivo sulle mesh selezionate quando [Scurisci gli oggetti non selezionati](#darken-unselected-objects) è disattivato.

Dal punto di vista delle prestazioni, usare [Scurisci gli oggetti non selezionati](#darken-unselected-objects) è molto meglio che usare il contorno.

### ![](/icons/grid.webp) Griglia {#grid-quick}
Attiva o disattiva una griglia di sfondo, utile per capire la posizione e la scala degli oggetti.

### ![](/icons/culling.webp) Dai due lati {#two-sided-quick}
Attiva o disattiva la visualizzazione dei poligoni da entrambi i lati. Ogni faccia è rivolta in una certa direzione.
Le facce considerate *lato posteriore* sono quelle rivolte "lontano" dal punto di vista della fotocamera.

Per esempio, la semplice sfera iniziale ha le facce rivolte verso l'esterno.
Se porti la fotocamera dentro la sfera, vedrai il lato posteriore di queste facce.

Il più delle volte non dovresti vedere il lato posteriore delle facce, quindi colorarlo può aiutarti a individuare problemi o topologia scorretta.

Disattivare il rendering `Dai due lati` può migliorare un po' le prestazioni.


### ![](/icons/wireframe.webp) Wireframe {#wireframe-quick}
Attiva o disattiva la sovrapposizione del wireframe. 

Nota che attivare il wireframe riduce le prestazioni.

### ![](/icons/navigator.webp) Navigatore {#snap-cube-quick}
Attiva o disattiva un'icona di aiuto nell'angolo della scena, utile per orientarti nello spazio e passare rapidamente tra le viste frontale/posteriore/sinistra/destra/superiore/inferiore.

### ![](/icons/palette.webp) Mostra pittura {#show-painting}
Mostra o nasconde la pittura. Quando è disattivata, gli oggetti vengono mostrati con un materiale bianco non metallico, con rugosità al 25%, invece della loro pittura.

### ![](/icons/tool_hide.webp) Usa Nascondi {#use-hide}
Attiva o disattiva la modalità Nascondi. Quando è spenta le zone nascoste restano, sono solo disattivate. Questo pulsante è disabilitato se stai usando lo strumento Nascondi.

### ![](/icons/shield.webp) Mostra maschera {#show-mask}
Attiva o disattiva la modalità maschera. Quando è spenta la maschera resta, è solo disattivata. Premi di nuovo questo pulsante per riattivarla.

Se ti serve nascondere la maschera MA tenerla attiva, usa il colore della maschera qui sotto e impostalo sul bianco. Ricordati di rimetterlo grigio quando hai finito!

Nota che questo pulsante è disabilitato se stai usando uno strumento maschera. 

### ![](/icons/shield.webp) Maschera → Opaco {#mask-opaque}
`Maschera → Opaco` ignora i vertici trasparenti per la maschera. Riguarda solo l'opacità dei vertici e delle texture: le facce nascoste con "Nascondi" restano comunque nascoste. È disponibile solo mentre `Mostra maschera` è attivo.

### ![](/icons/bang.webp) Evidenziazione {#highlight-quick}
Attiva o disattiva il lampo che evidenzia la selezione. Quando selezioni degli oggetti, quello selezionato lampeggia per 500 millisecondi. Il colore e la durata del lampo si possono personalizzare più sotto.

### ![](/icons/list.webp) Statistiche {#stats-quick}
Mostra o nasconde il testo di stato nella vista 3d. Mostra informazioni sulla memoria del sistema, sul numero totale di vertici della scena e sul numero di vertici della selezione attuale.

----- 

### ![](/icons/cube.webp) Scurisci gli oggetti non selezionati {#darken-unselected-objects}
Gli oggetti non selezionati vengono scuriti, così la selezione attuale risalta.

### ![](/icons/shield.webp) Maschera {#mask}
Il colore usato per la maschera, di default un grigio medio, moltiplicato per il colore dell'oggetto. Impostalo sul bianco per rendere invisibile la maschera, ma ricordati di rimetterlo grigio quando hai finito!

## ![](/icons/cursor.webp) Cursore {#cursor}

### Cerchio {#show-circle-while-sculpting}
Quando mostrare il cerchio del raggio del pennello:

* `Auto` - mostra il cerchio, ma lo nasconde mentre scolpisci.
* `No` - non mostra mai il cerchio.
* `Sì` - mostra sempre il cerchio, anche mentre scolpisci.

### Mostra puntino {#show-small-dot}
Mostra un puntino al centro del tratto del pennello mentre scolpisci, o quando cambia il pivot della fotocamera.

### Mostra stabilizzatore di corda {#show-rope-stabilizer}
Disegna una linea che indica la lunghezza della corda quando lo [Stabilizzatore di corda ritardato](stroke.md#lazy-rope-stabilizer) è attivo nelle impostazioni del tratto.

### Mostra indicatore di rollio {#show-roll-hint}
Mostra la guida della direzione di rollio mentre usi una scorciatoia di rollio.

### ![](/icons/radius.webp) Dimensioni {#dot-size}
La dimensione del puntino.

### Colori {#cursor-colors}
Il cursore cambia colore in base a ciò che stai facendo: `Scolpire`, `Sfondo` (passando sopra lo sfondo), `Maschera`, `Leviga`, `Fotocamera` e `Raggio`. Qui puoi personalizzare ogni colore.

## ![](/icons/cursor.webp) Indicatore {#indicator}
![](/images/settings_indicator.webp)

Mostra uno o più indicatori visivi per tutorial e registrazioni dello schermo. Impostalo su `Sì` per attivarlo (su iOS c'è anche l'opzione `Auto`).

I pulsanti `Dito`, `Stilo` e `Mouse` attivano la visualizzazione di un'icona quando viene rilevato quel tipo di input.

### Colore {#indicator-color}
Il colore dell'indicatore.

### Dimensioni/Icona/Cerchio {#indicator-shape}
Controlli per regolare la dimensione dell'indicatore, e l'opacità dell'icona e del cerchio al suo interno.

## ![](/icons/wireframe.webp) Wireframe {#wireframe}
![](/images/settings_wireframe.webp)
Attiva la sovrapposizione del wireframe.

### Target {#target}
Stabilisce se il wireframe viene mostrato sugli oggetti non selezionati, solo su quelli selezionati, o su tutti gli oggetti.

### Nascondi {#hide}
Stabilisce se il wireframe viene mostrato anche per i poligoni nascosti.

### Multirisoluzione: solo livello 0 {#multiresolution-level-0-only}
Con la multirisoluzione, il wireframe del livello 0 è più scuro e quello dei livelli superiori via via più chiaro. Quando è attiva, questa opzione mostra solo il wireframe del livello 0.

### Colore {#wireframe-color}
Imposta il colore e l'opacità del wireframe.

## ![](/icons/grid.webp) Griglia {#grid}
![](/images/settings_grid.webp)
Attiva la griglia.

### Aggancio {#snap}
Queste opzioni fanno agganciare i punti degli strumenti basati su curve e forme (`Lathe`, `Tubo`, forme a poligono e a tracciato...) mentre li disegni:

* `Aggancia alla griglia` - si aggancia alla griglia.
* `Aggancia ai punti (vista allineata)` - si aggancia ai punti esistenti vicini quando la fotocamera è allineata a un asse.
* `Aggancia ai punti (visualizzazione libera)` - si aggancia ai punti esistenti vicini quando la fotocamera non è allineata.

### Colore {#grid-color}
Imposta il colore e l'opacità della griglia. Queste opzioni compaiono quando la griglia è visibile.

`Vignettatura` sfuma la griglia verso i bordi. `Soglia di divisione della griglia` imposta, in pixel, quanto possono infittirsi le linee della griglia sullo schermo prima che la griglia passi a un altro livello di suddivisione.

## ![](/icons/culling.webp)Dai due lati {#two-sided}
Permette di vedere le facce dei poligoni da entrambi i lati.

### Colore lato posteriore {#backface-color}
`Lato posteriore colorato` attiva la colorazione del lato posteriore delle facce, e `Colore lato posteriore` ne imposta il colore.

## ![](/icons/outline.webp)Bordato {#outline}
Attiva un contorno attorno agli oggetti selezionati.

### Colore del contorno, Spessore {#outline-color-thickness}
Imposta il colore e lo `Spessore` del contorno.


## ![](/icons/bang.webp) Evidenziazione {#highlight}
Attiva un breve lampo quando la selezione cambia.
### Colore, Durata {#color-duration}
Imposta il colore e la durata del lampo in millisecondi.

## ![](/icons/navigator.webp) Navigatore {#snap-cube}
![](/images/settings_snapcube.webp)

Mostra un'icona di aiuto nell'angolo della scena, utile per passare rapidamente tra le viste frontale/posteriore/sinistra/destra/superiore/inferiore. Tocca i suoi lati per passare da una vista ortografica all'altra.

### Forma {#shape}
Scegli tra una sfera, un cubo o uno gnomone come forma del navigatore.

### Restringi allineamento {#restrict-alignment}
Allinea le viste di aggancio agli assi del mondo. Quando è attivo, sono possibili solo le 6 viste principali. Su `Auto`, questa restrizione vale solo quando la fotocamera è in modalità `Piattaforma girevole`.

### Dimensioni {#size}
Imposta la dimensione del navigatore.

### Ribalta 180° {#flip-180}
Attiva un comportamento al tocco: se la vista è agganciata, toccando il centro del navigatore la vista ruota di 180 gradi. Per esempio, se la vista è agganciata di fronte, toccando il navigatore passi alla vista posteriore.

### Bordi e angoli {#edges-corners}
Aggiunge viste di aggancio sugli spigoli e sugli angoli (le zone ambrate). Non disponibile con la forma a gnomone.

### Trascinamento a piattaforma girevole {#turntable-drag}
Trascinando il navigatore la vista ruota senza rollio della fotocamera, e si ferma su ogni vista di aggancio. Disattivalo per trascinare il navigatore con la rotazione `Trackball`. In entrambi i casi il trascinamento resta orizzontale o verticale. Con una fotocamera in modalità `Piattaforma girevole`, il navigatore si trascina sempre in questo modo.

### Posizione {#snap-position}
Imposta in quale angolo si trova il navigatore.


## ![](/icons/list.webp) Statistiche {#stats}
![](/images/settings_stats.webp)

Mostra informazioni sulla memoria del sistema, sul numero totale di vertici della scena e sul numero di vertici della selezione attuale.

### Posizione {#stats-position}
Imposta in quale angolo si trovano le statistiche.

## ![](/icons/edit_radius.webp) Maniglia {#handle}
Impostazioni per le maniglie che trascini nella vista, come il gizmo.

### Inserimento numerico {#gizmo-input}
Consente di inserire valori numerici toccando uno dei controlli del gizmo.

### Nascondi durante l'interazione {#hide-on-interaction}
Sfuma il gizmo mentre interagisci con esso, così non ti intralcia.

### ![](/icons/opacity.webp) Opacità {#handle-opacity}
L'opacità delle maniglie.

## ![](/icons/shape_lasso.webp) Forma {#shape-settings}
L'aspetto sullo schermo delle forme che disegni con i tratti a forma (lazo, rettangolo, curva...).

### ![](/icons/opacity.webp) Riempimento, Contorno {#shape-fill-outline}
L'opacità dell'interno della forma e della linea che la circonda.

### Colori {#shape-colors}
Il colore della forma per ogni tipo di strumento: `Maschera`, `Nascondi`, `Gruppo di facce` e `Rifila`.

## ![](/icons/array.webp) Ripetitori {#primitive-repeaters}
Limiti per le copie create dai [ripetitori](scene#repeaters) (array, radiale, curva, superficie). Mantengono Nomad reattivo quando un ripetitore sfugge di mano.

### ![](/icons/cube.webp) Max copie {#repeater-max-copies}
Il numero massimo di copie create da un singolo ripetitore. Nomad fatica con molti oggetti, qualunque sia la loro dimensione.

### ![](/icons/cube.webp) Copie nella scena {#repeater-scene-copies}
Il budget di copie per tutta la scena. Una copia low poly costa poca geometria ma resta un oggetto completo, quindi è questo il limite che le copie piccole raggiungono per primo.

### ![](/icons/triangle.webp) Facce max {#repeater-max-faces}
Il budget di facce per tutte le copie della scena. Oltre questo limite, gli oggetti più pesanti perdono copie per primi.

## ![](/icons/multires.webp) Multirisoluzione {#multires}
### Numero massimo di vertici {#multires-lowres-count}
Imposta una soglia che impedisce una suddivisione multires oltre questo numero di vertici, che probabilmente farebbe crashare Nomad: Nomad non controlla la memoria disponibile prima di suddividere. Il valore predefinito è 10 milioni.
### Soglia di bassa risoluzione {#multires-lowres-threshold}
Quando muovi la fotocamera può essere mostrata una versione a risoluzione più bassa della mesh. Puoi aumentare questo valore se vuoi vedere la mesh a una risoluzione più alta.

## Impostazioni {#advanced}
### ![](/icons/reset.webp) Ripristina valori predefiniti {#reset}
Riporta tutte le preferenze dell'app ai valori predefiniti.

Alcune risorse sono salvate a parte e NON vengono ripristinate: progetti, scorciatoie da tastiera, preset degli strumenti, ambienti HDR, MatCap, alfa, texture dei pennelli e immagini di riferimento. Anche tutto ciò che è salvato con il progetto, come illuminazione, post processing o viste della fotocamera, resta intatto.

# ![](/icons/sliders.webp) Menu Interfaccia {#interface-menu}

Questo menu raccoglie molte opzioni per personalizzare l'interfaccia di Nomad.

![](/images/interface_overview2.webp)

Nomad si può personalizzare in profondità: questo menu è diviso in 5 schede, Interfaccia, Scorciatoie, Gesto, Collegamenti e Debug.

![](/images/interface_menu.webp)


::: tip
Questa pagina riguarda il menu Interfaccia, non l'interfaccia in sé! L'interfaccia nel suo insieme è descritta in [Per iniziare](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interfaccia {#interface}

La scheda Interfaccia controlla il colore, la dimensione e la disposizione dell'interfaccia di Nomad. Ha due sotto-schede, `Aspetto` e `Disposizione`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Colori {#presets}

![](/images/interface_presets.webp)

La sotto-scheda `Aspetto` si apre con una raccolta di preset di colore per l'interfaccia. Toccane uno per applicarlo, poi rifiniscilo con le opzioni qui sotto.

#### Accento e Base {#color-widgetcolor-base}
I colori principali dell'interfaccia: `Accento` per i pulsanti selezionati e le barre dei cursori, `Base` per i pannelli.

#### Opacità testo {#text-opacity}
Attenua il testo e le icone rispetto ai pannelli.

#### Interruttori, Casella di spunta, Schede {#high-contrast-button}
Lo stile degli interruttori (`Morbido` o `Pieno`), delle caselle di spunta (`Bordato`, `Accento` o `Riempimento`) e delle schede (`Sottolineatura`, `Morbido` o `Pieno`).

#### Strumenti colorati {#colored}
Colora le icone per categoria: per esempio tutti gli strumenti di maschera sono marroni, gli strumenti di divisione rossi, quelli di appiattimento verdi, ecc.

#### Ombra pannelli {#material-color-preview}
I pannelli proiettano un'ombra per staccarsi dalla scena.

#### Pannello trasparente {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Quando è attivo, compaiono altre opzioni per controllare l'aspetto dei menu e dei pannelli di Nomad: `Tinta pannelli` ne imposta il colore, `Intensità sfocatura` quanto viene sfocata la scena dietro di loro, e `Vetro` aggiunge rifrazione e riflessi sui bordi, più visibili con una sfocatura bassa.

::: tip
Sui dispositivi piccoli può essere utile rendere la tinta dei pannelli quasi bianca e trasparente, con un'intensità di sfocatura bassa, così i menu non coprono la scena.
:::

#### ![](/icons/reset.webp) Ripristina aspetto {#reset-style}
Riporta tutte le opzioni di aspetto ai valori predefiniti.

### ![](/icons/panel_detach.webp) Disposizione {#layout}

La sotto-scheda `Disposizione` controlla dove si trovano gli elementi e quanto sono grandi.

#### Casella strumenti {#toolbox}

Opzioni per il menu degli strumenti a destra dell'interfaccia di Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Ridimensiona {#ui-resize-corner}

Mostra o nasconde una maniglia di ridimensionamento nell'angolo in basso della casella strumenti.

##### Nascosta {#hidden}
Normalmente l'icona della casella strumenti nella barra superiore alterna tra una lunga colonna singola e un elenco di strumenti su più colonne. Con questa opzione alterna invece tra l'elenco su più colonne e la casella nascosta.

##### Ripristina ordine {#reset-order}
Riporta gli strumenti predefiniti della casella strumenti nell'ordine originale. Le icone personalizzate restano nella casella, in fondo all'elenco.

#### Barra superiore {#rows-auto-1}
`Reattivo` sceglie cosa fa la barra superiore quando non entra nello schermo, soprattutto sugli schermi piccoli: `Multilinea` dispone i menu su più righe, `Scorri` li tiene su una riga che puoi far scorrere.

#### Inverti barra superiore {#mirror-top-bar}
Inverte l'ordine dei menu nella barra superiore.

#### Inverti barre laterali {#mirror-side-bars}
Scambia le barre laterali: la casella strumenti va a sinistra e le opzioni dello strumento a destra.

#### Inverti barra inferiore {#mirror-bottom-bar}
Sposta la barra inferiore nell'angolo in basso a destra e inverte l'ordine dei pulsanti.

#### ![](/icons/move.webp) Trascina pannello {#drag-panel}
Un pannello mobile si sposta sempre trascinandone la barra; questa opzione ti permette di trascinarne anche il corpo. Su `Auto`, un dito o uno stilo spostano il pannello solo se il trascinamento è più orizzontale che verticale, così un trascinamento verticale continua a far scorrere il contenuto. Impostala su `Sì` per trascinare anche con il mouse, in qualsiasi direzione.

#### ![](/icons/pencil.webp) Usa finestra di dialogo Nomad {#use-nomad-dialog}
Mostra la finestra di testo di Nomad invece di quella del sistema quando scrivi un nome o un valore.

#### ![](/icons/stylus.webp) Punto al passaggio {#hover-dot}
Mostra un piccolo punto nell'interfaccia quando viene rilevato uno stilo sospeso sopra lo schermo.

#### ![](/icons/help.webp) Aiuto al passaggio {#help-popup-on-hover}

Sui dispositivi che supportano il passaggio del puntatore, sceglie se l'aiuto contestuale di Nomad, indicato dall'icona ![](/icons/help.webp), compare al passaggio o solo quando lo tocchi.

#### Scala complessiva {#overall-scale}
Un moltiplicatore di dimensione per tutti gli elementi dell'interfaccia.
#### Larghezza pannello {#panel-width}
La larghezza dei menu e dei pannelli.
#### Dimensione font {#font-scale}
Scala i caratteri.
#### Spaziatura verticale {#vertical-spacing}
La spaziatura tra gli elementi nei menu e nei pannelli.
#### Spaziatura verticale (sinistra) {#vertical-spacing-left}
La spaziatura tra gli elementi della barra degli strumenti di sinistra.

#### Spostamenti dei bordi {#edge-offset}
Modifica questi valori solo se hai problemi a usare i pulsanti ai bordi dello schermo. Se questi cursori sono disattivati, Nomad usa i valori dell'area sicura forniti dal dispositivo stesso.

::: tip
Quando trasferisci Nomad su un nuovo dispositivo (per esempio passando da un iPhone 12 a un iPhone 15), ricordati di ripristinare le opzioni dei bordi ai valori predefiniti!
:::

#### ![](/icons/reset.webp) Ripristina disposizione {#reset-layout}
Riporta tutte le opzioni di disposizione ai valori predefiniti.

## ![](/icons/window.webp) Scorciatoie {#shortcuts}

La scheda Scorciatoie sceglie quali pulsanti rapidi compaiono attorno al viewport e ti permette di creare le tue barre degli strumenti mobili.

### Barra laterale {#side-bar}
I pulsanti rapidi degli strumenti in fondo alla barra laterale sinistra: `Leviga`, `Maschera`, `Nascondi`, `Gruppo di facce` e `Gizmo`. Trascinali per cambiarne l'ordine.

### Aggiungi scorciatoie (in basso)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Tocca una scorciatoia per aggiungerla alla barra inferiore, o per toglierla. Queste sono attive per impostazione predefinita:
* `Annulla` - annulla l'ultima operazione
* `Ripeti` - ripristina l'ultima operazione annullata
* `Isolato` - Nasconde temporaneamente tutti gli altri oggetti, lasciando visibile solo quello selezionato. Premi di nuovo per far ricomparire tutti gli oggetti.
* `Raggi X` - Rende temporaneamente semitrasparenti tutti gli altri oggetti, lasciando solido solo quello selezionato. Premi di nuovo per ripristinare i materiali predefiniti.
* `Voxel` - Esegue il remeshing dell'oggetto corrente con l'ultima risoluzione voxel usata. Una pressione lunga o uno scorrimento verso l'alto mostrano un cursore della risoluzione e l'interruttore dei bordi affilati.
* `Griglia` - Mostra o nasconde la griglia della vista. Una pressione lunga o uno scorrimento verso l'alto ti permettono di cambiare il colore e l'opacità della griglia.
* `Wireframe` - Mostra o nasconde il wireframe sovrapposto. Una pressione lunga o uno scorrimento verso l'alto ti permettono di cambiare il colore e l'opacità del wireframe.
* `Ispeziona` - ti permette di vedere alcune proprietà della mesh, come le UV, le texture generate e altre proprietà, sovrapposte allo sfondo di Nomad.
* `Gruppo di facce` - Mostra o nasconde la sovrapposizione dei gruppi di facce, maggiori informazioni in [Strumenti->Gruppo di facce](tools.md#facegroup)

Sono disponibili anche altre scorciatoie di uso comune: `Bordato`, `Proiezione` (prospettica o ortografica), `MatCap`, `DynTopo`, e i pulsanti `Suddividi`, `Rovescia` e dei livelli della [Multirisoluzione](topology.md#multiresolution).

#### ![](/icons/more.webp) Collegamenti {#bindings-list}

Quasi tutte le funzioni di Nomad si possono aggiungere alla barra inferiore tramite il pulsante dei collegamenti, che mostra quante scorciatoie contiene la barra. Toccando il pulsante si apre un menu dei collegamenti:

![](/images/interface_bindings_search.webp)

Puoi cercare per categoria tramite le icone in alto, oppure usare il campo di ricerca per trovare le funzioni per nome. Tocca una funzione per aggiungerla alla barra. Toccala di nuovo per toglierla.

#### ![](/icons/eye_open.webp) Visibile {#order}

Mostra o nasconde l'intera barra inferiore.

#### ![](/icons/reset.webp) Ripristina {#reset}

`Ripristina` riporta la barra inferiore alle impostazioni predefinite.

### Aggiungi scorciatoie (finestra)... {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Toccando il + aggiungi una barra degli strumenti mobile. Non sarà visibile finché non tocchi il pulsante dei collegamenti e ci aggiungi qualche scorciatoia; a quel punto puoi renderla visibile.

Puoi creare tante barre, e ognuna ha una riga con queste opzioni:

* Trascina la maniglia a sinistra di una riga per riordinare le barre.
* `Nome` - Il nome della barra.
* `Visibile` - Mostra o nasconde la barra.
* `Barra` - Mostra una barra del titolo sulla barra degli strumenti.
* `Compatta` - Tiene la barra sullo schermo quando l'interfaccia è compattata.
* `Collegamenti` - Mostra la finestra dei collegamenti per scegliere le funzioni da aggiungere o togliere dalla barra.
* `Elimina` - Elimina la barra.


## ![](/icons/gesture.webp) Gesto {#gesture}
Il menu Gesto controlla come dito, stilo, mouse e trackpad comandano Nomad.

![](/images/interface_gesture.webp)

### Opzioni dei gesti {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad può limitare le operazioni in base al dispositivo di input. Per esempio, trascinare con il dito potrebbe solo muovere la fotocamera, mentre trascinare con lo stilo potrebbe solo scolpire. Se hai un mouse o un trackpad, puoi assegnare anche a loro operazioni specifiche.

Ogni riga è un'operazione: attiva `Dito`, `Stilo` e `Mouse` per scegliere quali input possono eseguirla.

* `Fotocamera` - Muove la fotocamera.
* `Modifica dei nodi` - Trascina le maniglie disegnate nel canvas, per esempio per modificare una primitiva, una curva, un ripetitore o una luce.
* `Scolpire` - Scolpisce con i pennelli. Gli strumenti che hanno una propria riga più sotto seguono quella riga.
* `Seleziona oggetto` - Tocca un oggetto per selezionarlo.
* `Selezione materiale` - Tieni premuto sul canvas per prendere il colore o il materiale sotto il cursore. Funziona solo se il pennello corrente ha la pittura attiva.
* `Tocco` - Le scorciatoie a tocco di strumenti come Maschera, Nascondi e Gruppo di facce (vedi sotto).
* `Pittura` - Gli strumenti Dipingi e Sfumino.
* `Maschera` - Lo strumento Maschera.
* `Faccia` - Gli strumenti Nascondi e Gruppo di facce.
* `Crea` - Gli strumenti Tubo, Lathe e Inserisci.
* `Taglia` - Gli strumenti Rifila, Dividi e Proietta.
* `Seleziona` - Gli strumenti Seleziona e Misura.
* `Gizmo` - Gli strumenti Gizmo e Reticolo.
* `Trasforma` - Gli strumenti Trasforma e Disponi.

::: tip
Una configurazione comune su tablet è lasciare scolpire e dipingere solo allo stilo, e tenere le dita per la fotocamera. Così il palmo o un dito che sfiora lo schermo non lasciano mai un tratto sul modello.
:::

### ![](/icons/tool_smooth.webp) Il dito leviga sempre {#finger-always-smooths}
Quando è attivo, il dito leviga sempre mentre è attivo uno strumento di scultura, qualunque sia il pennello. Attivandolo, `Dito` viene tolto dalla riga `Scolpire`: lo stilo scolpisce e il dito leviga.

### Consenti tratto nel vuoto {#allow-air-stroke}
Permette di iniziare un tratto anche se il cursore tocca prima fuori dalla mesh. Scegli gli strumenti a cui si applica: `Strumento` (tutti gli altri pennelli), `Leviga`, `Maschera` e `Nascondi`. Funziona solo con gli input che possono scolpire ma non muovere la fotocamera, quindi questi pulsanti restano disattivati finché uno dei tuoi input non è impostato così.

### ![](/icons/stroke.webp) Aggancio del tratto {#stroke-snap}
Tieni fermo il puntatore alla fine di un tratto per trasformarlo in una linea dritta o in una curva morbida. Continua a trascinare per ruotare e scalare il tratto agganciato attorno al suo punto di partenza.

`Tempo di pressione` imposta per quanto tempo devi restare fermo prima che il tratto si agganci, o prima che una forma passi in modifica.

### ![](/icons/stylus.webp) Utilizza campioni di input aggiuntivi {#use-extra-input-samples}
Usa i campioni di input aggiuntivi forniti dal dispositivo. Disattivalo se i tuoi tratti sono seghettati o se la pressione si comporta in modo strano. Questa opzione non compare su iOS.

### ![](/icons/tool_mask.webp) Maschera {#mask}

![](/images/interface_gesture_mask.webp)

`Scorciatoie con un tocco` - Attiva le seguenti scorciatoie con un solo tocco, senza dover tenere premuto il pulsante della maschera. Permette questi gesti:
* tocca lo sfondo per invertire la maschera
* tocca un'area mascherata per sfumare la maschera
* tocca un'area non mascherata per rendere più netta la maschera

#### Pressione lunga {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Una pressione lunga con lo strumento Maschera alterna tra il pennello maschera e il lazo (SelMasch.):
* `Pressione lunga - Scolpire` - Tieni premuto, poi continua a trascinare: il tratto viene disegnato con l'altra modalità, e quella precedente torna alla fine del tratto.
* `Pressione lunga - Attiva/Disattiva` - Tieni premuto e rilascia senza muoverti per passare da una all'altra.

### ![](/icons/tool_smooth.webp) Leviga {#smooth}
`Pressione lunga - Lazo` - Una pressione lunga con lo strumento Leviga passa allo strumento Seleziona per la durata del tratto di selezione.

### ![](/icons/tool_hide.webp) Nascondi {#hide}
![](/images/interface_gesture_hide.webp)

`Scorciatoie con un tocco` attiva queste scorciatoie con lo strumento Nascondi:
* Tocca un gruppo di facce per nasconderlo
* Tocca uno spazio vuoto per invertire i poligoni nascosti

### ![](/icons/finger3.webp) Tre dita {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Se il tuo dispositivo supporta i gesti a 3 dita, configura qui le scorciatoie per quel gesto.

La matrice di opzioni ti permette di assegnare il trascinamento verticale e quello orizzontale a scorciatoie diverse, oppure `No` per lasciarlo disattivato. Nota che se lo stesso gesto è scelto per 2 opzioni, una viene disattivata e il suo nome appare barrato.

* `Ruota illuminazione` - Ruota l'ambiente, le luci e la MatCap.
* `Raggio strumento` - Modifica il raggio dello strumento.
* `Intensità strumento` - Modifica l'intensità dello strumento.

### ![](/icons/fingerprint.webp) Cronologia 2/3 {#history-23}
`Cronologia scorciatoie` - quando è attivo, sono disponibili questi gesti:
* Annulla - tocco con 2 dita
* Ripeti - tocco con 3 dita

`Pressione lunga` - quando è attivo, tenendo appoggiate 2/3 dita annulli/ripeti in rapida successione.

### ![](/icons/mouse.webp) Rotella del mouse {#mouse-wheel}
`Velocità (zoom 3d)` imposta quanto velocemente la rotella ingrandisce la vista, e `Velocità (interfaccia 2d)` quanto velocemente fa scorrere i menu e i pannelli. Il pulsante meno accanto a ogni cursore inverte la direzione.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
Su Mac, `Due dita` sceglie cosa fanno due dita sul trackpad. Pizzicare fa sempre zoom e ruotare le dita fa sempre ruotare la vista su sé stessa.
* `Disattivato` - Lo scorrimento a due dita fa zoom, come la rotella del mouse. Le dita non vengono lette singolarmente.
* `Panoramica` - Due dita spostano la vista, e sollevandone una la fai orbitare. Come su un tablet.
* `Orbita` - Due dita fanno orbitare la vista, e sollevandone una la sposti.

### Accessibilità {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Finestra assistiva` apre una barra degli strumenti mobile per controllare trascinamento, pizzico, rotazione e fotocamera.

### Fotocamera {#camera}
Una scorciatoia per andare al menu `Fotocamera` (le opzioni della fotocamera prima si trovavano qui, ma sono state spostate nel menu Fotocamera).

### Doppio tocco Pencil → Collegamenti {#pencil-tap}

Una scorciatoia per andare al menu `Collegamenti`, dove imposti cosa fa il doppio tocco della Pencil. Fuori da iOS diventa `Pulsante stilo → Collegamenti`, per il pulsante dello stilo.

### Rifiuto del palmo {#palm-rejection}
Su telefoni e tablet, ignora i tocchi con un'area di contatto più grande di `Soglia di dimensione massima`, come il palmo della mano appoggiato sullo schermo. Potrebbe non funzionare su tutti i dispositivi: disattivalo se hai problemi a interagire con il canvas.


## ![](/icons/keyboard.webp) Collegamenti {#bindings}
Dal menu Collegamenti puoi definire scorciatoie da tastiera e da pulsante:

![](/images/interface_bindings.webp)
Quasi tutte le funzioni di Nomad si possono collegare a scorciatoie da tastiera, se il tuo dispositivo ne ha una, oppure ai pulsanti aggiuntivi dello stilo, o persino ai gamepad.

Per creare un collegamento, tocca il rettangolo accanto alla funzione e premi il tasto o il pulsante.

Trova le funzioni tramite le icone delle categorie in alto, oppure cercale per nome con la barra di ricerca.

Puoi disattivare i singoli collegamenti con la casella di spunta accanto al loro nome. Tieni premuta la casella e trascina per riordinare l'elenco.

Quando due collegamenti attivi usano la stessa scorciatoia, accanto a loro compare un'icona ![](/icons/help.webp), che elenca le funzioni in conflitto.

### ![](/icons/more.webp) Menu contestuale {#context-menu}
L'icona ![](/icons/more.webp) dopo ogni collegamento apre un menu contestuale:

![](/images/interface_bindings_context.webp)

* `Clona` - Clona il collegamento, per esempio per dare a una funzione una seconda scorciatoia.
* `Ripristina` - Ripristina il collegamento
* `Elimina` - Elimina il collegamento. Possibile solo quando la funzione ha più di un collegamento.

Sotto di loro, alcuni collegamenti hanno opzioni aggiuntive:

* `Tasti permanenti` - Per le scorciatoie degli strumenti e le scorciatoie rapide (Maschera, Leviga, Gizmo, Nascondi, Gruppo di facce, Agg./Sott.), sceglie come la pressione di un tasto cambia strumento. `Auto` usa il valore predefinito impostato nelle opzioni [Avanzato](#advanced).
  * `Tenere premuto` - Tieni premuto il tasto per usare lo strumento, rilascialo per tornare allo strumento precedente.
  * `Attiva/Disattiva` - Premi una volta per cambiare strumento.
  * `Pressione Rapida` - Tieni premuto per usare lo strumento temporaneamente, oppure premi rapidamente per passare a esso.
* `Tieni premuto per annullare` - Per le scorciatoie rapide, sceglie se rilasciare un tasto tenuto premuto riporta sempre allo strumento precedente, anche quando quello strumento era già attivo.
* `Alterna strumento precedente` - Per le scorciatoie degli strumenti, premere la scorciatoia dello strumento corrente riporta all'ultimo strumento usato. Richiede `Tasti permanenti` su `Attiva/Disattiva` o `Pressione Rapida`.
* `Posizione` - Per le scorciatoie delle finestre mobili, apre la finestra dove si trovava (`Mantieni il precedente`) o sotto il cursore (`Sul cursore`).
* `Traslazione (al rilascio)` / `Zoom (al rilascio)` - Per i collegamenti di zoom e spostamento della fotocamera, passa all'altro quando rilasci il tasto.
* Direzione di trascinamento - Per `Ruota illuminazione`, `Raggio strumento` e `Intensità strumento`, sceglie un trascinamento orizzontale o verticale.
* `Sincronizza` - Per le funzioni che aggiungono, clonano o creano istanze di oggetti, sceglie se sincronizzare il risultato. Per impostazione predefinita usa il valore di sincronizzazione impostato nel menu Scena.
* `Sullo sfondo` - Per le scorciatoie rapide Leviga e Maschera, trascina sullo sfondo tenendo premuto il tasto per disegnare un lazo: un lazo di selezione per Leviga, un lazo di maschera per Maschera.
* `Forza telecamera` - Per i collegamenti della fotocamera, muove la fotocamera anche se la stessa scorciatoia è usata da un altro collegamento, di solito una scorciatoia di strumento o Agg./Sott.
* `Rollio lineare` - Per il collegamento del rollio, ruota la vista con un trascinamento orizzontale, verticale o diagonale invece di girare attorno al pivot.

::: tip
Con `Pressione Rapida` un solo tasto fa entrambe le cose: tienilo premuto per una levigatura o una maschera veloce e, quando lo rilasci, torni al tuo pennello; oppure premilo brevemente per restare su quello strumento.
:::

### ![](/icons/cog.webp) Avanzato {#advanced}
In fondo al menu Collegamenti c'è un menu ingranaggio con le opzioni avanzate:

![](/images/interface_bindings_advanced.webp)

* `Scorciatoie rapide` - I valori predefiniti di `Tasti permanenti` e `Tieni premuto per annullare` per le scorciatoie Maschera, Leviga, Gizmo, Nascondi, Gruppo di facce e Agg./Sott.
* `Scorciatoie degli strumenti` - I valori predefiniti di `Tasti permanenti` e `Alterna strumento precedente` per le scorciatoie degli strumenti. Con `Alterna strumento precedente` puoi continuare a passare da uno strumento all'altro con lo stesso tasto.
* `Finestra scorciatoie` - La modalità `Tasti permanenti` delle scorciatoie che mostrano le finestre mobili.
* `Invertire zoom Y` - Inverte la direzione del trascinamento verticale quando fai zoom con un collegamento.
* `Rollio lineare` - Ruota la vista con un trascinamento orizzontale, verticale o diagonale invece di girare attorno al pivot.
* `SpaceMouse` - Attiva il supporto per lo SpaceMouse di 3Dconnexion. Su alcuni sistemi compaiono opzioni aggiuntive: cosa muove (`Oggetto`, `Fotocamera`, `In prima persona`, `Drone`), `Aggiorna pivot automaticamente` per spostare il pivot sulla superficie sotto il cursore quando inizia a muoversi, e le sue velocità di `Traslazione`, `Zoom` e `Rotazione`.
* `Zone morte (drift)` - Per i controller `Gamepad`, `Joystick` e `Pulsante`. Alza questi valori se la fotocamera si muove mentre non tocchi il controller.
* `Raggio strumento` - Come un trascinamento con il collegamento del raggio ridimensiona il pennello (`Cerchio`, `Centrato` o `dx`), poi quanto aggiungono (in pixel) o moltiplicano i collegamenti del raggio a ogni pressione.
* `Intensità strumento` - Quanto aggiungono o moltiplicano i collegamenti dell'intensità a ogni pressione.
* `Fotocamera - Velocità` - La velocità di `Traslazione` e di `Rotazione` dei collegamenti che spostano e ruotano la vista.
* `Ripristina collegamenti` - riporta tutti i collegamenti ai valori predefiniti.
* `Ripristina ordine` - ripristina l'ordine predefinito dell'elenco dei collegamenti.


## Elenco delle scorciatoie da tastiera ⌘ su iOS {#ios-keyboard-shortcuts-display}

Sui dispositivi iOS con tastiera, tieni premuto il tasto ⌘ (cmd) per vedere l'elenco delle scorciatoie.

Il supporto della tastiera su Android è ancora un po' sperimentale.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
Questo menu contiene alcune opzioni sperimentali e di debug. Molte vanno lasciate ai valori predefiniti e modificate solo dopo aver contattato l'assistenza di Nomad. Le icone in alto portano a ciascuna sezione.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalizza UVs` - Nomad normalizza le UV della mesh selezionata dentro la tile [0-1].

### ![](/icons/sun.webp) Shading {#render}
* `Scrivi profondità rifrazione (retro)` - Il retro delle mesh con rifrazione viene scritto nel buffer di profondità.
* `Normali smussate pesate per angolo` - Una correzione del funzionamento dell'ombreggiatura uniforme che in certi casi evita delle pieghe.

### ![](/icons/speed.webp) FPS obiettivo {#target-fps}
Quando è disattivato, Nomad sincronizza i fotogrammi al secondo con la frequenza di aggiornamento del display.

Quando è attivo, puoi impostare i fotogrammi al secondo che Nomad renderizza.

### ![](/icons/window.webp) Interfaccia {#debug-interface}
* `Strumenti: mostra tutti` - Nomad nasconde gli strumenti non pertinenti per la selezione corrente: per esempio tutti i pennelli di scultura sono nascosti sulle primitive non ancora confermate. Questa opzione mostra gli strumenti disattivati in grigio invece di nasconderli.

Le altre opzioni dell'interfaccia che prima si trovavano qui ora sono nella scheda [Interfaccia](#interface).

### ![](/icons/turntable.webp) Piattaforma girevole {#gif-turntable}
Nomad può esportare una GIF animata della piattaforma girevole. Nota che, per i limiti del formato GIF, la qualità è bassa. Di solito una registrazione dello schermo è un metodo migliore.

* `Durata` - quanti secondi dura la rotazione
* `Campionamento fotogrammi max` - Molti degli effetti di rendering di alta qualità di Nomad nascono dalla combinazione di più fotogrammi. Questo cursore imposta quanti fotogrammi combinare, e la sua casella di spunta lo attiva o disattiva.
* `Centro di rotazione` - attorno a cosa ruota la fotocamera: `Mantieni attuale` mantiene il pivot attuale, `(0, 0, 0)` usa il centro del mondo, `Scena` il centro della scena.
* `Sfondo trasparente` - Usa l'opzione di trasparenza per le GIF. Nota che le GIF supportano solo la trasparenza a 1 bit, quindi i bordi possono risultare molto seghettati.
* `Esporta (GIF)` - avvia l'esportazione della GIF.

### ![](/icons/postprocess.webp) Post processing {#post-process}
* `Filtraggio` - Opzione di debug
* `Formato` - Opzione di debug
* `Riutilizza buffer` - Opzione di debug

### ![](/icons/ram.webp) Prestazioni {#performance}
* `Multithread: generale` - Opzione di debug
* `Multithread: scultura` - Opzione di debug
* `Disegna ripetizioni con istanze` - Disegna tutte le copie di un ripetitore in una sola chiamata di disegno. Opzione di debug.

### ![](/icons/star.webp) Funzionalità {#feature}
* `nom: comprimi multirisoluzione` - Riduce la dimensione dei progetti e delle esportazioni Nomad che usano la multirisoluzione. Questi file non si possono aprire con le versioni più vecchie di Nomad. In futuro questa opzione potrebbe sparire ed essere attiva di default.
* `Inverti diagonale quad (al tocco)` - Opzione di debug

### ![](/icons/bug.webp) Debug {#dev}
* `Log` - Apre una finestra con i log
* `Registra eventi` - Scrive nella finestra dei log gli eventi del puntatore (dito, stilo, mouse), per indagare sui problemi di input.
* `FPS` - aggiunge un contatore dei fotogrammi al secondo alle statistiche del viewport.
* `Finestra recensione app` - Opzione di debug, su iOS e Android.

### ![](/icons/image.webp) Icone personalizzate {#custom-icons}
Sostituisci le icone di Nomad con i tuoi file png.
* `Importa icone` - Importa i file png in `tmp_session/icons`. Ognuno sostituisce l'icona di base con lo stesso nome. Vengono eliminati al riavvio di Nomad.
* `Esporta icone strumenti` - Copia le icone di base `tool_<tool>.png` in `tmp_session/icons`, senza sovrascrivere. Puoi modificarle lì e applicarle con `Ricarica icone`.
* `Ricarica icone` - Applica le icone presenti in `tmp_session/icons`.

### Remeshing quad {#quad-remesh}
Le opzioni del remeshing quad non sono più in questo menu: vedi [Remeshing quad](topology.md#quad-remesh-instant) nel menu Topologia e lo strumento [Quad Remesher](tools.md#quad-remesher).

### Crea miniature per lo store {#make-store-thumbnails}
Renderizza screenshot nelle dimensioni adatte all'App Store di iOS.

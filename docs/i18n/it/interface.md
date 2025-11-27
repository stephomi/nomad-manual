# ![](/icons/interface.webp) Menu Interfaccia 

Questo menu controlla molte opzioni per personalizzare l’interfaccia di Nomad. 

![](/images/interface_overview2.webp)

Nomad può essere personalizzato in modo piuttosto approfondito, questo menu è suddiviso in 4 sezioni: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Questa pagina riguarda il menu dell’interfaccia, non l’interfaccia stessa! L’interfaccia generale è descritta in [Getting Started](gettingstarted.md).
:::

## Interface 

La sezione Interface ti permette di aggiungere scorciatoie, creare toolbar flottanti e controllare colore, dimensione e aspetto dell’interfaccia utente di Nomad.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

La toolbar inferiore ha queste scorciatoie abilitate per impostazione predefinita:
* `Undo` - annulla l’operazione precedente
* `Redo` - ripristina l’operazione annullata in precedenza
* `Solo` - Nasconde temporaneamente tutti gli altri oggetti, lasciando visibile solo quello selezionato. Premi di nuovo per ripristinare tutti gli oggetti.
* `X-ray` - Rende temporaneamente tutti gli altri oggetti semitrasparenti, lasciando solo quello selezionato opaco. Premi di nuovo per ripristinare i materiali predefiniti.
* `Voxel remesh` - Esegue il remesh dell’oggetto corrente usando l’ultima risoluzione voxel utilizzata. Una pressione prolungata o uno swipe verso l’alto mostreranno uno slider per la risoluzione e un interruttore per gli spigoli netti.
* `Grid` - Attiva/disattiva la griglia di vista. Una pressione prolungata o uno swipe verso l’alto permetteranno di cambiare colore e opacità della griglia.
* `Wireframe` - Attiva/disattiva una sovrapposizione wireframe. Una pressione prolungata o uno swipe verso l’alto permetteranno di cambiare colore e opacità del wireframe.
* `Inspector` - permette di visualizzare proprietà della mesh come UV, texture bake e altre proprietà, sovrapposte allo sfondo di Nomad.
* `Face Group` - Attiva/disattiva la sovrapposizione dei face group, maggiori informazioni in [Tools->FaceGroup](tools.md#facegroup) 

Altre scorciatoie comunemente usate sono disponibili da questo menu, molte altre si trovano nel pulsante bindings.

#### ![](/icons/more.webp) Bindings

Quasi ogni funzione di Nomad può essere aggiunta alla toolbar delle scorciatoie tramite il pulsante bindings. Quando il pulsante viene premuto, viene mostrato un menu di bindings:

![](/images/interface_bindings_search.webp)

Puoi cercare per categoria tramite le icone in alto, oppure usare il campo di ricerca per trovare le funzioni per nome. Clicca su una funzione per aggiungerla alla toolbar. Clicca di nuovo per rimuoverla.

#### ![](/icons/list.webp) Order

Mostra un elenco delle scorciatoie. Premi a lungo e trascina per riordinare le scorciatoie.

#### ![](/icons/reset.webp) Reset

Reset ripristinerà la toolbar inferiore alle impostazioni predefinite.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

Cliccando il + verrà aggiunta una toolbar flottante. Non sarà visibile finché non clicchi il pulsante bindings e non aggiungi alcune scorciatoie, quindi potrai renderla visibile. 

Puoi creare molte toolbar, ognuna con le seguenti opzioni in questo menu:

* ![](/icons/checked.webp) `Visible` - Attiva/disattiva la visibilità della toolbar
* ![](/icons/more.webp)`Bindings` - Mostra la finestra dei binding per selezionare le funzioni da aggiungere o rimuovere dalla toolbar.
* ![](/icons/list.webp)`Order` - Mostra un menu per riordinare la toolbar.
* ![](/icons/reset.webp) `Reset` - Ripristina la toolbar al suo stato predefinito.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Attiva un handle di ridimensionamento nell’angolo in basso a destra della toolbar.
* ![](/icons/sort_down.webp) `Collapsable` - Attiva un handle di collasso nell’angolo in alto a destra.
* ![](/icons/trash.webp) `Delete` - Elimina la toolbar.

### Toolbox

Opzioni per il menu degli strumenti sul lato destro dell’interfaccia di Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Attiva un handle di ridimensionamento nell’angolo inferiore della toolbar.

#### Hidden
Normalmente l’icona della toolbox nella barra superiore alterna tra una singola colonna lunga o un elenco multi-colonna di strumenti. Questa opzione alterna tra l’elenco multi-colonna o la modalità nascosta.

#### Colored
Codifica a colori le icone per categoria, ad esempio tutti gli strumenti di maschera sono marroni, gli strumenti di split sono rossi, quelli di flatten verdi ecc.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Ripristina gli strumenti predefiniti nella toolbox al loro ordine originale. Le icone personalizzate rimarranno nella toolbox alla fine dell’elenco.


### Presets

![](/images/interface_presets.webp)

Una raccolta di preset di colore per l’interfaccia.

#### High-contrast button
Uno stile alternativo per i pulsanti che li rende più visibili quando sono abilitati. Se impostato su Auto, Nomad userà questa modalità quando il contrasto di colore dell’interfaccia tra abilitato/disabilitato è basso.

#### Color widget/Color base
I colori principali usati nell’interfaccia.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Quando abilitato, appariranno opzioni extra per controllare l’aspetto di menu e pannelli in Nomad. È possibile regolarne colore, trasparenza e quantità di sfocatura.

::: tip
Su dispositivi piccoli può essere utile rendere il pannello dei colori quasi bianco, trasparente e con bassa sfocatura, così i menu non oscureranno la scena.
:::

----

### Mirror top bar
Inverte l’ordine dei menu nella barra superiore.

### Mirror side bars
Scambia le barre laterali in modo che la toolbox sia a sinistra e le opzioni dello strumento a destra.

### Mirror bottom bar
Sposta la barra inferiore nell’angolo in basso a destra e inverte l’ordine dei pulsanti.

### Material color preview
Quando selezioni un colore per un materiale, un’anteprima di questo materiale viene visualizzata sull’oggetto attualmente selezionato.

----
### Help popup on hover

Per i dispositivi che supportano l’hover, abilita se l’aiuto contestuale in Nomad rappresentato dall’icona ![](/icons/help.webp) apparirà al passaggio del cursore o solo quando cliccato.

----

### Overall scale
Un moltiplicatore di dimensione per tutti gli elementi dell’interfaccia.
### Panel width
La larghezza di menu e pannelli.
### Font scale
Scala dei font.
### Vertical spacing
La spaziatura verticale tra gli elementi in menu e pannelli.
### Vertical spacing (left)
La spaziatura verticale tra gli elementi nella toolbar sinistra.

----

### Edge offset
Dovresti modificare questi valori solo se hai problemi a interagire con i pulsanti sui bordi dello schermo. Se questi slider sono disabilitati, Nomad userà i valori di area sicura restituiti dal dispositivo stesso.

::: tip
Quando migri Nomad su un nuovo dispositivo (ad es. sostituendo un iPhone 12 con un iPhone 15), assicurati di reimpostare le opzioni dei bordi ai valori predefiniti!
:::

### Reset style
Ripristina tutti gli elementi dell’interfaccia ai valori predefiniti.


## Gesture
Il menu Gesture controlla come penna e dita comandano Nomad.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad può limitare le operazioni in base al dispositivo di input. Per esempio, un trascinamento con il dito può solo muovere la camera, mentre un trascinamento con la penna può solo scolpire. Se hai un mouse o un trackpad, anche questi possono essere assegnati a operazioni specifiche.

Attualmente Nomad ti permette di impostare queste modalità per essere controllate da qualsiasi combinazione di gesture con dito, penna o mouse:

* Camera
* Sculpt
* Gizmo
* Material picking (tramite pressione prolungata)
* Select object


`Finger always smooths` - Smooth può essere impostato per funzionare solo con un trascinamento del dito.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Abilita le seguenti scorciatoie con un singolo tap senza dover tenere premuto il pulsante mask. Permetterà i seguenti gesti:
* tap sullo sfondo per invertire la maschera
* tap su un’area mascherata per sfumare la maschera
* tap su un’area non mascherata per rendere più netta la maschera

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Una pressione prolungata attiverà il passaggio tra Mask e SelMask e inizierà una nuova pennellata. Alla fine della pennellata verrà riselezionato lo strumento precedente. 
* `Tool` - Pressione prolungata e rilascio senza muovere per passare tra Mask e SelMask. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` abiliterà le seguenti scorciatoie con lo strumento hide:
* Tap su un face group per nasconderlo
* Tap nello spazio vuoto per invertire i poligoni nascosti

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Se il tuo dispositivo supporta gesture a 3 dita, configura le scorciatoie per quella gesture. 

La matrice di opzioni ti permette di definire trascinamenti verticali e orizzontali come scorciatoie separate. Nota che se la stessa gesture è scelta per 2 opzioni, una verrà disabilitata.

* `Rotate lighting` - Ruota environment, luci e Matcap.
* `Tool Radius` - Modifica il raggio dello strumento.
* `Tool Intensity` - Modifica l’intensità dello strumento. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - quando abilitato, le seguenti gesture sono attive:
* Undo - tap con 2 dita
* Redo - tap con 3 dita

`Long press` - quando abilitato, tenere premute 2/3 dita eseguirà rapidamente undo/redo.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` farà apparire una toolbar flottante per controllare drag, pinch, roll e operazioni della camera.

### Camera
Una scorciatoia per andare al menu `Camera` (le opzioni della camera erano qui, ma sono state spostate nel menu camera).

### Pencil double tap -> Bindings 

Una scorciatoia per andare al menu `Bindings` (le opzioni per il tap e double tap della Pencil erano qui, ma sono state spostate nel menu bindings).


## Bindings
Le scorciatoie da tastiera e pulsante possono essere definite dal menu bindings:

![](/images/interface_bindings.webp)
Quasi tutte le funzioni in Nomad possono essere associate a scorciatoie da tastiera se il tuo dispositivo ha una tastiera, o a pulsanti extra sulla penna, o persino a controller di gamepad.

Per creare un binding, clicca il rettangolo accanto alla funzione e premi il tasto/pulsante. 

Trova le funzioni tramite le icone di categoria in alto o tramite la barra di ricerca per nome. 

I singoli binding possono essere disabilitati tramite la casella di spunta accanto al nome del binding.

### ![](/icons/more.webp) Context menu
L’icona ![](/icons/more.webp) dopo ogni binding apre un menu contestuale:

![](/images/interface_bindings_context.webp)

* `Clone` - Clona il binding
* `Reset` - Reimposta il binding
* `Delete` - Elimina il binding
* `Toggle shortcut on key tap` - Configura se un tap rispetto a una pressione prolungata vengono trattati in modo diverso. Quando abilitato, un tap attiverà lo strumento. Una pressione prolungata attiverà lo strumento solo mentre il tasto è premuto, al rilascio si tornerà allo strumento precedente. A volte chiamato “sticky keys” in altre app 3D.

### Advanced
In fondo al menu bindings c’è un menu a ingranaggio per le opzioni avanzate:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Un tap delle scorciatoie standard per mask, smooth, gizmo, hide, sub passerà a quella modalità, ma tenendo premuto il tasto si passerà a quella modalità solo finché il tasto è premuto, poi al rilascio si tornerà alla modalità precedente. A volte chiamato “sticky keys” in altre app 3D.
* `Toggle tool shortcuts` - Quando si usa una delle scorciatoie degli strumenti, se la stessa scorciatoia viene premuta due volte, passerà allo strumento precedente. In questo modo puoi continuare a scambiare tra due strumenti con la stessa hotkey.
* `Invert Y (Zooming)` - Inverte lo zoom
* `Reset bindings` - reimposta tutti i binding ai valori predefiniti.


## iOS ⌘ Visualizzazione scorciatoie da tastiera

Su dispositivi iOS con tastiera, tieni premuto il tasto ⌘ (cmd) per visualizzare un elenco di scorciatoie.

Il supporto per tastiera su Android è un po’ sperimentale.

![](/images/shortcuts.webp)


## Debug
Alcune opzioni sperimentali e di debug sono memorizzate in questo menu. Molte di queste opzioni dovrebbero essere lasciate ai valori predefiniti e modificate solo dopo aver contattato il supporto Nomad.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad normalizzerà le UV all’interno della tile [0-1].

### Quad Remesh
* `Instant Mesh` - Abilita l’algoritmo di remesh istantaneo
* `Quadriflow` - Un metodo alternativo di quad remesh.

### Render
* `Heightmap` - Cambia il viewport per renderizzare la profondità della scena. Può essere usato per creare alpha map da usare per i pennelli.
* `Refraction write depth (back)` - Il retro delle mesh con rifrazione verrà scritto nel depth buffer.
* `Flip Y (normal map)` - Inverte il canale y durante il baking delle normal map, richiesto per alcuni motori di gioco e di rendering.
* `Angle weighted smooth normals` - Una regolazione del funzionamento dello smooth shading che può evitare pieghe in alcuni casi.

### Target FPS
Quando disabilitato, Nomad sincronizzerà i fotogrammi al secondo con la frequenza di aggiornamento del display.

Quando abilitato, puoi impostare i fotogrammi al secondo che Nomad renderizzerà.

### Interface
* `Top: layout` 
  * Collapse: Su dispositivi piccoli la barra superiore verrà compressa in più sottomenu. 
  * Scroll: Se sei abituato a Nomad su schermi grandi e preferisci il layout normale, abilitando questa opzione verrà usata la barra superiore ampia standard, che potrà essere scrollata.
  * Multiline: Mostra l’intero menu superiore su più righe.
* `Bottom: draggable popup` - La toolbar inferiore ha diversi pulsanti che aprono una finestra di dialogo. Se questa opzione è abilitata, tali finestre possono essere spostate altrove sullo schermo.  
* `Toolbox: show all` - Nomad nasconderà gli strumenti non rilevanti per la selezione corrente, ad esempio tutti i pennelli di sculpt sono nascosti sui primitivi non validati. Questa opzione attenuerà gli strumenti disabilitati invece di nasconderli.
* `Toolbox: colored` - Codifica a colori le icone della toolbox in base al loro tipo.
* `Panel: Drop shadows` - Disegna ombre portate attorno a menu e pannelli. Su alcuni dispositivi più vecchi può influire sulle prestazioni.
* `Panel: Blending` - Opzione di debug
* `Pointer: hovering dot` - Per i dispositivi che supportano l’hover della penna, mostra un punto quando la penna è in hover su menu e pannelli.

### Gif turntable
Nomad può esportare una turntable animata in formato gif. Nota che, a causa dei limiti del formato gif, la qualità è bassa. La registrazione dello schermo è di solito un metodo migliore.

* `Duration` - durata in secondi della turntable
* `Rotation center` - dove si trova il pivot della camera, quindi quale parte della scena la camera ruoterà attorno
* `Transparent background` - Usa l’opzione trasparente per le gif. Nota che le gif supportano solo trasparenza a 1 bit, quindi i bordi possono risultare molto aliasati.
* `Max frame sampling` - Molti degli effetti di rendering di alta qualità di Nomad derivano dalla combinazione di diversi fotogrammi. Questo slider imposta quanti fotogrammi combinare.
* `Export (GIF)` - avvia il processo di esportazione gif.

### Post Process
* `Filtering` - Opzione di debug
* `Format` - Opzione di debug
* `Buffer reuse` - Opzione di debug

### Performance
* `Multicore general` - Opzione di debug
* `Multicore sculpting` - Opzione di debug
* `Partial Drawing` - Funzionalità sperimentale! Usala se stai scolpendo una parte relativamente piccola di una mesh ad alta densità di poligoni. Dovrebbe rendere lo sculpt più fluido, ma non dovresti abilitare il wireframe! Inoltre potrebbe introdurre artefatti visivi durante le pennellate.

### Feature
* `Flip quad split (on tap)` -  Opzione di debug
* `Join: merge radius` - I vertici verranno automaticamente saldati se sono sufficientemente vicini quando le mesh vengono unite. Puoi regolare il raggio con questo slider.

### Debug
* `Logs` - Mostra una finestra di log
* `App review popup` - Opzione di debug
* `FPS` - aggiunge un contatore di fotogrammi al secondo alle statistiche del viewport.

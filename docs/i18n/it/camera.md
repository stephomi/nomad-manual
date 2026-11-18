# ![](/icons/camera.webp) Fotocamera {#camera}

Questo menu ti permette di creare e modificare le fotocamere, e di controllare come interagisci con esse.

![](/images/camera_overview2.webp)

In Nomad le fotocamere hanno diversi usi:

* Preparare delle viste per scolpire da angolazioni precise
* Inquadrare i tuoi oggetti come con una vera macchina fotografica
* Esplorare la scena come una fotocamera in prima persona
* Come fotocamera ortografica, per i giochi isometrici o per un rendering in stile disegno tecnico.

## Controllare la fotocamera {#control}

### Rotazione {#rotation}
Ruoti la fotocamera trascinando *un* dito sullo sfondo.
Se invece trascini il dito sul modello, inizi a scolpire.

::: tip Posso ruotare la fotocamera se non riesco a raggiungere lo sfondo?
Sì: appoggia *due* dita sullo schermo, come per iniziare un gesto di spostamento/zoom, poi solleva *un* dito.
:::

### Fuoco / Ripristina {#focus}
*Tocca due volte* il modello per centrare la vista sul punto toccato.
Se invece *tocchi due volte* lo sfondo, la fotocamera si centra sulla mesh selezionata o su tutta la scena, vedi [Tocca due volte sullo sfondo](#dtap-tap-background).


### Traslazione {#translation}
Muovendo *due* dita, sposti la fotocamera lateralmente.


### Zoom {#zooming}
Con il gesto di pizzico puoi ingrandire o rimpicciolire.


### Rollio {#rolling}
Puoi far *rollare* la vista ruotando *due* dita.
::: warning
Questo gesto è disponibile solo con le modalità di rotazione `Trackball`.
:::

### Controlli da computer {#desktop}

Sul computer, la fotocamera si controlla con il tasto alt/opt:

* trascinare la punta nello spazio vuoto = ruota la fotocamera
* alt+trascinare la punta = sposta
* alt+trascinare la punta, poi rilasciare alt = zoom (come in ZBrush)

Con le tavolette Wacom che hanno 2 o più pulsanti sulla penna, configura la punta e i pulsanti così dalle impostazioni Wacom:

* punta = clic sinistro
* pulsante inferiore = clic centrale
* pulsante superiore = clic destro

Con queste impostazioni puoi manovrare la fotocamera solo con la penna:

* pulsante superiore e penna sospesa in movimento = ruota la fotocamera
* pulsante inferiore e penna sospesa in movimento = sposta

## Controlli della fotocamera {#camera-controls}

![](/images/camera_list.webp)

### Viste {#views}
Puoi salvare dei punti di vista della fotocamera con `Aggiungi vista`.
Toccando il nome della vista, la fotocamera torna a quella vista.


::: tip
Una vista salvata memorizza le impostazioni del [Tipo di proiezione](#projection) e anche l'[immagine di riferimento](background.md).  
È utile se vuoi passare tra viste di riferimento frontale/sinistra/posteriore con sfondi diversi.
:::

| Azione      | Icona                         | Descrizione                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilità  | ![](/icons/eye_open.webp)    | Attiva o disattiva la fotocamera. Le fotocamere nascoste vengono saltate dai pulsanti precedente/successiva |
| Nome        |                               | Seleziona la fotocamera                                                     |
| Immagine    | ![](/icons/image.webp)       | Una miniatura dell'immagine di riferimento, se è collegata alla fotocamera  |
| Proiezione  | ![](/icons/perspective.webp) | La proiezione della fotocamera, con il suo campo visivo quando è in prospettiva |
| Aggiorna vista | ![](/icons/update_view.webp) | Aggiorna la vista salvata con il punto di vista attuale                  |
| Modifica nome | ![](/icons/pencil.webp)    | Modifica il nome della fotocamera                                           |
| Elimina     | ![](/icons/trash.webp)       | Elimina la fotocamera                                                       |

### ![](/icons/camera_add.webp) Aggiungi vista {#add}
Crea una nuova fotocamera a partire dalla vista attuale.

### ![](/icons/camera.webp) Icone {#icons-test}

Mostra o nasconde le icone delle fotocamere nella vista. Il pulsante compare accanto ad `Aggiungi vista` quando hai almeno una fotocamera. Se una fotocamera è selezionata, la sua icona è sempre visibile.

### Tipo di proiezione {#projection}
Scegli tra `Prospettiva` e `Ortografica`.

In prospettiva puoi cambiare il `Campo visivo verticale` (FoV) della fotocamera. Sopra il cursore è indicata la lunghezza focale equivalente di una fotocamera 35mm, comodo se sei abituato alla fotografia.
Per scolpire si consiglia di solito un FoV basso, perché aiuta a valutare le proporzioni.  
La modalità `Ortografica` equivale più o meno a un FoV pari a 0.

### In prima persona {#fps}
Solo in prospettiva. Mette il pivot direttamente sulla fotocamera invece che sulla scultura. Trascinando un dito sullo sfondo, la posizione della fotocamera resta bloccata ma ne cambia la rotazione, come nei giochi in prima persona. Utile quando scolpisci ambientazioni invece di singoli oggetti.

![](/images/camera_rotation_ortho_view.webp)

### Tipo di rotazione {#rotation-type}
Di default la fotocamera usa la modalità di rotazione `Piattaforma girevole`.
Hai solo due gradi di libertà: è più intuitiva, ma in certi casi vorrai più flessibilità.  
Puoi passare a `Trackball`, che ti permette di far *rollare* la vista ruotando *due* dita nella vista. Ci sono due modalità `Trackball`: la prima fa rollare la vista come una sfera sotto il dito, mentre la seconda (con l'icona delle frecce) ruota la vista in base al movimento orizzontale e verticale del trascinamento, cosa che ad alcuni potrebbe risultare più familiare.

### Aggancio ortografico {#orthographic}

Quando è attivo, se hai una tastiera, tenendo premuto Shift mentre ruoti la vista la fotocamera si aggancia alla vista frontale/posteriore/superiore/inferiore/sinistra/destra più vicina e diventa ortografica. La fotocamera diventa ortografica anche quando tocchi il cubo di navigazione per agganciarti a una vista frontale/posteriore/sinistra/destra/superiore/inferiore.

### Reimposta vista {#reset}

Porta la fotocamera di fronte e inquadra tutta la scena nella vista

### Aggancia vista {#snap}
Si aggancia alla vista frontale/posteriore/sinistra/destra/superiore/inferiore più vicina. Se sei già in una di queste viste, toccando di nuovo ruoti di 180 gradi verso il lato opposto.

### Velocità {#speed}

Se ti sembra che la fotocamera si muova troppo lentamente o troppo velocemente, puoi impostare un moltiplicatore di velocità per `Rotazione`, `Zoom` e `Traslazione`. Utile se la tua scultura è molto grande o molto piccola.

### Il pivot {#pivot}

Quando ruoti la fotocamera vedi un puntino rosa: è il punto di pivot della fotocamera.  
È molto importante capire dove si trova il pivot, così non ti perdi e la fotocamera non ti fa impazzire.

Di default il pivot viene aggiornato da queste operazioni:
- toccare due volte il modello
- toccare due volte lo sfondo (il nuovo pivot sarà al centro della mesh)
- appoggiare *due* dita sullo schermo (spostamento/zoom/rollio) aggiorna il pivot al centro delle *due* dita

### Aggiorna pivot... {#update-pivot}

Puoi personalizzare ulteriormente l'aggiornamento del pivot con queste opzioni:

* `Quando si muove la camera` - Aggiorna il pivot quando inizi a interagire con la fotocamera.
* `Consenti pivot nel vuoto` - Consente un nuovo pivot anche quando zoomi fuori dalla superficie dell'oggetto. Richiede `Quando si muove la camera`.
* `Al doppio tocco` - Aggiorna il pivot di rotazione quando tocchi due volte la superficie dell'oggetto.
* `Scolpire (Tratto)` - Aggiorna il pivot quando scolpisci.

::: tip
Quando ci avrai fatto l'abitudine, puoi nascondere il puntino rosa (l'indicatore) dai menu [Impostazioni](settings.md).
:::

### Centra la vista quando si zooma indietro {#center-view-when-zooming-out}
Quando zoomi indietro, la fotocamera non si sposta lateralmente: arretra soltanto, così la vista resta centrata.

### Tocca due volte l'oggetto {#dtap-object}
Quando è attivo, toccare due volte un oggetto centra la fotocamera sul punto toccato.

### Tocca due volte sullo sfondo {#dtap-tap-background}
Quando è attivo, toccare due volte lo sfondo centra la fotocamera su:
* `Selezione` - Gli oggetti selezionati.
* `Scena` - Tutta la scena.
* `Attiva/Disattiva` - Passa dall'una all'altra a ogni doppio tocco. Ci sono due opzioni `Attiva/Disattiva`, che differiscono per quale viene prima, come mostrano le loro icone.

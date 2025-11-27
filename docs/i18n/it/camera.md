# ![](/icons/camera.webp) Fotocamera

Questo menu consente di creare e modificare le fotocamere, oltre a controllare come interagisci con esse.

![](/images/camera_overview2.webp)

Le fotocamere in Nomad hanno diversi utilizzi:

* Impostare viste per scolpire da angolazioni precise
* Usarle come una fotocamera per inquadrare i tuoi oggetti
* Come fotocamera in prima persona per navigare nella scena
* Come fotocamera ortografica per giochi isometrici o rendering in stile industriale.

## Controllare la fotocamera

### Rotazione
Ruoti la fotocamera trascinando *un* dito sullo sfondo.
Se trascini il dito sul modello, verrà invece avviata l’operazione di scultura.

::: tip Posso ruotare la fotocamera se non riesco a raggiungere lo sfondo?
Sì, puoi appoggiare *due* dita sullo schermo - come se volessi iniziare un gesto di pan/zoom - e poi sollevare *un* dito.
:::

### Messa a fuoco / Reset
*Doppio tocco* sul modello per mettere a fuoco il punto selezionato.
Se fai *doppio tocco* sullo sfondo, la fotocamera metterà a fuoco la mesh selezionata.

### Traslazione
Muovendo *due* dita puoi effettuare il pan della fotocamera.

### Zoom
Usando il gesto di pizzico puoi effettuare lo zoom avanti/indietro.

### Rotazione sull’asse di vista (Roll)
Puoi *ruotare* la vista ruotando *due* dita.
::: warning
Questo gesto è disponibile solo per la modalità di rotazione `trackball`.
:::

### Controlli da desktop

Su desktop, il tasto alt/opt viene usato per controllare la fotocamera:

* tip drag nello spazio vuoto = ruota la fotocamera
* alt+tip drag = pan
* alt+tip drag, poi rilasciare alt = zoom (come in ZBrush)

Con tavolette Wacom che hanno 2 o più pulsanti sulla penna, usa le impostazioni Wacom per configurare la punta e i pulsanti in questo modo:

* tip = clic sinistro
* rocker inferiore = clic centrale
* rocker superiore = clic destro

Con queste impostazioni, puoi manipolare la fotocamera solo con la penna:

* rocker superiore e movimento in hover = ruota la fotocamera
* rocker inferiore e movimento in hover = pan

## Controlli fotocamera

![](/images/camera_list.webp)

### Viste
Puoi salvare punti di vista della fotocamera usando `Add View`.
Se fai clic sul nome della vista, la fotocamera ripristinerà quella vista.

::: tip
Una vista salvata memorizzerà le impostazioni del [Tipo di proiezione](#projection-type) e anche l’[Immagine di riferimento](background.md).  
Può essere utile se vuoi passare ciclicamente tra viste di riferimento frontali/sinistra/retro con sfondi diversi.
:::

|   Azione    | Icona                         | Descrizione                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilità  | ![](/icons/eye_open.webp)    | Attiva/disattiva la fotocamera. Le fotocamere nascoste saranno saltate dai pulsanti precedente/successivo |
| Nome        |                               | Seleziona la fotocamera                                                     |
| Immagine    | ![](/icons/image.webp)       | Miniatura di un’immagine di riferimento se è collegata alla fotocamera      |
| Aggiorna vista | ![](/icons/update_view.webp) | Aggiorna la vista salvata con l’attuale punto di vista                  |
| Modifica nome | ![](/icons/pencil.webp)    | Modifica il nome della fotocamera                                           |
| Elimina     | ![](/icons/trash.webp)       | Elimina la fotocamera                                                       |

### ![](/icons/tool_view.webp) Add View
Crea una nuova fotocamera basata sulla vista corrente.

### ![](/icons/camera.webp) Icons

Attiva/disattiva la visibilità delle icone delle fotocamere nel viewport. Se una fotocamera è selezionata, la sua icona è sempre visibile.

### Projection Type
Puoi modificare il `Field of View` (FOV / lunghezza focale) della fotocamera.
Di solito è consigliato usare un FOV basso per scopi di scultura, poiché può aiutare con le proporzioni.  
Puoi anche usare la modalità `Orthographic`, che è più o meno simile a un FOV pari a 0.

### First Person
Abilita l’impostazione del pivot direttamente sulla fotocamera, invece che sulla scultura. Trascinando un dito sullo sfondo la posizione della fotocamera rimarrà bloccata, ma cambierà la rotazione, in modo simile ai giochi in prima persona. Utile quando si scolpiscono ambienti piuttosto che singoli oggetti.

![](/images/camera_rotation_ortho_view.webp)

### Rotation Type
Per impostazione predefinita la fotocamera usa la modalità di rotazione `Turntable`.
Significa che hai solo due gradi di libertà, è più intuitiva ma in alcuni casi potresti volere più flessibilità.  
Puoi passare a `Trackball`, potrai *ruotare* la vista ruotando *due* dita sul viewport. Su desktop esiste una modalità trackball alternativa che potrebbe risultare più familiare ad alcuni utenti.

### Orthographic snap

Quando è abilitata, se hai una tastiera tenere premuto shift mentre ruoti la vista farà agganciare la fotocamera alla vista frontale/posteriore/superiore/inferiore/sinistra/destra più vicina e renderà la fotocamera ortografica. La fotocamera verrà inoltre resa ortografica quando il cubo di vista viene cliccato per agganciare a front/back/left/right/top/bottom.

### Reset view

Sposta la fotocamera sul fronte e adatta la scena alla vista.

### Snap view
Aggancia alla vista frontale/posteriore/sinistra/destra/superiore/inferiore più vicina. Se ti trovi già in una di queste viste, facendo clic di nuovo verrà effettuato uno snap di 180 gradi al lato opposto.

### Speed

Se senti che la fotocamera si muove troppo lentamente o troppo velocemente, puoi impostare un moltiplicatore di velocità per `rotation`, `translation` e `zooming`. Utile se la tua scultura è molto grande o molto piccola.

### Panoramica del pivot

Quando ruoti la fotocamera puoi vedere un piccolo punto rosa, questo è il punto di pivot della fotocamera.  
È molto importante capire dove si trova il pivot per non perderti o sentirti frustrato dai movimenti della fotocamera.

Per impostazione predefinita il pivot viene aggiornato tramite queste operazioni:
- doppio tocco sul modello
- doppio tocco sullo sfondo (il nuovo pivot sarà al centro della mesh)
- appoggiare *due* dita sullo schermo (pan/zoom/roll) aggiornerà il pivot al centro delle *due* dita

### Update Pivot...

Puoi personalizzare ulteriormente l’aggiornamento del pivot con queste opzioni:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Quando ti ci sarai abituato, puoi nascondere il punto rosa (di suggerimento) andando nei menu delle [Impostazioni](settings.md).
:::

### Double tap on object
Quando `Focus` è abilitato, il doppio tocco sposterà il pivot sull’oggetto toccato.

### Double tap on background
Quando è abilitato, imposta il pivot su una delle opzioni Selection, Scene, oppure alterna tra di esse.

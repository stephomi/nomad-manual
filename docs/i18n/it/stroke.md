# ![](/icons/pencil.webp) Tratto {#stroke}

---
![](/images/stroke_overview.webp) 

## Panoramica {#overview}

Puoi personalizzare il comportamento del tratto per la maggior parte dei pennelli degli strumenti.
Le impostazioni sono simili a quelle presenti nelle applicazioni di pittura 2D, tuttavia alcune opzioni sono specifiche per lo sculpting e il 3D.

Le opzioni sono suddivise in 5 sottomenu:

| Nome     | Icona                        | Descrizione                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Controlla come il tratto viene applicato al modello                |
| Alpha    | ![](/icons/alpha.webp)      | Come viene usata una texture in scala di grigi per l’impronta del pennello |
| Falloff  | ![](/icons/falloff.webp)    | Controlla come la forza del pennello cambia dal centro al bordo    |
| Filter   | ![](/icons/filter.webp)     | Come il pennello è influenzato dalla geometria del modello         |
| Pressure | ![](/icons/pressure.webp)   | Controlla la risposta alla pressione della penna                   |

::: tip
Non tutte le opzioni di tratto si applicano a tutti gli strumenti. Le opzioni di tratto che non sono usate dallo strumento corrente saranno disabilitate o nascoste. 
:::


## Tratto {#stroke-1}

### Raggio {#radius}

![](/images/stroke_radius.webp)

#### Condividi raggio {#share-radius}

Quando è abilitato, tutti gli strumenti useranno lo stesso raggio; l’impostazione predefinita è che ogni strumento abbia il proprio raggio.

#### Dimensione {#size}

* Schermo - il raggio è impostato in unità schermo. Se imposti il raggio a 100 pixel di larghezza, rimarrà di 100 pixel indipendentemente dallo zoom.
* Costante (3D) - il raggio è impostato in unità 3D. Per esempio, se crei una sfera e imposti il raggio alla stessa dimensione della sfera, il raggio rimarrà della stessa dimensione della sfera mentre fai zoom in e out.


### Tratto {#stroke-type}

![](/images/stroke_strokemode.webp)

I tratti possono funzionare in più modalità:

### ![](/icons/stroke_dot.webp) Punto {#dot}
Trascina come un normale tratto di pittura. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rotolamento {#roll}
L’alpha del pennello verrà ruotata per seguire la direzione del tratto, utile per creare cuciture di tessuto. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Blocca + raggio
 Applica un’impronta di pennello con **_altezza_** fissa. Il trascinamento imposta scala e rotazione.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Blocco + intensità {#lock-intensity}
Applica un’impronta di pennello con **_raggio_** fisso. Il trascinamento imposta altezza e rotazione.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Gli strumenti `Move` e `Drag` hanno 3 opzioni proprie:

### ![](/icons/snake.webp) Trascina {#drag}

Continuerà ad aggiornare ciò che è all’interno del raggio del pennello durante il tratto. Un tratto veloce lascerà indietro la superficie, mentre un tratto lento tratterrà il materiale, creando forme più lunghe. Questa è la modalità predefinita per lo strumento `Drag`. Con la `Dynamic Topology` può essere usato per creare estrusioni simili a serpenti. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Afferra {#grab}
Selezionerà ciò che è all’interno del raggio del pennello quando il pennello viene avviato, e manterrà quella selezione. È utile per operazioni di spostamento più precise, poiché puoi regolare con cura la distanza dello spostamento senza muovere accidentalmente più di quanto selezionato inizialmente. Questa è la modalità predefinita per lo strumento `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Blocco + raggio (trascina) {#lock-radius-drag}
Il raggio impostato dall’utente viene ignorato e viene impostato dinamicamente in base a quanto il tratto viene trascinato lontano dal punto di partenza. Distanza piccola = raggio piccolo, distanza maggiore = raggio più grande. Usa il cursore di intensità per controllare la forma del falloff. Utile per abbozzare forme organiche e gommose.
![](/videos/stroke_lockradius_drag.mp4) 



### Regola intensità spaziatura {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

I tratti con una spaziatura bassa (inferiore al 50%) possono accumularsi rapidamente, rendendo i tratti più intensi rispetto a valori di spaziatura più alti. Questa opzione compenserà questo effetto, così i tratti avranno approssimativamente la stessa intensità indipendentemente dalla spaziatura.

### Spaziatura tratto {#stroke-spacing}
Quanto distanziare l’applicazione di ogni impronta di pennello durante un’operazione di trascinamento. Valori inferiori al 100% si sovrapporranno, dando l’impressione di un tratto continuo. Valori superiori al 100% inizieranno a lasciare spazi, utili per scolpire dettagli come cuciture o cerniere.

### Stabilizzatore «lazy rope» {#lazy-rope-stabilizer}
I tratti rimarranno indietro rispetto alla posizione del puntatore di una certa distanza. Può essere usato per disegnare linee fluide.
![](/videos/stroke_lazy_rope.mp4) 

### Levigatura tratto {#stroke-smoothing}
Media più posizioni del puntatore per ottenere un tratto più fluido.
Con valori alti, il tratto rimarrà indietro rispetto al puntatore ma alla fine lo raggiungerà.
È utile per disegnare linee morbide.

### Raggio di aggancio {#snap-radius}
Aggancia l’inizio del tratto alla fine del tratto precedente. Il raggio determina quanto lontano cercare la fine del tratto precedente. Può essere utile quando si disegnano linee lunghe e continue, facendo pause frequenti.

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
Per impostazione predefinita i tratti influenzeranno solo la superficie del modello all’interno del raggio del pennello. Quando la silhouette è abilitata, il tratto verrà proiettato attraverso l’intero modello. Può essere molto utile durante il blocco iniziale di un modello, o per forme che richiedono lati che rimangano perpendicolari.

La direzione di proiezione può essere impostata esplicitamente; il metodo predefinito “Closest” rileverà il miglior angolo rispetto alla vista. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Randomizza {#randomize}

![](/images/stroke_randomize.webp)

L’intensità, la traslazione, la rotazione e la scala del tratto possono essere ognuna randomizzate. Questo può essere usato per creare una serie di effetti, ad esempio la randomizzazione con lo strumento paint può creare colore maculato, oppure la randomizzazione con lo strumento crease può essere usata per creare dettagli della pelle.

![](/videos/stroke_randomize.mp4) 

### Offset tratto {#stroke-offset}

Applica un offset costante al tratto. È utile per schermi piccoli dove il dito coprirebbe il tratto. 


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

L’`Alpha` è una texture che modula il comportamento del pennello.
È un’immagine in scala di grigi, dove i pixel neri significano nessuna deformazione e i pixel bianchi deformazione completa.

Tocca l’immagine dell’alpha per cambiarla.

Tocca l’anteprima del materiale per caricare un’alpha da un preset di materiale. Puoi anche salvare preset di materiale qui e scegliere di incorporare le texture con lo strumento.

::: tip
La texture non viene mai ridimensionata, quindi texture grandi possono rallentare le prestazioni.
:::

### Inverti pixel {#invert-pixels}
Questo invertirà i valori dell’immagine, quindi i pixel neri diventeranno bianchi e quelli bianchi diventeranno neri.

::: tip

Le alpha integrate fornite con Nomad non possono essere invertite.

:::

### Scalatura {#scaling}

La dimensione del pennello in Nomad è un cerchio con un raggio definito dall’utente. Le texture sono spesso quadrate o rettangolari; i parametri di `Scaling` ti permettono di decidere come la texture deve adattarsi all’interno del cerchio. Per una texture quadrata, un valore di 0.7 la farà rientrare nel cerchio. Un valore di 1 scalerà la texture più grande in modo che il cerchio rientri al suo interno, tagliando i bordi.

![](/images/alpha_scaling.webp) 

Abilitando `Scaling - Y` potrai stirare l’alpha verticalmente.

![](/images/alpha_scaling_y.webp) 

### Rotazione {#rotation}

La texture alpha verrà ruotata per seguire la direzione del tratto. Puoi aggiungere un offset di rotazione e, se l’icona del lucchetto è abilitata, la texture rimarrà bloccata a questa rotazione rispetto allo schermo.

### Piastrellatura {#tiling}
![](/images/stroke_tiling.webp) 

Con quale frequenza la texture si ripete all’interno del profilo del pennello. Le modalità di tiling ti permettono di limitarti a una singola texture all’interno del tratto, a texture ripetute, oppure a texture specchiate dove ogni seconda texture è ribaltata per creare pattern o aiutare a rendere le texture senza giunzioni.

![](/videos/alpha_tiling.mp4) 



### Valore medio {#mid-value}

Per impostazione predefinita i pixel neri significano nessuna deformazione e i pixel bianchi significano deformazione positiva completa, quindi per esempio, un pennello clay con una texture alpha di rocce tirerà fuori la superficie solo dove l’alpha non è nera.

Se vuoi che il pennello spinga la superficie verso l’interno, o che spinga verso l’interno E tiri verso l’esterno, puoi modificare il valore medio. Se imposti il valore a 0.5, un grigio medio nell’alpha non farà nulla, un valore nero spingerà verso l’interno, il bianco tirerà verso l’esterno.




## Decadimento {#falloff}

![](/images/falloff_menu.webp) 

È simile all’[Alpha](#alpha), tranne per il fatto che controlli l’intensità con una singola curva. Questa viene combinata con l’alpha in modo che tu possa usare una texture per i dettagli e il falloff per controllare la sfumatura del bordo e l’intensità al centro dello strumento.

Quando la curva è in alto, c’è deformazione completa; quando è in basso il pennello non ha effetto.

Puoi pensare alla curva come a una sezione trasversale attraverso la punta del pennello. La sezione inferiore mostra un’anteprima di come apparirebbe una singola “impronta” del pennello sulla superficie del modello e, se c’è una texture alpha per il pennello, verrà mostrata anche questa per vedere in anteprima come interagiranno falloff e alpha.

### Preset {#preset}
Con questa opzione selezionata, toccando il grafico della curva verrà visualizzato un menu di preset. Le curve arrotondate daranno risultati più morbidi, le curve angolari avranno risultati più netti. Il pulsante `Sub` nella barra degli strumenti a sinistra invertirà di fatto il falloff, così la parte alta della curva spingerà nella superficie invece di tirare fuori, o viceversa.

### Catmull-Rom {#catmull-rom}
Quando è selezionato, l’utente può disegnare le proprie curve di falloff. L’editor di curve funziona come le curve nel resto di Nomad:

* Tocca la curva per creare un nuovo punto
* Trascina un punto per riposizionarlo
* Tocca un punto per alternare tra spigolo vivo e morbido
* Trascina un punto sopra un punto vicino per rimuoverlo

### B-spline {#b-spline}
Quando è selezionato, l’utente può disegnare le proprie curve di falloff. L’editor funziona come per Catmull-Rom, ma i punti di curva influenzano la curva invece di trovarsi direttamente su di essa, il che può aiutare a creare forme di curva più morbide.

L’editor di curve ha 3 pulsanti:

| Voce     | Icona                       | Descrizione                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Espande l’editor di curve                    |
| Reset    | ![](/icons/reset.webp)     | Riporta la curva allo stato predefinito      |
| Symmetry | ![](/icons/symmetric.webp) | Mostra la curva come una “punta di pennello” simmetrica |


### Influenza {#influence}

* Sfera (3D) - L’influenza è calcolata prendendo la distanza dal vertice al centro del pennello.
* Cerchio (2D) - Il vertice viene prima proiettato sul piano dell’area, prima di calcolare la sua distanza dal centro del pennello. È simile a come vengono campionate le alpha. 
* Cilindro - L’influenza è proiettata attraverso l’area come un cilindro, usato dalla modalità Silhouette qui sotto.

### Silhouette {#silhouette-1}
Per impostazione predefinita i tratti influenzeranno solo la superficie del modello all’interno del raggio del pennello. Quando la silhouette è abilitata, il tratto verrà proiettato attraverso l’intero modello. Può essere molto utile durante il blocco iniziale di un modello, o per forme che richiedono lati che rimangano perpendicolari.



## Filtro {#filter}

![](/images/filter_menu.webp) 

### Accumula tratto {#accumulate-stroke}
Abilita l’assenza di limite a quanto materiale può essere aggiunto/rimosso per tratto. Ad esempio lo strumento `Clay` ha questa opzione abilitata, quindi il materiale può continuare ad accumularsi, mentre lo strumento `Brush` ce l’ha disabilitata, quindi i tratti smetteranno di aggiungere materiale se continui a passare lo stesso tratto sulla stessa regione della mesh. 

### Solo vertici frontali {#front-facing-vertex-only}
Questa opzione ignorerà i vertici rivolti all’indietro.
Può essere utile se vuoi dipingere una parte di una geometria sottile senza influenzare l’altro lato.
Funziona anche per lo sculpting ma potresti riscontrare alcuni artefatti.

### Consenti topologia dinamica {#allow-dynamic-topology}
Questa opzione è disponibile solo se la tua mesh è in modalità [Dynamic Topology](topology.md#dynamic-topology). Puoi disabilitare o abilitare la topologia dinamica per singolo strumento.

### Topologia connessa {#connected-topology}
Abilita lo sculpting solo sui vertici che sono collegati alla superficie che tocchi con lo strumento. Per esempio, quando usato con lo strumento `Move`, ti permetterà di spostare una parte anche se interseca con un’altra parte.
![](/videos/connected_topology.mp4)

### Proteggi area {#protect-area}
![](/images/filter_protect_area.webp) 

Queste opzioni impediranno agli strumenti di influenzare parti della mesh in varie condizioni. 

L’opzione “Auto” significa che se hai hide, mask o facegroup visibili nel menu [Shading](shading), saranno protetti, ma se sono disattivati in quel menu, la protezione è disabilitata.

* `All` - Imposta se i filtri di protezione sono globali o per singolo strumento.
* `Hide` - Se parti della mesh sono nascoste con lo strumento hide, imposta se devono essere protette.
* `Mask` - Se parti della mesh sono mascherate, imposta se devono essere protette.
* `Facegroup` - Imposta se puoi usare uno strumento solo all’interno del primo facegroup toccato.


### Mantieni spigoli vivi {#keep-sharp-edges}
Esclude i punti i cui normali differiscono troppo dalla normale della superficie.

Cambierà il modo in cui viene calcolata l’area del piano (Area sampling).

Questa opzione può essere utile per strumenti basati su flatten, o se vuoi colorare una superficie per lo più piatta senza sbavature.

![](/videos/filter_keep_sharp_edges.mp4)

### Campionamento area {#area-sampling}
Alcuni pennelli o opzioni di tratto richiedono una normale di piano e una posizione di piano sulla superficie per funzionare.

Puoi controllare come calcolare questo piano medio impostando l’area di campionamento come rapporto del raggio dello strumento.

Al 100%, ogni punto all’interno del cerchio di selezione viene preso in considerazione.

A 0%, viene preso in considerazione solo il vertice o il triangolo più vicino. Questi valori possono essere collegati sia per `Normal radius` che per `Position radius`, oppure sbloccati e impostati in modo indipendente.


### Mascheratura profondità {#depth-masking}
![](/images/stroke_depthmask.webp)

Esclude i punti che sono al di sopra o al di sotto di una certa distanza dal piano calcolato (Area sampling).

Può essere usato per dipingere solo sulle zone in rilievo o solo sulle cavità.

Il grafico rappresenta una sezione trasversale della superficie; la linea orizzontale è dove si trova la superficie, il cerchio rappresenta il raggio di falloff della pittura relativo sopra e sotto la superficie. `Height offset` è una percentuale sopra o sotto la superficie da cui iniziare il calcolo del masking. `Top area` e `Bottom area` ti permettono di scalare il falloff sopra e sotto il punto di offset.

#### Esempio: Dipingi nelle cavità {#example-paint-in-cavities}
Per dipingere solo le regioni in cavità, imposta l’height offset a -100% e regola il cursore top area in modo che sia distante dalla linea orizzontale. Questo significa che il primo clic imposta la profondità “zero” e poi solo le aree al di sotto di questa profondità verranno influenzate.

![](/videos/stroke_depth_cavity.mp4)

#### Esempio: Dipingi sui rigonfiamenti {#example-paint-on-bumps}
Per dipingere solo nelle zone alte, imposta l’height offset a +90%, in modo che il fondo del cerchio intersechi la linea orizzontale di una piccola quantità. Quando clicchi sulla cima di una zona “alta”, questo imposterà la profondità, così che tutto ciò che si trova a quella profondità, più un po’ al di sotto, e tutto ciò che è più in alto, verrà dipinto. Le cavità profonde verranno saltate.
![](/videos/stroke_depth_bump.mp4)


## Pressione {#pressure}
![](/images/pressure_menu.webp) 

Controlla come la pressione della penna/stylus influenza i pennelli.

Per impostazione predefinita `Use global settings` è abilitato, il che significa che tutti i pennelli condivideranno gli stessi valori di pressione.

### Pressione - Raggio {#pressure-radius}

Questa curva controlla come il raggio del pennello è influenzato dalla pressione. Il valore predefinito è una relazione lineare, quindi se il tuo stylus ha una risposta fluida, anche il cambiamento di raggio dovrebbe risultare fluido. Detto ciò, molte penne hanno una risposta non lineare, che puoi compensare con questa curva. Per esempio, se il raggio non sembra raggiungere il suo valore massimo ad alta pressione, usa un preset di curva come “out-pow3”, con una piega verso l’alto, per aumentare il raggio prima.

Questa finestra di dialogo è simile alla visualizzazione della curva di falloff; puoi usare un preset toccando la finestra della curva, oppure disegnare le tue curve con le modalità Catmull-Rom e B-Spline.

Se vuoi un raggio costante, disabilita questa sezione.

### Pressione - Intensità {#pressure-intensity}

Simile al cursore del raggio, ma per controllare l’intensità. Se vuoi un’intensità costante, disabilita questa sezione.

### Levigatura pressione {#pressure-smoothing}

Media gli eventi di pressione della penna per risultati più uniformi.
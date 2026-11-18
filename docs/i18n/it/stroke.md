# ![](/icons/brush.webp) Tratto {#stroke}

---
![](/images/stroke_overview.webp) 

## Panoramica {#overview}

Puoi personalizzare il comportamento del tratto della maggior parte dei pennelli degli strumenti.
Le impostazioni sono simili a quelle delle app di pittura 2d, ma alcune opzioni sono specifiche della scultura e del 3d.

Le opzioni sono divise in 5 sottomenu:

| Nome     | Icona                        | Descrizione                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Tratto   | ![](/icons/brush.webp)      | Controlla come il tratto viene applicato al modello                |
| Alfa     | ![](/icons/alpha.webp)      | Come una texture in scala di grigi viene usata per l'impronta del pennello |
| Decadimento | ![](/icons/falloff.webp) | Controlla come la forza del pennello varia dal centro al bordo     |
| Filtro   | ![](/icons/filter.webp)     | Come il pennello è influenzato dalla geometria del modello         |
| Pressione | ![](/icons/pressure.webp)  | Controlla la risposta alla pressione dello stilo                   |

::: tip
Non tutte le opzioni del tratto valgono per tutti gli strumenti. Quelle che lo strumento corrente non usa sono disattivate o nascoste.
:::


## ![](/icons/brush.webp) Tratto {#stroke-1}

### ![](/icons/radius.webp) Raggio {#radius}

![](/images/stroke_radius.webp)

Le opzioni del raggio sono impostazioni globali: valgono per tutti gli strumenti.

#### Spazio {#size}

* `Schermo` - il raggio è espresso in unità dello schermo. Se imposti un raggio di 100 pixel, resterà di 100 pixel sia che tu ingrandisca sia che tu rimpicciolisca la vista.
* `Mondo (3D)` - il raggio è espresso in unità 3d. Per esempio, se crei una sfera e dai al raggio la stessa dimensione della sfera, il raggio resterà grande quanto la sfera mentre ingrandisci o rimpicciolisci la vista.

#### ![](/icons/link.webp) Sincronizza scorciatoia {#sync-shortcut}

Se attivata, le impostazioni di raggio e silhouette restano sincronizzate quando passi ai pennelli di scorciatoia (`Leviga`, `Maschera` o `Nascondi`). Così una rapida passata di levigatura o di maschera usa la stessa dimensione del pennello dello strumento che stavi usando.

#### ![](/icons/link.webp) Condividi raggio {#share-radius}

Se attivata, tutti gli strumenti usano lo stesso raggio. Di base, ogni strumento ha il proprio raggio.


### Tipo di tratto {#stroke-type}

![](/images/stroke_strokemode.webp)

I tratti possono funzionare in diverse modalità:

### ![](/icons/stroke_dot.webp) Punto {#dot}
Trascina come in un normale tratto di pittura.
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rotolamento {#roll}
L'alfa del pennello ruota per seguire la direzione del tratto, utile per creare le cuciture di un tessuto.
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Blocco + raggio {#lock-radius}
Applica un'impronta del pennello con **_altezza_** fissa. Trascinando imposti la scala e la rotazione.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Blocco + intensità {#lock-intensity}
Applica un'impronta del pennello con **_raggio_** fisso. Trascinando imposti l'altezza e la rotazione.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Le modalità `Blocco + raggio` e `Blocco + intensità` ignorano le impostazioni di [Pressione](#pressure), perché è già il trascinamento a impostare la dimensione e la forza.
:::

![](/images/stroke_strokemodemove.webp)

Gli strumenti `Sposta` e `Trascina` hanno 3 opzioni proprie:

### ![](/icons/snake.webp) Trascina {#drag}

Aggiorna di continuo ciò che si trova nel raggio del pennello durante il tratto. Un tratto veloce lascia indietro la superficie, mentre un tratto lento trattiene il materiale, creando forme più lunghe. È la modalità predefinita dello strumento `Trascina`. Con la `Topologia dinamica` puoi usarla per creare estrusioni a forma di serpente.
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Cattura {#grab}
Seleziona ciò che si trova nel raggio del pennello all'inizio del tratto e mantiene quella selezione. È utile per spostamenti più precisi: puoi regolare con cura la distanza dello spostamento senza rischiare di muovere più di quanto avevi selezionato. È la modalità predefinita dello strumento `Sposta`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Blocco + raggio (trascinamento) {#lock-radius-drag}
Il raggio scelto viene ignorato e si imposta dinamicamente in base a quanto trascini il tratto lontano dal punto di partenza: piccola distanza = raggio piccolo, distanza maggiore = raggio più grande. Usa il cursore dell'intensità per controllare la forma del decadimento. Utile per abbozzare forme organiche e gommose.
![](/videos/stroke_lockradius_drag.mp4) 

Alcuni altri strumenti elencano qui i propri tipi di tratto, per esempio `Rilassa`, `Leviga` e `Sfumino` per gli strumenti di levigatura, o forme come `Lazo` e `Curva` per gli strumenti basati su una selezione. Sono descritti con ciascuno [strumento](tools.md).


### Regola l'intensità della spaziatura {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

I tratti con una spaziatura bassa (sotto il 50%) si accumulano in fretta e risultano più intensi di quelli con una spaziatura più alta. Questa opzione compensa l'effetto, così i tratti hanno più o meno la stessa intensità qualunque sia la spaziatura.

### Spaziatura tratto {#stroke-spacing}
La distanza tra un'impronta e l'altra durante un trascinamento. Sotto il 100% le impronte si sovrappongono e danno l'aspetto di un tratto continuo. Sopra il 100% iniziano a lasciare degli spazi, utili per scolpire dettagli come cuciture o cerniere.

### Stabilizzatore di corda ritardato {#lazy-rope-stabilizer}
Il tratto segue il puntatore a una certa distanza, come se fosse tirato da una corda. Serve a disegnare linee morbide.
![](/videos/stroke_lazy_rope.mp4) 

### Levigatura tratto {#stroke-smoothing}
Fa la media di più posizioni del puntatore per ottenere un tratto più morbido.
Con valori alti il tratto resta indietro rispetto al puntatore, ma finisce per raggiungerlo.
È utile per disegnare linee morbide.

### Raggio di aggancio {#snap-radius}
Aggancia il tratto al precedente quando il puntatore parte vicino al punto in cui è finito l'ultimo tratto. Il raggio indica fino a che distanza cercare la fine del tratto precedente. Può servire per disegnare lunghe linee continue facendo spesso delle pause.

### ![](/icons/trail.webp) Scia {#trail}

Se attivata, ogni nuova impronta riapplica anche gli ultimi punti del tratto alle sue spalle. `Conteggio scia` imposta quanti punti vengono riapplicati, `Intensità scia` quanto sono forti e `Raggio scia` di quanto si ingrandiscono.

La scia funziona solo con il tipo di tratto `Punto`, e non con l'[influenza del decadimento](#influence) `Cresta`.

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
Di base i tratti agiscono solo sulla superficie del modello compresa nel raggio del pennello. Con la silhouette attiva, il tratto viene proiettato attraverso tutto il modello. È molto utile per abbozzare le forme iniziali di un modello, o per forme i cui lati devono restare perpendicolari.

Puoi scegliere la direzione di proiezione:

* `X`, `Y`, `Z` - proietta lungo un asse fisso.
* `Vista` - proietta lungo la direzione della fotocamera.
* `Se agganciato` - proietta lungo la direzione della fotocamera, ma solo quando la fotocamera è agganciata a una vista. Altrimenti il tratto resta normale.
* `Più vicino` - proietta lungo l'asse più vicino alla direzione della fotocamera. È l'opzione predefinita.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomizza {#randomize}

![](/images/stroke_randomize.webp)

`Intensità`, `Spostamento`, `Rotazione` e `Scala` del tratto possono essere resi casuali ciascuno per conto proprio. Usa la casella di ogni riga per attivarla o disattivarla. Puoi ottenere tanti effetti diversi: per esempio, la casualità con lo strumento di pittura crea un colore screziato, mentre con lo strumento solco permette di creare i dettagli della pelle.

`Periodo (più lento)` imposta la durata del ciclo casuale: aumentalo per variazioni lente e ondulate, diminuiscilo per un rumore rapido. Il piccolo pulsante accanto a ogni riga modifica il periodo solo per quella riga.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Randomizza - HSV {#randomize-hsv}

Per gli strumenti che dipingono, anche `Tonalità`, `Saturazione` e `Valore` del colore possono essere resi casuali, con un periodo proprio. Perfetto per aggiungere sottili variazioni di colore alla pelle o alla pietra.

### Spostamento tratto {#stroke-offset}

Applica uno spostamento costante al tratto, così il dito non lo copre. È utile sugli schermi piccoli. È un'impostazione globale: attivala con la sua casella e varrà per tutti gli strumenti.

## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

L'`Alfa` è una texture che modula il comportamento del pennello.
È un'immagine in scala di grigi, in cui i pixel neri indicano nessuna deformazione e quelli bianchi la deformazione massima.

Tocca l'immagine dell'alfa per cambiarla. Oltre agli alfa integrati e a quelli che importi tu, l'elenco degli alfa può anche scaricare mappe di displacement da Poly Haven.

Tocca l'anteprima del materiale per caricare un alfa da un preset di materiale. Qui puoi anche salvare i preset di materiale e scegliere di incorporare le texture nello strumento.

::: tip
La texture non viene mai ridimensionata, quindi le texture grandi possono rallentare le prestazioni.
:::

### ![](/icons/blend_contrast.webp) Correggi alfa {#invert-pixels}
Il pulsante `Correggi...` di un alfa importato apre un popup che corregge l'immagine stessa: il valore medio, l'inversione dei pixel (il nero diventa bianco e il bianco diventa nero), una rotazione di 90° e un ribaltamento orizzontale o verticale. Il file dell'immagine viene riscritto, quindi anche le altre app vedono l'immagine corretta.

::: tip

Gli alfa integrati forniti con Nomad non si possono correggere.

:::

### Proiezione {#projection}

Come l'alfa viene proiettato sul modello:

* `Superficie` - l'alfa si appoggia alla superficie sotto il pennello, seguendone l'orientamento.
* `Schermo` - l'alfa è proiettato direttamente dalla vista.
* `Tassello` - l'alfa è proiettato dalla vista e resta fermo mentre ci dipingi sopra, come uno stencil, così un motivo ripetuto si raccorda senza giunture. La rotazione è bloccata e la pressione della penna non cambia la dimensione del motivo.
* `Triplanare` - l'alfa è proiettato lungo i 3 assi. Le opzioni di ridimensionamento, rotazione e tiling qui sotto sono sostituite dalle impostazioni della texture triplanare.

### ![](/icons/diagonal.webp) Ridimensionamento {#scaling}

In Nomad il pennello è un cerchio con un raggio a tua scelta. Le texture invece sono spesso quadrate o rettangolari: i parametri di `Ridimensionamento` ti permettono di decidere come la texture deve stare nel cerchio. Per una texture quadrata, un valore di 0.7 la fa stare dentro il cerchio. Un valore di 1 la ingrandisce in modo che sia il cerchio a starci dentro, tagliandone i bordi.

![](/images/alpha_scaling.webp) 

Attivando `Ridimensionamento Y` puoi allungare l'alfa in verticale. Il primo cursore diventa allora `Ridimensionamento X`.

![](/images/alpha_scaling_y.webp) 

`Rifletti orizzontalmente` specchia l'alfa da sinistra a destra.

### Rotazione {#rotation}

La texture alfa ruota per seguire la direzione del tratto. Puoi aggiungere uno scostamento di rotazione e, se l'icona del lucchetto è attiva, la texture resta bloccata su questa rotazione rispetto allo schermo.

Il pulsante a forma di penna accanto fa ruotare l'alfa quando ruoti lo stilo su se stesso (barrel roll), con i tratti `Blocco + raggio` e `Blocco + intensità` e la rotazione sbloccata. Funziona solo con gli stili che lo supportano.

### Tiling {#tiling}
![](/images/stroke_tiling.webp) 

Quante volte la texture si ripete nel profilo del pennello. Le modalità `Tiling - X` e `Tiling - Y` permettono di limitarsi a una sola texture nel tratto (`Nessuno`), di ripeterla (`Ripeti`), oppure di specchiarla ribaltando una texture su due per creare motivi o aiutare a rendere le texture senza giunture (`Specchia`). Sono disponibili con il tratto `Rotolamento`, la proiezione `Tassello` o un `Tiling` superiore a 1.

`Aderente (immagini non quadrate)` conta solo per gli alfa e le texture del pennello non quadrati. Se attivata, ogni immagine si ripete per conto proprio, senza spazi. Disattivala per mantenere l'alfa e le altre immagini sincronizzati quando le loro proporzioni sono diverse.

![](/videos/alpha_tiling.mp4) 



### Valore medio {#mid-value}

Di base i pixel neri indicano nessuna deformazione e quelli bianchi la deformazione positiva massima: per esempio, un pennello argilla con una texture alfa di rocce tirerà fuori la superficie solo dove l'alfa non è nero.

Se vuoi che il pennello spinga la superficie verso l'interno, o che la spinga dentro E la tiri fuori, puoi modificare il valore medio. Se lo imposti a 0.5, un grigio medio nell'alfa non fa nulla, il nero spinge verso l'interno e il bianco tira verso l'esterno.

Due pulsanti ti aiutano a trovare il valore giusto: il pulsante quadrato legge il valore medio dal bordo dell'immagine, e il contagocce ti permette di prelevarlo direttamente sull'alfa.




## ![](/icons/falloff.webp) Decadimento {#falloff}

![](/images/falloff_menu.webp) 

È simile all'[Alfa](#alpha), ma qui l'intensità è guidata da una sola curva. Si combina con l'alfa, così puoi usare una texture per il dettaglio e il decadimento per controllare la sfumatura del bordo e l'intensità al centro dello strumento.

Quando la curva è in alto la deformazione è massima, quando è in basso il pennello non ha effetto.

Puoi immaginare la curva come una sezione della punta del pennello. La parte inferiore mostra un'anteprima di come apparirebbe una singola "impronta" del pennello sulla superficie del modello e, se il pennello ha una texture alfa, mostra anche quella, per farti vedere come decadimento e alfa interagiscono.

### ![](/icons/fx.webp) Preset {#preset}
Con `Preset...` selezionato, toccando il grafico della curva si apre un menu di preset. Le curve arrotondate danno risultati più morbidi, quelle spigolose risultati più netti. Il pulsante `Sub` nella barra degli strumenti a sinistra inverte di fatto il decadimento, quindi la parte alta della curva spinge dentro la superficie invece di tirarla fuori, o viceversa.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Con questa opzione puoi disegnare le tue curve di decadimento. L'editor funziona come le curve nel resto di Nomad:

* Tocca la curva per creare un nuovo punto
* Trascina un punto per spostarlo
* Tocca un punto per passare da spigoloso a morbido e viceversa
* Trascina un punto su un punto vicino per eliminarlo

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Con questa opzione puoi disegnare le tue curve di decadimento. L'editor funziona come Catmull-Rom, ma i punti influenzano la curva invece di trovarsi direttamente su di essa, il che aiuta a ottenere forme più morbide.

### ![](/icons/curve_bevel.webp) Smusso {#bevel}
I punti sono uniti da linee rette, con angoli arrotondati la cui dimensione dipende dalla nitidezza di ciascun punto. Comodo per pennelli con la cima piatta e un bordo smussato pulito.

L'editor della curva ha 3 pulsanti:

| Elemento | Icona                       | Descrizione                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Ingrandisci | ![](/icons/maximize.webp) | Espande l'editor della curva                |
| Ripristina | ![](/icons/reset.webp)   | Riporta la curva allo stato predefinito      |
| Simmetria | ![](/icons/symmetric.webp) | Mostra la curva come una "punta di pennello" simmetrica |


### Influenza {#influence}

* `Sfera` (3d) - l'influenza si calcola dalla distanza tra il vertice e il centro del pennello.
* `Cerchio` (2d) - il vertice viene prima proiettato sul piano dell'area, poi si calcola la sua distanza dal centro del pennello. È simile al modo in cui vengono campionati gli alfa.
* `Cilindro` - l'influenza è proiettata attraverso l'area come un cilindro. Equivale ad attivare la [Silhouette](#silhouette-1) qui sotto.
* `Cresta` - il decadimento si misura di traverso rispetto al tratto, quindi la curva diventa la sezione dell'intero tratto. Il pulsante `Simm` specchia allora il profilo da un lato all'altro del tratto: modifichi un lato e l'altro lo segue. Quando è spento, la curva va dal lato sinistro del tratto al lato destro. Non disponibile per gli strumenti basati sull'appiattimento.

### ![](/icons/silhouette.webp) Silhouette {#silhouette-1}
Di base i tratti agiscono solo sulla superficie del modello compresa nel raggio del pennello. Con la silhouette attiva, il tratto viene proiettato attraverso tutto il modello. È molto utile per abbozzare le forme iniziali di un modello, o per forme i cui lati devono restare perpendicolari. Ha le stesse opzioni di proiezione della [Silhouette](#silhouette) della scheda Tratto.



## ![](/icons/filter.webp) Filtro {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Accumulazione tratto {#accumulate-stroke}
Toglie ogni limite alla quantità di materia che un tratto può aggiungere o togliere. Per esempio, lo strumento `Argilla` ha questa opzione attiva, quindi il materiale continua ad accumularsi, mentre lo strumento `Pennello` ce l'ha disattivata, quindi il tratto smette di aggiungere materiale se continui a ripassare sulla stessa zona della mesh.

### ![](/icons/culling.webp) Solo vertice frontale {#front-facing-vertex-only}
Questa opzione ignora i vertici rivolti all'indietro.
Può servire se vuoi dipingere una parte di una geometria sottile senza toccare l'altro lato.
Funziona anche per scolpire, ma potresti notare qualche artefatto.

### ![](/icons/eye_open.webp) Solo vertici visibili {#visible-vertex-only}
Ignora i vertici nascosti dietro altre superfici, visti dalla fotocamera. Questa opzione compare per i tratti a forma (lazo, rettangolo...) degli strumenti di maschera, di pittura, `Gruppo di facce` e `Nascondi`.

### ![](/icons/dynamic.webp) Permetti topologia dinamica {#allow-dynamic-topology}
Questa opzione è disponibile solo se la mesh è in modalità [Topologia dinamica](topology.md#dynamic-topology). Puoi attivare o disattivare la topologia dinamica per ogni strumento.

### ![](/icons/connect.webp) Topologia collegata {#connected-topology}
Scolpisce solo i vertici collegati alla superficie che tocchi con lo strumento. Per esempio, con lo strumento `Sposta` puoi spostare una parte anche se si interseca con un'altra.
![](/videos/connected_topology.mp4)

### Proteggi l'area {#protect-area}
![](/images/filter_protect_area.webp) 

Queste opzioni impediscono agli strumenti di agire su alcune parti della mesh in diverse situazioni. Ognuna può essere impostata su `Auto`, `No` o `Sì`, e la piccola freccia mostra a cosa corrisponde `Auto` in quel momento.

* `Nascondi` - se alcune parti della mesh sono nascoste con lo strumento nascondi, imposta se devono essere protette. Su `Auto` le facce nascoste sono protette, a meno che il loro wireframe sia visibile (vedi le impostazioni [Wireframe](settings.md#wireframe)).
* `Maschera` - se alcune parti della mesh sono mascherate, imposta se devono essere protette. Su `Auto` le parti mascherate sono protette finché la maschera è visibile nel menu [Shading](shading).
* `Gruppo di facce` - imposta se puoi usare uno strumento solo all'interno del primo gruppo di facce toccato. Su `Auto` dipende dalla visibilità dei gruppi di facce nel menu [Shading](shading).

Il pulsante `(All)` imposta se queste protezioni sono globali, condivise da tutti gli strumenti, o impostate per ogni strumento.


### Campionamento area {#area-sampling}
Alcuni pennelli o opzioni del tratto hanno bisogno della normale e della posizione di un piano sulla superficie per funzionare.

Puoi controllare come viene calcolato questo piano medio impostando l'area di campionamento come percentuale del raggio dello strumento.

Al 100%, viene considerato ogni punto all'interno del cerchio di selezione.

Allo 0%, viene considerato solo il vertice o il triangolo più vicino. Questi valori possono essere collegati per `Raggio normale` e `Raggio posizione`, oppure sbloccati e impostati separatamente.

### Filtro normale area {#keep-sharp-edges}
Esclude i punti le cui normali si discostano troppo dalla normale della superficie.

Cambia il modo in cui viene calcolato il piano dell'area (Campionamento area), quindi è utile soprattutto per gli strumenti argilla o basati sull'appiattimento, o se vuoi colorare una superficie quasi piatta senza sbordare.

Gli angoli `Min` e `Max` controllano la sfumatura tra i punti esclusi e quelli pienamente interessati, come mostra il piccolo disco colorato accanto.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtro normale falloff {#falloff-normal-filter}
Come il [Filtro normale area](#keep-sharp-edges), esclude i punti le cui normali si discostano troppo dalla normale della superficie, ma agisce sul decadimento del pennello invece che sul calcolo del piano. È utile per dipingere solchi o rilievi.


### Filtro profondità {#depth-masking}
![](/images/stroke_depthmask.webp)

Esclude i punti che si trovano sopra o sotto una certa distanza dal piano calcolato (Campionamento area).

Puoi usarlo per dipingere solo sulle zone in rilievo, o solo nelle cavità.

Il grafico rappresenta una sezione della superficie: la linea orizzontale è la superficie, e il cerchio rappresenta il raggio di decadimento della pittura sopra e sotto la superficie. `Compensazione altezza` è una percentuale sopra o sotto la superficie da cui parte il calcolo della maschera. Con `Attenuazione della profondità` attiva, `Area superiore` e `Area inferiore` ti permettono di ridimensionare il decadimento sopra e sotto il punto di partenza.

#### Esempio: dipingere nelle cavità {#example-paint-in-cavities}
Per dipingere solo nelle cavità, imposta la compensazione dell'altezza a -100% e regola il cursore dell'area superiore in modo che si stacchi dalla linea orizzontale. Così il primo tocco imposta la profondità "zero", e solo le zone più profonde vengono interessate.

![](/videos/stroke_depth_cavity.mp4)

#### Esempio: dipingere sui rilievi {#example-paint-on-bumps}
Per dipingere solo nelle zone alte, imposta la compensazione dell'altezza a +90%, così la parte bassa del cerchio interseca di poco la linea orizzontale. Quando tocchi la cima di una zona "alta", ne imposti la profondità: tutto ciò che è a quella profondità, un po' più in basso o più in alto viene dipinto. Le cavità profonde vengono saltate.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Pressione {#pressure}
![](/images/pressure_menu.webp) 

Controlla come la pressione dello stilo o della penna agisce sui pennelli.

### Usa le impostazioni globali {#use-global-settings}

Di base `Usa le impostazioni globali` è attivo, quindi tutti i pennelli condividono gli stessi valori di pressione. Toglilo per dare allo strumento corrente le sue impostazioni di pressione.

### ![](/icons/radius.webp) Raggio {#pressure-radius}

Questa curva controlla come la pressione agisce sul raggio del pennello. Di base la relazione è lineare, quindi se il tuo stilo ha una risposta regolare, anche la variazione del raggio sarà regolare. Detto questo, molti stili hanno una risposta non lineare, che puoi compensare con questa curva. Per esempio, se il raggio non sembra raggiungere il suo massimo alle pressioni alte, usa un preset come 'out-pow3', con una curvatura rivolta verso l'alto, per aumentare il raggio prima.

Questa finestra è simile alla curva di decadimento: puoi usare un preset toccando la finestra della curva, oppure disegnare le tue curve con le modalità `Catmull-Rom`, `B-spline` e `Smusso`.

Se vuoi un raggio costante, disattiva questa sezione.

### ![](/icons/intensity.webp) Intensità {#pressure-intensity}

Simile alla curva del raggio, ma controlla l'intensità. Se vuoi un'intensità costante, disattiva questa sezione.

### Limita la pressione al 100% {#limit-pressure}

Fa in modo che la pressione dello stilo non superi mai il 100%. È un'impostazione globale.

### Livellamento della pressione {#pressure-smoothing}

Fa la media degli eventi di pressione dello stilo per ottenere risultati più morbidi.

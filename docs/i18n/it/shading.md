# ![](/icons/sun.webp) Shading {#shading}

Questo menu controlla le modalità di shading usate da Nomad, le proprietà dell'illuminazione, l'ambiente e il matcap, e la nebbia.

![](/images/shading_overview.webp)



Puoi scegliere tra diverse modalità di rendering:

| Modalità                    | Significato                | Descrizione                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Illuminato (PBR)](#pbr)    | Physically Based Rendering | Luci, ombre, ambiente, e metallicità/rugosità dipinte           |
| [MatCap](#matcap)           | Material Capture           | Modalità veloce per scolpire, che usa meno gpu/cpu del PBR      |
| [Non illuminato](#unlit)    | Colore della superficie    | Solo il colore della superficie, senza shading né illuminazione |
| [ID oggetto](#object-id)    | ID oggetto                 | Un colore casuale per oggetto, utile nelle app di pittura.      |
| [ID istanza](#instance-id)  | ID istanza                 | Un colore casuale per istanza, utile per riconoscere le mesh condivise |

Per saperne di più su metallicità e rugosità, vedi la sezione [Pittura](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Gruppo di facce {#face-group}
Mostra in sovrimpressione i colori dei gruppi di facce. I gruppi di facce sono selezioni colorate di poligoni che puoi creare con lo strumento [Gruppo di facce](tools#facegroup), e che la maggior parte delle primitive crea automaticamente.

Alcuni strumenti filtrano automaticamente per gruppi di facce quando questi sono visibili.

### ![](/icons/palette.webp) Mostra pittura {#show-paint}
Nomad può memorizzare colore, rugosità e metallicità nei vertici della tua scultura. Con questa casella puoi mostrare o nascondere queste proprietà in modo globale.

Nota che se hai sia proprietà dei vertici sia texture, e sono attive entrambe, i valori vengono moltiplicati tra loro.

### ![](/icons/shield.webp) Mostra maschera {#show-mask}
Mostra o nasconde la sovrimpressione in scala di grigi della maschera creata con gli [strumenti maschera](tools#mask). Quando è disattivata, anche la maschera viene disattivata: comodo per fare modifiche rapide senza la maschera, per poi riattivarla senza perderla.

### ![](/icons/tool_hide.webp) Usa Nascondi {#use-hide}

Attiva o disattiva le facce nascoste. Nota che funziona solo se NON sei nello strumento nascondi!

### ![](/icons/image.webp) Usa texture {#use-textures}

Nomad permette di assegnare delle texture agli oggetti dal menu [Materiale](material). Se sono assegnate delle texture, puoi attivarle o disattivarle in modo globale con questa casella.

Non puoi creare o modificare texture in Nomad, ma le texture dei file importati funzionano. Le texture di opacità funzionano in Illuminato, MatCap e Non illuminato, le normal map in Illuminato e MatCap, il colore in Illuminato e Non illuminato, e l'emissione, la rugosità e la metallicità solo in Illuminato. Il pulsante è disattivato quando la scena non ha texture.

### Panoramica di PBR e luci {#pbr}
Questo manuale non entra nei dettagli del Physically Based Rendering.

Una cosa importante da tenere a mente è che illuminazione e materiale sono completamente separati.
Puoi quindi dipingere il colore, la rugosità e la metallicità del tuo oggetto, mentre l'illuminazione è gestita in modo indipendente.
Così puoi dipingere l'oggetto e poi ritoccare l'illuminazione in un secondo momento, senza rovinare l'aspetto generale del modello.

Le luci, l'ambiente e la nebbia sono disponibili solo in [modalità PBR](#pbr).
Per motivi di prestazioni, sei limitato a 4 luci su mobile e 6 su desktop.

::: tip
Puoi caricare un file glTF che contiene più luci, e Nomad le manterrà tutte.
Le prestazioni però potrebbero risentirne.
:::

::: tip
Puoi simulare tante luci rendendo degli oggetti non illuminati/emissivi, poi attivando l'illuminazione globale nel menu [Post processing](postprocess).
:::

### Panoramica dei tipi di luce {#light-types-overview}

Ecco i tipi di luce attualmente supportati:

| Modalità                    | Descrizione                                             | Può proiettare ombre |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Direzionale](#directional) | Luce solare infinitamente lontana                       | Sì               |
| [Ambiente](#env-light)      | Una luce lontana allineata all'HDR dell'ambiente        | Sì               |
| [Spot](#spot)               | Luci a forma di cono                                    | Sì               |
| [Puntiforme](#point)        | Punto di luce omnidirezionale                           | Sì               |

#### ![](/icons/sun.webp) Direzionale {#directional}
Emette luce da una distanza infinita, con un'intensità uniforme.
La sua posizione 3d nella scena non conta, conta solo il suo orientamento.

Puoi collegare questa luce alla fotocamera, così l'illuminazione resta costante.
Per esempio puoi usarla per creare una luce di contorno (una luce forte che arriva da dietro il modello, puntata verso la fotocamera) che illumina sempre il retro del modello.

#### ![](/icons/panorama.webp) Luce ambiente {#env-light}
Usare un [HDR di ambiente](#environment) funziona bene per un'illuminazione generale morbida, ma se nell'HDR c'è una luce forte e netta, l'ombra che crea sarà molto morbida, spesso del tutto invisibile. Usare una luce direzionale insieme all'HDR di ambiente può aiutare, ma può essere difficile allinearle.

Questa luce fa il lavoro al posto tuo. Viene ruotata automaticamente per allinearsi con la parte più luminosa dell'HDR, poi puoi controllarne separatamente l'intensità e l'angolo (la morbidezza delle ombre).

#### ![](/icons/spotlight.webp) Spot {#spot}
La luce spot emette luce in una sola direzione, limitata da una forma a cono.

#### ![](/icons/light.webp) Puntiforme {#point}
La luce puntiforme emette luce in tutte le direzioni, e anche lei può proiettare ombre.

#### Ombre {#shadows}
Ogni luce può proiettare ombre, e puoi scegliere come vengono calcolate nelle sue [impostazioni](#light-extra-controls). Se vedi degli artefatti nelle ombre, i cursori `Tolleranza` lì possono aiutarti.

La qualità delle ombre dipende dalle dimensioni degli oggetti rispetto all'intera scena.
Se nella scena hai un oggetto grande che non ha bisogno di proiettare ombre (per esempio un grande piano), ricordati di disattivare la proiezione delle ombre nelle sue [impostazioni del materiale](material.md#casts-shadows).

## ![](/icons/sun.webp) Luci {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Casella Luci {#lights-checkbox}

Attiva o disattiva tutte le luci dirette della scena.



### Aggiungi luce {#add-light}

Aggiunge una luce alla scena, fino a 4 luci su mobile e 6 su desktop. Quando aggiungi una luce, compare l'elenco delle luci con i relativi pulsanti, e in cima alla vista viene aggiunta una barra degli strumenti della luce.

![](/images/shading_lights_icons.webp)

* Il testo mostra il nome della luce e la sua luminosità. Toccalo per selezionare la luce.
* L'icona dell'occhio mostra o nasconde la luce.
* L'icona della matita ti permette di rinominare la luce.
* L'icona del cestino elimina la luce.
* L'icona di copia duplica la luce.
* L'icona con i 3 puntini apre l'editor completo della luce. Quasi tutte queste funzioni sono disponibili anche dalla barra degli strumenti che compare nella vista.

Puoi anche trascinare una luce nell'elenco per riordinarla.

### ![](/icons/spotlight.webp)  Icone {#icons}

Mostra o nasconde le icone delle luci nella vista.

### Barra degli strumenti della luce {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Questa barra compare in cima alla vista quando una luce è selezionata.

* `Visibile` mostra o nasconde la luce.
* Direzionale/Ambiente/Spot/Puntiforme cambia il tipo di luce. Tocca per passare da uno all'altro, oppure tieni premuto per vedere un menu.
* Intensità controlla la forza della luce; il valore può superare 1.0 per luci molto intense, utile insieme all'illuminazione globale del Post processing.
* Toccando il campione di colore si apre un selettore di colore. Nomad offre diversi modi per scegliere il colore. Il controllo in Kelvin permette di scegliere in modo naturale un'illuminazione calda o fredda.
* Ombra attiva o disattiva le ombre.
* Angolo (_direzionale e ambiente_) o Dimensioni (_spot e puntiforme_) imposta l'ampiezza della luce. Le luci più ampie proiettano ombre morbide, danno un'illuminazione morbida e un riflesso più morbido sugli oggetti.
* Collegamento (_solo direzionale_), Angolo del cono e Morbidezza (_solo spot_) sono descritti nell'[editor della luce](#light-extra-controls) qui sotto.
* ... apre `Clona`, `Ricentra` ed `Elimina`, insieme alle impostazioni delle ombre.

### Controlli aggiuntivi della luce {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

L'icona con i 3 puntini di una luce nell'elenco apre il suo editor completo. Nota che alcune opzioni sono specifiche di certi tipi di luce.

* `Direzionale/Ambiente/Spot/Puntiforme` ti permettono di cambiare il tipo di luce.
* Toccando il `campione di colore` si apre un selettore di colore.
* `Intensità` controlla la forza della luce.
* `Collegamento` (_solo direzionale_) collega la luce al mondo (`Fisso`) oppure alla fotocamera (`Fotocamera`). Per esempio, se usi una luce direzionale dietro il personaggio come luce di contorno, scegliendo il collegamento alla fotocamera la luce resterà sempre dietro il personaggio quando ruoti la fotocamera.
* `Morbidezza` (_solo spot_) controlla la nitidezza del bordo del cono dello spot. 0 è un bordo molto netto, 1 è molto morbido, con una sfumatura verso il centro del cono di luce. Nella vista, puoi usare il piccolo punto blu sul cono dello spot per regolare la morbidezza in modo interattivo.
* `Angolo del cono` (_solo spot_) controlla l'apertura dello spot. Un angolo piccolo dà un fascio di luce molto sottile, 170 dà una luce molto diffusa. Nella vista, puoi usare il punto arancione per regolare l'angolo del cono in modo interattivo.
* `Angolo` (_solo direzionale e ambiente_) è la dimensione apparente della luce: pensa a quanto appare grande il sole nel cielo. Angoli più grandi proiettano ombre più morbide e riflessi più ampi.
* `Dimensioni` (_solo spot e puntiforme_) è l'ampiezza della luce. Le luci più grandi proiettano ombre più morbide.
* `Ombra` attiva o disattiva le ombre per la luce corrente.
* Il tipo di ombra sceglie come vengono calcolate le ombre. Una `Shadow map` renderizza la scena dal punto di vista della luce, quindi proietta ombre anche dalla geometria che la fotocamera non vede. `Spazio dello schermo` usa solo ciò che è già visibile sullo schermo: è più leggero, ma sperimentale. In genere la shadow map è più affidabile.
* `Tolleranza` (_solo spazio dello schermo_): se vedi degli artefatti nelle ombre (le ombre non sembrano toccare le superfici, oppure ci sono rumore e motivi strani al loro interno), regolare la tolleranza può risolvere il problema.
* `Di contatto` aggiunge ombre più precise sulle brevi distanze, dove gli oggetti si toccano. Con `Auto` solo la luce dominante della scena ha le ombre di contatto; `No` e `Sì` le forzano spente o accese per questa luce. Il suo cursore `Tolleranza` funziona come quello sopra.

Il pulsante `...` della barra degli strumenti nella vista contiene le stesse impostazioni delle ombre, più:

* `Clona` duplica la luce.
* `Ricentra` sposta la luce davanti alla fotocamera, mantenendone l'orientamento.
* `Elimina` elimina la luce.


## ![](/icons/panorama.webp) Ambiente {#environment}

![](/images/shading_environment.webp)

Nel mondo reale la luce arriva da tutte le direzioni: il blu del cielo, il verde dell'erba, il rosso di un edificio. Tutta questa luce dell'"ambiente" si può simulare con una mappa di ambiente.

Usa la casella accanto al titolo per attivare o disattivare l'illuminazione dell'ambiente.

Nomad include diverse mappe di ambiente di esempio, per interni ed esterni, con tinte e livelli di luminosità diversi. Prova mappe diverse per vedere quale fa risaltare di più i dettagli delle tue sculture.

Tocca l'immagine per vedere le mappe di ambiente disponibili. Da quella finestra scegli `Importa...` per caricarne una tua. È meglio usare immagini ad alta gamma dinamica (HDR), in formato latlong o equirettangolare, come file .hdr o .exr. Il browser può anche scaricare ambienti direttamente da [Poly Haven](https://polyhaven.com/hdris), che ha una bella raccolta di mappe di ambiente gratuite.

### Esposizione {#env-exposure}
Regola la luminosità della mappa di ambiente. Spesso le mappe risultano troppo luminose se usate insieme alle luci normali: abbassare l'esposizione aiuta a bilanciare, soprattutto con l'illuminazione globale delle impostazioni di [Post processing](postprocess).

### Rotazione {#env-rotation}

Dato che le mappe di ambiente catturano la luce da tutte le direzioni, puoi ruotarle per far sì che i riflessi e l'illuminazione generale si sposino bene con la tua scultura. Puoi anche ruotare l'ambiente trascinando 3 dita in orizzontale sulla vista.

### Collegato alla telecamera {#env-attached}
Collega l'ambiente alla fotocamera.

L'illuminazione resta così costante, il che può essere utile mentre scolpisci.

### Sfocatura (sfondo) {#env-background-blur}
Questo cursore compare solo quando lo [sfondo](background.md) è impostato sull'ambiente. Sfoca l'immagine dell'ambiente dietro il modello, senza cambiare l'illuminazione.


## ![](/icons/fog.webp) Nebbia {#fog}

La nebbia aggiunge profondità atmosferica alla scena e rende visibili i fasci di luce. Attivala con la casella accanto al titolo. Come le luci e l'ambiente, è disponibile solo in modalità [Illuminato (PBR)](#pbr).

::: tip Fasci di luce più intensi
Abbassa l'`Ambiente` della nebbia e usa una luce spot o puntiforme molto luminosa. Aumenta la `Densità` finché la nebbia non è ben visibile. Per avere fasci visibili in una nebbia più leggera, imposta la `Direzione di diffusione` su un valore positivo alto e punta la fotocamera verso la luce.
:::

### Colore {#fog-color}
Il colore della nebbia e della luce che diffonde.

### Densità {#fog-density}
Quanto in fretta la nebbia si infittisce con la distanza.

### Opacità massima {#fog-opacity}
Limita quanto la nebbia può coprire la scena, anche a densità elevata.

### Direzione di diffusione {#fog-scattering}
La direzione in cui la nebbia diffonde la luce (detta anche anisotropia). I valori positivi schiariscono la nebbia quando guardi verso una luce, quelli negativi quando guardi dalla parte opposta, e lo zero diffonde la luce in modo uniforme in tutte le direzioni.

### ![](/icons/panorama.webp) Ambiente {#fog-environment}
Quanto l'[ambiente](#environment) illumina la nebbia. È disattivato quando l'ambiente è spento.

### Rumore {#fog-noise}
Mescola del rumore alla nebbia per spezzarla in chiazze, senza cambiarne la densità complessiva. Quando il rumore è sopra 0, un cursore `Dimensione` imposta la dimensione del motivo.

### Forma {#fog-shape}
Dove la nebbia riempie la scena:

* `Uniforme` - riempie tutta la scena.
* `Verticale` - mantiene la nebbia in una fascia verticale con i bordi sfumati. I cursori `Basso` e `Alto` impostano l'altezza dei bordi inferiore e superiore, e il loro pulsante a forma di occhio mostra la fascia nella vista mentre li regoli.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Come suggerisce il nome (MATerial CAPture), un matcap gestisce sia l'illuminazione sia il materiale in un'unica immagine.
Dato che il materiale è già contenuto nel matcap, i canali di pittura di rugosità e metallicità vengono ignorati.
Il colore dipinto viene moltiplicato con il matcap: se hai un matcap nero o grigio, dipingere di bianco non lo renderà più chiaro.

Gli artisti tendono a preferire questa modalità per scolpire, perché permette di concentrarsi sulla forma e sulla geometria.

Toccando la sfera si apre un browser di immagini. Puoi anche aggiungere un tuo matcap: in genere va bene qualsiasi foto, render o persino dipinto di una sfera ritagliata stretta in un quadrato. Online si trovano molte librerie di matcap; una risorsa utile è la [libreria di matcap di nidorx](https://github.com/nidorx/matcaps).

### Usa MatCap globale {#matcap-global}

Di solito gli artisti usano un solo matcap per l'intera scultura, ma se disattivi questa opzione, l'oggetto selezionato può avere un matcap tutto suo. Puoi sfruttarlo in modo creativo per ottenere risultati sorprendenti.

::: tip
Disattiva questa opzione e usa l'immagine di un bulbo oculare per gli occhi dei tuoi personaggi!
:::

### Rotazione {#matcap-rotation}
Un matcap è una forma particolare di mappa di ambiente, quindi, proprio come una mappa di ambiente, si può ruotare. Puoi farlo anche in qualsiasi momento nella vista, trascinando 3 dita a sinistra e a destra.

Il pulsante del lucchetto accanto al cursore blocca la rotazione, così un trascinamento a 3 dita non ruoterà il matcap per sbaglio.



## ![](/icons/circle_fill.webp) Non illuminato {#unlit}

Questa modalità mostra solo il colore della superficie. Può servire per controllare che il colore della superficie dei tuoi oggetti sia quello che ti aspetti, senza distrazioni dovute a luci, ombre, riflessi o trasparenze.

Puoi usarla anche per render non fotorealistici, con un aspetto piatto da cartone animato.

## ![](/icons/cube.webp) ID oggetto {#object-id}

Tutte le informazioni di illuminazione e di superficie vengono ignorate, e ogni oggetto viene colorato con un colore piatto unico. Se lo renderizzi insieme a un render PBR, puoi usarlo in un programma di pittura per selezionare per colore, e quindi fare correzioni di colore su oggetti specifici.

Nota che questi colori compaiono anche nella [vista ad albero del menu Scena](scene#tree-view).

### Randomizza ID {#object-random}

Genera un nuovo insieme di colori casuali.

## ![](/icons/link.webp) ID istanza {#instance-id}

Come ID oggetto, ma le istanze hanno lo stesso colore.

### Randomizza ID {#instance-random}

Genera un nuovo insieme di colori casuali.

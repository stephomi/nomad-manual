# ![](/icons/sun.webp) Ombreggiatura {#shading}

Questo menu controlla le modalità di ombreggiatura usate da Nomad, le proprietà delle luci e le proprietà della luce d’ambiente/matcap.

![](/images/shading_overview.webp)



Puoi scegliere tra diverse modalità di rendering:

| Modalità                    | Significato                | Descrizione                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Pittura con metalness/roughness                                |
| [Matcap](#matcap)           | Material Capture           | Usato durante lo sculpt con minore uso di gpu/cpu rispetto al PBR |
| [Unlit](#unlit)             | Surface Color              | Solo colore di superficie senza ombreggiatura o illuminazione  |
| [Object Id](#object-id)      | Object ID                  | Un colore casuale per oggetto, utile per applicazioni di painting |
| [Instance Id](#instance-id)  | Instance ID                | Un colore casuale per istanza, utile per identificare mesh condivise |

Se vuoi saperne di più su metalness e roughness, vedi la sezione [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Gruppo di facce {#face-group}
Sovrapponi i colori dei facegroup. I facegroup sono selezioni colorate di poligoni che possono essere creati con lo strumento [Face group](tools#facegroup) e vengono generati automaticamente con la maggior parte delle primitive.

Alcuni strumenti filtreranno automaticamente per facegroup quando i facegroup sono visibili.

### Mostra vernice {#show-paint}
Nomad può memorizzare colore, roughness e metalness nei vertici del tuo sculpt. Puoi attivare o disattivare globalmente la visualizzazione di queste proprietà con questa casella di controllo.

Nota che se hai sia proprietà per vertice che texture, e entrambe sono abilitate, i valori verranno moltiplicati tra loro.

### Mostra maschera {#show-mask}
Attiva la sovrapposizione in scala di grigi della maschera degli [strumenti di maschera](tools#mask). Quando è disabilitata, la maschera è anche disabilitata, utile per fare modifiche rapide senza la maschera, poi puoi riattivarla senza perdere la maschera.

### Usa Nascondi {#use-hide}

Attiva le facce nascoste. Nota che funziona solo se NON sei nello strumento hide!

### Usa texture {#use-textures}

Nomad permette di assegnare texture agli oggetti dal menu [material](material). Se sono state assegnate texture, possono essere attivate o disattivate globalmente con questa casella di controllo.







### Panoramica PBR e luci {#pbr}
Questo manuale non entrerà nei dettagli del Physically Based Rendering.

Una cosa importante da tenere a mente è che illuminazione e materiale sono completamente separati.
Significa che puoi dipingere colore, roughness e metalness del tuo oggetto mentre l’illuminazione è gestita in modo indipendente.
Questo ti permette di dipingere il tuo oggetto e poi modificare l’illuminazione in seguito, senza rovinare l’aspetto generale del modello.

Le luci sono disponibili solo con la [modalità PBR](#pbr).
Per motivi di prestazioni, sei limitato a sole 4 luci.

::: tip
Puoi caricare un file glTF con più di 4 luci e Nomad le manterrà tutte.
Tuttavia potrebbe non avere buone prestazioni.
:::

::: tip
Puoi simulare molte luci rendendo gli oggetti unlit/emissive, quindi abilitando la global illumination nel menu [post process](postprocess).
:::

### Panoramica dei tipi di luce {#light-types-overview}

Ecco i tipi di luce attualmente supportati:

| Modalità                    | Descrizione                                             | Può proiettare ombre                                   |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Luce solare infinitamente lontana                      | sì                                                     |
| [Environment](#environment) | Una luce distante che corrisponde all’ambiente HDR     | sì                                                     |
| [Spot](#spot)               | Luci a cono				                            | Sì                                                     |
| [Point](#point)             | Punto luce omnidirezionale                             | Sì, ma solo tramite ombre in screen-space meno robuste |

#### Direzionale {#directional}
Emette luce da una distanza infinita, con intensità uniforme.
La sua posizione 3D nella scena non ha importanza, conta solo l’orientamento.

Puoi collegare questa luce alla camera, in modo da avere un’illuminazione coerente.  
Per esempio puoi usarla per creare una rim light (una luce intensa che arriva da dietro il modello, puntata verso la camera) che illumina sempre il retro del tuo modello.

#### Luce ambiente {#env-light}
Usare una [environment hdr](#environment) funziona bene per un’illuminazione generale morbida, ma se nell’HDR è visibile una luce forte e netta, l’ombra creata sarà molto morbida, spesso quasi invisibile. Usare una luce direzionale in combinazione con l’HDR d’ambiente può aiutare, ma può essere difficile allinearle.

Questa luce fa il lavoro per te. La luce verrà ruotata automaticamente per allinearsi con la parte più luminosa dell’HDR, poi potrai controllarne separatamente intensità e angolo (morbidezza dell’ombra). 

#### Spot {#spot}
La luce spot emette luce in una singola direzione, limitata da una forma a cono.

#### Punto {#point}
La luce point emette luce in tutte le direzioni.  
Al momento, la luce point non supporta le ombre.

#### Ombre {#shadows}
L’opzione `normal bias` può essere usata per ridurre i comuni artefatti delle ombre (acne/peter-panning).

La qualità delle ombre dipende dalla dimensione degli oggetti rispetto all’intera scena.  
Se hai un grande oggetto nella scena che non deve proiettare ombre (per esempio un grande piano), assicurati di disabilitare la proiezione di ombre nelle sue [impostazioni del materiale](material.md#cast-shadows).

## Luci {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Checkbox Luci {#lights-checkbox}

Attiva o disattiva tutte le luci dirette nella scena.



### Aggiungi luce {#add-light}

Aggiunge una luce alla scena, fino a un massimo di 4. Quando viene aggiunta una luce, viene mostrato l’elenco delle luci con i pulsanti e viene aggiunta una toolbar delle luci nella parte superiore della viewport.

![](/images/shading_lights_icons.webp)

* Il testo mostra il nome della luce e la luminosità.
* L’icona a forma di occhio attiva/disattiva la visibilità.
* L’icona a matita permette di rinominare la luce.
* L’icona del cestino elimina una luce.
* L’icona di copia duplica una luce. 
* L’icona con 3 puntini apre un editor completo della luce. Gran parte di questa funzionalità è disponibile anche dalla toolbar che appare nella viewport. 

### ![](/icons/spotlight.webp)  Icone {#icons}

Attiva o disattiva la visualizzazione delle icone delle luci nella viewport.

### Barra strumenti luce {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Questa toolbar appare nella parte superiore della viewport quando una luce è selezionata.

* Show attiva/disattiva la visibilità della luce.
* Directional/Environment/Spot/Point cambia il tipo di luce. Tocca per scorrere, o tieni premuto per vedere un menu.
* Intensity controlla la forza della luce; il valore può superare 1.0 per luci molto intense, utile se usato con la Global Illumination nel Post Process.
* Cliccando sul riquadro colore si apre un selettore di colore. Nomad offre diversi modi per scegliere il colore. Il controllo Kelvin offre un modo naturale per selezionare luci calde/fredde.
* Shadow attiva/disattiva le ombre.
* Size imposta la larghezza di una luce. Luci più larghe proiettano ombre morbide, illuminazione morbida e un highlight più morbido sugli oggetti.
* ... apre i controlli extra.

### Controlli extra luce {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Nota che alcune opzioni sono specifiche di certi tipi di luce.

* `Clone` duplica la luce.
* `Recenter` riporta la luce all’origine.
* `Delete` elimina la luce.
* `Directional/Environment/Spot/Point` permettono di cambiare il tipo di luce.
* Il `colour swatch` quando cliccato apre un selettore di colore. 
* `Intensity` controlla la forza della luce.
* `Attachment` (_solo directional_) imposta se la luce è collegata al mondo o alla camera. Ad esempio, se usi una luce direzionale dietro il personaggio come rim light, quando è selezionato attachment come camera, ruotando la camera la luce resterà sempre dietro il personaggio.
* `Angle` (_solo directional ed environment_) è la dimensione apparente della luce, pensala come quanto è grande il sole nel cielo. Angoli maggiori proiettano ombre più morbide e highlight più ampi.
* `Softness` (_solo spotlight_) controlla la nitidezza del bordo del cono della spotlight. 0 è un bordo molto netto. 1 è molto morbido, con un gradiente verso il centro del cono di luce. Nella viewport, il piccolo punto blu sul cono della spotlight può essere usato per impostare interattivamente la softness.
* `Cone angle` (_solo spotlight_) controlla l’angolo di apertura della spotlight. Un angolo piccolo è un fascio di luce molto sottile, 170 è una diffusione di luce molto ampia. Nella viewport, il punto arancione può essere usato per impostare interattivamente il cone angle.
* `Shadow` attiva/disattiva le ombre per la luce corrente.
* `Shadow map` e `screenspace` sono diversi modi di calcolare le ombre; in generale shadow map è più affidabile.
* `Contact` regola come vengono calcolate le ombre. Le ombre sono un problema complesso nella computer grafica e possono causare artefatti nel rendering. Ombre più accurate possono essere selezionate per la luce più importante in una scena; questo controllo determina se la luce più importante viene selezionata automaticamente da Nomad o dall’utente.
* `Tolerance` se sono visibili artefatti nelle ombre (per esempio le ombre non sembrano toccare le superfici, o c’è rumore e pattern all’interno delle ombre), regolare la tolerance può aiutare a risolvere questi problemi.


## Ambiente {#environment}

![](/images/shading_environment.webp)

La luce nel mondo reale proviene da tutte le direzioni; il blu del cielo, il verde dell’erba, il rosso di un edificio: tutta questa luce proveniente dall’“ambiente” può essere simulata con una environment map. 

Nomad include diversi esempi di environment map per ambienti interni ed esterni, con differenti tonalità e livelli di luminosità. Prova mappe diverse per vedere quale fa risaltare meglio i dettagli dei tuoi sculpt.

Tocca l’immagine per vedere le environment map disponibili. Da quella finestra scegli “Import...” per caricare le tue. È meglio usare immagini High Dynamic Range (HDR), in formato latlong o equirectangular, come file .hdr o .exr. [www.polyhaven.com](https://polyhaven.com/hdris) ha una buona raccolta di environment map gratuite da usare; in genere le mappe hdr 1k sono una buona dimensione e di buona qualità.

### Esposizione {#env-exposure}
Regola la luminosità della environment map. Spesso le mappe possono essere troppo luminose quando usate con luci normali; abbassare l’exposure può aiutare a bilanciare, specialmente se usato con la Global Illumination nelle impostazioni di [Post Process](postprocess).

### Rotazione {#env-rotation}

Poiché le environment map catturano la luce da tutte le direzioni, puoi ruotarle per far sì che riflessi e illuminazione generale si combinino bene con il tuo sculpt.

### Attaccato alla camera {#env-attached}
Collega l’ambiente alla camera.

Forzerà un’illuminazione coerente, cosa che può essere utile durante lo sculpt.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Come suggerisce il nome (MATerial CAPture), un matcap si occupa sia dell’illuminazione che delle informazioni di materiale in una singola immagine.
Poiché il materiale è già presente nel matcap, i canali di pittura roughness e metalness verranno ignorati.
Il colore di pittura verrà moltiplicato con il matcap, il che significa che se hai un matcap nero/grigio, usare pittura bianca non lo renderà più luminoso.

Gli artisti tendono a preferire questa modalità per lo sculpt, poiché permette loro di concentrarsi sulla forma e sulla geometria.

Toccando sulla sfera si apre un browser di immagini. Puoi anche aggiungere i tuoi matcap: in generale qualsiasi foto, render o persino un dipinto di una sfera ritagliata strettamente in un quadrato può essere usato. Molte librerie di matcap sono disponibili online; una risorsa utile è la [libreria di matcap di nidorx](https://github.com/nidorx/matcaps).

### Usa Matcap globale {#matcap-global}

Di solito gli artisti usano un singolo matcap per l’intero sculpt, ma se questo toggle è disabilitato, ogni oggetto può avere il proprio matcap. Questo può essere usato artisticamente per ottenere risultati d’impatto.

::: tip
Disabilita questa opzione e usa un’immagine di un bulbo oculare per gli occhi dei tuoi personaggi!
:::

### Rotazione {#matcap-rotation}
Un matcap è una forma specializzata di environment map, quindi, come una environment map, può essere ruotato. Puoi farlo anche in qualsiasi momento nella viewport trascinando con 3 dita a sinistra e a destra.



## ![](/icons/circle_fill.webp) Non illuminato {#unlit}

Questa modalità mostrerà solo il colore di superficie. Può essere utile per controllare che il colore di superficie dei tuoi oggetti sia quello che ti aspetti, senza essere distratto da luci, ombre, riflessi, trasparenze. 

Questa modalità può anche essere usata per render non fotorealistici, ottenendo un aspetto piatto e cartoonesco.

## ![](/icons/cube.webp) ID oggetto {#object-id}

Tutte le informazioni di illuminazione e superficie vengono ignorate e ogni oggetto è ombreggiato con un colore piatto unico. Se questo viene renderizzato insieme a un render PBR, può essere usato in un programma di painting per selezionare per colore e quindi poter fare correzioni di colore su oggetti specifici.

Nota che questi colori appariranno anche nella [vista ad albero del menu Scene](scene#tree-view).

### Randomizza ID {#object-random}

Genera un nuovo set di colori casuali. 

## ![](/icons/link.webp) ID istanza {#instance-id}

Come Object ID, ma le istanze avranno lo stesso colore. 

### Randomizza ID {#instance-random}

Genera un nuovo set di colori casuali.
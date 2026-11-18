# ![](/icons/postprocess.webp) Post processing {#post-process}

Questo menu controlla molti aspetti di Nomad che influiscono sull'aspetto del render.

![](/images/postprocess_overview_drac.webp)

Il post processing può cambiare in modo notevole l'aspetto finale della scena.

![](/images/postprocess_overview.webp)
*La stessa scena prima e dopo il post processing, senza luci aggiuntive né modifiche ai materiali.*

A seconda del dispositivo, il post processing può pesare molto sulle prestazioni.
C'è una casella globale `Post processing` per disattivare tutto il post processing, così puoi tornare rapidamente a scolpire/modellare senza perdere i tuoi preset.
Per il rendering PBR, conviene attivare [Occlusione ambientale](#ambient-occlusion-ssao), [Riflessione](#reflection-ssr) e [Mappatura dei toni](#tone-mapping).

Però, il più delle volte, mentre scolpisci è meglio tenere il post processing disattivato, per concentrarti sulla forma invece che sul rendering.


## Qualità {#quality}

![](/images/postprocess_quality.webp)

Queste opzioni migliorano la qualità del render, a scapito delle prestazioni.

### Campionamento fotogrammi max {#max-frame-sampling}
Per il render di un singolo fotogramma Nomad calcola una certa quantità di post processing, che può risultare rumorosa. Questo controllo stabilisce quanti fotogrammi vengono renderizzati e poi fusi insieme per eliminare la maggior parte del rumore. Alcuni effetti non richiedono campioni aggiuntivi (per esempio la gradazione colore), mentre altri, come le ombre morbide e l'illuminazione globale, possono richiedere centinaia di campioni per essere privi di rumore. 

Nella vista lo noti ogni volta che lasci Nomad inattivo: la qualità dell'immagine si affina gradualmente fino al numero massimo di campioni, poi si ferma. Una volta fermo, Nomad non fa nulla, risparmiando batteria. Questo numero di calcoli viene usato anche nella sezione di render del [menu File](files) quando premi 'export png'.

La casella accanto al cursore attiva o disattiva il campionamento dei fotogrammi.

### Risoluzione rendering {#resolution-multiplier}
Questo cursore controlla la risoluzione del render. Un valore di x1.0 significa che il render viene fatto alla risoluzione in pixel del dispositivo. Un valore di x0.5 renderizza a metà risoluzione: veloce, ma di bassa qualità. Un valore maggiore di 1 renderizza a una dimensione più grande, poi riduce. Il risultato è di qualità più alta, con meno rumore, ma con tempi di render più lunghi.

Ha un impatto enorme sulle prestazioni, quindi cerca di tenerlo a x1.25 o meno. Questo valore non viene salvato nelle impostazioni, e l'effetto [Pixel Art](#pixel-art) lo sostituisce.

### ![](/icons/intensity.webp) Max campioni {#max-samples}

Migliora la qualità degli effetti di post processing, a scapito delle prestazioni.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Applica il dithering ai pixel per ridurre gli artefatti a bande (nei gradienti o nella vignettatura, per esempio). Di solito va lasciato attivo, ma puoi disattivarlo per operazioni particolari (per esempio esportare mappe di profondità o altri dati specifici).

### ![](/icons/denoise.webp) Denoiser (oidn) {#oidn}

Applica un filtro di riduzione del rumore all'immagine una volta accumulati tutti i fotogrammi. Ti permette di usare molti meno campioni. La riduzione del rumore pesa molto sul processore, quindi attivala solo se l'immagine è rumorosa. Non è disponibile su tutti i dispositivi.

## Raccolta di preset {#preset-browser}
![](/images/postprocess_presets.webp)
Toccando l'immagine sotto il titolo `Post processing` compare una raccolta di preset di post processing. Usa `Nuovo` per creare un preset dalle impostazioni attuali. I preset integrati si possono solo clonare: per definirne uno tuo, selezionane uno, tocca `Clona` e fai le tue modifiche. Quando un preset ha modifiche non ancora salvate, mostra `Vi sono modifiche non salvate!`; per salvare, tocca l'immagine del preset, tocca di nuovo dentro la raccolta di preset e scegli `Salva`.

## Barra delle scorciatoie {#shortcut-bar}
Quando il post processing è attivo, una barra in fondo al menu elenca tutti gli effetti (`SSR`, `SSGI`, `SSAO`, `DoF`, `Bagliore diffuso`...). Toccane uno per saltare alla sua sezione. Gli effetti disattivati sono in grigio, così la barra è anche un rapido riassunto di ciò che fa il preset attuale.

## ![](/icons/postprocess_ssr.webp) Riflessione (SSR) {#reflection-ssr}
Con questa opzione, gli oggetti possono riflettere altri oggetti della scena, purché siano visibili sullo schermo.
Se nella scena hai oggetti metallici e lucidi, probabilmente conviene usarla.
Questa opzione richiede la modalità di shading [Illuminato (PBR)](shading.md#pbr).


| SSR disattivato            | SSR attivato              |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Illuminazione globale (SSGI) {#global-illumination-ssgi}

L'illuminazione globale simula come la luce rimbalza tra le superfici: per esempio, una parete rossa proietta del rosso su un oggetto bianco vicino. Insieme all'occlusione ambientale e ai riflessi, può aumentare moltissimo il realismo di un render. Come i riflessi, richiede la modalità di shading [Illuminato (PBR)](shading.md#pbr).

`Intensità` - L'intensità dell'illuminazione globale. 



| SSGI disattivato           | SSGI attivato             |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Un faretto è dietro la sfera, puntato verso il soffitto. Con SSGI disattivato, è illuminato solo il soffitto. Con SSGI attivato, la luce rimbalza dal soffitto alle pareti fino alla sfera._

## ![](/icons/postprocess_ssao.webp) Occlusione ambientale (SSAO) {#ambient-occlusion-ssao}
L'occlusione ambientale scurisce le zone che la luce ha meno probabilità di raggiungere (angoli, ecc.).
L'effetto dipende solo dalla geometria del modello.

* `Intensità` - Intensità dell'effetto.
* `Dimensioni` - Quanto è esteso l'effetto.
* `Spessore` - Lo spessore in profondità attribuito agli oggetti che fanno occlusione, in percentuale di `Dimensioni`.
* `Tinta` - Un colore moltiplicato nell'occlusione, per effetti creativi.


| SSAO disattivato            | SSAO attivato              |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
L'occlusione ambientale si vede di più nelle zone illuminate soprattutto dalla luce dell'ambiente. Le zone sotto una forte luce diretta ricevono un effetto molto più debole.

:::

## ![](/icons/postprocess_dof.webp) Profondità di campo {#depth-of-field-dof}
Aggiunge una sfocatura alle zone fuori fuoco.

Tocca semplicemente il modello per cambiare il punto di messa a fuoco.

* `Modalità apertura` - Gestisce la sfocatura con un'unica apertura della fotocamera, invece dei due cursori di sfocatura qui sotto.
* `Apertura` (_solo in modalità apertura_) - Il numero f dell'obiettivo, come su una vera fotocamera. Un valore più basso apre l'obiettivo e sfoca di più.
* `Sfocatura lontana` - La quantità di sfocatura applicata oltre il punto di messa a fuoco.
* `Sfocatura vicina` - La quantità di sfocatura applicata tra il punto di messa a fuoco e la fotocamera.


| DOF disattivato           | DOF a fuoco sull'anello lontano | DOF a fuoco sull'anello vicino |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Bagliore diffuso {#bloom}
Il bagliore diffuso fa brillare le zone luminose della scena.

* `Intensità` - intensità dell'effetto.
* `Raggio` - L'estensione dell'effetto.
* `Soglia` - Quanto devono essere luminosi i pixel della scena prima di iniziare a brillare. A 0 brilla tutto; con un valore alto brillano solo i pixel più luminosi.
* `Tinta` - un colore da aggiungere al bagliore per effetti creativi.

| Bagliore disattivato         | Bagliore con raggio 0       | Bagliore con raggio 1       |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mappatura dei toni {#tone-mapping}
La mappatura dei toni è un'operazione che rimappa i valori HDR nell'intervallo `[0, 1]`.
Se non la usi (o scegli `Nessuno`), ogni componente di colore superiore a 1 viene tagliata.
Tutte le variazioni di colore oltre questo intervallo vanno quindi perse.

* `Nessuno`/`Neutrale`/`Agx`/`ACES` - quale tonemapper usare. `Nessuno` non rimappa nulla (ma gli altri controlli funzionano comunque). Le altre opzioni sono come scegliere pellicole diverse: gestiscono in modi diversi i valori e i colori sovraesposti. È un argomento molto vasto: cerca tone mapping, Agx e ACES per saperne di più!
* `Esposizione` - la luminosità generale dell'immagine, come regolare l'apertura su una fotocamera. È un modo rapido per schiarire o scurire tutta l'immagine.
* `Saturazione` - l'intensità dei colori. 1 è neutro, 0 è monocromatico, i valori sopra 1 sono via via più saturi.
* `Contrasto` - Rende le zone scure più scure e quelle chiare più chiare. Usalo con attenzione: a valori alti può introdurre artefatti.

Nota che con la `Mappatura dei toni` disattivata alcuni dettagli spariscono, perché i pixel sono troppo luminosi.

| Mappatura dei toni disattivata | Mappatura dei toni attivata |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
La mappatura dei toni può accentuare l'effetto dell'illuminazione globale. Se abbassi l'intensità della mappa d'ambiente e alzi la sorgente di luce principale, puoi aumentare l'`Esposizione` della mappatura dei toni per vedere meglio gli effetti della luce che rimbalza.
:::

## ![](/icons/postprocess_tone_curve.webp) Gradazione colore {#color-grading}
Simile allo strumento Curve di Photoshop, ti permette di controllare l'equilibrio e la distribuzione dei colori nell'immagine. Il controllo `Principale` agisce sull'intero equilibrio dei colori, i controlli `Rosso`/`Verde`/`Blu` permettono regolazioni fini. 

| Gradazione colore disattivata | Gradazione colore attivata |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Curvatura {#curvature}
Rileva dove la curvatura cambia bruscamente, e applica un colore a quelle zone.

* `Fattore` - intensità generale dell'effetto
* `Rilievo` - quanto rileva i cambiamenti convessi netti, applicandovi il colore scelto (bianco di default)
* `Cavità` - quanto rileva i cambiamenti concavi, applicandovi il colore scelto (nero di default)
* `Spessore` - quanto sono larghi i bordi rilevati.

Accanto a `Rilievo` e `Cavità`, un campione di colore sceglie il colore, e un piccolo pulsante sceglie come quel colore si fonde con l'immagine.


| Curvatura disattivata            | Curvatura attivata             |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberrazione cromatica {#chromatic-aberration}
Simula il difetto delle lenti in cui la luce si scompone verso i bordi dello schermo.

* `Intensità` - quanto le componenti rossa/verde/blu dell'immagine si separano verso i bordi dello schermo

| Aberrazione disattivata       | Aberrazione attivata         |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vignettatura {#vignette}
Simula il difetto delle lenti che scurisce i bordi dello schermo.

* `Dimensioni` - La dimensione di un'ellisse invertita posta sopra l'immagine
* `Durezza` - Quanto l'ellisse si fonde in modo sfumato o netto sopra l'immagine.
* `Tinta` - Il colore della vignettatura, nero di default.


| Vignettatura disattivata        | Vignettatura attivata          |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Grana {#grain}
Aggiunge un effetto grana, che può rendere l'immagine un po' meno artificiale.

* `Intensità` - la quantità di grana/rumore aggiunta all'immagine.


| Grana disattivata            | Grana attivata             |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Nitidezza {#sharpness}
Un effetto di nitidezza simile a quello di Photoshop o delle app di fotoritocco.

* `Intensità` - la quantità di nitidezza applicata all'immagine.


| Nitidezza disattivata          | Nitidezza attivata           |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Simula la pixel art dei videogiochi retrò. Questo effetto sostituisce la [Risoluzione rendering](#resolution-multiplier).

* `Cursore` - dimensione dei pixel
* `Consenti campionamento fotogrammi` - se compaiono molti pixel neri, prova ad attivarlo. Senza di esso, l'effetto pixel art disattiva il [campionamento dei fotogrammi](#max-frame-sampling).

| Pixel disattivato           | Pixel attivato             |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Linea di scansione {#scanline}
Simula l'aspetto dei vecchi monitor a tubo catodico.

* `Fattore` - intensità delle linee
* `Spaziatura` - dimensione delle linee

| Linee di scansione disattivate | Linee di scansione attivate |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

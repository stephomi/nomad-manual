# ![](/icons/postprocess.webp) Postprocesso {#post-process}

Questo menu controlla molti aspetti di Nomad che influenzano l'aspetto del render.

![](/images/postprocess_overview_drac.webp)

L'uso del post processing può cambiare in modo sostanziale l'aspetto finale della scena.

![](/images/postprocess_overview.webp)
*La stessa scena prima e dopo il post processing, senza luci aggiuntive o modifiche ai materiali.*

Il post process può avere un forte impatto sulle prestazioni a seconda del dispositivo.
C'è una casella di controllo globale per disabilitare tutto il postprocess, così puoi tornare rapidamente a scolpire/modellare senza perdere i tuoi preset.
Per il rendering PBR, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) e [Tone Mapping](#tone-mapping) dovrebbero essere abilitati.

Tuttavia, la maggior parte delle volte è preferibile che il post process sia disabilitato mentre stai scolpendo, per concentrarti sulla forma stessa del modello.

## Qualidade {#quality}

![](/images/postprocess_quality.webp)
### Amostragem máxima por frame {#max-frame-sampling}
Nomad calcolerà una certa quantità di post processing per il render di un singolo frame, che può risultare rumoroso. Questo controllo determina quanti frame verranno renderizzati e poi fusi insieme per rimuovere la maggior parte degli artefatti di rumore. Alcuni effetti non richiedono campioni extra (ad es. color grading), mentre altri come la global illumination possono richiedere centinaia di campioni per essere privi di rumore. 

Nel viewport questo si nota quando Nomad viene lasciato inattivo: la qualità dell'immagine si affina gradualmente fino al numero massimo di campioni, quindi si ferma. Questo numero di calcoli viene usato anche nella sezione di render del [menu Files](files) quando si clicca su “export png”.

### Multiplicador de resolução {#resolution-multiplier}
Questo cursore controlla la risoluzione del post processing. Un valore di x1.0 significa che i render vengono eseguiti alla risoluzione in pixel del dispositivo. Un valore di x0.5 eseguirà il render a metà risoluzione, più veloce ma di qualità inferiore. Un valore superiore a 1 eseguirà il render a una dimensione maggiore, per poi ridimensionare verso il basso. Questo produce una qualità più alta, meno rumore, ma tempi di render più lunghi.

### Amostras máximas {#max-samples}

Aumenta la qualità del post process, ma in generale `Full resolution` avrà un impatto maggiore. 

### Denoiser (oidn) {#oidn}

Applica un denoiser all'immagine. Questo ti permette di usare un numero di campioni molto più basso. Funziona solo se `Full Resolution` è abilitato. Nota che il denoising avviene dopo che tutti i campioni sono stati calcolati e può essere intensivo per il processore.

## Navegador de predefinições {#preset-browser}
![](/images/postprocess_presets.webp)
Cliccando sull'immagine verrà mostrata una raccolta di preset di post processing. Per definire i tuoi preset, selezionane uno, clicca “clone”, apporta le modifiche. Per salvare, clicca sull'immagine del preset, clicca di nuovo all'interno del preset browser e scegli “save”.

## Reflexão (SSR) {#reflection-ssr}
Con questa opzione, gli oggetti possono riflettere altri oggetti nella scena, purché gli oggetti siano visibili sullo schermo.
Se hai oggetti metallici e lucidi nella scena, probabilmente dovresti usare questa opzione.
Questa opzione è efficace solo con la modalità PBR.

| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Iluminação Global (SSGI) {#global-illumination-ssgi}

La global illumination simula come la luce rimbalza tra le superfici, ad esempio un muro rosso proietterà rosso su un oggetto bianco vicino. Questo può aumentare enormemente il realismo di un render se usato insieme ad ambient occlusion e riflessioni. 

`Strength` - L'intensità della global illumination. 

| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Un faretto è dietro la sfera, puntato verso il soffitto. Con SSGI disattivato, è illuminato solo il soffitto. Con SSGI attivato, la luce rimbalza dal soffitto alle pareti fino alla sfera._

## Oclusão de Ambiente (SSAO) {#ambient-occlusion-ssao}
L'ambient occlusion scurisce le aree dove la luce ha meno possibilità di arrivare (angoli, ecc.).
L'effetto dipende solo dalla geometria del modello.

* `Strength` - Intensità dell'effetto.
* `Size` - Quanto è esteso l'effetto.
* `Curvature bias` - Quanto l'effetto è sensibile rispetto alle variazioni della superficie.
* `Color` - Una tinta moltiplicata nell'occlusione, usata per effetti creativi.

| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
L'AO sarà più visibile nelle aree illuminate principalmente dalla luce di ambiente. Le aree sotto una forte luce diretta riceveranno un effetto AO molto più debole.

:::

## Profundidade de Campo (DOF) {#depth-of-field-dof}
Aggiunge un effetto di sfocatura alle regioni fuori fuoco.

Tocca semplicemente il modello per cambiare il punto di messa a fuoco.

* `Far blur` - Quantità di sfocatura applicata oltre il punto di messa a fuoco.
* `Near blur` - Quantità di sfocatura applicata tra il punto di messa a fuoco e la camera.

| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |

## Bloom {#bloom}
Il bloom farà brillare le aree luminose della scena.

* `Intensity` - Intensità dell'effetto.
* `Radius` - L'ampiezza dell'effetto.
* `Threshold` - Quanto devono essere luminosi i pixel nella scena prima che inizino a generare bloom. Impostando questo valore basso tutto produrrà bloom, impostandolo alto solo i pixel più luminosi produrranno bloom.
* `Color` - una tinta che può essere aggiunta al bloom per effetti creativi.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |

## Mapeamento de tom {#tone-mapping}
Il Tone Mapping è un'operazione che rimappa i valori HDR nell'intervallo `[0, 1]`.
Se non lo usi (o selezioni `none`), qualsiasi componente di colore superiore a 1 verrà tagliata.
Qualsiasi variazione di colore al di sopra di questo intervallo andrà quindi persa.

* `None/Neutral/Agx/ACES` - quale tonemapper usare. `None` non esegue alcun remapping (ma gli altri controlli funzionano comunque). Le altre opzioni sono simili alla scelta di pellicole diverse: gestiranno i valori e i colori sovraesposti in modi differenti. È un argomento molto vasto, cerca informazioni su tone mapping, Agx, ACES per maggiori dettagli!
* `Exposure` - luminosità complessiva dell'immagine, simile alla regolazione del diaframma di una fotocamera. Può essere un modo rapido per schiarire o scurire globalmente un'immagine.
* `Saturation` - intensità del colore. 1 è neutro, 0 è monocromatico, valori superiori a 1 sono via via più saturi.
* `Contrast` - Rende i neri più neri e i bianchi più bianchi. Usalo con cautela, a valori alti può introdurre artefatti.

Nota che con il `Tone Mapping` disabilitato, alcuni dettagli scompaiono perché i pixel sono troppo luminosi.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Il tone mapping può amplificare l'effetto della global illumination. Se abbassi l'intensità della environment map e alzi la sorgente di luce primaria, puoi aumentare l'`exposure` del tone mapping per vedere meglio gli effetti della luce di rimbalzo.
:::

## Graduação de cor {#color-grading}
Simile allo strumento curve di Photoshop, ti permette di controllare il bilanciamento e la distribuzione del colore nell'immagine. Il controllo `main` influenza l'intero bilanciamento dei colori, mentre i controlli `red`/`green`/`blue` permettono una regolazione fine. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvatura {#curvature}
Rileva dove ci sono cambiamenti rapidi di curvatura e applica un colore a quelle regioni.

* `Factor` - intensità complessiva dell'effetto
* `Bump` - quanto rileverà i cambiamenti convessi netti, applicando lì il colore selezionato (bianco per impostazione predefinita)
* `Cavity` - quanto rileverà i cambiamenti concavi, applicando lì il colore selezionato (nero per impostazione predefinita)

| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |

## Aberração cromática {#chromatic-aberration}
Simula gli artefatti dell'obiettivo con la luce che viene scomposta attorno ai bordi dello schermo.

* `Strength` - quanto le componenti rosso/verde/blu dell'immagine vengono separate verso i bordi dello schermo

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |

## Vinheta {#vignette}
Simula gli artefatti dell'obiettivo scurendo i bordi dello schermo.

* `Size` - La dimensione di un'ellisse invertita posizionata sopra l'immagine
* `Hardness` - Quanto è sfocata o netta l'ellisse quando viene miscelata sopra l'immagine.

| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grão {#grain}
Aggiunge un effetto grana, può aiutare a rendere l'immagine un po' meno artificiale.

* `Strength` - la quantità di grana/rumore aggiunta all'immagine.

| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |

## Nitidez {#sharpness}
Un effetto di nitidezza simile a quello di Photoshop o delle app di fotoritocco.

* `Strength` - la quantità di nitidezza applicata all'immagine.

| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel art {#pixel-art}
Simula la pixel art dei giochi retrò.

* `Slider` - dimensione dei pixel
* `Allow frame sampling` - se ottieni molti pixel neri, prova ad attivarlo: sovrascriverà il sampling predefinito.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Linha de varredura {#scanline}
Simula l'aspetto dei vecchi monitor CRT.

* `Factor` - intensità delle linee
* `Spacing` - dimensione delle linee

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

## Dithering {#dithering}

Applica dithering ai pixel per ridurre gli artefatti di banding. Di solito dovrebbe essere abilitato, ma può essere disattivato per operazioni specifiche (ad es. esportazione di depth map o altre operazioni specifiche sui dati).
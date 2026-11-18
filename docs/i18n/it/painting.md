# ![](/icons/paint.webp) Pittura {#painting}

Controlla il colore, la rugosità e la metallicità dei tratti di pittura, permette di riempire interamente gli attributi di pittura, e stabilisce come gli strumenti di pittura interagiscono con livelli, maschere e zone nascoste.

![](/images/paint_overview.webp)  

## Panoramica {#overview}

Nomad usa la pittura PBR sui vertici. Cosa significa?

### PBR {#pbr}
Il PBR, o Physically Based Rendering (rendering basato sulla fisica), è una tecnica di computer grafica molto diffusa nel cinema, in televisione, nei videogiochi e sui dispositivi mobili. Basando le luci su proprietà fisiche e definendo le superfici tramite colore, rugosità e metallicità, si ottiene un'ampia varietà di aspetti fotorealistici.

### Pittura dei vertici {#vertex-painting}

Pittura dei vertici significa che le informazioni di pittura vengono salvate nei vertici del modello, invece che nelle texture. Dato che Nomad gestisce modelli con centinaia di migliaia, spesso milioni di vertici, i tuoi modelli possono avere una pittura della superficie molto dettagliata: se riesci a scolpire un dettaglio, puoi anche dipingerlo.

Significa anche che per dipingere in Nomad non serve la mappatura UV, spesso un processo lento e tecnico in altre app 3d. Molte altre app 3d non reggono l'alto numero di vertici che gestisce Nomad, ma Nomad ha anche buoni strumenti di trasferimento delle texture e di decimazione per aiutarti.

### Texture {#texturing}

Nomad supporta le texture, ma devono essere presenti in un modello importato, oppure ottenute trasferendo la pittura dei vertici su texture. 

Una texture è semplicemente un'immagine, ma nel contesto 3d indica di solito un'immagine assegnata a un oggetto.
Per avvolgere un'immagine attorno a un modello, il modello ha bisogno di coordinate di texture (UV).

Nomad può calcolarle [automaticamente](topology.md#uv-unwrap), ma non hai molto controllo sulla qualità complessiva.

::: tip
Un esempio di flusso di lavoro:
- Scolpisci in Nomad, poi esegui lo [sviluppo UV](topology.md#uv-unwrap)
- Se hai già iniziato a dipingere in Nomad, puoi [trasferire la pittura dei vertici sulle texture](topology.md#bake-texture)
- Esporta in Procreate
- Dipingi le texture in Procreate
- Riesporta in Nomad per il rendering
:::

Questa era la panoramica, ora esploriamo le sezioni del menu Pittura:


## Pittura del tratto {#stroke-painting}
![](/images/paint_intensity.webp)  

Abilita la pittura per questo strumento, utile se devi scolpire e dipingere contemporaneamente. Quando uno strumento può dipingere ma questa casella è disattivata, un'icona di avviso accanto al titolo te lo ricorda.

Per gli strumenti la cui funzione principale è dipingere (per esempio Dipingi, Sfumino, Maschera), questa casella non c'è.

### ![](/icons/opacity.webp) Intensità pittura {#paint-intensity}

Un cursore che ti permette di usare per la pittura un'intensità diversa da quella principale dello strumento.

Il pulsante con i cursori accanto aggiunge alla barra laterale un cursore rapido per l'intensità della pittura, per gli strumenti che scolpiscono e dipingono allo stesso tempo.

I pulsanti `Alfa`, `Decadimento` e `Randomizza intensità` stabiliscono se queste funzioni influiscono sulla pittura. Per esempio, puoi avere la randomizzazione attiva per lo strumento Argilla, senza che il colore venga randomizzato.

* `Alfa` - quando è disattivato, la pittura ignora l'alfa e copre tutta l'area del pennello. Con lo strumento VDM, questo pulsante è sostituito da `Materiale timbro`, che attiva o disattiva il materiale salvato nel timbro.
* `Decadimento` - quando è disattivato, la pittura resta a piena intensità fino al bordo del pennello.
* `Randomizza intensità` - se la parte di intensità della randomizzazione del tratto influisce sulla pittura. La randomizzazione di posizione, rotazione e scala sposta sempre l'intero timbro.

Queste opzioni vengono ignorate da [Dipingi tutto](#paint-all), ma la sua variante triplanare usa l'alfa.

### ![](/icons/link.webp) Materiale globale {#global-material}
Se questa opzione è attiva, il materiale selezionato è lo stesso degli altri strumenti. Nota che tiene conto solo delle impostazioni di rugosità, metallicità e colore. Disattivala per dare a questo strumento un materiale tutto suo.


## Materiale {#material}
![](/images/paint_material.webp) 

La prima icona è una forma di anteprima del materiale. Trascinando sull'anteprima 3d del materiale la fai ruotare. 

La seconda icona è un'anteprima del tratto di pittura con l'alfa e le opzioni di decadimento selezionate.

### ![](/icons/falloff.webp) Curve {#curves}

Apre un editor di curve per gli slot texture dei [cursori PBR](#pbr-sliders). Rimappa i valori della texture prima che vengano dipinti, senza toccare il file immagine. Una piccola icona a curva su uno slot texture ti indica che la sua curva è stata modificata.

### ![](/icons/cog.webp) Opzioni del materiale {#material-options}

Il pulsante `Materiale` accanto al titolo contiene due impostazioni.

`Anteprima materiale nel viewport` stabilisce cosa succede sull'oggetto selezionato mentre cambi i cursori di colore, rugosità, metallicità, opacità e intensità:

* `Nessuno` - Nessuna anteprima viene mostrata sul modello quando regoli le proprietà
* `Materiale` - I valori del materiale vengono mostrati in anteprima sull'oggetto quando regoli le proprietà.
* `Triplanare` - Il materiale viene mostrato in anteprima come proiezione triplanare. 

Le caselle di colore, rugosità, metallicità e opacità qui sotto scelgono quali canali vengono sostituiti dal [Contagocce materiale](#material-picker).

### ![](/icons/dropper.webp) Contagocce materiale {#material-picker}

Il contagocce preleva il materiale sotto il cursore, da qualsiasi oggetto della scena. Vengono sostituiti solo i canali spuntati nelle [Opzioni del materiale](#material-options).

## Preset di materiali {#material-presets}
Toccando la forma di anteprima 3d si apre un menu di preset di materiali, che puoi clonare per definire i tuoi preset.

![](/images/paint_presets.webp) 

L'interruttore `Incorpora texture` salva dentro il preset una copia delle texture usate da questo materiale. Senza di esso, il preset fa solo riferimento alle texture nella cartella textures/ di Nomad. Attivalo quando vuoi condividere un preset con texture senza inviarle a parte.

`Includi Alpha` salva anche l'alfa del pennello nel preset del materiale.

## Cursori PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

La pittura [PBR](shading.md#pbr) usa 4 canali:
- `Colore` Il colore che verrà dipinto. Il contagocce può prelevare il colore da altre parti del modello o dalle immagini di riferimento.
- `Rugosità` Indica quanto una superficie è "ruvida" o "liscia". Un valore basso di rugosità dà riflessi nitidi.
- `Metallicità` Indica semplicemente se la superficie è metallica o no. Il valore dovrebbe essere quasi sempre 0% o 100%; i valori intermedi dovrebbero essere un'eccezione.
- `Opacità` Quanto si vede attraverso il materiale. A rigore non fa parte delle specifiche PBR, ma è utile in molte situazioni. 1 è completamente opaco, 0 è trasparente. Nota che opacità e rifrazione sono cose diverse: in Nomad la rifrazione si gestisce con il materiale di rifrazione. 

Se selezioni un preset di materiale, vengono dipinti 3 canali contemporaneamente (l'opacità spesso è esclusa di proposito). Così, invece di dipingere solo 'rosso', puoi dipingere 'un metallo rosso ruvido' o 'una plastica bianca liscia'.

Il quadrato è uno slot texture: toccalo per usare una texture per quella proprietà invece di un valore fisso. Una texture di colore tinge il colore, mentre una texture di rugosità, metallicità o opacità sostituisce il valore del cursore (la sua etichetta viene barrata per mostrarlo). Per la texture di opacità, `Usa Alpha come Valore` legge il canale alfa della texture invece del suo valore in scala di grigi.

Con lo strumento VDM, quando il timbro ha un proprio materiale, uno slot in più lo mostra accanto allo slot texture. Toccalo per usare o ignorare quel canale del timbro.

L'icona del pennello accanto ai cursori riempie con quella proprietà tutto l'oggetto.

La casella di spunta attiva o disattiva quella proprietà, così puoi per esempio dipingere solo il colore, oppure solo rugosità e opacità. 

Ecco alcuni esempi di diverse combinazioni di rugosità e metallicità:

|                | Metallicità 0%                    | Metallicità 100%             |
| :------------: | :-------------------------------: | :--------------------------: |
| Rugosità 0%    | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Rugosità 50%   | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Rugosità 100%  | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Rugosità e metallicità richiedono la modalità di shading [Illuminato (PBR)](shading.md#pbr). In modalità [MatCap](shading.md#matcap) o [Non illuminato](shading.md#unlit) vengono ignorate, e il menu mostra un avviso.
:::

::: tip
Quando usi le texture per la pittura PBR, spesso conviene passare a uno strumento come `Timbro`, oppure usare il menu Tratto per scegliere una modalità diversa da quella a punti, che può sbavare la texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Valuta di attivare `Ombreggiatura uniforme` [globalmente](settings.md#smooth-shading) o [per oggetto](material.md#smooth-shading) se dipingi una superficie metallica su un oggetto con pochi poligoni.
:::

## ![](/icons/paint.webp) Dipingi tutto {#paint-all}

![](/images/paint_paint_all.webp)

Applica il materiale attuale agli oggetti selezionati, in modalità standard con `Dipingi tutto`, oppure come proiezione triplanare con `Dipingi tutto + Triplanare`. La variante triplanare non è disponibile sulle primitive non ancora convalidate.

Le caselle accanto ai cursori di colore/metallicità/rugosità/opacità vengono rispettate: le proprietà disattivate non vengono riempite.

I pulsanti aggiuntivi controllano come Dipingi tutto può essere ulteriormente condizionato. La maggior parte mostra una percentuale, e sono in grigio quando non avrebbero alcun effetto:

| Icona                       | Descrizione                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Le zone mascherate non vengono toccate.       |
| ![](/icons/tool_hide.webp) | Le zone nascoste non vengono toccate.         |
| ![](/icons/opacity.webp)   | Usa il fattore di pittura dello strumento qui sopra. |
| ![](/icons/layer.webp)     | Le zone non dipinte di un livello non vengono toccate. |
| ![](/icons/triplanar.webp) | `Vertice`: la variante triplanare sposta anche la superficie con l'alfa, secondo l'intensità dello strumento indicata. |
| ![](/icons/cog.webp)       | Apre le impostazioni triplanari               |

### ![](/icons/cog.webp) Impostazioni triplanari {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Come per le [impostazioni triplanari nel menu Materiale](material.md#triplanar), puoi controllare la fusione delle proiezioni, la ripetizione e gli spostamenti. 

Usa la casella di anteprima in cima a questo menu per avere un'anteprima continua mentre regoli i valori.

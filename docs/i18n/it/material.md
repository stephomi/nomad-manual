# ![](/icons/material.webp) Materiale {#material}

Questo menu ti permette di cambiare il materiale dell'oggetto attuale, le proprietà di rendering dell'oggetto/del materiale, e di assegnare texture al materiale.

![](/images/material_overview.webp)

I materiali definiscono l'aspetto di un oggetto, controllando come reagisce alla luce e agli altri oggetti. L'aspetto di un oggetto dipende da queste proprietà:

* `Tipo`
* `Colore`
* `Rugosità`
* `Metallicità`
* `Opacità`
* `Riflettanza`
* `Emissivo`/`Sempre non illuminato`

Combinando queste proprietà puoi ottenere un'ampia varietà di risultati, dal fotorealistico al cartoon fino allo sperimentale.

Colore, rugosità, metallicità e opacità si possono dipingere: vedi le [opzioni di pittura dei vertici](painting.md) per saperne di più.

Tipo di materiale, riflettanza ed emissivo/non illuminato sono proprietà del materiale spiegate qui sotto.

I pulsanti `Copia` e `Incolla` in cima a questo menu ti permettono di copiare i materiali da un oggetto all'altro.

Nota che il motore di rendering di Nomad lavora in tempo reale: pur essendo potente, per certi effetti privilegia la velocità rispetto alla precisione. 

## Tipi di materiale {#material-types}

![](/images/material_types.webp)

I tipi di materiale di Nomad sono Opaco, Subsurface, Fusione, Additivo, Rifrazione, Dithering e Raccoglitore di ombre.

### ![](/icons/material_opaque.webp) Opaco {#opaque}
La modalità predefinita, che tratta le superfici come un materiale semplice che supporta colore, rugosità, metallicità e opacità dipinti. L'opacità dipinta, una texture di opacità o il canale alfa della texture di colore rendono comunque l'oggetto trasparente, usando il dithering. Viene ignorato solo il cursore principale dell'opacità.

### ![](/icons/material_subsurface.webp) Subsurface {#subsurface}
Questa modalità simula i materiali in cui la luce si diffonde e si disperde all'interno, come la pelle, la cera o la giada.

Richiede la modalità di shading PBR. Per il risultato migliore, usa almeno una luce direzionale o spot, idealmente con un ambiente poco luminoso.

Il campione di colore imposta il colore della luce diffusa.

`Profondità` controlla quanto la luce si diffonde dalla parte frontale sotto la superficie, per poi riuscire dalla superficie frontale. L'effetto ammorbidisce le ombre nette e sfuma i dettagli della superficie.

`Traslucenza` controlla come la luce si diffonde dal davanti al retro di una forma, come attraverso il rovescio di una foglia, o come nelle orecchie in forte controluce. Per vederla ti serve una luce che proietta ombre.

### ![](/icons/material_blending.webp) Fusione {#blending}

Simile a Opaco, ma supporta il cursore dell'opacità, per far passare il materiale da pieno a trasparente. È un semplice cursore unico per l'opacità, a differenza dell'opacità dipingibile supportata dal materiale opaco. 

::: warning
La modalità Fusione può causare sfarfallii e salti nelle forme complesse o che si intersecano.
:::

### ![](/icons/material_additive.webp) Additivo {#additive}
Con questo materiale puoi rendere la mesh semitrasparente. È simile al materiale Fusione, ma mentre Fusione si mescola con ciò che lo circonda, Additivo è sempre più luminoso degli oggetti dietro di lui: ottimo per effetti luminosi come raggi di luce, fuoco o esplosioni.

Puoi impostare un'opacità superiore a 1, e l'oggetto risulterà più luminoso.  
È utile se vuoi usare il [bagliore diffuso](postprocess.md#bloom) e il `parametro di soglia` per far brillare solo questo oggetto, come un oggetto emissivo.

Questa modalità tende ad avere meno artefatti di [Fusione](#blending) (trasparenza indipendente dall'ordine).

### ![](/icons/material_refraction.webp) Rifrazione {#refraction}
Questa modalità serve a simulare il vetro. Richiede la modalità di shading PBR. Per i limiti del tempo reale, l'auto-rifrazione e la rifrazione su più strati sono piuttosto limitate.

La rugosità dipinta sul modello influisce su quanto è sfocata la rifrazione.
Di default, ogni oggetto creato in Nomad ha una rugosità di circa il 25%, quindi la rifrazione non sarà perfetta ma un po' sfocata.
Puoi usare il pulsante `Pittura lucida` per ridipingere il modello con rugosità e metallicità a 0 (i colori non vengono toccati).

Entrano in gioco 2 rugosità diverse: una determina quanto è sfocato il riflesso sulla superficie, l'altra l'interno (la rifrazione).  
Però, dato che Nomad ha un solo canale di rugosità dipinta, la rugosità interna ed esterna condividono lo stesso valore.  
Per avere valori diversi (per esempio un lecca-lecca con la superficie nitida ma l'interno sfocato), usa i cursori `Superficie` e `Interna` sotto `Ignora rugosità` per sostituire la rugosità dipinta.

![](/videos/refraction.mp4)

#### Indice di rifrazione {#index-of-refraction}
Quanto si piega la luce quando entra nell'oggetto. Valori più alti la piegano di più, come una lente spessa.

#### Assorbimento {#absorption}
Simula la luce assorbita mentre attraversa il volume, tinta dal campione di colore, con `Fattore` che ne imposta l'intensità. Le parti sottili sono più chiare perché lasciano passare più luce, mentre quelle spesse sono più scure. Viene usata solo un'approssimazione dello spessore dell'oggetto, quindi l'effetto dipende molto dalla forma.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Rende l'oggetto semitrasparente scartando alcuni pixel in modo casuale.

### ![](/icons/material_shadow_catcher.webp) Raccoglitore di ombre {#shadow-catcher}

Rende l'oggetto invisibile, e gli fa ricevere solo le ombre delle luci. Utile per combinare i render di Nomad con altre immagini, di solito su un piano. Il campione di colore imposta il colore dell'ombra.

Nella scena deve esserci una luce che proietta ombre, altrimenti il raccoglitore di ombre non fa nulla. I pulsanti `Metallicità → 0%` e `Metallicità → 100%` ridipingono l'oggetto: se è completamente metallico, il raccoglitore di ombre può anche riflettere la scena quando il post processing [Riflessione (SSR)](postprocess.md#reflection-ssr) è attivo.

::: tip

Altre informazioni sulla trasparenza e sulle modalità di fusione si trovano su https://support.fab.com/s/article/Transparency-Opacity

:::

## Controlli {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Sempre non illuminato {#always-unlit}
Se è attivo, l'oggetto ignora PBR e MatCap e mostra semplicemente il colore dipinto, senza ombreggiatura.
Nota che, se usi [Additivo](#additive), puoi dipingere direttamente la trasparenza usando il colore nero.

### Opacità {#opacity}
Quanto un oggetto appare pieno od opaco: 100% è pieno, 0% è trasparente. Il cursore compare per i tipi Fusione, Additivo, Dithering e Raccoglitore di ombre. Puoi anche dipingere l'opacità per un controllo più fine.

### Passaggio di pre-rifrazione {#pre-refract-pass}
Solo Fusione e Additivo. Disegna questo oggetto trasparente prima del passaggio di rifrazione. Utile quando un oggetto rifrangente si trova davanti ad altre superfici trasparenti.

### Riflettanza {#reflectance}
Controlla la quantità di riflesso che il materiale riceve, per i materiali non metallici. Il più delle volte conviene lasciare il valore predefinito (che corrisponde al classico 4% di luce riflessa ad angolo normale), ma puoi aumentarlo per accentuare riflessi e luci negli occhi di un personaggio, per esempio. Richiede la modalità di shading PBR.

### ![](/icons/culling.webp) Culling inverso {#inverse-culling}
Inverte le normali di una superficie. Di solito non serve, ma puoi usarlo se un modello appare rovesciato, oppure, con `Dai due lati` disattivato, per creare interni in cui la parete più vicina alla fotocamera è sempre nascosta.

Le opzioni seguenti possono essere impostate su `Auto`, `No` o `Sì`. Con `Auto`, la freccia mostra il valore effettivamente usato.

### ![](/icons/sphere_smooth.webp) Ombreggiatura uniforme {#smooth-shading}
Vedi l'[opzione globale](settings.md#smooth-shading).  
Il valore `Auto` usa l'opzione globale.

### ![](/icons/culling.webp) Dai due lati {#two-sided}
Le facce sono visibili da entrambi i lati. Vedi l'[opzione globale](settings.md#two-sided-quick).  
Il valore `Auto` usa l'opzione globale.

### ![](/icons/culling.webp) Lato posteriore colorato {#coloured-backface}
Vedi l'[opzione globale](settings.md#two-sided-quick).
Il valore `Auto` usa l'opzione globale.

### ![](/icons/shadow_cast.webp) Proietta ombre {#casts-shadows}
Anche gli oggetti trasparenti proiettano ombre (con un motivo a dithering per imitare le ombre sfumate).  
Ricordati di disattivare la proiezione delle ombre se nella scena hai un oggetto grande che non ne ha bisogno (per esempio un grande pavimento).

### ![](/icons/shadow_receive.webp) Ricevi ombre {#recieve-shadows}
Stabilisce se le ombre degli altri oggetti vengono disegnate su questo oggetto.

### ![](/icons/wireframe.webp) Wireframe {#wireframe}
Vedi l'[opzione globale](settings.md#wireframe).  
Il valore `Auto` usa l'opzione globale.

### ![](/icons/trash.webp) Ripristina normali {#reset-normals}
Compare solo quando un oggetto importato porta con sé le proprie normali (per esempio con `Mantieni topologia`). Le rimuove, così l'ombreggiatura usa le normali calcolate dalla superficie.


## Texture {#textures}

![](/images/material_textures.webp)

Se un oggetto ha gli UV, puoi applicare delle texture al materiale, oltre al colore/rugosità/metallicità/opacità dei vertici. Di solito sono il risultato di un trasferimento delle texture, ma puoi usare anche immagini create fuori da Nomad. `UV:✓` o `UV:✗` accanto al titolo ti dice se l'oggetto ha gli UV.

Le texture si possono applicare a

* Colore
* Normale
* Rugosità
* Metallicità
* Opacità
* Spostamento
* Emissivo

Compare anche una riga `Occlusione` quando un oggetto importato ha una texture di occlusione, ma Nomad non la usa.

Il cursore di ogni riga imposta con quanta forza viene applicata la sua texture, da per niente a completamente. `Colore` ed `Emissivo` hanno anche un campione di colore che tinge la texture, ed `Emissivo` imposta l'intensità del bagliore.

`Spostamento` imposta quanto la mappa di spostamento spinge la superficie. Il suo pulsante `Applica` sposta i vertici secondo lo spostamento, poi rimuove la mappa. Il risultato va nel livello attivo.

Il pulsante con la tavolozza accanto al titolo apre i preset di materiali del menu [Pittura](painting.md): toccane uno per copiarne le texture sull'oggetto. Sul computer, le immagini importate si sincronizzano con il loro file originale quando torni in Nomad, e un pulsante di sincronizzazione accanto al titolo le ricarica.

Toccando uno slot texture si apre un selettore. Dopo aver assegnato una texture a uno slot del materiale, toccandolo di nuovo si apre il pannello della texture:

### Opzioni del pannello texture {#texture-panel-options}

![](/images/material_texture_panel.webp)

Il pannello mostra le dimensioni dell'immagine e un'anteprima della texture.

### ![](/icons/open.webp) Apri {#open}
Seleziona un'altra texture. Sul computer, `Esplora` mostra il file immagine nel tuo gestore di file.

### ![](/icons/circle_cross.webp) Nessuno {#none}
Rimuove la texture

### Opacità {#texture-opacity}

Solo per la texture di colore. Se l'immagine ha un canale alfa, ti permette di usarlo per l'opacità, oppure di ignorarlo.

### Formato {#normal-format}
Solo per la texture delle normali. Le normal map esistono in due varianti, `OpenGL (+Y)` e `DirectX (-Y)`. Se i dettagli sembrano invertiti, prova l'altra.

### Altezza {#displacement-height}
Solo per la texture di spostamento.
* `Locale` - L'altezza cresce e diminuisce con la scala dell'oggetto.
* `Mondo` - L'altezza resta la stessa qualunque sia la scala dell'oggetto.

### Moltiplica {#multiply}
Solo per le texture di rugosità, metallicità e opacità. Moltiplica i valori della texture. Quando non è al 100%, il valore viene mostrato sullo slot texture.

### ![](/icons/link.webp) Icona catena/collegamento {#chainlink-icon}

L'icona di collegamento nelle sezioni seguenti, quando è attiva, fa sì che le opzioni usate siano condivise con le altre texture (colore, normale, rugosità, metallicità, opacità, emissivo) che hanno anch'esse l'icona di collegamento attiva. 

Così, se hai texture allineate, resteranno allineate anche quando modifichi i parametri o i tipi di proiezione.


### Proiezione {#projection}
![](/images/material_projection.webp)

Imposta come applicare la texture all'oggetto.

* `Auto` - UV se l'oggetto ha gli UV, altrimenti Triplanare
* `UV` - Usa le coordinate UV della mesh per applicare la texture. Se la mesh e la texture vengono da fuori Nomad, o saranno esportate da Nomad per usarle altrove, UV è l'opzione giusta.
* `Triplanare` - Proietta la texture lungo gli assi X, Y e Z, e fonde le giunture. 

### Triplanare {#triplanar}
![](/images/material_triplanar.webp)

Le proiezioni triplanari sono un modo potente ma semplice di applicare texture agli oggetti.

Una proiezione triplanare è come avere 6 videoproiettori con la stessa immagine, puntati sul davanti, sul retro, a sinistra, a destra, sopra e sotto l'oggetto.

Il risultato può poi essere trasferito sugli UV o sui colori dei vertici, se serve.


![](/images/material_triplanar_example.webp)

#### Metodo {#method}

* `Locale` - La proiezione si sposta con la trasformazione dell'oggetto
* `Mondo` - Le proiezioni restano fisse: spostando l'oggetto, questo scorre attraverso la proiezione.

#### Durezza {#hardness}

Come si mescolano le proiezioni. Al 100% non c'è fusione, e i bordi delle proiezioni sono netti. Allo 0% i bordi si fondono su un angolo ampio. Il valore predefinito è 90%: abbastanza fusione per nascondere i bordi, lasciando nitido il resto delle proiezioni.

### Uniforme {#uniform}

Se è spuntata, la stessa durezza vale per tutte le proiezioni. Se non è spuntata, compaiono controlli di durezza separati per le proiezioni X, Y e Z.


### Parametro {#parameter}
![](/images/material_parameter.webp)

#### Filtraggio {#filtering}
Il metodo di filtraggio della texture: `Auto` è il predefinito, i metodi sono `Più vicino`, `Lineare` e `Mipmap`. Più vicino non filtra, quindi le texture possono avere artefatti seghettati se viste da vicino. Lineare e Mipmap filtrano meglio, quindi da vicino le texture appaiono sfocate invece che seghettate.

#### Ripetizione - X {#tiling-x}
Se il parametro Scala è maggiore di 1, rendendo la texture più piccola degli UV dell'oggetto, stabilisce come la texture si ripete lungo l'asse X. `Nessuno` significa nessuna ripetizione. `Ripeti` crea copie della texture. `Specchia` crea copie della texture, con una copia su due capovolta, il che può aiutare a nascondere gli artefatti della ripetizione.

#### Ripetizione - Y {#tiling-y}
Come Ripetizione - X, ma per l'asse Y.

### Trasforma {#transform}
![](/images/material_transform.webp)

Trasformazioni 2d aggiuntive applicate alla texture nello spazio UV. Il pulsante di ripristino riporta ai valori predefiniti; l'icona della catena (quando sono selezionate texture diverse da quella di colore) collega o scollega la trasformazione da quella della texture di colore.

#### Traslazione {#translation}
Lo spostamento X e Y della texture

#### Rotazione {#rotation}
La rotazione della texture

#### Scala {#scale}
La scala della texture: valori più grandi rendono la texture più piccola sull'oggetto; usa le opzioni Ripetizione - X e Ripetizione - Y per controllare cosa succede.

### Scala uniforme {#uniform-scale}
Quando è disattivata, Nomad mostra controlli separati per Scala X e Scala Y.

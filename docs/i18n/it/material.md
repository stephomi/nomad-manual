# ![](/icons/material.webp) Materiale

Questo menu consente di cambiare il materiale dell'oggetto corrente, le proprietà di rendering dell'oggetto/materiale e di assegnare texture al materiale.

![](/images/material_overview.webp)

I materiali definiscono l'aspetto di un oggetto, controllando come reagisce alla luce e agli altri oggetti. L'aspetto di un oggetto è controllato da queste proprietà:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Combinazioni di queste proprietà possono ottenere una grande varietà di risultati, dal fotorealistico al cartoonesco allo sperimentale.

Color, roughness, metalness e opacity possono essere dipinti, vedi [Vertex Paint options](painting.md) per maggiori informazioni.

Material type, reflectance, emssive/unlit sono proprietà del materiale spiegate di seguito.

I pulsanti copia/incolla nella parte superiore di questo menu consentono di copiare i materiali da un oggetto a un altro.

Nota che il renderer di Nomad è un renderer in tempo reale; pur essendo potente, privilegia la velocità rispetto all'accuratezza per alcuni effetti. 

## Material types

![](/images/material_types.webp)

I tipi di materiale di Nomad sono Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaque
La modalità predefinita che tratta le superfici come un semplice materiale che supporta color, roughness, metalness, opacity dipinti.

### ![](/icons/material_subsurface.webp) Subsurface
Questa modalità può simulare materiali che permettono alla luce di sfocarsi e diffondersi internamente, come pelle, cera, giada.

Per ottenere il risultato migliore, passa alla modalità di shading PBR e usa almeno una luce direzionale o spot, idealmente con un environment tenue.

`Depth` controlla quanto lontano la luce si diffonde dalla parte frontale, sotto la superficie, per poi uscire di nuovo dalla superficie frontale. Questo ha l’effetto di ammorbidire le ombre dure e sfocare i dettagli superficiali.

`Translucency` controlla come la luce si diffonde dalla parte frontale a quella posteriore di una forma, come la diffusione attraverso la parte inferiore di una foglia, o quando le orecchie sono fortemente retroilluminate. 

### ![](/icons/material_blending.webp) Blending

Simile a Opaque, ma supporta lo slider di opacity per permettere al materiale di mescolarsi tra solido e trasparente. Questo è un semplice slider singolo per l’opacità, rispetto all’opacità dipingibile supportata dal materiale opaque. 

::: warning
La modalità Blending può causare sfarfallii e salti in forme complesse o intersecanti.
:::

### ![](/icons/material_additive.webp) Additive
Puoi rendere la tua mesh semitrasparente con questo materiale. È simile al materiale blending, ma mentre blending si mescola con ciò che lo circonda, additive sarà sempre più luminoso degli oggetti dietro di esso, adatto per effetti luminosi come raggi di luce, fuoco, esplosioni.

Puoi impostare un valore di opacity superiore a 1, il che significa che l’oggetto sarà più luminoso.  
Può essere utile se vuoi usare il [bloom](postprocess.md#bloom) e il `threshold parameter` per far brillare solo questo oggetto come un oggetto emissive.

Questa modalità tende ad avere meno artefatti rispetto a [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Refraction
Questa modalità può essere usata per simulare materiali in vetro. A causa dei vincoli del tempo reale, l’auto-rifrazione e la rifrazione multistrato sono in qualche modo limitate.

La roughness dipinta del modello influisce su quanto sfocata è la rifrazione.
Per impostazione predefinita, ogni oggetto creato in Nomad ha una roughness leggermente intorno al 25%, quindi la rifrazione non sarà perfetta ma un po’ sfocata.
Puoi usare il pulsante `paint glossy` per ridipingere il modello con roughness e metalness pari a 0 (i colori non saranno influenzati).

Ci sono 2 roughness diverse in gioco: una che controlla quanto è sfocato il riflesso sulla superficie e l’altra che controlla l’interno (rifrazione).  
Tuttavia, poiché in Nomad esiste un solo canale di roughness dipingibile, sia la roughness interna che quella esterna condivideranno lo stesso valore.  
Per avere valori diversi (per esempio un lecca-lecca con superficie nitida ma interno sfocato) usa gli slider `Surface glossiness` e `Interior roughness` per sovrascrivere la roughness dipinta.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering
Rende l’oggetto semitrasparente scartando alcuni pixel in modo casuale.

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher

Rende l’oggetto invisibile e riceve solo le ombre. Utile per combinare i render di Nomad con altre immagini. 

::: tip

Ulteriori informazioni su trasparenza e modalità di blending sono disponibili su https://support.fab.com/s/article/Transparency-Opacity

:::

## Controls

![](/images/material_controls.webp)

### Always unlit
Se abilitato, l’oggetto ignorerà PBR e Matcap e mostrerà semplicemente il suo color dipinto senza shading.
Nota che se usi [Additive](#additive), puoi dipingere la trasparenza direttamente usando il colore nero.

### Opacity
Quanto solido od opaco apparirà un oggetto; 100% è solido, 0% è trasparente. Puoi anche dipingere l’opacità per un controllo più fine.

### Reflectance
Controlla la quantità di riflessione che il materiale riceverà per i materiali non metallici. Nella maggior parte dei casi dovrebbe essere usato il valore predefinito (che corrisponde al 4% standard di luce riflessa ad angolo normale), ma può essere aumentato per potenziare riflessi e highlight negli occhi di un personaggio, per esempio.

### Inverse culling
Inverte le normali di una superficie. Di solito non è necessario, ma può essere usato se un modello appare capovolto, o in combinazione con `Two sided` disabilitato, per creare interni in cui la parete più vicina alla camera è sempre nascosta.

### Smooth Shading
Vedi l’[opzione globale](settings.md#smooth-shading).  
Il valore `Auto` userà l’opzione globale.

### Two sided
Vedi l’[opzione globale](settings.md#two-sided).  
Il valore `Auto` userà l’opzione globale.

### Coloured backface
Vedi l’[opzione globale](settings#two-sided).
Il valore `Auto` userà l’opzione globale.

### Casts shadows
Per ora `Auto` è uguale a `On`.
Anche gli oggetti trasparenti proiettano ombre (con un pattern di dithering per emulare ombre sfumate).  
Assicurati di disabilitare la proiezione di ombre se hai un grande oggetto nella scena che non ha bisogno di proiettarle (per esempio un grande pavimento).

### Recieve shadows
Per ora `Auto` è uguale a `On`.

### Wireframe
Vedi l’[opzione globale](settings.md#wireframe).  
Il valore `Auto` userà l’opzione globale.


## Textures

![](/images/material_textures.webp)

Se un oggetto ha UV, allora le texture possono essere applicate al materiale in aggiunta a vertex color/roughness/metalness/opacity. Di solito sono il risultato di un texture bake, ma possono essere usate anche immagini create al di fuori di Nomad.

Le texture possono essere applicate a

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Facendo clic su uno slot di texture verrà visualizzato un selettore. Dopo che una texture è stata assegnata a uno slot del materiale, facendo nuovamente clic verrà visualizzato un pannello texture:

### Texture panel options

![](/images/material_texture_panel.webp)

### Open
Seleziona un’altra texture

### None
Rimuovi la texture

### Opacity

Se l’immagine ha un canale alfa, questo ti permetterà di usarlo per l’Opacity o di ignorarlo.

### ![](/icons/link.webp) Chain/Link icon 

L’icona di collegamento nelle sezioni seguenti, quando abilitata, farà sì che qualunque opzione venga usata, sarà condivisa con le altre texture (color, normal, roughness, metalness, opacity, emissive) che hanno anch’esse la loro icona di collegamento abilitata. 

Questo ti permette di assicurarti che, se hai texture allineate, rimarranno allineate anche quando modifichi parametri o tipi di proiezione.


### Projection
![](/images/material_projection.webp)

Imposta come la texture deve essere applicata all’oggetto.

* `Auto` - Se l’oggetto ha UV, UV, altrimenti Triplanar
* `UV` - Usa le coordinate UV della mesh per applicare la texture. Se la mesh e la texture provengono da fuori Nomad, o devono essere esportate da Nomad per essere usate altrove, UV è l’opzione corretta.
* `Triplanar` - Proietta la texture lungo gli assi X,Y,Z e sfuma le giunzioni. 

### Triplanar
![](/images/material_triplanar.webp)

Le proiezioni triplanari sono un modo potente ma semplice per applicare texture agli oggetti.

Triplanar è come avere 6 videoproiettori tutti con la stessa immagine, che illuminano la parte frontale, posteriore, sinistra, destra, superiore e inferiore del tuo oggetto.

Questo può poi essere bakeato in UV o vertex color se necessario.


![](/images/material_triplanar_example.webp)

#### Method

* `Local` - La proiezione si muoverà con la trasformazione dell’oggetto
* `World` - La proiezione rimane fissa, spostare l’oggetto lo farà scorrere attraverso la proiezione.

#### Hardness

Come si mescolano le proiezioni. 100% non farà alcun blending e i bordi delle proiezioni saranno netti. 0% sfumerà i bordi su un ampio angolo. Il valore predefinito è 90%, sufficiente miscelazione per nascondere i bordi e lasciare il resto delle proiezioni nitido.

### Uniform

Quando è selezionato, viene usata la stessa hardness per tutte le proiezioni. Quando è deselezionato, vengono mostrati controlli di hardness aggiuntivi per le proiezioni X, Y, Z.


### Parameter
![](/images/material_parameter.webp)

#### Filtering
Il metodo di filtro della texture da usare, `Auto` è il predefinito, i metodi sono `Nearest`, `Linear`, `Mipmap`. Nearest non fa alcun filtraggio, quindi le texture possono avere artefatti frastagliati quando viste da vicino. Linear e Mipmap fanno un filtraggio migliore, quindi le texture appaiono sfocate piuttosto che frastagliate da vicino.

#### Tiling-X
Se il parametro Scale è maggiore di 1, rendendo la texture più piccola degli UV dell’oggetto, come verrà ripetuta la texture lungo l’asse X. `None` significa nessuna ripetizione. `Repeat` farà copie della texture. `Mirror` farà copie della texture, con ogni seconda copia invertita, il che può aiutare a nascondere gli artefatti di tiling.

#### Tiling-Y
Come Tiling-X, ma per l’asse Y.

### Transform
![](/images/material_transform.webp)

Ulteriori trasformazioni 2D applicate alla texture nello spazio UV. Il pulsante reset ripristina i valori predefiniti, l’icona a catena (quando sono selezionate texture diverse da color) collegherà o scolleggerà la trasformazione per essere la stessa della texture color.

#### Translation
L’offset X e Y della texture

#### Rotation
La rotazione della texture

#### Scale
La scala della texture, numeri più grandi renderanno la texture più piccola sull’oggetto, usa gli slider Tiling-X e Tiling-Y per controllare cosa succede.

### Uniform scale
Quando è disattivato, Nomad mostrerà controlli separati per Scale-X e Scale-Y.

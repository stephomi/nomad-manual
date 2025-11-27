# ![](/icons/toolbox.webp) Strumenti

![](/images/tools_menu.webp)

::: tip
Vai a [Strumenti](#tools-1) per le descrizioni dei singoli strumenti.
:::

## Panoramica

Gli strumenti vengono selezionati dalla `Toolbox` a destra e controllati con i `Tool Controls` a sinistra. Impostazioni aggiuntive si trovano nel menu `Settings`, la prima icona nel menu in alto a destra.

Gli strumenti pennello hanno controlli per dimensione e intensità. Gli strumenti di selezione hanno controlli per diversi stili di selezione. In fondo ai controlli dello strumento ci sono scorciatoie per operazioni usate di frequente (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Gli strumenti di Nomad sono codificati a colori nella toolbox:

* <span class=brush>**Brush tools**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Move tools**</span> (Move, Drag)
* <span class=mask>**Mask tools**</span> (Mask, SelMask)
* <span class=paint>**Paint tools**</span> (Paint, Smudge)
* <span class=flatten>**Flatten tools**</span> (Flatten, Planar)
* <span class=pinch>**Pinch tools**</span> (Crease, Pinch)
* <span class=selection>**Selection based tools**</span> dove prima si disegna una maschera 2D, poi avviene un’operazione (Trim, Split, Project)
* <span class=creation>**Creation tools**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transform tools**</span> (Transform, Gizmo)
* <span class=misc>**Misc tools**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**View tool**</span>



Molti di questi strumenti possono essere personalizzati con diversi comportamenti del pennello, pressione, texture ecc tramite il menu [Stroke](stroke.md). 


### Controlli del pennello

La barra degli strumenti a sinistra ha slider per raggio e intensità, e poi controlli specifici per la categoria di strumento, spiegati sotto.

![](/images/tool_left_panel.webp)

::: tip
Lo slider di intensità per molti strumenti può andare oltre il 100%, vale la pena sperimentare!
:::

### Sub mode
Il pulsante direttamente sotto lo slider di intensità è il pulsante `Sub`. La sua etichetta e funzione cambieranno con ogni strumento, e quando premuto invocherà un comportamento alternativo, di solito opposto. Ad es. per [Paint](#paint) invocherà una modalità Erase, per [Crease](#crease) creerà bordi rialzati invece che incisioni ecc.

Per impostazione predefinita funziona come un pulsante “sticky”; cioè puoi tenerlo premuto per attivarlo temporaneamente, quando lo rilasci verrà disattivato. Se lo tocchi, la sub mode verrà attivata in modo permanente.

### Scorciatoie
In fondo alla barra degli strumenti di sinistra ci sono scorciatoie per [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Per impostazione predefinita funzionano tutti come pulsanti “sticky”; cioè puoi tenerli premuti per attivarli temporaneamente, quando li rilasci verranno disattivati. Se li tocchi, quella modalità scorciatoia verrà attivata in modo permanente.

### Controlli di selezione

Gli strumenti [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) e [Hide](#hide) usano controlli simili per selezionare aree della mesh.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Una forma disegnata a mano libera
* `Polygon` - Una forma chiusa definita da una combinazione di curve e/o linee rette. Vedi [Shape editing](#shape-editing) sotto per maggiori informazioni.
* `Curve` - (solo Project) - Una curva a mano libera per la proiezione
* `Path` - (solo Project) - Una curva definita da punti. Vedi [Shape editing](#shape-editing) sotto per maggiori informazioni.
* `Line` - Trascina una linea per definire un segmento planare. Per impostazione predefinita opererà immediatamente sulla mesh, disattiva l’auto validate se non vuoi questo comportamento (pressione prolungata o swipe sull’icona della linea)
* `Rect` - Trascina una linea diagonale, questo definirà gli angoli di un rettangolo. Pressione prolungata o swipe per mostrare le opzioni per auto validate, forzare una forma quadrata e far sì che il primo clic sia il centro del rettangolo.
* `Ellipse` - Trascina una linea diagonale, questo definirà la dimensione di un’ellisse. Pressione prolungata o swipe per mostrare le opzioni per auto validate, forzare una forma circolare e far sì che il primo clic sia il centro dell’ellisse.
* `Flip` - inverte la maschera della forma o la direzione dello strumento project.

La maggior parte degli strumenti ha un’opzione di auto validate, il che significa che l’operazione avverrà non appena avrai finito di disegnare la forma. Quando l’auto validate è disattivato, verrà disegnato un pulsante verde accanto alla forma che eseguirà l’operazione. Questo ti permette di modificare la forma, regolare la vista, e quando sei pronto per usare la forma, premi il pulsante verde.

### Shape editing
L’editing di poligoni e curve si comporta in modo simile:

* Per iniziare, trascina una linea per definire 2 punti, poi trascina dal centro della linea per definire un poligono o una curva.
* Clicca sui punti per alternare tra morbido e spigoloso. 
* Clicca e trascina sulle sezioni di curva o linea per creare nuovi punti.
* Per eliminare un punto, trascinalo nel suo vicino finché non diventa rosso.
* L’icona del cestino nell’angolo dell’icona del poligono o del path eliminerà la forma.

### Menu Settings

Molti strumenti hanno impostazioni extra che si trovano nel menu settings, la prima icona nel menu in alto a destra:

![](/images/tools_settings_menu.webp)

## Tools

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
Lo strumento Clay è utile per costruire la tua scultura. `Sub` rimuoverà materiale dalla scultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
Il pennello standard. `Sub` rimuoverà materiale.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
L’area sotto il pennello si attaccherà al pennello, permettendo una deformazione elastica. La selezione viene mantenuta durante il movimento, quindi se sposti il pennello lontano, poi lo riporti dove hai iniziato, non vedrai alcuna deformazione.

La sub mode è `Normal` e sposterà l’area sotto il pennello lungo la normale della superficie.

Questo pennello è adatto sia per deformazioni su larga scala che per piccole deformazioni precise.

#### Impostazioni Move

* `Radius (Background)` - Quanto lontano dal bordo di un modello puoi essere e continuare a scolpire, utile quando lavori sulla silhouette di un oggetto. 
* `Same-side vertex only` - Ignora i vertici che puntano nella direzione opposta alla deformazione.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
L’area sotto il pennello si attaccherà al pennello, permettendo una deformazione elastica. A differenza del pennello Move, la selezione viene aggiornata continuamente durante la pennellata, quindi è possibile creare oggetti lunghi e sinuosi, specialmente quando la Dynamic Topology è attivata.

La sub mode è `Normal` e sposterà l’area sotto il pennello lungo la normale della superficie.

Questo pennello è adatto a modifiche di forma più libere e gestuali.

#### Impostazioni Drag

* `Radius (Background)` - Quanto lontano dal bordo di un modello puoi essere e continuare a scolpire, utile quando lavori sulla silhouette di un oggetto. 
* `Same-side vertex only` - Ignora i vertici che puntano nella direzione opposta alla deformazione.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Leviga l’area mediando le posizioni dei punti. Questo strumento dipende fortemente dalla densità dei poligoni.
Quindi se hai molti poligoni, la levigatura sarà meno efficace.

La sub mode è `Relax`, che leviga solo la wireframe ma cerca di mantenere i dettagli geometrici.

#### Impostazioni Smooth

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Levigherà i bordi dei facegroup. Usa un’intensità superiore al 100% per levigare rapidamente i bordi. `Auto` levigherà solo se l’anteprima dei facegroup è abilitata, `Off` disabilita, `On` abilita. 

##### Vertex
* `Sticky vertex on border` - Per mesh con bordi aperti, ad es. un piano, è possibile levigare gli angoli. Abilitando questa opzione i bordi aperti verranno bloccati.
* `Relax` - uguale alla modalità alternativa relax nella barra degli strumenti a sinistra.
* `Stable smoothing` - Cerca di rendere la levigatura indipendente dalla topologia. Funziona meglio con densità di topologia variabile e con un valore di intensità di smoothing alto.

##### Painting
* `Screen Smoothing` - Usa questa opzione per ottenere una levigatura indipendente dalla topologia, anche ad alti conteggi di poligoni.
* `Screen samples` - La qualità della levigatura, valori più alti saranno più morbidi ma più lenti.

::: tip
Densità di poligoni più alte possono richiedere di aumentare l’intensità oltre il 100%. Valori molto alti (300%, 500%) possono anche funzionare bene come strumento di scultura, forzando le aree a diventare piatte e lisce rapidamente sotto il pennello, come colpire l’argilla con un mazzuolo!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Questo strumento ti permette di mascherare i vertici. I vertici mascherati sono protetti da scultura o pittura. 

La sub mode è `Unmask` e cancellerà dove la maschera è stata dipinta.

Simile alle selezioni nei programmi di pittura 2D, le maschere possono essere dipinte con un pennello o create con selezioni di forma, sfocate o affilate. 

A differenza dei programmi di pittura 2D, possono anche essere create tramite facegroup, e le maschere possono essere usate per creare nuova geometria tramite operazioni in stile estrusione/estrazione. 

![](/videos/tool_mask1.mp4)

 Una toolbar apparirà nella parte superiore della viewport con controlli extra. 

![](/images/tool_mask_toolbar.webp)

Il titolo della barra può essere toccato per espandere/comprimere, oppure la freccia in alto a destra può essere toccata per spostarla in alto o in basso nell’interfaccia.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Cancella la maschera                                                                       |
| ![](/icons/invert.webp)        Invert             | Inverte la maschera                                                                        |
| ![](/icons/sharpen.webp)       Sharpen            | Affila il bordo della maschera                                                             |
| ![](/icons/blur.webp)          Blur               | Sfoca il bordo della maschera                                                              |
|                                 Blur ->            | Trascina a sinistra/destra per sfocare interattivamente la maschera                       |
| ![](/icons/culling.webp)       Front              | Attiva per mascherare solo i vertici frontali                                             |
|                                 Convert            | Converte la maschera in un facegroup                                                      |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Quando abilitato i facegroup verranno mostrati, toccandone uno lo si mascherà             |
|                                 On tap (mask)      | Quando abilitato, toccare un “isolotto” di poligoni mascherati o non mascherati lo riempirà |
| ![](/icons/vertex.webp)        Connected          | Quando abilitato permette alle pennellate di maschera di influenzare solo topologia connessa |

##### Gesture rapide Mask
Puoi eseguire gesture in stile ZBrush mentre tieni premuto il pulsante di quick masking nella barra in basso a sinistra:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Tap sullo sfondo                   |
| Clear   | Trascina sullo sfondo              |
| Blur    | Tap sull’area mascherata           |
| Sharpen | Tap sull’area non mascherata       |


#### Impostazioni Mask
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Il menu delle impostazioni Mask è usato principalmente per creare geometria dalla maschera. Per questo il comportamento predefinito è di mostrare un’anteprima di come sarà la nuova geometria. Puoi scegliere di non avere anteprima, un’anteprima di estrazione, un’anteprima di split e se questa geometria sarà mostrata in modalità x-ray.

##### Thickness
* `Height` - L’altezza della forma estratta. L’icona Plus/Minus ti permette di passare ciclicamente tra un’estrusione verso l’esterno, verso l’interno o centrata. 
* `Height/Height+Mask` - Alterna tra altezza costante o se le parti sfocate della maschera devono influenzare l’altezza, permettendo forme morbide con altezze variabili. 

##### Smoothness
Quando attivo, leviga il bordo della forma estratta, funziona meglio con conteggi di poligoni più alti. 
* `Iterations` - La quantità di levigatura applicata. Valori alti produrranno bordi curvi molto lisci, ma inizieranno ad allontanarsi dalla forma della maschera.
* `All/Sharp border/Borders only` - La levigatura può funzionare in tutte le direzioni, levigando sia i lati che la parte superiore della forma estratta, oppure levigare la parte superiore e i lati ma mantenere un bordo netto, oppure levigare solo il bordo lasciando la superficie superiore invariata.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Calcolerà il numero di divisioni sui lati della forma estratta per creare poligoni quadrati che corrispondano ai poligoni dell’area mascherata. Quando disabilitato, puoi impostare tu stesso il numero di edge loop con lo slider edge loop.

----

##### Extract
* `Extract` - Crea la geometria estratta.
* `Closing action` - Come deve comportarsi l’estrazione. “None” duplica i poligoni mascherati in una nuova forma. “Fill” fa lo stesso e cerca di chiudere la superficie posteriore. “Shell” estrude della quantità impostata in “thickness” ed è l’impostazione predefinita.

::: tip

Se l’anteprima è in modalità “Extract” con “X-ray” abilitato, cliccare il pulsante Extract può essere inizialmente confuso. Poiché il menu è attivo, cercherà di mostrare un’anteprima di un’estrazione sulla nuova forma e metterà in x-ray la superficie originale. Tuttavia, poiché non hai maschera sulla nuova superficie, non può mostrare l’anteprima dell’estrazione e Nomad ti avviserà con “Nothing to Extract!”.

È normale, chiudi il menu delle impostazioni Mask per vedere la nuova forma e l’originale, e seleziona di nuovo la superficie originale se devi cancellare la maschera o disegnarne di nuove.
:::

##### Split
* `Split` - Estrarrà sia le regioni mascherate CHE quelle non mascherate in nuove forme. 
* `Closing action (masked)` - Come deve comportarsi l’estrazione della parte mascherata. “None” duplica i poligoni mascherati in una nuova forma. “Fill” fa lo stesso e cerca di chiudere la superficie posteriore. “Shell” estrude della quantità impostata in “thickness” ed è l’impostazione predefinita.
* `Closing action (unmasked)` - Come deve comportarsi l’estrazione della parte non mascherata. “None” duplica i poligoni mascherati in una nuova forma. “Fill” fa lo stesso e cerca di chiudere la superficie posteriore. “Shell” estrude della quantità impostata in “thickness” ed è l’impostazione predefinita.
* `Sync border` - Garantisce che il bordo tra le forme estratte mascherate e non mascherate rimanga vicino. Quando disabilitato, poiché l’operazione shell estruderà ogni faccia lungo la sua normale, può formarsi uno spazio tra le forme.

##### Carve
* `Carve` - In modalità predefinita, si comporta come se avessi tagliato nella superficie della quantità “thickness”, come tagliare una sezione di buccia d’arancia. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Questo strumento è per lo più simile allo [strumento Mask](#mask), la differenza principale è che non usi lo stroke per dipingere la maschera, ma usi i [Selection Controls](#selection-controls).

La sub mode è `Unmask` e cancellerà la maschera usando i controlli di selezione.

Selection Mask condivide le stesse impostazioni di strumento di `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Applica colore e proprietà del materiale. Per saperne di più sui materiali puoi visitare la sezione [Painting](painting.md).

La sub mode è `Erase` e rimuoverà la pittura.

#### Impostazioni Paint
* `Layer fitering` - Funziona come il blocco alfa del livello in Photoshop o Procreate. Se stai dipingendo su un livello, quando è abilitato puoi modificare solo dove la pittura esiste già; le aree non dipinte saranno protette.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Sfuma colore e proprietà del materiale. Il menu delle impostazioni Smudge contiene uno slider `Quality`, valori più bassi significano pennellate più veloci.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Appiattisce l’area proiettando i punti sul piano medio.

La sub mode è `Fill` e definirà un piano impostato dal punto più alto, tendendo a tirare i punti verso l’alto.

#### Impostazioni Flatten

* `Lock plane direction` - Usa la direzione del piano calcolata al primo clic. Per impostazione predefinita è disabilitato.
* `Lock plane origin`- Usa il primo clic come centro del piano. Per impostazione predefinita è disabilitato.

Quando uno o entrambi sono disabilitati, il flatten può essere gradualmente approfondito o l’angolo del piano modificato usando pennellate lunghe che si muovono su diverse profondità e curvature. Questo, insieme alle opzioni di campionamento dell’area del menu Brush, può offrire un controllo molto preciso.

::: tip
Quando lavori in aree ad alta curvatura, ad es. cercando di appiattire le guance ma lo strumento continua a influenzare i lati del naso, prova a creare una maschera per proteggere le aree che il pennello Flatten non dovrebbe toccare.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Rende i punti complanari proiettandoli sul piano medio, ma con meno accumulo rispetto al pennello Flatten. Questo crea superfici pulite con spigoli netti. Pennellate rapide spingeranno e tireranno di più sulla superficie, pennellate più lente che partono da aree già planari e si espandono manterranno meglio il piano.

La sub mode è `Fill` e definirà un piano impostato dal punto più alto, tendendo a tirare i punti verso l’alto.

Planar è in realtà lo stesso strumento di `Flatten`, ma con `Lock plane direction` abilitato, il che significa che tenderà a creare superfici più stabili e dure, mentre Flatten può essere più scultoreo e usato per creare aree semi-piatte.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Gli strumenti Crease possono essere utili per scolpire piccoli tagli o incisioni.

La sub mode è `Invert` e creerà una cresta rialzata.

#### Impostazioni Crease

* `Pinch factor` - Quanto tirare lateralmente i vertici verso la pennellata. Se pinch è a 1 e offset a 0, la superficie non avrà cambiamenti di profondità, solo cambiamenti di topologia, tirando gli edge verso la pennellata.
* `Offset factor` - Quanto spingere/tirare i vertici in profondità. Se pinch è a 0 e offset a 1, verranno create incisioni profonde o rigonfiamenti rialzati, ma appariranno frastagliati perché non viene tirata abbastanza geometria verso l’incisione per definire accuratamente i lati o il fondo.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Questo strumento può essere usato per affilare i bordi.

La sub mode è `Invert` e allontanerà i vertici tra loro.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
Lo strumento Trim funziona rimuovendo una porzione della mesh e offre opzioni su come elaborare il vuoto lasciato. Usa i [Selection controls](#selection-controls) per definire il taglio.

::: tip
Poiché questo strumento proietta dalla camera, riceverai un avviso se la camera è in modalità prospettica.

In modalità ortografica il taglio effettuato attraverso la mesh è parallelo alla vista, che è ciò che di solito ci si aspetta. Quando viene fatto con una camera prospettica, il taglio apparirà diverso sul lato lontano dell’oggetto rispetto al lato vicino.
:::

#### Impostazioni Trim

* `Stroke painting` - Se la pittura è abilitata nel menu Paint, la regione chiusa verrà riempita con il colore attualmente selezionato.
* `Boolean` - riempie il foro del trim usando una regione di quad. La regione riempita sarà piatta.
* `Legacy` - riempie il foro del trim con una regione triangolata. La regione riempita sarà piatta.
* `Fill` - riempie il foro con una regione triangolata. La regione riempita sarà una superficie curva, come il film di una bolla di sapone.
* `None` - non riempie il foro.
* `Boolean Detail Shape` - La dimensione approssimativa dei quad e triangoli usati sul lato “shape” del trim.
* `Boolean Detail Hole` - La dimensione approssimativa dei triangoli o poligoni usati sul foro riempito del trim. 
* `Legacy Detail` - La dimensione approssimativa dei triangoli usati sul trim.
* `Legacy Hole smoothing` - Quanto i triangoli vengono rilassati nell’area riempita.
* `Legacy Threshold espilon` - Un valore che può essere regolato per migliorare l’algoritmo di riempimento foro legacy.
* `Fill Detail` - La dimensione approssimativa dei triangoli usati sul trim.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
Simile allo strumento [Trim](#trim), tranne per il fatto che mentre Trim scarta la selezione, Split manterrà la selezione come nuovo oggetto.

#### Impostazioni Split

* `Stroke painting` - Se la pittura è abilitata nel menu Paint, la regione chiusa verrà riempita con il colore attualmente selezionato.
* `Boolean` - riempie il foro dello split usando una regione di quad. Le regioni riempite saranno piatte.
* `Legacy` - riempie il foro dello split con una regione triangolata. Le regioni riempite saranno piatte.
* `Fill` - riempie i fori con una regione triangolata. Le regioni riempite saranno superfici curve, come il film di una bolla di sapone.
* `None` - non riempie i fori.
* `Boolean Detail Shape` - La dimensione approssimativa dei quad e triangoli usati sul lato “shape” dello split.
* `Boolean Detail Hole` - La dimensione approssimativa dei triangoli o poligoni usati sul foro riempito dello split. 
* `Legacy Detail` - La dimensione approssimativa dei triangoli usati sullo split.
* `Legacy Hole smoothing` - Quanto i triangoli vengono rilassati nell’area riempita.
* `Legacy Threshold espilon` - Un valore che può essere regolato per migliorare l’algoritmo di riempimento foro legacy.
* `Fill Detail` - La dimensione approssimativa dei triangoli usati sullo split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
Lo strumento Project assomiglia allo strumento [Trim](#trim), ma non elimina né crea geometria, sposta solo i vertici per conformarsi alla selezione.

![](/videos/tool_project.mp4)

::: tip
Se usi Project mentre sei in un layer, puoi sfumare tra la forma originale e quella proiettata con lo slider del layer.
:::

### ![](/icons/tool_layer.webp) Layer
Alza la superficie ma limita l’altezza.

Se tieni la penna abbassata e continui a passare su un’area, Layer alzerà fino a una certa altezza e non andrà oltre, a differenza di altri strumenti che continueranno ad accumulare altezza.

Nota che per impostazione predefinita il limite è impostato solo per pennellata! Se inizi una nuova pennellata, costruirà dalla nuova altezza della superficie.

Per impostare un’altezza massima costante su molte pennellate, usa lo strumento Layer con il sistema di [Layers](layers.md) di Nomad.

Crea un layer e usa questo strumento. L’altezza massima è ora impostata dal layer, quindi puoi applicare molte pennellate e l’altezza sarà sempre la stessa.

`Sub` userà una profondità minima, creando scanalature.

#### Impostazioni Layer

* `Use layer data` - Quando attivo, e quando un layer è selezionato, usa i dati del layer per impostare l’altezza massima.
* `Inflate`- Quando attivo regola la direzione in cui lavora Layer per ottenere risultati più morbidi.
* `Relax (Normal)` - La quantità di levigatura applicata alle normali.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Sposta i vertici lungo le proprie normali. `Sub` sposterà i vertici lungo la normale invertita.

#### Impostazioni Inflate
* `Relax (Normal)` - La quantità di levigatura applicata alle normali.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Sposta o “spalma” i punti nella direzione della pennellata.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Clicca e trascina per sollevare un’area della scultura con la forma dell’Alpha selezionata.

Questo è semplicemente lo [strumento Brush](#brush) con il tipo di stroke impostato su `Lock + radius`. 

`Sub` spingerà lo stamp verso l’interno invece che tirarlo fuori dalla superficie.

::: tip
Stamp di solito funziona meglio con geometria ad alta risoluzione. Se cerchi online “wrinkles alpha”, “pores alpha”, “scales alpha” ecc, queste texture alpha e Stamp possono essere un ottimo modo per aggiungere dettagli organici a una scultura di personaggio.

Le due modalità di stroke sono utili per cose diverse. 

* `Lock + radius` ha un’altezza *fissa*, trascinare regola la larghezza e la rotazione dello stamp. Buono per texture della pelle dove devono avere la stessa profondità/altezza, ma rotazioni e scale diverse per nascondere pattern ripetuti.
* `Lock + intensity` ha una larghezza *fissa*, trascinare regola la rotazione e l’altezza dello stamp. Buono per rivetti, dove devono avere tutti la stessa dimensione, ma rotazioni e altezze diverse. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Questo strumento può resettare i layer localmente, hai bisogno di un layer attivo altrimenti non succederà nulla.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Crea un tubo disegnando una curva. 
![](/images/tool_tube_new.webp)

Una volta creato il tubo, il path può essere modificato nello spazio 3D usando controlli simili ai normali strumenti di [Shape editing](#shape-editing) e di editing delle curve. 

![](/videos/tool_tube.mp4)

#### Toolbar sinistra Tube

![](/images/tool_tube_left_toolbar.webp)

La toolbar di sinistra ha le seguenti opzioni:

* `Sync` - Se il tubo corrente è instanziato e ci sono nodi figli del tubo che differiscono tra le istanze, questo li risincronizzerà.
* `Snap` - Quando attivo, le modalità curve e path si agganceranno ad altri oggetti mentre disegni. Quando inattivo, il primo punto si aggancerà, poi il resto del tubo verrà disegnato a quella profondità. Ha un piccolo menu a comparsa:
    * `Offset` - Imposta la profondità dello snap; 0% farà sì che il centro della sezione del tubo si agganci alla superficie, valori positivi lo solleveranno dalla superficie, valori negativi lo abbasseranno.
* `Curve` - Disegna liberamente un tubo. Ha un piccolo menu a comparsa:
    * `Auto-validate` - Creerà il tubo non appena la pennellata è completa. Quando disabilitato, un cerchio verde sarà visibile accanto al path della curva, premilo per validare o usa il link `Reset` che appare in questo menu per rimuovere il path.
    * `Closed` - rende il tubo un loop.
    * `Screen` - Disponibile solo quando Auto-validate è disabilitato. Quando attivo, il path è “fissato” allo schermo, permettendoti di muovere la vista e l’oggetto mentre il path rimane in posizione. Quando inattivo, il path fa parte della scena 3D e si muoverà con la camera e gli oggetti.
    * `Accuracy` - Quanti punti di curva verranno usati per convertire il path disegnato in un tubo. 0% userà il numero minimo di punti ma perderà piccole variazioni di curvatura. 100% sarà molto accurato e userà molti punti.
* `Path` - Crea un tubo cliccando per definire i punti della curva. Tocca il cerchio verde per validare il path. Ha un piccolo menu a comparsa:
    * `B-spline` - Un metodo alternativo di disegno curve in cui i punti di curva di solito non si trovano direttamente sulla curva, ma possono produrre risultati più morbidi del metodo predefinito.
    * `Closed` - rende il tubo un loop
    * `Screen` - Quando attivo, il path è “fissato” allo schermo, permettendoti di muovere la vista e l’oggetto mentre il path rimane in posizione. Quando inattivo, il path fa parte della scena 3D e si muoverà con la camera e gli oggetti.

##### Toolbar superiore Tube
![](/images/tool_tube_toolbar.webp)
Quando un tubo è selezionato, una toolbar apparirà nella parte superiore della viewport con controlli extra. Clicca il titolo della toolbar per comprimerla/espanderla e clicca la freccia in alto a destra per spostarla in alto o in basso nella viewport.

* `Validate` - converte il tubo in poligoni regolari così da poter essere scolpito.
* `Edit` - mostra i punti della curva così da poterli manipolare
* `Mirror` - aggiunge un mirror repeater come genitore di questa curva
* `Snap` - aggancia i punti della curva a superfici vicine
* `Closed` - unisce l’inizio e la fine della curva per formare un loop
* `B-spline` - Alterna tra interpolazione Catmull-rom e B-spline.
* `Cap` - Passa ciclicamente tra cappucci su entrambe le estremità del tubo, solo all’inizio o alla fine, o nessun cappuccio.
* `Hole` - Aggiunge spessore al tubo, convertendolo in un tubo cavo. Passa ciclicamente tra avere un foro a entrambe le estremità, solo alla fine o nessun foro. 
* `Radius` - Passa ciclicamente tra raggio uniforme, raggio all’inizio e alla fine o raggio per punto di curva. Questi vengono modificati con maniglie arancioni sulla curva.
* `Twist` - Passa ciclicamente tra nessuna torsione, torsione uniforme, torsione all’inizio e alla fine o torsione per punto di curva. Questi vengono modificati con maniglie rosa sulla curva.
* `Profile` - Passa ciclicamente tra nessun profilo (quindi profilo circolare), profilo uniforme, profilo all’inizio e alla fine o profilo per punto.
* `Profile edit` - Mostra un editor di profilo. Funziona in modo simile agli strumenti di [Shape editing](#shape-editing), può salvare e caricare preset di profilo e ha un toggle per permetterti di modificare il profilo nello spazio 3D.
* `Spiral` - Attiva un menu per aggiungere una torsione a spirale al tubo. Questo menu ha opzioni per `Twist Angle`, `Offset`, `Scale` e `Angle offset`.
* `X Divisions` - il numero di divisioni attorno al tubo, 4 divisioni creeranno ad esempio un tubo quadrato. 
* `Constant density` - quando attivo, manterrà i poligoni quadrati. Quando disabilitato, ti permetterà di impostare le `Y divisions` lungo la lunghezza del tubo.
* `...` - Menu impostazioni Tube.

#### Toggle eliminazione punti curva

![](/images/tool_tube_delete_toggle.webp)

Sotto la toolbar c’è un toggle per l’eliminazione dei punti curva. Quando trascini un punto curva vicino a un altro, diventerà rosso, indicando che se lo rilasci il punto verrà eliminato. Se stai facendo piccole modifiche e non vuoi eliminare punti, questo pulsante disabiliterà il comportamento di eliminazione.

#### Impostazioni Tube
* `Primitive` - pulsanti che permettono di abilitare/disabilitare le UV o di validare il tubo.
* `Post subdivision` - scorciatoia per impostare il livello di multiresolution prima della validazione.
* `Linear subdivision` - scorciatoia per impostare il livello di subdivision lineare prima della validazione. 
* `Division X` - come X Divisions nella toolbar.
* `Division Y` - come Y Divisions nella toolbar.
* `Curve (Repeater)` - converte il tubo in un [Curve Repeater](scene.md#curve)

::: tip
Divisioni a 4 e Post subdivision a 3 creeranno tubi con estremità arrotondate lisce, buoni per vermi, serpenti, parti del corpo.
:::


### ![](/icons/tool_lathe.webp) Lathe
Crea una superficie di rivoluzione disegnando una curva.

Questo strumento è ottimo per forme come vasi, calici.

![](/videos/tool_lathe.mp4)

#### Toolbar sinistra Lathe

![](/images/tool_lathe_left_toolbar.webp)

La toolbar di sinistra ha le seguenti opzioni:

* `Sync` - Se il lathe corrente è instanziato e ci sono nodi figli del lathe che differiscono tra le istanze, questo li risincronizzerà.
* `Fixed` - Quando abilitato, il centro del lathe è fisso e mostrato sullo schermo. Questa linea centrale ha punti di modifica che possono essere regolati. Quando disabilitato, il centro del lathe si aggiornerà dinamicamente per corrispondere all’inizio e alla fine della curva disegnata.
* `Curve` - Disegna il profilo del lathe in un’unica pennellata. Ha un piccolo menu a comparsa:
    * `Auto-validate` - Quando abilitato, il lathe verrà creato quando la penna viene sollevata dallo schermo. Quando disabilitato, un cerchio verde accanto alla curva può essere premuto per creare il lathe. La curva può essere eliminata con il pulsante `Reset`.
    * `Closed` - unisce l’inizio e la fine della curva per formare un loop
    * `Screen` - Disponibile solo quando Auto-validate è disabilitato. Quando attivo, il path è “fissato” allo schermo, permettendoti di muovere la vista e l’oggetto mentre il path rimane in posizione. Quando inattivo, il path fa parte della scena 3D e si muoverà con la camera e gli oggetti.
    * `Accuracy` - Quanti punti di curva verranno usati per convertire il path disegnato in un tubo. 0% userà il numero minimo di punti ma perderà piccole variazioni di curvatura. 100% sarà molto accurato e userà molti punti.
* `Path` - Crea un lathe cliccando per definire i punti della curva. Tocca il cerchio verde per validare il path. Ha un piccolo menu a comparsa:
    * `B-spline` - Un metodo alternativo di disegno curve in cui i punti di curva di solito non si trovano direttamente sulla curva, ma possono produrre risultati più morbidi del metodo predefinito.
    * `Closed` - rende il tubo un loop
    * `Screen` - Quando attivo, il path è “fissato” allo schermo, permettendoti di muovere la vista e l’oggetto mentre il path rimane in posizione. Quando inattivo, il path fa parte della scena 3D e si muoverà con la camera e gli oggetti.

#### Toolbar superiore Lathe
![](/images/tool_lathe_top_toolbar.webp)

Quando un lathe è selezionato, una toolbar apparirà nella parte superiore della viewport con controlli extra. Clicca il titolo della toolbar per comprimerla/espanderla e clicca la freccia in alto a destra per spostarla in alto o in basso nella viewport.

* `Validate` - converte il lathe in poligoni regolari così da poter essere scolpito.
* `Edit` - mostra i punti della curva così da poterli manipolare
* `Mirror` - aggiunge un mirror repeater come genitore di questo lathe
* `Snap` - aggancia i punti della curva a superfici vicine
* `Stable` - Quando abilitato, il profilo della curva verrà parentato alla linea centrale del lathe. Quando disabilitato, la linea centrale può essere modificata e non muoverà la curva, permettendo forme più complesse.
* `Focus` - Ruoterà la vista per vedere il profilo della curva perfettamente piatto rispetto alla camera.
* `Closed` - unisce l’inizio e la fine della curva per formare un loop
* `Cap` - Se Closed è disabilitato, passa ciclicamente tra cappucci su entrambe le estremità del tubo, solo all’inizio o alla fine, o nessun cappuccio.
* `Hole` - Aggiunge spessore al lathe, convertendolo in un tubo cavo. Passa ciclicamente tra avere un foro a entrambe le estremità, solo alla fine o nessun foro. 
* `B-spline` - Alterna tra interpolazione Catmull-rom e B-spline.
* `X Divisions` - il numero di divisioni attorno al tulathebe, 4 divisioni creeranno ad esempio un profilo quadrato. 
* `Constant density` - quando attivo, manterrà i poligoni quadrati. Quando disabilitato, ti permetterà di impostare le `Y divisions` lungo la lunghezza del tubo.
* `...` - Menu impostazioni Lathe.

#### Impostazioni Lathe
* `Primitive` - pulsanti che permettono di abilitare/disabilitare le UV o di validare il tubo.
* `Post subdivision` - scorciatoia per impostare il livello di multiresolution prima della validazione.
* `Linear subdivision` - scorciatoia per impostare il livello di subdivision lineare prima della validazione. 
* `Division X` - come X Divisions nella toolbar.
* `Division Y` - come Y Divisions nella toolbar.
* `Curve (Repeater)` - converte il profilo della curva in un [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
Posiziona un oggetto sulla superficie di un altro. Nell’uso è simile allo strumento Stamp, ma per forme 3D complete.

Se selezioni una primitiva dalla toolbar di sinistra, un clic-trascina su qualsiasi superficie posizionerà una primitiva dove clicchi, il trascinamento ne imposterà la dimensione. Una volta terminato il trascinamento, Insert passerà alla modalità [Transform](#transform).

In modalità Instance, trascinare creerà e farà scorrere una nuova istanza sulla superficie. La dimensione verrà duplicata dal primo oggetto, in questo modo puoi posizionare molte istanze della stessa dimensione di un oggetto su altre superfici.

Non devi inserire solo primitive! Seleziona *qualsiasi* forma nell’outliner, se Insert è in modalità Instance o Clone, puoi trascinare copie dell’oggetto selezionato su qualsiasi altra superficie.

Se un oggetto ha un pivot personalizzato, verrà usato come punto di ancoraggio. Vedi il video sotto.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Muovi/Ruota/Scala un modello direttamente con 1 o 2 dita, di solito sulla superficie di un altro oggetto.

Lo strumento è controllato dalla toolbar di sinistra e ha 5 pulsanti:

* `Snap` - aggancia il modello ad altre superfici
* `Group` - Se l’oggetto selezionato ha una combinazione di oggetti e istanze, questo ti permette di determinare il comportamento dello strumento.
* `Move` - Trascinamento con un dito muoverà l’oggetto. Quando Snap è attivo, questo farà scorrere l’oggetto lungo la superficie sotto il dito.
* `Rotate` - Trascinamento con un dito ruoterà l’oggetto. Quando Snap è attivo, ruoterà attorno alla normale della superficie sotto il dito.
* `Scale` - Trascinamento con un dito scalerà l’oggetto.

Transform può essere usato per operare rapidamente 2 di queste modalità usando 2 dita:

* Trascina un oggetto per posizionarlo. Smetti di muovere il primo dito, ma non sollevarlo dallo schermo.
* Tocca il secondo dito sullo schermo mentre tieni il primo dito abbassato. Quando il secondo dito viene trascinato, l’oggetto verrà scalato.
* Solleva il secondo dito e continua a trascinare il primo dito, l’oggetto sarà di nuovo in modalità Move.

Puoi anche cambiare la seconda modalità con un tap del secondo dito:

* Trascina l’oggetto per posizionarlo, smetti di muoverlo ma non sollevare il dito dallo schermo.
* Tocca con il secondo dito mentre tieni il primo dito abbassato
* Lo strumento viene scambiato in modalità Rotate. Trascina il primo dito per impostare la rotazione.
* Tocca di nuovo con il secondo dito, lo strumento torna in modalità Move.

Questo offre un flusso di lavoro veloce per clonare oggetti su un altro, ad es. rocce su un paesaggio. Nota che il pulsante Clone è anche nella toolbar di sinistra per un facile accesso:

* Usa lo strumento Transform per spostare una roccia in posizione.
* Rilascia, premi il pulsante Clone
* Sposta questa roccia, ruota/scala come necessario
* Rilascia, premi il pulsante Clone
* Sposta questa roccia, ripeti.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Questo strumento ti permette di muovere, ruotare e scalare oggetti e modificare i pivot degli oggetti.

L’handle nella viewport ha le seguenti caratteristiche:

* `Move` - Trascina sulla linea+freccia per muovere su X/Y/Z. Trascina sul punto pesca al centro del gizmo per traslare liberamente nello spazio schermo. Clicca sui quadrati rosso, verde, blu per traslare sui piani X/Y/Z.
* `Rotate` - Trascina sui cerchi rosso/verde/blu per ruotare su X/Y/Z. Trascina la sfera all’interno dei cerchi per ruotare liberamente.
* `Scale`- Trascina sui punti esterni rosso/verde/blu per scalare su X/Y/Z. Trascina sui coni esterni rosso/verde/blu per scalare sui piani X/Y/Z. Trascina sul cerchio esterno pesca per scalare uniformemente.

![](/images/tool_gizmo.webp)

#### Nodi e vertici 

Ogni oggetto in Nomad è composto da un nodo e da vertici:

* `Node` - Il “manico” dell’oggetto, che memorizza traslazione, rotazione, scala, chiamata matrice di trasformazione.
* `Vertices` - I punti che definiscono la superficie di un oggetto, memorizzano posizione e informazioni di pittura.

Se hai un semplice box composto da 8 vertici, potresti traslarlo modificando la sua matrice di trasformazione o modificando le posizioni dei vertici. Quando scolpisci di solito vuoi modificare i vertici, quando muovi oggetti con il gizmo di solito vuoi modificare il nodo. Nomad ti permette di fare entrambe le cose. 

#### Toolbar menu sinistro

La toolbar a sinistra controlla se il gizmo lavorerà sul nodo o sui vertici, oltre ad altre funzioni:

* `Clone` - Crea una copia indipendente dell’oggetto corrente, che può essere trascinata via con il gizmo.
* `Instance` - Crea una copia istanza dell’oggetto corrente. Gli oggetti sono collegati, quindi le modifiche di scultura su un oggetto appariranno su tutti gli oggetti instanziati.
* `Group/Object/Vertex/Auto` - Imposta se il gizmo influenzerà il nodo o i vertici di un oggetto. La modalità predefinita “auto” tenterà la scelta migliore. Se ci sono diversi oggetti parentati insieme in una gerarchia, “Object” muoverà solo l’oggetto corrente, gli oggetti figli rimarranno fermi. Il gizmo può anche tenere conto di maschere e simmetria.
* `Pin` - Per impostazione predefinita il gizmo si sposterà sul pivot dell’oggetto selezionato. Quando Pin è abilitato, il gizmo rimarrà dove si trova attualmente.
* `Align` - Alterna il pivot allineato con l’oggetto corrente o allineato con il mondo.
* `Snap rotation` - Abilita la rotazione a scatti, il valore di snap è mostrato e può essere modificato quando lo snap è attivo.
* `Snap translation` - Abilita la traslazione a scatti, il valore di snap è mostrato e può essere modificato quando lo snap è attivo.
* `Pivot` - Quando abilitato, il gizmo può essere mosso e ruotato senza muovere l’oggetto. Ha un menu extra spiegato sotto.

#### Pivot
Quando la modalità Pivot è attiva, viene mostrato un menu per permettere rapide modifiche al pivot:

**Reset** 
* `Center` - Sposta il pivot al centro dell’oggetto
* `Bottom` - Sposta il pivot alla base dell’oggetto
* `Align` - Reimposta le rotazioni per essere allineate al mondo.
* `Mask` - Sposta il pivot al centro della regione non mascherata.

**On Tap**
* `None` - non fare nulla quando l’oggetto viene toccato
* `Normal` - Sposta e ruota il pivot per allinearlo al punto della superficie toccato
* `First` - Sposta (ma non ruota) il pivot dove la superficie è stata toccata
* `Medial` - Sposta il pivot al centro dell’oggetto, sotto il punto della superficie toccato.

#### Impostazioni Gizmo

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Sposta l’oggetto in modo che il suo pivot sia al centro della scena, chiamato origine.
* ![](/icons/bake.webp)  `Bake` - Congela l’oggetto dove si trova attualmente e imposta i valori di traslazione/rotazione a 0, scala a 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Fa sì che i valori della matrice corrispondano a dove si trova l’handle del gizmo nel mondo.
* ![](/icons/reset.webp) `Reset` - Una scorciatoia che imposta i valori di traslazione a 0, rotazione a 0, scala a 1, muovendo e ruotando l’oggetto.

::: tip Bake vs bake to pivot
Crea un box, seleziona lo strumento Gizmo, apri e fissa il menu impostazioni. Per impostazione predefinita traslazione e rotazione sono 0, scala è 1.

Abilita la modalità Pivot, sposta l’handle su un lato, disabilita la modalità Pivot. Il pivot è cambiato, ma nota che i valori di traslazione sono ancora 0. 

Se vuoi vedere dove si trova *davvero* il pivot, clicca `Bake Pivot`. Ora i valori di traslazione si aggiornano. Nota che il box non si muove durante questa operazione, né in modalità Pivot.

Muovi e ruota il box da qualche parte, poi tocca `Move Origin`. Sposta l’oggetto in modo che il suo pivot sia al centro del mondo, ma lascia invariata la rotazione.

Clicca `Reset` e anche la rotazione verrà impostata a 0.

Muovi e ruota di nuovo il box, questa volta clicca `Bake`. Il pivot rimane dove si trova, il box rimane dove si trova, ma i valori di traslazione e rotazione vengono impostati a 0.

Esercitati un po’! Capisci che i valori del pivot sono nascosti, Nomad se ne occupa per te, ma se hai bisogno di impostare il pivot in posizioni reali nello spazio, Bake Pivot lo farà per te.

:::

* `Translation` - i valori di traslazione X, Y, Z
* `Rotation` - i valori di rotazione X, Y, Z
* `Scale` - La scala uniforme se abilitata, o la scala X, Y, Z se disabilitata.
* `Uniform scale` - Alterna la possibilità di scalare uniformemente o indipendentemente su ciascun asse

-----

* `Compact` - alterna il layout del gizmo per mettere le maniglie extra all’esterno o all’interno della sfera di rotazione
* `Widget size` - la dimensione del gizmo
* `Thickness` - lo spessore delle linee del gizmo
* `Opacity` - l’opacità del gizmo
* `Hide on interaction` - alterna se il gizmo deve essere temporaneamente nascosto durante il trascinamento

-----

* `Tangent roll threshold` - Controlla come si comporta l’interfaccia di rotazione quando trascini sulle maniglie circolari per ruotare su X/Y/Z. Se questo valore è 0, la rotazione funziona come una manopola, trascina il gizmo in cerchio. Se questo valore è 90, la rotazione funziona come tirare la cordicella di uno yo-yo; trascina in linea retta verso o lontano dal punto in cui hai cliccato. Valori tra 0 e 90 faranno una combinazione di entrambi; sotto il valore sarà movimento lineare, sopra il valore sarà movimento circolare.
* `Numerical input` - quando abilitato, un singolo tap sul gizmo farà apparire una finestra per inserire un valore esatto per l’asse del widget toccato.

::: warning
Gli strumenti [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) e [Scale](#scale) usano la propria casella di simmetria!

Per impostazione predefinita questa simmetria è disattivata.
:::

A sinistra puoi muovere il pivot del gizmo, puoi vedere il video sotto in azione.
Questo è particolarmente utile per la rotazione, poiché non cambia nulla per la traslazione.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

I Facegroup ti permettono di organizzare il tuo oggetto in facce di colore diverso. Puoi usare questi gruppi in molti modi in Nomad:

* Un metodo di selezione rapido per le maschere
* Nascondere/mostrare sezioni del tuo oggetto
* Organizzare il tuo oggetto senza doverlo dividere in parti separate
* Definire regioni UV
* Guidare il quad remesher
* Controllo aggiuntivo per strumenti come Smooth.

#### Toolbar sinistra Facegroup

* `Patch ` - Mostra i facegroup disponibili come patch. Le patch non usate possono essere eliminate. Tocca una patch per rinominarla o cambiarne il colore. L’icona più ti permette di creare nuove patch.
* `Dot` - Dipingi sull’oggetto per definire facegroup. Quando “+ Face Group” è abilitato, ogni nuova pennellata creerà automaticamente un nuovo facegroup, utile per definire rapidamente regioni. Un tap riempirà la regione selezionata. Lo slider imposta il raggio del dot.
* `Relax` - Leviga i bordi dei facegroup. Molto utile per definire bordi puliti per il quad remeshing o per definire pannelli per modellazione hard surface. Gli slider controllano raggio e intensità dell’operazione Relax.
* `Shape selector` - Crea facegroup con forme invece che con un pennello, tramite `Lock+Radius`, `Lasso`, `Polygon`, `Rect` ed `Ellipse`. Vedi [Shape Selector](#shape-selector) per maggiori informazioni.
* `Auto-pick` - Quando abilitato, selezionerà la patch da cui inizia la pennellata e applicherà quella patch per il resto della pennellata. Molto utile per ripulire le regioni dei facegroup; se un facegroup si è esteso troppo, abilita Auto-pick, inizia una pennellata da dove la patch del facegroup è corretta e trascina fino al bordo per riassegnare la patch corretta.

### ![](/icons/tool_hide.webp) Hide
Nascondi o isola parti dell’oggetto. 

Le modalità principali sono controllate dal menu a sinistra:

* `Dot` - Pennella sull’oggetto per nasconderne parti.
* `Shape selector` - Nascondi con forme invece che con un pennello, tramite `Lasso`, `Polygon`, `Line`, `Rect` ed `Ellipse`. Vedi [Shape Selector](#shape-selector) per maggiori informazioni.
* `Show` - inverte l’operazione, quindi la modalità selezionata mostrerà invece di nascondere parti dell’oggetto.

Una toolbar apparirà nella parte superiore della viewport con controlli extra:

* `Clear` - Ripristina l’oggetto, tutte le parti nascoste verranno mostrate.
* `Invert` - Scambia le parti nascoste e visibili.
* `Facegroup` - Usa i facegroup per nascondere rapidamente sezioni, toccando un facegroup verrà nascosto l’intero facegroup.
* `Mask` - Se una maschera è attiva, toccando questo pulsante verrà nascosta la sezione mascherata.
* `Delete` - Elimina la parte nascosta dell’oggetto
* `Split` - Divide la parte nascosta dell’oggetto in una nuova forma.

### ![](/icons/tool_measure.webp) Measure
Trascina per misurare la distanza tra 2 punti.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Questo strumento convertirà l’oggetto selezionato in una topologia pulita di quad, con controlli per densità, flusso degli edge, simmetria. 

::: tip
Quad Remesher è sviluppato da [Exoside](https://exoside.com/) per iOS e desktop. 

Per iOS è un acquisto in-app all’interno di Nomad, un pagamento una tantum di 16 USD.

Per desktop, acquista una licenza da [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Puoi acquistarlo solo per Nomad desktop o una licenza incrociata per tutte le app desktop supportate.

Se possiedi già Quad Remesher per un’altra app desktop, puoi [acquistare un upgrade a tutte le piattaforme a costo ridotto.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher non è disponibile per Android. Android può usare il “Quad Remesh - Instant” open source gratuito disponibile sotto Topology -> Misc, ma tieni presente che il suo set di funzionalità è molto limitato.
:::

Quando questo strumento viene attivato per la prima volta, chiederà se vuoi abilitarlo come acquisto in-app. Una volta attivo, le barre degli strumenti sinistra e superiore saranno abilitate.

* `Dot` - Questo pennello imposterà la densità target. Un’intensità al 100% dipingerà in rosso, il che utilizzerà il doppio della densità di quad target in quelle regioni. Un’intensità allo 0% dipingerà in ciano, il che utilizzerà metà della densità di quad target in quelle regioni. Un’intensità al 50% dipingerà in grigio, il che utilizzerà la densità di quad target predefinita.
* `Smooth` - Uniforma le transizioni di densità rosso/grigio/ciano.
* `Curve` - Schizza curve sulla superficie dello sculpt, il quad remesher le userà come guide per il flusso degli edge. Tocca una curva per eliminarla.
* `Path` - Disegna percorsi sulla superficie dello sculpt, il quad remesher li userà come guide per il flusso degli edge. Tocca un percorso per eliminarlo. 
* `Rect` - Disegna rettangoli sulla superficie dello sculpt, il quad remesher li userà come guide per il flusso degli edge. Tocca un percorso per eliminarlo.
* `Ellipse` - Disegna ellissi sulla superficie dello sculpt, il quad remesher le userà come guide per il flusso degli edge. Tocca un percorso per eliminarlo.

#### Barra degli strumenti superiore del quad remesher
![](/images/tool_quadremesher_toolbar.webp)

Una barra degli strumenti apparirà nella parte superiore della viewport con controlli aggiuntivi:


* `<Count>` - Clicca qui per avviare il processo di quad remeshing, questo numero indica quale sarà il conteggio target dei quad.
* `Quads` - Imposta il conteggio target dei quad scorrendo a sinistra e a destra, oppure tocca per impostare un numero esatto. Nota che questo è più una guida che un numero fisso, i vari controlli del quad remesher spesso faranno sì che il risultato non corrisponda esattamente a questo target.
* `Half` - Una scorciatoia per impostare il conteggio target alla metà dell’attuale conteggio di poligoni.
* `Same` - Una scorciatoia per impostare il conteggio target all’attuale conteggio di poligoni.
* `Guides` - indica il numero totale di guide, oppure tocca per eliminare tutte le guide.
* `Density X` - tocca per rimuovere tutta la pittura di densità.
* `Density (painting)` - attiva/disattiva l’uso della pittura di densità.
* `Face Group` - attiva/disattiva l’uso dei facegroup per guidare il quad remesher.
* `Relax` - attiva/disattiva il rilassamento automatico dei bordi dei facegroup durante il quad remeshing. Se hai già rilassato/smussato i bordi dei facegroup, disabilita questa opzione.
* `Relax Slider` - Uno slider scorciatoia per rilassare i bordi dei facegroup.
* `Hard Edges` - attiva/disattiva il tentativo di mantenere gli edge duri.
* `Reproject Vertex` - attiva/disattiva la riproiezione del nuovo layout sulla mesh di input.
* `Symmetry` - Attiva/disattiva per ottenere un risultato simmetrico. Nota che la simmetria è sempre calcolata attorno all’asse x del mondo, quindi assicurati che il tuo modello sia all’origine se ti aspetti un risultato simmetrico.
* `...` - Menu delle impostazioni del quad remesher. 

#### Menu delle impostazioni del quad remesher

La maggior parte di queste impostazioni è disponibile nella barra degli strumenti superiore.

* `<Count>, Half, Same` - Uguale ai pulsanti Remesh, Half, Same nella barra degli strumenti superiore.
* `Target Quads` - Uguale al pulsante `Quads` nella barra degli strumenti superiore
* `Adaptive quad count` - attiva/disattiva l’uso di quad più piccoli nelle aree ad alta curvatura e quad più grandi nelle aree a bassa curvatura.
* `Adaptive size` - Imposta la quantità di adattività. Il 100% consentirà la massima dimensione adattiva, allo 0% i quad saranno uniformi.
* `Auto-Detect Hard Edges` - attiva/disattiva l’adattamento del layout di quad remesh per seguire meglio le superfici affilate.
* `Density (painting)` - Uguale al pulsante `Density (painting)` nella barra degli strumenti superiore
* `Reproject Vertex` - attiva/disattiva la riproiezione del nuovo layout sulla mesh di input.
* `Face Group` - Uguale al pulsante `Face Group` nella barra degli strumenti superiore
* `Relax Slider` - Uno slider scorciatoia per rilassare i bordi dei facegroup.

::: tip

Una ricetta per ottenere un buon quad remesh con artefatti minimi:

* Crea i facegroup della mesh per definire il tuo flusso ideale dei quad.
* Rilassa i facegroup per ottenere bordi dei facegroup morbidi.
* Decimate. Questo garantirà che tu non abbia facce sottili o distorte sul bordo dei facegroup. Nelle impostazioni di decimate assicurati che facegroup sia abilitato. Questo farà sì che i bordi dei triangoli seguano con precisione i bordi dei facegroup. 

Nelle opzioni del quad remesh assicurati che il relax sia disabilitato (dato che hai già rilassato la mesh) e dovresti ottenere buoni risultati.

:::

### ![](/icons/tool_select.webp) Select
Usa le modalità di forma per selezionare oggetti nella scena. `Unselect` rimuoverà oggetti dalla selezione.

### ![](/icons/tool_view.webp) View
Questo "strumento" non fa nulla in particolare, è semplicemente un modo per visualizzare il modello senza modificare la scena.


## Menu contestuale della toolbox

![](/images/tools_context_menu.webp)

Un clic destro o una pressione prolungata su uno strumento nella toolbox farà apparire un menu contestuale. Questo menu ha le seguenti opzioni:

* `Save` - salva qualsiasi modifica apportata allo strumento
* `Clone` - duplica lo strumento in una nuova scorciatoia
* `Last save` - ripristina la versione precedentemente salvata dello strumento
* `Icon` - cambia l’icona dello strumento
* `Reset` - reimposta lo strumento ai suoi valori predefiniti

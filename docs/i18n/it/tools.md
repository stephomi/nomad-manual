# ![](/icons/toolbox.webp) Strumenti {#tools}

![](/images/tools_menu.webp)

::: tip
Vai direttamente a [Strumenti](#tools-1) per la descrizione dei singoli strumenti.
:::

## Panoramica {#overview}

Gli strumenti si scelgono dalla `Casella strumenti` a destra e si controllano con i controlli dello strumento a sinistra. Altre impostazioni si trovano nel menu `Strumento`, nel menu in alto a destra.

Gli strumenti pennello hanno controlli per la dimensione e l'intensità. Gli strumenti di selezione hanno controlli per vari stili di selezione. In fondo ai controlli dello strumento trovi le scorciatoie per le operazioni più usate (Leviga, Maschera, Nascondi, Gruppo di facce, Gizmo, Colore, Alfa).

Nella casella strumenti di Nomad gli strumenti hanno un codice colore (disattiva `Strumenti colorati` nel menu [Interfaccia](interface.md) per etichette semplici):

* <span class=brush>**Strumenti pennello**</span> (Argilla, Pennello, Leviga, Livello, Gonfia, DelLayer, Quad Remesher)
* <span class=move>**Strumenti di spostamento**</span> (Sposta, Trascina, Elastico, Spingi)
* <span class=mask>**Strumento maschera**</span> (Maschera)
* <span class=paint>**Strumenti di pittura**</span> (Dipingi, Sfumino)
* <span class=flatten>**Strumenti di appiattimento**</span> (Appiattisci, Planare, Polish)
* <span class=pinch>**Strumenti di pizzico**</span> (Solco, Pizzica)
* <span class=stamp>**Strumenti timbro**</span> (Timbro, VDM)
* <span class=selection>**Strumenti basati sulla selezione**</span>, in cui prima si disegna una maschera 2d e poi avviene un'operazione (Rifila, Dividi, Proietta)
* <span class=creation>**Strumenti di creazione**</span> (Tubo, Lathe, Inserisci)
* <span class=transform>**Strumenti di trasformazione**</span> (Trasforma, Gizmo, Disponi, Reticolo)
* <span class=misc>**Strumenti vari**</span> (Gruppo di facce, Nascondi)
* <span class=view>**Strumenti di visualizzazione**</span> (Vista, Misura, Seleziona)



Molti di questi strumenti si possono personalizzare con comportamenti del pennello, pressione, texture diverse ecc. tramite il menu [Tratto](stroke.md). 


### Controlli del pennello {#brush-controls}

La barra degli strumenti a sinistra ha i cursori per raggio e intensità, seguiti dai controlli specifici della categoria di strumento, spiegati qui sotto.

![](/images/tool_left_panel.webp)

::: tip
Per molti strumenti il cursore dell'intensità può superare il 100%: vale la pena sperimentare!
:::

### Modalità Sub {#sub-mode}
Il pulsante subito sotto il cursore dell'intensità è il pulsante `Sub`. La sua etichetta e la sua funzione cambiano con ogni strumento, e quando lo premi attiva un comportamento alternativo, di solito opposto. Per esempio con [Dipingi](#paint) attiva la modalità Cancella, con [Solco](#crease) crea bordi in rilievo invece di solchi, ecc.

Di default funziona come un pulsante temporaneo: puoi tenerlo premuto per attivarlo momentaneamente e, quando lo rilasci, si disattiva. Se lo tocchi, la modalità Sub resta attiva in modo permanente.

### Scorciatoie {#shortcuts}
In fondo alla barra degli strumenti a sinistra ci sono le scorciatoie per [Leviga](#smooth), [Maschera](#mask), [Nascondi](#hide), [Gruppo di facce](#facegroup), [Gizmo](#gizmo), [Colore](painting.md#pbr-sliders), [Alfa](stroke.md#alpha). 

Di default funzionano tutte come pulsanti temporanei: puoi tenerle premute per attivarle momentaneamente e, quando le rilasci, si disattivano. Se tocchi una scorciatoia, la sua modalità resta attiva in modo permanente.

### Controlli di selezione {#selection-controls}

Gli strumenti [Maschera](#mask), [Dipingi](#paint), [Rifila](#trim), [Dividi](#split), [Proietta](#project), [Gruppo di facce](#facegroup), [Nascondi](#hide) e [Seleziona](#select) usano tutti controlli simili per selezionare zone della mesh.

![](/images/tools_shape_selector_panel.webp)

Tocca il pulsante della forma nella barra a sinistra (mostra la forma attuale, `Lazo` di default) per aprire un popup con le forme. Per gli strumenti che funzionano anche con un pennello (Maschera, Dipingi, Gruppo di facce, Nascondi), lo stesso popup contiene anche i tipi di tratto.

* `Vista` - Nessuna forma: lo strumento non fa nulla di particolare, come la modalità fotocamera.
* `Lazo` - Una forma disegnata a mano libera
* `Poligono` - Una forma chiusa definita da una combinazione di curve e/o linee rette. Vedi [Modifica delle forme](#shape-editing) più sotto per saperne di più.
* `Curva` - (solo Proietta) - Una curva a mano libera per la proiezione
* `Tracciato` - (solo Proietta) - Una curva definita da punti. Vedi [Modifica delle forme](#shape-editing) più sotto per saperne di più.
* `Linea` - Trascina una linea per definire un segmento piano. Di default agisce subito sulla mesh; cambia l'opzione `Modifica` se non vuoi questo comportamento (tieni premuta o scorri sull'icona della linea)
* `Banda` - Una striscia tra due guide parallele, con un gradiente al suo interno. `Estendi` mantiene il valore pieno oltre la guida più lontana invece di fermarsi alla banda, `Inverti` scambia la guida da cui parte il gradiente.
* `Rett.` -  Trascina una linea diagonale per definire gli angoli di un rettangolo. Tieni premuto o scorri per mostrare l'opzione `Modifica`, `Quadrato` per forzare un quadrato e `Centrato` perché il primo clic sia il centro del rettangolo.
* `Ellisse` - Trascina una linea diagonale per definire la dimensione di un'ellisse. Tieni premuto o scorri per mostrare l'opzione `Modifica`, `Cerchio` per forzare un cerchio e `Centrata` perché il primo clic sia il centro dell'ellisse.
* `Rifletti` - inverte la maschera della forma, o la direzione dello strumento Proietta.

La maggior parte degli strumenti ha un'opzione `Modifica` che decide cosa succede quando finisci di disegnare la forma:
* `Modifica: disattivata` - l'operazione avviene appena rilasci.
* `Modifica: attivata` - la forma resta modificabile. Accanto alla forma compare un pulsante verde che esegue l'operazione. Così puoi modificare la forma e sistemare la vista; quando sei pronto a usare la forma, premi il pulsante verde.
* `Modifica: tieni premuto` - l'operazione avviene al rilascio, a meno che tu non tenga premuto alla fine del tratto per continuare a modificare la forma.

### Modifica delle forme {#shape-editing}
La modifica dei poligoni e quella delle curve funzionano in modo simile:

* Per iniziare, trascina una linea per definire 2 punti, poi trascina dal centro della linea verso l'esterno per creare un poligono o una curva.
* Fai clic sui punti per passare da morbido a spigoloso e viceversa. 
* Fai clic e trascina sui tratti di curva o di linea per creare nuovi punti.
* Per eliminare un punto, trascinalo sul punto vicino finché non diventa rosso.
* L'icona del cestino nell'angolo dell'icona del poligono o del tracciato elimina la forma.

### Menu delle impostazioni {#settings-menu}

Molti strumenti hanno impostazioni aggiuntive che si trovano nel menu `Strumento`, nel menu in alto a destra. Il menu è disattivato (in grigio) per gli strumenti che non hanno impostazioni aggiuntive.

![](/images/tools_settings_menu.webp)

## Strumenti {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Argilla](#clay)    | ![](/icons/tool_brush.webp)   <br> [Pennello](#brush)  | ![](/icons/tool_move.webp)       <br> [Sposta](#move)            | ![](/icons/tool_drag.webp)      <br> [Trascina](#drag)       | ![](/icons/tool_elastic.webp)   <br> [Elastico](#elastic)    | ![](/icons/tool_smooth.webp)  <br> [Leviga](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Maschera](#mask)   | ![](/icons/tool_paint.webp)   <br> [Dipingi](#paint)   | ![](/icons/tool_smudge.webp)     <br> [Sfumino](#smudge)         | ![](/icons/tool_flatten.webp)   <br> [Appiattisci](#flatten) | ![](/icons/tool_planar.webp)    <br> [Planare](#planar)      | ![](/icons/tool_polish.webp)  <br> [Polish](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Solco](#crease)    | ![](/icons/tool_pinch.webp)   <br> [Pizzica](#pinch)   | ![](/icons/tool_trim.webp)       <br> [Rifila](#trim)            | ![](/icons/tool_split.webp)     <br> [Dividi](#split)        | ![](/icons/tool_project.webp)   <br> [Proietta](#project)    | ![](/icons/tool_layer.webp)   <br> [Livello](#layer)   |
| ![](/icons/tool_inflate.webp) <br> [Gonfia](#inflate)  | ![](/icons/tool_nudge.webp)   <br> [Spingi](#nudge)    | ![](/icons/tool_stamp.webp)      <br> [Timbro](#stamp)           | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [DelLayer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tubo](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Inserisci](#insert) | ![](/icons/tool_transform.webp)  <br> [Trasforma](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Gruppo di facce](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Nascondi](#hide)   |
| ![](/icons/tool_measure.webp) <br> [Misura](#measure)  | [Disponi](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Seleziona](#select)    | ![](/icons/tool_lattice.webp)   <br> [Reticolo](#lattice)    | ![](/icons/tool_view.webp)    <br> [Vista](#view)      |

------

### ![](/icons/tool_clay.webp) Argilla {#clay}
Lo strumento Argilla è utile per costruire la tua scultura aggiungendo materiale. `Sub` toglie materiale dalla scultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pennello {#brush}
Il pennello standard. `Sub` toglie materiale.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Sposta {#move}
La zona sotto il pennello resta attaccata al pennello, permettendo una deformazione elastica. La selezione viene mantenuta durante lo spostamento: se allontani il pennello e poi lo riporti al punto di partenza, non vedrai alcuna deformazione.

La modalità Sub è `Normale` e sposta la zona sotto il pennello lungo la normale della superficie.

Questo pennello va bene sia per deformazioni ampie sia per piccole deformazioni precise.

#### Impostazioni di Sposta {#move-settings}

* `Raggio (Sfondo)` - Quanto lontano dal bordo di un modello puoi trovarti e continuare a scolpire, utile quando lavori sulla silhouette di un oggetto. Deselezionalo per afferrare solo quando inizi sul modello.
* `Solo vertice dello stesso lato` - Ignora i vertici rivolti nella direzione opposta alla deformazione.
* `Direzione` - Usata dalla modalità Sub `Normale`, decide se un trascinamento spinge o tira la superficie:
    * `Auto` - Sceglie per te uno dei due metodi qui sotto, in base all'angolo della normale della superficie.
    * `Normale 3D` - Confronta la posizione del puntatore sullo schermo con la normale della superficie vista dalla fotocamera.
    * `XY` - Usa la posizione del puntatore sullo schermo (su/giù, sinistra/destra) per decidere se spingere o tirare.
    * `Soglia` - Con `Auto`, il limite d'angolo che decide quale metodo usare.
* `Velocità di rollio` - Puoi torcere la zona afferrata mentre la sposti: ruota due dita, ruota il corpo della penna, oppure tieni premuto un tasto modificatore (Alt, Ctrl, Shift o Cmd) mentre trascini con il mouse. C'è un cursore per ciascuno tra dita, penna e mouse; deselezionane uno per disattivare quell'input.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Trascina {#drag}
La zona sotto il pennello resta attaccata al pennello, permettendo una deformazione elastica. A differenza del pennello Sposta, la selezione viene aggiornata continuamente durante il tratto, quindi puoi creare oggetti lunghi, simili a serpenti, soprattutto con la topologia dinamica attiva.

La modalità Sub è `Normale` e sposta la zona sotto il pennello lungo la normale della superficie.

Questo pennello è adatto a cambiamenti di forma più liberi e gestuali.

#### Impostazioni di Trascina {#drag-settings}

Trascina ha le stesse impostazioni di [Sposta](#move-settings): `Raggio (Sfondo)`, `Solo vertice dello stesso lato`, `Direzione` e `Velocità di rollio`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastico {#elastic}
Afferra e tira la superficie come [Sposta](#move), ma con una deformazione elastica: invece di fermarsi al bordo del pennello, la trazione si attenua dolcemente con la distanza su tutto l'oggetto, un po' come quando tendi la gomma. Il raggio del pennello imposta l'ampiezza della trazione.

La modalità Sub è `Normale` e sposta la zona sotto il pennello lungo la normale della superficie.

Questo pennello è ideale per grandi cambiamenti di proporzioni, morbidi e che restano lisci.

#### Impostazioni di Elastico {#elastic-settings}

Elastico ha le stesse impostazioni di [Sposta](#move-settings), tranne `Solo vertice dello stesso lato`. `Raggio (Sfondo)` è disattivato di default.

### ![](/icons/tool_smooth.webp) Leviga {#smooth}
Leviga la zona facendo la media delle posizioni dei punti. Questo strumento dipende molto dalla densità dei poligoni.
Quindi, se hai molti poligoni, la levigatura sarà meno efficace.

La modalità Sub è `Rilassa`, che leviga solo la wireframe cercando di conservare i dettagli geometrici.

#### Impostazioni di Leviga {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Gruppo di facce {#smooth-facegroup}

* `Rilassa` - Leviga i bordi dei gruppi di facce. Usa un'intensità superiore al 100% per levigare i bordi rapidamente. `Auto` leviga solo se l'anteprima dei gruppi di facce è attiva, `No` disattiva, `Sì` attiva. 

##### Vertice {#vertex}
* `Mantieni volume` - Leviga senza restringere la superficie, così levigature ripetute non sgonfiano le tue forme. Il pulsante a ingranaggio accanto contiene i valori `Restringi` e `Gonfia` usati a questo scopo.
* `Mantieni bordi` - Sulle mesh con bordi aperti, per esempio un piano, gli angoli possono venire levigati. Attivando questa opzione i vertici sul bordo della mesh restano fermi.
* `Levigatura stabile` - Cerca di rendere la levigatura indipendente dalla topologia. Funziona meglio con una densità di topologia variabile e con un'intensità di levigatura alta.
* `Rilassa` - uguale alla modalità alternativa Rilassa nella barra degli strumenti a sinistra.

##### Pittura {#painting}
* `Levigatura schermo` - Usa questa opzione per una levigatura indipendente dalla topologia, anche con molti poligoni. `Auto`, `No` o `Sì`.
* `Campioni dello schermo` - La qualità della levigatura: valori più alti danno un risultato più liscio, ma più lento.

::: tip
Con densità di poligoni più alte può servire alzare l'intensità oltre il 100%. Valori molto alti (300%, 500%) funzionano bene anche come strumento di scultura, costringendo le zone sotto il pennello a diventare piatte e lisce in fretta, come colpire l'argilla con un mazzuolo!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maschera {#mask}
Questo strumento ti permette di mascherare i vertici. I vertici mascherati sono protetti dalla scultura e dalla pittura. 

La modalità Sub è `Togli masch.` e cancella la maschera dove è stata dipinta.

Come le selezioni nei programmi di pittura 2d, le maschere si possono dipingere con un pennello o creare con selezioni a forma (`Lazo`, `Rett.`, `Banda`...), sfocare o rendere più nitide. Scegli il pennello o la forma nel popup del tratto della barra a sinistra, vedi [Controlli di selezione](#selection-controls).

A differenza dei programmi di pittura 2d, si possono creare anche a partire dai gruppi di facce, e le maschere si possono usare per creare nuova geometria con operazioni di estrusione/estrazione. 

![](/videos/tool_mask1.mp4)

 In cima al viewport compare una barra degli strumenti con controlli aggiuntivi. 

![](/images/tool_mask_toolbar.webp)

Tocca il titolo della barra per espanderla/comprimerla, oppure tocca la freccia in alto a destra per spostarla in cima o in fondo all'interfaccia.

| Azione                                             | Descrizione                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Pulisci tutto      | Cancella la maschera su tutti gli oggetti. Quando anche altri oggetti sono mascherati, un pulsante `Cancella` in più cancella solo gli oggetti selezionati |
| ![](/icons/invert.webp)        Inverti            | Inverte la maschera                                                                        |
| ![](/icons/sharpen.webp)       Aumenta nitidezza  | Rende più netto il bordo della maschera                                                    |
| ![](/icons/blur.webp)          Sfoca              | Sfoca il bordo della maschera                                                              |
| ![](/icons/outline.webp)       Bordo              | Maschera il bordo aperto della mesh, come il contorno di un piano o il bordo di un buco    |
| ![](/icons/blur.webp)          Sfoca ->           | Trascina a destra per sfocare la maschera, a sinistra per renderla più netta               |
| ![](/icons/circle_plus.webp)   Espandi ->         | Trascina a destra per espandere la zona mascherata, a sinistra per restringerla            |
| ![](/icons/intensity.webp)     Potenzia ->        | Trascina a destra per rafforzare la maschera, a sinistra per attenuarla, senza cambiarne la forma |
| ![](/icons/dig.webp)           Cavità ->          | Ricostruisce la maschera dalla curvatura della superficie: trascina a destra perché restino dipingibili solo le cavità, a sinistra solo i rilievi |
| ![](/icons/culling.webp)       Frontale           | Attiva/disattiva per mascherare solo i vertici rivolti verso di te                         |
| ![](/icons/eye_open.webp)      Visibile           | Con le forme, attiva/disattiva per ignorare i vertici nascosti dietro altre superfici      |
|                                 Converti           | Converte la maschera in un gruppo di facce                                                 |
| ![](/icons/group_to_mask.webp) Tocco (gruppo di facce) | Se attivo, i gruppi di facce vengono mostrati e toccandone uno lo si maschera          |
|                                 Tocco (maschera)   | Se attivo, toccando un'"isola" di poligoni mascherati o non mascherati la si riempie interamente. |
| ![](/icons/connect.webp)       Collegata          | Se attivo, i tratti della maschera agiscono solo sulla topologia collegata.               |

##### Gesti rapidi della maschera {#mask-quick-gesture}
Puoi eseguire gesti in stile ZBrush tenendo premuto il pulsante della maschera rapida nella barra a sinistra:
| Azione  | Gesto (tieni premuta la scorciatoia in basso a sinistra) |
| :-----: | :--------------------------------: |
| Inverti | Tocca lo sfondo                    |
| Cancella | Trascina sullo sfondo             |
| Sfoca   | Tocca una zona mascherata          |
| Aumenta nitidezza | Tocca una zona non mascherata |


#### Impostazioni di Maschera {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Le impostazioni di Maschera servono soprattutto a creare geometria a partire dalla maschera. Le schede in alto scelgono l'operazione: [Estrai](#extract), [Dividi](#split-mask) o [Intaglia](#carve). Le opzioni sotto cambiano in base all'operazione.

* `Anteprima` - Mostra come apparirà la nuova geometria mentre regoli le impostazioni.
* `Raggi X` - Quali oggetti vengono mostrati ai raggi X durante l'anteprima: `Nessuno`, `Non selezionati`, `Selezionati` o `Tutti`.

##### Estrai {#extract}
* `Estrai` - Crea la geometria estratta come nuovo oggetto.
* `Azione di chiusura` - Come viene chiusa la forma estratta. `Nessuno` duplica i poligoni mascherati in una nuova forma e la lascia aperta. `Riempi` fa lo stesso, poi riempie e leviga il buco sul retro (non usarlo su superfici piatte). `Involucro` chiude la forma usando il valore `Altezza` ed è l'opzione predefinita.

::: tip

Se l'anteprima è attiva con i raggi X, premere il pulsante Estrai può confondere all'inizio. Siccome il menu è attivo, Nomad prova a mostrare l'anteprima di un'estrazione sulla nuova forma e mostra ai raggi X la superficie originale. Ma poiché la nuova superficie non ha alcuna maschera, l'anteprima non è possibile e Nomad ti avvisa con 'Niente da estrarre!'. 

È normale: chiudi il menu delle impostazioni della maschera per vedere la nuova forma e quella originale, e seleziona di nuovo la superficie originale se devi cancellare la maschera o disegnarne di nuove.
:::

##### Dividi {#split-mask}
* `Dividi` - Estrae sia la zona mascherata SIA quella non mascherata in nuove forme. 
* `Azione di chiusura` (mascherata) - Come viene chiusa la parte mascherata, con le stesse scelte `Nessuno`, `Riempi` e `Involucro` di Estrai.
* `Azione di chiusura` (non mascherata) - Come viene chiusa la parte non mascherata, con le stesse scelte.

##### Intaglia {#carve}
* `Intaglia` - Si comporta come se avessi rifilato la superficie per una profondità pari a `Altezza`, come quando tagli un pezzo di buccia d'arancia. `Altezza` non può essere 0.

##### Altezza {#thickness}
* `Altezza` - L'altezza della forma estratta. Il pulsante Più/Meno ti permette di passare tra un'estrusione verso l'esterno, verso l'interno o su entrambi i lati. 

##### Levigatezza {#smoothness}
Quando è attiva, leviga la forma estratta; funziona meglio con un numero di poligoni più alto. 
* `Tutti` / `Solo bordi` - Leviga l'intera forma, oppure solo i bordi, lasciando intatta la forma della superficie superiore.
* `Iterazioni` - Con `Tutti`, la quantità di levigatura applicata. Valori alti producono bordi curvi molto morbidi, ma iniziano ad allontanarsi dalla forma della maschera.
* `Parete` - Con `Solo bordi`, la quantità di levigatura sulle pareti. Il suo pulsante passa da Rilassa, che conserva gli angoli netti, a Leviga, che arrotonda anche quelli.
* `Interno` - Con `Solo bordi`, quanto viene uniformata la superficie superiore. Il suo pulsante passa da Rilassa, che conserva i dettagli scolpiti e uniforma solo la direzione di estrusione (così i dettagli non creano più punte), a Leviga, che leviga la superficie stessa.

##### Lati {#edge-loop-side}
* `Dritto` - Pareti semplici sui lati della forma estratta.
* `Smusso` - (solo Estrai con `Involucro`) Un bordo inclinato sullo spigolo frontale. `Smusso` ne imposta la larghezza, in % di `Altezza` o in unità del mondo (il pulsante accanto cambia unità), `Divisioni dello smusso` lo suddivide (`Auto` di default), e una curva ti permette di modellarne il profilo.
* `Profilo` - Modella le pareti con una curva di profilo, con una `Larghezza` in % di `Altezza` o in unità del mondo.
* `Maschera` - L'altezza segue la maschera: le parti sfocate della maschera hanno un'altezza minore, per ottenere forme morbide e di altezza variabile.
* `Divisioni parete` - Il numero di edge loop sui lati. Con `Auto`, Nomad sceglie il numero di divisioni che crea poligoni quadrati, in linea con i poligoni della zona mascherata.




### ![](/icons/tool_maskSelector.webp) Maschera a selezione {#selection-mask}
Lo strumento Maschera a selezione (SelMasch.) ora fa parte dello [strumento Maschera](#mask). Per mascherare con delle forme invece che con un tratto di pennello, scegli una forma (`Lazo`, `Poligono`, `Rett.`...) nel popup del tratto dello strumento Maschera, vedi [Controlli di selezione](#selection-controls).

Anche la modalità Sub `Togli masch.` funziona con le forme, e cancella la maschera all'interno della forma.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Dipingi {#paint}
Applica colore e proprietà del materiale. Per saperne di più sui materiali puoi consultare la sezione [Pittura](painting.md).

La modalità Sub è `Cancella` e rimuove la pittura.

Oltre ai tratti di pennello, Dipingi può anche riempire delle forme (`Lazo`, `Rett.`, `Banda`...), vedi [Controlli di selezione](#selection-controls).

#### Impostazioni di Dipingi {#paint-settings}
* `Filtro livelli` - Funziona come il blocco alfa dei livelli in Photoshop o Procreate. Se dipingi su un livello e questa opzione è attiva, puoi modificare solo dove c'è già della pittura; le zone non dipinte restano protette. È disponibile solo quando è selezionato un livello.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Sfumino {#smudge}
Sfuma il colore e le proprietà del materiale. Il menu delle impostazioni di Sfumino contiene un cursore `Qualità`: valori più bassi danno tratti più veloci.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Appiattisci {#flatten}
Appiattisce la zona proiettando i punti sul piano medio.

La modalità Sub è `Riempi`: definisce un piano a partire dal punto più alto e tende a tirare i punti verso l'alto.

#### Impostazioni di Appiattisci {#flatten-settings}

* `Blocca direzione del piano` - Usa la direzione del piano calcolata al primo clic. Di default è disattivato.
* `Blocca origine del piano`- Usa il primo clic come centro del piano. Di default è disattivato, e si può attivare solo insieme a `Blocca direzione del piano`.

Quando una o entrambe le opzioni sono disattivate, puoi approfondire gradualmente l'appiattimento o cambiare l'angolo del piano con tratti lunghi che passano su profondità e curvature diverse. Insieme alle opzioni di campionamento dell'area del menu del pennello, questo offre un controllo molto preciso.

::: tip
Quando lavori in zone molto curve, per esempio se vuoi appiattire le guance ma lo strumento continua a intaccare i lati del naso, prova a creare una maschera per proteggere le zone che il pennello Appiattisci non deve toccare.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planare {#planar}
Rende i punti complanari proiettandoli sul piano medio, ma con meno accumulo rispetto al pennello Appiattisci. Così crea superfici più pulite con spigoli netti. I tratti rapidi spingono e tirano di più la superficie, mentre i tratti lenti che partono da zone già piane e si allargano mantengono meglio il piano.

La modalità Sub è `Riempi`: definisce un piano a partire dal punto più alto e tende a tirare i punti verso l'alto.

In realtà Planare è lo stesso strumento di `Appiattisci`, ma con `Blocca direzione del piano` attivo: tende quindi a creare superfici più stabili e con spigoli netti, mentre Appiattisci è più scultoreo e si usa per creare zone semi-piatte.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polish {#polish}
Un altro membro della famiglia di Appiattisci, configurato per lucidare le superfici fino a ottenere piani puliti. È lo stesso strumento di `Appiattisci`, con impostazioni predefinite di [Tratto](stroke.md) diverse: `Scia`, `Filtro normale area` e `Filtro profondità` sono attivi.

La modalità Sub è `Riempi`, come per Appiattisci.

Polish ha le stesse impostazioni di [Appiattisci](#flatten-settings): `Blocca direzione del piano` e `Blocca origine del piano`.

### ![](/icons/tool_crease.webp) Solco {#crease}
Gli strumenti Solco sono utili per scolpire piccoli tagli o incavi.

La modalità Sub è `Inverti` e crea un solco in rilievo.

#### Impostazioni di Solco {#crease-settings}

* `Fattore pizzico` - Quanto tirare lateralmente i vertici verso il pennello. Con il pizzico a 1 e l'offset a 0, la superficie non cambia in profondità, cambia solo la topologia, con gli spigoli tirati verso il tratto.
* `Fattore di offset` - Quanto spingere/tirare i vertici in profondità. Con il pizzico a 0 e l'offset a 1 si ottengono solchi profondi o rilievi, ma dall'aspetto frastagliato, perché non viene tirata abbastanza geometria verso il solco per definirne con precisione i lati o il fondo.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pizzica {#pinch}
Questo strumento si può usare per rendere più netti gli spigoli.

La modalità Sub è `Inverti` e allontana i vertici tra loro.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Rifila {#trim}
Lo strumento Rifila rimuove un pezzo della mesh e offre varie opzioni per trattare il vuoto che resta. Usa i [Controlli di selezione](#selection-controls) per definire il taglio.

La modalità Sub è `Rifletti` e inverte la forma, così viene rimosso l'altro lato.

::: tip
Siccome questo strumento proietta dalla fotocamera, riceverai un avviso se la fotocamera è in modalità prospettiva.

In modalità ortografica il taglio attraverso la mesh è parallelo alla vista, che è quello che di solito ci si aspetta. Con una fotocamera in prospettiva, il taglio apparirà diverso sul lato lontano dell'oggetto rispetto a quello vicino.
:::

#### Impostazioni di Rifila {#trim-settings}

Le impostazioni sono raggruppate sotto `Riempimento aperture`:

* `Pittura del tratto` - Se la pittura è attiva nel menu Pittura, la zona riparata viene riempita con il colore selezionato.
* `Booleano` - riempie il buco del taglio con una zona di poligoni quad. La zona riempita sarà piatta.
* `Legacy` - riempie il buco del taglio con una zona triangolata. La zona riempita sarà piatta.
* `Riempi` - riempie il buco con una zona triangolata. La zona riempita sarà una superficie curva, come la pellicola di una bolla di sapone.
* `Nessuno` - non riempie il buco.

Con `Booleano`, la sezione `Dettaglio` contiene:

* `Forma` - La dimensione approssimativa dei quad e dei triangoli usati sul lato della forma del taglio.
* `Aperture` - La dimensione approssimativa dei triangoli o dei poligoni usati sul buco riempito. Il pulsante di collegamento accanto a `Dettaglio` lo mantiene sincronizzato con `Forma`; scollegalo per impostarlo separatamente.
* `Mantieni topologia` - Non leviga e non semplifica il bordo del taglio, mantenendo la topologia originale della mesh vicino alle facce mascherate e nascoste.

Con `Legacy`:

* `Dettaglio` - La dimensione approssimativa dei triangoli usati nel taglio.
* `Levigatura apertura` - Quanto vengono rilassati i triangoli nella zona riempita.
* `Soglia epsilon` - Un valore che si può regolare per migliorare l'algoritmo di riempimento legacy.

Con `Riempi`:

* `Dettaglio` - La dimensione approssimativa dei triangoli usati nel taglio.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Dividi {#split}
Simile allo strumento [Rifila](#trim), ma mentre Rifila scarta la selezione, Dividi la conserva come nuovo oggetto.

La modalità Sub è `Dividi`: ogni pezzo viene tenuto come oggetto a sé, quindi le forme sovrapposte (per esempio con la simmetria) vengono tagliate in parti separate invece di essere unite in una sola.

#### Impostazioni di Dividi {#split-settings}

Dividi ha le stesse impostazioni di `Riempimento aperture` di [Rifila](#trim-settings): `Pittura del tratto`, i metodi `Booleano`, `Legacy`, `Riempi` e `Nessuno`, e le relative opzioni di `Dettaglio`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Proietta {#project}
Lo strumento Proietta somiglia allo strumento [Rifila](#trim), ma non elimina né crea geometria: si limita a spostare i vertici per adattarli alla selezione.

![](/videos/tool_project.mp4)

::: tip
Se usi Proietta mentre sei su un livello, puoi miscelare la forma originale e quella proiettata con il cursore del livello.
:::

### ![](/icons/tool_layer.webp) Livello {#layer}
Solleva la superficie, ma ne limita l'altezza.

Se tieni la penna appoggiata e continui a passare su una zona, Livello la solleva fino a una certa altezza e poi si ferma, mentre altri strumenti continuano ad accumulare altezza.

Nota che di default il limite vale solo per il singolo tratto! Se inizi un nuovo tratto, l'accumulo riparte dalla nuova altezza della superficie.

Per impostare un'altezza massima costante su molti tratti, usa lo strumento Livello con il sistema dei [Livelli](layers.md) di Nomad.

Crea un livello e usa questo strumento. Ora l'altezza massima viene definita dal livello, quindi puoi dare tutti i tratti che vuoi e l'altezza resterà sempre la stessa.

`Sub` usa una profondità minima, creando scanalature.

#### Impostazioni di Livello {#layer-settings}

* `Utilizza dati del livello` - Se attivo, e se è selezionato un livello, usa i dati del livello per impostare l'altezza massima. Un avviso te lo ricorda quando nessun livello è selezionato.
* `Gonfia`- Se attivo, corregge la direzione in cui agisce Livello per ottenere risultati più morbidi.
* `Rilassa (Normale)` - Con `Gonfia` attivo, la quantità di levigatura applicata alle normali.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Gonfia {#inflate}
Sposta i vertici lungo le rispettive normali. `Sub` sposta i vertici lungo la normale invertita.

#### Impostazioni di Gonfia {#inflate-setings}
* `Rilassa (Normale)` - La quantità di levigatura applicata alle normali.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Spingi {#nudge}
Sposta o 'spalma' i punti nella direzione del tratto.

La modalità Sub è `Piega` e spinge una piega di materiale lungo il tratto: un rigonfiamento davanti al pennello, un avvallamento dietro.

#### Impostazioni di Spingi {#nudge-settings}
* `Leviga` - Quanto viene levigata la zona sotto il pennello mentre la spingi, per mantenere pulita la superficie spalmata.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Timbro {#stamp}

Fai clic e trascina per sollevare una zona della scultura con la forma dell'Alfa selezionata.

È semplicemente lo [strumento Pennello](#brush) con il tipo di tratto impostato su `Blocco + raggio`. 

`Sub` spinge il timbro verso l'interno invece di estrarlo dalla superficie.

::: tip
Timbro di solito funziona meglio con geometria ad alta risoluzione. Se cerchi online 'wrinkles alpha', 'pores alpha', 'scales alpha' ecc., queste texture alfa insieme a Timbro sono un ottimo modo per aggiungere dettagli organici alla scultura di un personaggio.

I due tipi di tratto servono a cose diverse. 

* `Blocco + raggio` ha un'*altezza* fissa: trascinando regoli la larghezza e la rotazione del timbro. Ideale per le texture della pelle, che devono avere la stessa profondità/altezza ma rotazioni e scale diverse per nascondere la ripetizione.
* `Blocco + intensità` ha una *larghezza* fissa: trascinando regoli la rotazione e l'altezza del timbro. Ideale per i rivetti, che devono avere tutti la stessa dimensione ma rotazioni e altezze diverse. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Applica come timbro una mappa di displacement vettoriale (VDM). A differenza di un'alfa, che può solo spingere la superficie in su o in giù, una VDM contiene una forma 3d completa, quindi può timbrare sporgenze come orecchie, corna o foglie arricciate. Funziona come [Timbro](#stamp), con gli stessi tipi di tratto `Blocco + raggio` e `Blocco + intensità`.

`Sub` (`Inverti`) inverte la profondità del timbro, per premerlo nella superficie come uno stampo.

La VDM si sceglie nel menu [Alfa](stroke.md#alpha), che ha anche un cursore `Altezza` per scalare solo l'altezza del timbro, senza cambiarne lo spostamento laterale.

Il pulsante `Crea` nella barra a sinistra ti permette di creare i tuoi timbri:

* `Nuovo VDM...` - Aggiunge un piano preparato per scolpire una VDM. Scolpisci la tua forma sul piano, poi esegui il bake con `Topologia -> Trasferisci -> VDM`: Nomad aggiunge il nuovo timbro alla libreria VDM e lo seleziona.
* `Cattura VDM` - (Sperimentale) Trascina sulla superficie di un modello per catturare quella zona e trasformarla in un timbro VDM. `Tolleranza` appiattisce dolcemente il bordo della cattura.

::: tip
Evita DynTopo quando scolpisci un piano VDM: danneggia le UV del piano e distorce il timbro. Tieni anche la scultura lontana dal bordo del piano, altrimenti il timbro mostrerà uno spigolo netto.
:::


### ![](/icons/tool_clearLayer.webp) DelLayer {#delete-layer}
Questo strumento può azzerare localmente i livelli; serve un livello attivo, altrimenti non succede nulla. Cancella i dati scolpiti del livello e, quando la pittura è attiva, anche la sua pittura.

La modalità Sub è `Inverti` e rafforza leggermente il livello invece di cancellarlo.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tubo {#tube}
Crea un tubo disegnando una curva. 
![](/images/tool_tube_new.webp)

Una volta creato il tubo, puoi modificarne il percorso nello spazio 3d con controlli simili a quelli della [Modifica delle forme](#shape-editing) e degli strumenti di modifica delle curve. 

![](/videos/tool_tube.mp4)

#### Barra a sinistra di Tubo {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

La barra degli strumenti a sinistra ha le seguenti opzioni:

* `Sincronizza` - Se il tubo attuale è istanziato e ha nodi figli diversi tra un'istanza e l'altra, questa opzione li risincronizza.
* `Aggancio` - Se attivo, le modalità curva e tracciato si agganciano agli altri oggetti mentre disegni. Se disattivo, si aggancia il primo punto e il resto del tubo viene disegnato a quella profondità.
* `Spostamento` - Imposta la profondità dell'aggancio: con 0% il centro della sezione del tubo si aggancia alla superficie, i valori positivi lo sollevano dalla superficie, quelli negativi lo abbassano. 100% equivale al raggio del tubo.
* `Vista` - Nessuna modalità di disegno, così puoi muovere liberamente la fotocamera.
* `Curva` - Disegna un tubo a mano libera. Ha un piccolo menu a comparsa:
    * `Modifica` - Cosa succede quando finisci il tratto, vedi [Controlli di selezione](#selection-controls): crea subito il tubo, mantieni la curva modificabile con un cerchio verde di conferma accanto, oppure `Tieni premuto` alla fine del tratto per continuare a modificarla.
    * `Chiuso` - trasforma il tubo in un anello.
    * `Continua a disegnare` - Dopo aver confermato un tubo, resta nello strumento per disegnare il successivo.
    * `Precisione` - Quanti punti di curva vengono usati per convertire il percorso disegnato in un tubo. Con 0% si usa il numero minimo di punti, ma si perdono i piccoli cambi di curvatura del percorso. Con 100% il risultato è molto preciso e usa molti punti.
* `Tracciato` - Crea un tubo facendo clic per definire i punti della curva. Tocca il cerchio verde per confermare il tracciato. Ha un piccolo menu a comparsa:
    * `B-spline` - Un metodo alternativo di disegno delle curve in cui i punti di solito non stanno direttamente sulla curva, ma che può dare risultati più morbidi del metodo predefinito.
    * `Chiuso` - trasforma il tubo in un anello
    * `Schermo` - Se attivo, il tracciato è 'fissato' allo schermo: puoi muovere la vista e l'oggetto e il tracciato resta al suo posto. Se disattivo, il tracciato fa parte della scena 3d e si muove con la fotocamera e gli oggetti.
* `Sezione` - La curva diventa un anello attorno alla forma, tagliato attraverso i suoi due punti lungo la direzione da cui stavi guardando.

##### Barra in alto di Tubo {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Quando un tubo è selezionato, in cima al viewport compare una barra degli strumenti con controlli aggiuntivi. Fai clic sul titolo della barra per comprimerla/espanderla, e sulla freccia in alto a destra per spostarla in cima o in fondo al viewport.

* `Conferma` - converte il tubo in poligoni normali così da poterlo scolpire.
* `Modifica` - mostra i punti della curva per poterli manipolare
* `Specchia` - aggiunge un ripetitore specchio come genitore di questa curva
* `Aggancio` - aggancia i punti della curva alle superfici vicine
* `Chiuso` - Unisce l'inizio e la fine della curva per formare un anello
* `B-spline` - Passa dall'interpolazione Catmull-rom a quella B-spline e viceversa.
* `Estremità` - Passa ciclicamente tra estremità chiuse su entrambi i lati del tubo, solo all'inizio o alla fine, o nessuna chiusura.
* `Apertura` - Aggiunge spessore al tubo, trasformandolo in una canna. Passa ciclicamente tra un'apertura a entrambe le estremità, solo alla fine, o nessuna apertura. 
* `Raggio` - Passa ciclicamente tra un raggio uniforme, un raggio all'inizio e alla fine, o un raggio per ogni punto della curva. Si modificano con le maniglie arancioni sulla curva.
* `Torsione` - Passa ciclicamente tra nessuna torsione, una torsione uniforme, una torsione all'inizio e alla fine, o una torsione per ogni punto della curva. Si modificano con le maniglie rosa sulla curva.
* `Profilo` - Passa ciclicamente tra nessun profilo (cioè un profilo circolare), un profilo uniforme, un profilo all'inizio e alla fine, o un profilo per ogni punto.
* `Modifica profilo` - Mostra un editor del profilo. Funziona in modo simile agli strumenti di [Modifica delle forme](#shape-editing), può salvare e caricare preset di profilo e ha un interruttore per modificare il profilo nello spazio 3d.
* `Spirale` - Apre un menu per aggiungere una torsione a spirale al tubo. Questo menu ha le opzioni `Angolo di torsione`, `Spostamento`, `Scala` e `Offset angolare`.
* `Divisioni X` - il numero di divisioni attorno al tubo; con 4 divisioni, per esempio, ottieni un tubo a sezione quadrata. 
* `Densità costante` - se attiva, mantiene i poligoni quadrati. Se disattivata, ti permette di impostare le `Divisioni Y` lungo il tubo.
* `...` - Menu delle impostazioni di Tubo.

#### Interruttore di eliminazione dei punti {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Sotto la barra degli strumenti c'è un interruttore per l'eliminazione dei punti della curva. Quando trascini un punto della curva vicino a un altro, diventa rosso: significa che, se lo rilasci, il punto verrà eliminato. Se stai facendo piccole modifiche e non vuoi eliminare punti, questo pulsante disattiva l'eliminazione.



#### Impostazioni di Tubo {#tube-settings}
* `Primitiva` - pulsanti per attivare/disattivare le UV, o per confermare il tubo.
* `Post-suddivisione` - una scorciatoia per impostare il livello di multires prima di confermare.
* `Suddivisione lineare` - scorciatoia per impostare il livello di suddivisione lineare prima di confermare. 
* `Divisione X` - uguale a Divisioni X nella barra degli strumenti.
* `Divisione Y` - uguale a Divisioni Y nella barra degli strumenti.
* `Curva (Ripetitore)` - converte il tubo in un [Ripetitore curva](scene.md#curve)

::: tip
Divisioni a 4 e Post-suddivisione a 3 danno tubi lisci con le punte arrotondate, ideali per vermi, serpenti, parti del corpo.
:::


### ![](/icons/tool_lathe.webp) Lathe {#lathe}
Crea una superficie di rivoluzione disegnando una curva.

Questo strumento è ottimo per forme come vasi e calici.

![](/videos/tool_lathe.mp4)

#### Barra a sinistra di Lathe {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

La barra degli strumenti a sinistra ha le seguenti opzioni:

* `Sincronizza` - Se il lathe attuale è istanziato e ha nodi figli diversi tra un'istanza e l'altra, questa opzione li risincronizza.
* `Fisso` - Se attivo, il centro del lathe è fisso e viene mostrato sullo schermo. Questa linea centrale ha punti di modifica regolabili. Se disattivo, il centro del lathe si aggiorna dinamicamente in base all'inizio e alla fine della curva disegnata.
* `Vista` - Nessuna modalità di disegno, così puoi muovere liberamente la fotocamera.
* `Curva` - Disegna il profilo del lathe in un solo tratto. Ha un piccolo menu a comparsa:
    * `Modifica` - Cosa succede quando sollevi la penna, vedi [Controlli di selezione](#selection-controls): crea subito il lathe, mantieni la curva modificabile con un cerchio verde accanto per creare il lathe, oppure `Tieni premuto` alla fine del tratto per continuare a modificarla.
    * `Chiuso` - Unisce l'inizio e la fine della curva per formare un anello
    * `Continua a disegnare` - Dopo aver confermato un lathe, resta nello strumento per disegnare il successivo.
    * `Precisione` - Quanti punti di curva vengono usati per convertire il percorso disegnato in un tubo. Con 0% si usa il numero minimo di punti, ma si perdono i piccoli cambi di curvatura del percorso. Con 100% il risultato è molto preciso e usa molti punti.
* `Tracciato` - Crea un lathe facendo clic per definire i punti della curva. Tocca il cerchio verde per confermare il tracciato. Ha un piccolo menu a comparsa:
    * `B-spline` - Un metodo alternativo di disegno delle curve in cui i punti di solito non stanno direttamente sulla curva, ma che può dare risultati più morbidi del metodo predefinito.
    * `Chiuso` - trasforma il tubo in un anello
    * `Schermo` - Se attivo, il tracciato è 'fissato' allo schermo: puoi muovere la vista e l'oggetto e il tracciato resta al suo posto. Se disattivo, il tracciato fa parte della scena 3d e si muove con la fotocamera e gli oggetti.

#### Barra in alto di Lathe {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Quando un lathe è selezionato, in cima al viewport compare una barra degli strumenti con controlli aggiuntivi. Fai clic sul titolo della barra per comprimerla/espanderla, e sulla freccia in alto a destra per spostarla in cima o in fondo al viewport.

* `Conferma` - converte il lathe in poligoni normali così da poterlo scolpire.
* `Modifica` - mostra i punti della curva per poterli manipolare
* `Specchia` - aggiunge un ripetitore specchio come genitore di questo lathe
* `Aggancio` - aggancia i punti della curva alle superfici vicine
* `Stabile` - Se attivo, il profilo della curva è figlio della linea centrale del lathe. Se disattivo, puoi modificare la linea centrale senza spostare la curva, per ottenere forme più complesse.
* `Fuoco` - Ruota la vista per vedere il profilo della curva perfettamente in piano rispetto alla fotocamera.
* `Chiuso` - Unisce l'inizio e la fine della curva per formare un anello
* `Estremità` - Se Chiuso è disattivato, passa ciclicamente tra estremità chiuse su entrambi i lati, solo all'inizio o alla fine, o nessuna chiusura.
* `Apertura` - Aggiunge spessore al lathe, trasformandolo in una canna. Passa ciclicamente tra un'apertura a entrambe le estremità, solo alla fine, o nessuna apertura. 
* `B-spline` - Passa dall'interpolazione Catmull-rom a quella B-spline e viceversa.
* `Divisioni X` - il numero di divisioni attorno al lathe; con 4 divisioni, per esempio, ottieni un lathe a profilo quadrato. 
* `Densità costante` - se attiva, mantiene i poligoni quadrati. Se disattivata, ti permette di impostare le `Divisioni Y` lungo il tubo.
* `...` - Menu delle impostazioni di Lathe.

#### Impostazioni di Lathe {#lathe-settings}
* `Primitiva` - pulsanti per attivare/disattivare le UV, o per confermare il tubo.
* `Post-suddivisione` - una scorciatoia per impostare il livello di multires prima di confermare.
* `Suddivisione lineare` - scorciatoia per impostare il livello di suddivisione lineare prima di confermare. 
* `Divisione X` - uguale a Divisioni X nella barra degli strumenti.
* `Divisione Y` - uguale a Divisioni Y nella barra degli strumenti.
* `Curva (Ripetitore)` - converte il profilo della curva in un [Ripetitore curva](scene.md#curve)

### ![](/icons/tool_insert.webp) Inserisci {#insert}
Posiziona un oggetto sulla superficie di un altro. Nell'uso è simile allo strumento Timbro, ma per forme 3d complete.

Se selezioni una primitiva nella barra a sinistra, facendo clic e trascinando su una superficie qualsiasi posizioni una primitiva dove fai clic, e il trascinamento ne imposta la dimensione. Quando finisci di trascinare, Inserisci passa alla modalità [Trasforma](#transform).

In modalità Istanza, trascinando crei una nuova istanza e la fai scorrere sulla superficie. La dimensione viene copiata dalla prima forma: in questo modo puoi posizionare molte istanze della stessa dimensione di un oggetto su altre superfici.

Non sei limitato a inserire primitive! Seleziona *qualsiasi* forma nella gerarchia: se Inserisci è in modalità Istanza o Clona, puoi trascinare copie dell'oggetto selezionato su qualsiasi altra superficie.

Se un oggetto ha un pivot personalizzato, questo viene usato come punto di ancoraggio. Guarda il video qui sotto.

La barra a sinistra ha anche `Vista`, per muovere la fotocamera senza inserire nulla, e `Sincronizza`: quando l'oggetto di destinazione è istanziato, il nuovo oggetto viene aggiunto anche su tutte le altre istanze.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Trasforma {#transform}
Sposta/ruota/scala un modello direttamente con 1 e 2 dita, di solito sulla superficie di un altro oggetto.

La barra a sinistra ha questi pulsanti:

* `Clona` / `Istanza` - Crea una copia o un'istanza dell'oggetto, vedi la barra di [Gizmo](#left-menu-toolbar).
* `Sposta` - Il trascinamento con un dito sposta l'oggetto. Con l'aggancio attivo, fa scorrere l'oggetto lungo la superficie sotto il dito.
* `Ruota` - Il trascinamento con un dito ruota l'oggetto. Con l'aggancio attivo, ruota attorno alla normale della superficie sotto il dito.
* `Scala` - Il trascinamento con un dito scala l'oggetto.

Una barra in cima al viewport contiene:

* `Target` - Se lo strumento sposta l'oggetto, il suo gruppo o i suoi vertici, come per il [Gizmo](#left-menu-toolbar).
* `Aggancia` - aggancia il modello ad altre superfici.
* `Superficie` / `Vertice` - Con `Aggancia`, aggancia alla superficie o al vertice più vicino.

Con Trasforma puoi usare rapidamente 2 di queste modalità usando 2 dita:

* Trascina un oggetto per posizionarlo. Smetti di muovere il primo dito, ma non sollevarlo dallo schermo.
* Appoggia il secondo dito sullo schermo tenendo giù il primo. Trascinando il secondo dito, l'oggetto viene scalato.
* Solleva il secondo dito e continua a trascinare il primo: l'oggetto torna in modalità spostamento.

Puoi anche cambiare la seconda modalità con un tocco del secondo dito:

* Trascina l'oggetto per posizionarlo, smetti di muoverlo, ma non sollevare il dito dallo schermo.
* Tocca con il secondo dito tenendo giù il primo
* Lo strumento passa in modalità rotazione. Trascina il primo dito per impostare la rotazione.
* Tocca di nuovo con il secondo dito come prima: lo strumento torna in modalità spostamento.

Questo offre un flusso di lavoro rapido per clonare oggetti su un altro, per esempio rocce su un paesaggio. Nota che il pulsante di clonazione si trova anche nella barra a sinistra, per averlo sempre a portata di mano:

* Usa lo strumento Trasforma per mettere una roccia al suo posto.
* Rilascia, premi il pulsante di clonazione
* Sposta questa roccia, ruotala/scalala come serve
* Rilascia, premi il pulsante di clonazione
* Sposta questa roccia, e ripeti.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Questo strumento ti permette di spostare, ruotare e scalare gli oggetti, e di modificarne i pivot.

La maniglia nel viewport ha le seguenti funzioni:

* `Sposta` - Trascina sulla linea con la freccia per spostare su X/Y/Z. Trascina il punto color pesca al centro del gizmo per traslare liberamente nello spazio dello schermo. Fai clic sui quadrati rosso, verde e blu per traslare sui piani X/Y/Z.
* `Ruota` - Trascina sui cerchi rosso/verde/blu per ruotare su X/Y/Z. Trascina la sfera all'interno dei cerchi per ruotare liberamente.
* `Scala`- Trascina sui punti esterni rosso/verde/blu per scalare su X/Y/Z. Trascina sui coni esterni rosso/verde/blu per scalare sui piani X/Y/Z. Trascina sul cerchio esterno color pesca per una scala uniforme.

![](/images/tool_gizmo.webp)

#### Nodi e vertici {#nodes-and-vertices}

Ogni oggetto in Nomad è composto da un nodo e da vertici:

* `Nodo` - La 'maniglia' dell'oggetto, che memorizza traslazione, rotazione e scala: la sua cosiddetta matrice di trasformazione.
* `Vertici` - I punti che definiscono la superficie di un oggetto; memorizzano la posizione e le informazioni di pittura.

Se hai un semplice cubo composto da 8 vertici, puoi traslarlo modificando la sua matrice di trasformazione, oppure modificando le posizioni dei vertici. Quando scolpisci di solito vuoi modificare i vertici, quando sposti gli oggetti con il gizmo di solito vuoi modificare il nodo. Nomad ti permette di fare entrambe le cose. 

#### Barre di Gizmo {#left-menu-toolbar}

La barra a sinistra contiene:

* `Clona` - Crea una copia indipendente dell'oggetto attuale, che puoi trascinare via con il gizmo.
* `Istanza` - Crea una copia istanziata dell'oggetto attuale. Gli oggetti sono collegati, quindi le modifiche di scultura su uno appaiono su tutti gli oggetti istanziati.
* `Pivot` - (icona del lucchetto, al posto del pulsante `Sub`) Se attivo, puoi spostare e ruotare il gizmo senza spostare l'oggetto. Come `Sub`, tienilo premuto per un cambio rapido, o toccalo per lasciarlo attivo.

Una barra in cima al viewport contiene gli altri controlli:

* `Target` - Stabilisce se il gizmo agisce sul nodo o sui vertici di un oggetto:
    * `Auto` - L'opzione predefinita: funziona come `Gruppo`, ma se la mesh ha una maschera o la simmetria è attiva, funziona come `Vertice`.
    * `Vertice` - Applica la trasformazione ai vertici, tenendo conto della maschera e della simmetria. Non funziona sulle primitive non confermate, e coinvolge anche le istanze.
    * `Oggetto` - Sposta solo l'oggetto attuale, ignorando simmetria e maschera. Gli oggetti figli restano fermi.
    * `Gruppo` - Sposta l'oggetto e il resto della sua gerarchia, ignorando simmetria e maschera.
    * `Istanza` - (Oggetto e Gruppo) Lo stesso, ma si spostano anche tutte le istanze dell'oggetto.
* `Pivot` - Un popup per posizionare rapidamente il pivot, spiegato [più sotto](#pivot).
* `Tutti` / `Sposta` / `Ruota` / `Scala` - Mostra tutte le maniglie del gizmo, oppure solo quelle di spostamento, rotazione o scala.
* `Fissa` - Di default il gizmo si sposta sul pivot dell'oggetto selezionato. Con Fissa attivo, il gizmo resta dove si trova.
* `Allinea` - Allinea il pivot all'oggetto attuale oppure al mondo.
* `Aggancia` (rotazione) - Fa scattare i valori di rotazione a incrementi; il valore di scatto viene mostrato e si può modificare quando l'aggancio è attivo. La sua opzione `Magnete` fa aderire la rotazione a uno scatto quando lo attraversa, poi la lascia di nuovo libera; disattivala per saltare da uno scatto all'altro.
* `Aggancia` (traslazione) - Fa scattare i valori di traslazione a incrementi; il valore di scatto viene mostrato e si può modificare quando l'aggancio è attivo.

#### ![](/icons/reset.webp) Pivot {#pivot}
Il popup `Pivot` nella barra in alto permette di cambiare rapidamente il pivot. La posizione e l'orientamento del pivot guidano il gizmo.

**Ripristina** 
* `Auto` - Centro dell'oggetto, allineato alla sua trasformazione.
* `Centrato` - Sposta il pivot al centro dell'oggetto, mantenendone l'orientamento.
* `Inferiore` - Sposta il pivot al centro della base dell'oggetto. Tocca di nuovo per usare invece il riquadro di delimitazione nel mondo.
* `Superiore` - Sposta il pivot al centro della sommità dell'oggetto. Tocca di nuovo per usare invece il riquadro di delimitazione nel mondo.
* `Oggetto` - Sposta il pivot nell'origine dell'oggetto, allineato alla sua trasformazione.
* `Maschera` - Sposta il pivot al centro della zona non mascherata. Tocca di nuovo per passare alla zona mascherata.
* `Allinea` - Azzera le rotazioni per allinearle al mondo, mantenendo la posizione.
* `Vista` - Allinea il pivot alla vista attuale, mantenendo la posizione. In seguito non segue la fotocamera.

**Solo tocco (modalità Pivot)**

Attivo solo quando `Pivot` è acceso, stabilisce cosa succede quando tocchi una volta la superficie della mesh:
* `Nessuno` - non fa nulla quando si tocca l'oggetto
* `Normale` - Sposta e ruota il pivot per allinearlo al punto toccato della superficie
* `Prima` - Sposta (senza ruotare) il pivot nel punto toccato della superficie
* `Mediana` - Sposta il pivot al centro dell'oggetto, sotto il punto toccato della superficie.

#### Impostazioni di Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Compatto` - cambia la disposizione del gizmo per mettere le maniglie extra fuori o dentro la sfera di rotazione
* `Dimensione widget` - la dimensione del gizmo
* `Spessore` - lo spessore delle linee del gizmo
* `Opacità` - l'opacità del gizmo
* `Nascondi durante l'interazione` - stabilisce se il gizmo viene nascosto temporaneamente mentre lo trascini

-----

* `Soglia scorrimento tangente` - Controlla il comportamento della rotazione quando trascini sulle maniglie circolari per ruotare su X/Y/Z. Con un valore di 0, la rotazione funziona come una manopola: trascini il gizmo in cerchio. Con un valore di 90, la rotazione funziona come tirare il filo di uno yo-yo: trascini in linea retta avvicinandoti o allontanandoti dal punto in cui hai fatto clic. I valori tra 0 e 90 combinano i due comportamenti: sotto il valore il movimento è lineare, sopra è circolare.
* `Inserimento numerico` - se attivo, un singolo tocco sul gizmo apre una finestra per inserire un valore esatto per l'asse toccato.

::: warning
Gli strumenti [Gizmo](#gizmo) e [Trasforma](#transform) usano una propria casella di simmetria, separata dalla simmetria di scultura!

Di default questa simmetria è disattivata.
:::

##### Matrice {#matrix}
I valori esatti di trasformazione dell'oggetto non si trovano più nelle impostazioni di Gizmo: sono stati spostati nel menu `Trasforma`, nel menu in alto a destra. La sua sezione `Matrice` contiene:

* ![](/icons/target.webp) `Sposta origine` - Sposta l'oggetto in modo che il suo pivot sia al centro della scena, chiamato origine.
* ![](/icons/bake.webp)  `Trasferisci` - Blocca l'oggetto dove si trova e imposta i valori di traslazione/rotazione a 0 e la scala a 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivot` - Esegue il bake del pivot: fa corrispondere i valori della matrice alla posizione della maniglia del gizmo nel mondo.
* ![](/icons/reset.webp) `Ripristina` - Una scorciatoia che imposta i valori di traslazione a 0, quelli di rotazione a 0 e la scala a 1, spostando e ruotando l'oggetto.

::: tip Bake o bake del pivot
Crea un cubo, seleziona lo strumento Gizmo, apri e fissa il menu `Trasforma`. Di default traslazione e rotazione sono a 0 e la scala è 1.

Attiva la modalità pivot, sposta la maniglia da un lato, poi disattiva la modalità pivot. Il pivot è cambiato, ma nota che i valori di traslazione sono ancora a 0. 

Se vuoi vedere dove si trova *davvero* il pivot, fai clic sul pulsante di bake `Pivot`. Ora i valori di traslazione si aggiornano. Nota che il cubo non si muove durante questa operazione, né in modalità pivot.

Sposta e ruota il cubo da qualche parte, poi tocca `Sposta origine`. L'oggetto viene spostato in modo che il suo pivot sia al centro del mondo, ma la rotazione resta invariata.

Fai clic su `Ripristina`, e anche la rotazione viene impostata a 0.

Sposta e ruota di nuovo il cubo, questa volta fai clic su `Trasferisci`. Il pivot resta dov'è, il cubo resta dov'è, ma i valori di traslazione e rotazione vengono impostati a 0.

Esercitati qualche volta! Devi capire che i valori del pivot sono nascosti e che Nomad se ne occupa per te, ma se hai bisogno di posizionare il pivot in punti reali dello spazio, il bake del pivot lo fa per te.

:::

* `Traslazione` - i valori di traslazione X, Y, Z
* `Rotazione` - i valori di rotazione X, Y, Z
* `Scala` - La scala uniforme se è attiva, altrimenti la scala X, Y, Z.
* `Inclina` - i valori di inclinazione (taglio) X, Y, Z, mostrati solo quando l'oggetto è già inclinato
* `Scala uniforme` - Permette di scalare in modo uniforme o indipendente su ogni asse

A sinistra puoi spostare il pivot del gizmo: lo vedi in azione nel video qui sotto.
È particolarmente utile per la rotazione, perché per la traslazione non cambia nulla.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Gruppo di facce {#facegroup}

I gruppi di facce ti permettono di organizzare l'oggetto in facce di colori diversi. In Nomad puoi usare questi gruppi in molti modi:

* Un metodo rapido di selezione per le maschere
* Nascondere/mostrare sezioni dell'oggetto
* Organizzare l'oggetto senza doverlo dividere in parti separate
* Definire le regioni UV
* Guidare il quad remesher
* Un controllo in più per strumenti come Leviga.

#### Barra a sinistra di Gruppo di facce {#facegroup-left-toolbar}

* `Gruppo` - Il pulsante mostra il gruppo di facce attuale. Toccalo per vedere i gruppi di facce disponibili come tasselli e sceglierne uno. Tocca un tassello per rinominarlo, cambiarne il colore o eliminarlo. `Rimuovi inutilizzati` elimina i tasselli non usati, `Ripristina` li rimuove tutti. L'icona più ti permette di creare nuovi tasselli.
* `Punto` - Dipingi sull'oggetto per definire i gruppi di facce. Quando '+ Gruppo di facce' è attivo, ogni nuovo tratto crea automaticamente un nuovo gruppo di facce, utile per definire rapidamente le regioni. Un tocco riempie la regione selezionata. Il cursore imposta il raggio del punto.
* `Rilassa` - Leviga i bordi dei gruppi di facce. Molto utile per definire bordi puliti per il remeshing quad, o per definire pannelli nella modellazione hard surface. I cursori controllano raggio e intensità del rilassamento.
* Forme - Crea gruppi di facce con le forme invece che con un pennello, tramite `Blocco + raggio`, `Lazo`, `Poligono`, `Linea`, `Rett.` ed `Ellisse`. Vedi [Controlli di selezione](#selection-controls) per saperne di più.
* `Scegli` - La modalità Sub. Se attiva, seleziona il tassello in cui inizia il tratto e lo applica per tutto il resto del tratto. Molto utile per sistemare le regioni dei gruppi di facce: se un gruppo di facce si è esteso troppo, attiva `Scegli`, inizia un tratto da dove il tassello del gruppo è corretto e trascina fino al bordo per riassegnare il tassello giusto.

#### Barra in alto di Gruppo di facce {#facegroup-top-toolbar}

Una barra in cima al viewport contiene controlli aggiuntivi:

* `Rilassa (Tutti)` - Trascina per rilassare i bordi di tutti i gruppi di facce in una volta.
* `Frontale` / `Visibile` / `Collegata` - Gli stessi filtri del tratto della barra di [Maschera](#mask).
* `Da normali` - Crea gruppi di facce in base all'angolo tra le facce. Il popup contiene l'`Angolo` e ti permette di ignorare i gruppi piccoli in base al `Conteggio facce` o all'`Area superficiale`, con un'`Anteprima` prima di confermare.
* `Da parti` - Crea un gruppo di facce per ogni parte non collegata.
* `Da UV` - Crea un gruppo di facce per ogni isola UV.
* `Da maschera` - Crea un gruppo di facce dalla zona mascherata.
* `Tocco` - Scegli cosa fa un tocco su un gruppo di facce: lo riempie con il gruppo di facce attuale, lo nasconde, lo maschera, oppure lo mette in `Posa` (il gruppo toccato e ciò che sta oltre vengono smascherati, e il gizmo si posiziona sull'articolazione, con un cursore `Sfoca` per la maschera). Un secondo interruttore `Tocco`, disponibile quando la mesh ha una maschera, limita il tocco alle facce sullo stesso lato della maschera.
* Pulsanti `Cancella` per gli strumenti [Nascondi](#hide) e [Maschera](#mask), per mostrare di nuovo tutto o cancellare la maschera senza uscire dallo strumento.

#### Impostazioni di Gruppo di facce {#facegroup-settings}

Il menu `Strumento` estrae i gruppi di facce in nuovi oggetti, con le stesse opzioni di `Estrai` nelle [Impostazioni di Maschera](#mask-settings). Il pulsante `Gruppo di facce` in alto sceglie quali gruppi estrarre, e c'è un cursore `Spazio` in più: sposta ogni bordo verso l'interno lungo la superficie, mentre un valore negativo lo sposta verso l'esterno per sovrapporsi. Per pannelli adiacenti, usa metà dello spazio desiderato.

### ![](/icons/tool_hide.webp) Nascondi {#hide}
Nasconde o isola parti dell'oggetto. 

Le modalità principali si controllano dal menu a sinistra:

* `Punto` - Passa il pennello sull'oggetto per nasconderne delle parti.
* Forme -  Nascondi con le forme invece che con un pennello, tramite `Lazo`, `Poligono`, `Linea`, `Rett.` ed `Ellisse`. Vedi [Controlli di selezione](#selection-controls) per saperne di più.
* `Mostra` - La modalità Sub: inverte l'operazione, così la modalità scelta mostra le parti dell'oggetto invece di nasconderle.

In cima al viewport compare una barra degli strumenti con controlli aggiuntivi:

* `Pulisci tutto` - Ripristina gli oggetti: tutte le parti nascoste tornano visibili. Quando anche altri oggetti hanno parti nascoste, un pulsante `Cancella` in più ripristina solo gli oggetti selezionati.
* `Inverti` - Scambia le parti nascoste con quelle visibili.
* `Elimina` - Elimina la parte nascosta dell'oggetto
* `Dividi` - Separa la parte nascosta dell'oggetto in una nuova forma.
* `Frontale` / `Visibile` / `Collegata` - Gli stessi filtri del tratto della barra di [Maschera](#mask).
* `Tocco` (gruppo di facce) - Usa i gruppi di facce per nascondere rapidamente delle sezioni: toccando un gruppo di facce lo nascondi per intero.
* `Tocco` (maschera) - Se è attiva una maschera, un tocco nasconde la sezione mascherata.

### ![](/icons/tool_measure.webp) Misura {#measure}
Trascina per misurare la distanza tra 2 punti. Una volta posizionati, puoi trascinare i punti finali per regolare la misura.

La barra a sinistra sceglie come viene misurata la distanza:

* `Linea` - Una linea retta tra i due punti.
* `Superficie` - La distanza lungo la superficie, seguendo il taglio che passa per i due punti visto dalla fotocamera.
* `Sezione` - Il perimetro della sezione che passa per i due punti, come un metro da sarta attorno a un braccio.
* `Vertice` - Aggancia i punti finali al vertice più vicino.
* `Sezione aurea` - Mostra un punto giallo nel punto della sezione aurea della misura.
* Il pulsante `?` mostra il volume, l'area della superficie e la dimensione degli oggetti selezionati.

### ![](/icons/tool_arrange.webp) Disponi {#arrange}
Allinea e disponi più oggetti in una volta, come gli strumenti di allineamento di un'app di grafica 2d. Seleziona prima gli oggetti; con un solo oggetto, Disponi agisce invece sulle sue parti separate. Attorno alla selezione viene disegnato un riquadro: trascinane le maniglie per scalarla.

Una barra in cima al viewport contiene i controlli:

* `Mondo` / `Schermo` - Disponi lungo gli assi del mondo, oppure lungo lo schermo (sinistra, destra, alto, basso).
* `Allinea` - Allinea gli oggetti sul minimo, sul centro o sul massimo, su ogni asse.
* `Distribuisci` - Distribuisce gli oggetti in modo uniforme tra i due più esterni, in base al minimo, al centro o al massimo. Servono almeno 3 oggetti.
* `Linea` - Mette gli oggetti in fila lungo un asse.
* `Griglia` - Dispone gli oggetti in una griglia, con un numero di oggetti su `X`, `Y` e `Z`.
* `Cerchio` - (solo Mondo) Dispone gli oggetti in cerchio attorno all'asse `X`, `Y` o `Z`.
* `Sfera` - (solo Mondo) Dispone gli oggetti su una sfera.

`Linea`, `Griglia`, `Cerchio` e `Sfera` hanno tutti un cursore `Spaziatura` per la distanza tra gli oggetti.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Questo strumento converte l'oggetto selezionato in una topologia quad pulita, con controlli per densità, flusso degli spigoli e simmetria. 

::: tip
Quad Remesher è sviluppato da [Exoside](https://exoside.com/) per iOS e desktop. 

Su iOS è un acquisto in-app all'interno di Nomad, con un pagamento unico di 16 USD.

Su desktop, acquista una licenza da [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Puoi acquistarla solo per Nomad desktop, oppure una licenza multipla per tutte le app desktop supportate.

Se possiedi già Quad Remesher per un'altra app desktop, puoi [acquistare un aggiornamento a tutte le piattaforme a un costo ridotto.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher non è disponibile per Android. Su Android puoi usare i remesher gratuiti e open source della scheda di topologia [Remeshing quad](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), ma tieni presente che le loro funzionalità sono più limitate.
:::

Finché Quad Remesher non è sbloccato, la barra in alto inizia con un pulsante carrello al posto dei pulsanti di remeshing. Su iOS apre l'acquisto in-app. Su desktop mostra `Sblocca (acquisto, ripristino, prova)`, che verifica la tua licenza Exoside (o avvia la prova). Una volta attivo, le barre a sinistra e in alto vengono abilitate.

* `Punto` - Questo pennello imposta la densità desiderata. Con l'intensità al 100% dipinge in rosso, cioè il doppio della densità di quad desiderata in quelle zone. Con l'intensità allo 0% dipinge in ciano, cioè la metà della densità di quad desiderata in quelle zone. Con l'intensità al 50% dipinge in grigio, cioè la densità di quad desiderata predefinita.
* `Leviga` - Leviga le transizioni di densità rosso/grigio/ciano.
* `Sfumino` - Sfuma la pittura di densità.
* `Curva` - Disegna curve sulla superficie della scultura: il quad remesher le userà come guide per il flusso degli spigoli. Tocca una curva per eliminarla.
* `Tracciato` - Disegna tracciati sulla superficie della scultura: il quad remesher li userà come guide per il flusso degli spigoli. Tocca un tracciato per eliminarlo. 
* `Rett.` - Disegna rettangoli sulla superficie della scultura: il quad remesher li userà come guide per il flusso degli spigoli. Tocca un tracciato per eliminarlo.
* `Ellisse` - Disegna ellissi sulla superficie della scultura: il quad remesher le userà come guide per il flusso degli spigoli. Tocca un tracciato per eliminarlo.

#### Barra in alto di Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

In cima al viewport compare una barra degli strumenti con controlli aggiuntivi:


* `<Count>` - Fai clic qui per avviare il quad remesher; questo numero indica il numero di quad desiderato.
* `Quadrilateri` - Imposta il numero di quad desiderato scorrendo a sinistra e a destra, o tocca per inserire un numero esatto. Nota che è un'indicazione più che un numero fisso: i vari controlli del quad remesher spesso fanno sì che il risultato non corrisponda esattamente all'obiettivo.
* `Metà` - Una scorciatoia per impostare l'obiettivo alla metà del numero attuale di poligoni.
* `Uguale` - Una scorciatoia per impostare l'obiettivo al numero attuale di poligoni.
* `Guide` - attiva/disattiva l'uso delle guide. Quando ci sono delle guide, un secondo pulsante `Guide` ne mostra il numero: toccalo per eliminarle tutte.
* `Densità` - attiva/disattiva l'uso della pittura di densità. Quando c'è della pittura di densità, un secondo pulsante `Densità` la rimuove.
* `Gruppo di facce` - attiva/disattiva l'uso dei gruppi di facce per guidare il quad remesher.
* `Rilassa` - attiva/disattiva il rilassamento automatico dei bordi dei gruppi di facce durante il remeshing quad. Se hai già rilassato/levigato i bordi dei tuoi gruppi di facce, disattiva questa opzione.
* `Cursore Rilassa` - Un cursore scorciatoia per rilassare i bordi dei gruppi di facce.
* `Bordi netti` - attiva/disattiva il tentativo di mantenere gli spigoli netti.
* `Riproietta Vertice` - attiva/disattiva la riproiezione della nuova topologia sulla mesh di partenza.
* `Simm` - Attiva un risultato simmetrico. Nota che la simmetria viene sempre calcolata attorno all'asse x del mondo, quindi assicurati che il modello sia nell'origine se vuoi un risultato simmetrico.
* `...` - Popup delle impostazioni di Quad Remesher. 

#### Menu delle impostazioni di Quad Remesher {#quad-remesher-settings-menu}

Il pulsante `...` alla fine della barra in alto apre un popup con le impostazioni rimanenti:

* `Numero quad adattivo` - attiva l'uso di quad più piccoli nelle zone molto curve e di quad più grandi in quelle meno curve.
* `Dimensione adattiva` - Imposta il grado di adattività. Con 100% l'adattività è massima, con 0% i quad sono uniformi.

::: tip

Una ricetta per ottenere un buon remeshing quad con pochi artefatti:

* Dividi la mesh in gruppi di facce per definire il flusso di quad ideale.
* Rilassa i gruppi di facce per ottenere bordi morbidi.
* Decima. Così non avrai facce sottili o distorte sui bordi dei gruppi di facce. Nelle impostazioni di Decima assicurati che i gruppi di facce siano attivi: così gli spigoli dei triangoli seguiranno esattamente i bordi dei gruppi di facce. 

Nelle opzioni del remeshing quad assicurati che Rilassa sia disattivato (dato che hai già rilassato la mesh) e dovresti ottenere buoni risultati.

:::

### ![](/icons/tool_select.webp) Seleziona {#select}
Usa le modalità a forma (`Lazo`, `Rett.`, `Ellisse`) per selezionare oggetti nella scena. `Deseleziona` rimuove oggetti dalla selezione.

### ![](/icons/tool_lattice.webp) Reticolo {#lattice}
Deforma un oggetto con una gabbia di punti di controllo attorno, invece di scolpirne la superficie. Spostando pochi punti della gabbia pieghi, torci o allunghi l'intero oggetto in modo morbido: ottimo per sistemare le proporzioni o mettere in posa senza toccare la topologia. La deformazione resta modificabile finché non la confermi.

La barra a sinistra sceglie come modificare la gabbia:

* `Punti` - Trascina direttamente i punti e gli spigoli della gabbia. Tocca un punto per selezionarlo.
* `Vista` - Muovi la fotocamera senza modificare la gabbia.
* `Rilassa` - Un pennello che rilassa i punti della gabbia sotto di esso.
* `Elastico` - Un pennello che tira i punti della gabbia con un'attenuazione elastica, come lo strumento [Elastico](#elastic).
* `Gizmo` - Sposta, ruota e scala i punti selezionati con il gizmo. La sua modalità Sub è `Pivot`.
* `Lazo` - Seleziona i punti della gabbia con un lazo; `Deseleziona` li rimuove dalla selezione.

Il popup delle forme contiene anche `Raggio morbido`, che fa spostare anche i punti vicini quando trascini un punto (in celle della griglia, 0 sposta solo la selezione), e `Inverti la selezione`.

Una barra in cima al viewport contiene:

* `Conferma` - Applica la deformazione all'oggetto e rimuove la gabbia.
* `Ripristina` - Rimuove la gabbia e la sua deformazione.
* `Opacità` - L'opacità di visualizzazione della gabbia.
* `Lato specchio` - Con la simmetria, passa ciclicamente tra i lati della gabbia mostrati e selezionabili, con una propria `Opacità` per il lato nascosto.
* `Punti della griglia` - Quali punti della gabbia si possono spostare: la griglia completa, la superficie e il punto centrale, oppure solo la superficie.
* `Rigidità` - Quanto è rigida la deformazione, da morbida (0%) a rigida e lineare (100%).
* `Attenuazione` - Quanto la deformazione sfuma al di fuori della gabbia.
* `Allinea` - Allinea la gabbia all'oggetto, oppure al mondo.
* `X`, `Y`, `Z` `Divisione` - Il numero di celle della gabbia su ogni asse. Il pulsante di modalità accanto stabilisce come sono legate: `x = y = z` usa lo stesso numero sui 3 assi, `Uniforme` mantiene la stessa spaziatura tra i punti su ogni asse, e `Personalizzato` ti permette di impostare ogni asse liberamente.

#### Impostazioni di Reticolo {#lattice-settings}
* `Velocità di rollio` - Le stesse opzioni di rollio dello strumento [Sposta](#move-settings), usate quando trascini i punti della gabbia.

### ![](/icons/tool_view.webp) Vista {#view}
Questo "strumento" non fa nulla di particolare: è semplicemente un modo per guardare il modello senza modificare la scena.

#### Impostazioni di Vista {#view-settings}
Mentre lo strumento Vista è attivo, queste impostazioni sostituiscono alcune opzioni di visualizzazione, così puoi avere una vista pulita per presentare o controllare il tuo modello:

* `Primitiva (Modifica)`, `Ripetitore (Modifica)`, `Luce (Modifica)`, `Fotocamera (Modifica)` - Permettono di modificare primitive, ripetitori, luci e fotocamere nel viewport mentre sei nello strumento Vista. Disattivali per evitare di spostarne le maniglie per sbaglio.
* `Scorciatoia fotocamera (sempre)` - Mostra sempre i pulsanti scorciatoia della fotocamera nel viewport.
* `Mostra maschera`, `Bordato`, `Scurisci gli oggetti non selezionati` - Mostra la maschera, il contorno degli oggetti selezionati, o scurisce gli oggetti non selezionati. `Auto` segue la tua impostazione abituale, `No` e `Sì` la forzano.
* `Mostra linea (Simmetria)`, `Mostra piano (Simmetria)` - Mostra la linea o il piano di simmetria, con le stesse scelte `Auto`, `No` e `Sì`.
* `Icona` - Mostra nel viewport le icone di gruppi, ripetitori, luci, fotocamere e la gerarchia, con le stesse scelte.


## Menu contestuale della casella strumenti {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Un clic destro o una pressione prolungata su uno strumento nella casella strumenti apre un menu contestuale. Questo menu ha le seguenti opzioni:

* `Salva` - salva le modifiche che hai fatto allo strumento
* `Clona` - duplica lo strumento in una nuova scorciatoia
* `Ultimo salvataggio` - torna all'ultima versione salvata dello strumento
* `Icona` - cambia l'icona dello strumento. Quando lo strumento ha un'icona personalizzata, questo pulsante la rimuove.
* `→ ...` - sposta lo strumento in un'altra cartella della casella strumenti, o in una nuova
* `Ripristina` - riporta lo strumento alle impostazioni predefinite

Gli strumenti clonati hanno anche `Rinomina` ed `Elimina`.

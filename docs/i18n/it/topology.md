# ![](/icons/multires.webp) Topologia {#topology}

Questo menu controlla la topologia degli oggetti in Nomad, oltre a fornire strumenti per il baking e il trasferimento dei dettagli tra oggetti e tra texture.

![](/images/topology_overview.webp)

Nomad è basato su poligoni, utilizza triangoli e quad per gestire la geometria.
Per topologia si intende sia il numero di facce sia il modo in cui i punti (vertici) sono connessi.

È importante tenere traccia della topologia, soprattutto se si vogliono scolpire o dipingere dettagli fini.

::: tip How to keep track of your topology?
You can display the [Wireframe](settings.md#wireframe) or simply disable [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Il menu Topology di Nomad ha diverse sezioni:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Edit multiple levels of detail using subdivision                 |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Recompute a new topology with uniform density                    |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Add/Remove faces locally in real-time when sculpting or painting |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimation, UVs, baking, remeshing, reprojection                 |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitive options                                                |


## Statistiche poligoni {#polygon-stats}

![](/images/topology_stats.webp)

La sezione superiore del menu Topology mostra le informazioni sui poligoni per l’oggetto selezionato e per l’intera scena. I numeri indicano il numero totale di vertici, il numero totale di triangoli e il numero totale di quad (poligoni a 4 lati).

Toccando questa sezione verrà visualizzato un elenco di statistiche sui poligoni per tutti gli oggetti poligonali nella scena.

## ![](/icons/multires.webp) Multirisoluzione {#multiresolution}

![](/images/topology_multires_menu.webp)

### Che cos’è la multirisoluzione? {#what-is-multiresolution}
La funzione multiresolution è utile in due scenari principali:
- L’algoritmo di smooth subdivision per aumentare il numero di poligoni dell’oggetto
- Gestire più livelli di risoluzione in modo da poter alternare tra modifiche su larga scala e di piccolo dettaglio

![](/videos/multiresolution.mp4)

#### Workflow di multirisoluzione {#multiresolution-workflow}
Un aspetto importante della multiresolution è che è possibile tornare a una risoluzione più bassa, apportare modifiche all’oggetto e poi tornare alla risoluzione più alta senza perdere i dettagli ad alta risoluzione. Tutti i dettagli ad alta risoluzione verranno proiettati automaticamente.

::: warning
Se utilizzi uno strumento che altera la topologia dell’oggetto, perderai tutti gli altri livelli di risoluzione dell’oggetto!
Dovresti sempre ricevere un avviso nel caso ciò stia per accadere, ad esempio quando utilizzi:
- il [Voxel Remesher](#voxel-remesher)
- la [Dynamic Topology](#dynamic-topology)
- il [Trim tool](tools.md#trim)
- lo [Split tool](tools.md#split)
:::


### Cursore multirisoluzione {#multiresolution-slider}
Questo slider indica il numero di livelli di subdivision nell’oggetto corrente. Se ci sono 6 barre verticali, ci sono 6 livelli di subdivision. Il cerchio indica il livello di subdivision attualmente visualizzato. 

### Inverti {#reverse}
Quando ci si trova al livello di subdivision più basso, il pulsante Reverse tenterà di creare un livello al di sotto di quello corrente. Nota che questo in genere è possibile solo se l’oggetto è stato creato con subdivision fin dall’inizio, ad esempio in Nomad o in altre applicazioni 3D che usano superfici di subdivision multiresolution.

### Suddividi {#subdivide}
Il pulsante *Subdivide* aumenterà il numero di poligoni di 4 volte, quindi assicurati di tenere d’occhio il polycount perché può aumentare molto rapidamente!
Un aspetto importante delle *Subdivision Surface* è che convergono verso una *Smooth Surface*.
Per capire come funziona, puoi provare il pulsante *Subdivide* su un oggetto con pochi poligoni.

Puoi disabilitare questo comportamento *Smooth* attivando l’opzione `Linear subdivision`.

### Elimina livelli inferiori {#delete-lower}
Se esistono livelli di subdivision al di sotto di quello attualmente visualizzato, li elimina. Se lo fai per errore, puoi ricrearli con il pulsante Reverse.

### Elimina livelli superiori {#delete-higher}
Se esistono livelli di subdivision al di sopra di quello attualmente visualizzato, li elimina.

### Suddivisione lineare {#linear-subdivision}
Suddivide la mesh senza applicare lo smoothing.

### Bordo netto {#sharp-border}
Se l’oggetto ha dei facegroup, abilitando questa opzione i bordi dei facegroup rimarranno netti. Può essere impostata a ciascun livello di subdivision (lo slider di subdivision avrà una piccola icona sopra il livello per indicarlo).

### Mantieni triangoli {#keep-triangles}
La maggior parte dei sistemi standard di subdivision surface tenterà di convertire tutti i poligoni in quad durante un’operazione di subdivision. Questo toggle forza la subdivision a usare invece triangoli.

### Blocca (LV0) {#lock-lv0}

Impedisce la modifica del livello di subdivision più basso. Può essere importante se l’oggetto è stato generato in un’altra applicazione e l’oggetto base deve rimanere invariato. Quando questa opzione è disabilitata, grandi modifiche fatte ai livelli di subdivision più alti sposteranno il livello 0.

::: tip 

La subdivision per impostazione predefinita ammorbidisce tutti i bordi netti. Per mantenere i bordi leggermente netti, prova a usare la linear subdivision o Sharp border sui primi 2 livelli di subdivision, quindi disattivala per i livelli più alti. Questo creerà una mesh suddivisa semi‑sharp.

:::


## ![](/icons/voxel.webp) Voxel Remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Quando si utilizza il `Voxel Remesher`, l’intera mesh forzerà la topologia ad avere una risoluzione uniforme, il che significa che tutti i poligoni avranno più o meno la stessa dimensione. Questo è molto utile quando non si vuole pensare alla topologia e si desidera semplicemente scolpire in modo libero.

Un tipico workflow di sculpting può iniziare usando il `Voxel Remesher` per bloccare una forma grezza con una bassa risoluzione.
Premi semplicemente il pulsante *Remesh* di tanto in tanto quando stai stirando troppo la mesh per evitare eccessive distorsioni.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Come detto sopra, Nomad è un software poligonale, ma il `Voxel Remesher` è un’eccezione in cui viene usato (temporaneamente) un altro approccio per eseguire il remeshing.

Una grande differenza è che l’approccio voxel non accetta auto‑intersezioni, quindi queste verranno risolte.
Inoltre non supporta mesh con buchi.

Per buchi non si intende il `genus hole` (il `buco` di una ciambella), ma piuttosto mesh che non sono `watertight`/`closed`.
In pratica, ciò significa che prima di applicare il remeshing, tutti i buchi verranno chiusi, in modo simile allo [strumento Trim](tools.md#trim) o alla [funzione Hole filling](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Esegue il voxel remesh.

### Risoluzione {#voxel-resolution}
La dimensione dei voxel usati durante il calcolo. Durante la modifica di questo parametro verrà sovrapposto alla mesh un pattern a scacchiera per dare un’anteprima del risultato.

### Crea multirisoluzione {#build-multiresolution}
Crea livelli di multiresolution inferiori per il voxel remesh. Se utilizzi il pattern a scacchiera per impostare una risoluzione e imposti build multiresolution a 2, il risultato finale avrà un dettaglio che corrisponde allo slider di risoluzione e, se vai nella scheda multires, sarà al livello 2, il che significa che hai mesh multires a risoluzione più bassa ai livelli 1 e 0. Può essere un buon modo per generare sia una mesh pulita con poligoni uniformi, sia una mesh di controllo a bassa risoluzione.

::: tip Tip: Build multiresolution and stable smoothing

Questa opzione a volte può causare “loop” nella geometria che possono essere difficili da lisciare, causando piccoli rigonfiamenti. Se ciò accade, abilita “Stable smoothing” nelle opzioni dello strumento smooth. 

:::

### Mantieni spigoli nitidi {#keep-sharp-edges}
Abilita lo snapping dei nuovi punti ai bordi netti della mesh originale. Può introdurre distorsioni.

## ![](/icons/dynamic.webp) Topologia dinamica {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution e voxel remeshing sono metodi industriali comuni per controllare la topologia, ma entrambi richiedono di fare attenzione a non stirare troppo i poligoni o a non comprimerli troppo.

Dynamic Topology è un metodo alternativo. Durante la scultura, Nomad aggiungerà e rimuoverà in modo adattivo i poligoni durante la pennellata, quindi incidere piccoli dettagli aggiungerà molti piccoli poligoni dove servono, mentre lo smoothing altrove rimuoverà poligoni.

Nota che la dynamic topology utilizzerà poligoni triangolari anziché quad. Questo può sembrare un po’ disordinato, ma è quasi meglio non guardare il wireframe e concentrarsi solo sul creare una scultura dall’aspetto gradevole senza preoccuparsi della topologia, per poi usare in seguito uno degli altri strumenti di remeshing di Nomad per generare una mesh quad pulita.

Vedi il video qui sotto in azione.

![](/videos/dynamic.mp4)

### Abilitato {#enabled}
Attiva la dynamic topology. Un’icona DynTopo verrà posizionata sotto gli slider di raggio e intensità del pennello per consentire di attivare/disattivare la Dyntopo per singolo strumento.

### Dettaglio {#dyn-detail}
Controlla la quantità di dettaglio; il suo comportamento cambia in base alla selezione “Detail based on...”, vedi sotto.

### Dettaglio basato su... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | The level of detail will depend how big the object is on screen. The detail slider is 100% or higher for fine detail, making small triangles, or 1% for low detail, making big triangles.  |
| Radius   | The tool radius defines the amount of detail. Use a small tool radius, for fine detail, a big tool radius for low detail. The detail slider is a multiplier on this ratio.                     |
| Constant | The detail slider defines the amount of detail, and isn't affected by screen size or tool size.             |

::: tip TIP: Radius mode

To get a better sense of how radius mode works, start moving the detail slider with one finger, then at the same time change the tool radius with another finger. You will see how they are linked.

:::

### Preferisci... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Favor performance |
| Quality | Favor quality     |

Quando si favorisce `Quality`, le 2 differenze principali sono:
- il refinement viene applicato prima della scultura, quindi si otterranno meno artefatti di interpolazione quando si dipingono o scolpiscono dettagli molto piccoli
- il refinement viene eseguito finché non converge al livello di dettaglio corretto, in contrasto con un comportamento incrementale.
 
In questo modo, se scolpisci dettagli molto piccoli o fai tratti rapidi, la topologia verrà sempre raffinata come previsto


### Usa pressione sul raggio {#use-pressure-on-radius}
Rilevante solo se `Radius` è attivato. Quando abilitato, il livello di dettaglio rifletterà sempre la dimensione del pennello, anche quando la dimensione del pennello è influenzata dalla pressione della penna.

### Usa attenuazione della pennellata {#use-stroke-falloff}

Include anche la curva di falloff del pennello e l’alpha nei calcoli della dyntopo.

### Metodo {#method}
Sia che tu stia usando la `Dynamic Topology` sul tuo [Brush](#brush) sia [Globalmente](#global), puoi scegliere in quale modalità opererà:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | It can add and remove faces, this is the mode used in the video above |
| Subdivision    | Add new faces only, it cannot remove faces                            |
| Decimation     | Remove faces only, it cannot add new faces                            |

### Proteggi area mascherata {#protect-masked-area}
Abilita la protezione delle aree mascherate in modo che la topologia non venga modificata.

### Estrazione vertici {#vertex-extrapolation}


### Dettaglio {#all-detail}
La risoluzione utilizzata per l’operazione di remesh. Se Dyntopo è in modalità “Constant”, sarà lo stesso valore dello slider Detail nella parte superiore di questo menu.

### Remesh {#dyn-remesh}
Esegue un remesh globale usando l’algoritmo dyntopo. Di solito dovresti usare il [Voxel Remesher](#voxel-remesher) per il remeshing completo.

Tuttavia, un vantaggio rispetto ai voxel è che l’area mascherata sarà protetta, quindi puoi avere un controllo migliore su dove mettere più o meno densità.



## ![](/icons/topo_extra.webp) Varie {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu ingranaggio {#gear-menu}
Molti degli strumenti in questo menu hanno opzioni extra. Sono accessibili tramite l’icona a forma di ingranaggio accanto al titolo della sezione.

### Decimazione {#decimation}

![](/images/topology_decimation.webp)

Riduce il numero di poligoni cercando di mantenere il maggior numero possibile di dettagli, utilizzando poligoni triangolari.

Questa funzione può essere utile se vuoi esportare per la stampa 3D.
Tuttavia probabilmente non dovresti usarla se vuoi continuare a scolpire sull’oggetto, poiché può produrre triangoli irregolari.

Nota che le aree mascherate non verranno decimate.

![](/videos/decimate.mp4)

::: tip

Usare il [Quadremesh tool](tools.md#quad-remesher) su oggetti ad alta densità poligonale può richiedere molto tempo di calcolo e dare risultati difficili da controllare. Pre‑processare la mesh con i [facegroups](tools.md#facegroup-1) e la decimation renderà Quadremesh molto più veloce e permetterà un controllo molto maggiore sulla topologia.

* Crea i facegroup sulla mesh per definire il flusso ideale dei quad.
* Usa Facegroup relax per ottenere bordi dei facegroup più morbidi.
* Esegui la Decimate. Questo assicurerà che non ci siano facce sottili o distorte sul bordo dei facegroup. Nelle impostazioni di decimate assicurati che facegroup sia abilitato. Questo farà sì che i bordi dei triangoli seguano con precisione i bordi dei facegroup.
* Nelle opzioni di Quadremesh assicurati che relax sia disabilitato (dato che hai già rilassato la mesh) e dovresti ottenere buoni risultati.

:::

#### Decima {#decimate}
Avvia l’operazione di decimation.

Le icone accanto al pulsante decimate consentono di attivare/disattivare opzioni che influenzano la decimation. La percentuale indica quanto è forte tale opzione e può essere impostata nel gear menu avanzato.

* ![](/icons/palette.webp)  `Preserve Painting` - Posiziona più triangoli dove ci sono dettagli di pittura.
* ![](/icons/triforce.webp) `Uniform Faces` - Preferisce creare triangoli di dimensioni uniformi.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate cercherà di mantenere invariati i bordi vicino a geometrie aperte e buchi.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate cercherà di mantenere invariati i bordi dei facegroup.
* ![](/icons/uv.webp) `Preserve UV Borders` - Decimate cercherà di mantenere invariati i bordi delle UV.

#### ![](/icons/cog.webp) Menu ingranaggio Decima {#decimate-gear-menu}
Il gear menu contiene queste opzioni avanzate:
##### Preserva pittura {#preserve-painting}
La checkbox attiva/disattiva questa modalità, il valore determina quanto accuratamente verranno preservati i dettagli di pittura. Valori più alti preserveranno più pittura. Imposta a 0 se non ti interessa la pittura.


##### Facce uniformi {#uniform-faces}
La checkbox attiva/disattiva questa modalità. Valori più alti produrranno triangoli di dimensioni simili.

##### Preserva bordi {#preserve-borders}
Abilita per evitare che i bordi vengano decimati. I pesi dei bordi possono essere selezionati per i bordi di `Geometry`, `Face Group` o `UV`.

#### Triangoli target {#target-triangles}
Imposta il numero di triangoli target. Il valore predefinito è 50%; il pulsante percent/target consente di alternare tra una percentuale o un conteggio poligonale esatto.



### Unwrap UV - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Calcola le coordinate di texture (UV) per la mesh corrente, preferendo in generale creare più isole con tagli per minimizzare la distorsione.

La piccola icona a forma di occhio tra il titolo del menu e il gear menu consente di attivare/disattivare l’anteprima delle UV sull’oggetto.

![](/videos/unwrap.mp4)

#### Unwrap {#unwrap}
Calcola le UV per l’oggetto selezionato, che verranno visualizzate sullo sfondo.

#### Elimina UV {#delete-uvs}
Elimina le UV sull’oggetto.

#### ![](/icons/cog.webp) Menu ingranaggio UVAtlas {#uvatlas-gear-menu}
Il gear menu contiene queste opzioni avanzate:

#### Gruppo facce {#atlas-face-group}

Usa i facegroup per definire i tagli delle UV.

##### Stiramento massimo {#max-stretch}
Valori bassi creano meno distorsione e più isole, valori alti creano più distorsione e meno isole. 

##### Spaziatura isole {#island-spacing}
La quantità di padding tra le isole. Valori bassi sprecheranno meno spazio, ma rischieranno che le texture sbavino tra le isole. 

::: warning
Il calcolo delle UV può richiedere del tempo, è meglio avere una mesh con meno di 100k vertici.
:::

::: tip UVs?
Un’analogia comune per le UV è l’incarto di un regalo: qual è il modo migliore di tagliare la carta da regalo per coprire completamente un oggetto, senza sovrapposizioni? 

Le UV sono simili, ma invece di tagliare la carta, tagli l’oggetto. Immagina che il tuo modello sia fatto di plastica sottile: come lo taglieresti per poterlo aprire e stenderlo in piano, dipingerlo in quello stato piatto e poi riassemblarlo?

Ora immagina che la superficie del tuo modello sia fatta di lycra elastica. Potresti stirare il modello fino a renderlo piatto, oppure tagliarlo, o una combinazione di entrambi. Ma se dipingessi una scacchiera sull’oggetto quando è appiattito, la scacchiera sarebbe distorta quando lo riassembli. Qual è il metodo migliore, più tagli con meno distorsione o meno tagli con più distorsione?

Le UV sono istruzioni che dicono al software 3D come “tagliare e stirare” l’oggetto quando si applicano le texture. Lo strumento UV Atlas utilizza in genere un approccio “più tagli, meno distorsione”.


:::

::: tip UV's and Nomad and other apps

Most textured models you find online will be textured with UVs. Nomad can import and display this via the [material](material#textures) panel.

When models are made in Nomad, you can paint directly onto objects without UVs. If you need to export them to other apps, eg [Procreate](https://procreate.art/), you can 'bake' Nomad color information into textures via UVs. 

:::

### Unwrap UV - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Le UV BFF privilegiano un approccio “meno tagli, più distorsione”. 

#### ![](/icons/cog.webp) Menu ingranaggio UV BFF {#uv-bff-gear-menu}

#### Gruppo facce {#bff-face-group}

Usa i facegroup per definire i tagli delle UV.

##### Conteggio coni {#cone-count}
Definisce il numero di proiezioni principali utilizzate. Valori più bassi produrranno meno isole ma più distorsione.

##### Patch senza giunte {#seamless-patches}
Influisce sul layout delle patch UV, funziona meglio con facegroup creati con cura.

### Bake -> texture {#bake-texture}
![](/images/topology_bake_menu.webp)

Il texture baking creerà texture proiettando altri oggetti visibili nella scena nelle UV dell’oggetto selezionato.

Ecco il workflow tipico per il baking:
- Hai una mesh con dettagli fini e pittura
- Clonala
- Esegui la decimation (imposta `Preserve painting` a 0)
- Esegui l’UV unwrap
- Esegui il Bake!

Per impostazione predefinita Nomad prenderà in considerazione tutte le mesh visibili nella scena.
Puoi anche usare la modalità Solo per nascondere rapidamente la maggior parte delle altre mesh.
Se non ci sono altri oggetti visibili, allora verrà presa in considerazione l’intera scena.

Ora dovresti avere una mesh a bassa risoluzione che conserva la maggior parte della pittura e dei dettagli del tuo oggetto precedente.

Dopo l’operazione, i colori dei vertici verranno spostati in un nuovo layer disabilitato, in modo che non interferiscano con le texture.

#### Da se stesso {#tex-from-itself}
Esegue il bake del livello di multiresolution più alto verso il livello più basso sull’oggetto corrente. È semplice da configurare, ma spesso avrai bisogno di più controllo, nel qual caso l’opzione successiva è più utile.

#### Da alta risoluzione () {#tex-from-high-res}
Esegue il bake dagli altri oggetti visibili nella scena verso l’oggetto selezionato. Il numero tra parentesi indica il numero di altri oggetti visibili che verranno usati come target high‑res e “baked” nell’oggetto low‑res corrente con UV. Gli altri oggetti non devono essere simili per layout o topologia all’oggetto su cui si esegue il bake, consentendo workflow di bake versatili.

#### Risoluzione {#tex-bake-resolution}
La risoluzione della texture di bake. Le texture di bake sono sempre quadrate, quindi 1024 creerà un’immagine 1024x1024. 

I pulsanti sottostanti sono scorciatoie per risoluzioni comunemente usate. Per riferimento, 512x512 è relativamente piccola, ad esempio per grafica web e geometria semplice. 4096x4096 (4k in breve) è per render di alta qualità.

#### ![](/icons/cog.webp) Menu ingranaggio Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Il gear menu contiene queste opzioni avanzate:

##### Normale, Rugosità, Metallicità, Colore, Emissivo, Opacità {#tex-normal-roughness-metalness-color-emissive-opacity}
Queste checkbox determinano quali proprietà verranno “baked”, ciascuna in mappe separate. Dopo il completamento del bake, verranno aggiunte come texture al materiale dell’oggetto corrente.

##### Backup {#tex-backup}
Per visualizzare in anteprima le texture di bake, le informazioni di pittura dell’oggetto devono essere disabilitate. Questa opzione trasferirà qualsiasi informazione di pittura in un nuovo layer come backup, in modo che possa essere facilmente abilitata/disabilitata.

#### Raggio gabbia {#tex-cage-radius}
Regola la distanza dalla quale, rispetto all’oggetto di bake, vengono inviati i raggi per cercare gli oggetti target. Per impostazione predefinita questa distanza è mantenuta bassa per evitare artefatti, ma può essere aumentata se gli oggetti target sono lontani dall’oggetto di bake.

##### Offset raggio {#tex-ray-offset}
Regola il punto da cui iniziano i calcoli di bake sull’oggetto di bake. Per impostazione predefinita iniziano al 5% di distanza dalla superficie, il che evita la maggior parte degli artefatti comuni. Se gli oggetti target sono molto lontani dall’oggetto di bake, questo offset potrebbe dover essere aumentato.


### Riproietta su vertici {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Proietta dettagli scolpiti, pittura, layer, texture nei valori dei vertici.

Può essere considerato l’inverso del baking; se il baking trasferisce le proprietà dei vertici alle texture, la reprojection trasferisce le texture (e altre proprietà)
 di nuovo ai vertici.

::: tip
Quando si utilizza `Bake to texture` o `Reproject to vertex`, sia i colori dei vertici sia le texture del materiale verranno presi in considerazione.
:::

#### Da se stesso {#vertex-from-itself}
Converte le texture del materiale in valori dei vertici. Questo pulsante sarà attivo solo se l’oggetto ha UV e le texture sono attive nel materiale.

::: tip TIP: Texture painting
Nomad non supporta direttamente la pittura e la modifica delle texture, ma si possono ottenere risultati molto simili proiettando texture -> valori dei vertici, dipingendo sui vertici, quindi eseguendo il bake vertici -> texture:

1. Imposta un oggetto low‑poly con UV
1. Carica le texture nel suo materiale
1. Suddividilo a sufficienza per poter dipingere
1. Esegui `Reproject to vertex` in modalità `From itself`, ora la texture è stata convertita in valori dei vertici
1. Dipingi, liscia, sfuma, timbra, fai tutte le modifiche che ti servono
1. Esegui `Bake to texture`, in modalità `From itself`. Queste modifiche vengono convertite nuovamente in texture.
:::

#### Da alta risoluzione () {#vertex-from-high-res}
Converte qualsiasi oggetto visibile in valori dei vertici sull’oggetto selezionato. Il numero su questo pulsante indica il numero di oggetti visibili.

::: tip
La reprojection di altri oggetti può essere usata non solo per trasferire informazioni di colore da altri oggetti, ma anche per proiettare vertici su altri oggetti, ad esempio bende che possono essere proiettate su un personaggio.
:::

#### ![](/icons/cog.webp) Menu ingranaggio Riproiezione {#vertex-reproject-gear-menu}
Il gear menu contiene queste opzioni avanzate:

#### Vertici, Rugosità, Metallicità, Colore, Opacità, Opacità->Maschera, Maschera, Layer, Gruppo facce {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Queste checkbox determinano quali proprietà verranno proiettate sull’oggetto selezionato. 

#### Rilassa {#vertex-relax}
La mesh selezionata può avere il suo layout ammorbidito o rilassato in una certa misura per adattarsi meglio ai target di reprojection. Smooth è migliore per mesh ad alta densità poligonale. Relax è migliore per mesh a bassa densità. Auto lascerà che sia Nomad a determinare il metodo migliore.

#### Iterazioni {#vertex-iterations}
Quante volte l’operazione di relax deve essere applicata durante la reprojection.

#### Raggio gabbia {#vertex-cage-radius}
Regola la distanza dalla quale, rispetto all’oggetto selezionato, vengono inviati i raggi per cercare gli oggetti target. Per impostazione predefinita questa distanza è mantenuta bassa per evitare artefatti, ma può essere aumentata se gli oggetti target sono lontani dall’oggetto di bake.

#### Bias raggio {#vertex-ray-bias}
Valori più bassi favoriranno la proiezione verso il punto più vicino sulla superficie target. Valori più alti favoriranno un punto di intersezione usando la normale della superficie. 

#### Offset raggio {#ray-vertex-offset}
Regola il punto da cui iniziano i calcoli di bake sull’oggetto selezionato. Per impostazione predefinita iniziano al 5% di distanza dalla superficie, il che evita alcuni artefatti. Se gli oggetti target sono molto lontani dall’oggetto selezionato, questo offset potrebbe dover essere aumentato.


### Quad Remesh - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Esegue il remesh usando l’[algoritmo Instant Meshes di Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analizza il flusso di una mesh e crea una topologia quad pulita.

::: tip
Su iOS e desktop, lo strumento [Quad remesher](tools#quad-remesher) offre risultati migliori e più controllo.
:::

#### Remesh {#instant-remesh}
Avvia l’operazione Instant Meshes.

#### Quad target {#target-quads}
Il numero di poligoni quad che Quad Remesh tenterà di creare.

#### ![](/icons/cog.webp) Menu ingranaggio Quad Remesh Instant {#quad-remesh-instant-gear-menu}
Il gear menu contiene queste opzioni avanzate:

##### Angolo crease {#crease-angle}
Una soglia per gli angoli netti che cercherà di aiutare a guidare l’operazione di remesh.

#### Riempimento max buchi {#max-fill-hole}
L’algoritmo a volte può produrre buchi indesiderati. Se un buco ha meno vertici di questo valore, verrà riempito.

### Buchi {#holes}
![](/images/topology_holes_menu.webp)
La maggior parte delle volte il tuo oggetto sarà probabilmente watertight, il che significa che la mesh è “chiusa”.

Se l’oggetto ha buchi, puoi riempirli. Nota che funziona solo su buchi “ingenui”, quindi non può “saldare” due bordi separati.

![](/videos/hole_filling.mp4)

::: tip
Quando esegui il Voxel remesher, tutti i buchi vengono chiusi automaticamente, sia che tu lo stia usando su una o più mesh.
:::

#### Chiudi buchi {#close-holes}
Esegue l’azione di chiusura dei buchi.

#### ![](/icons/cog.webp) Menu ingranaggio Buchi {#holes-gear-menu}
Il gear menu contiene queste opzioni avanzate:

##### Dettaglio {#fill-detail}
La densità di poligoni usata per riempire il buco. Durante il trascinamento di questo slider verrà mostrato un pattern a scacchiera sul modello, che darà un’indicazione della dimensione dei triangoli da usare. La checkbox disabiliterà questo comportamento e userà solo i punti esistenti, il che di solito creerà triangoli lunghi e sottili sopra il buco, difficili da scolpire.

##### Riempimento non-manifold {#fill-non-manifold}
Tenta di riempire buchi non manifold.

##### Gruppo facce {#fill-face-group}

Quando si riempiono i buchi, ogni buco deve ottenere il proprio facegroup (Auto), oppure devono condividerne uno solo (Off), o non creare facegroup (On).

### Forza manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Tenta di pulire gli edge non manifold. Può essere utile per software esterni che non supportano edge con più di 2 facce in comune.

#### Pulisci {#clean}
Esegue l’azione di pulizia.
#### ![](/icons/cog.webp) Menu ingranaggio Forza manifold {#force-manifold-gear-menu}
Il gear menu contiene queste opzioni avanzate:

#### Elimina facce piccole {#delete-small-faces}
Una soglia usata per rimuovere e unire poligoni piccoli.


### Triplanare {#triplanar}
![](/images/topology_triplanar_menu.webp)
Converte la mesh in una primitiva [triplanar](scene.md#triplanar).
Probabilmente perderai molti dettagli nel processo.

#### Forza cubico {#force-cubic}
Forza il triplanar a essere un cubo. In caso contrario il triplanar si adatterà al bounding box più vicino attorno all’oggetto.

#### Converti {#convert}
Esegue l’azione triplanar.

#### Risoluzione {#triplanar-resolution}
La dimensione dei voxel usata nell’operazione triplanar.

## ![](/icons/dot.webp) Primitiva {#primitive}
Parametri per la primitiva selezionata. Sono disponibili anche nella toolbar della viewport delle primitive.

![](/images/topology_primitive_screenshot.webp)
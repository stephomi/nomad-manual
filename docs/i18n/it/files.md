# ![](/icons/open.webp) File {#files}

Il menu File ti permette di salvare e caricare i progetti Nomad, importare ed esportare modelli 3d, esportare immagini renderizzate e collegare Nomad ad altre app. Ha tre schede: `File`, `Renderizza` e `Collegamento`.

![](/images/file_menu.webp)

## Progetto {#project}
![](/images/file_project.webp)

La miniatura in alto mostra il progetto corrente, con accanto la dimensione del file, il salvataggio automatico e la cronologia salvata. Tocca la miniatura per aprire un piccolo browser dei tuoi progetti, poi tocca un progetto per avere un menu che permette di aprirlo, aggiungerlo, sovrascriverlo, duplicarlo, rinominarlo o eliminarlo.

Quando il progetto ha modifiche non ancora salvate, sotto la miniatura compare `Vi sono modifiche non salvate!`.

### Ambito {#scope}
Su desktop, scegli dove vengono salvati i tuoi progetti:
* `Interno` - l'opzione predefinita, come su mobile. I progetti vengono salvati solo all'interno della cartella principale di Nomad.
* `Sul posto` - quando apri un progetto che si trova fuori dalla cartella di Nomad, il salvataggio sovrascrive il file originale. Il salvataggio automatico non funziona per questi progetti esterni.

### ![](/icons/nomad.webp) Preset {#preset}
Accedi a una raccolta di demo e di componenti per personaggi. Selezionane uno, poi selezionalo di nuovo per scegliere se `Apri` o `Aggiungi alla scena`. Da questo browser puoi anche scaricare modelli gratuiti da Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Cronologia... {#history}
Accesso rapido alle opzioni di cronologia del progetto, come `Salva cronologia`, che conserva la cronologia degli annullamenti quando il progetto viene salvato. Un badge verde sul pulsante indica che la cronologia viene salvata con il progetto. Vedi [Cronologia](history.md#save-history) per i dettagli.

### ![](/icons/save.webp) Salva {#save}
Salva il progetto Nomad. Se il progetto non è mai stato salvato, ti verrà chiesto un nome.

### ![](/icons/save_as.webp) Salva come... {#save-as}
Salva il progetto con un nuovo nome, come nuovo progetto.

### ![](/icons/save_as.webp) Sovrascrivere... {#overwrite}
Mostra il browser dei progetti per salvare la scena corrente al posto di un altro progetto. Attiva `Includi solo oggetti selezionati` per salvare solo gli oggetti selezionati invece dell'intera scena. Il browser ha anche un pulsante `Salva come...` per salvare invece come nuovo progetto.

### ![](/icons/pencil.webp) Rinomina {#rename}
Mostra una casella di testo per rinominare il progetto corrente.

### ![](/icons/open.webp) Apri... {#open}
Mostra il browser dei progetti per aprire un progetto.

### ![](/icons/add_file.webp) Aggiungi alla scena... {#add}
Mostra il browser dei progetti: quando selezioni un progetto, il suo contenuto viene unito alla scena corrente.

### ![](/icons/trash.webp) Elimina... {#delete}
Mostra il browser dei progetti: i progetti selezionati vengono eliminati dal file system.

### ![](/icons/new_file.webp) Nuovo {#new}
Inizia un nuovo progetto; se ci sono modifiche non salvate, ti verrà chiesto di confermare. La conferma ti permette di `Mantieni` o `Ripristina` le impostazioni `Sfondo`, `Ambiente`, `MatCap` e `Raggi X`, e di scegliere se il nuovo progetto usa `Salva cronologia`.

### ![](/icons/autosave.webp) Salvataggio automatico... {#auto-save}
Menu delle opzioni di salvataggio automatico. Attiva `Salvataggio automatico` per salvare il progetto in un file separato a intervalli regolari. Il badge sul pulsante mostra se è attivo.

Nomad non salva in background perché i file 3d possono essere piuttosto pesanti, e questo potrebbe causare rallentamenti notevoli mentre scolpisci.

Inoltre, per evitare problemi di memoria insufficiente, di solito la scena viene compressa prima del salvataggio.
Anche questa compressione/decompressione rallenta il salvataggio.

### Intervallo di salvataggio {#timer-pop-up}
Quanti minuti Nomad aspetta tra un salvataggio automatico e l'altro.

### Mostra conto alla rovescia {#popup-timeout}
Mostra un conto alla rovescia prima di ogni salvataggio automatico, così puoi annullarlo se sei nel bel mezzo di qualcosa. Se disattivato, Nomad salva appena smetti di scolpire.

### ![](/icons/trash.webp) Scarta salvataggio automatico {#discard-autosave}
Se esiste un file di salvataggio automatico per un progetto, viene caricato automaticamente al posto del progetto originale. Se non ti serve, questo pulsante elimina il salvataggio automatico. Aprendo il file verrà quindi caricato l'ultimo salvataggio manuale del progetto.

### ![](/icons/open.webp) Apri il salvataggio obsoleto {#open-outdated-save}
Quando un progetto ha sia un salvataggio automatico sia un salvataggio manuale, questo pulsante apre il più vecchio dei due (`Apri il salvataggio automatico obsoleto` o `Apri il salvataggio manuale obsoleto`), con la sua data. Comodo se l'ultimo salvataggio non è quello che volevi.

### ![](/icons/storage.webp) Eliminati di recente... {#recently-deleted}
Nomad conserva per un certo numero di giorni i dati dei progetti usciti dalla cartella dei progetti e i file sostituiti da un'importazione, prima di eliminarli definitivamente. I file la cui importazione non è riuscita restano finché non li elimini tu. Questo elenco li mostra con dimensione e data, così puoi eliminarli uno per uno oppure con `Elimina tutto`.

## Importa {#import}

### ![](/icons/add_file.webp) Importa {#import-button}
Per importare file 3d che non sono progetti Nomad.

Quando importi in Nomad un file di scena esterno, puoi *aggiungerlo* oppure iniziare con esso un *nuovo* progetto.

Aggiungere un file inserisce semplicemente gli oggetti nella scena corrente.
Scegliendo `Nuovo` crei un nuovo progetto Nomad che contiene i nuovi oggetti.

La finestra di importazione elenca ogni file che hai scelto, con le sue opzioni di importazione. Anche le immagini si possono importare così: scegli per ciascuna se diventa un `HDRI`, un `MatCap`, un `Riferimento`, un `Alfa`, delle `Texture` o un `VDM`.

Nomad può importare questi formati:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), sulle piattaforme che lo supportano

### ![](/icons/cog.webp) Impostazioni {#advanced}
Il pulsante `Impostazioni...` accanto alla miniatura del progetto mostra le principali opzioni di importazione. Queste impostazioni non vengono salvate, e la finestra di importazione mostra le opzioni che valgono per i file che stai importando.

### Tutti i formati {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Mantieni topologia {#keep-topology}
Di base Nomad cerca di correggere le geometrie problematiche al caricamento. Attivando questa opzione, Nomad non riordina vertici e facce, non unisce i duplicati e non rimuove i vertici inutilizzati.

::: warning
Con `Mantieni topologia`, operazioni come booleana, unione, decimazione o manifold potrebbero non unire i vertici duplicati.
:::

#### ![](/icons/image.webp) Ignora texture {#skip-textures}
Non carica le texture incorporate nel file, per i formati che lo supportano come glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Carica impostazioni UI {#keep-gui-settings}
Quando apri o importi un file di progetto, carica tutte le impostazioni dell'interfaccia salvate al suo interno.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Dividi OBJ per gruppi {#split-obj-by-groups}
Divide i gruppi OBJ in oggetti separati.

#### ![](/icons/vertex.webp) Unisci posizioni duplicate {#merge-duplicate-positions}
Unisce i vertici che hanno la stessa posizione.

#### ![](/icons/uv.webp) Unisci UV duplicati {#merge-duplicate-uvs}
Unisce le coordinate texture che hanno gli stessi UV.

#### ![](/icons/paint.webp) Spazio colore {#color-space}
Imposta come interpretare i colori del file: `Auto`, `Lineare` o `sRGB`. Prova a cambiare questa opzione se i colori sembrano sbagliati.

#### ![](/icons/image.webp) Formato {#normal-format}
Il formato delle normal map delle texture: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`. Prova l'altro se i dettagli della normal map sembrano invertiti.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Spazio colore {#color-space-ply}
Imposta come interpretare i colori del file: `Auto`, `Lineare` o `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Unisci UV duplicati {#merge-duplicate-uvs-fbx}
Unisce le coordinate texture che hanno gli stessi UV.

#### ![](/icons/paint.webp) Spazio colore {#color-space-fbx}
Imposta come interpretare i colori del file: `Auto`, `Lineare` o `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-fbx}
Il formato delle normal map delle texture: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Spazio colore {#color-space-usd}
Imposta come interpretare i colori del file: `Auto`, `Lineare` o `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-usd}
Il formato delle normal map delle texture: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`.



## Esporta {#export}
Salva in un formato di geometria 3d utilizzabile in altri software.

![](/images/file_export.webp)

I vari formati di file supportano funzionalità diverse: le opzioni disponibili cambiano in base al tipo di file selezionato.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Colori dei vertici](#vertex-colors) | ✅ | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR dei vertici](#pbr-paint)   | ✅     | Nomad ✅<br>Altri ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Altri ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Livelli](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Oggetti                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Gruppo di facce                 | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Gerarchia                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Luci                            | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texture                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitive, post processing, ecc. | ✅    | Nomad ✅<br>Altri ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Pulsante Esporta {#export-button}
Tocca qui per esportare la geometria con le impostazioni selezionate. Il pulsante mostra il formato selezionato e una stima della dimensione del file. Su Android, un pulsante `Condividi` accanto invia il file direttamente a un'altra app.

### Formato file {#file-format}
Scegli il formato di esportazione: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` o `USD`. NOMAD è il formato di Nomad: non si apre in altri software, quindi serve soprattutto per reimportare in Nomad.

### Includi {#allvisibleselected}
Scegli quali oggetti esportare: `Tutti`, `Visibile` o `Selezionati`. Il numero accanto a ogni opzione indica quanti oggetti verranno esportati.

### Un file per oggetto {#one-file-per-object}
Esporta ogni oggetto in un file a sé. Il numero indica quanti file verranno scritti.

### Tipo {#type}
Quando l'esportazione scrive più file (un file per oggetto, o un OBJ con texture), salvali in una `Cartella` o in uno `Zip`. Alcune app (Google Drive, One Drive, ecc.) non supportano l'importazione di cartelle: in quel caso usa Zip.

### Incorpora cronologia {#embed-history}
Solo NOMAD. Include nel file la cronologia degli annullamenti, che viene ripristinata quando apri il file in Nomad. Aumenta la dimensione del file e richiede di esportare l'intera scena in un unico file.

### Incorpora risorse {#embed-assets}
Solo NOMAD. Include nel file i tuoi matcap, ambienti e font personalizzati. Le risorse integrate non vengono incorporate.

### Colori dei vertici {#vertex-colors}
Esporta i colori dei vertici, se il formato di file li supporta. Alcuni software 3d sanno leggerli, ma non tutti.

Per OBJ puoi scegliere:
* `Nessuno` - nessun colore.
* `RGB` - i colori vengono aggiunti dopo i vertici.
* `MRGB (ZBrush)` - un altro modo di codificare il colore, che supporta anche i dati della maschera.

### Spazio colore {#color-space-export}
Solo OBJ, con i colori dei vertici `RGB`. Scrive i colori in `Lineare` o in `sRGB`.

### Pittura PBR {#pbr-paint}
Esporta la pittura di rugosità, metallicità e maschera. Altri software potrebbero ignorare questi dati.
I colori dei vertici PBR vengono esportati come attributi secondari di colore dei vertici.
I canali sono organizzati così:

|           | Canale   |
| :-------: | :------: |
| Rugosità  | R        |
| Metallicità | G      |
| Maschera  | B        |


### Livelli {#layers}
I livelli sono supportati tramite i morph target di glTF. glTF li supporta ufficialmente, quindi dovrebbero funzionare anche in altri software.
Nomad esporta anche i colori, la rugosità e la metallicità di ciascun livello, ma gli altri software li ignorano.

### Pittura dei livelli {#layer-painting}
Esporta la pittura dei livelli, di solito ignorata dagli altri software.

### Gruppo di facce {#face-group}
Esporta i gruppi di facce; a volte l'esportazione può creare problemi con altri software.

### Scrivi oggetti {#write-objects}
Solo OBJ. Mantiene gli oggetti separati. Disattivalo per esportare tutto come un unico oggetto, per esempio per usare la funzione 'Mesh ID / Polygroup' di Substance Painter.

### Normali {#normals}
Esporta le informazioni sulle normali. Nota che Nomad calcola sempre le proprie normali quando importa altri formati di file.

### Tangenti {#tangents}
Esporta le informazioni sulle tangenti, usate se il modello ha delle normal map.

### Texture {#textures}
Se al materiale sono state aggiunte delle texture, vengono esportate. Nota che questo non effettua il bake delle texture: quello si fa con le opzioni di trasferimento nella topologia.

### Formato {#fbx-format}
Solo FBX. `Binario` è più leggero ma potrebbe non funzionare in tutte le applicazioni, `ASCII` è un file di testo.

### Compresso {#compressed}
Solo FBX. Riduce la dimensione del file, al prezzo di un'esportazione e di un'importazione più lente.

### Preset {#usd-preset}
Solo USD. Scegli l'app per cui stai esportando: `OpenUSD`, `Apple`, `Procreate` o `Zbrush`. Alcune opzioni sono disponibili solo con alcuni preset.

### Istanza {#instance}
Solo USD. Esporta gli oggetti istanziati come istanze, invece di duplicarne la geometria.

### Permetti distorsione {#allow-skew}
Solo USD. Permette la distorsione (skew) nelle trasformazioni delle matrici. Se disattivato, Nomad scompone le trasformazioni distorte in trasformazioni separate di scala e di rotazione.

### Ripetitore {#repeater}
Solo USD. Esporta le copie create dai ripetitori come istanze.

### Unisci copie {#join-copies}
Ogni oggetto e le sue copie del ripetitore diventano un unico oggetto.

::: tip Consiglio: importare rugosità e metallicità in Blender

Blender può importare glTF/glb, ma non interpreta automaticamente gli attributi dei vertici per metallicità e rugosità. Per usarli, nell'editor dei materiali crea un nodo Vertex Color e imposta la sua proprietà sull'attributo di colore successivo (di solito Col.001). Collega un nodo 'Separate XYZ', manda X a Roughness e Y a Metallic.

Questo video mostra il procedimento:

![](/videos/blender_pbr.mp4)

::: 

::: tip Consiglio: funzionalità supportate da USD

USD è un formato complesso: le sue specifiche supportano molte funzionalità, ma non tutti i software 3d le gestiscono. OSX/iOS per esempio non supportano i colori dei vertici. I preset dell'esportatore USD cercano la migliore compatibilità possibile con OpenUSD, Apple, Procreate e Zbrush.

::: 

## ![](/icons/screen.webp) Renderizza {#render}

Esporta un'immagine che combina tutte le impostazioni del progetto (luci, materiali, post processing, ecc.).

![](/images/file_render.webp)
### ![](/icons/preview.webp) Anteprima {#preview}

Il pulsante `Anteprima` accanto al titolo del menu rende l'interfaccia trasparente, per aiutarti a valutare l'inquadratura del risultato finale.

### ![](/icons/home.webp) Fuoco {#focus}
Inquadra la scena o la selezione in modo che stia nelle dimensioni del render. Tocca di nuovo per passare dall'una all'altra.

### ![](/icons/map.webp) Heightmap {#heightmap}
Renderizza la scena come una mappa di altezza in scala di grigi vista dalla fotocamera, dove le parti più vicine sono le più chiare. Attivandola si passa a una dimensione `Quadrato` e si inquadra la selezione. Una piccola barra nella vista ti permette di regolare il `Fuoco` del gradiente.

Quando `Heightmap` è attiva, accanto al pulsante di esportazione compare un pulsante `Salva come alfa`, per salvare il render come nuovo alfa del pennello invece di esportare un file.

### ![](/icons/opacity.webp) Sfondo trasparente {#transparent-background}
Aggiunge un canale alfa al render, utile per combinarlo con altre immagini nei programmi 2d. Nota che la trasparenza parziale non è supportata.

### ![](/icons/sliders.webp) Mostra interfaccia {#show-interface}
Include l'interfaccia di Nomad nel render.

### Dimensione finale {#final-size}
La risoluzione del render: `Schermo`, `720`, `1080`, `4096`, `Quadrato` o `Personalizzata`.

Quando il menu File è attivo, nella vista viene disegnato un contorno tratteggiato che indica l'area del render, se non corrisponde alla risoluzione dello schermo.

### Larghezza / Altezza {#render-ratio}
Con `Personalizzata`, imposta la larghezza e l'altezza dell'immagine. Il pulsante di collegamento tra i due cursori mantiene le proporzioni quando ne modifichi uno. Con `Quadrato` si può impostare solo la larghezza.

### ![](/icons/export.webp) Esporta → PNG {#export-png}
Tocca questo pulsante per avviare il render. Al termine puoi scegliere come salvare o condividere l'immagine. Per dimensioni molto grandi viene chiesta prima una conferma: salva il progetto prima, nel caso il dispositivo esaurisca la memoria.

## ![](/icons/network.webp) Collegamento {#link}

Collega Nomad a un altro dispositivo o a un'altra app, per inviare e ricevere oggetti o per sincronizzare le modifiche in tempo reale. Un dispositivo ospita la sessione, gli altri si uniscono.

### Abilita GoZ {#enable-goz}
Solo desktop. Scambia mesh con ZBrush sullo stesso computer. `Invia` le importa in ZBrush, `Ottieni` importa da ZBrush in esecuzione: `Selezione` prende il subtool attivo, `Scena` prende tutti i subtool. Puoi anche premere GoZ in ZBrush in qualsiasi momento.

### Modalità {#link-mode}
* `Disattivato` - nessun collegamento.
* `Host` - questo dispositivo ospita la sessione e aspetta che gli altri si uniscano.
* `Partecipa` - cerca i dispositivi vicini, poi tocca il nome dell'host per unirti.

Per collegare due Nomad, scegli `Host` su un dispositivo e `Partecipa` sugli altri. Per collegarti a Blender, Nomad deve essere l'host: il pulsante di aiuto accanto al titolo `Collegamento` mostra come installare l'estensione Nomad Blender Link.

### ![](/icons/network.webp) Porta di rete {#network-port}
La porta di rete usata dal collegamento. Cambiala solo se un'altra app la sta già usando.

### Invia / Ottieni {#send-get}
Una volta connesso, puoi `Invia` la tua `Selezione` o l'intera `Scena` all'altro dispositivo, oppure `Ottieni` da esso. `Sostituisci` elimina la scena corrente, poi ottiene la scena dell'altro dispositivo.

### ![](/icons/link.webp) Sincronizzazione in tempo reale {#live-sync}
Trasmette le tue modifiche all'altro dispositivo mentre lavori. `Vista di lavoro` sincronizza anche la fotocamera. `Modifiche alla scena` imposta quale dispositivo invia le modifiche: `Auto` dà la direzione all'attività più recente. Poi scegli cosa sincronizzare: `Oggetti e geometria`, `Materiali`, `Luci`, `Fotocamere` e, quando l'altro lato lo supporta, `Shading` e `Post processing`.

::: tip
Gli oggetti esistenti hanno bisogno prima di un `Invia` o di un `Ottieni`, per collegarli prima che la sincronizzazione in tempo reale possa aggiornarli.
:::

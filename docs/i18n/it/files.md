# ![](/icons/open.webp) File

Il menu File consente di salvare e caricare progetti Nomad, importare ed esportare modelli 3D ed esportare immagini renderizzate.

![](/images/file_menu.webp)

## Progetto
![](/images/file_project.webp)

Nella parte superiore di questo menu viene mostrata una miniatura dell’ultimo salvataggio. Facendo clic su questa miniatura si apre un mini browser; tocca due volte un altro progetto per far apparire un mini menu che permette di aprire, aggiungere, salvare, clonare, rinominare o eliminare quel progetto.

### ![](/icons/nomad.webp) Preset 
Accedi a una raccolta di demo e componenti di personaggi. Selezionane uno, poi selezionalo di nuovo per scegliere se Aprire, Aggiungere alla scena o Clonare l’elemento nella cartella dei tuoi progetti.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Salva
Salva il progetto Nomad.

### ![](/icons/save_as.webp) Salva con nome...
Mostra il browser dei progetti per consentirti di salvare il progetto Nomad con un nuovo nome.

### ![](/icons/pencil.webp) Rinomina
Mostra una casella di testo per rinominare il progetto corrente.

### ![](/icons/open.webp) Apri...
Mostra il browser dei progetti per aprire un progetto.

### ![](/icons/add_file.webp) Aggiungi alla scena...
Mostra il browser dei progetti; quando un progetto viene selezionato, il suo contenuto verrà unito con la scena corrente.

### ![](/icons/trash.webp) Elimina...
Mostra il browser dei progetti; tutti i progetti selezionati verranno eliminati dal file system.

### ![](/icons/new_file.webp) Nuovo
Avvia un nuovo progetto; se ci sono modifiche non salvate ti verrà chiesto se desideri salvarle.

### ![](/icons/autosave.webp) Salvataggio automatico...
Menu per controllare le opzioni di salvataggio automatico.

Se abiliti il salvataggio automatico, puoi impostare un timer in modo che un popup appaia a intervalli regolari.
Il motivo per cui Nomad non salva in background è che i file 3D possono essere piuttosto grandi e questo può causare un notevole rallentamento mentre stai scolpendo.

Inoltre, per evitare problemi di memoria insufficiente, la scena viene in genere compressa prima dell’operazione di salvataggio.
Questa compressione/decompressione rallenterà anche l’operazione di salvataggio.

### Timer pop up
Con quale frequenza apparirà il popup del timer.

### Timeout popup
Abilita il timeout del popup.

### Scarta autosalvataggio
Se esiste un file di autosalvataggio per un progetto, verrà caricato automaticamente al posto del progetto originale. Se questo non è necessario, questo pulsante eliminerà l’autosalvataggio. Il caricamento del file utilizzerà quindi l’ultimo salvataggio manuale del progetto.


## Importa

### ![](/icons/add_file.webp) Importa
Per importare file 3D che non sono progetti Nomad.

Quando importi un file di scena esterno in Nomad, puoi *importarlo* oppure *aggiungerlo*.

Aggiungere un file semplicemente aggiungerà gli oggetti alla scena corrente.
Importare un file creerà un nuovo progetto Nomad con i nuovi oggetti al suo interno.

Nomad può importare questi formati:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, sperimentale)

### ![](/icons/cog.webp) Avanzate
Mostra le opzioni avanzate di importazione:

### Progetto/ glTF / OBJ / STL / FBX
#### Mantieni topologia
Per impostazione predefinita Nomad tenterà di correggere la geometria problematica in fase di caricamento. Abilitando questa opzione si impedirà a Nomad di riordinare vertici/facce, rimuovere duplicati di vertici/facce, rimuovere vertici non utilizzati.

#### Salta texture
Salta il caricamento delle texture per i formati che le supportano, come glTF.

### Progetto / glTF
#### Mantieni impostazioni GUI
Abilita il salvataggio dell’interfaccia grafica e delle impostazioni del progetto all’interno del file Nomad .nom o glTF.

### OBJ
#### Dividi OBJ per gruppi
Abilita la suddivisione dei gruppi OBJ in oggetti separati.

#### Spazio colore
Imposta la modalità colore interpretata dall’OBJ come Lineare, sRGB o Auto.

### PLY
#### Spazio colore
Imposta la modalità colore interpretata dal PLY come Lineare, sRGB o Auto.


### FBX
#### Spazio colore
Imposta la modalità colore interpretata dall’OBJ come Lineare, sRGB o Auto.



## Esporta
Salva in un formato di geometria 3D che può essere utilizzato in altri software. 

![](/images/file_export.webp)

Formati di file diversi supportano funzionalità differenti; le opzioni disponibili cambieranno in base al tipo di file selezionato.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, ecc.  | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Tutti/Visibili/Selezionati
Lo stato attivo del pulsante imposta quali oggetti verranno esportati. Il numero accanto alle icone indica quanti oggetti verranno esportati per quella opzione.

### Colori per vertice
Esporta i colori per vertice se supportati dal formato di file.

### PBR Paint
I colori PBR per vertice vengono esportati come attributi secondari di colori per vertice.
I canali sono impacchettati nel modo seguente:

|           | Canale  |
| :-------: | :-----: |
| Roughness | R       |
| Metalness | G       |
| Masking   | B       |


### Livelli
I livelli sono supportati tramite i morph target glTF.
Nomad esporta anche colori, roughness e metalness per livello, ma verranno ignorati da altri software.

### Pittura livelli
Esporta la pittura dei livelli, solitamente ignorata da altri software.

### Face Group
Esporta i facegroup; l’esportazione può talvolta interferire con altri software.

### Normali
Esporta le informazioni sulle normali. Nota che Nomad calcolerà sempre le proprie normali quando importa altri formati di file.

### Tangenti
Esporta le informazioni sulle tangenti, utilizzate se il modello ha normal map. 

### Texture
Se sono state aggiunte texture al materiale, verranno esportate. Nota che questo non effettuerà il baking delle texture, che viene invece eseguito tramite le opzioni di baking nella sezione topologia.

### Pulsante Esporta
Fai clic qui per esportare la geometria utilizzando le impostazioni selezionate.

::: tip Suggerimento: importa roughness e metalness in Blender

Blender può importare glTF/glb, ma non interpreta automaticamente gli attributi per vertice per metalness e roughness. Per usarli, nell’editor dei materiali crea un nodo Vertex Color, imposta la sua proprietà sul successivo attributo colore (di solito Col.001). Collega un nodo “Separate XYZ”, invia X alla roughness e Y al Metallic.

Questo video mostra il procedimento:

![](/videos/blender_pbr.mp4)

::: 

::: tip Suggerimento: supporto delle funzionalità USD

USD è un formato complesso, la sua specifica supporta molte funzionalità, ma non tutti i software 3D le supportano. OSX/iOS, per esempio, non supportano i colori per vertice. Le modalità predefinite all’interno dell’esportatore USD cercano di ottenere la migliore compatibilità possibile con OpenUSD, Apple, Procreate, ZBrush.

::: 

## Render

Esporta un’immagine che è la combinazione di tutte le impostazioni nel progetto (luci, materiali, post-processing, ecc.). 

![](/images/file_render.webp)
### Anteprima

Il piccolo pulsante di anteprima accanto al titolo del menu attenuerà le barre degli strumenti per aiutare a visualizzare il risultato finale.

### Sfondo trasparente
Abilita un canale alfa per il render, utile per combinare il render con altre immagini in programmi 2D. Nota che la trasparenza parziale non è supportata.

### Mostra interfaccia
Abilita l’inclusione dell’interfaccia di Nomad nel render.

### Rapporto di render
Un moltiplicatore sulla risoluzione dell’immagine.

### Dimensione finale
La risoluzione da utilizzare per il render. Quando è selezionato `Custom`, gli slider di larghezza e altezza saranno abilitati. 

Quando il menu File è attivo, nel viewport verrà disegnato un riquadro tratteggiato per indicare la regione di render se non corrisponde alla risoluzione dello schermo (nota che devi essere in modalità orizzontale perché sia corretta).

### Esporta png
Fai clic su questo pulsante per avviare il processo di render. Al termine potrai scegliere come salvare o condividere l’immagine.

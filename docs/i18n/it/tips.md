# ![](/icons/manual.webp) Suggerimenti {#tips}

[[toc]]

## Come iniziare un modello {#how-to-start-a-model}

I principianti nella scultura 3D spesso chiedono qual è il modo migliore per iniziare un modello. Non esiste un modo migliore in assoluto, persone diverse hanno preferenze diverse. Ecco alcuni degli approcci più comuni.

### Scolpire su sfera, multires {#sculpt-on-sphere-multires}

Il modello predefinito quando si avvia Nomad è il modo più comune. Usa gli strumenti sposta, clay, crease per spingere e tirare la sfera fino a darle forma, usa i livelli di suddivisione più bassi quando vuoi fare grandi cambiamenti rapidamente, usa i livelli di suddivisione più alti per il lavoro di dettaglio.

Un problema comune è che spesso finirai i poligoni dove ti servono, mentre ne avrai troppi in altre zone. Ad esempio, se spingi la sfera predefinita fino a ottenere un corpo intero, è probabile che non avrai abbastanza dettaglio per fare le dita, mentre avrai un sacco di poligoni sprecati sulla parte posteriore della testa. Per forme per lo più sferiche come una testa però, questo può andare bene.

### Dyntopo {#dyntopo}

Abilitare Dyntopo aggiungerà e rimuoverà in modo adattivo i poligoni mentre scolpisci. Questi poligoni saranno triangoli, e i principianti spesso non gradiscono il layout disordinato rispetto all’aspetto pulito del multires. Vale la pena insistere! Se attivi lo smooth shading, disattivi il wireframe e smetti di preoccuparti del layout, questa modalità può dare una sensazione molto simile all’argilla. Non dimenticare che se usi un pennello grande, o un pennello smooth, questa modalità può anche rimuovere poligoni, quindi lo strumento risulta sempre veloce e reattivo. Una volta terminata una prima passata della scultura, puoi clonarla ed eseguirla attraverso il quad remesher per ottenere un layout pulito, e riproiettare i dettagli originali su un livello di suddivisione alto.

### Voxel remesh {#voxel-remesh}

Il voxel remesh applicherà una topologia per lo più basata su quad alla tua scultura. Questa operazione è veloce a risoluzioni basse e può essere usata per sostituire rapidamente poligoni stirati o eccessivamente densi con un layout a spaziatura uniforme. Questo può essere un ottimo modo per iniziare un corpo intero partendo da una sfera; ad esempio inizi con una testa, puoi allungare un collo, fare voxel remesh. Allunghi un corpo, voxel remesh, braccia, voxel remesh, e così via, finché non hai le forme di base.

### Usare oggetti multipli {#use-multiple-objects}

Molte guide di anatomia rappresentano un corpo con semplici sfere, cilindri, cubi. Puoi scolpire in questo modo anche in Nomad. Questo ha il vantaggio di permetterti di collegare gli oggetti nella gerarchia della scena, così puoi ruotare il collo e la testa lo seguirà, per esempio. Poter usare lo strumento gizmo per traslazioni/rotazioni/scale precise è anche molto utile, e puoi anche impostare pivot per forma in modo che si muovano esattamente come ti aspetti. Quando i blocchi di base sono nella posizione giusta, puoi selezionarli tutti e fare voxel remesh o booleane per unirli in una singola superficie per una scultura più dettagliata.

Un suggerimento utile per questo modo di lavorare è iniziare con una sfera, scalarla in una salsiccia allungata, premere pivot, cliccare “bottom”, premere di nuovo pivot. Ora hai una parte del corpo che può essere clonata, traslata lungo la lunghezza della prima sfera, clonata, ruotata, clonata, fatta scorrere, clonata ecc. per impostare rapidamente un corpo.

### Tubes {#tubes}

Lo strumento tube è un ottimo modo per iniziare una scultura. Code di rettili, braccia, gambe, dita, sopracciglia, possono essere tutte abbozzate rapidamente con lo strumento tube, quindi facilmente modificate in seguito. Ti permette anche di modificare il profilo della sezione trasversale, consentendo cambi di forma rapidi. Puoi convalidare la forma per iniziare a scolpirci sopra, e fare voxel remesh insieme ad altri oggetti per ottenere una mesh di corpo intero.

### Usare altre app {#use-other-apps}

Alcune persone preferiscono iniziare un modello in altre app, va benissimo anche questo. Strumenti come Blender o Valence permettono di iniziare i modelli usando tecniche low poly, che possono poi essere importati in Nomad per la scultura.

### Usare i preset integrati {#use-the-built-in-presets}

Dal menu progetto clicca `Preset...` in alto a destra. Qui troverai diversi preset di teste e corpi dalla Blender Foundation. Seleziona quello che ti piace, toccalo di nuovo, aggiungilo alla scena. 

### Usare modelli online {#use-online-models}

Ci sono molti modelli gratuiti disponibili online, ad esempio polyhaven, sketchfab, turbosquid. Di solito questi modelli possono essere importati in Nomad, e o scolpiti direttamente, o usati come riferimento.

### Nessuna regola! {#no-rules}

In definitiva puoi usare qualsiasi combinazione di queste tecniche, o nessuna! Nomad è molto flessibile da questo punto di vista, gli utenti avanzati potrebbero iniziare con i tubes, poi dyntopo, poi combinare con un piede scaricato, poi fare quad remesh di tutto, poi multires per il dettaglio finale. Qualunque cosa funzioni per te.

## Facegroups {#facegroups}

Lo strumento facegroup può essere usato per molte cose, come spiegato in questo video su YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Questa è una sintesi testuale delle funzionalità trattate in quel video.

### Perché i facegroups? {#why-facegroups}

I facegroups ti permettono di organizzare e selezionare le facce (“faces” e “polygons” sono usati in modo intercambiabile in questo manuale). Questo è più facile da spiegare rispetto agli altri strumenti di selezione e organizzazione di Nomad. Nomad ti permette di creare oggetti, nominarli, collegarli, è facile creare una struttura di oggetti per definire una stanza composta da pavimento, pareti, sedia, tavolo e così via.

Per un personaggio potresti fare un primo block-out usando oggetti separati per testa, braccio, gamba, ma una volta che unisci tutti i pezzi in una singola mesh, questa struttura è persa. Puoi lavorare su sotto-sezioni di un personaggio con le maschere, ma può diventare noioso continuare a dipingere una maschera per le mani, poi per il naso, poi di nuovo per le mani.

Qui entrano in gioco i facegroups. Ti permettono di etichettare le facce dei poligoni con un colore, e poi poter selezionare e manipolare i poligoni che hanno lo stesso colore. Nota che il colore del facegroup e il vertex color sono cose diverse.

L’analogia più vicina sarebbe dipingere colori su una mappa, e poi in seguito poter selezionare paesi o regioni in base al colore.

Per le teste dei personaggi potresti dipingere zone per marcare le cavità oculari, il naso, le labbra, il mento, le orecchie, e poi selezionare facilmente quelle zone in seguito. Per la scultura hard surface e meccanica può essere utile definire pannelli e sezioni.

### Creare e modificare i facegroups {#creating-and-editing-facegroups}

I facegroups possono essere applicati con un pennello, dove ogni nuova pennellata crea un nuovo facegroup, oppure possono selezionare il facegroup sotto il cursore ed estenderlo. Possono anche essere creati usando forme.

* Dot, auto-pick abilitato - un singolo trascinamento definirà un nuovo colore di facegroup e lo assegnerà alle facce su cui trascini. Ogni nuovo trascinamento definirà un nuovo facegroup. Un tap riempirà un nuovo facegroup.
* Dot, auto-pick disabilitato - quando il pulsante auto-pick è in modalità “sub”, Nomad selezionerà il facegroup sotto il cursore e lo applicherà durante il resto del trascinamento. Questo è utile per rifinire i facegroups senza doverli selezionare manualmente.

### Mascheratura {#masking}

Quando lo strumento mask è attivo, e il pulsante facegroup è attivo sulla sua toolbar, toccare un facegroup lo maschererà.

### Nascondere {#hiding}

Quando lo strumento hide è attivo, e il pulsante facegroup è attivo sulla sua toolbar, toccare un facegroup lo nasconderà.

### Organizzare {#organizing}

Come accennato prima, i facegroups possono essere usati per organizzare la tua mesh senza richiederti di creare oggetti separati. Potresti non voler dividere una testa in oggetti separati per naso, mento, orecchie, ma è molto utile averli definiti tramite facegroups.

### Aree UV {#uv-regions}

Lo strumento UV Atlas tenterà di definire automaticamente le cuciture, ma a volte le metterà dove non le vuoi. Se esistono facegroups su un oggetto, e l’opzione facegroup è attiva nelle opzioni di UV Atlas, userà invece i bordi dei facegroups come cuciture UV.

### Quad remesher {#quad-remesher}

Il plugin quad remesher di solito farà scorrere bene i bordi sul tuo modello, ma puoi usare i facegroups per aiutarlo a guidare il flusso quando l’opzione facegroup è abilitata. Questo può rendere facile definire un flusso di edge pulito attorno agli occhi, una cresta del sopracciglio, le labbra, una piega della guancia per esempio.

### Filtrare con altri strumenti {#filter-with-other-tools}

Molti strumenti avranno opzioni per essere consapevoli dei facegroups, o dal loro menu principale, o tramite il menu stroke -> filtering. Ad esempio lo strumento smooth a intensità superiori al 100% può levigare in modo aggressivo i dettagli all’interno di un facegroup, ma mantenere relativamente intatto il bordo del facegroup.

### Rilassare e ammorbidire i bordi dei facegroup {#relax-and-smooth-facegroup-borders}

L’opzione relax all’interno dello strumento facegroup fa un ottimo lavoro nel levigare i bordi dei facegroups mantenendo intatte le altre caratteristiche. Questo può essere un ottimo modo per definire regioni di bordo dei facegroups lisce prima del quad remeshing.

## Limitazioni su tablet/mobile {#limitations-on-tabletmobile}

I tablet e i telefoni attuali sono molto potenti, ma hanno differenze importanti rispetto ai computer desktop e ai laptop:

### Niente raffreddamento attivo {#no-active-cooling}

I computer hanno ventole e/o grandi dissipatori per mantenerli freschi, e sono progettati per funzionare a temperature elevate. L’hardware mobile è di solito progettato prima di tutto per essere sottile, non per aiutare a mantenere freschi i componenti interni. Se Nomad viene spinto alle sue impostazioni di qualità più alte (modalità di illuminazione PBR, materiali complessi, molti oggetti, molte opzioni di post processing abilitate), questo può sia surriscaldare il dispositivo che scaricare la batteria molto rapidamente. 

Un approccio migliore è usare una modalità di illuminazione matcap e usare un render multiplier più basso (in cima al menu di post process). Queste scelte manterranno il dispositivo fresco e ti permetteranno di scolpire più a lungo.

### Memoria limitata {#limited-memory}

Nomad può ottenere risultati pari alla maggior parte delle app di scultura desktop, ma non può piegare le leggi della fisica! La maggior parte dei computer desktop ha il doppio della memoria dei dispositivi mobili, le workstation costruite per l’animazione 3D spesso hanno 4x o 8x la memoria. Per questo motivo, è bene essere consapevoli di quanti poligoni stai usando, fare alcuni test sul tuo dispositivo per vedere quando inizia a diventare lento. Quasi tutti i dispositivi che possono eseguire Nomad possono gestire 1 milione di poligoni abbastanza facilmente. Un iPad Pro M2 può gestire comodamente 8 milioni, le persone hanno testato sugli ultimi iPad andando ben oltre.

Detto questo, solo le sculture più dettagliate hanno bisogno di più di 4 milioni di poligoni; se stai creando oggetti relativamente semplici e ti ritrovi spesso ad andare oltre 500.000, 1 milione, 4 milioni, stai usando troppi poligoni! Assicurati di avere la modalità smooth shaded abilitata nelle opzioni.

### Il sistema operativo è meno tollerante con le app pesanti {#os-is-less-forgiving-with-intensive-apps}

Apple e Android si aspettano che le app salvino e carichino piccoli file molto rapidamente. Presuppongono anche che le app possano fare task switching molto velocemente. Anche qui Nomad fa alcuni trucchi intelligenti per mantenere le dimensioni dei file relativamente piccole e salvarli molto rapidamente, ma se il sistema operativo mobile decide che Nomad sta impiegando troppo tempo, semplicemente lo ucciderà prima che abbia finito il suo compito. Questo è un altro motivo per mantenere i file sul lato più piccolo; è possibile lavorare con sculture da 37 milioni di poligoni come ha riportato un utente su Discord, ma non è raccomandato!

## Lavorare su schermi piccoli {#working-on-small-screens}

Nomad è progettato per funzionare su tablet, ma funziona bene anche sui telefoni. Scolpire su uno schermo piccolo come quello di un telefono può essere reso più facile con alcuni accorgimenti di interfaccia e di workflow:

* Un tap con 4 dita attiverà/disattiverà l’intera UI, dandoti più spazio per scolpire.
* Un trascinamento con 3 dita verso l’alto e verso il basso cambierà il raggio del pennello
* La scala della UI può essere resa più piccola per far entrare più pulsanti se hai una buona vista, o più grande se hai una vista scarsa!
* I menu più larghi a volte possono intralciare la scultura, puoi renderli trasparenti e non sfocati per permetterti di vedere la scultura sotto il menu.
* Se scolpisci con un dito, usa l’opzione offset per spostare il centro del pennello un po’ lontano dal dito.
* Queste e molte altre opzioni possono essere trovate nel [menu Interface](./interface.md). 

## Deformatore Inflate o Peak {#inflate-or-peak-deformer}

Molte app 3D includono un deformatore inflate, che spinge tutti i vertici lungo la loro normale di una quantità controllabile. Sebbene Nomad attualmente non abbia deformatori, è possibile emulare questo comportamento con il pennello inflate:

* Seleziona il pennello inflate
* Dal [menu Stroke](./stroke.md#stroke) cambia il metodo di stroke in `Lock + Radius'
* Rendi il raggio del pennello più grande della tua scultura, allontana la camera dalla scultura se necessario.
* Clicca quindi trascina una pennellata sulla superficie del tuo oggetto; quando il raggio è più grande dell’oggetto, l’intera forma verrà gonfiata uniformemente di una quantità fissa.
* Regola l’intensità del pennello per controllare la quantità di inflazione
* Usa le maschere se necessario per proteggere o ridurre l’effetto dell’inflate in certe aree.

## Rimuovere grumi o “brufoli” da un’operazione di voxel remesh {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Il voxel remesh è ottimo per creare poligoni a spaziatura uniforme, ma a volte crea una topologia che causerà piccoli bozzi o brufoli quando viene levigata. Per esempio:

* Usa il pennello crease sulla sfera predefinita e fai un vortice
* Fai voxel remesh con “build multiresolution at 3”
* Leviga con alta intensità
* compaiono artefatti (più facili da vedere con un materiale matcap ad alto contrasto):

![](/videos/tip_pimples_before.mp4)

Per correggere via scultura, prova l’opzione `Stable smoothing` nelle impostazioni dello smooth. Questa può gestire il layout di topologia irregolare del voxel remesh e ottenere risultati puliti.

![](/videos/tip_pimples_stable_smooth.mp4)

Per correggere la topologia stessa, usa una nuova primitiva, o gli strumenti di quad remesh, o un modellatore 3D esterno, e proietta il dettaglio dalla mesh originale a quella nuova tramite `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Illuminazione diurna {#daylight-lighting}

Il render PBR predefinito è, come suggerisce il nome, fisicamente basato, il che, come una foto digitale non elaborata, può apparire un po’ slavato e piatto. Le luci e il post processing di Nomad possono essere usati per rendere i render più vivaci.

Ecco un render predefinito, vediamo se possiamo farlo sembrare migliore:
![](/images/tips_lighting_default.webp)

Abilitare il post processing e il tonemapping può aggiungere luminosità e contrasto:

![](/images/tips_lighting_tonemap.webp)

Per concentrarsi sulle luci, la luce ambiente predefinita è buona per scolpire, ma può essere migliorata per un render finale. Un modo di pensarci è separare la luce diretta (ad es. il sole) dalla luce ambiente (ad es. la luce dal blu del cielo, dal terreno). Riducendo la luce ambiente e ruotandola, si inizia a catturare l’aspetto che l’illuminazione dovrebbe avere se il soggetto fosse in un’area in ombra:

![](/images/tips_lighting_env.webp)

Si può aggiungere una luce diretta e aumentarne l’intensità per simulare una luce solare intensa. Bilanciandola con la luce ambiente si otterrà un risultato gradevole:

![](/images/tips_lighting_sunlight.webp)

I personaggi possono beneficiare del cambio del loro materiale in subsurface, e del posizionamento di uno spotlight dietro il personaggio puntato verso le orecchie per farle brillare:

![](/images/tips_lighting_sss.webp)

Poi sperimenta con il resto delle impostazioni di post process! Global Illumination e Ambient Occlusion aiutano con un’illuminazione più realistica. Curvature e Sharpen possono aiutare a far risaltare più dettagli nella scultura. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette aiutano a simulare gli effetti della fotocamera. Nota che man mano che le funzionalità vengono abilitate, l’illuminazione e gli altri valori di post processing devono essere regolati per compensare.

Ecco il render con un set completo di regolazioni di post processing:
![](/images/tips_lighting_final.webp)
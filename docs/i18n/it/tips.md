# ![](/icons/manual.webp) Consigli {#tips}

[[toc]]

## Come iniziare un modello {#how-to-start-a-model}

Chi è alle prime armi con la scultura 3d chiede spesso qual è il modo migliore per iniziare un modello. Non esiste un modo migliore: ognuno ha le proprie preferenze. Ecco alcuni degli approcci più comuni.

### Scolpire su una sfera, multirisoluzione {#sculpt-on-sphere-multires}

Il modello predefinito all'avvio di Nomad è il punto di partenza più comune. Usa gli strumenti sposta, argilla e solco per spingere e tirare la sfera fino a darle forma; usa i livelli di suddivisione bassi quando vuoi fare grandi cambiamenti in fretta, e quelli alti per il lavoro di dettaglio.

Un problema comune è che spesso finisci i poligoni proprio dove ti servono, mentre altrove ne hai troppi. Per esempio, se trasformi la sfera predefinita in un corpo intero, probabilmente non avrai abbastanza dettaglio per le dita, mentre sprecherai un sacco di poligoni sulla nuca. Per forme quasi sferiche come una testa, però, può andare benissimo.

### DynTopo {#dyntopo}

Attivando DynTopo, i poligoni vengono aggiunti e rimossi in modo adattivo mentre scolpisci. Questi poligoni sono triangoli, e chi inizia spesso non apprezza la loro disposizione disordinata rispetto all'aspetto pulito della multirisoluzione. Vale la pena insistere! Se attivi l'ombreggiatura uniforme, spegni il wireframe e smetti di preoccuparti della disposizione, questa modalità dà una sensazione molto simile all'argilla. Non dimenticare che, con un pennello grande o con il pennello leviga, questa modalità può anche rimuovere poligoni, così lo strumento resta sempre veloce e reattivo. Una volta finita una prima passata della scultura, puoi clonarla, passarla nel remeshing quad per ottenere una bella disposizione, e riproiettare i dettagli originali su un livello di suddivisione alto.

### Remeshing dei voxel {#voxel-remesh}

Il remeshing dei voxel applica alla scultura una topologia fatta per lo più di quad. A basse risoluzioni è un'operazione rapida, e può servire per sostituire velocemente poligoni stirati o troppo densi con una disposizione uniforme. È un ottimo modo per partire da una sfera e arrivare a un corpo intero: diciamo che inizi da una testa, allunghi un collo, remeshing dei voxel. Allunghi un corpo, remeshing dei voxel, le braccia, remeshing dei voxel, e così via, finché non hai le forme di base.

### Usare più oggetti {#use-multiple-objects}

Molte guide di anatomia rappresentano il corpo con sfere, cilindri e cubi semplici. Puoi scolpire così anche in Nomad. Il vantaggio è che puoi imparentare gli oggetti tra loro nella gerarchia della scena: per esempio, ruoti il collo e la testa lo segue. È molto utile anche poter usare lo strumento gizmo per spostamenti, rotazioni e ridimensionamenti precisi, e puoi impostare il pivot di ogni forma perché si muova esattamente come ti aspetti. Quando i blocchi di base sono al loro posto, puoi selezionarli tutti e unirli in un'unica superficie con il remeshing dei voxel o con un'operazione booleana, per scolpire più nel dettaglio.

Un trucco comodo per lavorare così: parti da una sfera, ridimensionala in una salsiccia allungata, premi pivot, tocca "basso", premi di nuovo pivot. Ora hai una parte del corpo che puoi clonare, spostare lungo la prima sfera, clonare, ruotare, clonare, far scorrere, clonare e così via... per impostare velocemente un corpo.

### Tubi {#tubes}

Lo strumento tubo è un ottimo modo per iniziare una scultura. Code di rettile, braccia, gambe, dita, sopracciglia: puoi abbozzarle tutte in fretta con lo strumento tubo e modificarle facilmente in seguito. Ti permette anche di cambiare il profilo della sezione, per modificare rapidamente la forma. Puoi convalidare la forma per iniziare a scolpirci sopra, e farne il remeshing dei voxel insieme ad altri oggetti per ottenere la mesh di un corpo intero.

### Usare altre app {#use-other-apps}

Alcuni preferiscono iniziare un modello in altre app, e va benissimo. Strumenti come Blender o Valence permettono di iniziare un modello con tecniche low poly, per poi importarlo in Nomad e scolpirlo.

### Usare i preset integrati {#use-the-built-in-presets}

Dal menu [File](files.md), tocca `Preset…` a sinistra della sezione del progetto. Qui trovi diversi preset di teste e corpi della Blender Foundation. Scegline uno che ti piace, toccalo di nuovo e aggiungilo alla scena.

### Usare modelli online {#use-online-models}

Online si trovano molti modelli gratuiti, per esempio su polyhaven, sketchfab, turbosquid. Di solito questi modelli si possono importare in Nomad e scolpire direttamente, oppure usare come riferimento.

### Nessuna regola! {#no-rules}

Alla fine puoi combinare queste tecniche come vuoi, oppure non usarne nessuna! Nomad è molto flessibile da questo punto di vista: un utente esperto potrebbe partire dai tubi, poi passare a DynTopo, poi aggiungere un piede scaricato, poi fare il remeshing quad di tutto, e infine usare la multirisoluzione per i dettagli finali. Qualsiasi cosa funzioni per te.

## Gruppi di facce {#facegroups}

Lo strumento gruppo di facce si può usare per molte cose, come spiegato in questo video su YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Ecco un riassunto testuale delle funzioni mostrate nel video.

### Perché i gruppi di facce? {#why-facegroups}

I gruppi di facce ti permettono di organizzare e selezionare le facce (in questo manuale "facce" e "poligoni" sono sinonimi). È più facile spiegarlo partendo dagli altri strumenti di selezione e organizzazione di Nomad. Nomad ti permette di creare oggetti, dar loro un nome, imparentarli: è facile creare una struttura di oggetti per descrivere una stanza fatta di pavimento, pareti, sedia, tavolo e così via.

Per un personaggio potresti fare un primo abbozzo con oggetti separati per testa, braccia e gambe, ma una volta uniti tutti i pezzi in un'unica mesh, questa struttura va persa. Puoi lavorare su parti del personaggio con le maschere, ma alla lunga diventa noioso dipingere una maschera per le mani, poi per il naso, poi di nuovo per le mani.

Ed è qui che i gruppi di facce diventano utili. Ti permettono di etichettare le facce dei poligoni con un colore, per poi selezionare e manipolare i poligoni che hanno lo stesso colore. Nota che il colore dei gruppi di facce e il colore dei vertici sono due cose diverse.

L'analogia più vicina è colorare una cartina geografica, per poi poter selezionare paesi o regioni in base al colore.

Per la testa di un personaggio potresti dipingere delle zone per segnare le orbite, il naso, le labbra, il mento e le orecchie, per poi selezionarle facilmente in seguito. Nella scultura hard surface e meccanica può essere utile per definire pannelli e sezioni.

### Creare e modificare i gruppi di facce {#creating-and-editing-facegroups}

I gruppi di facce si possono applicare con un pennello, dove ogni nuovo tratto crea un nuovo gruppo di facce, oppure si può selezionare il gruppo di facce sotto il cursore ed estenderlo. Si possono creare anche con le forme.

* Punto, modalità predefinita - un singolo trascinamento definisce un nuovo colore di gruppo di facce e lo assegna alle facce su cui passi. Ogni nuovo trascinamento definisce un nuovo gruppo di facce. Un tocco riempie un'area con un nuovo gruppo di facce.
* Punto, modalità `Scegli` - quando il pulsante `Scegli` nella barra a sinistra è attivo, Nomad seleziona il gruppo di facce sotto il cursore e lo applica per il resto del trascinamento. È utile per rifinire i gruppi di facce senza doverli selezionare a mano.

### Maschera {#masking}

Quando lo strumento maschera è attivo e il pulsante gruppo di facce è attivo nella sua barra degli strumenti, toccando un gruppo di facce lo mascheri.


### Nascondere {#hiding}

Quando lo strumento nascondi è attivo e il pulsante gruppo di facce è attivo nella sua barra degli strumenti, toccando un gruppo di facce lo nascondi.

### Organizzare {#organizing}

Come detto prima, i gruppi di facce servono a organizzare la mesh senza doverla dividere in oggetti separati. Magari non vuoi dividere una testa in oggetti separati per naso, mento e orecchie, ma è molto utile averli definiti come gruppi di facce.

### Regioni UV {#uv-regions}

Lo strumento UV Atlas cerca di definire automaticamente le cuciture, ma a volte le mette dove non le vuoi. Se un oggetto ha dei gruppi di facce e l'opzione gruppo di facce è attiva nelle opzioni di UV Atlas, userà invece i bordi dei gruppi di facce come cuciture UV.

### Quad Remesher {#quad-remesher}

Il plugin Quad Remesher di solito fa scorrere bene gli spigoli sul modello, ma puoi usare i gruppi di facce per guidarlo quando l'opzione gruppo di facce è attiva. Così è facile definire un flusso di spigoli pulito intorno agli occhi, all'arcata sopraccigliare, alle labbra o alla piega della guancia, per esempio.

### Filtrare con altri strumenti {#filter-with-other-tools}

Molti strumenti hanno opzioni per tenere conto dei gruppi di facce, nel loro menu principale oppure nel menu Tratto -> Filtro. Per esempio, lo strumento leviga con una forza oltre il 100% può cancellare in modo deciso i dettagli all'interno di un gruppo di facce, lasciando però quasi intatto il bordo del gruppo.

### Rilassare e levigare i bordi dei gruppi di facce {#relax-and-smooth-facegroup-borders}

L'opzione `Rilassa` dello strumento gruppo di facce leviga in modo eccellente i bordi dei gruppi di facce, lasciando intatto il resto. È un ottimo modo per definire bordi morbidi tra i gruppi di facce prima del remeshing quad.

## Limiti su tablet e smartphone {#limitations-on-tabletmobile}

I tablet e gli smartphone di oggi sono molto potenti, ma hanno differenze importanti rispetto ai computer desktop e ai portatili:

### Nessun raffreddamento attivo {#no-active-cooling}

I computer hanno ventole e/o grandi dissipatori per restare freschi, e sono progettati per funzionare ad alte temperature. I dispositivi mobili sono di solito progettati prima di tutto per essere sottili, non per tenere fresco l'interno. Se spingi Nomad alle impostazioni di qualità più alte (modalità di illuminazione PBR, materiali complessi, tanti oggetti, molte opzioni di post processing attive), il dispositivo può surriscaldarsi e la batteria scaricarsi molto in fretta.

Un approccio migliore è usare una modalità di illuminazione matcap e una `Risoluzione rendering` più bassa (in cima al menu Post processing). Così il dispositivo resta fresco e puoi scolpire più a lungo.

### Memoria limitata {#limited-memory}

Nomad può ottenere risultati pari alla maggior parte delle app di scultura per desktop, ma non può piegare le leggi della fisica! La maggior parte dei computer desktop ha il doppio della memoria dei dispositivi mobili, e le workstation per l'animazione 3d ne hanno spesso 4 o 8 volte tanto. Per questo è bene sapere quanti poligoni stai usando: fai qualche prova sul tuo dispositivo per vedere quando inizia a rallentare. Quasi tutti i dispositivi che fanno girare Nomad gestiscono 1 milione di poligoni senza problemi. Un iPad Pro M2 ne gestisce comodamente 8 milioni, e c'è chi ha provato gli iPad più recenti andando ben oltre.

Detto questo, solo le sculture più dettagliate hanno bisogno di più di 4 milioni di poligoni; se crei oggetti relativamente semplici e ti ritrovi spesso oltre 500.000, 1 milione, 4 milioni, stai usando troppi poligoni! Assicurati di avere `Ombreggiatura uniforme` attiva nelle [Impostazioni](settings.md).

### Il sistema operativo è meno tollerante con le app pesanti {#os-is-less-forgiving-with-intensive-apps}

Apple e Android si aspettano che le app salvino e carichino file piccoli molto rapidamente. Danno anche per scontato che le app possano passare da un'attività all'altra molto in fretta. Anche qui Nomad usa qualche trucco intelligente per mantenere i file relativamente piccoli e salvarli molto in fretta, ma se il sistema operativo del dispositivo decide che Nomad ci sta mettendo troppo, lo chiude semplicemente prima che abbia finito. È un motivo in più per tenere i file piuttosto leggeri: si può lavorare con sculture da 37 milioni di poligoni, come ha riferito un utente su Discord, ma non è consigliato!

## Lavorare su schermi piccoli {#working-on-small-screens}

Nomad è pensato per i tablet, ma funziona bene anche sui telefoni. Scolpire su uno schermo piccolo come quello di un telefono diventa più facile con qualche accorgimento nell'interfaccia e nel modo di lavorare:

* Un tocco con 4 dita mostra o nasconde tutta l'interfaccia, lasciandoti più spazio per scolpire.
* Trascinando 3 dita in su e in giù cambi il raggio del pennello.
* Puoi ridurre la scala dell'interfaccia per far stare più pulsanti se hai una buona vista, o ingrandirla se non ci vedi bene!
* A volte i menu più larghi coprono la scultura: puoi renderli trasparenti e senza sfocatura per vedere la scultura sotto il menu.
* Se scolpisci con un dito, usa l'opzione [`Spostamento tratto`](stroke.md#stroke-offset) per allontanare un po' il centro del pennello dal dito.
* Queste e molte altre opzioni si trovano nel [menu Interfaccia](./interface.md).


## Deformatore di gonfiaggio {#inflate-or-peak-deformer}

Molte app 3d hanno un deformatore di gonfiaggio, che spinge tutti i vertici lungo la loro normale di una quantità regolabile. Nomad per ora non ha deformatori, ma è possibile imitare questo comportamento con il pennello gonfia:

* Seleziona il pennello gonfia
* Dal [menu Tratto](./stroke.md#stroke) cambia il metodo del tratto in `Blocco + raggio`
* Rendi il raggio del pennello più grande della scultura, allontanando la fotocamera se serve.
* Tocca e trascina un tratto sulla superficie dell'oggetto: quando il raggio è più grande dell'oggetto, tutta la forma viene gonfiata in modo uniforme di una quantità fissa.
* Regola l'intensità del pennello per controllare quanto gonfiare
* Se serve, usa la maschera per proteggere alcune zone o ridurvi l'effetto del gonfiaggio.

## Eliminare i bozzi o i "brufoli" dopo un remeshing dei voxel {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Il remeshing dei voxel è ottimo per ottenere poligoni distribuiti in modo uniforme, ma a volte crea una topologia che fa comparire piccoli bozzi o brufoli quando la levighi. Per esempio:

* Usa il pennello solco sulla sfera predefinita e disegna una spirale
* Fai un remeshing dei voxel con `Crea multirisoluzione` a 3
* Leviga con un'intensità alta
* compaiono degli artefatti (si vedono meglio con un materiale matcap molto contrastato):

![](/videos/tip_pimples_before.mp4)

Per correggerli scolpendo, prova l'opzione `Levigatura stabile` nelle impostazioni dello strumento leviga. Gestisce bene la topologia irregolare del remeshing dei voxel e dà risultati puliti.

![](/videos/tip_pimples_stable_smooth.mp4)

Per correggere la topologia stessa, usa una nuova primitiva, gli strumenti di remeshing quad o un modellatore 3d esterno, e proietta i dettagli dalla mesh originale a quella nuova con `Topologia -> Trasferisci -> Riproietta → Vertice`.

![](/videos/tip_pimples_reproject.mp4)

## Illuminazione diurna {#daylight-lighting}

Il render PBR predefinito è, come dice il nome, fisicamente basato, e come una foto digitale non ritoccata può sembrare un po' sbiadito e piatto. Puoi usare le luci e il post processing di Nomad per rendere i render più vivaci.

Ecco un render predefinito, vediamo se riusciamo a migliorarlo:
![](/images/tips_lighting_default.webp)

Attivando il post processing e la mappatura dei toni puoi aggiungere luminosità e contrasto:

![](/images/tips_lighting_tonemap.webp)

Passiamo alle luci: l'illuminazione d'ambiente predefinita va bene per scolpire, ma si può migliorare per un render finale. Un modo di ragionare è separare la luce diretta (per esempio il sole) dalla luce d'ambiente (per esempio la luce che arriva dal blu del cielo o dal terreno). Riducendo la luce d'ambiente e ruotandola, si inizia a ottenere l'illuminazione che avrebbe il soggetto se si trovasse all'ombra:

![](/images/tips_lighting_env.webp)

Puoi aggiungere una luce diretta e aumentarne l'intensità per simulare una luce solare forte. Bilanciandola con la luce d'ambiente ottieni un risultato piacevole:

![](/images/tips_lighting_sunlight.webp)

I personaggi possono guadagnarci passando a un materiale subsurface, con una luce spot dietro il personaggio puntata verso le orecchie per farle brillare:

![](/images/tips_lighting_sss.webp)

Poi sperimenta con il resto delle impostazioni di post processing! L'illuminazione globale e l'occlusione ambientale aiutano a ottenere un'illuminazione più realistica. Curvatura e nitidezza aiutano a far risaltare i dettagli della scultura. Aberrazione cromatica, profondità di campo, grana, bagliore diffuso e vignettatura simulano gli effetti di una fotocamera. Nota che, man mano che attivi nuove funzioni, devi regolare l'illuminazione e gli altri valori di post processing per compensare.

Ecco il render con una serie completa di ritocchi di post processing:
![](/images/tips_lighting_final.webp)

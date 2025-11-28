# ![](/icons/faq.webp) Domande frequenti {#faq}

[[toc]]

## Piattaforma {#platform}
### Dove si trovano i miei progetti sul dispositivo? {#locate}
I progetti si trovano nella cartella `projects` all'interno della cartella principale di Nomad.

Su iOS puoi accedere alla cartella di Nomad con l'app File di iOS.

Su Android, la cartella di Nomad si trova in `Android/data/com.stephaneginier.nomad/files/`.  
Nelle versioni recenti di Android (10/11), non hai più accesso alla cartella `Android/data`.
Puoi accedervi tramite un'app separata, per esempio [questa](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### È possibile fare beta test? {#beta}
Per Windows e MacOS potrebbe essere disponibile una beta sulla [Homepage](https://nomadsculpt.com).
<br>
Per iOS esiste una TestFlight privata, visita il [Discord](https://discord.com/invite/8h7BwpRz29) nel canale #beta-ios.
<br>
La [Web Demo](https://nomadsculpt.com/demo) è di solito aggiornata con le funzionalità più recenti.

### Perché su Android c’è una prova gratuita ma su iOS no? {#android-trial}
Perché i vecchi dispositivi Android fanno schifo (e anche alcuni recenti...), e non volevo che le persone comprassero l’app e venissero accolte da uno schermo nero.
Ma il motivo principale è che ho la sensazione che le app a pagamento su Android non siano davvero la norma.

### Qual è il tablet migliore per usare Nomad? {#best-tablet}

TLDR: Un iPad.

La risposta un po’ più lunga è 

> "L’iPad più nuovo _che puoi permetterti_, a meno che tu non odi davvero Apple, in quel caso il tablet Samsung più nuovo che puoi permetterti. Qualsiasi altra cosa, provala prima." 

Le persone vogliono sempre più informazioni, quindi ecco un riassunto.

Nomad funziona meglio sugli iPad più recenti:

* Gli iPad e gli iPhone possono accedere al plugin [Quad Remesher](tools#quad-remesher) di [Exoside](https://exoside.com/)
* Gli iPad recenti con l’ultima versione di Pencil supportano il [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), puoi ruotare la matita in alcuni strumenti di Nomad. 
* Le prestazioni dei più recenti chip serie M sono molto elevate. 

L’iPad più nuovo e costoso disponibile sarà in grado di renderizzare immagini finali molto velocemente e permetterti di scolpire con moltissimo dettaglio.

Tuttavia, il calo di prestazioni con gli iPad più economici e vecchi non è così drastico come ci si aspetta. Qualsiasi iPad che supporti Apple Pencil esegue Nomad piuttosto bene. Per esempio:

* Un iPad Pro del 2023 può gestire sculture da 5 milioni di poligoni restando reattivo, e un’immagine di qualità finale può essere renderizzata in 5 secondi.
* Un iPad Pro del 2015 può gestire un oggetto da 1,2 milioni di poligoni con un po’ di lag, e un’immagine di qualità finale può essere renderizzata in 20 secondi.

È una grande differenza di prestazioni, ma devi anche tenere conto del prezzo:

* L’iPad Pro 2025 costa *2500 USD* nuovo con tutte le opzioni. 
* L’iPad Pro 2023 attualmente costa *400 USD* su eBay.
* L’iPad Pro 2015 costa *250 USD* su eBay.

Vale la pena spendere 2100 dollari in più per avere 4 milioni di poligoni extra e risparmiare 15 secondi? Dipende da te.

I modelli non Pro possono essere ancora più economici e offrire una grande varietà di dimensioni e prestazioni tra cui scegliere. L’attuale iPad Air supporta la Pencil di seconda generazione con barrel roll, ed è sensibilmente più economico del Pro. Il mercato dell’usato e dei ricondizionati offre ancora più opzioni. 

Questo significa che, qualunque sia il tuo budget, dovresti riuscire a trovare un iPad adatto a te. E ricorda che la maggior parte delle sculture non arriva a milioni di poligoni! Se riesci a restare sotto i 500.000 poligoni, anche gli iPad vecchi ti permetteranno di scolpire velocemente.

`E Android?`

Le prestazioni grafiche di Android sono inferiori a quelle degli iPad. Secondo lo sviluppatore di Nomad, "Un Samsung Galaxy Tab S9 eseguirà Nomad un ordine di grandezza più lentamente di un iPad Air". Detto questo, molti utenti sono molto soddisfatti dei loro tablet Samsung, Nomad funziona bene per la maggior parte delle sculture. 

Per altri tablet Android, fai attenzione. L’hardware Android può variare moltissimo in termini di prestazioni, non è facile prevedere come girerà Nomad.

Usa prima la versione gratuita senza salvataggio di Nomad per fare dei test. 

`E memoria e archiviazione?`

La maggior parte dei file di Nomad tende a essere di 100 MB o meno. Questo significa che praticamente qualsiasi tablet in vendita oggi, iPad o Android, avrà spazio più che sufficiente per i tuoi progetti Nomad.


### Ho comprato Nomad per un dispositivo, posso usarlo su un altro? {#multi-devices}
Finché utilizza lo stesso app store e lo stesso account, sì.

Per esempio, se lo hai comprato sull’App Store iOS, puoi usarlo sugli altri tuoi dispositivi iOS.

Se lo hai comprato per il tuo tablet Android su Google Play, puoi usarlo sugli altri tuoi dispositivi Android.

Tuttavia, se hai comprato Nomad su Android e poi prendi un iPad, dovrai comprarlo di nuovo.

Questo perché Nomad non ha un proprio server di licenze o un modello in abbonamento. Non esiste alcun accordo tra Apple/Google/AppGallery per gestire la condivisione delle licenze. 


### Come faccio a ripristinare il mio acquisto? {#restore}
Google Play e AppGallery gestiscono entrambe la sincronizzazione in automatico.

- Vai nel menu About (icona di Nomad in alto a sinistra) e premi `restore purchase`
- Controlla di essere connesso allo stesso account che hai usato per acquistare Nomad (su Google Play).
- Riavvia il dispositivo
- A volte è necessario aspettare un paio d’ore
- Assicurati che l’app Google Play sia aggiornata
- Reinstalla Nomad (assicurati di [fare il backup dei file](#where-are-my-projects-located-on-my-device) se non vuoi perdere nulla)
- Puoi provare ad acquistare di nuovo per vedere cosa succede (nota: non puoi comprare due volte lo stesso articolo con lo stesso account)

:::tip
Puoi contattarmi a <support@nomadsculpt.com> ma l’unica cosa che potrò fare è confermare se a un’email è associato un acquisto.

Nota che ricevo regolarmente segnalazioni riguardo licenze che non si aggiornano correttamente dopo l’acquisto di un nuovo dispositivo.
Non ho alcun controllo sui pagamenti e sulla sincronizzazione degli account, è tutto gestito da Google/AppGallery!

Alla fine l’acquisto viene sempre ripristinato, ma i passaggi necessari per velocizzare il processo non sono chiari.
:::

::: warning
I dispositivi Huawei recenti non hanno accesso ai servizi Google.
In quel caso dovrai acquistare di nuovo l’app su AppGallery (lo store di Huawei).
:::

### Potete tradurre o correggere la mia lingua? {#locale}
Posso aggiungere relativamente facilmente un’altra lingua, ma mi affido alla traduzione tramite IA perché è molto più semplice da gestire per gli aggiornamenti regolari.
I file di traduzione si trovano [qui](https://github.com/stephomi/nomad-translation).

## Funzionalità {#features}

### Perché il gizmo non si muove? {#gizmo-not-moving}
Potresti avere [il pin abilitato nella toolbar del menu di sinistra](tools#left-menu-toolbar). 

### Possiamo animare all’interno di Nomad? {#animate}
Non per ora. Una timeline che permetta di animare i livelli potrebbe essere interessante, ma al momento non è davvero pianificata.  

Mi piacerebbe supportare rigging/skinning in futuro, ma pone alcune sfide (in particolare l’interazione con gli strumenti di scultura...) quindi per ora non c’è nulla di sicuro.


### Possiamo fare vero low‑poly modeling? {#lowpoly}
Non per ora.
Non rientra davvero nell’ambito di Nomad *Sculpt*, ma forse in futuro fornirò qualche strumento.


### Possiamo fare UV e texturing? {#texturing}
Risposta breve: Sì. Risposta lunga: Non direttamente, ma ci sono diversi modi per combinare gli ottimi strumenti di vertex paint di Nomad con UV e texture.

* Nomad ti permette di dipingere colore, roughness e proprietà del materiale direttamente nei vertici della tua scultura.
* Nomad permette conteggi di vertici molto alti, così puoi dipingere senza preoccuparti delle UV.
* Nomad può caricare texture da usare nei pennelli, permettendo di stampare e dipingere con texture.
* Nomad può caricare oggetti che hanno texture preassegnate, per scopi di rendering.
* Nomad può fare [UV unwrap](topology.md#uv-unwrap) di oggetti a bassa poligonizzazione.
* Colore/roughness/metalness possono essere trasferiti dalle texture ai vertici tramite [le opzioni di proiezione](topology.md#reproject-to-vertex).
* Colore/roughness/metalness/normali possono essere bake-ati dai vertici alle texture tramite [le opzioni di baking](topology.md#bake-to-texture)
* Baking e proiezione possono essere gestiti tra singoli oggetti o molti oggetti, oppure tra il livello di suddivisione più alto e quello più basso di un singolo oggetto, permettendo una varietà di workflow di bake e proiezione.
* Dopo il baking, esportando un obj verranno esportate anche le texture, che possono essere portate in un’app come Procreate per dipingere direttamente sulle texture.

### Posso registrare un video di turntable? {#video}
Non è pianificato per ora, iOS ha una [funzione di registrazione video](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) molto facile da usare.

Su iOS, si fa scorrendo il dito dall’angolo in alto a sinistra verso il basso e toccando il pulsante di registrazione. Avrai un conto alla rovescia di 3 secondi, fai scorrere via il menu per mostrare Nomad e usa la funzione turntable. Quando hai finito, scorri di nuovo dall’angolo in alto a destra verso il basso e tocca di nuovo il pulsante di registrazione. Modifica il video dalla libreria foto per rimuovere il filmato in eccesso all’inizio e alla fine.

### Potete aggiungere la mia funzione preferita come pulsante di primo livello? {#interface}
Sì, la toolbar inferiore ora può essere personalizzata dal menu [interface](interface.md), e ora è possibile creare toolbar flottanti.

### Quali saranno le prossime funzionalità? {#next-features}
Per la roadmap a medio/lungo termine ho molte idee ma ancora non so.  

La correzione dei bug e il miglioramento delle funzionalità esistenti avranno sempre priorità più alta rispetto all’aggiunta di nuove funzionalità.


### Possiamo fare rigging in Nomad? {#rigging}
No, ma è previsto. Per ora puoi collegare (parent) le forme tra loro e modificare i pivot, permettendo sculture semplici posabili.

### Possiamo usare più di 4 luci? {#lights}
No, è una limitazione del motore di rendering in tempo reale di Nomad. È possibile aggirarla usando oggetti emissivi e global illumination nel post process, come mostrato in [questo tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Possiamo importare gli strumenti di ZBrush? {#zbrush-import}
No, ZBrush usa un formato proprietario. Dovresti riuscire a estrarre le alpha map e usarle in Nomad. 

### Perché i colori non corrispondono a quello che ho dipinto? Perché non riesco a ottenere il bianco nel render? {#paint-pbr}
Immagina di scattare una foto a un foglio di carta, a una lampada da tavolo e al sole. Le fotocamere e gli schermi più vecchi li renderebbero tutti semplicemente “bianchi”. I sistemi più moderni possono mostrare la differenza tra il bianco riflesso della carta, la luce emessa da una lampada e il super brillante del sole.

La grafica computerizzata moderna cerca di funzionare in modo simile, emulando la fisica della luce e delle superfici. Questo si chiama `Physically Based Rendering`, o PBR, e il renderer PBR di Nomad si basa su questo. Il risultato è realistico ed equilibrato, ma spesso i colori molto brillanti dipinti appariranno più scuri.

Se hai bisogno che il render corrisponda meglio ai colori dipinti, puoi sistemare la cosa sia in modi non fisicamente basati che fisicamente basati:

Non PBR:
* `Usa la modalità 'Unlit' nel menu delle luci`. I colori verranno mostrati esattamente come dipinti, ma perderai anche tutte le ombreggiature. Utile per controlli rapidi e output più grafici.
* `Usa la modalità 'Matcap' nel menu delle luci`. Scegli un matcap più luminoso che sia per lo più bianco, senza dominante di colore.

PBR:
* `Usa un environment neutro`. Puoi [cambiare l’environment](shading.md#environment) con uno più neutro. Evita gli environment interni perché tendono a essere più colorati. Preferisci un environment diurno esterno o da studio.
* `Aumenta l’illuminazione`. Se stessi fotografando un foglio bianco in una stanza buia, aggiungeresti semplicemente più luce. Sulla luce di environment, alza lo slider di esposizione finché i colori non iniziano a sembrarti corretti, oppure aggiungi più luci singole con maggiore intensità.
* `Aumenta l’esposizione della camera`. Se la stanza buia non avesse luci extra, potresti far tenere aperto l’otturatore della fotocamera più a lungo o usare un ISO più sensibile. In Nomad puoi ottenere un risultato simile con il post processing. Vai in post process, abilitalo, vai in tone mapping, abilitalo e alza lo slider di esposizione finché i colori non ti sembrano giusti.
* `Usa il colore emissivo`. Nel menu dei materiali puoi abilitare “emissive” sotto textures, il che farà apparire un oggetto come una sorgente di luce. Se attivi la global illumination nelle impostazioni di post process, proietterà luce sugli altri oggetti nella scena. Puoi anche abilitare “unlit” per quel materiale, ottenendo un effetto simile senza texture.

## Arresti anomali {#crashes}

### Va in crash quando salvo o faccio il remesh del modello! {#crash-remesh}
Il tuo dispositivo sta esaurendo la memoria (RAM).  
Per ridurre l’uso di memoria nella scena, puoi usare alcune delle opzioni di [Topology](topology.md) per ridurre il numero di poligoni.

::: tip RAM/Storage
Quello che conta è la quantità di RAM, non lo storage (che di solito è molto più grande).
:::


### Va in crash quando carico il mio progetto! {#crash-load}
Se il file è piccolo, puoi inviarmelo e gli darò un’occhiata (via email <support@nomadsculpt.com>).

Altrimenti il dispositivo probabilmente sta esaurendo la memoria RAM.

- Assicurati di chiudere tutte le altre app aperte sul dispositivo.
- Avvia un nuovo progetto in Nomad invece di avere un progetto già aperto.
- Se va ancora in crash, l’unica soluzione è caricare [il file del progetto](#where-are-my-projects-located-on-my-device) su un dispositivo con più memoria.

::: tip
Su un browser desktop, puoi provare a caricare il file [a questo url](https://nomadsculpt.com/demo_save/) e poi esportarlo di nuovo dopo aver semplificato la scena.

Alcuni browser limitano la quantità di RAM che una singola scheda può usare, quindi è possibile che questa tecnica non funzioni.

Se il tuo progetto usa i [Layers](layers.md), potresti volerli unire (squash) per ridurre l’uso di memoria.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Va in crash quando avvio Nomad! {#crash-start}
Se va in crash al caricamento, significa che Nomad ha problemi con un certo file presente nella cartella di Nomad.

La maggior parte delle volte succede perché il progetto è pesante e purtroppo supera il limite di RAM.

Individua la [cartella di Nomad](#where-are-my-projects-located-on-my-device), quindi rinomina o sposta alcuni file per trovare il colpevole.

Per prima cosa prova a rinominare `settings.json`. In questo modo smetterà di caricare l’ultimo progetto.

Se non funziona, prova a spostare alcuni file recenti fuori dalle rispettive cartelle di risorse (`projects`, `matcaps`, `environments`, ecc.).

Puoi anche rinominare direttamente le cartelle in modo che Nomad le ignori completamente.
Se rinomini o sposti tutti i file nella cartella di Nomad, otterrai lo stesso risultato di un’installazione pulita.

::: tip
Quando Nomad carica un file all’avvio, sposta sempre il file nella cartella `can_be_deleted/`.
Se l’operazione riesce, il file viene spostato di nuovo nella cartella originale.

Se va in crash prima che il caricamento sia terminato, allora Nomad si avvierà correttamente al prossimo avvio, perché ignora la cartella `can_be_deleted/`.

Puoi semplicemente provare a caricare di nuovo questo file se pensi che possa andare a buon fine.
:::
# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Piattaforma {#platform}
### Dove si trovano i miei progetti sul dispositivo? {#locate}
I progetti si trovano nella cartella `projects`, all'interno della cartella principale di Nomad.

Su iOS, puoi accedere alla cartella di Nomad con l'app File di iOS.

Su Android, la cartella di Nomad si trova in `Android/data/com.stephaneginier.nomad/files/`.  
Sulle versioni recenti di Android (10/11) non hai più accesso alla cartella `Android/data`.
Puoi accederci tramite un'app separata, per esempio [questa](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Si può partecipare ai beta test? {#beta}
Per Windows e MacOS, potrebbe essere disponibile una beta sulla [Homepage](https://nomadsculpt.com).
<br>
Per iOS c'è un TestFlight privato: passa sul [Discord](https://discord.com/invite/8h7BwpRz29), nel canale #beta-ios.
<br>
La [Demo web](https://nomadsculpt.com/demo) di solito è aggiornata con le ultime funzionalità.

### Perché c'è una prova gratuita su Android e non su iOS? {#android-trial}
Perché i vecchi dispositivi Android sono pessimi (e anche alcuni recenti...), e non volevo che le persone comprassero l'app per poi trovarsi davanti a uno schermo nero.
Ma il motivo principale è che le app Android a pagamento non mi sembrano proprio la norma.

### Qual è il miglior tablet per Nomad? {#best-tablet}

In breve: un iPad.

La risposta un po' più lunga è

> "L'iPad più recente _che ti puoi permettere_, a meno che tu non detesti proprio Apple: in quel caso, il tablet Samsung più recente che ti puoi permettere. Per tutto il resto, prova prima."

Le persone vogliono sempre più informazioni, quindi ecco un riassunto.

Nomad funziona al meglio sugli iPad più recenti:

* iPad e iPhone hanno accesso al plugin [Quad Remesher](tools#quad-remesher) di [Exoside](https://exoside.com/)
* gli iPad recenti con l'ultima Pencil supportano il [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0): in alcuni strumenti di Nomad puoi ruotare la Pencil su se stessa.
* le prestazioni degli ultimi chip della serie M sono molto elevate.

L'iPad più recente e più costoso disponibile renderizza le immagini finali molto in fretta e ti permette di scolpire tantissimi dettagli.

Però il calo di prestazioni con gli iPad più economici e più vecchi non è così forte come si pensa. Qualsiasi iPad che supporta una Apple Pencil fa girare Nomad piuttosto bene. Per esempio:

* Un iPad Pro del 2023 gestisce sculture da 5 milioni di poligoni restando reattivo, e renderizza un'immagine di qualità finale in 5 secondi.
* Un iPad Pro del 2015 gestisce un oggetto da 1,2 milioni di poligoni con un po' di rallentamento, e renderizza un'immagine di qualità finale in 20 secondi.

È una bella differenza di prestazioni, ma devi tenere conto anche del prezzo:

* L'iPad Pro del 2025 costa *2500 USD* nuovo, con tutte le opzioni.
* L'iPad Pro del 2023 costa attualmente *400 USD* su eBay.
* L'iPad Pro del 2015 costa *250 USD* su eBay.

Avere 4 milioni di poligoni in più e risparmiare 15 secondi vale 2100 dollari? Sta a te deciderlo.

I modelli non Pro possono costare ancora meno e offrono un'ampia scelta di dimensioni e prestazioni. L'attuale iPad Air supporta la Pencil di seconda generazione con il barrel roll, e costa molto meno del Pro. Il mercato dell'usato e del ricondizionato offre ancora più opzioni.

Quindi, qualunque sia il tuo budget, dovresti riuscire a trovare l'iPad che fa per te. E ricorda che la maggior parte delle sculture non ha milioni di poligoni! Se resti sotto i 500.000 poligoni, anche i vecchi iPad ti permettono di scolpire in modo fluido.

`E Android?`

Le prestazioni grafiche di Android sono inferiori a quelle degli iPad. Secondo lo sviluppatore di Nomad, "un Samsung Galaxy Tab S9 fa girare Nomad un ordine di grandezza più lentamente di un iPad Air". Detto questo, molti utenti sono molto contenti dei loro tablet Samsung: Nomad funziona bene per la maggior parte del lavoro di scultura.

Per gli altri tablet Android, fai attenzione. Le prestazioni dell'hardware Android variano molto, ed è difficile prevedere come girerà Nomad.

Prova prima con la versione gratuita di Nomad, quella senza salvataggio.

`E la memoria e lo spazio di archiviazione?`

La maggior parte dei file di Nomad pesa 100 MB o meno. Questo significa che quasi ogni tablet in commercio oggi, iPad o Android, ha spazio in abbondanza per i tuoi progetti Nomad.


### Ho comprato Nomad per un dispositivo, posso usarlo su un altro? {#multi-devices}
Sì, purché usi lo stesso store di app e lo stesso account.

Per esempio, se l'hai comprato sull'App Store di iOS, puoi usarlo sugli altri tuoi dispositivi iOS.

Se l'hai comprato per il tuo tablet Android su Google Play, puoi usarlo sugli altri tuoi dispositivi Android.

Se invece hai comprato Nomad su Android e poi prendi un iPad, dovrai comprarlo di nuovo.

Questo perché Nomad non ha un proprio server di licenze né un modello in abbonamento. Non esiste alcun accordo tra Apple/Google/AppGallery per condividere le licenze.


### Come ripristino il mio acquisto? {#restore}
Google Play e AppGallery gestiscono entrambi la sincronizzazione in automatico.

- Vai nel menu Info (l'icona di Nomad in alto a sinistra) e tocca `Ripristina acquisto`
- Verifica di aver effettuato l'accesso con lo stesso account che hai usato per comprare Nomad (su Google Play).
- Riavvia il dispositivo
- A volte bisogna aspettare un paio d'ore
- Assicurati che l'app Google Play sia aggiornata
- Reinstalla Nomad (ricordati di [fare un backup dei tuoi file](#locate) se non vuoi perdere nulla)
- Puoi provare ad acquistare di nuovo per vedere cosa succede (nota: non puoi comprare due volte lo stesso articolo con lo stesso account)

:::tip
Puoi contattarmi a <support@nomadsculpt.com>, ma l'*unica* cosa che potrò fare è confermare se a un indirizzo email è associato un acquisto.

Ricevo regolarmente segnalazioni di licenze che non si aggiornano correttamente dopo il passaggio a un nuovo dispositivo.
Non ho alcun controllo sul pagamento e sulla sincronizzazione degli account: è tutto gestito da Google/AppGallery!

Alla fine l'acquisto viene sempre ripristinato, ma non è chiaro quali passaggi servano per velocizzare la cosa.
:::

::: warning
I dispositivi Huawei recenti non hanno accesso ai servizi Google.
In quel caso dovrai acquistare di nuovo l'app su AppGallery (lo store di app di Huawei).
:::

### Puoi tradurre o correggere [la-mia-lingua]? {#locale}
Posso aggiungere una nuova lingua in modo relativamente semplice, ma mi affido alla traduzione con l'IA, perché è molto più facile da gestire con gli aggiornamenti frequenti.
I file di traduzione si trovano [qui](https://github.com/stephomi/nomad-translation).

## Funzionalità {#features}

### Perché il gizmo non si muove? {#gizmo-not-moving}
Forse hai attivato [Fissa nella barra degli strumenti del menu a sinistra](tools#left-menu-toolbar).

### Si può animare in Nomad? {#animate}
Per ora no. Una timeline che permetta di animare i livelli potrebbe essere interessante, ma al momento non è proprio in programma.

Mi piacerebbe supportare rigging/skinning in futuro, ma pone alcune difficoltà (in particolare l'interazione con gli strumenti di scultura...), quindi per ora non c'è nulla di sicuro.


### Si può fare una vera modellazione low poly? {#lowpoly}
Per ora no.
Non rientra davvero negli obiettivi di Nomad *Sculpt*, ma forse in futuro aggiungerò qualche strumento.


### Si possono fare UV e texture? {#texturing}
Risposta breve: sì. Risposta lunga: non direttamente, ma ci sono diversi modi per combinare gli ottimi strumenti di pittura sui vertici di Nomad con UV e texture.

* Nomad ti permette di dipingere colore, rugosità e proprietà del materiale direttamente nei vertici della scultura.
* Nomad permette un numero di vertici molto alto, così puoi dipingere senza preoccuparti degli UV.
* Nomad può caricare texture da usare nei pennelli, per applicare impronte e dipingere con le texture.
* Nomad può caricare oggetti a cui sono già assegnate delle texture, per il rendering.
* Nomad può fare lo [sviluppo UV](topology.md#uv-unwrap-uvatlas) degli oggetti con pochi poligoni.
* Colore/rugosità/metallicità si possono trasferire dalle texture ai vertici con [le opzioni di proiezione](topology.md#reproject-to-vertex).
* Colore/rugosità/metallicità/normali si possono trasferire (bake) dai vertici alle texture con [le opzioni di trasferimento](topology.md#bake-texture)
* Il bake e la proiezione si possono fare tra singoli oggetti o tra molti oggetti, oppure tra il livello di suddivisione più alto e quello più basso di uno stesso oggetto, il che permette tanti flussi di lavoro diversi.
* Dopo il bake, esportando un OBJ vengono esportate anche le texture, che puoi portare in un'app come Procreate per dipingerci sopra direttamente.

### Posso registrare un video su piattaforma girevole? {#video}
Per ora non è previsto, ma iOS ha una [funzione di registrazione dello schermo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) molto facile da usare.

Su iOS, scorri verso il basso dall'angolo in alto a sinistra e tocca il pulsante di registrazione. Parte un conto alla rovescia di 3 secondi: chiudi il menu per tornare a Nomad e usa la funzione piattaforma girevole. Quando hai finito, scorri di nuovo verso il basso dall'angolo in alto a destra e tocca di nuovo il pulsante di registrazione. Modifica il filmato dalla libreria Foto per togliere le parti in eccesso all'inizio e alla fine del video.

### Puoi aggiungere [la-mia-funzione-preferita] come pulsante principale? {#interface}
Sì: ora puoi personalizzare la barra degli strumenti in basso dal menu [Interfaccia](interface.md#shortcuts), e puoi creare barre degli strumenti fluttuanti.

### Quali sono le prossime funzionalità? {#next-features}
Per la roadmap a medio/lungo termine ho tante idee, ma non so ancora.

La correzione dei bug e il miglioramento delle funzioni esistenti avranno sempre la priorità sull'aggiunta di nuove funzionalità.


### Si può fare il rigging in Nomad? {#rigging}
No, ma è in programma. Per ora puoi imparentare le forme tra loro e modificare i punti di pivot, per ottenere semplici sculture in posa.

### Si possono usare più di 4 luci? {#lights}
Puoi usare fino a 4 luci su mobile e fino a 6 su desktop. È un limite del motore di rendering in tempo reale di Nomad. Puoi aggirarlo usando oggetti emissivi e l'illuminazione globale del post processing, come mostrato in [questo tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Si possono importare gli strumenti di ZBrush? {#zbrush-import}
No, ZBrush usa un formato proprietario. Dovresti però riuscire a estrarre le mappe alfa e usarle in Nomad.

### Perché i colori non corrispondono a quelli che ho dipinto? Perché non riesco a ottenere il bianco nel render? {#paint-pbr}
Immagina di fotografare un foglio di carta, poi una lampada da scrivania, poi il sole. Le fotocamere e gli schermi più vecchi li renderebbero tutti semplicemente "bianchi". I sistemi più moderni sanno mostrare la differenza tra il bianco riflesso della carta, la luce emessa da una lampada e la luminosità estrema del sole.

La grafica computerizzata moderna cerca di funzionare in modo simile, imitando la fisica della luce e delle superfici. Si chiama `Physically Based Rendering`, o PBR, e il renderer PBR di Nomad si basa su questo principio. Il risultato è realistico ed equilibrato, ma spesso i colori dipinti molto chiari appaiono più scuri.

Se vuoi che il render si avvicini di più ai colori dipinti, puoi rimediare sia in modo non fisicamente basato sia in modo fisicamente basato:

Senza PBR:
* `Usa la modalità 'Non illuminato' nel menu Shading`. I colori vengono mostrati esattamente come li hai dipinti, ma perdi anche tutto lo shading. Comodo per controlli rapidi e per un risultato più grafico.
* `Usa la modalità 'MatCap' nel menu Shading`. Scegli un matcap più chiaro, quasi bianco, senza tinte di colore.

Con PBR:
* `Usa un ambiente neutro`. Puoi [cambiare l'ambiente](shading.md#environment) con uno più neutro. Evita gli ambienti interni, che tendono a essere più colorati, e preferisci un ambiente esterno di giorno o uno studio.
* `Aumenta l'illuminazione`. Se stessi fotografando un foglio bianco in una stanza buia, aggiungeresti semplicemente più luce. Sulla luce d'ambiente, alza il cursore dell'esposizione finché i colori non ti sembrano giusti, oppure aggiungi altre luci con un'intensità maggiore.
* `Aumenta l'esposizione della fotocamera`. Se nella stanza buia non ci fossero altre luci, potresti tenere aperto l'otturatore più a lungo o usare una sensibilità ISO più alta. In Nomad puoi ottenere un risultato simile con il post processing: vai su Post processing, attivalo, scendi fino a Mappatura dei toni, attivala e alza il cursore dell'esposizione finché i colori non ti sembrano giusti.
* `Usa un colore emissivo`. Nel menu Materiale puoi attivare "Emissivo" sotto le texture, così l'oggetto sembrerà una fonte di luce. Se attivi l'illuminazione globale nelle impostazioni di post processing, l'oggetto proietterà luce sugli altri oggetti della scena. Puoi anche attivare "Sempre non illuminato" per quel materiale, per ottenere un aspetto simile senza texture.

## Crash {#crashes}

### L'app si chiude quando salvo o faccio il remeshing del modello! {#crash-remesh}
Il dispositivo sta esaurendo la memoria (RAM).  
Per ridurre l'uso di memoria della scena, puoi usare alcune opzioni di [Topologia](topology.md) per diminuire il numero di poligoni.

::: tip RAM/spazio di archiviazione
Quello che conta è la quantità di RAM, non lo spazio di archiviazione (che di solito è molto più grande).
:::


### L'app si chiude quando carico il mio progetto! {#crash-load}
Se il file è piccolo, puoi mandarmelo e gli darò un'occhiata (via email a <support@nomadsculpt.com>).

Altrimenti è probabile che il dispositivo stia esaurendo la RAM.

- Assicurati di chiudere tutte le altre app aperte sul dispositivo.
- Inizia un nuovo progetto in Nomad invece di avere un progetto già aperto.
- Se l'app si chiude ancora, l'unica soluzione è caricare [il file del tuo progetto](#locate) su un dispositivo con più memoria.

::: tip
Se il tuo dispositivo mobile non riesce a caricare il progetto, prova la [versione desktop](https://nomadsculpt.com). Puoi usarla gratis in modalità Demo per importare ed esportare progetti, anche se sono disponibili solo pochi strumenti di modifica.

Se il progetto usa i [Livelli](layers.md), conviene unirli per ridurre l'uso di memoria.
:::

### L'app si chiude quando avvio Nomad! {#crash-start}
Se l'app si chiude durante il caricamento, significa che Nomad ha problemi con un certo file presente nella cartella di Nomad.

Il più delle volte succede perché il progetto è pesante e purtroppo supera il limite di RAM.

Trova la [cartella di Nomad](#locate), poi rinomina o sposta alcuni file per scovare il colpevole.

Per prima cosa, prova a rinominare `settings.json`. Così Nomad smetterà di caricare l'ultimo progetto.

Se non funziona, prova a spostare alcuni file recenti fuori dalle rispettive cartelle di risorse (`projects`, `matcaps`, `environments`, ecc.).

Puoi anche rinominare le cartelle stesse, in modo che Nomad le ignori del tutto.
Se rinomini o sposti tutti i file nella cartella di Nomad, il risultato è lo stesso di un'installazione pulita.

::: tip
Quando Nomad carica un file all'avvio, lo sposta sempre nella cartella `can_be_deleted/`.
Se l'operazione riesce, il file viene rimesso nella sua cartella originale.

Se l'app si chiude prima della fine del caricamento, al successivo avvio Nomad partirà senza problemi, perché ignora la cartella `can_be_deleted/`.

Puoi semplicemente provare a caricare di nuovo questo file, se pensi che possa funzionare.
:::

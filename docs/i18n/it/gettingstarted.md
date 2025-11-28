# Per Iniziare {#getting-started}

## Benvenuto in Nomad! {#welcome-to-nomad}

Nomad è un’app di scultura 3D che funziona su molti dispositivi, e dà il meglio di sé sui tablet con pennino sensibile alla pressione, ad esempio un iPad con Apple Pencil, o un Samsung Galaxy Tab con pennino.

È ispirata alle app di scultura per desktop come ZBrush e Blender, con un’interfaccia facile da capire, senza sacrificare le funzionalità. Se hai già usato app di scultura 3D, Nomad ti sembrerà molto familiare.

Se è la prima volta che fai scultura 3D, è utile conoscere alcune basi.

::: tip Preferisci i video?
Su YouTube ora ci sono MOLTI video tutorial per principianti, ecco alcuni ottimi link:

* [Nomad Sculpt Crash Course di Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Tutorial per principianti di Nomad Sculpt di Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Serie NOMAD FOR BEGINNERS di SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Vale la pena controllare il canale principale di questi creatori, pubblicano spesso nuovi tutorial.
:::

## La tua prima scultura {#your-first-sculpt}

Quando avvii Nomad per la prima volta vedrai una sfera sullo schermo. Trascina semplicemente il pennino sulla sfera per iniziare a scolpire. La simmetria è attivata per impostazione predefinita per rendere la scultura più semplice.

![](/videos/gettingstarted_01.mp4)

Per rendere il pennello più grande o più piccolo, usa il cursore del raggio sulla sinistra.

![](/videos/gettingstarted_02.mp4)

Per rendere il pennello più forte o più debole, usa il cursore di intensità sulla sinistra.

![](/videos/gettingstarted_03.mp4)

Lo strumento predefinito è il `Clay tool`, e aggiunge materiale alla superficie. Per sottrarre dalla superficie, tocca il pulsante `Sub` sulla sinistra. Per tornare ad aggiungere materiale, tocca di nuovo il pulsante Sub.

![](/videos/gettingstarted_04.mp4)

Per levigare la superficie, tocca il pulsante `Smooth`. Per tornare alla scultura normale, tocca di nuovo il pulsante Smooth.

![](/videos/gettingstarted_05.mp4)

Per ruotare intorno al modello, trascina nello spazio vuoto fuori dal modello.

![](/videos/gettingstarted_06.mp4)

Per eseguire lo zoom, usa il gesto di pizzico/zoom con due dita.

![](/videos/gettingstarted_07.mp4)

Per traslare la camera, appoggia 2 dita sullo schermo e trascina.

![](/videos/gettingstarted_08.mp4)

Se commetti un errore, un tocco con 2 dita annullerà l’azione, oppure usa il pulsante di annullamento in basso a sinistra. 

![](/videos/gettingstarted_09.mp4)

::: tip Versione desktop
Su desktop, il tasto alt/opt viene usato per controllare la camera:

* tip trascina nello spazio vuoto = ruota la camera
* alt+tip trascina = trasla
* alt+tip trascina, poi rilascia alt = zoom (come in ZBrush)

Con tavolette Wacom che hanno 2 o più pulsanti sulla penna, usa le impostazioni Wacom per configurare la punta e i pulsanti in questo modo:

* tip = clic sinistro
* rocker inferiore = clic centrale
* rocker superiore = clic destro

Con queste impostazioni, puoi manipolare la camera solo con la penna:

* rocker superiore e movimento in hover = ruota la camera
* rocker inferiore e movimento in hover = trasla
:::

## Aggiungi colore {#add-color}

Nomad ti permette di dipingere la superficie della tua scultura. Dal menu degli strumenti sulla destra, trova lo strumento `Paint` e cliccalo. Sulla barra degli strumenti a sinistra apparirà una sfera colorata. Cliccala, si aprirà un selettore di colore. Scegli un colore e dipingi sul tuo modello.

![](/videos/gettingstarted_10.mp4)

Per cancellare, tocca il pulsante `Erase` sulla barra degli strumenti di sinistra, poi cancella sulla superficie. Tocca di nuovo il pulsante erase per tornare in modalità pittura.

![](/videos/gettingstarted_11.mp4)

Usando il pennello clay in modalità add/sub, smooth e paint, prova a creare una semplice testa cartoon:

![](/images/gettingstarted_head1.webp)

## Altri strumenti {#other-tools}

La palette degli strumenti ha molti strumenti per aiutarti nella scultura. Finora hai usato il pennello clay (lo strumento predefinito), smooth e paint. Poiché smooth è usato spesso, ha una scorciatoia extra nella barra degli strumenti a sinistra.

Gli strumenti in Nomad possono fare una grande varietà di cose, da strumenti legati alla scultura come move, crease, inflate, a strumenti come split e trim che sono più simili a utensili da falegnameria o lavorazione dei metalli. La pagina [Tools](tools.md) contiene maggiori informazioni.

Vedi se riesci a usare gli strumenti move, crease, inflate e smooth per aggiungere più dettagli alla tua testa, cambiandone la forma:

![](/images/gettingstarted_head2.webp)

Ora che conosci le basi di Nomad, diamo un’occhiata al resto dell’interfaccia.

## Interfaccia {#interface}

![](/images/interface_overview1.webp)

* `Menu superiori` - I menu per accedere alla maggior parte delle funzionalità di Nomad. I menu in alto a sinistra riguardano principalmente le funzioni di scena e oggetto, quelli in alto a destra sono relativi agli strumenti. Sugli schermi più piccoli questi menu verranno compressi insieme per risparmiare spazio.
* `Statistiche` - Informazioni sulla scena, sull’oggetto corrente, sullo stato della maschera, sull’uso della memoria.
* `Nav Cube` - Un aiuto per mostrare da che lato della scultura stai guardando, oltre a una scorciatoia per saltare a diverse viste. Toccando il cubo la vista salterà al lato toccato. Trascinando il cubo lo ruoterai. Tocca le piccole icone a lato del cubo per inquadrare l’oggetto corrente o resettare alla vista iniziale predefinita.
* `Toolbox` - Gli strumenti di Nomad sono disponibili in quest’area scorrevole.
* `Barra degli strumenti sinistra` - Cursori per raggio e intensità per la maggior parte degli strumenti, pulsanti contestuali per altri strumenti, e scorciatoie per simmetria, modalità alt/sub dello strumento, mascheratura, smoothing, gizmo e opzioni di pittura.
* `Barra degli strumenti inferiore` - Scorciatoie per le funzioni usate più spesso, spiegate qui sotto.

::: tip Mancino?
Puoi invertire il posizionamento e l’ordine di tutte le barre degli strumenti, vedi [Mirror top bar](interface.md#mirror-top-bar) e altre opzioni correlate.
:::

## Barra degli strumenti inferiore {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Undo` - annulla l’ultima operazione
* `Redo` - ripristina l’ultima operazione annullata
* `History` - accedi alle opzioni di cronologia, spiegate nel menu [History](history.md).
* `Solo` - Attiva/disattiva la visualizzazione del solo oggetto corrente o di tutti gli oggetti
* `X-Ray` - Fa sì che tutti gli altri oggetti vengano renderizzati in modalità raggi X, e l’oggetto corrente in modo solido. Una pressione prolungata o uno swipe verso l’alto ti permetteranno di impostare colore e opacità della modalità raggi X.
* `Voxel` - Una scorciatoia per il pulsante di [Voxel Remesher](topology.md#voxel-remesher). Una pressione prolungata o uno swipe verso l’alto riveleranno scorciatoie per impostare la qualità del voxel remesh.
* `Grid` - Attiva/disattiva la visualizzazione della griglia. Una pressione prolungata o uno swipe verso l’alto riveleranno le opzioni per la griglia.
* `Wire` - Attiva/disattiva una sovrapposizione wireframe. Una pressione prolungata o uno swipe verso l’alto riveleranno le opzioni per il wireframe.
* `Inspect` - Attiva/disattiva la visualizzazione di dati extra sulla mesh corrente. Per impostazione predefinita mostrerà le UV, ma una pressione prolungata o uno swipe verso l’alto ti permetteranno di ispezionare altre proprietà se esistono, e se queste vengono visualizzate sullo sfondo o sulla mesh.

## Prossimi passaggi {#next-steps}

Cosa imparare dopo dipende da te, e da ciò che trovi interessante! Ecco alcuni suggerimenti:

Vuoi imparare di più sugli strumenti di scultura? Vai alla sezione [Tools](tools.md).

Vuoi esportare i tuoi modelli? O importare modelli su cui scolpire? O creare immagini delle tue sculture? Vai alla sezione [Files](files.md).

Vuoi imparare di più sul controllo del dettaglio nella tua scultura? Vai alla sezione [Topology](topology.md) e scopri multires e decimation.

Vuoi lavorare con più oggetti? Combinare oggetti semplici e primitive in una scena più grande? Vai alla sezione [Scene](scene.md).

Vuoi imparare *tutto* su Nomad? Ottima scelta! Questo manuale copre tutto Nomad, include molti suggerimenti e trucchi, e ha un’ottima funzione di ricerca in alto. Usa la navigazione a sinistra per saperne di più.

Se preferisci i video, Holger Schönischka ha realizzato una grande raccolta di suggerimenti e trucchi per Nomad su YouTube: https://www.youtube.com/@ProcreateFX/videos


## Ottenere aiuto {#getting-help}

Se hai ancora domande dopo aver letto il manuale e guardato i video tutorial, ci sono tre modi principali per parlare con altri utenti di Nomad o con lo sviluppatore di Nomad:

* Visita i forum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Unisciti alla chat Discord di Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contatta direttamente lo sviluppatore all’indirizzo support@nomadsculpt.com
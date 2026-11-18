# ![](/icons/symmetry.webp) Simmetria {#symmetry}

Questo menu controlla come i tratti vengono ripetuti oltre un piano di specchio, in modo radiale o a tasselli, e offre dei modi per ripristinare la simmetria sugli oggetti non simmetrici.

![](/images/symmetry_overview.webp) 

## Panoramica {#overview}
Puoi usare la simmetria in diversi modi:

* Come uno specchio, ribaltando il lavoro lungo X (sinistra/destra), Y (alto/basso), Z (dietro/davanti) o una loro combinazione. 
* La simmetria radiale si imposta su X Y Z con un numero di ripetizioni, per esempio per scolpire una stella marina. 
* La tassellatura ripete i tratti lungo l'oggetto, così la scultura si ripete senza giunture visibili.
* Gli specchi possono lavorare attorno all'origine (modalità mondo) o attorno al centro di un oggetto (modalità locale).
* Una scultura nata non simmetrica può essere resa simmetrica a forza.

Trovi anche una scorciatoia per attivare/disattivare la simmetria nel pannello rapido a sinistra (*"Simm"*). La piccola 'L/W' indica se Nomad è in modalità di simmetria Locale o Mondo. Puoi anche tenere premuto o trascinare verso il centro dello schermo per far apparire un menu.

![](/images/symmetry_button.webp) 

Le impostazioni di simmetria vengono salvate con ogni oggetto, e il titolo del menu mostra il nome dell'oggetto che stai modificando.
Gli strumenti di scultura condividono lo stesso stato attivo/disattivo, mentre gli strumenti di trasformazione ([Trasforma](tools.md#transform) e [Gizmo](tools.md#gizmo)) hanno il loro.

::: tip
Il menu Simmetria serve soprattutto a controllare la simmetria dei tratti. Puoi anche specchiare e ripetere gli oggetti con i [ripetitori del menu Scena](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Abilitato {#enabled}
Attiva o disattiva la modalità specchio: è lo stesso pulsante `Simm` del pannello rapido a sinistra. Un'icona di avviso ti ricorda quando è spenta, e il menu ti segnala anche quando lo strumento attuale ignora la simmetria.

## Piani {#planes}

Abilita uno o più piani di simmetria e il numero di ripetizioni per la simmetria radiale. Non sei obbligato a scegliere un solo piano: puoi abilitarne 1, 2 o tutti e 3 per una simmetria complessa.

La riga `Radiale` imposta il numero di ripetizioni della simmetria radiale attorno a ciascun asse. Anche qui non sei limitato a un solo asse, e puoi perfino combinarla con la simmetria a piani per ottenere risultati ricchi di dettagli molto in fretta. (Il numero totale di ripetizioni è limitato a 200)

![](/videos/symmetry_demo.mp4) 

## Tassello {#tile}

Ripete i tratti lungo un asse, a distanza regolare, così la scultura si ripete senza giunture. Comodo per motivi decorativi, mattoni o una texture che vuoi ripetere.

Attiva la tassellatura per ogni asse con i pulsanti `Tassello`, poi imposta un `Conteggio` (quante ripetizioni coprono l'oggetto) oppure una `Distanza` (lo spazio tra due ripetizioni). Tocca l'interruttore a sinistra per passare dall'uno all'altra.

## Metodo {#method}
Lo specchio può essere `Locale`, e si sposta con l'oggetto, oppure `Mondo`, e resta fermo. Se non sai quale modalità ti serve, osserva gli indicatori del piano di specchio e della simmetria radiale sovrapposti all'oggetto. In modalità locale, se usi gli strumenti di trasformazione (`Gizmo` o `Trasforma`) e sposti il modello, anche gli indicatori dello specchio si spostano. In modalità mondo, gli indicatori restano fissi e l'oggetto ci scorre attraverso.

## Specchio {#mirroring}
![](/images/symmetry_mirroring.webp)

Scolpendo vicino ai piani di simmetria, alcuni pennelli hanno un comportamento simmetrico imperfetto. Questa sezione ti permette di ripristinare la simmetria copiando un lato della scultura sull'altro. 

`Direzione` - I due pulsanti a freccia accanto al titolo `Specchio` stabiliscono quale lato viene copiato sull'altro. Nomad lo calcola dalla vista attuale, così il lato resta lo stesso sullo schermo da qualunque parte guardi il modello.

![](/icons/shield.webp) `Maschera` - Il pulsante maschera ti permette di isolare ciò che verrà specchiato: mascherare il lato di destinazione protegge quella zona, mascherare il lato di origine impedisce che quella zona venga specchiata sulla destinazione. 

![](/icons/tool_hide.webp) `Nascondi` - Quando è attivo, le zone nascoste sul lato di origine non vengono specchiate sulla destinazione. 

`Specchio` (Mantieni topologia) cerca di capire se la topologia è uguale sui due lati dello specchio e, in quel caso, si limita a spostare i vertici. È il caso più comune. La simmetria radiale viene ignorata. Se la topologia non è simmetrica, Nomad ti propone di forzare la specchiatura con `Taglia • Specchio`.

I pulsanti `Taglia` tagliano l'oggetto lungo il piano (o i piani) di simmetria. Modificano la topologia, quindi sono più distruttivi di `Specchio`. Il numero su ciascun pulsante indica quanti oggetti ottieni:

* `Taglia` - rimuove un lato dell'oggetto.
* `Taglia • Specchio` - taglia l'oggetto, copia un lato, lo specchia sull'altro e salda i vertici lungo lo specchio. A volte questo metodo è necessario, se il modello è molto diverso tra i due lati.
* `Taglia • Dividi` - taglia l'oggetto e tiene ogni lato come oggetto separato.
* `Taglia • Specchio • Dividi` - come `Taglia • Specchio`, ma ogni lato diventa un oggetto separato.

Se sono selezionati più oggetti, `Specchio` e [Rifletti oggetto](#flip-object) si applicano a tutti.

### Rifletti oggetto {#flip-object}
![](/images/symmetry_flip.webp)
Porta il lato sinistro a destra e viceversa, lungo `X`, `Y` o `Z`. Il risultato è simile a quello che otterresti impostando la scala a -1 su X dal menu dello strumento Gizmo.

## Ripristina e modifica {#reset-and-edit}

![](/images/symmetry_edit.webp)

È possibile modificare la posizione e l'orientamento della simmetria (ma non è consigliato!). Se serve, `Centro del mondo` (`Centro dell'oggetto` in modalità locale) e `Orientamento` riportano la posizione e l'orientamento della simmetria ai valori predefiniti.

Di solito Nomad sa dove mettere il piano di simmetria. Non è consigliato regolarlo a mano, ma il pulsante `Gizmo` (`Modifica`) lo permette agli utenti esperti. Quando lo premi, compare un gizmo che ti permette di traslare e ruotare il piano di simmetria. Per tornare al centro e all'orientamento predefiniti, usa i pulsanti di ripristino qui sopra.

`Da perno` mette il piano di simmetria sul pivot dello strumento [Gizmo](tools.md#gizmo). È disponibile solo mentre lo strumento `Gizmo` è attivo.

Il comportamento di queste opzioni cambia a seconda dello spazio (*Locale/Mondo*) in cui ti trovi.
Quindi, se qualcosa non funziona come ti aspetti, controlla di essere nello spazio giusto.

::: tip
Modificare il piano di simmetria con il gizmo è un po' sperimentale: probabilmente non ti servirà mai!
:::

## Opzioni di visualizzazione {#show-options}
![](/images/symmetry_show.webp)


`Mostra linea` e `Mostra piano` attivano o disattivano la sovrapposizione nella vista che indica dove si trova la simmetria. Nota che disattivare queste opzioni ha effetto solo quando il menu Simmetria è chiuso.

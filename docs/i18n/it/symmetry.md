# ![](/icons/symmetry.webp) Simmetria {#symmetry}

Questo menu controlla come i tratti verranno ripetuti attraverso un piano a specchio o radialmente, e i modi per ripristinare la simmetria su oggetti non simmetrici.

![](/images/symmetry_overview.webp) 

## Panoramica {#overview}
Puoi usare la simmetria in diversi modi:

* Come uno specchio, ribaltando il lavoro sugli assi X (sinistra/destra), Y (alto/basso), Z (dietro/davanti), o una combinazione di essi. 
* La simmetria radiale può essere impostata su X Y Z con un numero di ripetizioni, ad esempio per scolpire una stella marina. 
* Gli specchi possono operare attorno all’origine (chiamata modalità mondo) o attorno al centro di un oggetto (chiamata modalità locale).
* Scolpiture iniziate senza simmetria possono essere forzate a diventare simmetriche.

Una scorciatoia per abilitare/disabilitare la simmetria si trova anche nel pannello rapido a sinistra (*"Sym"*). La piccola “L/W” indica se Nomad è in modalità di simmetria Locale o Mondo. Puoi anche tenere premuto a lungo o scorrere verso il centro dello schermo per far apparire un menu.

![](/images/symmetry_button.webp) 

Questa è un’opzione globale, quindi lo stato verrà mantenuto tra i diversi strumenti.
Le uniche eccezioni sono gli strumenti di trasformazione ([Sposta](#translate), [Ruota](#rotate), [Scala](#scale) e [Gizmo](#gizmo)) che hanno il proprio stato di simmetria.

::: tip
Il menu di simmetria serve principalmente a controllare la simmetria dei tratti. Puoi anche specchiare e ripetere oggetti tramite i [ripetitori presenti nel menu scena](scene#repeaters). 
:::

## Abilitato {#enabled}
Attiva/disattiva la modalità specchio, è la stessa del pulsante `Sym` nel pannello rapido a sinistra. 

## Piani {#planes}

Abilita uno o più piani di simmetria e il numero di ripetizioni per la simmetria radiale. Nota che non devi scegliere un solo piano: puoi avere 1, 2 o 3 piani abilitati per una simmetria complessa.

L’asse e il conteggio delle ripetizioni per la simmetria radiale. Nota che anche questi non sono limitati a un singolo asse e possono persino funzionare in combinazione con la simmetria per piani per generare risultati dettagliati molto rapidamente. (Il numero totale di ripetizioni è limitato a 150)

![](/videos/symmetry_demo.mp4) 

## Metodo {#method}
Lo specchio può essere “Locale”, e muoversi con l’oggetto, oppure “Mondo”, e rimanere fermo. Se non sei sicuro di quale modalità ti serva, osserva il piano a specchio e gli indicatori radiali sovrapposti all’oggetto. In modalità locale, se usi il gizmo di trasformazione e sposti il modello, anche gli indicatori dello specchio si muoveranno. In modalità mondo, gli indicatori dello specchio resteranno fissi e l’oggetto scivolerà attraverso di essi.

## Mirroring {#mirroring}
![](/images/symmetry_mirroring.webp)

Quando scolpisci vicino ai piani di simmetria, alcuni pennelli possono avere un comportamento di simmetria imperfetto. Questa sezione ti permette di ripristinare la simmetria copiando un lato della tua scultura sull’altro. 

`Direction` - I pulsanti `<<` e `>>` determinano quale lato verrà copiato sull’altro. Nomad lo calcola dalla tua vista corrente, quindi impostandolo su `<<` ad esempio copierà sempre da destra schermo a sinistra schermo.

![](/icons/shield.webp) `Mask` - Il pulsante maschera ti permette di isolare ciò che verrà specchiato; mascherare il lato di destinazione proteggerà quella regione, mascherare il lato sorgente impedirà a quell’area di essere specchiata sulla destinazione. 

![](/icons/tool_hide.webp) `Hide` - Quando attivo, le aree nascoste sul lato sorgente non verranno specchiate sulla destinazione. 

`Mirror` cercherà di identificare se la topologia è la stessa su entrambi i lati dello specchio e, in tal caso, sposterà solo i vertici. Questo è lo scenario più comune.

`Split & Mirror` essenzialmente taglierà l’oggetto lungo lo specchio, copierà un lato, lo specchierà sull’altro e salderà i vertici lungo lo specchio. È un’opzione più distruttiva e cancellerà la multirisoluzione, ma a volte questo metodo è necessario se il modello è molto diverso attraverso lo specchio.

### Capovolgi oggetto {#flip-object}
![](/images/symmetry_flip.webp)
Rende il lato sinistro il lato destro e viceversa. Simile, come risultato, a usare il menu dello strumento gizmo e impostare la scala a -1 sull’asse X.

## Reimposta e modifica {#reset-and-edit}

![](/images/symmetry_edit.webp)

È possibile modificare la posizione e l’orientamento della simmetria (ma non è consigliato!). Se necessario, `World center` e `Orientation` ripristineranno la posizione e l’orientamento della simmetria ai valori predefiniti.

Nomad di solito sa dove posizionare il piano di simmetria. Non è consigliato regolarlo manualmente, ma il pulsante `Gizmo (Edit)` lo permette agli utenti avanzati. Quando questo pulsante viene cliccato, viene mostrato un gizmo che ti permette di traslare e ruotare il piano di simmetria. Se vuoi ripristinare il centro e l’orientamento predefiniti, i pulsanti `object center` e `orientation` lo faranno.

Il comportamento di queste opzioni cambierà a seconda dello spazio (*Locale/Mondo*) in cui ti trovi.
Quindi, se non funziona come ti aspetti, assicurati di controllare di essere nello spazio corretto.

::: tip
Il pulsante `Gizmo (Edit)` è intenzionalmente disattivato come promemoria del fatto che probabilmente non dovresti usarlo!
:::

## Mostra opzioni {#show-options}
![](/images/symmetry_show.webp)


`Show line` e `Show plane` attivano/disattivano una sovrapposizione in viewport delle posizioni di simmetria. Nota che disattivare queste opzioni avrà effetto solo quando il menu di simmetria è chiuso.
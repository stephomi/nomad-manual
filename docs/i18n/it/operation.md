# ![](/icons/operation.webp) Operazione {#operation}

Questo menu applica un'operazione a tutta la superficie degli oggetti selezionati in un colpo solo: levigare, rilassare, lucidare, gonfiare, regolare i colori, sfocare o rendere più nitidi la pittura e la maschera.

![](/images/operation_overview.webp)

## Panoramica {#overview}

Un pennello agisce dove passi col tratto, mentre un'operazione agisce su tutti i vertici degli oggetti selezionati in una volta sola. Il titolo mostra il nome dell'oggetto, o il numero di oggetti quando ne sono selezionati diversi.

Ogni operazione è un cursore: trascinalo verso destra per applicarne di più, verso sinistra per applicarne di meno (o l'operazione opposta, per i cursori con una freccia su entrambi i lati). Il cursore torna a zero appena lo rilasci, e ogni trascinamento è un singolo passaggio nella [Cronologia](history.md), così puoi applicare un'operazione più volte a piccole dosi.

::: tip
Le operazioni sono un modo rapido per ripulire un'intera mesh dopo un remeshing voxel o un'operazione booleana: un po' di `Rilassa` uniforma i triangoli, un po' di `Leviga` toglie il rumore, senza dover andare a caccia di ogni punto col pennello.
:::

## Filtri {#filters}

I pulsanti in alto limitano le zone in cui si applicano le operazioni:

* `Maschera` - Le zone mascherate restano intatte.
* `Nascondi` - Le zone nascoste restano intatte.
* `Spostamento` - (Con un [livello](layers.md) selezionato) Vengono modificate solo le zone in cui il livello attivo contiene della scultura, così puoi levigare o gonfiare il contenuto di un livello senza toccare il resto.

## Levigatura {#smoothing}

* `Mantieni volume` - Leviga senza far restringere la superficie. Il pulsante a ingranaggio contiene i valori `Restringi` e `Gonfia` usati per farlo.
* `Mantieni bordi` - I vertici sul bordo della mesh (il contorno di un buco) restano fermi.
* `Levigatura stabile` - Cerca di rendere la levigatura indipendente dalla topologia. Funziona meglio quando la densità dei poligoni varia molto.
* `Leviga` - Leviga la superficie. Trascina verso sinistra per `Aumenta nitidezza` invece.
* ![](/icons/group.webp) `Leviga` - Leviga i confini tra i [gruppi di facce](tools.md#facegroup), raddrizzando i contorni frastagliati dei gruppi. Trascina verso sinistra per renderli più netti.
* `Rilassa` - Uniforma i poligoni, mantenendo la forma.
* ![](/icons/group.webp) `Rilassa` - Rilassa i poligoni lungo i confini dei gruppi di facce.
* `Mantieni angoli` - Con `Leviga` e `Rilassa` dei gruppi di facce, i confini restano fissi dove girano più di questo angolo, così gli angoli restano netti mentre i lati si levigano. Usa la sua casella di spunta per attivarlo.

## Polish {#polish}

Appiattisce la superficie in sfaccettature pulite, come lo strumento [Polish](tools.md#polish). `Angolo` stabilisce quali facce si appiattiscono insieme: le facce che si piegano meno di questo angolo diventano un'unica sfaccettatura. Un angolo più basso conserva più pieghe e sfaccettature più piccole.

## Gonfia {#inflate}

Spinge la superficie verso l'esterno lungo le sue normali, o verso l'interno quando trascini a sinistra. `Normale` (`Rilassa`) rilassa i poligoni nello stesso momento, così non si stirano; usa la sua casella di spunta per disattivarlo.

## Regolazioni del colore {#color-adjustments}

Scegli il canale da regolare, `Colore`, `Rugosità`, `Metallicità`, `Opacità`, `Densità` (la pittura della densità del [Quad Remesher](tools.md#quad-remesher), se l'oggetto ne ha) o `Maschera`, poi:

* `Esposizione` - Schiarisce o scurisce i valori.
* `Saturazione` - (Solo `Colore`) Colori più o meno vivaci.
* `Contrasto` - Allontana i valori tra loro, o li avvicina.
* `Tonalità` - Sposta i colori lungo la ruota dei colori.

## Sfoca {#blur}

Sfoca i canali selezionati su tutta la superficie: attiva `Colore`, `Rugosità`, `Metallicità`, `Opacità`, `Densità` o `Maschera`, poi trascina `Sfoca`. Trascina verso sinistra per `Aumenta nitidezza` invece.

Per la maschera, è lo stesso del cursore `Sfoca` dello strumento [Maschera](tools.md#mask). Qui però puoi sfocare anche i canali di pittura.

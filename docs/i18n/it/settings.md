# ![](/icons/cog.webp) Impostazioni 

Il menu delle impostazioni contiene molte opzioni per controllare l'aspetto e il comportamento di Nomad.

![](/images/settings_overview.webp)

## Impostazioni di visualizzazione
Questa sezione contiene scorciatoie di avvio rapido per la maggior parte delle impostazioni più in basso in questo menu.

![](/images/settings_display_settings.webp)

### Ombreggiatura morbida 
Attiva/disattiva l’ombreggiatura morbida o sfaccettata. Con l’ombreggiatura sfaccettata i poligoni sono ombreggiati in modo indipendente, così puoi vedere la topologia sottostante.
Può essere utile vedere l’ombreggiatura sfaccettata durante la fase di scolpitura, quindi passare all’ombreggiatura morbida per il rendering.

Disabilitare l’Ombreggiatura morbida migliora leggermente le prestazioni.

### Contorno
Attiva/disattiva un contorno sulla selezione corrente.

Questo è utile per avere un riscontro visivo sulla mesh o sulle mesh attualmente selezionate nel caso in cui [Scurisci non selezionati](#darken-unselected-objects) sia disattivato.

Dal punto di vista delle prestazioni, usare [Scurisci non selezionati](#darken-unselected-objects) è molto meglio che usare la soluzione del contorno.

### Griglia
Attiva/disattiva una griglia di sfondo, utile per comprendere il posizionamento e la scala degli oggetti.

### Due lati
Attiva/disattiva la visualizzazione dei poligoni su due lati. Tutte le facce puntano in una certa direzione.
Le facce considerate *retro* sono quelle che puntano “lontano” dal punto di vista della camera.

Per esempio, la sfera semplice di avvio avrà le sue facce rivolte verso l’esterno.
Se sposti la camera all’interno della sfera vedrai quindi il retro di queste facce.

La maggior parte delle volte non dovresti vedere il retro delle facce, quindi colorarle può aiutarti a rilevare potenziali problemi o topologia non corretta.

Disabilitare il rendering `due lati` può migliorare un po’ le prestazioni di rendering.


### Wireframe
Attiva/disattiva una sovrapposizione wireframe. 

Nota che abilitare il wireframe ridurrà le prestazioni.

### Cubo di scatto
Attiva/disattiva un’icona di supporto nell’angolo della scena, utile per orientarti nello spazio e passare rapidamente tra le viste fronte/retro/sinistra/destra/alto/basso.

### Mostra pittura
Attiva/disattiva la visualizzazione della pittura. Il materiale predefinito è un materiale bianco non metallico, con rugosità al 25%.

### Usa Nascondi
Attiva/disattiva la modalità di nascondimento. Quando è disattivata è comunque presente, solo disabilitata. Questo pulsante è disabilitato se stai usando lo strumento di nascondimento.

### Mostra Maschera
Attiva/disattiva la modalità maschera. Quando è disattivata è comunque presente, solo disabilitata. Premi di nuovo questo pulsante per riattivarla.

Se hai bisogno di nascondere la maschera E averla comunque attiva, usa il colore della maschera qui sotto e impostalo su bianco. Ricordati di riportarlo a un grigio quando hai finito!

Nota che questo pulsante è disabilitato se stai usando uno strumento maschera. 

### Maschera -> Opaca
Maschera -> opaca ignorerà i vertici trasparenti per le maschere mascherate. Questo è rilevante solo per l’opacità dei vertici e delle texture, le facce nascoste tramite “nascondi” rimarranno comunque nascoste.

### Evidenzia
Attiva/disattiva il lampeggio di evidenziazione della selezione. Quando selezioni oggetti, l’oggetto selezionato lampeggia temporaneamente in rosa acceso per 500 millisecondi. Il colore e la durata del lampeggio possono essere personalizzati qui sotto.

### Statistiche
Attiva/disattiva il testo di stato nella viewport 3D. Mostra informazioni sulla memoria di sistema, il conteggio totale dei vertici della scena e il conteggio dei vertici della selezione corrente.

----- 

### Scurisci oggetti non selezionati
Gli oggetti che non sono selezionati verranno scuriti in modo che la selezione corrente risalti.

### Maschera
Il colore usato per la mascheratura, di default un grigio medio, moltiplicato per il colore del tuo oggetto. Impostalo su bianco per rendere la maschera invisibile, ma ricordati di riportarlo a un grigio quando hai finito!

## ![](/icons/cursor.webp) Cursore

### Mostra cerchio durante la scolpitura
Continua a mostrare il raggio del pennello durante la scolpitura.

### Mostra piccolo punto
Mostra un punto al centro della pennellata durante la scolpitura, o quando il pivot della camera viene cambiato.

### Mostra stabilizzatore a corda
Disegna una linea per indicare la lunghezza della corda quando lo stabilizzatore “lazy rope” è attivo nelle impostazioni della pennellata.

## ![](/icons/cursor.webp) Indicatore
![](/images/settings_indicator.webp)

Mostra indicatori visivi per tutorial e registrazioni dello schermo.

I pulsanti `Dito`, `Stilo` e `Mouse` abilitano la visualizzazione di un’icona quando viene rilevato quel tipo di input.

### Colore
Il colore dell’indicatore.

### Dimensione/Icona/Cerchio
Controlli per regolare la dimensione dell’indicatore e le forme all’interno dell’indicatore.

## ![](/icons/wireframe.webp) Wireframe
![](/images/settings_wireframe.webp)
Attiva la sovrapposizione wireframe.

### Target
Imposta se gli oggetti non selezionati mostreranno il wireframe, oppure solo gli oggetti selezionati, o tutti gli oggetti.

### Nascondi
Imposta se il wireframe verrà comunque mostrato per i poligoni nascosti.

### Multirisoluzione: solo livello 0
La multirisoluzione mostrerà i wireframe per il livello 0 più scuri e i livelli più alti progressivamente più chiari. Quando abilitata, questa opzione mostrerà solo il wireframe del livello 0.

### Colore
Imposta colore e opacità del wireframe.

## ![](/icons/grid.webp) Griglia
![](/images/settings_grid.webp)
Attiva la griglia.

### Colore
Imposta colore e opacità della griglia.

### Snap
Abilita lo snap alla griglia per gli strumenti basati su curve.

## ![](/icons/culling.webp)Two sided
Abilita la visualizzazione delle facce dei poligoni da entrambi i lati.

### Colora retro, Colore retro
Abilita la colorazione dei retro e il colore della tinta.

## ![](/icons/outline.webp)Outline
Abilita un contorno attorno all’oggetto attivo.

### Colore contorno, Spessore
Imposta il colore e lo spessore del contorno.


## ![](/icons/bang.webp) Evidenzia
Abilita un breve lampeggio quando l’oggetto attivo viene cambiato.
### Colore, Durata
Imposta il colore e la durata del lampeggio in millisecondi.

## ![](/icons/snap_cube.webp) Cubo di scatto
![](/images/settings_snapcube.webp)

Mostra un’icona di supporto nell’angolo della scena, utile per passare rapidamente tra le viste fronte/retro/sinistra/destra/alto/basso. Tocca i lati del cubo per passare tra le viste ortografiche.

### Forma
Scegli tra una forma a cubo, sfera o gnomone per il cubo di scatto.

### Limita allineamento
Abilita il blocco della rotazione della camera quando trascini sul cubo di scatto. Quando è attivo, un movimento di trascinamento sul cubo di scatto andrà solo a sinistra/destra o su/giù.

### Dimensione
Imposta la dimensione del cubo di scatto.

### Ribalta 180
Abilita un comportamento al tocco per cui, se la vista è bloccata, toccando il centro del cubo la vista ruoterà di 180 gradi. Per esempio, se la vista è bloccata sul fronte, toccando il cubo di vista ruoterai alla vista posteriore.

### Posizione
Imposta in quale angolo sarà il cubo di scatto.


## ![](/icons/edit_radius_n.webp) Statistiche
![](/images/settings_stats.webp)

Mostra informazioni sulla memoria di sistema, il conteggio totale dei vertici della scena e il conteggio dei vertici della selezione corrente.

### Posizione
Imposta in quale angolo saranno le statistiche.

## Primitive/Ripetitori
## Input numerico
Consenti l’input numerico quando si toccano i widget del gizmo.

## Multirisoluzione
### Conteggio massimo vertici
Imposta una soglia per non consentire un’operazione di suddivisione multirisoluzione oltre questo numero di poligoni, che probabilmente manderebbe in crash Nomad. Il valore predefinito è 10 milioni.
### Soglia bassa risoluzione
Una risoluzione più bassa della mesh può essere visualizzata quando muovi la camera. Puoi aumentare questo valore se vuoi visualizzare una risoluzione più alta della mesh.

## Impostazioni
### Ripristina predefiniti
Ripristina tutte le impostazioni ai valori predefiniti.

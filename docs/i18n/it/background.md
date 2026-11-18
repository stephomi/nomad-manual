# ![](/icons/image.webp) Sfondo {#background}

Questo menu controlla il colore dello sfondo di Nomad e le eventuali immagini di riferimento da usare.

![](/images/background_overview.webp)

## Tipo {#type}
![](/images/background_selector.webp)

Per lo sfondo del viewport hai tre opzioni.

* `Ambiente` - Mostra la mappa d'ambiente scelta in [Shading](shading.md). Puoi regolarla ulteriormente con i cursori `Sfocatura` ed `Esposizione` (luminosità). 
* `Colore` - Un colore uniforme a tua scelta
* `Gradiente` - Una sfumatura tra due colori. Il cursore `Fattore` ti permette di spostare il punto centrale del gradiente.  

### Tipo di gradiente {#gradient-type}
Con `Gradiente`, scegli la sua forma:
* `Lineare` - Un gradiente rettilineo, la cui direzione si imposta con il cursore `Angolo`.
* `Radiale` - Un gradiente circolare che parte dal centro dello schermo.
* `Cielo` - Un gradiente ancorato all'orizzonte del mondo, che quindi segue la fotocamera quando guardi in alto e in basso.

Ogni colore ha un pulsante di ripristino e un contagocce, per prelevare un colore dallo schermo.

## ![](/icons/lock.webp) Sincronizza al blocco camera {#sync-on-camera-lock}
Quando la fotocamera è bloccata con il [Navigatore](settings.md#snap-cube), l'immagine di riferimento segue il movimento della fotocamera, così resta allineata alla tua scultura.

* `Consenti rollio (trackball)` - Permette alla fotocamera di ruotare su se stessa quando esci dal blocco.
* `Reimposta vista allo sblocco` - Reimposta la vista quando esci dal blocco della fotocamera.

## Immagine di riferimento {#reference}

![](/images/background_reference.webp)

Puoi aggiungere sullo sfondo un'immagine a tua scelta da usare come riferimento. Tocca `Importa...` per aggiungerne una, poi spunta `Immagine di riferimento` per mostrarla.
Puoi cambiarne posizione e scala, per esempio se vuoi spostarla in un angolo dello schermo.

### ![](/icons/tool_transform.webp) Trasforma {#transform}

Questo pulsante ti permette di posizionare l'immagine di riferimento in modo interattivo. Usa 2 dita per spostare, scalare e ruotare l'immagine fino a metterla al suo posto. `Ripristina impostazioni` riporta l'immagine alla posizione predefinita. Il posizionamento finale si riflette nei cursori qui sotto:

* `Sovrapposizione` - allo 0% l'immagine di riferimento resta sempre dietro gli oggetti, al 100% sta davanti. 
* `Opacità` - Quanto è trasparente l'immagine.
* `Post processing` - Applica gli effetti di post processing all'immagine di riferimento. Disattivalo per mantenere i colori originali.
* `Posizione X` / `Posizione Y` - La posizione X e Y dell'immagine.
* `Scala` - La scala dell'immagine.
* `Rotazione` - La rotazione dell'immagine.


::: tip

Fotocamere e immagini di riferimento sono collegate. 

Questo significa che, se allinei l'immagine di riferimento alla tua scultura e poi crei una fotocamera dal [menu Fotocamera](camera.md), anche posizione, rotazione e scala dell'immagine di riferimento vengono salvate con la fotocamera. Puoi disattivare l'immagine di riferimento e ruotare verso un'altra vista: quando guardi di nuovo attraverso quella fotocamera, l'immagine di riferimento si riattiva con le impostazioni che avevi usato.

Puoi perfino scegliere immagini diverse per fotocamere diverse!

 ![](/videos/reference_camera.mp4)

:::

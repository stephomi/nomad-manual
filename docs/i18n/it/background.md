# ![](/icons/image.webp) Sfondo

Questo menu controlla il colore di sfondo di Nomad, oltre a eventuali immagini di riferimento da utilizzare.

![](/images/background_overview.webp)

## Sfondo 
![](/images/background_selector.webp)

Ci sono tre opzioni per lo sfondo della viewport.

* `Environment` - Mostra la mappa ambiente selezionata in [Shading](shading). Può essere ulteriormente controllata con i controlli Blur ed Exposure (luminosità). 
* `Color` - Un colore uniforme che puoi scegliere
* `Gradient` - Una sfumatura di colore dall’alto verso il basso. Lo slider Factor ti permette di determinare il punto medio del gradiente.  

## Immagine di riferimento

![](/images/background_reference.webp)

Puoi aggiungere un’immagine a tua scelta sullo sfondo da usare come riferimento.
Puoi cambiarne posizione e scala, per esempio se vuoi spostarla in un angolo dello schermo.

### ![](/icons/tool_transform.webp) Transform 

Questo pulsante ti permette di posizionare l’immagine di riferimento in modo interattivo. Usa 2 dita per spostare, scalare e ruotare l’immagine di riferimento nella posizione desiderata. Il posizionamento finale sarà riportato negli slider sottostanti:

* `Overlay` - a 0% l’immagine di riferimento sarà sempre dietro ai tuoi oggetti, a 100% sarà davanti. 
* `Opacity` - Quanto l’immagine è trasparente.
* `Position` - La posizione X e Y dell’immagine.
* `Rotation` - Rotazione dell’immagine.
* `Scale` - Scala dell’immagine.


::: tip

Le camere e le immagini di riferimento sono collegate. 

Questo significa che se imposti la tua immagine di riferimento in modo che si allinei con il tuo sculpt, quando crei una camera dal [menu Camera](camera), posizione, rotazione e scala dell’immagine di riferimento vengono anch’esse memorizzate con la camera. Puoi disattivare l’immagine di riferimento, ruotare verso un’altra viewport. Se guardi di nuovo attraverso la camera, l’immagine di riferimento verrà attivata con le impostazioni che avevi usato.

Questo include anche la possibilità di scegliere immagini diverse per camere diverse!

 ![](/videos/reference_camera.mp4)

:::

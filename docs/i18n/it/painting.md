# ![](/icons/paint.webp) Pittura  

Controlla il colore, la ruvidità, la metallicità dei tratti di pittura, consenti il riempimento globale degli attributi di pittura e definisci come gli strumenti di pittura interagiscono con livelli, maschere e selezioni nascoste.

![](/images/paint_overview.webp)  

## Panoramica

Nomad utilizza la pittura PBR sui vertici. Cosa significa?

### PBR
PBR, o Physically Based Rendering, è una tecnica di grafica computerizzata molto diffusa per cinema, televisione, videogiochi e mobile. Basando le luci su proprietà fisiche e definendo le superfici tramite colore, ruvidità, metallicità, è possibile ottenere un’ampia varietà di risultati fotorealistici.

### Pittura sui vertici

Pittura sui vertici significa che le informazioni di pittura sono memorizzate nei vertici del modello, invece che nelle texture. Poiché Nomad può gestire modelli con centinaia di migliaia, spesso milioni di vertici, i tuoi modelli possono avere una pittura superficiale altamente dettagliata; se puoi scolpire il dettaglio, puoi anche dipingerlo.

Questo significa anche che dipingere in Nomad non richiede il mapping UV, spesso un processo lento e tecnico in altre applicazioni 3D. Molte altre applicazioni 3D non supportano i conteggi di vertici elevati che supporta Nomad, tuttavia Nomad dispone anche di buoni strumenti di baking delle texture e di decimazione per aiutare.

### Texturing

Nomad supporta le texture, ma devono essere presenti in un modello importato, oppure tramite il baking della pittura sui vertici in texture. 

Una texture è semplicemente un’immagine, ma nel contesto 3D di solito si riferisce a un’immagine assegnata a un oggetto.
Per avvolgere un’immagine attorno a un modello, il modello ha bisogno di coordinate di texture (UV).

Nomad può [calcolarle automaticamente](topology.md#uv-unwrap) ma non hai molto controllo sulla qualità complessiva.

::: tip
Un esempio di workflow:
- Scolpisci in Nomad, poi esegui l’[UV unwrap](topology.md#uv-unwrap)
- Se hai già iniziato a dipingere in Nomad puoi [trasferire la pittura sui vertici alle texture](topology.md#bake-vertex-colors-to-texture)
- Esporta in Procreate
- Fai il texturing in Procreate
- Esporta di nuovo in Nomad per il rendering
:::

Questa è la panoramica, ora esploriamo le sezioni del menu di pittura:


## Pittura a tratto
![](/images/paint_intensity.webp)  

Abilita la pittura per questo strumento, utile se hai bisogno di scolpire e dipingere allo stesso tempo.

Per gli strumenti in cui la pittura è la funzione principale (ad es. Paint, Smudge, Mask), questa casella non esiste.

### Intensità della pittura

Uno slider che ti permette di usare un’intensità diversa rispetto all’intensità principale dello strumento.

Le caselle `Alpha`, `Falloff` e `Randomize` determinano se queste funzioni influenzeranno la pittura. Ad esempio potresti avere la randomizzazione abilitata per lo strumento Clay, ma il colore non verrà randomizzato.


## Materiale
![](/images/paint_material.webp) 

La prima icona è una forma di anteprima del materiale. Trascinando sull’anteprima 3D del materiale lo ruoterai. 

La seconda icona è un’anteprima del tratto di pittura con l’alpha e il falloff selezionati.

Il pulsante di anteprima accanto al titolo Material ti permette di passare tra None, Material o Triplanar. Questo determina cosa accadrà quando cambi interattivamente le proprietà di pittura:

* `None` - Nessuna anteprima verrà mostrata sul modello quando regoli le proprietà
* `Material` - I valori del materiale verranno mostrati in anteprima sull’oggetto quando regoli le proprietà. Se usi texture e il modello ha UV, verranno usati gli UV.
* `Triplanar` - Il materiale verrà mostrato in anteprima come proiezione Triplanar. 

Il contagocce può essere usato per campionare tutte le proprietà da un oggetto nella tua scena.

## Preset di materiale
Toccando la forma di anteprima 3D verrà visualizzato un menu di preset di materiali, che possono essere clonati per definire i tuoi preset.

![](/images/paint_presets.webp) 

Le opzioni `Embed Textures` e `Alpha`, se abilitate, memorizzeranno all’interno del preset qualsiasi texture usata da questo materiale. Questo è spiegato meglio più avanti.

## Slider PBR
![](/images/paint_sliders.webp) 

La pittura [PBR](shading.md#pbr) utilizza 4 canali:
- `Color` Il colore che verrà dipinto. Il contagocce può essere usato per selezionare il colore da altre parti del modello o da immagini di riferimento.
- `Roughness` Indica quanto è “ruvida” o “liscia” una superficie. Un valore basso di ruvidità significa che i riflessi saranno nitidi.
- `Metalness` Indica semplicemente se la superficie è metallica o no. Il valore dovrebbe essere per lo più 0% o 100%, i valori intermedi dovrebbero essere eccezioni.
- `Opacity` Quanto il materiale può essere visto attraverso. Rigorosamente parlando non fa parte della specifica PBR, ma è utile in molte situazioni. 1 è completamente opaco, 0 è trasparente. Nota che opacità e rifrazione sono cose diverse, la rifrazione in Nomad è gestita tramite il materiale di rifrazione. 

Se selezioni un preset di materiale, 3 canali vengono dipinti simultaneamente (l’opacità è spesso intenzionalmente esclusa). Questo significa che invece di dipingere solo “rosso”, puoi dipingere “un metallo rosso ruvido” o “una plastica bianca liscia”.

Il quadrato è uno slot di texture, toccalo per usare una texture per quella proprietà invece di un valore uniforme.

L’icona del pennello accanto agli slider eseguirà un riempimento globale di quella proprietà sull’oggetto.

La casella abilita o disabilita quella particolare proprietà, quindi potresti dipingere solo il colore, oppure solo la ruvidità e l’opacità, per esempio. 

Ecco alcuni esempi di diverse proprietà di ruvidità e metallicità:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Solo il colore è supportato nella modalità di [rendering Matcap](shading.md#matcap), metallicità e ruvidità vengono ignorate.
:::

::: tip
Quando usi texture per la pittura PBR, è spesso utile passare a uno strumento come `Stamp`, oppure usare il menu Stroke per usare una modalità diversa da Dot, che può sbavare la texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Potresti considerare di attivare lo `Smooth Shading` [globalmente](settings.md#smooth-shading) o [per oggetto](material.md#smooth-shading) se stai dipingendo una superficie metallica su un oggetto con un numero di poligoni basso.
:::

## Paint all

![](/images/paint_paint_all.webp)

Applica il materiale corrente all’oggetto, in modalità standard con “Paint All”, oppure come proiezione Triplanar.

Le caselle accanto agli slider di color/metalness/roughness/opacity vengono rispettate, qualsiasi proprietà disabilitata non verrà riempita.

I pulsanti aggiuntivi controllano come il Paint All può essere ulteriormente influenzato:

| Icon                        | Description                                      |
| :-------------------------: | :----------------------------------------------: |
| ![](/icons/tool_mask.webp) | Le aree mascherate non verranno influenzate.     |
| ![](/icons/tool_hide.webp) | Le aree nascoste non verranno influenzate.       |
| ![](/icons/opacity.webp)   | Usa il fattore di pittura dello strumento sopra. |
| ![](/icons/layer.webp)     | Le aree non dipinte di un livello non verranno influenzate. |
| ![](/icons/triplanar.webp) | Indicatore delle impostazioni Triplanar          |
| ![](/icons/cog.webp)       | Apre le impostazioni Triplanar                   |

### Impostazioni Triplanar
![](/images/paint_triplanar_settings.webp)

Simili alle [impostazioni Triplanar nel menu Material](material.md#triplanar), puoi controllare la fusione delle proiezioni, il tiling e gli offset. 

Usa la casella di anteprima in cima a questo menu per abilitare un’anteprima persistente mentre regoli i valori.

## Materiale globale
Se questa opzione è abilitata, il materiale selezionato sarà lo stesso per gli altri strumenti. Nota che tiene conto solo delle impostazioni di ruvidità, metallicità e colore.

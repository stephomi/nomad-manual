# ![](/icons/layer.webp) Camadas 

Este menu contém a pilha de camadas, uma forma de armazenar edições no seu objeto de maneira não destrutiva, e muitas maneiras de combinar e reaproveitar camadas.

![](/images/layers_overview.webp) 

## Visão geral

As camadas do Nomad têm múltiplos propósitos.

As informações de pintura (Cor, Rugosidade, Metalicidade, Opacidade) funcionam com camadas de forma semelhante a aplicativos de pintura 2D. Uma camada pode ser criada e a pintura aplicada a um modelo. A camada pode ser ligada ou desligada, ter sua opacidade ajustada, pode ser duplicada, sua ordem pode ser alterada na pilha de camadas, e seu modo de mesclagem ajustado.

O Nomad também usa camadas para escultura. Uma camada pode armazenar detalhes finos como rugas, ou pode armazenar grandes alterações, permitindo que funcionem como blendshapes/shape keys/morph targets em outros aplicativos 3D. Por exemplo, você pode esculpir diferentes expressões faciais em camadas diferentes e ajustar os controles deslizantes das camadas para combiná‑las em novas expressões.

Nesse caso, as alterações armazenadas em uma camada são puramente aditivas, a ordem das camadas não importa como acontece com pintura.

As camadas podem ser parcialmente apagadas por meio da ferramenta [Delete Layer](tools.md#delete-layer), e as camadas também podem ser usadas para criar máscaras com base nas diferentes informações armazenadas na camada.

![](/videos/layer.mp4)

::: tip
Ao contrário da maioria dos softwares de escultura, mudar a topologia de uma malha não descartará as camadas. Você pode usar o [Voxel Remesher](topology.md#voxel-remesher), o [Multiresolution](topology.md#multiresolution) ou as ferramentas [Trim](tools.md#trim)/[Split](tools.md#split), mas note que ao usar o [Voxel Remesher](topology.md#voxel-remesher), a qualidade da camada será impactada.
:::

::: tip
Se estiver usando camadas para blendshapes/morph targets, há funcionalidades extras de camada no [menu de cena](scene.md#object-menu). Você pode separar camadas em objetos e combinar objetos correspondentes em camadas.
:::
----

## Menu de camadas 

![](/images/layers_menu.webp)

Pressione `Add layer` para criar uma nova camada.

Cada camada tem um nome, um controle deslizante para controlar sua intensidade/fator e botões de opções.

### Opções

| Ação         | Ícone                        | Descrição                                           |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visível      | ![](/icons/eye_open.webp)   | Mostrar/ocultar a camada                            |
| Modo de mesclagem | ![](/icons/opacity.webp)    | O modo de mesclagem ao estilo Photoshop. Os 4 ícones exibem os modos para Cor, Rugosidade, Metalicidade, Opacidade. |
| Editar nome  | ![](/icons/pencil.webp)     | Editar o nome da camada                             |
| Excluir      | ![](/icons/trash.webp)      | Excluir a camada                                    |
| Duplicar     | ![](/icons/clone.webp)      | Duplicar a camada                                   |
| Mesclar para baixo | ![](/icons/merge_down.webp) | Mesclar a camada com a camada inferior (ou malha base) |
| Mais         | ![](/icons/more.webp)       | Opções [More...](#more)                             |

Para mover uma camada para outra parte da pilha de camadas, pressione e segure no nome dela e então arraste.

### More...

O botão 'More...' mostrará opções extras para a camada atual:

![](/images/layers_more.webp) 

#### Fatores de canal

Esses controles permitem escalar a quantidade de escultura/cor/rugosidade/metalicidade/opacidade da camada. Esses valores são multiplicados pelo controle deslizante de fator da camada, então, por exemplo, se a intensidade da camada for 1, mas o fator do canal de cor for 0,5, a cor exibida terá intensidade 0,5.

`Offset` controla a intensidade de escultura da camada. Enquanto cor/rugosidade/metalicidade são limitadas entre 0 e 1, o offset pode ter qualquer valor, tanto positivo quanto negativo. 

::: tip
Offset pode ser usado para transformar uma camada de relevos em uma camada de cavidades, ou um sorriso em um franzir de testa:
![](/videos/layer_happysad.mp4)


Uma camada simétrica pode ser clonada e então dividida em formas esquerda/direita com del layer:
![](/videos/layer_leftright.mp4)

Camadas com fatores de offset negativos podem ser assadas (baked) em camadas vazias para criar novas formas positivas.

Camadas com fatores de offset positivos acima de 1 podem ser usadas para experimentar blendshapes mais extremos.
:::

::: warning
No momento, as camadas compartilham apenas um único canal de opacidade para todos os 3 canais (cor/metalicidade/rugosidade).
Se você mesclar múltiplas camadas com intensidade por canal que não estejam em intensidade máxima, é possível que o resultado final pareça diferente.

Talvez no futuro, cada canal tenha seu próprio canal alfa para remover essa limitação.
:::


#### ![](/icons/tool_mask.webp) Mask
O botão de máscara ao lado de cada controle deslizante criará uma máscara a partir daquele canal. Similar ao uso de camadas para fazer seleções em aplicativos de pintura, isso permite reutilizar o trabalho que você fez em uma camada para outras operações.

#### ![](/icons/preview.webp) Preview
![](/images/layers_preview.webp) 

Quando ativado, irá pré-visualizar as configurações de extração para esta camada (veja a próxima seção).

Quando o raio‑X (xray) está ativado, apenas a forma extraída ficará sólida, o restante da forma ficará transparente, útil se você estiver usando alturas de extração negativas.

#### Extract
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

O botão `Extract` irá duplicar o conteúdo da camada em um novo objeto, geralmente com uma espessura especificada pelo usuário definida na próxima seção.

`Closing action` determina como a duplicação é feita:

* None - Simplesmente extrai a parte, sem tentar gerar laterais ou preencher buracos.
* Fill - O buraco é preenchido e suavizado com triângulos. Não use esta opção para superfícies planas.
* Shell - Fecha a forma extraída com o valor de espessura e opções de direção.
* Layer - Extrai a diferença da camada.

#### ![](/icons/height.webp) Thickness
![](/images/layers_thickness.webp) 

A profundidade da extrusão do shell. Valores positivos crescem para fora da superfície, valores negativos crescem para dentro da superfície.

O sinal de mais/menos ao lado desse valor define a direção da extrusão:
* Menos ( - ) começará da superfície atual e extrudirá para baixo. 
* Mais ( + ) começará da superfície atual e extrudirá para cima.
* MaisMenos ( ± ) empurrará o topo e a base da extrusão para longe em quantidades iguais, de modo que ficará metade embutida na superfície original.

#### Suavidade
![](/images/layers_smoothness.webp) 

Se as bordas da região a ser extraída estiverem irregulares, este controle deslizante tentará desfocar a borda em uma forma mais suave. 

#### ![](/icons/height.webp) Edge loop (side)
![](/images/layers_edgeloop.webp) 

Esta seção fica visível quando a ação de fechamento é 'Shell'. 

`Auto Edge-loop (side)` calculará o número de edge loops ao longo das laterais do shell para criar polígonos quadrados. 

Se desativado, o controle deslizante `Division` definirá o número de divisões nas laterais.

_Este é o fim do submenu 'More...'._

### Avançado
![](/images/layers_advanced.webp)

#### Keep top layers details

Garante que pequenos detalhes em camadas superiores permaneçam visíveis quando grandes alterações são feitas em camadas inferiores.

Por padrão, se você esculpir pequenas rugas em uma camada e depois fizer grandes alterações na camada base, as rugas serão perdidas. Ativar esta opção permitirá que esses pequenos detalhes sempre flutuem acima das grandes alterações inferiores. No vídeo a seguir, veja como o detalhe da ruga é removido por padrão, mas permanece visível quando 'keep top layers details' está ativado:

![](/videos/layers_details.mp4)


#### UI: Expand list

O menu de camadas padrão permite alternar a visibilidade da camada e a opacidade da camada. Ativar esta opção expande os controles completos para cada camada.

![](/images/layers_expand.webp)

#### Sync transform

Se ativado, todas as camadas não selecionadas serão ajustadas dependendo da rotação, escala e inclinação (skew) da transformação. 

Desative esta opção se as outras camadas forem usadas sem a nova transformação que você está aplicando.

Quando definido como `Auto`, apenas as camadas visíveis serão ajustadas.

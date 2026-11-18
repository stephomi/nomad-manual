# ![](/icons/layer.webp) Camadas {#layers}

Este menu contém a pilha de camadas, uma forma de guardar as edições do seu objeto de maneira não destrutiva, e muitas maneiras de combinar e reaproveitar camadas.

![](/images/layers_overview.webp) 

## Visão geral {#overview}

As camadas do Nomad servem para várias coisas.

As informações de pintura (Cor, Aspereza, Metalidade, Opacidade) funcionam com camadas de forma parecida com os aplicativos de pintura 2d. Você pode criar uma camada e pintar um modelo nela. A camada pode ser ligada ou desligada, ter a opacidade ajustada, ser duplicada, mudar de posição na pilha de camadas e ter o modo de mistura alterado.

O Nomad também usa camadas para esculpir. Uma camada pode guardar detalhes finos como rugas, ou mudanças grandes, funcionando como blendshapes/shape keys/morph targets em outros aplicativos 3d. Por exemplo, você pode esculpir expressões faciais diferentes em camadas diferentes e ajustar os controles das camadas para combiná-las em novas expressões.

Nesse caso, as mudanças guardadas em uma camada são puramente aditivas: a ordem das camadas não importa como importa para a pintura.

As camadas podem ser apagadas parcialmente com a ferramenta [ApagCamada](tools.md#delete-layer), e também podem ser usadas para criar máscaras a partir das diferentes informações que guardam.

![](/videos/layer.mp4)

::: tip
Ao contrário da maioria dos programas de escultura, mudar a topologia de uma malha não descarta as camadas. Você pode usar o [Remalhamento por voxels](topology.md#voxel-remesher), a [Multirresolução](topology.md#multiresolution) ou as ferramentas [Aparar](tools.md#trim)/[Dividir](tools.md#split), mas ao usar o [Remalhamento por voxels](topology.md#voxel-remesher) a qualidade da camada é afetada.
:::

::: tip
Se você usa camadas como blendshapes/morph targets, há recursos extras de camadas no [menu Cena](scene.md#object-menu): você pode separar camadas em objetos e combinar objetos correspondentes em camadas.
:::
----

## Menu de camadas {#layer-menu}

![](/images/layers_menu.webp)

O título mostra o nome do objeto selecionado. As camadas não estão disponíveis em primitivas, então valide a primitiva antes.

Toque em `Adicionar camada` para criar uma nova camada. `Combinar Camadas` mescla todas as camadas na malha base; o número ao lado do ícone indica quantas camadas existem.

Cada camada tem um nome, um controle deslizante para a força/fator dela e botões de opções. Toque em uma camada para torná-la ativa: a escultura e a pintura vão para essa camada. Toque em `Base` para voltar a trabalhar na malha base.

### ![](/icons/sort_right.webp) Expandir lista {#ui-expand-list}

Por padrão, a lista de camadas mostra apenas a visibilidade, o modo de mistura e a força de cada camada, e a camada ativa aparece expandida com todos os controles. A seta à esquerda do título expande todos os controles de todas as camadas.

![](/images/layers_expand.webp)

### Opções {#options}

| Ação            | Ícone                        | Descrição                                           |
| :-------------: | :--------------------------: | :-------------------------------------------------  |
| Visível         | ![](/icons/eye_open.webp)   | Mostra/oculta a camada                              |
| Mistura         | ![](/icons/opacity.webp)    | O modo de mistura no estilo do Photoshop. Os 4 ícones mostram os modos de Cor, Aspereza, Metalidade e Opacidade. |
| Editar nome     | ![](/icons/pencil.webp)     | Edita o nome da camada                              |
| Apagar          | ![](/icons/trash.webp)      | Apaga a camada                                      |
| Duplicar        | ![](/icons/clone.webp)      | Duplica a camada                                    |
| Combinar abaixo | ![](/icons/merge_down.webp) | Combina a camada com a camada de baixo (ou com a malha base) |
| Mais            | ![](/icons/more.webp)       | Opções em [Mais...](#more)                          |

Quando uma camada não está expandida, `Editar nome`, `Apagar`, `Duplicar` e `Combinar abaixo` ficam no menu [Mais...](#more) dela.

Para mover uma camada para outra posição na pilha, toque e segure no nome dela e depois arraste.

### Base {#base}

O botão de 3 pontos da linha `Base` move a pintura da malha base para uma nova camada, com o botão `Base → Camada`. A base então volta ao material de fundo. Isso é prático quando você pintou bastante antes de criar qualquer camada.

* Os botões de máscara e de ocultar ao lado deixam as áreas mascaradas e ocultas intactas.
* `Extrair` - os canais a mover: `Cor`, `Opacidade`, `Aspereza` e `Metalidade`.
* `Material de fundo` - se ativado, só os valores diferentes desse material são movidos. Defina-o com os controles deslizantes, ou pegue-o do modelo com o conta-gotas.

### ![](/icons/more.webp) Mais... {#more}

O botão 'Mais...' mostra opções extras para a camada atual, em duas abas: os ajustes (ícone de engrenagem) e a extração (ícone de cubo).

![](/images/layers_more.webp) 

#### Fatores do canal {#channel-factors}

Estes controles permitem escalar a quantidade de escultura/cor/aspereza/metalidade/opacidade da camada. Esses valores são multiplicados pelo controle de fator da camada; por exemplo, se a força da camada for 1 mas o fator do canal de cor for 0.5, a cor aparece com força 0.5.

`Deslocamento` controla a força da escultura da camada. Enquanto cor/aspereza/metalidade ficam limitadas entre 0 e 1, o deslocamento pode ter qualquer valor, positivo ou negativo.

::: tip
O deslocamento pode transformar uma camada de saliências em uma camada de cavidades, ou um sorriso em uma cara fechada:
![](/videos/layer_happysad.mp4)


Uma camada simétrica pode ser clonada e depois separada em formas esquerda/direita com a ferramenta ApagCamada:
![](/videos/layer_leftright.mp4)

Camadas com fatores de deslocamento negativos podem ser seladas em camadas vazias para criar novas formas positivas.

Camadas com fatores de deslocamento positivos acima de 1 podem ser usadas para experimentar blendshapes mais extremos.
:::

::: warning
No momento, as camadas compartilham um único canal de opacidade para os 3 canais (cor/metalidade/aspereza).
Se você combinar várias camadas com intensidades por canal que não estejam no máximo, o resultado final pode ficar diferente.

Talvez no futuro cada canal tenha o seu próprio canal alfa para remover essa limitação.
:::


#### ![](/icons/shield.webp) Máscara {#mask}
O botão de máscara ao lado de cada controle deslizante cria uma máscara a partir desse canal. Assim como usar camadas para fazer seleções em aplicativos de pintura, isso permite reaproveitar o trabalho feito em uma camada para outras operações.

#### ![](/icons/preview.webp) Pré-visualização {#preview}
![](/images/layers_preview.webp) 

As opções a seguir ficam na aba de extração do menu 'Mais...'.

Quando ativada, mostra uma pré-visualização dos ajustes de extração desta camada (veja a próxima seção).

`Raio-X` escolhe quais objetos ficam transparentes durante a pré-visualização (`Nenhum`, `Não selecionados`, `Selecionados` ou `Todos`), para que a forma extraída continue sólida. É útil se você estiver usando alturas de extração negativas.

#### ![](/icons/mask_extract.webp) Extrair {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

O botão `Extrair` duplica o conteúdo da camada em um novo objeto, normalmente com uma espessura definida por você na próxima seção.

`Ação de fechamento` determina como a duplicação é feita:

* `Nenhuma` - Apenas extrai a parte, sem tentar gerar laterais nem preencher buracos.
* `Preencher` - O buraco é preenchido e suavizado com triângulos. Não use esta opção em superfícies planas.
* `Casca` - Fecha a forma extraída usando o valor de espessura e as opções de direção.
* `Camada` - Extrai a diferença da camada.

#### ![](/icons/height.webp) Altura {#thickness}
![](/images/layers_thickness.webp) 

A profundidade da extrusão da casca. Valores positivos crescem para fora da superfície, valores negativos crescem para dentro. Fica oculta quando a ação de fechamento é `Camada`.

O mais/menos ao lado deste valor define a direção da extrusão:
* Menos ( - ) começa na superfície atual e extruda para baixo.
* Mais ( + ) começa na superfície atual e extruda para cima.
* Mais-menos ( ± ) empurra o topo e o fundo da extrusão na mesma medida, de modo que ela fica com metade embutida na superfície original.

#### Lados {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Esta seção aparece quando a ação de fechamento é `Casca`.

`Divisões da parede` define o número de divisões ao longo das laterais da casca. Com a opção `Auto` ligada, o Nomad calcula o número de loops de arestas para criar polígonos quadrados.

#### Suavidade {#smoothness}
![](/images/layers_smoothness.webp) 

Se as bordas da região a extrair estiverem serrilhadas, ative esta opção para suavizá-las em uma forma mais bonita. `Todos` suaviza toda a superfície extraída, `Apenas bordas` suaviza só as bordas. `Iterações` define a força da suavização.

_Aqui termina o submenu 'Mais...'._

### ![](/icons/cog.webp) Avançado {#advanced}
![](/images/layers_advanced.webp)

O botão `Avançado` na parte de baixo do menu aparece quando o objeto tem camadas.

#### Manter detalhes das camadas superiores {#keep-top-layers-details}

Garante que os pequenos detalhes das camadas superiores continuem visíveis quando você faz grandes mudanças nas camadas inferiores. Enquanto você esculpe, a deformação vinda das camadas superiores é ignorada, mas os detalhes delas continuam visíveis. Só funciona bem se essas camadas superiores tiverem detalhes relativamente pequenos.

Por padrão, se você esculpir pequenas rugas em uma camada e depois fizer grandes mudanças na camada base, as rugas se perdem. Ativar esta opção faz esses pequenos detalhes ficarem sempre por cima das grandes mudanças de baixo. No vídeo a seguir, veja como o detalhe da ruga é removido por padrão, mas continua visível quando 'Manter detalhes das camadas superiores' está ativado:

![](/videos/layers_details.mp4)


#### Sincronizar transformação {#sync-transform}

Quando ativada, todas as camadas não selecionadas são ajustadas de acordo com a rotação, a escala e o cisalhamento da transformação, quando você usa as ferramentas Gizmo ou Transformar. Pode ser `Auto`, `Não` ou `Sim`.

Desative esta opção se as outras camadas devem ser usadas sem a nova transformação que você está aplicando.

Quando definida como `Auto`, só as camadas visíveis são ajustadas.

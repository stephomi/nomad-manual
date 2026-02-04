# ![](/icons/scene.webp) Cena {#scene}

Este menu permite gerir objetos, luzes, câmaras e repetidores no Nomad. Mostra a hierarquia da cena como uma vista em árvore, permitindo modificar muitos aspetos dos seus objetos. Também permite criar novos objetos, bem como combinar e separar objetos de várias formas.


![](/images/scene_menu_summary.webp)


## Barra de atalho {#shortcut-bar}
| Ação                  | Ícone                             | Descrição                                                                                                          |
| :-------------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| [Adicionar...](#add-menu) | ![](/icons/plus.webp)            | Mostra o [Menu Adicionar](#add-menu) para adicionar um objeto à cena                                               |
| Apagar                | ![](/icons/trash.webp)           | Apaga o objeto                                                                                                     |
| Bloquear              | ![](/icons/lock.webp)            | Torna o objeto não selecionável na viewport. Ainda pode ser selecionado na vista em árvore.                       |
| Unir                  | ![](/icons/merge.webp)           | Une os objetos selecionados num único objeto sem alterações de geometria                                          |
| Separar               | ![](/icons/diagonal.webp)        | Se um objeto for composto por “conchas” de polígonos distintas, divide-o em objetos separados. O inverso de unir  |
| [Booleano...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Mostra o menu [Booleano](#boolean)                                                                                |
| Clonar                | ![](/icons/clone.webp)           | Duplica o objeto num novo objeto                                                                                   |
| Instância             | ![](/icons/link.webp)            | Duplica o objeto como instância, de forma que alterações de modelação numa sejam aplicadas a todas as instâncias  |
| Remover instância     | ![](/icons/unlink.webp)          | Converte uma instância numa forma única, deixando de copiar alterações de modelação para outras instâncias        |
| Sincronizar           | ![](/icons/link.webp)            | Se instâncias tiverem filhos, garante que todas as instâncias partilham a mesma hierarquia de filhos              |


## Exibição em árvore {#tree-view}
![](/images/scene_treeview.webp) 

| Ação         | Ícone                      | Descrição                |
| :----------: | :------------------------: | :----------------------: |
| Selecionar   | ![](/icons/checked.webp)  | Alternar selecionado/não |
| Visível      | ![](/icons/eye_open.webp) | Alternar visibilidade    |
| Menu         | ![](/icons/more.webp)     | Mostrar menu do objeto   |

::: tip DICA: Selecionar ou ocultar rapidamente muitos objetos

Toque no ícone de seleção para alternar um único objeto, ou arraste verticalmente na coluna de seleção para selecionar muitos objetos. O mesmo pode ser feito com a coluna de visibilidade.

:::

### Manipulação da exibição em árvore {#tree-view-manipulation}

Faça um toque longo num item da vista em árvore até ficar amarelo. Depois pode movê‑lo para cima ou para baixo na árvore, bem como arrastá‑lo sobre outro item para o tornar filho desse item.

Quando muitos itens estão selecionados, a maioria ficará amarelo escuro e um ficará amarelo mais claro. Faça um toque longo e arraste o item mais claro para mover todos os objetos de uma vez.

Quando seleciona um item pai, por predefinição todos os itens filho também serão selecionados. Tocar no ícone do pai alternará entre selecionar apenas o pai, ou o pai e os filhos.

### Menu do objeto {#object-menu}

Clicar no botão de reticências (...) de um objeto na vista em árvore mostra o menu do objeto.  
Muitas destas opções são semelhantes à barra de atalho no topo, repetidas por conveniência.

|       Ação        |                        Ícone                        | Descrição                                                                                                                                                             |
| :---------------: | :-------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     Instância     |               ![](/icons/link.webp)               | Duplica o objeto como instância, de forma que alterações de modelação numa sejam aplicadas a todas as instâncias                                                     |
|       Clonar      |              ![](/icons/clone.webp)               | Duplica o objeto num novo objeto                                                                                                                                      |
|        Nome       |              ![](/icons/pencil.webp)              | Altera o nome do objeto                                                                                                                                                |
|      Apagar       |              ![](/icons/trash.webp)               | Apaga o objeto                                                                                                                                                        |
|     Apagar+       |            ![](/icons/removeNode.webp)            | Apaga o objeto e os seus filhos                                                                                                                                       |
|  Remover instância |              ![](/icons/unlink.webp)             | Converte uma instância numa forma única, deixando de copiar alterações de modelação para outras instâncias                                                           |
| Separar Topologia |             ![](/icons/separate.webp)             | Se um objeto for composto por “conchas” de polígonos distintas, divide-o em objetos separados. O inverso da operação de unir.                                        |
| Separar Face Group |            ![](/icons/faceGroup.webp)            | Se um objeto tiver vários grupos de faces, divide a malha em objetos separados.                                                                                      |
|  Separar Layers   |              ![](/icons/layer.webp)               | Se um objeto tiver layers, divide cada layer num objeto separado. Útil para enviar blendshapes para outras aplicações.                                               |
|   Unir -> Layers  | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Se vários objetos estiverem selecionados e tiverem topologia correspondente, funde esses objetos em layers para o objeto principal (os outros objetos serão apagados). Novamente, útil para blendshapes vindos DE outras aplicações.<br><br> Note que as layers estarão desativadas por predefinição. Ative‑as se precisar de ajustar os seus sliders. |




### Multiseleção {#multiselection}
Pode selecionar vários objetos para ajudar em duas coisas:
- usar a ferramenta de gizmo para mover vários objetos de uma vez
- fundir objetos usando operações de unir e booleanas.

Pode fazê‑lo usando a caixa de seleção `Multiselection` e depois clicando no objeto na lista.

::: tip Multiseleção rápida
Também pode fazer multiseleção na viewport mantendo o atalho `Smooth` pressionado e tocando noutro mesh.

Pode desselecionar um objeto tocando nele novamente (apenas se a sua seleção tiver mais de um objeto).
:::

::: warning Funcionalidade limitada do gizmo
Ao usar multiseleção, a ferramenta de gizmo irá sempre ignorar máscaras.  
Além disso, a escala X/Y/Z é removida.

A razão é que a multiseleção apenas permite transformação de malha inteira, não transformação por vértice.  
Isto poderá ser melhorado no futuro.
:::


## Unir {#join}
Esta opção simplesmente cria uma única entrada de objeto a partir de vários objetos selecionados.

Pode ver um exemplo em vídeo na secção [Separar](#separate).

## Booleano {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina objetos numa única superfície.

`Voxel merge` preserva o volume dos objetos e calcula novos polígonos uniformemente espaçados na superfície. Devido à etapa de cálculo, uma fusão por voxel consegue lidar com geometria complexa, mas pode perder detalhes finos se a resolução alvo não for suficientemente alta.

`Boolean` tenta manter os polígonos no seu layout original e coser os polígonos onde os objetos se sobrepõem. Isto pode produzir resultados muito mais limpos e nítidos do que uma fusão por voxel; no entanto, requer meshes “watertight”: não podem existir buracos ou formas malformadas nos objetos. Se isto falhar, normalmente uma fusão por voxel funcionará.

### Operações booleanas {#boolean-operations}
Tanto o Voxel Merge como o Boolean usam a visibilidade dos objetos para controlar a operação:

#### União {#union}
Ambos os objetos visíveis criam uma **união** booleana; a pele exterior dos objetos é combinada, sem superfícies interiores. ![](/images/boolean_union.webp)

#### Subtrair {#subtract}
Um objeto invisível = **subtração** booleana; o objeto invisível será subtraído do objeto visível. ![](/images/boolean_subtract.webp)

#### Interseção {#intersect}
Ambos os objetos invisíveis = **interseção** booleana; cria uma nova forma apenas onde os dois objetos se sobrepõem. ![](/images/boolean_intersect.webp)


### Botão de Mesclagem Voxel {#voxel-merge-button}
Premir este botão fará uma operação de fusão por voxel nos objetos selecionados. Quando feito num único objeto, irá retopologizar em polígonos uniformemente espaçados, útil quando um objeto tem polígonos esticados.

### Resolução {#resolution}
A resolução da grelha 3D de voxels usada para o cálculo. Quando este valor é alterado, um padrão de tabuleiro de xadrez é sobreposto no objeto para pré-visualizar o tamanho dos polígonos.

### Construir multirresolução {#build-multiresolution}
Cria níveis de multirresolução abaixo da sua resolução alvo. Assim, se a sua resolução for 400 e “build multiresolution” for 3, obterá uma nova malha com, por exemplo, 296 000 polígonos, mas existirão 3 níveis de subdivisão inferiores com 74 000, 18 000, 4 000.

### Manter arestas afiadas {#keep-sharp-edges}
Ativa o encaixe da malha de voxel às arestas. Funciona melhor em formas simples.

### Botão booleano {#boolean-button}
Premir este botão fará uma operação booleana de polígonos usando a biblioteca Manifold de Emmett Lalish. 


## Separar {#separate}
Se tiver um único objeto baseado em várias partes desconectadas, pode dividir esse objeto em vários objetos.  
Isto pode ser visto como o oposto de [Simple Merging](#simple-merge).

![](/videos/merge_separate.mp4)


## Menu Adicionar {#add-menu}

![](/images/scene_addmenu_overview.webp)

Este menu cria primitivas, grupos, câmaras, repetidores e luzes.

Primitivas são tipos de formas básicas que podem ser ajustadas usando parâmetros. Depois de ajustar a primitiva às suas necessidades, “valida‑a”, o que converte esses parâmetros numa malha de polígonos que pode ser esculpida e pintada. Uma primitiva não pode ter os seus parâmetros ajustados depois de ser validada.


![](/images/scene_addmenu_top.webp)

### No gizmo {#on-gizmo}
Ativa colocar a nova primitiva onde está a forma selecionada ou o gizmo atual. Quando desativado, a primitiva será colocada no centro da cena.

### Selecionar gizmo {#select-gizmo}
Ativa a mudança automática para a ferramenta de gizmo quando uma nova primitiva é criada. 

### Avançado {#add-advanced}

Este menu permite definir a sua preferência para onde novas primitivas, grupos e repetidores serão criados. Podem ser criados sobre o objeto selecionado, na origem do mundo ou na posição do gizmo.


### UVs {#uvs}
Ativa UVs nas primitivas. UVs (frequentemente chamados coordenadas de textura) são dados extra usados em 3D para permitir que texturas sejam aplicadas às superfícies. Consomem mais memória, mas para a maioria dos dispositivos isto não deve ser um problema, exceto em contagens de polígonos muito altas (por exemplo, 10 milhões de polígonos ou mais). 

### Primitivas {#primitives}

| Primitiva      | Ícone                                     | Descrição                                                                                                         |
| :------------: | :---------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | É um cubo simples; pode controlar a divisão em X, Y e Z                                                           |
| Sphere         | ![](/icons/circle.webp)                  | Por conveniência chama‑se Sphere, mas é na verdade um cubo subdividido, com `Project on sphere` forçado          |
| Cylinder       | ![](/icons/cylinder.webp)                | Pode adicionar um furo central ao cilindro, por exemplo para fazer um tubo oco                                   |
| Torus          | ![](/icons/torus.webp)                   | O torus pode ser um bom ponto de partida para anéis                                                               |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                                 |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                                 |
| UV-sphere      | ![](/icons/circle.webp)                  | Uma esfera com layout de polígonos irregular, ver [Aviso abaixo](#uv-sphere)                                     |
| Plane          | ![](/icons/rectangle.webp)               | É um plano simples; note que é a única primitiva que não é fechada                                               |
| Tube           | ![](/icons/tool_tube.webp)               | ver [Tube](tools#tube)                                                                                            |
| Lathe          | ![](/icons/tool_lathe.webp)              | ver [Lathe](tools#lathe)                                                                                          |
| Triplanar      | ![](/icons/triplanar.webp)               | ver [Triplanar](#triplanar)                                                                                       |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | ver [Shadow Catcher](#shadow-catcher)                                                                             |
| Head           | ![](/icons/face.webp)                    | Uma cabeça simples com uma layer para misturar entre masculino/feminino                                          |

::: tip
Se se pergunta qual é a malha base quando inicia o Nomad: também é um cubo subdividido.  
No entanto, a malha base no Nomad não usa `Project on sphere`, o que significa que não é perfeitamente redonda.
:::

### Barra de ferramentas de primitivas {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Depois de uma primitiva ser criada, aparece uma barra de ferramentas para controlar os seus parâmetros.

* `Validate` Converte a primitiva num objeto padrão para que possa ser esculpido e pintado.
* `Edit` Alterna a exibição do gizmo da primitiva. Este é mostrado diretamente na primitiva para controlar os seus parâmetros, por exemplo a largura do cubo ou o raio do furo de um cilindro.
* `Mirror` Alterna a colocação de um repetidor de espelho acima da primitiva.
* `...` Mostra o menu da primitiva.

Primitivas diferentes terão opções extra na barra de ferramentas:

* `Project` A esfera é construída como um cubo subdividido, o que é melhor para escultura, mas significa que não é perfeitamente redonda. Esta opção força a forma a aproximar‑se de uma esfera perfeita. O icosaedro partilha esta opção.
* `Cap` Alterna tampas numa forma, por exemplo um cilindro pode ter tampas em cima, em baixo, em ambos ou nenhuma.
* `Hole` Alterna a criação de um furo no centro da forma. Cicla entre sem furo, furo com um único raio ou furo com raios diferentes em cima e em baixo.
* `Radius` Alterna se um cilindro deve ter um único raio ou raios diferentes em cima e em baixo.
* `Disk` Alterna se um plano deve ser uma forma de 4 lados ou uma forma circular.

A pequena barra de ferramentas abaixo da barra principal permite alternar entre o gizmo da primitiva e o gizmo de transformação.

::: tip

Clicar no título da barra de ferramentas alterna‑a entre o topo e a base do ecrã. Clicar na seta no canto recolhe‑a.

:::


### Menu de primitivas {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Contém todos os parâmetros da primitiva selecionada. Parâmetros são as descrições básicas de uma forma. Para descrever um anel, por exemplo, descreveria o seu raio exterior, o raio interior e o número de polígonos.

A maioria dos parâmetros das primitivas deve ser autoexplicativa, e há alguns parâmetros comuns partilhados por todas:

* `UVs` O pequeno botão de UVs no topo do menu alterna a criação de coordenadas UV
* `Validate` O pequeno botão de validação converte a primitiva num objeto padrão para que possa ser esculpido e pintado.
* `Max faces` Define um limite máximo para a quantidade de polígonos no objeto para evitar que o dispositivo bloqueie.
* `Post subdivision` Ativa o número escolhido de subdivisões da secção de multirresolução do menu de topologia. Pode ser usado para criar primitivas suavizadas, com cantos suaves, em combinação com divisões de topologia baixas. Por exemplo, definir as divisões de topologia de um cubo para 2 e as subdivisões pós para 4 criará um cubo com cantos suaves.
* `Linear subdivision` Define quantos níveis de subdivisão linear usar antes da subdivisão suave normal. Pode ser usado para controlar quão vivos ou suaves são os cantos nas superfícies subdivididas. Por exemplo, defina as divisões de topologia de um cubo para 2, subdivisões pós para 4 e depois experimente alterar as subdivisões lineares entre 0 e 4. Os cantos do cubo passarão de suaves a vivos.

### Topologia {#topology}

Controla o número de polígonos numa primitiva. Normalmente os controlos estão ligados, por isso alterar o slider ativo ajustará todos os polígonos de forma uniforme. Pode tocar no botão de desligar e controlar separadamente as divisões X/Y/Z de uma forma.

### Geometria {#geometry}

Controla o tamanho geral de uma primitiva, em unidades X/Y/Z para formas quadradas e em raio para formas redondas.


### Esfera UV {#uv-sphere}
::: warning
A UV Sphere não é adequada para escultura, especialmente nos polos.

Prefira as primitivas [Sphere](#sphere), [Box](#box) ou [Icosahedron](#icosahedron), juntamente com a opção `Project on sphere`.

Note que a topologia pode ser aceitável para escultura se usar um valor muito baixo para os sliders de `Division`.  
Depois pode usar o slider `Overall Subdivision` para aumentar o número de polígonos.

Embora não seja adequada para escultura geral, é útil para olhos; se rodar a esfera de forma que os polos fiquem na pupila, o layout dos polígonos encaixará naturalmente para pintar e esculpir a íris e a pupila.
:::


### Triplanar {#triplanar}
Esta primitiva é especial, pois deve usar a [ferramenta de máscara](tools.md#mask) nela para moldar a geometria.

![](/videos/triplanar.mp4)


::: tip
Toque duas vezes num plano e a câmara focará esse plano em particular.  
Isto não funcionará se rodar a primitiva com o gizmo.
:::

O Triplanar usa a informação de máscara de 3 planos para preencher uma grelha de voxels que é depois poligonizada (graças ao [Voxel Remesher](topology.md#voxel-remeshere)).

Cada plano tem o seu próprio plano de simetria.

::: warning
Sempre que atualizar o tamanho da primitiva Triplanar, a qualidade da pintura da máscara irá degradar‑se.

Por agora não há opção para “bloquear” a pintura num único plano, mas talvez venha no futuro.  
Pode usar a [Connected Topology](stroke.md#connected-topology) para ajudar um pouco, pois se o cursor estiver precisamente sobre um plano não afetará os outros planos.
:::

### Captura de sombra {#shadow-catcher}
Adiciona um plano com o material shadow catcher. Veja [Shadow Catcher material](material.md#shadow-catcher) para mais detalhes. 


## Grupo/Câmera {#groupcamera}
### Grupo {#group}
Cria um objeto “vazio”, ao qual pode atribuir outros objetos como filhos. Pode ser usado simplesmente para organizar a hierarquia, colocando muitos objetos dentro de um grupo e depois fechando‑o. Um grupo também pode ser usado como auxiliar para mover objetos; muitos objetos podem ser colocados dentro de um grupo e depois o grupo é movido, rodado ou escalado com a ferramenta de gizmo.

### Adicionar vista {#add-view}
Cria uma câmara.

## Repetidores {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repetidores são nós que criam instâncias dos objetos abaixo deles. 

### Matriz {#array}
![](/images/scene_primitive_array.webp)

Quando objetos são tornados filhos deste nó, podem ser instanciados numa disposição em grelha. Quando selecionado, tem controlos para:
* Fit inside - alterna entre controlar o tamanho da grelha/caixa do array ou controlar o espaço entre as instâncias do array
* CountX/Y/Z - o número de instâncias em cada eixo
* OffsetX/Y/Z - distância entre as instâncias quando “fit inside” está ativado
* SizeX/Y/Z - a largura/altura/profundidade da grelha total do array quando “fit inside” está ativado.

### Curva {#curve}
![](/images/scene_primitive_curve.webp)
Cria uma curva; filhos deste nó serão repetidos ao longo da curva. Quando selecionado, tem controlos para:
* Edit - permite adicionar pontos à curva e mover pontos na curva
* Snap - encaixa pontos da curva noutra geometria
* Align - roda as formas filhas para se alinharem na direção da curva
* Count - o número de instâncias
* Closed - alterna a curva entre unir início e fim ou ser uma curva aberta
* Radius - alterna controlos em cada ponto da curva para controlar a escala das instâncias
* Twist - alterna controlos em cada ponto da curva para controlar a rotação de torção das instâncias 
* B-spline - alterna entre as instâncias seguirem exatamente a curva ou usarem interpolação B-spline, que tem resultados mais suaves. 

### Radial {#radial}
![](/images/scene_primitive_radial.webp)

Filhos deste nó serão instanciados num círculo. Mova o objeto filho para alterar o raio deste repetidor. Quando selecionado, tem controlos para:
* RadialX/Y/Z - selecionar estes botões define o eixo radial e o número de instâncias.



### Espelho {#mirror}
![](/images/scene_primitive_mirror.webp)

Filhos deste nó serão espelhados através de um eixo. Quando selecionado, tem controlos para:
* Gizmo - ativa o gizmo de transformação para definir o centro do espelho. Também pode ser rodado e escalado. Quando terminar, toque novamente em gizmo para mostrar os controlos padrão.
* X/Y/Z - define o plano de espelho

Todos os repetidores têm um controlo `Validate`, que converte o resultado do repetidor e pergunta como efetuar essa conversão:
* Join children - as instâncias são unidas num único objeto
* Keep instances - as instâncias permanecem como instâncias, mas deixam de ter o repetidor como “pai”
* Un-instances - as instâncias são convertidas em objetos únicos

::: tip Dica: Combinar repetidores
Repetidores podem ser colocados como filhos uns dos outros, e vários objetos podem ser filhos de repetidores, levando a efeitos complexos.

![](/images/scene_repeater_combine.webp)
:::

::: tip Dica: Pivots de repetidores

Alguns repetidores tentarão autoajustar o pivot dos objetos filhos, por isso, mesmo que os mova ou rode com o gizmo, eles não se moverão. Se precisar de substituir este comportamento, insira um grupo entre o repetidor e o filho. Agora pode mover a forma filha independentemente do repetidor.
:::

## Luz {#light}

![](/images/scene_primitive_light.webp)

### Direcional {#directional}
Cria uma luz direcional, uma fonte de luz infinitamente distante como o sol.

### Spot {#spot}
Cria uma luz spot, com controlos sobre a largura do cone e suavidade

### Ponto {#point}
Cria uma luz pontual

## Avançado {#advanced}
### Focar no item {#focus-on-item}
Fazer duplo clique num item na lista da Cena centrará a câmara nesse item na vista 3D.

### Sincronizar visibilidade {#sync-visibility}
Usar o ícone de olho afetará todos os itens selecionados. 

### Instância: Mostrar {#instance-show}
Mostra uma cápsula de cor à esquerda da lista da cena para indicar instâncias.


### Ícones {#icons}
Define o tamanho e a opacidade dos ícones de grupo, luz, câmara e espelho na viewport

### Linhas de hierarquia {#hierarchy-lines}
Mostra uma linha entre o pai e os seus filhos na viewport

## Barra de ferramentas inferior {#bottom-toolbar}
Estes ícones alternam a visibilidade de Grupo, Luz, Câmara, Repetidor e linhas de Hierarquia na viewport.
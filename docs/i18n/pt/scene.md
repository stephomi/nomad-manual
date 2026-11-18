# ![](/icons/scene.webp) Cena {#scene}

Este menu permite gerenciar os objetos, as luzes, as câmeras e os repetidores no Nomad. Ele mostra a hierarquia da cena em forma de árvore, onde você pode alterar muitos aspectos dos seus objetos. Também é por aqui que você cria novos objetos e combina ou separa objetos de várias maneiras.


![](/images/scene_menu_summary.webp)


## Barra de atalhos {#shortcut-bar}
| Ação                   | Ícone                             | Descrição                                                                                                           |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Adicionar...](#add-menu) | ![](/icons/plus.webp)         | Abre o [menu Adicionar](#add-menu) para adicionar um objeto à cena                                                  |
| Apagar                 | ![](/icons/trash.webp)           | Apaga os objetos selecionados. Os secundários deles são mantidos.                                                   |
| Bloquear               | ![](/icons/lock.webp)            | Impede que os objetos selecionados sejam selecionados na viewport. Eles ainda podem ser selecionados pela árvore. Bloquear um grupo bloqueia tudo o que está dentro dele. Toque de novo para desbloquear. |
| [Unir](#join)          | ![](/icons/merge.webp)           | Une os objetos selecionados em um único objeto, sem alterar a geometria                                             |
| [Separar...](#separate) | ![](/icons/separate.webp)       | Abre a janela [Separar](#separate), para dividir um objeto em vários. O inverso da operação Unir                     |
| [Booleano...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Abre a janela [Booleano](#boolean)                                                                          |
| Clonar                 | ![](/icons/clone.webp)           | Duplica os objetos selecionados em novos objetos                                                                    |
| Instância              | ![](/icons/link.webp)            | Duplica os objetos selecionados como instâncias: as alterações de modelagem em uma se aplicam a todas as instâncias. |
| Desinstanciar          | ![](/icons/unlink.webp)          | Converte uma instância em uma forma única, para que as alterações de modelagem não sejam mais copiadas para as outras instâncias |
| Sincronizar            | ![](/icons/checked.webp)         | Quando marcado, as operações se aplicam a todas as instâncias dos objetos selecionados, não só aos selecionados. Só fica disponível quando a seleção contém instâncias. A [aba Sincronizar](#sync) da janela `Avançado` define quais operações seguem esta caixa. |

::: tip
Quando uma operação também vai afetar as outras instâncias, um pequeno ícone de elo aparece no botão dela.
:::


## Árvore da cena {#tree-view}
![](/images/scene_treeview.webp) 

A árvore lista os objetos, grupos, repetidores, luzes e câmeras da cena. Ao lado do nome de uma malha você vê a contagem de vértices dela, com um ícone de camada colorido quando ela tem camadas. Cada linha tem estes botões:

| Ação         | Ícone                      | Descrição                |
| :----------: | :------------------------: | :----------------------: |
| Nome         | ![](/icons/pencil.webp)   | Renomeia o objeto. Se ele estiver selecionado, todos os objetos selecionados são renomeados de uma vez, com um número acrescentado. Mantenha pressionado para renomeá-lo junto com os secundários. |
| Selecionar   | ![](/icons/checked.webp)  | Seleciona/desmarca       |
| Visível      | ![](/icons/eye_open.webp) | Mostra/oculta            |
| Menu         | ![](/icons/more.webp)     | Abre o [menu do objeto](#object-menu) |

::: tip DICA: Selecionar ou ocultar muitos objetos rapidamente

Toque no ícone de seleção para alternar um único objeto, ou arraste na vertical sobre a coluna de seleção para selecionar vários objetos. O mesmo vale para a coluna de visibilidade.

Mantenha pressionado o ícone de seleção ou de visibilidade para afetar também os secundários.

:::

### Cabeçalho da árvore {#tree-view-header}

A linha acima da lista tem alguns atalhos úteis:

* ![](/icons/sort_down.webp) - recolhe ou expande todos os grupos de uma vez.
* ![](/icons/preview.webp) - ativa ou desativa as `Pré-visualizações de objetos`, uma pequena miniatura renderizada de cada objeto da lista.
* ![](/icons/search.webp) - filtra a lista pelo nome.

### Organizar a árvore {#tree-view-manipulation}

Mantenha pressionado um item da árvore até ele ficar destacado. Aí você pode movê-lo para cima ou para baixo na árvore, ou arrastá-lo sobre outro item para torná-lo secundário desse item.

Quando vários itens estão selecionados, um deles é a seleção principal e aparece mais claro. Mantenha pressionado e arraste qualquer um deles para mover todos os objetos selecionados de uma vez.

Quando você seleciona um item pai, por padrão todos os itens secundários também são selecionados. Tocar no pai de novo alterna entre selecionar só o pai ou o pai com os secundários.

Toque duas vezes em um item para centralizar a câmera nele (veja [Avançado](#focus-on-item)).

### Menu do objeto {#object-menu}

Clicar no botão de reticências (...) de um objeto na árvore abre o menu do objeto.
Muitas destas opções são iguais às da barra de atalhos no topo, repetidas por conveniência.

|       Ação          |                        Ícone                       | Descrição                                                                                                                                                               |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nome         |              ![](/icons/pencil.webp)           | Muda o nome do objeto                                                                                                                                                   |
|    Desinstanciar    |              ![](/icons/unlink.webp)           | Converte uma instância em uma forma única, para que as alterações de modelagem não sejam mais copiadas para as outras instâncias.                                        |
|      Instância      |               ![](/icons/link.webp)            | Duplica o objeto como instância: as alterações de modelagem em uma se aplicam a todas as instâncias.                                                                     |
|       Clonar        |              ![](/icons/clone.webp)            | Duplica o objeto em um novo objeto                                                                                                                                      |
|       Apagar        |              ![](/icons/trash.webp)            | Apaga o objeto. Os secundários dele são mantidos, a menos que `Secundários` esteja marcado.                                                                             |
|     Secundários     |            ![](/icons/hierarchy.webp)          | Quando marcado, `Instância`, `Clonar` e `Apagar` também agem sobre os secundários do objeto.                                                                            |
| Separar por Partes  |             ![](/icons/separate.webp)          | Se um objeto é formado por partes desconectadas, cria um objeto separado para cada uma delas. O inverso da operação Unir.                                               |
| Separar por Grupos  |            ![](/icons/group.webp)          | Se um objeto tem vários grupos de faces, cria um objeto separado para cada grupo de faces.                                                                                 |
| Separar por Camadas |              ![](/icons/layer.webp)            | Se um objeto tem camadas, cria objetos separados para a malha base e para cada camada. Útil para enviar blendshapes para outros aplicativos.                             |
|   Unir → Camadas    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Se vários objetos estão selecionados e têm a mesma topologia, combina esses objetos em camadas do objeto principal (os outros objetos são apagados). De novo, útil para blendshapes VINDOS de outros aplicativos.<br><br> As camadas ficam desativadas por padrão. Ative-as se precisar ajustar os controles delas. |
| Curva (Repetidor)   |              ![](/icons/curve.webp)            | Só para um tubo ou um torno: adiciona um repetidor [Curva](#curve) que segue a mesma curva, como secundário do objeto.                                                  |
|        Tubo         |             ![](/icons/tube.webp)              | Para um torno, adiciona um [tubo](tools.md#tube) que segue o perfil dele, como secundário. Para um cilindro, um cone ou um toro, converte-o em um tubo com a mesma forma, para que você possa curvá-lo ao longo de uma curva. |




### Seleção múltipla {#multiselection}
Selecionar vários objetos serve para duas coisas:
- usar a ferramenta gizmo para mover vários objetos de uma vez
- combinar objetos com as operações Unir e Booleano.

Na árvore, toque no ícone de seleção de cada objeto ou arraste ao longo da coluna de seleção. Ao tocar nos nomes, segure o atalho `Máscara` (ou `Ctrl` no teclado) para adicionar ou remover um único objeto, ou segure o atalho `Suavizar` (ou `Shift`) para selecionar todos os objetos entre o atual e o que você tocar.

::: tip Seleção múltipla rápida
Você também pode selecionar vários objetos na viewport segurando o atalho `Suavizar` (ou `Shift`) e tocando em outra malha.

Para desmarcar um objeto, toque nele de novo (só se a seleção tiver mais de um objeto).
:::

O gizmo move todos os objetos selecionados juntos, veja [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Unir {#join}
Esta opção simplesmente transforma vários objetos selecionados em um único objeto.
Os pontos e as UVs mais próximos do que o [raio de soldagem](#weld-radius) são fundidos.

Há um exemplo em vídeo na seção [Separar](#separate).

## ![](/icons/bool_subtract_circle.webp) Booleano {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina objetos em uma única superfície.

`Combinar voxels` preserva o volume dos objetos e calcula novos polígonos distribuídos por igual na superfície. Graças a essa etapa de cálculo, a combinação por voxels lida com geometrias complexas, mas pode perder detalhes finos se a resolução escolhida não for alta o bastante.

`Booleano` tenta manter os polígonos na disposição original e costura os polígonos onde os objetos se sobrepõem. Isso pode dar resultados bem mais limpos e nítidos que a combinação por voxels, mas exige malhas "fechadas": os objetos não podem ter furos nem formas malformadas. Se der errado, a combinação por voxels geralmente funciona.

### Operações booleanas {#boolean-operations}
Tanto Combinar voxels quanto Booleano usam a visibilidade dos objetos para controlar a operação, como lembram as indicações na parte de baixo da janela:

#### União {#union}
Os dois objetos visíveis criam uma **união** booleana: as cascas externas dos objetos são combinadas, sem superfícies internas. ![](/images/boolean_union.webp)

#### Subtração {#subtract}
Um objeto oculto = **subtração** booleana: o objeto oculto é subtraído do objeto visível. ![](/images/boolean_subtract.webp)

#### Interseção {#intersect}
Os dois objetos ocultos = **interseção** booleana: cria uma nova forma só onde os dois objetos se sobrepõem. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Combinar voxels {#voxel-merge-button}
Este botão faz uma combinação por voxels dos objetos selecionados. Em um único objeto, ele refaz a topologia com polígonos distribuídos por igual, o que é útil quando um objeto tem polígonos esticados. As opções abaixo funcionam como as do [remalhamento por voxels](topology.md#voxel-remesher).

### Resolução {#resolution}
A resolução da grade 3d de voxels usada no cálculo. Quando você muda este valor, um padrão xadrez aparece sobre o objeto para mostrar o tamanho dos polígonos.

O seletor ao lado do controle pega o detalhe da densidade da malha sob o seu dedo. O botão ao lado dele troca o controle para `Comprimento da borda`, um tamanho no mundo: o mesmo valor dá o mesmo detalhe em qualquer objeto.

### Construir multirresolução {#build-multiresolution}
Cria níveis de multirresolução abaixo da resolução escolhida. Por exemplo, se a resolução é 400 e Construir multirresolução é 3, você obtém uma nova malha com uns 296.000 polígonos, mas com 3 níveis de subdivisão mais baixos, de cerca de 74.000, 18.500 e 4.600.

### Engrossar partes finas {#thicken-thin-parts}
Engrossa as partes finas demais para a grade de voxels, para que não se rompam. Não está disponível com `Bordas nítidas` ou `Borda nítida`.

### Furos {#holes}
Como os furos dos objetos abertos são fechados antes da combinação:
* `Preencher` - cada furo é fechado sozinho, a partir da borda dele.
* `Forma` - os furos são fechados seguindo a superfície ao redor, e as peças abertas que se sobrepõem são unidas.

### ![](/icons/angle.webp) Manter bordas nítidas {#keep-sharp-edges}
O botão `Bordas nítidas` encaixa a malha de voxels nas bordas nítidas dos objetos. Funciona melhor em formas simples e pode causar distorções em algumas áreas.

### ![](/icons/group.webp) Borda nítida {#sharp-border}
As novas faces seguem as bordas dos grupos de faces, e uma borda continua nítida onde a superfície forma um vinco ao longo dela.

### ![](/icons/group_separate.webp) Manter grupos separados {#keep-groups-separate}
Cada grupo de faces é remalhado sozinho: os grupos nunca se fundem, e cada um continua sendo uma peça fechada no seu próprio grupo. Neste modo, a multirresolução não é construída.

### ![](/icons/bool_subtract_circle.webp) Botão Booleano {#boolean-button}
Este botão faz uma operação booleana de polígonos com a biblioteca Manifold, de Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Limpar sobreposições {#clean-overlaps}
Quando só um objeto está selecionado, o botão `Booleano` vira `Limpar sobreposições`: ele funde as partes do objeto que se atravessam em uma superfície limpa.


## ![](/icons/separate.webp) Separar {#separate}
Se você tem um único objeto formado por várias partes desconectadas, pode separá-lo em vários objetos.
É o oposto de [Unir](#join).

A janela `Separar...` oferece três maneiras de separar os objetos selecionados:
* `Separar por Partes` - cria um objeto separado para cada parte desconectada.
* `Separar por Grupos` - cria um objeto separado para cada grupo de faces.
* `Separar por Camadas` - cria objetos separados para a malha base e para cada camada.

![](/videos/merge_separate.mp4)

## ![](/icons/plus.webp) Menu Adicionar {#add-menu}

![](/images/scene_addmenu_overview.webp)

Este menu cria primitivas, grupos, câmeras, repetidores e luzes.

As primitivas são formas básicas que podem ser ajustadas por parâmetros. Quando a primitiva estiver do jeito que você quer, você a "valida", o que converte esses parâmetros em uma malha de polígonos que pode ser esculpida e pintada. Depois de validada, os parâmetros de uma primitiva não podem mais ser ajustados.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) No gizmo {#on-gizmo}
Coloca a nova primitiva onde está a forma selecionada ou o gizmo. Quando desativado, a primitiva é colocada no centro da cena.

### ![](/icons/gizmo.webp) Selecionar gizmo {#select-gizmo}
Muda automaticamente para a ferramenta gizmo quando uma nova primitiva é criada.

### ![](/icons/cog.webp) Avançado {#add-advanced}

Este menu define onde as novas primitivas, grupos e repetidores são criados. Eles podem ficar no objeto selecionado, na origem do mundo ou na posição do gizmo.


### UVs {#uvs}
O botão `UVs` ao lado do título Primitiva ativa as UVs nas primitivas. As UVs (muitas vezes chamadas de coordenadas de textura) são dados extras usados em 3d para aplicar texturas nas superfícies. Elas ocupam mais memória, mas na maioria dos dispositivos isso não deve preocupar, a não ser que você chegue a contagens de polígonos muito altas (por exemplo, 10 milhões de polígonos ou mais).

### Primitivas {#primitives}

| Primitiva      | Ícone                                     | Descrição                                                                                                       |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Caixa          | ![](/icons/cube.webp)                    | Um cubo simples; você controla as divisões em X, Y e Z                                                          |
| Esfera de quads | ![](/icons/circle.webp)                 | Uma caixa subdividida com `Esfera` sempre ativado, o que dá uma distribuição regular de quads, boa para esculpir |
| Cilindro       | ![](/icons/cylinder.webp)                | Você pode adicionar um furo central ao cilindro, por exemplo para fazer um cano oco                             |
| Toro           | ![](/icons/torus.webp)                   | O toro pode ser um bom ponto de partida para anéis                                                              |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaedro      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Esfera UV      | ![](/icons/circle.webp)                  | Uma esfera com distribuição irregular de polígonos, veja o [aviso abaixo](#uv-sphere)                           |
| Plano          | ![](/icons/rectangle.webp)               | Um plano simples; é a única primitiva que não é fechada                                                         |
| Texto          | ![](/icons/text.webp)                    | Texto 3d, com fonte, estilo, alinhamento, profundidade e curvatura. `Mesclar letras` funde as letras que se tocam |
| Tubo           | ![](/icons/tube.webp)                    | veja [Tubo](tools#tube)                                                                                         |
| Torno          | ![](/icons/lathe.webp)                   | veja [Torno](tools#lathe)                                                                                       |
| Triplano       | ![](/icons/triplanar.webp)               | veja [Triplano](#triplanar)                                                                                     |
| VDM            | ![](/icons/vdm.webp)                     | Um plano preparado para esculpir um carimbo de deslocamento vetorial: ele vem com UVs e fica de frente para a câmera |
| Capturador de sombras | ![](/icons/material_shadow_catcher.webp) | veja [Capturador de sombras](#shadow-catcher)                                                          |
| Cabeça         | ![](/icons/face.webp)                    | Uma cabeça simples com uma camada para misturar entre masculino e feminino                                      |

::: tip
Se você está se perguntando qual é a malha base que aparece quando você abre o Nomad: também é uma caixa subdividida.
Mas a malha base do Nomad não usa `Esfera`, ou seja, ela não é perfeitamente redonda.
:::

### Barra de ferramentas da primitiva {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Quando uma primitiva é criada, aparece uma barra de ferramentas para controlar os parâmetros dela.

* `Validar` Converte a primitiva em um objeto comum, para que possa ser esculpido e pintado.
* `Espelhar` Coloca ou remove um repetidor de espelho acima da primitiva.
* `Todos` (ícone de olho) Escolhe quais alças aparecem diretamente sobre a primitiva para controlar os parâmetros dela, por exemplo a largura do cubo ou o raio do furo de um cilindro: `Nenhum`, `Todos` ou só um tipo (raio, furo, perfil...), conforme a primitiva.
* `Divisão` O número de divisões da primitiva, aqui ao longo de X para uma caixa.
* `Densidade constante` Quando você estica a primitiva ao longo de um eixo com o gizmo, o tamanho e as divisões aumentam em vez de os polígonos se esticarem, assim as faces continuam quadradas. Disponível em caixas, planos e cilindros.
* `...` Abre o menu da primitiva.

Algumas primitivas têm opções extras na barra:

* `Esfera` A esfera é construída como um cubo subdividido, o que é melhor para esculpir, mas significa que ela não é perfeitamente redonda. Esta opção aproxima a forma de uma esfera perfeita. O icosaedro também tem esta opção.
* `Tampa` Ativa ou desativa as tampas nas pontas de uma forma: por exemplo, um cilindro pode ter tampa em cima, embaixo, nos dois lados ou em nenhum.
* `Furo` Cria um furo atravessando o centro de uma forma. Alterna entre sem furo, furo com um único raio ou furo com raios diferentes em cima e embaixo.
* `Raio` Define se um cilindro tem um único raio ou raios diferentes em cima e embaixo.
* `Disco` Define se um plano tem 4 lados ou forma de círculo.

A barrinha abaixo da barra principal alterna entre o gizmo da primitiva e o gizmo de transformação.

::: tip

Clicar no título da barra a leva para o topo ou para baixo da tela. Clicar na seta do canto a recolhe.

:::


### Menu da primitiva {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Ele reúne todos os parâmetros da primitiva selecionada. Os parâmetros são a descrição básica de uma forma. Para descrever um anel, por exemplo, você daria o raio externo, o raio interno e o número de polígonos.

A maioria dos parâmetros das primitivas fala por si, e alguns são comuns a todas as primitivas:

* `UVs` O pequeno botão UVs no topo do menu ativa ou desativa a criação de coordenadas UV
* `Validar` O pequeno botão Validar converte a primitiva em um objeto comum, para que possa ser esculpido e pintado.
* `Máximo de faces` Define um limite máximo de polígonos no objeto, para não travar o seu dispositivo.
* `Subdivisão posterior` Aplica o número escolhido de subdivisões da seção de multirresolução do menu Topologia. Junto com poucas divisões de topologia, serve para criar primitivas suavizadas, com cantos arredondados. Por exemplo, uma caixa com 2 divisões de topologia e 4 subdivisões posteriores fica com cantos suaves.
* `Subdivisão linear` Define quantos níveis de subdivisão linear usar antes da subdivisão suave normal. Serve para controlar o quanto os cantos das superfícies subdivididas ficam nítidos ou suaves. Por exemplo, coloque 2 divisões de topologia e 4 subdivisões posteriores em uma caixa e depois experimente variar a subdivisão linear entre 0 e 4. Os cantos da caixa vão de suaves a nítidos.

### Topologia {#topology}

Controla o número de polígonos de uma primitiva. Normalmente os controles estão vinculados, então mexer no único controle ativo ajusta todos os polígonos por igual. Você pode tocar no botão de desvincular para controlar as divisões X/Y/Z de uma forma separadamente.

### Geometria {#geometry}

Controla o tamanho geral de uma primitiva, em unidades X/Y/Z para as formas retas e em raio para as formas redondas.


### ![](/icons/circle.webp) Esfera UV {#uv-sphere}
::: warning
A esfera UV não é adequada para esculpir, principalmente nos polos.

Prefira as [primitivas](#primitives) Esfera de quads, Caixa ou Icosaedro, com a opção `Esfera`.

A topologia pode ser aceitável para esculpir se você usar um valor bem baixo nos controles `Divisão`.
Depois você pode usar o controle `Subdivisão geral` para aumentar o número de polígonos.

Embora não sirva para esculpir em geral, ela é útil para olhos: se você girar a esfera para que os polos fiquem na pupila, a distribuição dos polígonos se encaixa naturalmente para pintar e esculpir a íris e a pupila.
:::


### ![](/icons/triplanar.webp) Triplano {#triplanar}
Esta primitiva é especial: você deve usar a [ferramenta Máscara](tools.md#mask) nela para modelar a geometria.

![](/videos/triplanar.mp4)


::: tip
Toque duas vezes em um plano e a câmera se concentra nesse plano.
Mas isso não funciona se você girar a primitiva com o gizmo.
:::

O Triplano usa a informação da máscara de 3 planos para preencher uma grade de voxels, que depois é convertida em polígonos (graças ao [remalhamento por voxels](topology.md#voxel-remesher)).

Cada plano tem seu próprio plano de simetria.

::: warning
Cada vez que você muda o tamanho da primitiva Triplano, a qualidade da máscara pintada piora.

Por enquanto não há opção para "travar" a pintura em um único plano, mas talvez isso venha no futuro.
A [Topologia conectada](stroke.md#connected-topology) ajuda um pouco: se o cursor estiver exatamente sobre um plano, ele não afeta os outros planos.
:::

### ![](/icons/material_shadow_catcher.webp) Capturador de sombras {#shadow-catcher}
Adiciona um plano com o material capturador de sombras. Veja [Material capturador de sombras](material.md#shadow-catcher) para mais detalhes.


## Grupo/Câmera {#groupcamera}
### ![](/icons/share.webp) Grupo {#group}
Cria um objeto "vazio", sob o qual você pode colocar outros objetos. Serve para organizar a hierarquia, juntando muitos objetos em um grupo e depois recolhendo-o. Um grupo também ajuda a mover objetos: coloque vários objetos sob um grupo e depois mova, gire ou redimensione o grupo com a ferramenta gizmo.

### ![](/icons/camera.webp) Câmera {#add-view}
Cria uma câmera.

## Repetidores {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Os repetidores são nós que criam instâncias dos objetos abaixo deles.

### ![](/icons/array.webp) Matriz {#array}
![](/images/scene_primitive_array.webp)

Os objetos colocados como secundários deste nó podem ser instanciados em uma grade. Quando selecionado, ele tem controles para:
* `Encaixar dentro` - quando ativado, todas as cópias ficam dentro dos limites da matriz; quando desativado, os controles definem o espaço entre as cópias
* `Contagem X/Y/Z` - o número de instâncias em cada eixo
* `Tamanho X/Y/Z` - o tamanho da grade em cada eixo, ou a distância entre as cópias quando `Encaixar dentro` está desativado
* `Randomizar...` - adiciona variações aleatórias às cópias, veja [Randomizar](#curve) abaixo.

### ![](/icons/curve.webp) Curva {#curve}
![](/images/scene_primitive_curve.webp)
Cria uma curva; os secundários deste nó são repetidos ao longo dela. Quando selecionado, ele tem controles para:
* `Curva` - edita a curva: adiciona pontos e move os pontos da curva.
* `Mostrar` - mostra ou esconde a curva e seus pontos.
* `Ajuste` - encaixa os pontos da curva em outra geometria.
* `Simetria` - edita a curva de forma simétrica.
* `Fechado` - liga o início ao fim da curva, ou a deixa aberta.
* `B-spline` - faz as instâncias seguirem a curva exatamente, ou usa interpolação b-spline, que dá resultados mais suaves.
* `Deformar` - curva cada cópia ao longo da curva, para que as cópias encostem nas vizinhas (`Suave` curva os lados delas para que se encontrem sem ângulo).
* `Alinhar` - gira as cópias para seguir a direção da curva.
* `Pivô` - o pivô das cópias: a própria curva (`Ela mesma`) ou os secundários dela.
* `Contagem` - o número de instâncias. O botão de modo ao lado troca para `Distância`: um espaçamento fixo entre as cópias, e a contagem acompanha o comprimento da curva.
* `Raio` - controles em cada ponto da curva para definir a escala das instâncias.
* `Torção` - controles em cada ponto da curva para definir a rotação de torção das instâncias.
* `Alternar` - gira uma cópia sim, uma não, em torno da curva: 90° para elos de corrente, 180° para folhas ou dentes de zíper, em torno do `Eixo` que você escolher.
* `Espiral...` - enrola as cópias em torno da curva, em vários fios (corda, trança, fita...).
* `Randomizar...` - adiciona variações aleatórias às cópias; cada linha pode, em vez disso, somar o mesmo valor a cada cópia.

Abaixo da barra, a opção `(mesclar)` funde um ponto com outro quando você o arrasta sobre ele. `IK` (cinemática inversa) permite posar a curva: arraste um ponto e os pontos ligados acompanham. Toque em um ponto para travá-lo ou destravá-lo, ou mantenha pressionado para travar ou destravar todos; os pontos travados ficam no lugar.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Os secundários deste nó são instanciados em círculo. Mova o objeto secundário para mudar o raio deste repetidor. Quando selecionado, ele tem controles para:
* RadialX/Y/Z - estes botões definem o eixo radial e o número de instâncias.



### ![](/icons/mirror.webp) Espelhar {#mirror}
![](/images/scene_primitive_mirror.webp)

Os secundários deste nó são espelhados em relação a um eixo. Quando selecionado, ele tem controles para:
* Gizmo - ativa o gizmo de transformação para definir o centro do espelho. Ele também pode ser girado e redimensionado. Quando terminar, toque em gizmo de novo para ver os controles normais.
* X/Y/Z - define o plano do espelho

### ![](/icons/surface.webp) Superfície {#surface}

Os secundários deste nó são copiados sobre a superfície de um objeto: uma cópia por face, por aresta ou por vértice, ou espalhadas ao acaso. Quando selecionado, ele tem controles para:
* Modo - coloca as cópias nas `Faces`, nas `Arestas` ou nos vértices, ou as `Espalhar`.
* A cada - uma cópia a cada N faces, arestas ou vértices. `Aleatório` os escolhe ao acaso, e `Redistribuir` sorteia outro conjunto aleatório.
* Espaçamento - ao espalhar, a distância mínima entre duas cópias.
* Alinhar - as cópias ficam de pé sobre a superfície, seguindo a normal dela, em vez de manter a orientação do original.
* Encaixar - projeta o original no ponto mais próximo da superfície, e as cópias acompanham.
* Ajustar tamanho, Cisalhamento - redimensionam e esticam as cópias conforme a forma de cada face.
* Deformar - curva cada cópia sobre a sua face, ou ao longo da sua aresta, para que as cópias vizinhas se encontrem sem frestas.

Todos os repetidores têm um controle `Validar`, que fixa o resultado do repetidor e pergunta como fazer isso:
* Unir secundários - as instâncias são unidas em um único objeto
* Manter instâncias - as instâncias continuam sendo instâncias, mas não têm mais o repetidor como "pai"
* Desinstanciar - as instâncias são convertidas em objetos únicos

`Achatar tudo` também fixa os repetidores aninhados dentro deste, para que cada cópia vire um objeto comum.

::: tip Dica: Combine repetidores
Os repetidores podem ser colocados uns sob os outros, e vários objetos podem ser secundários de repetidores, o que permite efeitos complexos.

![](/images/scene_repeater_combine.webp)
:::

::: tip Dica: Pivôs dos repetidores

Alguns repetidores tentam ajustar automaticamente o pivô dos objetos secundários, então, mesmo que você os mova ou gire com a ferramenta gizmo, eles não saem do lugar. Se precisar contornar esse comportamento, coloque um grupo entre o repetidor e o secundário. Aí você pode mover a forma secundária independentemente do repetidor.
:::

## Luz {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Direcional {#directional}
Cria uma luz direcional, uma fonte de luz infinitamente distante, como o sol.

### ![](/icons/panorama.webp) Ambiente {#environment}
Cria uma luz de ambiente, que ilumina a cena a partir de uma imagem ao redor dela (iluminação baseada em imagem, como um HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Cria uma luz spot, com controles para a largura e a suavidade do cone

### ![](/icons/light.webp) Ponto {#point}
Cria uma luz pontual

## ![](/icons/cog.webp) Avançado {#advanced}
O botão `Avançado`, no canto inferior esquerdo do painel, abre uma janela com duas abas: `Geral` e `Sincronizar`.

### ![](/icons/focus.webp) UI: Focar no item ao tocar duas vezes {#focus-on-item}
Tocar duas vezes em um item da lista da cena centraliza a câmera nesse item na vista 3d.

### ![](/icons/eye_open.webp) Sincronizar visibilidade {#sync-visibility}
Quando ativado, usar o ícone de olho de um item selecionado afeta todos os itens selecionados.

### ![](/icons/bang.webp) Destaque {#highlight}
Realça os objetos selecionados na viewport quando a seleção muda.

### ![](/icons/link.webp) Mostrar (Instância) {#instance-show}
Mostra uma cápsula colorida à esquerda da lista da cena para indicar as instâncias.

### ![](/icons/preview.webp) Pré-visualizações de objetos {#object-previews}
Mostra uma miniatura renderizada de cada objeto na lista da cena. É o mesmo que o botão de pré-visualização acima da lista.

### Raio de soldagem {#weld-radius}
Sob o título `Unir`, `Raio de soldagem de posição` e `Raio de soldagem de UV`: os pontos e as UVs mais próximos do que esses raios são fundidos. Cada um pode ser desligado com sua caixa de seleção. Isso vale para Unir, Booleano, Aparar, Dizimar, as remalhagens e a importação de arquivos.

### Ícones {#icons}
Define o `Tamanho` mínimo e máximo e a `Opacidade` dos ícones de grupo, luz, câmera e repetidor na viewport.

### ![](/icons/hierarchy.webp) Linhas de hierarquia {#hierarchy-lines}
Mostra uma linha entre o pai e seus secundários na viewport. Quando ativado, você também pode definir:
* `Usar pivô do Nomad` - as linhas partem do pivô usado pelas ferramentas Transformar e Gizmo. Quando desativado, elas usam o pivô base natural, que pode ficar longe do centro do objeto.
* `Espessura` - a largura das linhas. O botão ao lado do controle adiciona um contorno a elas.
* A cor das linhas.

### ![](/icons/link.webp) Sincronizar {#sync}
A aba `Sincronizar` define, para cada operação (`Adicionar`, `Apagar`, `Bloquear`, `Clonar`, `Instância`, `Desinstanciar`, `Unir`, `Separar` e `Booleano`), se ela se aplica a todas as instâncias da seleção:
* `Auto` - segue a caixa `Sincronizar` no topo do menu Cena.
* `Não` - só os objetos selecionados.
* `Sim` - sempre todas as instâncias.

Por padrão, `Unir`, `Separar` e `Booleano` ficam em `Sim` e os outros em `Auto`. `Redefinir` restaura esses padrões.

## Barra de ferramentas inferior {#bottom-toolbar}
Estes ícones mostram ou escondem os grupos, luzes, câmeras, repetidores e linhas de hierarquia na viewport. Os ícones exibidos na tela podem ser tocados para selecioná-los e editá-los diretamente.

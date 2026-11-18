# ![](/icons/multires.webp) Topologia {#topology}

Este menu controla a topologia dos objetos no Nomad, e também reúne ferramentas para selar (bake) e transferir detalhes entre objetos e entre texturas.

![](/images/topology_overview.webp)

O Nomad trabalha com polígonos: ele usa triângulos e quads para representar a geometria.
Por topologia, entendemos tanto o número de faces quanto a maneira como os pontos (vértices) estão ligados.

É importante ficar de olho na topologia, principalmente se você quer esculpir ou pintar detalhes finos.

::: tip Como acompanhar a sua topologia?
Você pode mostrar a [Armação](settings.md#wireframe) ou simplesmente desativar o [Sombreamento suave](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

O menu Topologia do Nomad tem várias abas, em duas linhas:

| Método                                | Ícone                        | Descrição                                                        |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multirresolução](#multiresolution)   | ![](/icons/multires.webp)   | Edita vários níveis de detalhe usando subdivisão                 |
| [Remalhamento por voxels](#voxel-remesher) | ![](/icons/voxel.webp) | Recalcula uma nova topologia com densidade uniforme              |
| [Topologia dinâmica](#dynamic-topology) | ![](/icons/dynamic.webp)  | Adiciona/remove faces localmente em tempo real enquanto você esculpe ou pinta |
| [Diversos](#misc)                     | ![](/icons/topo_extra.webp) | Fecha furos, força o manifold e converte em triplano             |
| [Primitiva](#primitive)               | ![](/icons/dot.webp)        | Opções da primitiva                                              |
| [Dizimar](#decimation)                | ![](/icons/decimate.webp)      | Reduz o número de faces mantendo a forma                      |
| [Remalhar em quads](#quad-remesh)     | ![](/icons/quad.webp)       | Reconstrói o objeto com uma distribuição limpa de quads          |
| [Desdobramento UV](#uv-unwrap)        | ![](/icons/uv.webp)         | Cria UVs para texturização                                       |
| [Selar](#bake)                        | ![](/icons/bake.webp)       | Sela detalhes e pintura em texturas, vértices ou carimbos VDM    |


## Estatísticas de polígonos {#polygon-stats}

![](/images/topology_stats.webp)

A parte de cima de cada aba mostra a contagem de polígonos do objeto selecionado e, quando a cena tem mais de um objeto, a da cena inteira. As colunas são o número de vértices, de triângulos, de quads (polígonos de 4 lados) e de coordenadas UV (0 quando o objeto não tem UVs).

Toque nessa seção para listar todos os objetos da cena com as contagens exatas, incluindo o número de grupos de faces.

## ![](/icons/cog.webp) Menu de engrenagem {#gear-menu}
Algumas seções, como as das abas [Remalhar em quads](#quad-remesh) e [Selar](#bake), têm opções extras. Abra-as pelo ícone de engrenagem ao lado do título da seção.

## ![](/icons/multires.webp) Multirresolução {#multiresolution}

![](/images/topology_multires_menu.webp)

### O que é multirresolução? {#what-is-multiresolution}
A multirresolução é útil em dois casos principais:
- O algoritmo de subdivisão suave, para aumentar a contagem de polígonos do seu objeto
- Lidar com vários níveis de resolução, para alternar entre edições em pequena e em grande escala

![](/videos/multiresolution.mp4)

#### Fluxo de trabalho com multirresolução {#multiresolution-workflow}
Uma grande vantagem da multirresolução é que você pode voltar a uma resolução mais baixa, fazer alterações no objeto e depois voltar à resolução mais alta sem perder os detalhes de alta resolução. Todos os detalhes de alta resolução são projetados automaticamente.

As [camadas](layers.md#layers) estão disponíveis em todas as resoluções.

::: warning
Se você usar uma ferramenta que altera a topologia do objeto, vai perder todas as outras resoluções dele!
Você sempre deve receber um aviso quando isso estiver para acontecer, por exemplo ao usar:
- o [Remalhamento por voxels](#voxel-remesher)
- a [Topologia dinâmica](#dynamic-topology)
- a [ferramenta Aparar](tools.md#trim)
- a [ferramenta Dividir](tools.md#split)
:::


### Controle de multirresolução {#multiresolution-slider}
Este controle indica o número de níveis de subdivisão do objeto atual. Se houver 6 barras verticais, há 6 níveis de subdivisão. O círculo indica o nível de subdivisão exibido no momento.

Pequenos ícones acima do controle mostram quais opções (`Bloquear nível 0`, `Linear`, `Borda nítida`, `Manter triângulos`) foram usadas em cada nível.

### Inverter {#reverse}
No nível de subdivisão mais baixo, o botão Inverter tenta criar um nível abaixo do atual. Em geral, isso só é possível se o objeto foi criado por subdivisão desde o início, por exemplo no Nomad ou em outros aplicativos 3d com superfícies de subdivisão em multirresolução.

### Subdividir {#subdivide}
O botão *Subdividir* multiplica o número de polígonos por 4, então fique de olho na contagem de polígonos, porque ela pode subir muito rápido! O Nomad pede confirmação quando o resultado ficaria pesado demais.
Uma característica importante das *superfícies de subdivisão* é que elas convergem para uma *superfície suave*.
Para entender como funciona, experimente o botão *Subdividir* em um objeto com poucos polígonos.

Você pode desativar esse comportamento *suave* com a opção `Linear`.

### Apagar mais baixa {#delete-lower}
Se houver subdivisões abaixo do nível exibido, apaga essas subdivisões. Se fizer isso sem querer, você pode recriá-las com o botão Inverter.

### Apagar mais alta {#delete-higher}
Se houver subdivisões acima do nível exibido, apaga essas subdivisões.

### ![](/icons/lock.webp) Bloquear nível 0 {#lock-lv0}
Mantém a forma do nível de subdivisão mais baixo quando você esculpe nos níveis mais altos. A pintura continua descendo até o nível 0. Isso pode ser importante se o objeto foi gerado em outro aplicativo e a malha base precisa ficar intacta.

Esta opção só está disponível antes da primeira subdivisão. Quando ela está desativada, grandes alterações feitas nos níveis de subdivisão mais altos movem o nível 0.

### ![](/icons/linear.webp) Linear {#linear-subdivision}
Subdivide a malha sem aplicar nenhuma suavização.

### ![](/icons/group.webp) Borda nítida {#sharp-border}
Se o objeto tem grupos de faces, esta opção mantém nítidas as bordas entre os grupos de faces. Ela pode ser definida para cada nível de subdivisão (o controle de subdivisão mostra um pequeno ícone acima do nível para indicar isso).

### ![](/icons/triangle.webp) Manter triângulos {#keep-triangles}
A maioria dos sistemas de superfície de subdivisão tenta converter todos os polígonos em quads durante a subdivisão. Esta opção força a subdivisão a usar triângulos.

::: tip

A subdivisão suaviza todas as bordas nítidas por padrão. Para manter as bordas um pouco nítidas, experimente usar `Linear` ou `Borda nítida` nos 2 primeiros níveis de subdivisão e depois desativá-los nos níveis mais altos. Assim você obtém uma malha subdividida semi-nítida.

:::

### Mostrar nível mais alto {#show-highest-level}
Mostra o nível mais alto, com todos os detalhes, enquanto você esculpe um nível mais baixo. Prático para ver o resultado final enquanto faz grandes alterações.

### Armação: Apenas nível 0 {#wireframe-level-0-only}
Quando a [Armação](settings.md#wireframe) está ativada, mostra só a armação do nível mais baixo. A armação densa dos níveis altos pode esconder a forma.


## ![](/icons/voxel.webp) Remalhamento por voxels {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Com o `Remalhamento por voxels`, a malha inteira passa a ter uma resolução uniforme, ou seja, todos os polígonos ficam mais ou menos do mesmo tamanho. Isso é muito útil quando você não quer pensar na topologia e só quer esculpir livremente.

Um fluxo de escultura típico pode começar com o `Remalhamento por voxels` para esboçar uma forma bruta em baixa resolução.
Basta apertar o botão *Remalhar* de vez em quando, sempre que esticar demais a malha, para evitar distorções excessivas.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Como dito acima, o Nomad é um software de polígonos, mas o `Remalhamento por voxels` é uma exceção em que outra abordagem é usada (temporariamente) para refazer a malha.

Uma grande diferença é que a abordagem por voxels não aceita autointerseções, então elas são resolvidas.
Ela também não aceita malhas com furos.

Por furos, não queremos dizer o `genus hole` (o `furo` de um donut), mas sim malhas que não são `watertight`/`fechadas`.
Na prática, isso quer dizer que, antes de refazer a malha, todos os furos são preenchidos, de forma parecida com a [ferramenta Aparar](tools.md#trim) ou o [preenchimento de furos](#holes). A opção [Furos](#voxel-holes) abaixo escolhe como.
:::

### ![](/icons/voxel.webp) Remalhar {#voxel-remesh}
Executa o remalhamento por voxels. Pequenos ícones no botão lembram quais das opções abaixo estão ativadas.

### Resolução {#voxel-resolution}
O tamanho dos voxels usados no cálculo; valores mais altos dão mais detalhe. Enquanto você muda este parâmetro, um padrão xadrez aparece sobre a malha para mostrar uma prévia do resultado.

O conta-gotas pega a resolução da densidade da malha onde você toca. O botão de cubo ao lado troca o valor para um `Comprimento da borda` em unidades do mundo: o mesmo valor passa a dar o mesmo detalhe em qualquer objeto.

### Construir multirresolução {#build-multiresolution}
Cria níveis de multirresolução mais baixos para o remalhamento por voxels. Se você usar o padrão xadrez para escolher a resolução e definir Construir multirresolução em 2, o resultado final terá o detalhe correspondente ao controle de resolução e, na aba de multirresolução, estará no nível 2, ou seja, você terá malhas de resolução mais baixa nos níveis 1 e 0. É uma boa maneira de obter ao mesmo tempo uma malha limpa com polígonos regulares e uma malha de controle de resolução mais baixa.

Também é mais rápido e usa menos memória em resoluções altas. Mas com uma resolução baixa e muitos níveis, você perde detalhes.

::: tip Dica: Construir multirresolução e suavização estável

Às vezes esta opção cria "laços" na geometria que são difíceis de suavizar e formam pequenas espinhas. Se isso acontecer, ative `Suavização estável` nas opções da ferramenta Suavizar.

:::

### Engrossar partes finas {#thicken-thin-parts}
As partes mais finas que os voxels podem se romper ou sumir durante o remalhamento. Esta opção as engrossa para que sobrevivam; valores mais altos engrossam mais. Não está disponível com `Bordas nítidas` ou `Borda nítida`.

### Furos {#voxel-holes}
Como os furos são fechados antes do remalhamento:

* `Preencher` - Cada furo é fechado sozinho, a partir da borda dele.
* `Forma` - Os furos são fechados seguindo a superfície ao redor, e as peças abertas que se sobrepõem são unidas.

### ![](/icons/angle.webp) Bordas nítidas {#keep-sharp-edges}
Encaixa os novos pontos nas bordas nítidas da malha original. É útil principalmente para operações booleanas simples com primitivas, e pode causar distorções.

### ![](/icons/group.webp) Borda nítida {#voxel-sharp-border}
As novas faces seguem as bordas dos grupos de faces, e uma borda continua nítida onde a superfície forma um vinco ao longo dela.

### ![](/icons/group_separate.webp) Manter grupos separados {#keep-groups-separate}
Cada grupo de faces é remalhado sozinho: os grupos nunca se fundem, e cada um continua sendo uma peça fechada no seu próprio grupo. Neste modo, a multirresolução não é construída. Disponível quando o objeto tem vários grupos de faces.

## ![](/icons/dynamic.webp) Topologia dinâmica {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
A multirresolução e o remalhamento por voxels são métodos comuns na indústria para controlar a topologia, mas os dois exigem que você cuide para não esticar demais os polígonos nem apertá-los demais.

A topologia dinâmica é um método alternativo. Enquanto você esculpe, o Nomad adiciona e remove polígonos de forma adaptativa durante o traçado do pincel: esculpir pequenos detalhes adiciona muitos polígonos pequenos onde você precisa, e suavizar em outros lugares retira polígonos.

A topologia dinâmica usa triângulos em vez de quads. Isso pode parecer um pouco bagunçado, mas o melhor é quase nem olhar a armação: concentre-se em fazer uma escultura bonita sem se preocupar com a topologia, e depois use uma das outras ferramentas de remalhamento do Nomad para gerar uma malha limpa de quads.

Veja no vídeo abaixo como funciona.

![](/videos/dynamic.mp4)

### Ativada {#enabled}
Liga a topologia dinâmica. Um ícone TopoDin aparece abaixo dos controles de raio e intensidade do pincel para você ligar ou desligar a TopoDin por ferramenta. Ela pode ter um impacto perceptível no desempenho, e as camadas são atualizadas corretamente.

### Detalhe {#dyn-detail}
Controla a quantidade de detalhe; o comportamento muda conforme a escolha em "Detalhe baseado em...", veja abaixo. No modo `Tela`, o rótulo mostra o tamanho alvo dos triângulos em pixels. No modo `Constante`, um conta-gotas permite pegar o detalhe da densidade da malha onde você toca.

### Detalhe baseado em... {#detail-based-on}
| Método    | Descrição                                                       |
| :-------: | :-------------------------------------------------------------: |
| Tela      | O nível de detalhe depende do tamanho do objeto na tela. O controle de detalhe em 100% ou mais dá detalhe fino, com triângulos pequenos, e em 1% dá pouco detalhe, com triângulos grandes.  |
| Raio      | O raio da ferramenta define a quantidade de detalhe. Use um raio pequeno para detalhe fino e um raio grande para pouco detalhe. O controle de detalhe é um multiplicador dessa relação.                     |
| Constante | O controle de detalhe define a quantidade de detalhe, sem influência do tamanho na tela nem do tamanho da ferramenta. É o mesmo valor do controle [Detalhe](#all-detail) de `Remalhar`.             |

::: tip DICA: Modo Raio

Para entender melhor como o modo Raio funciona, comece a mexer no controle de detalhe com um dedo e, ao mesmo tempo, mude o raio da ferramenta com outro dedo. Você vai ver como os dois estão ligados.

:::

### Preferir... {#prefer}
| Método     | Descrição               |
| :--------: | :---------------------: |
| Velocidade | Favorece o desempenho   |
| Qualidade  | Favorece a qualidade    |

Quando você favorece a `Qualidade`, as 2 principais diferenças são:
- o refinamento é aplicado antes de esculpir, então você tem menos artefatos de interpolação ao pintar ou esculpir detalhes muito pequenos
- o refinamento continua até convergir para o nível de detalhe correto, em vez de agir de forma incremental.
 
Assim, mesmo se você esculpir detalhes muito pequenos ou fizer traçados rápidos, a topologia sempre é refinada como esperado

### ![](/icons/pressure.webp) Usar pressão no raio {#use-pressure-on-radius}
Só é relevante se `Raio` estiver ativado. Quando ativado, o nível de detalhe sempre acompanha o tamanho do pincel, mesmo quando o tamanho do pincel varia com a pressão da caneta.

### Usar decaimento do traçado {#use-stroke-falloff}

Inclui também a curva de decaimento e o alfa do pincel nos cálculos da topologia dinâmica.

### Método {#method}
Escolhe como a topologia dinâmica altera a malha, tanto enquanto você esculpe quanto quando você usa [Remalhar](#dyn-remesh):

| Método         | Descrição                                                             |
| :------------: | :-------------------------------------------------------------------: |
| Uniformização  | Pode adicionar e remover faces; é o modo usado no vídeo acima         |
| Subdivisão     | Só adiciona novas faces, não pode remover faces                       |
| Dizimação      | Só remove faces, não pode adicionar novas faces                       |

### ![](/icons/shield.webp) Proteger área com máscara {#protect-masked-area}
Faz as áreas com máscara protegerem a topologia contra alterações.

### ![](/icons/normal.webp) Extrapolação de vértice {#vertex-extrapolation}
Coloca os pontos em uma superfície suave que acompanha a curvatura ao redor, em vez de deixá-los achatados sobre as faces existentes.

### Detalhe {#all-detail}
A resolução usada na operação de remalhamento. Se a TopoDin estiver no modo `Constante`, é o mesmo valor do controle Detalhe no topo deste menu. O conta-gotas pega o detalhe da densidade da malha onde você toca.

### Remalhar {#dyn-remesh}
Executa um remalhamento global com o algoritmo da topologia dinâmica. Para um remalhamento completo, normalmente você deve usar o [Remalhamento por voxels](#voxel-remesher).

Mas uma vantagem em relação aos voxels é que a malha não precisa ser fechada, e a área com máscara fica protegida, então você controla melhor onde colocar mais ou menos densidade.



## ![](/icons/topo_extra.webp) Diversos {#misc}

![](/images/topology_misc_menu.webp)

Esta aba reúne ferramentas para limpar ou converter a malha: fechar os furos, forçá-la a ser manifold ou transformá-la em triplano.

### ![](/icons/hole.webp) Furos {#holes}
![](/images/topology_holes_menu.webp)
Na maioria das vezes, seu objeto provavelmente será fechado, ou seja, a malha não tem aberturas.

Se o seu objeto tiver furos, você pode preenchê-los.

![](/videos/hole_filling.mp4)

::: tip
Quando você usa o remalhamento por voxels, todos os furos são fechados automaticamente, seja em 1 ou em várias malhas.
:::

#### Fechar furos {#close-holes}
Executa o fechamento dos furos.

#### Opções {#holes-gear-menu}
Estas opções mudam a forma como os furos são preenchidos:

##### Grupo de faces {#fill-face-group}
Escolhe o grupo de faces das novas faces:

* `Misto` - Um furo cercado por um único grupo de faces reutiliza esse grupo; um furo que toca vários grupos recebe um novo.
* `Novo` - Os furos preenchidos recebem um novo grupo de faces.
* `Reutilizar` - Cada furo recebe o grupo de faces que mais o cerca.

##### Detalhe {#fill-detail}
A densidade de polígonos usada para preencher o furo. Enquanto você arrasta este controle, um padrão xadrez aparece no modelo, indicando o tamanho dos triângulos que serão usados. A caixa de seleção desativa isso e usa só os pontos existentes, o que normalmente cria triângulos longos e finos sobre o furo, difíceis de esculpir.

##### Ponte {#fill-non-manifold}
Preenche um furo e as ilhas dentro dele como uma única superfície, em vez de preencher cada borda separadamente. Um ângulo maior cria pontes em furos mais curvos. A caixa de seleção desativa a opção.

### ![](/icons/cog.webp) Forçar Manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Tenta limpar as arestas não-manifold. Pode ser útil para softwares externos que não aceitam arestas compartilhadas por mais de 2 faces.

#### Limpar {#clean}
Executa a limpeza.

#### Opções {#force-manifold-gear-menu}
Esta opção muda a forma como a malha é limpa:

##### Excluir pequenas faces {#delete-small-faces}
Um limite usado para remover e juntar polígonos pequenos. Ative-o pela caixa de seleção.


### ![](/icons/triplanar.webp) Triplano {#triplanar}
![](/images/topology_triplanar_menu.webp)
Converte a malha em uma primitiva [triplano](scene.md#triplanar).
Você provavelmente vai perder muitos detalhes no processo: as camadas, a pintura e a multirresolução também são perdidas.

#### Forçar cúbico {#force-cubic}
Faz o triplano ser um cubo. Caso contrário, o triplano se ajusta à caixa delimitadora mais próxima do seu objeto.

#### Converter {#convert}
Executa a conversão em triplano.

#### Resolução {#triplanar-resolution}
A resolução da grade do triplano; valores mais altos mantêm mais detalhe.

## ![](/icons/decimate.webp) Dizimar {#decimation}

![](/images/topology_decimation.webp)

Reduz o número de polígonos tentando manter o máximo de detalhes possível, usando triângulos.

Este recurso pode ser útil se você quiser exportar para impressão 3d.
Mas provavelmente não é uma boa ideia usá-lo se você pretende continuar esculpindo, porque ele pode gerar triângulos irregulares.

As áreas com máscara não são dizimadas.

![](/videos/decimate.mp4)

::: tip

Usar a [ferramenta Quad Remesher](tools.md#quad-remesher) em objetos com muitos polígonos pode levar muito tempo e dar resultados difíceis de controlar. Preparar a malha com [grupos de faces](tools.md#facegroup) e dizimação faz o Quad Remesher rodar muito mais rápido e dá muito mais controle sobre a topologia.

* Crie grupos de faces na malha para definir o fluxo de quads ideal.
* Relaxe os grupos de faces para obter bordas de grupo suaves.
* Dizime. Isso garante que não haja faces finas ou distorcidas nas bordas dos grupos de faces. Em `Manter bordas`, verifique se `Grupo de faces` está ativado. Assim as arestas dos triângulos seguem exatamente as bordas dos grupos de faces.
* Nas opções do Quad Remesher, deixe o relaxamento desativado (você já relaxou a malha) e você deve obter bons resultados.

:::

### Dizimar {#decimate}
Inicia a dizimação.

Os ícones ao lado do botão Dizimar mostram as opções abaixo e permitem ativá-las ou desativá-las. A porcentagem indica a intensidade da opção.

* ![](/icons/palette.webp)  `Manter pintura` - Coloca mais triângulos onde há detalhes de pintura.
* ![](/icons/triforce.webp) `Faces uniformes` - Prefere criar triângulos de tamanho parecido.
* ![](/icons/hole.webp)  `Furo` - A dizimação tenta manter intactas as bordas perto de geometria aberta e de furos.
* ![](/icons/group.webp) `Grupo de faces` - A dizimação tenta manter intactas as bordas dos grupos de faces.
* ![](/icons/uv.webp) `UV` - A dizimação tenta manter intactas as bordas das UVs.

### Triângulos alvo {#target-triangles}
Define a contagem alvo de triângulos. O valor padrão é 50%; o botão porcentagem/alvo alterna entre uma porcentagem e uma contagem exata de polígonos.

### Opções {#decimate-gear-menu}
Cada opção tem uma caixa de seleção para ligá-la e um valor para a intensidade dela:

#### ![](/icons/palette.webp) Manter pintura {#preserve-painting}
O valor define a precisão com que os detalhes de pintura são preservados. Valores mais altos preservam mais a pintura. Coloque 0 se a pintura não importa.

#### ![](/icons/triforce.webp) Faces uniformes {#uniform-faces}
Valores mais altos geram triângulos de tamanho parecido.

#### Manter bordas {#preserve-borders}
Impede que as bordas sejam dizimadas. É possível definir pesos para as bordas de `Furo`, `Grupo de faces` ou `UV` (`UV` exige um objeto com UVs).

## ![](/icons/quad.webp) Remalhar em quads {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Reconstrói o objeto com uma distribuição limpa de quads. Esta aba tem vários remalhadores, cada um com seu próprio botão `Remalhar`, controle `Quads alvo` e menu de engrenagem. Experimente todos no seu objeto, os resultados são bem diferentes!

### Quad Remesher {#quad-remesher}
O mesmo remalhador da ferramenta [Quad Remesher](tools.md#quad-remesher), desenvolvido pela [Exoside](https://exoside.com/). Ele só está disponível em algumas plataformas e precisa ser comprado: até lá, o botão `Remalhar` mostra um carrinho.

`Selecionar ferramenta` muda para a ferramenta Quad Remesher, para desenhar guias e pintar a densidade. O menu de engrenagem contém `Contagem adaptativa de quads`, `Tamanho adaptativo` (em 100% o tamanho dos quads acompanha a curvatura, em 0% os quads são uniformes), `Detectar bordas duras` e `Reprojetar vértice`.

::: tip
Onde está disponível, o Quad Remesher geralmente dá os melhores resultados e o maior controle.
:::

### AutoRemesher {#autoremesher}
Um remalhador de quads alternativo, com opções para adaptar o tamanho e a forma dos quads à superfície.

#### ![](/icons/cog.webp) Menu de engrenagem do AutoRemesher {#autoremesher-gear-menu}
O menu de engrenagem tem estas opções avançadas:

##### Escala das arestas {#edge-scaling}
Ajusta o tamanho dos quads; valores mais altos geram quads maiores.

##### Adaptatividade {#adaptivity}
Adapta a densidade de quads à curvatura. 0 gera quads uniformes, 1 gera quads menores nas áreas curvas.

##### Anisotropia {#anisotropy}
Estica os quads na direção mais plana da superfície. 0 gera quads quadrados, 1 gera quads alongados em tubos e cristas.

##### Aresta nítida {#sharp-edge}
As arestas dobradas mais do que este ângulo são preservadas como detalhes nítidos.

##### Suavizar normais {#smooth-normal}
0 mantém a superfície facetada durante o remalhamento. Valores mais altos suavizam a superfície levando em conta as normais dos vértices.

##### Preenchimento máximo de furos {#autoremesher-max-fill-hole}
Às vezes o algoritmo gera furos indesejados. Se um furo tiver menos vértices que este valor, ele é preenchido.

### Instant Mesh {#quad-remesh-instant}
Refaz a malha com o [algoritmo Instant Meshes, de Wenzel Jakob, Marco Tarini, Daniele Panozzo e Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Ele analisa o fluxo da malha e cria uma topologia limpa de quads.

#### Remalhar {#instant-remesh}
Inicia o remalhamento.

#### Quads alvo {#target-quads}
O número de quads que o remalhador tenta criar.

#### ![](/icons/cog.webp) Menu de engrenagem do Instant Mesh {#quad-remesh-instant-gear-menu}
O menu de engrenagem tem estas opções avançadas:

##### Ângulo de vinco {#crease-angle}
Um limite de ângulo para os cantos nítidos, que ajuda a guiar o remalhamento. Ative-o pela caixa de seleção.

##### Preenchimento máximo de furos {#max-fill-hole}
Às vezes o algoritmo gera furos indesejados. Se um furo tiver menos vértices que este valor, ele é preenchido.

### QuadriFlow {#quadriflow}
Refaz a malha com o algoritmo QuadriFlow, outra maneira de obter uma distribuição limpa de quads.

#### ![](/icons/cog.webp) Menu de engrenagem do QuadriFlow {#quadriflow-gear-menu}
O menu de engrenagem tem estas opções avançadas:

##### Manter bordas {#quadriflow-preserve-boundary}
Protege as bordas dos furos.

##### Manter arestas nítidas {#keep-sharp}
Alinha os quads com as arestas nítidas da superfície.

##### Fluxo de custo mínimo {#min-cost-flow}
Usa um solucionador de fluxo de custo mínimo para a distribuição dos quads. Mais lento, mas pode gerar uma topologia mais regular.

## ![](/icons/uv.webp) Desdobramento UV {#uv-unwrap}
Calcula as coordenadas de textura (UVs) do objeto selecionado. O Nomad tem dois métodos, `UVAtlas` e `BFF`, cada um com seu próprio botão `Desdobrar`.

![](/videos/unwrap.mp4)

::: tip UVs?
Uma analogia comum para as UVs é embrulhar um presente: qual a melhor maneira de cortar o papel de presente para cobrir um objeto inteiro, sem sobreposições?

As UVs são parecidas, mas em vez de cortar o papel, você corta o objeto. Imagine que o seu modelo é feito de plástico fino: como você o cortaria para desdobrá-lo e deixá-lo plano, pintá-lo nesse estado plano e depois montá-lo de novo?

Agora imagine que a superfície do seu modelo é feita de lycra elástica. Você poderia esticar o modelo até ficar plano, ou cortá-lo, ou uma combinação dos dois. Mas se você pintasse um xadrez no objeto achatado, o xadrez ficaria distorcido ao remontá-lo. Qual método é melhor: mais cortes com menos distorção, ou menos cortes com mais distorção?

As UVs são instruções que dizem ao software 3d como "cortar e esticar" o objeto ao aplicar as texturas. A ferramenta UV Atlas geralmente segue a abordagem "mais cortes, menos distorção".


:::

::: tip UVs, o Nomad e outros aplicativos

A maioria dos modelos texturizados que você encontra na internet usa UVs. O Nomad pode importá-los e exibi-los pelo painel [Material](material.md#textures).

Nos modelos feitos no Nomad, você pode pintar diretamente nos objetos sem UVs. Se precisar exportá-los para outros aplicativos, como o [Procreate](https://procreate.art/), você pode "selar" a informação de cor do Nomad em texturas por meio das UVs.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
O UVAtlas geralmente prefere criar mais ilhas com cortes, para minimizar a distorção.

#### Desdobrar {#unwrap}
Calcula as UVs do objeto selecionado.

#### Opções {#uvatlas-gear-menu}
Os botões ao lado de `Desdobrar`:

##### Grupo de faces {#atlas-face-group}
Quando mostra `Sim`, os grupos de faces definem os cortes das UVs. Esta configuração é compartilhada com o BFF.

##### Apagar UVs {#delete-uvs}
O botão de lixeira apaga as UVs do objeto.

##### Inspecionar {#uv-inspect}
Mostra as UVs do objeto no fundo.

#### Alongamento máximo {#max-stretch}
Valores baixos criam menos distorção e mais ilhas; valores altos criam mais distorção e menos ilhas.

#### Espaçamento entre ilhas {#island-spacing}
A margem entre as ilhas. Valores baixos desperdiçam menos espaço, mas arriscam que as texturas vazem de uma ilha para outra.

::: warning
Calcular as UVs pode demorar; o ideal é ter uma malha com menos de 100k vértices.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

As UVs do BFF seguem a abordagem "menos cortes, mais distorção".

#### Opções {#uv-bff-gear-menu}
Os mesmos botões `Grupo de faces`, apagar e `Inspecionar` do [UVAtlas](#uvatlas-gear-menu) ficam ao lado de `Desdobrar`.

##### Grupo de faces {#bff-face-group}

Usa os grupos de faces para definir os cortes das UVs.

#### Contagem de cones {#cone-count}
Define o número de projeções principais usadas. Valores mais baixos geram menos ilhas, mas mais distorção. Valores mais altos demoram mais para calcular.

#### Remendos sem costura {#seamless-patches}
Afeta a disposição dos remendos de UV e pode causar bastante distorção. Funciona melhor com grupos de faces criados com cuidado.

::: warning
O BFF pode criar UVs sobrepostas se a malha tiver alças (como o furo de um donut).
:::

### ![](/icons/preview.webp) Mostrar UV após o desdobramento {#show-uv-after-unwrap}
Abre o inspetor de UV depois do desdobramento, para você conferir o resultado na hora.

### ![](/icons/bake.webp) Selar: Textura → Textura {#unwrap-bake-texture}
Só está disponível quando o material do objeto tem texturas. Quando você desdobra o objeto de novo, as texturas são transferidas para as novas UVs, para continuarem encaixando. A resolução é `Auto` por padrão, igual à da maior textura, ou você pode defini-la.

## ![](/icons/bake.webp) Selar {#bake}
Esta aba transfere detalhes e pintura entre objetos, e entre vértices e texturas.

`De alta resolução` usa outros objetos como fonte; o número entre parênteses indica quantos. O Nomad os escolhe assim:

- todos os objetos selecionados são usados, e o objeto selecionado principal é o alvo (o mais destacado no menu [Cena](scene.md))
- se só um objeto estiver selecionado, o Nomad usa todos os objetos visíveis
- se todos os outros objetos estiverem ocultos (por exemplo com Solo), a cena inteira é usada

### ![](/icons/bake.webp) Selar → Textura {#bake-texture}
![](/images/topology_bake_menu.webp)

A selagem de texturas cria texturas projetando os outros objetos visíveis da cena nas UVs do objeto selecionado. O objeto precisa ter UVs.

Este é o fluxo de trabalho típico para selar:
- Você tem uma malha com detalhes finos e pintura
- Clone-a
- Dizime-a (coloque `Manter pintura` em 0)
- Desdobre as UVs dela
- Sele!

Agora você deve ter uma malha de baixa resolução que mantém a maior parte da pintura e dos detalhes do objeto anterior.

Depois da operação, as cores de vértice são movidas para uma nova camada desativada, para não interferirem nas texturas.

#### De si mesmo {#tex-from-itself}
Sela o objeto nas próprias UVs: a pintura dele vira textura e, se ele tiver níveis de multirresolução, os detalhes do nível mais alto são selados no nível atual (nesse caso, um ícone de multirresolução aparece no botão). É simples de configurar, mas muitas vezes você vai precisar de mais controle, e aí a próxima opção é mais útil.

#### De alta resolução {#tex-from-high-res}
Sela os outros objetos no objeto selecionado. O número entre parênteses indica quantos outros objetos serão usados como fontes de alta resolução e selados no objeto atual de baixa resolução com UVs. Os outros objetos não precisam ter disposição ou topologia parecida com a do objeto selado, o que permite fluxos de selagem bem versáteis.

#### Resolução {#tex-bake-resolution}
A resolução da textura selada. As texturas seladas são sempre quadradas, então 1024 cria uma imagem de 1024x1024.

Os botões abaixo são atalhos para as resoluções mais usadas. Como referência, 512x512 é relativamente pequeno, para gráficos da web e geometria simples. 4096x4096 (4k, para encurtar) é para renderizações de alta qualidade.

#### Cor, Aspereza, Metalidade, Normal, Deslocamento, Emissiva, Opacidade {#tex-normal-roughness-metalness-color-emissive-opacity}
Estes botões definem quais propriedades serão seladas, cada uma em um mapa separado. Quando a selagem termina, elas são adicionadas como texturas ao material do objeto atual. `Deslocamento` sela a altura dos detalhes como um mapa de deslocamento.

#### ![](/icons/cog.webp) Menu de engrenagem de Selar {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
O menu de engrenagem tem estas opções avançadas:

##### Backup {#tex-backup}
Para pré-visualizar as texturas seladas, a pintura do objeto deve estar desativada. `Backup (Pintura → Camada)` transfere toda a pintura para uma nova camada como backup, para que ela possa ser facilmente ativada/desativada.

##### Usar multirresolução {#tex-use-multires}
Para `De si mesmo` em um objeto com níveis de multirresolução. O Nomad lê a alta resolução pelos níveis de subdivisão em vez de lançar raios: é mais rápido e sem erros de projeção. Desative para selar com as opções abaixo.

##### Base suave {#tex-smooth-base}
Para `Deslocamento` em um objeto com níveis de multirresolução. Mede o deslocamento a partir da base subdividida em vez das faces planas dela. Deixe ativado quando o mapa de deslocamento for usado em uma malha subdividida, como a subdivisão adaptativa do Blender.

##### Distância de pesquisa {#tex-cage-radius}
A distância máxima usada para encontrar a superfície de origem. Por padrão, essa distância é pequena para evitar artefatos, mas pode ser aumentada se os objetos de origem estiverem longe do objeto selado.

##### Projeção {#tex-projection}
Como a superfície de origem é encontrada:

* `Raio` - Projeta ao longo da normal da superfície.
* `Raio + mais próximo` - Usa o raio da normal e, se ele não acertar nada, usa a superfície mais próxima.
* `Mais próximo` - Projeta no ponto mais próximo da superfície de origem.

##### Offset de raio {#tex-ray-offset}
Ajusta de onde os cálculos de selagem partem no objeto selado. Um pequeno afastamento da superfície evita a maioria dos artefatos comuns. Se os objetos de origem estiverem muito longe do objeto selado, talvez seja preciso aumentar esse valor. Não é usado por `Mais próximo`.


### ![](/icons/bake.webp) Reprojetar → Vértice {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Projeta detalhes esculpidos, pintura, camadas e texturas em valores de vértice.

Dá para pensar nisso como o inverso da selagem: se a selagem transfere as propriedades dos vértices para texturas, a reprojeção transfere as texturas (e outras propriedades)
 de volta para os vértices.

::: tip
Ao usar `Selar → Textura` ou `Reprojetar → Vértice`, tanto as cores de vértice quanto as texturas do material são levadas em conta.
:::

#### De si mesmo {#vertex-from-itself}
Converte as texturas do material em valores de vértice. Este botão só fica ativo se o objeto tiver UVs e o material tiver texturas ativas.

::: tip DICA: Pintura de texturas
O Nomad não permite pintar e editar texturas diretamente, mas dá para chegar a resultados bem parecidos projetando as texturas -> valores de vértice, pintando nos vértices e depois selando vértices -> texturas:

1. Prepare um objeto com poucos polígonos e com UVs
1. Carregue as texturas no material dele
1. Subdivida o suficiente para pintar
1. `Reprojetar → Vértice` no modo `De si mesmo`: agora a textura foi convertida em valores de vértice
1. Pinte, suavize, borre, carimbe, faça todas as edições que precisar
1. `Selar → Textura`, no modo `De si mesmo`. Essas edições são convertidas de volta em texturas.
:::

#### De alta resolução {#vertex-from-high-res}
Converte os outros objetos em valores de vértice no objeto selecionado. O número neste botão indica o número de objetos de origem. Isto é pensado principalmente para ser usado também em uma malha de alta resolução, normalmente com uma topologia limpa.

::: tip
Reprojetar outros objetos serve não só para transferir a informação de cor de outros objetos, mas também para projetar os vértices sobre outros objetos: por exemplo, ataduras podem ser projetadas sobre um personagem.
:::

#### Vértices, Cor, Aspereza, Metalidade, Opacidade, Máscara, Camadas, Grupo de faces {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Estes botões definem quais propriedades serão projetadas no objeto selecionado. `Camadas` transfere as outras camadas para a malha selecionada.

#### ![](/icons/cog.webp) Menu de engrenagem de Reprojetar {#vertex-reproject-gear-menu}
O menu de engrenagem tem estas opções avançadas:

##### Opacidade → Máscara {#vertex-opacity-to-mask}
Transforma a opacidade da origem em máscara no objeto selecionado.

##### Iterações {#vertex-iterations}
Quantas vezes a operação de relaxamento é aplicada durante a reprojeção. Só é usado quando `Vértices` está ativado.

##### Relaxar {#vertex-relax}
A disposição da malha selecionada pode ser suavizada ou relaxada um pouco para se encaixar melhor nos objetos de origem. `Suavizar` é melhor para malhas com muitos polígonos, `Relaxar` para malhas com poucos polígonos. `Auto` deixa o Nomad escolher o melhor método.

##### Distância de pesquisa {#vertex-cage-radius}
A distância máxima usada para encontrar a superfície de origem. Por padrão, essa distância é pequena para evitar artefatos, mas pode ser aumentada se os objetos de origem estiverem longe do objeto selecionado.

##### Projeção {#vertex-projection}
Como a superfície de origem é encontrada:

* `Raio` - Projeta ao longo da normal da superfície.
* `Mistura adaptativa` - Mistura o raio da normal e a superfície mais próxima conforme a distância e a `Preferência do raio`. Se um deles não acertar nada, usa o outro.
* `Mais próximo` - Projeta no ponto mais próximo da superfície de origem.

##### Preferência do raio {#vertex-ray-bias}
Só para `Mistura adaptativa`. Valores mais altos puxam a mistura para o resultado do raio da normal, valores mais baixos para o ponto mais próximo.

##### Offset de raio {#ray-vertex-offset}
Ajusta de onde os cálculos partem no objeto selecionado. Um pequeno afastamento da superfície evita certos artefatos. Se os objetos de origem estiverem muito longe do objeto selado, talvez seja preciso aumentar esse valor. Não é usado por `Mais próximo`.

### ![](/icons/bake.webp) Selar → VDM {#bake-vdm}
Cria um carimbo VDM (deslocamento vetorial) a partir do objeto selecionado e o adiciona à biblioteca de VDM. O Nomad pede um nome.

Este é o fluxo de trabalho típico:
- Adicione um plano, ou escolha `Novo VDM` no seletor de VDM para adicionar um já configurado (a primitiva [VDM](scene.md#add-menu))
- Esculpa sua forma nele, mantendo a borda plana
- Sele!

As UVs do plano definem o quadrado que é selado, então o objeto precisa ter UVs. Escolha o tamanho do carimbo com `Resolução`, e escolha com `Cor`, `Aspereza`, `Metalidade` e `Opacidade` o que o carimbo leva além do deslocamento.

::: tip
Evite a TopoDin no plano: ela degrada as UVs e o carimbo sai distorcido. Esculpir em uma camada dá o resultado mais preciso, já que o plano liso continua lá embaixo. A pintura também precisa de uma camada; caso contrário, o material é carimbado no quadrado inteiro em vez de só onde você pintou.
:::

## ![](/icons/dot.webp) Primitiva {#primitive}
Os parâmetros da primitiva selecionada. A maioria também está disponível pelo botão `…` da barra de ferramentas da primitiva na viewport.

![](/images/topology_primitive_screenshot.webp)

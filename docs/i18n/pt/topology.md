# ![](/icons/multires.webp) Topologia 

Este menu controla a topologia dos objetos no Nomad, bem como ferramentas para assar (bake) e transferir detalhes entre objetos e entre texturas.

![](/images/topology_overview.webp)

Nomad é baseado em polígonos, usando triângulos e quads para lidar com a geometria.
Por topologia, nos referimos tanto ao número de faces quanto à forma como os pontos (vértices) são conectados.

É importante acompanhar a topologia, especialmente se você quiser esculpir ou pintar detalhes finos.

::: tip Como acompanhar sua topologia?
Você pode exibir o [Wireframe](settings.md#wireframe) ou simplesmente desativar o [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

O menu de topologia do Nomad possui várias seções:

| Método                                | Ícone                         | Descrição                                                        |
| :-----------------------------------: | :---------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Editar múltiplos níveis de detalhe usando subdivisão             |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Recalcular uma nova topologia com densidade uniforme             |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Adicionar/Remover faces localmente em tempo real ao esculpir ou pintar |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimação, UVs, baking, remeshing, reprojeção                    |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Opções de primitivas                                             |


## Estatísticas de polígonos

![](/images/topology_stats.webp)

A seção superior do menu de topologia exibe informações de polígonos para o objeto selecionado e para a cena inteira. Os números mostram o total de vértices, o total de triângulos e o total de quads (polígonos de 4 lados).

Tocar nesta seção exibirá uma lista de estatísticas de polígonos para todos os objetos poligonais na cena.

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### O que é multiresolution?
O recurso de multiresolução é útil em dois cenários principais:
- O algoritmo de subdivisão suave para aumentar o número de polígonos do seu objeto
- Lidar com múltiplos níveis de resolução para que você possa alternar entre edições em pequena e grande escala

![](/videos/multiresolution.mp4)

#### Fluxo de trabalho de multiresolution
Um aspecto importante da multiresolução é que você pode voltar para uma resolução mais baixa, fazer alterações no seu objeto e então voltar para a resolução mais alta sem perder os detalhes de alta resolução. Todos os detalhes de alta resolução serão projetados automaticamente.

::: warning
Se você estiver usando uma ferramenta que altera a topologia do seu objeto, você perderá todos os outros níveis de resolução do seu objeto!
Você sempre deverá receber um aviso caso isso vá acontecer, por exemplo quando estiver usando:
- o [Voxel Remesher](#voxel-remesher)
- o [Dynamic Topology](#dynamic-topology)
- a [ferramenta Trim](tools.md#trim)
- a [ferramenta Split](tools.md#split)
:::


### Controle deslizante de Multiresolution
Este controle indica o número de níveis de subdivisão no objeto atual. Se houver 6 barras verticais, existem 6 níveis de subdivisão. O círculo indica o nível de subdivisão atualmente exibido. 

### Reverse
Quando estiver no nível de subdivisão mais baixo, o botão Reverse tentará criar um nível abaixo do atual. Note que isso geralmente só é possível se o objeto tiver sido criado com subdivisão desde o início, por exemplo no Nomad ou em outros aplicativos 3D que usam superfícies de subdivisão com multiresolução.

### Subdivide
O botão *Subdivide* aumentará o número de polígonos em 4 vezes, então fique de olho no número de polígonos, pois ele pode aumentar muito rapidamente!
Um aspecto importante da *Subdivision Surface* é que ela converge para uma *Superfície Suave*.
Para entender como funciona, você pode testar o botão *Subdivide* em um objeto com apenas alguns polígonos.

Você pode desativar esse comportamento *Smooth* marcando a opção `Linear subdivision`.

### Delete lower
Se houver subdivisões abaixo do nível atualmente exibido, elas serão apagadas. Se você fizer isso por engano, poderá recriá-las com o botão Reverse.

### Delete higher
Se houver subdivisões acima do nível atualmente exibido, elas serão apagadas.

### Linear subdivision
Subdivide a malha sem aplicar suavização.

### Sharp border
Se o seu objeto tiver facegroups, ativar esta opção manterá as bordas dos facegroups afiadas. Isso pode ser definido em cada nível de subdivisão (o controle deslizante de subdivisão terá um pequeno ícone acima do nível para indicar isso).

### Keep triangles
A maioria dos sistemas padrão de superfícies de subdivisão tentará converter todos os polígonos em quads durante uma operação de subdivisão. Esta opção força a subdivisão a usar triângulos em vez disso.

### Lock (LV0)

Impede que o nível de subdivisão mais baixo seja modificado. Isso pode ser importante se o seu objeto foi gerado em outro aplicativo e a malha base precisa permanecer inalterada. Quando esta opção está desativada, grandes alterações feitas em níveis de subdivisão mais altos moverão o nível 0.

::: tip 

A subdivisão suavizará todas as bordas afiadas por padrão. Para manter as bordas levemente afiadas, experimente usar subdivisão linear ou Sharp border nos 2 primeiros níveis de subdivisão e depois desativá-las nos níveis mais altos. Isso criará uma malha subdividida semi-afiada.

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
Ao usar o `Voxel Remesher`, toda a malha terá sua topologia forçada a ter uma resolução uniforme, o que significa que todos os polígonos terão mais ou menos o mesmo tamanho. Isso é muito útil quando você não quer pensar em topologia e simplesmente fazer escultura livre.

Um fluxo de trabalho típico de escultura pode começar usando o `Voxel Remesher` para bloquear uma forma grosseira com baixa resolução.
Basta pressionar o botão *Remesh* de vez em quando quando você estiver esticando demais a malha para evitar muita distorção.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Como dito acima, o Nomad é um software poligonal, mas o `Voxel Remesher` é uma exceção em que outra abordagem é usada (temporariamente) para realizar o remeshing.

Uma grande diferença é que a abordagem de voxel não aceita auto-interseção, então estas serão resolvidas.
Além disso, ela não suporta malhas com buracos.

Por buracos, não queremos dizer o `genus hole` (`buraco` de um donut), mas sim malhas que não são `watertight`/`closed`.
Tipicamente, isso significa que antes de aplicar o remeshing, todos os buracos serão preenchidos, de forma semelhante à [ferramenta Trim](tools.md#trim) ou ao [recurso de preenchimento de buracos](scene.md#hole-filling).
:::

### Remesh
Executa o voxel remesh.

### Resolution
O tamanho dos voxels usados durante o cálculo. Ao alterar este parâmetro, um padrão quadriculado será sobreposto na malha para dar uma prévia do resultado.

### Build multiresolution
Cria níveis inferiores de multiresolução para o voxel remesh. Se você usar o padrão quadriculado para definir uma resolução e definir build multiresolution para 2, o resultado final terá detalhes que correspondem ao controle de resolução e, se você for para a aba de multires, estará no nível 2, o que significa que você terá malhas de multires em resolução mais baixa nos níveis 1 e 0. Isso pode ser uma boa forma de gerar uma malha limpa com polígonos uniformes e ter uma malha de controle em baixa resolução.

::: tip Dica: Build multiresolution e stable smoothing

Esta opção às vezes pode causar “loops” na geometria que podem ser difíceis de suavizar, causando pequenas saliências. Se isso acontecer, ative o 'Stable smoothing' nas opções da ferramenta de suavização. 

:::

### Keep sharp edges
Ativa o encaixe dos novos pontos às bordas afiadas da malha original. Isso pode introduzir distorção.

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
Multiresolution e voxel remeshing são métodos comuns na indústria para controlar topologia, mas ambos exigem que você tome cuidado para não esticar demais os polígonos ou comprimi-los demais. 

Dynamic Topology é um método alternativo. Enquanto você esculpe, o Nomad adiciona e remove polígonos de forma adaptativa durante o traço do pincel, então esculpir pequenos detalhes adicionará muitos polígonos pequenos onde você precisa deles, e suavizar em outras áreas removerá polígonos.

Note que o dynamic topology usará polígonos triangulares em vez de quads. Isso pode parecer um pouco bagunçado, mas é quase melhor não olhar para o wireframe, apenas se concentrar em fazer uma escultura bonita sem se preocupar com topologia, e depois usar uma das outras ferramentas de remeshing do Nomad para gerar uma malha quad limpa.

Veja o vídeo abaixo em ação.

![](/videos/dynamic.mp4)

### Enabled
Ativa o dynamic topology. Um ícone DynTopo será colocado abaixo dos controles de raio e intensidade do pincel para permitir que você ative/desative o Dyntopo por ferramenta.

### Detail
Controla a quantidade de detalhe; seu comportamento muda com base na seleção de 'Detail based on...', veja abaixo.

### Detail based on...
| Método  | Descrição                                                                                                                                                |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Screen  | O nível de detalhe dependerá do tamanho do objeto na tela. O controle de detalhe é 100% ou mais para detalhes finos, criando triângulos pequenos, ou 1% para baixo detalhe, criando triângulos grandes. |
| Radius  | O raio da ferramenta define a quantidade de detalhe. Use um raio pequeno para detalhes finos, um raio grande para baixo detalhe. O controle de detalhe é um multiplicador nessa relação.              |
| Constant| O controle de detalhe define a quantidade de detalhe e não é afetado pelo tamanho da tela ou da ferramenta.                                             |

::: tip DICA: modo Radius

Para entender melhor como o modo Radius funciona, comece a mover o controle de detalhe com um dedo e, ao mesmo tempo, altere o raio da ferramenta com outro dedo. Você verá como eles estão ligados.

:::

### Prefer...
| Método | Descrição          |
| :----: | :----------------: |
| Speed  | Favorecer desempenho |
| Quality| Favorecer qualidade |

Quando você favorece `Quality`, as 2 principais diferenças são:
- o refinamento é aplicado antes da escultura, então você terá menos artefatos de interpolação ao pintar ou esculpir detalhes muito pequenos
- o refinamento é executado até convergir para o nível de detalhe correto, em contraste com um comportamento incremental.
 
Dessa forma, se você esculpir detalhes muito pequenos ou fizer traços rápidos, a topologia sempre será refinada como esperado


### Use pressure on radius
Relevante apenas se `Radius` estiver ativado. Quando habilitado, o nível de detalhe sempre refletirá o tamanho do pincel, mesmo quando o tamanho do pincel for afetado pela pressão da caneta.

### Use stroke falloff

Também inclui a curva de falloff do pincel e o alfa nos cálculos do dyntopo.

### Method
Esteja você usando `Dynamic Topology` no seu [Brush](#brush) ou [Globalmente](#global), você pode escolher em qual modo ele opera:

| Método         | Descrição                                                                 |
| :------------: | :-----------------------------------------------------------------------: |
| Uniformisation | Pode adicionar e remover faces; este é o modo usado no vídeo acima       |
| Subdivision    | Adiciona apenas novas faces, não pode remover faces                      |
| Decimation     | Remove apenas faces, não pode adicionar faces                            |

### Protect masked area
Ativa a proteção das áreas mascaradas contra alterações na topologia.

### Vertex extrapolation


### Detail
A resolução usada para a operação de remesh. Se o Dyntopo estiver no modo 'Constant', será o mesmo valor do controle de Detail no topo deste menu.

### Remesh
Executa um remesh global usando o algoritmo do dyntopo. Normalmente você deve usar o [Voxel Remesher](#voxel-remesher) para remeshing completo.

No entanto, uma vantagem em relação aos voxels é que a área mascarada será protegida, então você pode ter um controle melhor sobre onde colocar mais ou menos densidade.



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu de engrenagem
Muitas das ferramentas neste menu possuem opções extras. Elas podem ser acessadas através do ícone de engrenagem ao lado do título da seção.

### Decimation

![](/images/topology_decimation.webp)

Reduz o número de polígonos tentando manter o máximo possível de detalhes, usando polígonos triangulares.

Este recurso pode ser útil se você quiser exportar para impressão 3D.
No entanto, provavelmente você não deve usá-lo se quiser continuar esculpindo, pois ele pode produzir triângulos irregulares.

Note que as áreas mascaradas não serão decimadas.

![](/videos/decimate.mp4)

::: tip

Usar a [ferramenta Quadremesh](tools.md#quad-remesher) em objetos de alta contagem de polígonos pode levar muito tempo para calcular e gerar resultados difíceis de controlar. Pré-processar a malha com [facegroups](tools.md#facegroup-1) e decimate fará o Quadremesh rodar muito mais rápido e permitirá muito mais controle sobre a topologia.

* Crie facegroups na malha para definir o fluxo ideal de quads.
* Use Facegroup relax para suavizar as bordas dos facegroups.
* Faça Decimate. Isso garantirá que você não tenha faces finas ou distorcidas na borda dos facegroups. Nas configurações de decimate, certifique-se de que facegroup esteja ativado. Isso fará com que as arestas dos triângulos sigam precisamente as bordas dos facegroups.
* Nas opções do Quadremesh, certifique-se de que relax esteja desativado (já que você já relaxou a malha) e você deverá obter bons resultados.

:::

#### Decimate
Inicia a operação de decimação.

Os ícones ao lado do botão decimate permitem ativar/desativar opções que afetam a decimação. A porcentagem indica quão forte é essa opção e pode ser definida no menu avançado de engrenagem.

* ![](/icons/palette.webp)  `Preserve Painting` - Coloca mais triângulos onde há detalhes de pintura.
* ![](/icons/triforce.webp) `Uniform Faces` - Prefere criar triângulos de tamanho uniforme.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate tentará manter inalteradas as bordas próximas à geometria aberta e aos buracos.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate tentará manter inalteradas as bordas dos facegroups.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate tentará manter inalteradas as bordas de UV.

#### ![](/icons/cog.webp) Menu de engrenagem do Decimate
O menu de engrenagem possui estas opções avançadas:
##### Preserve painting
A caixa de seleção ativa/desativa este modo; o valor determina quão precisamente os detalhes de pintura serão preservados. Valores mais altos preservam mais pintura. Defina como 0 se você não se importar com a pintura.


##### Uniform faces
A caixa de seleção ativa/desativa este modo. Valores mais altos produzem triângulos com tamanho semelhante.

##### Preserve borders
Ative para impedir que bordas sejam decimadas. Pesos de borda podem ser selecionados para bordas de `Geometry`, `Face Group` ou `UV`.

#### Target triangles
Define a contagem alvo de triângulos. O valor padrão é 50%; o botão percent/target alterna entre uma porcentagem ou uma contagem exata de polígonos alvo.



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
Calcula coordenadas de textura (UVs) para a malha atual, geralmente preferindo criar mais ilhas com cortes para minimizar a distorção.

O pequeno ícone de olho entre o título do menu e o menu de engrenagem alterna a visualização das UVs no objeto.

![](/videos/unwrap.mp4)

#### Unwrap
Calcula UVs para o objeto selecionado, que serão exibidas ao fundo.

#### Delete UVs
Apaga as UVs do objeto.

#### ![](/icons/cog.webp) Menu de engrenagem do UVAtlas
O menu de engrenagem possui estas opções avançadas:

#### Face Group

Usa facegroups para definir os cortes das UVs.

##### Max Stretch
Valores baixos criam menos distorção e mais ilhas; valores altos criam mais distorção e menos ilhas. 

##### Island spacing
A quantidade de espaçamento entre as ilhas. Valores baixos desperdiçam menos espaço, mas aumentam o risco de vazamento de textura entre as ilhas. 

::: warning
Calcular UVs pode levar algum tempo; é melhor ter uma malha com menos de 100k vértices.
:::

::: tip UVs?
Uma analogia comum para UVs é embrulhar um presente: qual é a melhor forma de cortar o papel de presente para cobrir completamente um objeto, sem sobreposições? 

As UVs são semelhantes, mas em vez de cortar o papel, você corta o objeto. Imagine que seu modelo é feito de plástico fino: como você o cortaria para desdobrá-lo e deixá-lo plano, pintar nele nesse estado plano e depois remontá-lo?

Agora imagine que a superfície do seu modelo é feita de lycra elástica. Você poderia esticar o modelo até ficar plano, ou cortá-lo, ou uma combinação de ambos. Mas se você pintasse um padrão quadriculado no objeto quando ele estivesse achatado, o quadriculado ficaria distorcido quando você o remontasse. Qual é o melhor método: mais cortes com menos distorção ou menos cortes com mais distorção?

As UVs são instruções para dizer ao software 3D como “cortar e esticar” o objeto ao aplicar texturas. A ferramenta UV Atlas geralmente usa uma abordagem de “mais cortes, menos distorção”.


:::

::: tip UVs, Nomad e outros aplicativos

A maioria dos modelos texturizados que você encontra online terá texturas baseadas em UVs. O Nomad pode importar e exibir isso via o painel de [material](material#textures).

Quando os modelos são feitos no Nomad, você pode pintar diretamente nos objetos sem UVs. Se você precisar exportá-los para outros aplicativos, por exemplo o [Procreate](https://procreate.art/), você pode “assar” as informações de cor do Nomad em texturas via UVs. 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

As UVs BFF favorecem uma abordagem de “menos cortes, mais distorção”. 

#### ![](/icons/cog.webp) Menu de engrenagem do UV BFF

#### Face Group

Usa facegroups para definir os cortes das UVs.

##### Cone count
Define o número de projeções principais usadas. Valores mais baixos produzem menos ilhas, mas mais distorção.

##### Seamless patches
Afeta o layout dos patches de UV, funcionando melhor com facegroups cuidadosamente criados.

### Bake -> texture 
![](/images/topology_bake_menu.webp)

O baking de textura criará texturas projetando outros objetos visíveis na cena nas UVs do objeto selecionado.

Aqui está o fluxo de trabalho típico para baking:
- Você tem uma malha com detalhes finos e pintura
- Clone-a
- Faça Decimate (defina `Preserve painting` para 0)
- Faça UV unwrap
- Faça o Bake!

Por padrão, o Nomad levará em conta todas as malhas visíveis na cena.
Você também pode usar o modo Solo para ocultar rapidamente a maioria das outras malhas.
Se não houver outros objetos visíveis, então ele levará em conta a cena inteira.

Você deverá ter agora uma malha de baixa resolução que mantém a maior parte da pintura e dos detalhes do seu objeto anterior.

Após a operação, as cores de vértice serão movidas para uma nova camada desativada, para que não interfiram com as texturas.

#### From itself
Assa o nível de multiresolução mais alto para o nível mais baixo no objeto atual. Isso é simples de configurar, mas muitas vezes você precisará de mais controle; nesse caso, a próxima opção é mais útil.

#### From high-res ()
Assa a partir de outros objetos visíveis na cena para o objeto selecionado. O número entre parênteses indica o número de outros objetos visíveis que serão usados como alvos de alta resolução e assados no objeto atual de baixa resolução com UVs. Os outros objetos não precisam ser semelhantes em layout ou topologia ao objeto que está sendo assado, permitindo fluxos de trabalho de bake versáteis.

#### Resolution
A resolução da textura assada. As texturas de bake são sempre quadradas, então 1024 criará uma imagem de 1024x1024. 

Os botões abaixo são atalhos para resoluções comumente usadas. Para referência, 512x512 é relativamente pequeno, por exemplo para gráficos web e geometria simples. 4096x4096 (4k) é para renders de alta qualidade.

#### ![](/icons/cog.webp) Menu de engrenagem do Bake
![](/images/topology_bake_gear_menu.webp)
O menu de engrenagem possui estas opções avançadas:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
Essas caixas de seleção determinam quais propriedades serão assadas, cada uma em mapas separados. Após o término do bake, elas serão adicionadas como texturas ao material do objeto atual.

##### Backup
Para visualizar as texturas assadas, as informações de pintura do objeto devem ser desativadas. Esta opção transferirá qualquer informação de pintura para uma nova camada como backup, para que possa ser facilmente ativada/desativada.

#### Cage radius
Ajusta quão longe do objeto de bake os raios são enviados para procurar objetos-alvo. Por padrão, essa distância é mantida baixa para evitar artefatos, mas pode ser aumentada se os objetos-alvo estiverem longe do objeto de bake.

##### Ray offset
Ajusta de onde os cálculos de bake começam no objeto de bake. Por padrão, eles começam a 5% de distância da superfície, o que evita a maioria dos artefatos comuns. Se os objetos-alvo estiverem muito longe do objeto de bake, esse deslocamento pode precisar ser aumentado.


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

Projeta detalhes esculpidos, pintura, camadas e texturas em valores de vértice.

Pode ser visto como o inverso do baking; se o baking transfere propriedades de vértice para texturas, a reprojeção transfere texturas (e outras propriedades)
 de volta para vértices.

::: tip
Ao usar `Bake to texture` ou `Reproject to vertex`, tanto as cores de vértice quanto as texturas de material serão levadas em conta.
:::

#### From itself
Converte texturas do material em valores de vértice. Este botão só ficará ativo se o objeto tiver UVs e texturas estiverem ativas no material.

::: tip DICA: pintura em textura
O Nomad não suporta diretamente pintar e editar texturas, mas resultados muito semelhantes podem ser obtidos projetando texturas -> valores de vértice, pintando em vértices e depois assando vértices -> texturas:

1. Configure um objeto de baixa contagem de polígonos com UVs
1. Carregue texturas no material dele
1. Subdivida o suficiente para poder pintar
1. Use `Reproject to vertex` no modo `From itself`; agora a textura foi convertida em valores de vértice
1. Pinte, suavize, esfume, carimbe, faça as edições que precisar
1. Use `Bake to texture` no modo `From itself`. Essas edições são convertidas de volta em texturas.
:::

#### From high-res ()
Converte quaisquer objetos visíveis em valores de vértice no objeto selecionado. O número neste botão indica o número de objetos visíveis.

::: tip
Reprojetar outros objetos pode ser usado não apenas para transferir informações de cor de outros objetos, mas também para projetar vértices em outros objetos, por exemplo, bandagens podem ser projetadas em um personagem.
:::

#### ![](/icons/cog.webp) Menu de engrenagem do Reproject
O menu de engrenagem possui estas opções avançadas:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
Essas caixas de seleção determinam quais propriedades serão projetadas no objeto selecionado. 

#### Relax
A malha selecionada pode ter seu layout suavizado ou relaxado em certa medida para se ajustar melhor aos alvos de reprojeção. Smooth é melhor para malhas de alta contagem de polígonos. Relax é melhor para malhas de baixa contagem. Auto permite que o Nomad determine o melhor método.

#### Iterations
Quantas vezes a operação de relaxamento deve ser aplicada durante a reprojeção.

#### Cage radius
Ajusta quão longe do objeto selecionado os raios são enviados para procurar objetos-alvo. Por padrão, essa distância é mantida baixa para evitar artefatos, mas pode ser aumentada se os objetos-alvo estiverem longe do objeto de bake.

#### Ray bias
Valores mais baixos favorecem a projeção para o ponto mais próximo na superfície alvo. Valores mais altos favorecem um ponto de interseção usando a normal da superfície. 

#### Ray offset
Ajusta de onde os cálculos de bake começam no objeto selecionado. Por padrão, eles começam a 5% de distância da superfície, o que evita certos artefatos. Se os objetos-alvo estiverem muito longe do objeto selecionado, esse deslocamento pode precisar ser aumentado.


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
Refaz a malha usando o [algoritmo Instant Meshes de Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Ele analisará o fluxo de uma malha e criará uma topologia de quads limpa.

::: tip
No iOS e no desktop, a ferramenta [Quad remesher](tools#quad-remesher) oferece melhores resultados e mais controle.
:::

#### Remesh
Inicia a operação do Instant Meshes.

#### Target quads
O número de polígonos quad que o quad remesh tentará criar.

#### ![](/icons/cog.webp) Menu de engrenagem do Quad Remesh Instant
O menu de engrenagem possui estas opções avançadas:

##### Crease angle
Um limite de cantos afiados que tentará ajudar a orientar a operação de remesh.

#### Max fill hole
O algoritmo às vezes pode produzir buracos indesejados. Se um buraco tiver menos vértices do que este valor, ele será preenchido.

### Holes
![](/images/topology_holes_menu.webp)
Na maior parte do tempo, seu objeto provavelmente será “watertight”, o que significa que a malha é “fechada”.

Se o seu objeto tiver buracos, você pode preenchê-los. Note que isso só funciona em buracos “ingênuos”; assim, ele não pode “soldar” duas bordas separadas.

![](/videos/hole_filling.mp4)

::: tip
Quando você executa o Voxel remesher, todos os buracos são automaticamente fechados, esteja você usando-o em 1 ou em múltiplas malhas.
:::

#### Close holes
Executa a ação de fechamento de buracos.

#### ![](/icons/cog.webp) Menu de engrenagem do Holes
O menu de engrenagem possui estas opções avançadas:

##### Detail
A densidade de polígonos usada para preencher o buraco. Ao arrastar este controle, um padrão quadriculado será mostrado no modelo, dando uma indicação do tamanho dos triângulos a serem usados. A caixa de seleção desativa isso e usa apenas os pontos existentes, o que geralmente criará triângulos longos e finos sobre o buraco, que podem ser difíceis de esculpir.

##### Fill non-manifold
Tenta preencher buracos não manifold.

##### Face Group

Ao preencher buracos, cada buraco deve receber seu próprio facegroup (Auto), todos devem compartilhar um facegroup (Off) ou não criar facegroups (On).

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
Tenta limpar arestas não manifold. Pode ser útil para softwares externos que não suportam arestas com mais de 2 faces em comum.

#### Clean
Executa a ação de limpeza.
#### ![](/icons/cog.webp) Menu de engrenagem do Force manifold
O menu de engrenagem possui estas opções avançadas:

#### Delete small faces
Um limite usado para remover e unir polígonos pequenos.


### Triplanar
![](/images/topology_triplanar_menu.webp)
Converte a malha em uma primitiva [triplanar](scene.md#triplanar).
Você provavelmente perderá muitos detalhes no processo.

#### Force cubic
Faz com que o triplanar seja um cubo. Caso contrário, o triplanar se ajustará ao menor bounding box em torno do seu objeto.

#### Convert
Executa a ação de triplanar.

#### Resolution
O tamanho do voxel usado na operação de triplanar.

## ![](/icons/dot.webp) Primitive
Parâmetros para a primitiva selecionada. Eles também estão disponíveis na barra de ferramentas de viewport de primitivas.

![](/images/topology_primitive_screenshot.webp)

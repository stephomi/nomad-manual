# ![](/icons/toolbox.webp) Ferramentas {#tools}

![](/images/tools_menu.webp)

::: tip
Vá direto para [Ferramentas](#tools-1) para ver a descrição de cada ferramenta.
:::

## Visão geral {#overview}

As ferramentas são escolhidas na `Caixa de ferramentas` à direita e controladas pelos `Controles da ferramenta` à esquerda. Os ajustes extras ficam no menu `Ferramenta`, no menu do canto superior direito.

As ferramentas de pincel têm controles de tamanho e intensidade. As ferramentas de seleção têm controles para vários estilos de seleção. A parte de baixo dos controles da ferramenta tem atalhos para as operações mais usadas (Suavizar, Máscara, Ocultar, Grupo de faces, Gizmo, Cor, Alfa).

As ferramentas do Nomad são coloridas por categoria na caixa de ferramentas (desative `Ferramentas coloridas` no menu [Interface](interface.md) para ter rótulos neutros):

* <span class=brush>**Ferramentas de pincel**</span> (Argila, Pincel, Suavizar, Camada, Inflar, ApagCamada, Quad Remesher)
* <span class=move>**Ferramentas de movimento**</span> (Mover, Arrastar, Elástico, Empurrar)
* <span class=mask>**Ferramenta de máscara**</span> (Máscara)
* <span class=paint>**Ferramentas de pintura**</span> (Pintar, Borrar)
* <span class=flatten>**Ferramentas de achatar**</span> (Achatar, Planar, Polir)
* <span class=pinch>**Ferramentas de apertar**</span> (Vincar, Apertar)
* <span class=stamp>**Ferramentas de carimbo**</span> (Carimbo, VDM)
* <span class=selection>**Ferramentas baseadas em seleção**</span>, em que primeiro se desenha uma máscara 2d e depois uma operação acontece (Aparar, Dividir, Projetar)
* <span class=creation>**Ferramentas de criação**</span> (Tubo, Torno, Inserir)
* <span class=transform>**Ferramentas de transformação**</span> (Transformar, Gizmo, Organizar, Grade)
* <span class=misc>**Ferramentas diversas**</span> (Grupo de faces, Ocultar)
* <span class=view>**Ferramentas de visualização**</span> (Vista, Medir, Selecionar)



Muitas dessas ferramentas podem ser personalizadas com outros comportamentos de pincel, pressão, texturas etc. pelo menu [Traçado](stroke.md).


### Controles do pincel {#brush-controls}

A barra de ferramentas da esquerda tem controles de raio e intensidade e, depois, controles específicos de cada categoria de ferramenta, explicados abaixo.

![](/images/tool_left_panel.webp)

::: tip
O controle de intensidade de muitas ferramentas pode passar de 100%: vale a pena experimentar!
:::

### Modo Sub {#sub-mode}
O botão logo abaixo do controle de intensidade é o botão `Sub`. O rótulo e a função dele mudam conforme a ferramenta e, ao ser pressionado, ele ativa um comportamento alternativo, geralmente o oposto. Por exemplo, em [Pintar](#paint) ele ativa o modo de apagar, em [Vincar](#crease) ele cria bordas elevadas em vez de vincos etc.

Por padrão, ele funciona como um botão temporário: você pode mantê-lo pressionado para ativá-lo momentaneamente, e ele desliga quando você solta. Se você tocar nele, o modo Sub fica ativado de forma permanente.

### Atalhos {#shortcuts}
Na parte de baixo da barra de ferramentas da esquerda há atalhos para [Suavizar](#smooth), [Máscara](#mask), [Ocultar](#hide), [Grupo de faces](#facegroup), [Gizmo](#gizmo), [Cor](painting.md#pbr-sliders) e [Alfa](stroke.md#alpha).

Por padrão, todos funcionam como botões temporários: você pode mantê-los pressionados para ativá-los momentaneamente, e eles desligam quando você solta. Se você tocar em um deles, aquele modo de atalho fica ativado de forma permanente.

### Controles de seleção {#selection-controls}

As ferramentas [Máscara](#mask), [Pintar](#paint), [Aparar](#trim), [Dividir](#split), [Projetar](#project), [Grupo de faces](#facegroup), [Ocultar](#hide) e [Selecionar](#select) usam controles parecidos para selecionar áreas da malha.

![](/images/tools_shape_selector_panel.webp)

Toque no botão de forma na barra de ferramentas da esquerda (ele mostra a forma atual, `Laço` por padrão) para abrir uma janela com as formas. Nas ferramentas que também funcionam com pincel (Máscara, Pintar, Grupo de faces, Ocultar), essa mesma janela também traz os tipos de traçado.

* `Vista` - Nenhuma forma: a ferramenta não faz nada em especial, como no modo de câmera.
* `Laço` - Uma forma desenhada à mão livre.
* `Polígono` - Uma forma fechada, definida por uma combinação de curvas e/ou linhas retas. Veja [Edição de formas](#shape-editing) abaixo para mais informações.
* `Curva` - (Só em Projetar) - Uma curva à mão livre para a projeção.
* `Caminho` - (Só em Projetar) - Uma curva definida por pontos. Veja [Edição de formas](#shape-editing) abaixo para mais informações.
* `Linha` - Arraste uma linha para definir um corte plano. Por padrão, a operação é aplicada na malha na hora; mude a opção `Editar` se não quiser isso (mantenha pressionado ou deslize sobre o ícone da linha).
* `Faixa` - Uma tira entre duas guias paralelas, com um gradiente de um lado ao outro. `Estender` mantém o valor máximo depois da guia mais distante em vez de parar na faixa; `Inverter` troca a guia de onde o gradiente começa.
* `Retângulo` - Arraste uma linha diagonal: ela define os cantos de um retângulo. Mantenha pressionado ou deslize para ver a opção `Editar`, `Quadrado` para forçar um quadrado e `Centralizado` para que o primeiro clique seja o centro do retângulo.
* `Elipse` - Arraste uma linha diagonal: ela define o tamanho de uma elipse. Mantenha pressionado ou deslize para ver a opção `Editar`, `Círculo` para forçar um círculo e `Centralizado` para que o primeiro clique seja o centro da elipse.
* `Virar` - Inverte a máscara da forma, ou a direção da ferramenta Projetar.

A maioria das ferramentas tem uma opção `Editar`, que decide o que acontece quando você termina de desenhar a forma:
* `Editar: desativado` - A operação acontece assim que você solta.
* `Editar: ativado` - A forma continua editável. Um botão verde aparece ao lado dela para executar a operação. Assim você pode ajustar a forma e a vista e, quando estiver pronto, tocar no botão verde.
* `Editar: segurar` - A operação acontece ao soltar, a menos que você segure no fim do traçado para continuar editando a forma.

### Edição de formas {#shape-editing}
A edição de polígonos e a de curvas funcionam de forma parecida:

* Para começar, arraste uma linha para definir 2 pontos e depois puxe a partir do meio da linha para criar um polígono ou uma curva.
* Toque nos pontos para alternar entre suave e anguloso.
* Toque e arraste nos trechos de curva ou de linha para criar novos pontos.
* Para apagar um ponto, arraste-o sobre o vizinho até ele ficar vermelho.
* O ícone de lixeira no canto do ícone de polígono ou de caminho apaga a forma.

### Menu de ajustes {#settings-menu}

Muitas ferramentas têm ajustes extras, que ficam no menu `Ferramenta`, no menu do canto superior direito. O menu fica acinzentado nas ferramentas que não têm ajustes extras.

![](/images/tools_settings_menu.webp)

## Ferramentas {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Argila](#clay)       | ![](/icons/tool_brush.webp)   <br> [Pincel](#brush)     | ![](/icons/tool_move.webp)       <br> [Mover](#move)              | ![](/icons/tool_drag.webp)      <br> [Arrastar](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elástico](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Suavizar](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Máscara](#mask)       | ![](/icons/tool_paint.webp)   <br> [Pintar](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Borrar](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Achatar](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Polir](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Vincar](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Apertar](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Aparar](#trim)              | ![](/icons/tool_split.webp)     <br> [Dividir](#split)         | ![](/icons/tool_project.webp)   <br> [Projetar](#project)     | ![](/icons/tool_layer.webp)   <br> [Camada](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Inflar](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Empurrar](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Carimbo](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [ApagCamada](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tubo](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Torno](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Inserir](#insert)   | ![](/icons/tool_transform.webp)  <br> [Transformar](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Grupo de faces](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Ocultar](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Medir](#measure) | [Organizar](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Selecionar](#select)       | ![](/icons/tool_lattice.webp)   <br> [Grade](#lattice)     | ![](/icons/tool_view.webp)    <br> [Vista](#view)       |

------

### ![](/icons/tool_clay.webp) Argila {#clay}
A ferramenta Argila é útil para ir construindo volume na escultura. `Sub` remove material da escultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pincel {#brush}
O pincel padrão. `Sub` remove material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Mover {#move}
A área sob o pincel fica grudada nele, permitindo uma deformação elástica. A seleção é mantida durante o movimento: se você afastar o pincel e depois voltar ao ponto de partida, não verá nenhuma deformação.

O modo Sub é `Normal` e move a área sob o pincel ao longo da normal da superfície.

Este pincel serve tanto para deformações grandes quanto para pequenos ajustes cuidadosos.

#### Ajustes de Mover {#move-settings}

* `Raio (Fundo)` - A que distância da borda de um modelo você pode estar e ainda assim esculpir; útil ao trabalhar na silhueta de um objeto. Desmarque para só pegar a superfície quando começar sobre o modelo.
* `Apenas vértice do mesmo lado` - Ignora os vértices voltados para a direção oposta à da deformação.
* `Direção` - Usada pelo modo Sub `Normal`, decide se arrastar empurra ou puxa a superfície:
    * `Auto` - Escolhe para você um dos dois métodos abaixo, com base no ângulo da normal da superfície.
    * `Normal 3D` - Compara a posição do ponteiro na tela com a normal da superfície vista pela câmera.
    * `XY` - Usa a posição do ponteiro na tela (para cima/baixo, esquerda/direita) para decidir entre empurrar e puxar.
    * `Limite` - Com `Auto`, o ângulo limite que decide qual método é usado.
* `Velocidade de rotação` - Você pode torcer a área agarrada enquanto a move: gire dois dedos, gire o corpo da sua caneta ou segure uma tecla modificadora (Alt, Ctrl, Shift ou Cmd) enquanto arrasta com o mouse. Há um controle para dedo, um para caneta e um para mouse; desmarque um deles para desativar aquela entrada.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Arrastar {#drag}
A área sob o pincel fica grudada nele, permitindo uma deformação elástica. Ao contrário do pincel Mover, a seleção é atualizada continuamente durante o traçado, então dá para criar formas mais longas, como cobras, principalmente com a Topologia dinâmica ativada.

O modo Sub é `Normal` e move a área sob o pincel ao longo da normal da superfície.

Este pincel é bom para mudanças de forma mais soltas e gestuais.

#### Ajustes de Arrastar {#drag-settings}

Arrastar tem os mesmos ajustes que [Mover](#move-settings): `Raio (Fundo)`, `Apenas vértice do mesmo lado`, `Direção` e `Velocidade de rotação`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elástico {#elastic}
Agarra e puxa a superfície como [Mover](#move), mas com uma deformação elástica: em vez de parar na borda do pincel, o puxão vai diminuindo suavemente com a distância ao longo do objeto, um pouco como esticar borracha. O raio do pincel define a largura do puxão.

O modo Sub é `Normal` e move a área sob o pincel ao longo da normal da superfície.

Este pincel é bom para mudanças de proporção grandes e suaves, que continuam lisas.

#### Ajustes de Elástico {#elastic-settings}

Elástico tem os mesmos ajustes que [Mover](#move-settings), exceto `Apenas vértice do mesmo lado`. `Raio (Fundo)` vem desativado por padrão.

### ![](/icons/tool_smooth.webp) Suavizar {#smooth}
Suaviza a área tirando a média das posições dos pontos. Esta ferramenta depende muito da densidade de polígonos.
Ou seja, se você tiver muitos polígonos, a suavização será menos eficaz.

O modo Sub é `Relaxar`, que suaviza apenas a malha de arame, mas tenta manter os detalhes geométricos.

#### Ajustes de Suavizar {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grupo de faces {#smooth-facegroup}

* `Relaxar` - Suaviza as bordas dos grupos de faces. Use uma intensidade acima de 100% para suavizar as bordas rapidamente. `Auto` suaviza só se a pré-visualização dos grupos de faces estiver ativada, `Não` desativa, `Sim` ativa.

##### Vértice {#vertex}
* `Manter volume` - Suaviza sem encolher a superfície, para que suavizar várias vezes não murche suas formas. O botão de engrenagem ao lado guarda os valores de `Encolher` e `Inflar` usados para isso.
* `Manter bordas` - Em malhas com bordas abertas, como um plano, os cantos podem acabar suavizados. Ativar esta opção mantém parados os vértices da borda da malha.
* `Suavização estável` - Tenta tornar a suavização independente da topologia. Funciona melhor com densidade de topologia variada e com um valor alto de intensidade de suavização.
* `Relaxar` - O mesmo que o modo alternativo Relaxar da barra de ferramentas da esquerda.

##### Pintura {#painting}
* `Suavização da tela` - Use esta opção para ter uma suavização independente da topologia, mesmo com muitos polígonos. `Auto`, `Não` ou `Sim`.
* `Amostras da tela` - A qualidade da suavização: números mais altos suavizam mais, porém de forma mais lenta.

::: tip
Densidades de polígonos maiores podem exigir uma intensidade acima de 100%. Valores bem altos (300%, 500%) também funcionam bem como ferramenta de escultura, forçando as áreas sob o pincel a ficarem planas e lisas rapidamente, como bater na argila com um martelo de madeira!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Máscara {#mask}
Esta ferramenta permite mascarar vértices. Vértices mascarados ficam protegidos da escultura e da pintura.

O modo Sub é `Desmascara` e apaga onde a máscara foi pintada.

Como as seleções dos programas de pintura 2d, as máscaras podem ser pintadas com um pincel ou feitas com seleções por forma (`Laço`, `Retângulo`, `Faixa`...), desfocadas ou com mais nitidez. Escolha o pincel ou a forma na janela de traçado da barra de ferramentas da esquerda; veja [Controles de seleção](#selection-controls).

Diferente dos programas de pintura 2d, elas também podem ser criadas a partir de grupos de faces, e as máscaras podem ser usadas para gerar nova geometria com operações do tipo extrusão/extração.

![](/videos/tool_mask1.mp4)

 Uma barra de ferramentas aparece no topo da viewport com controles extras.

![](/images/tool_mask_toolbar.webp)

Toque no título da barra para expandi-la/recolhê-la, ou na seta no canto superior direito para movê-la para o topo ou para a base da interface.

| Ação                                               | Descrição                                                                                  |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Limpar tudo        | Limpa a máscara de todos os objetos. Quando outros objetos também têm máscara, um botão `Limpar` extra limpa apenas os objetos selecionados |
| ![](/icons/invert.webp)        Inverter           | Inverte a máscara                                                                          |
| ![](/icons/sharpen.webp)       Aumentar nitidez   | Deixa a borda da máscara mais nítida                                                       |
| ![](/icons/blur.webp)          Desfocar           | Desfoca a borda da máscara                                                                 |
| ![](/icons/outline.webp)       Borda              | Mascara a borda aberta da malha, como a beirada de um plano ou o contorno de um furo       |
| ![](/icons/blur.webp)          Desfocar ->        | Arraste para a direita para desfocar a máscara, para a esquerda para deixá-la mais nítida  |
| ![](/icons/circle_plus.webp)   Expandir ->        | Arraste para a direita para aumentar a área mascarada, para a esquerda para reduzi-la      |
| ![](/icons/intensity.webp)     Reforçar ->        | Arraste para a direita para reforçar a máscara, para a esquerda para diluí-la, sem mudar a forma |
| ![](/icons/dig.webp)           Cavidade ->        | Refaz a máscara a partir da curvatura da superfície: arraste para a direita para deixar pintáveis só as cavidades, para a esquerda só as saliências |
| ![](/icons/culling.webp)       Frontal            | Ative para mascarar apenas os vértices voltados para a frente                              |
| ![](/icons/eye_open.webp)      Visível            | Com formas, ative para ignorar os vértices escondidos atrás de outras superfícies          |
|                                 Converter          | Converte a máscara em um grupo de faces                                                    |
| ![](/icons/group_to_mask.webp) Toque (grupo de faces) | Quando ativado, os grupos de faces são exibidos, e tocar em um grupo de faces o mascara |
|                                 Toque (máscara)    | Quando ativado, tocar em uma "ilha" de polígonos mascarados ou não mascarados preenche aquela ilha inteira. |
| ![](/icons/connect.webp)       Conectada          | Quando ativado, os traçados de máscara só afetam a topologia conectada.                    |

##### Gestos rápidos de máscara {#mask-quick-gesture}
Você pode fazer gestos no estilo do ZBrush enquanto segura o botão de máscara rápida na barra de ferramentas da esquerda:
| Ação             | Gesto (segurando o atalho no canto inferior esquerdo) |
| :--------------: | :---------------------------------------------------: |
| Inverter         | Tocar no fundo                                        |
| Limpar           | Arrastar no fundo                                     |
| Desfocar         | Tocar na área mascarada                               |
| Aumentar nitidez | Tocar na área não mascarada                           |


#### Ajustes de Máscara {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Os ajustes de Máscara servem principalmente para criar geometria a partir da máscara. As abas no topo escolhem a operação: [Extrair](#extract), [Dividir](#split-mask) ou [Escavar](#carve). As opções abaixo delas mudam conforme a operação.

* `Pré‑visualização` - Mostra como a nova geometria vai ficar enquanto você ajusta os parâmetros.
* `Raio-X` - Quais objetos são desenhados em raio-X durante a pré-visualização: `Nenhum`, `Não selecionados`, `Selecionados` ou `Todos`.

##### Extrair {#extract}
* `Extrair` - Cria a geometria extraída como um novo objeto.
* `Ação de fechamento` - Como a forma extraída é fechada. `Nenhuma` duplica os polígonos mascarados em uma nova forma e a deixa aberta. `Preencher` faz o mesmo, mas também preenche e suaviza o buraco na parte de trás (não use em superfícies planas). `Casca` fecha a forma usando o valor de `Altura`, e é o padrão.

::: tip

Com a pré-visualização em raio-X ativada, tocar no botão Extrair pode confundir no começo. Como o menu está ativo, ele tenta pré-visualizar uma extração na sua nova forma e mostra a superfície original em raio-X. Mas, como a nova superfície não tem máscara, não há como pré-visualizar a extração, e o Nomad avisa 'Nada para extrair!'.

Isso é normal: feche o menu de ajustes de Máscara para ver a nova forma e a original, e selecione de novo a superfície original se precisar limpar a máscara ou desenhar novas máscaras.
:::

##### Dividir {#split-mask}
* `Dividir` - Extrai tanto as regiões mascaradas QUANTO as não mascaradas em novas formas.
* `Ação de fechamento` (mascarada) - Como a parte mascarada é fechada, com as mesmas opções `Nenhuma`, `Preencher` e `Casca` de Extrair.
* `Ação de fechamento` (não mascarada) - Como a parte não mascarada é fechada, com as mesmas opções.

##### Escavar {#carve}
* `Escavar` - Funciona como se você tivesse aparado a superfície até a profundidade de `Altura`, como cortar um pedaço de casca de laranja. A `Altura` não pode ser 0.

##### Altura {#thickness}
* `Altura` - A altura da forma extraída. O botão Mais/Menos alterna entre uma extrusão para fora, para dentro ou para os dois lados.

##### Suavidade {#smoothness}
Quando ativada, suaviza a forma extraída; funciona melhor com mais polígonos.
* `Todos` / `Apenas bordas` - Suaviza a forma inteira ou só as bordas, sem mexer no formato da superfície de cima.
* `Iterações` - Com `Todos`, a quantidade de suavização aplicada. Valores altos produzem bordas curvas bem suaves, mas começam a se afastar do formato da máscara.
* `Parede` - Com `Apenas bordas`, a quantidade de suavização nas paredes. O botão dela alterna entre Relaxar, que mantém os cantos vivos, e Suavizar, que também os arredonda.
* `Interior` - Com `Apenas bordas`, o quanto a superfície de cima é uniformizada. O botão dela alterna entre Relaxar, que mantém os detalhes esculpidos e só uniformiza a direção da extrusão (para que os detalhes não criem espinhos), e Suavizar, que suaviza a própria superfície.

##### Laterais {#edge-loop-side}
* `Reto` - Paredes simples nas laterais da forma extraída.
* `Chanfro` - (Só em Extrair com `Casca`) Uma beirada inclinada na borda da frente. `Chanfro` define a largura, em % da `Altura` ou em unidades do mundo (o botão ao lado alterna), `Divisões do chanfro` o subdivide (`Auto` por padrão), e uma curva permite moldar o perfil dele.
* `Perfil` - Molda as paredes com uma curva de perfil, com uma `Largura` em % da `Altura` ou em unidades do mundo.
* `Máscara` - A altura segue a máscara: as partes desfocadas da máscara ficam mais baixas, o que permite formas suaves e de altura variável.
* `Divisões da parede` - O número de loops de arestas nas laterais. Com `Auto`, o Nomad escolhe o número de divisões que gera polígonos quadrados, iguais aos polígonos da área mascarada.




### ![](/icons/tool_maskSelector.webp) Máscara por seleção {#selection-mask}
A ferramenta Máscara por seleção (MáscSel) agora faz parte da [ferramenta Máscara](#mask). Para mascarar com formas em vez de um traçado de pincel, escolha uma forma (`Laço`, `Polígono`, `Retângulo`...) na janela de traçado da ferramenta Máscara; veja [Controles de seleção](#selection-controls).

O modo Sub `Desmascara` também funciona com formas e apaga a máscara dentro da forma.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Pintar {#paint}
Aplica cor e propriedades de material. Para saber mais sobre materiais, veja a seção [Pintura](painting.md).

O modo Sub é `Apagar` e remove a pintura.

Além dos traçados de pincel, Pintar também pode preencher formas (`Laço`, `Retângulo`, `Faixa`...); veja [Controles de seleção](#selection-controls).

#### Ajustes de Pintar {#paint-settings}
* `Filtro de camada` - Funciona como o bloqueio de alfa da camada no Photoshop ou no Procreate. Se você estiver pintando em uma camada com esta opção ativada, só pode alterar onde já existe pintura; as áreas sem pintura ficam protegidas. Só está disponível quando há uma camada selecionada.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Borrar {#smudge}
Borra a cor e as propriedades de material. O menu de ajustes de Borrar tem um controle de `Qualidade`: valores mais baixos deixam os traçados mais rápidos.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Achatar {#flatten}
Achata a área projetando os pontos no plano médio.

O modo Sub é `Preencher`: ele define um plano a partir do ponto mais alto e tende a puxar os pontos para cima.

#### Ajustes de Achatar {#flatten-settings}

* `Bloquear direção do plano` - Usa a direção do plano calculada no primeiro clique. Vem desativado por padrão.
* `Bloquear origem do plano` - Usa o primeiro clique como centro do plano. Vem desativado por padrão e só pode ser ativado junto com `Bloquear direção do plano`.

Quando uma ou as duas opções estão desativadas, dá para aprofundar o achatamento aos poucos ou mudar o ângulo do plano com traçados longos que passam por profundidades e curvaturas diferentes. Junto com as opções de amostragem de área do menu do pincel, isso oferece um controle bem preciso.

::: tip
Ao trabalhar em áreas de curvatura acentuada, por exemplo ao tentar achatar as bochechas enquanto a ferramenta insiste em afetar as laterais do nariz, crie uma máscara para proteger as áreas que o pincel Achatar não deve afetar.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Deixa os pontos planos projetando-os no plano médio, mas acumulando menos que o pincel Achatar. Isso gera superfícies de arestas vivas mais limpas. Traçados rápidos empurram e puxam mais a superfície; traçados mais lentos, que começam em áreas já planas e vão se expandindo, mantêm melhor o plano.

O modo Sub é `Preencher`: ele define um plano a partir do ponto mais alto e tende a puxar os pontos para cima.

Na verdade, Planar é a mesma ferramenta que `Achatar`, mas com `Bloquear direção do plano` ativado. Por isso tende a criar superfícies mais estáveis e de arestas vivas, enquanto Achatar é mais escultórico e serve para criar áreas semiplanas.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Polir {#polish}
Outro membro da família Achatar, configurado para polir superfícies até virarem planos limpos. É a mesma ferramenta que `Achatar`, com outros padrões de [Traçado](stroke.md): `Rastro`, `Filtro de normal por área` e `Filtro de profundidade` vêm ativados.

O modo Sub é `Preencher`, como em Achatar.

Polir tem os mesmos ajustes que [Achatar](#flatten-settings): `Bloquear direção do plano` e `Bloquear origem do plano`.

### ![](/icons/tool_crease.webp) Vincar {#crease}
As ferramentas de vinco são úteis para esculpir pequenos cortes ou sulcos.

O modo Sub é `Inverter` e cria um vinco em relevo.

#### Ajustes de Vincar {#crease-settings}

* `Fator de aperto` - O quanto os vértices são puxados de lado, em direção ao pincel. Se o aperto estiver em 1 e o deslocamento em 0, a superfície não muda de profundidade, só de topologia, com as arestas puxadas em direção ao traçado.
* `Fator de deslocamento` - O quanto os vértices são empurrados/puxados em profundidade. Se o aperto estiver em 0 e o deslocamento em 1, surgem vincos profundos ou relevos, mas com aspecto serrilhado, porque não há geometria suficiente puxada em direção ao vinco para definir com precisão as laterais e o fundo dele.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Apertar {#pinch}
Esta ferramenta pode ser usada para deixar as arestas mais vivas.

O modo Sub é `Inverter` e afasta os vértices uns dos outros.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Aparar {#trim}
A ferramenta Aparar remove um pedaço da malha e oferece opções para tratar o vão que fica. Ela usa os [Controles de seleção](#selection-controls) para definir o corte.

O modo Sub é `Virar` e inverte a forma, para remover o outro lado.

::: tip
Como esta ferramenta projeta a partir da câmera, você recebe um aviso se a câmera estiver no modo perspectiva.

No modo ortográfico, o corte na malha é paralelo à vista, que é o que as pessoas costumam esperar. Com uma câmera em perspectiva, o corte fica diferente no lado distante do objeto em relação ao lado próximo.
:::

#### Ajustes de Aparar {#trim-settings}

Os ajustes ficam agrupados em `Preenchimento de furo`:

* `Pintura com traçado` - Se a pintura estiver ativada no menu Pintura, a região remendada é preenchida com a cor selecionada.
* `Booleano` - Preenche o buraco do corte com uma região de quads. A região preenchida fica plana.
* `Legado` - Preenche o buraco do corte com uma região triangulada. A região preenchida fica plana.
* `Preencher` - Preenche o buraco com uma região triangulada. A região preenchida forma uma superfície curva, como a película de uma bolha de sabão.
* `Nenhum` - Não preenche o buraco.

Com `Booleano`, a seção `Detalhe` tem:

* `Forma` - O tamanho aproximado dos quads e triângulos usados no lado da forma do corte.
* `Furos` - O tamanho aproximado dos triângulos ou polígonos usados no buraco preenchido. O botão de vínculo ao lado de `Detalhe` o mantém sincronizado com `Forma`; desvincule para defini-lo separadamente.
* `Manter topologia` - Não suaviza nem simplifica o limite do corte, mantendo a topologia original da malha perto das faces mascaradas e ocultas.

Com `Legado`:

* `Detalhe` - O tamanho aproximado dos triângulos usados no corte.
* `Suavização do furo` - O quanto os triângulos são relaxados na área preenchida.
* `Épsilon limite` - Um valor que pode ser ajustado para melhorar o algoritmo legado de preenchimento de furos.

Com `Preencher`:

* `Detalhe` - O tamanho aproximado dos triângulos usados no corte.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Dividir {#split}
Parecida com a ferramenta [Aparar](#trim), só que, enquanto Aparar descarta a seleção, Dividir mantém a seleção como um novo objeto.

O modo Sub é `Dividir`: cada pedaço vira um objeto próprio, então formas sobrepostas (por exemplo, com simetria) são cortadas em partes separadas em vez de serem unidas em uma só.

#### Ajustes de Dividir {#split-settings}

Dividir tem os mesmos ajustes de `Preenchimento de furo` que [Aparar](#trim-settings): `Pintura com traçado`, os métodos `Booleano`, `Legado`, `Preencher` e `Nenhum`, e as opções de `Detalhe` de cada um.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projetar {#project}
A ferramenta Projetar parece com a ferramenta [Aparar](#trim), mas não apaga nem cria geometria: ela só move os vértices para se ajustarem à seleção.

![](/videos/tool_project.mp4)

::: tip
Se você usar Projetar em uma camada, pode misturar a forma original e a projetada com o controle da camada.
:::

### ![](/icons/tool_layer.webp) Camada {#layer}
Eleva a superfície, mas com uma altura limite.

Se você mantiver a caneta encostada e continuar passando sobre uma área, Camada sobe até uma certa altura e para por ali, enquanto outras ferramentas continuam acumulando altura.

Observe que, por padrão, o limite vale só para cada traçado! Se você começar um novo traçado, ele parte da nova altura da superfície.

Para definir uma altura máxima constante ao longo de vários traçados, use a ferramenta Camada com o sistema de [Camadas](layers.md) do Nomad.

Crie uma camada e use esta ferramenta. Agora a altura máxima é definida pela camada, então você pode dar vários traçados e a altura será sempre a mesma.

`Sub` usa uma profundidade mínima, criando sulcos.

#### Ajustes de Camada {#layer-settings}

* `Usar dados da camada` - Quando ativado e com uma camada selecionada, usa os dados da camada para definir a altura máxima. Um aviso lembra você quando nenhuma camada está selecionada.
* `Inflar` - Quando ativado, ajusta a direção em que a camada age, para resultados mais suaves.
* `Relaxar (Normal)` - Com `Inflar` ativado, a quantidade de suavização aplicada às normais.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Inflar {#inflate}
Move os vértices ao longo das próprias normais. `Sub` move os vértices ao longo da normal invertida.

#### Ajustes de Inflar {#inflate-setings}
* `Relaxar (Normal)` - A quantidade de suavização aplicada às normais.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Empurrar {#nudge}
Move ou "espalha" os pontos na direção do traçado.

O modo Sub é `Dobra` e empurra uma dobra de material ao longo do traçado: um volume à frente do pincel e uma depressão atrás dele.

#### Ajustes de Empurrar {#nudge-settings}
* `Suavizar` - O quanto a área sob o pincel é suavizada enquanto você a empurra, o que mantém limpa a superfície espalhada.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Carimbo {#stamp}

Toque e arraste para elevar uma área da escultura com o formato do Alfa selecionado.

É simplesmente a [ferramenta Pincel](#brush) com o tipo de traçado `Bloqueio + raio`.

`Sub` afunda o carimbo na superfície em vez de puxá-lo para fora.

::: tip
O Carimbo costuma funcionar melhor com geometria de alta resolução. Se você procurar na internet por "wrinkles alpha", "pores alpha", "scales alpha" etc., essas texturas alfa junto com o Carimbo são uma ótima forma de adicionar detalhes orgânicos à escultura de um personagem.

Os dois modos de traçado servem para coisas diferentes.

* `Bloqueio + raio` tem uma *altura* fixa; arrastar ajusta a largura e a rotação do carimbo. Bom para texturas de pele, que precisam ter a mesma profundidade/altura, mas rotações e escalas diferentes para disfarçar padrões repetidos.
* `Bloqueio + intensidade` tem uma *largura* fixa; arrastar ajusta a rotação e a altura do carimbo. Bom para rebites, que precisam ter todos o mesmo tamanho, mas rotações e alturas diferentes.

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Carimba um mapa de deslocamento vetorial (VDM). Diferente de um alfa, que só consegue empurrar a superfície para cima ou para baixo, um VDM guarda uma forma 3d completa, então consegue carimbar partes salientes, como orelhas, chifres ou folhas enroladas. Funciona como o [Carimbo](#stamp), com os mesmos modos de traçado `Bloqueio + raio` e `Bloqueio + intensidade`.

`Sub` (`Inverter`) inverte a profundidade do carimbo, para pressioná-lo na superfície como um molde.

O próprio VDM é escolhido no menu [Alfa](stroke.md#alpha), que também tem um controle de `Altura` para mudar a escala só da altura do carimbo, sem alterar o deslocamento lateral.

O botão `Criar` na barra de ferramentas da esquerda permite fazer seus próprios carimbos:

* `Novo VDM...` - Adiciona um plano preparado para esculpir um VDM. Esculpa sua forma nele e depois sele com `Topologia -> Selar -> VDM`: o Nomad adiciona o novo carimbo à biblioteca de VDM e o seleciona.
* `Capturar VDM` - (Experimental) Arraste sobre a superfície de um modelo para pegar aquela área e transformá-la em um carimbo VDM. `Tolerância` achata suavemente a borda da captura.

::: tip
Evite a TopoDin ao esculpir um plano de VDM: ela estraga as UVs do plano e distorce o carimbo. Mantenha também a escultura longe da borda do plano, senão o carimbo vai mostrar uma aresta dura.
:::


### ![](/icons/tool_clearLayer.webp) ApagCamada {#delete-layer}
Esta ferramenta redefine camadas localmente; é preciso ter uma camada ativa, senão nada acontece. Ela apaga os dados esculpidos da camada, e também a pintura dela quando a pintura está ativada.

O modo Sub é `Inverter` e reforça levemente a camada em vez de apagá-la.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tubo {#tube}
Cria um tubo desenhando uma curva.
![](/images/tool_tube_new.webp)

Depois que o tubo é criado, o caminho pode ser editado no espaço 3d com controles parecidos com os de [Edição de formas](#shape-editing) e das ferramentas de edição de curvas.

![](/videos/tool_tube.mp4)

#### Barra de ferramentas da esquerda do Tubo {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

A barra de ferramentas da esquerda tem as seguintes opções:

* `Sincronizar` - Se o tubo atual for instanciado e houver nós filhos do tubo que diferem entre as instâncias, isto os sincroniza de novo.
* `Ajuste` - Quando ativado, os modos curva e caminho se ajustam a outros objetos enquanto você desenha. Quando desativado, só o primeiro ponto se ajusta, e o resto do tubo é desenhado naquela profundidade.
* `Deslocamento` - Define a profundidade do ajuste: com 0%, o meio da seção do tubo fica sobre a superfície; valores positivos o levantam da superfície, valores negativos o afundam. 100% equivale ao raio do tubo.
* `Vista` - Nenhum modo de desenho, para você mover a câmera livremente.
* `Curva` - Desenha um tubo à mão livre. Tem um pequeno menu suspenso:
    * `Editar` - O que acontece quando você termina o traçado, veja [Controles de seleção](#selection-controls): cria o tubo na hora, mantém a curva editável com um círculo verde de validação ao lado ou permite `Segurar` no fim do traçado para continuar editando.
    * `Fechado` - Transforma o tubo em um laço.
    * `Continuar desenhando` - Depois de validar um tubo, continua na ferramenta para desenhar o próximo.
    * `Precisão` - Quantos pontos de curva são usados para converter o caminho desenhado em tubo. 0% usa o menor número de pontos, mas perde pequenas mudanças de curvatura. 100% é bem preciso e usa muitos pontos.
* `Caminho` - Cria um tubo tocando para definir os pontos da curva. Toque no círculo verde para validar o caminho. Tem um pequeno menu suspenso:
    * `B-spline` - Um método alternativo de desenhar curvas, em que os pontos geralmente não ficam sobre a curva, mas que pode dar resultados mais suaves que o método padrão.
    * `Fechado` - Transforma o tubo em um laço.
    * `Tela` - Quando ativado, o caminho fica "preso" à tela, então você pode mover a vista e o objeto e o caminho continua no lugar. Quando desativado, o caminho faz parte da cena 3d e se move com a câmera e os objetos.
* `Seção` - A curva vira um anel ao redor da forma, cortado pelos seus dois pontos na direção de onde você estava olhando.

##### Barra de ferramentas superior do Tubo {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Quando um tubo está selecionado, uma barra de ferramentas aparece no topo da viewport com controles extras. Toque no título da barra para recolhê-la/expandi-la, e na seta no canto superior direito para movê-la para o topo ou para a base da viewport.

* `Validar` - Converte o tubo em polígonos comuns para que ele possa ser esculpido.
* `Editar` - Mostra os pontos da curva para que possam ser manipulados.
* `Espelhar` - Adiciona um repetidor de espelho como pai desta curva.
* `Ajuste` - Ajusta os pontos da curva às superfícies próximas.
* `Fechado` - Une o início e o fim da curva para formar um laço.
* `B-spline` - Alterna entre interpolação Catmull-Rom e B-spline.
* `Tampa` - Alterna entre tampas nas duas pontas do tubo, só no início ou no fim, ou sem tampas.
* `Furo` - Dá espessura ao tubo, transformando-o em um cano. Alterna entre ter um furo nas duas pontas, só no fim, ou sem furos.
* `Raio` - Alterna entre um raio uniforme, um raio no início e no fim, ou um raio por ponto da curva. Eles são editados com alças laranja na curva.
* `Torção` - Alterna entre sem torção, uma torção uniforme, uma torção no início e no fim, ou uma torção por ponto da curva. Elas são editadas com alças rosa na curva.
* `Perfil` - Alterna entre sem perfil (ou seja, perfil circular), um perfil uniforme, um perfil no início e no fim, ou um perfil por ponto.
* `Editar perfil` - Mostra um editor de perfil. Funciona como as ferramentas de [Edição de formas](#shape-editing), pode salvar e carregar predefinições de perfil e tem uma opção para editar o perfil no espaço 3d.
* `Espiral` - Abre um menu para adicionar uma torção em espiral ao tubo. Esse menu tem as opções `Enrolamento`, `Afastamento`, `Escala` e `Rotação`.
* `Divisões X` - O número de divisões ao redor do tubo; com 4 divisões, por exemplo, o tubo fica quadrado.
* `Densidade constante` - Quando ativado, mantém os polígonos quadrados. Quando desativado, permite definir as `Divisões Y` ao longo do comprimento do tubo.
* `...` - Menu de ajustes do tubo.

#### Opção de apagar pontos da curva {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Abaixo da barra de ferramentas há uma opção para apagar pontos da curva. Quando você arrasta um ponto da curva para perto de outro, ele fica vermelho, indicando que, se você soltar, o ponto será apagado. Se estiver fazendo pequenos ajustes e não quiser apagar pontos, este botão desativa esse comportamento.



#### Ajustes do Tubo {#tube-settings}
* `Primitiva` - Botões para ativar/desativar as UVs ou validar o tubo.
* `Subdivisão posterior` - Um atalho para definir o nível de multirresolução antes de validar.
* `Subdivisão linear` - Um atalho para definir o nível de subdivisão linear antes de validar.
* `Divisão X` - O mesmo que Divisões X na barra de ferramentas.
* `Divisão Y` - O mesmo que Divisões Y na barra de ferramentas.
* `Curva (Repetidor)` - Converte o tubo em um [Repetidor de curva](scene.md#curve).

::: tip
Divisões em 4 e Subdivisão posterior em 3 geram tubos lisos com pontas arredondadas, bons para minhocas, cobras e partes do corpo.
:::


### ![](/icons/tool_lathe.webp) Torno {#lathe}
Cria uma superfície de revolução desenhando uma curva.

Esta ferramenta é ótima para formas como vasos e taças.

![](/videos/tool_lathe.mp4)

#### Barra de ferramentas da esquerda do Torno {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

A barra de ferramentas da esquerda tem as seguintes opções:

* `Sincronizar` - Se o torno atual for instanciado e houver nós filhos do torno que diferem entre as instâncias, isto os sincroniza de novo.
* `Fixo` - Quando ativado, o centro do torno fica fixo e aparece na tela. Essa linha central tem pontos de edição que podem ser ajustados. Quando desativado, o centro do torno se atualiza dinamicamente para coincidir com o início e o fim da curva desenhada.
* `Vista` - Nenhum modo de desenho, para você mover a câmera livremente.
* `Curva` - Desenha o perfil do torno em um só traçado. Tem um pequeno menu suspenso:
    * `Editar` - O que acontece quando você levanta a caneta, veja [Controles de seleção](#selection-controls): cria o torno na hora, mantém a curva editável com um círculo verde ao lado para criar o torno ou permite `Segurar` no fim do traçado para continuar editando.
    * `Fechado` - Une o início e o fim da curva para formar um laço.
    * `Continuar desenhando` - Depois de validar um torno, continua na ferramenta para desenhar o próximo.
    * `Precisão` - Quantos pontos de curva são usados para converter o caminho desenhado em tubo. 0% usa o menor número de pontos, mas perde pequenas mudanças de curvatura. 100% é bem preciso e usa muitos pontos.
* `Caminho` - Cria um torno tocando para definir os pontos da curva. Toque no círculo verde para validar o caminho. Tem um pequeno menu suspenso:
    * `B-spline` - Um método alternativo de desenhar curvas, em que os pontos geralmente não ficam sobre a curva, mas que pode dar resultados mais suaves que o método padrão.
    * `Fechado` - Transforma o tubo em um laço.
    * `Tela` - Quando ativado, o caminho fica "preso" à tela, então você pode mover a vista e o objeto e o caminho continua no lugar. Quando desativado, o caminho faz parte da cena 3d e se move com a câmera e os objetos.

#### Barra de ferramentas superior do Torno {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Quando um torno está selecionado, uma barra de ferramentas aparece no topo da viewport com controles extras. Toque no título da barra para recolhê-la/expandi-la, e na seta no canto superior direito para movê-la para o topo ou para a base da viewport.

* `Validar` - Converte o torno em polígonos comuns para que ele possa ser esculpido.
* `Editar` - Mostra os pontos da curva para que possam ser manipulados.
* `Espelhar` - Adiciona um repetidor de espelho como pai deste torno.
* `Ajuste` - Ajusta os pontos da curva às superfícies próximas.
* `Estável` - Quando ativado, o perfil da curva fica preso à linha central do torno. Quando desativado, a linha central pode ser editada sem mover a curva, o que permite formas mais complexas.
* `Foco` - Gira a vista para mostrar o perfil da curva perfeitamente de frente para a câmera.
* `Fechado` - Une o início e o fim da curva para formar um laço.
* `Tampa` - Se Fechado estiver desativado, alterna entre tampas nas duas pontas do tubo, só no início ou no fim, ou sem tampas.
* `Furo` - Dá espessura ao torno, transformando-o em um cano. Alterna entre ter um furo nas duas pontas, só no fim, ou sem furos.
* `B-spline` - Alterna entre interpolação Catmull-Rom e B-spline.
* `Divisões X` - O número de divisões ao redor do torno; com 4 divisões, por exemplo, o torno fica com perfil quadrado.
* `Densidade constante` - Quando ativado, mantém os polígonos quadrados. Quando desativado, permite definir as `Divisões Y` ao longo do comprimento do tubo.
* `...` - Menu de ajustes do torno.

#### Ajustes do Torno {#lathe-settings}
* `Primitiva` - Botões para ativar/desativar as UVs ou validar o tubo.
* `Subdivisão posterior` - Um atalho para definir o nível de multirresolução antes de validar.
* `Subdivisão linear` - Um atalho para definir o nível de subdivisão linear antes de validar.
* `Divisão X` - O mesmo que Divisões X na barra de ferramentas.
* `Divisão Y` - O mesmo que Divisões Y na barra de ferramentas.
* `Curva (Repetidor)` - Converte o perfil da curva em um [Repetidor de curva](scene.md#curve).

### ![](/icons/tool_insert.webp) Inserir {#insert}
Coloca um objeto sobre a superfície de outro. No uso, é parecida com a ferramenta Carimbo, mas para formas 3d completas.

Se você escolher uma primitiva na barra de ferramentas da esquerda, tocar e arrastar sobre qualquer superfície coloca uma primitiva onde você tocou, e o arrasto define o tamanho. Quando você termina de arrastar, Inserir passa para o modo [Transformar](#transform).

No modo Instância, arrastar cria uma nova instância e a desliza sobre a superfície. O tamanho é copiado da primeira forma; assim você pode espalhar várias instâncias do mesmo tamanho de um objeto sobre outras superfícies.

Você não precisa inserir só primitivas! Selecione *qualquer* forma no outliner: se Inserir estiver no modo Instância ou Clonar, você pode arrastar cópias do objeto selecionado sobre qualquer outra superfície.

Se um objeto tiver um pivô personalizado, ele é usado como ponto de ancoragem. Veja o vídeo abaixo.

A barra de ferramentas da esquerda também tem `Vista`, para mover a câmera sem inserir nada, e `Sincronizar`: quando o objeto de destino é instanciado, o novo objeto também é adicionado em todas as outras instâncias.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformar {#transform}
Move/gira/redimensiona um modelo diretamente com 1 e 2 dedos, geralmente sobre a superfície de outro objeto.

A barra de ferramentas da esquerda tem estes botões:

* `Clonar` / `Instância` - Faz uma cópia ou uma instância do objeto; veja a barra de ferramentas do [Gizmo](#left-menu-toolbar).
* `Mover` - Arrastar com um dedo move o objeto. Com o ajuste ativado, o objeto desliza pela superfície sob o seu dedo.
* `Girar` - Arrastar com um dedo gira o objeto. Com o ajuste ativado, gira em torno da normal da superfície sob o seu dedo.
* `Escala` - Arrastar com um dedo muda a escala do objeto.

Uma barra de ferramentas no topo da viewport tem:

* `Destino` - Se a ferramenta move o objeto, o grupo dele ou os vértices, como no [Gizmo](#left-menu-toolbar).
* `Ajustar` - Ajusta o modelo sobre outras superfícies.
* `Superfície` / `Vértice` - Com `Ajustar`, ajusta sobre a superfície ou sobre o vértice mais próximo.

Com 2 dedos, Transformar permite usar 2 desses modos rapidamente:

* Arraste um objeto para posicioná-lo. Pare de mover o primeiro dedo, mas não o tire da tela.
* Encoste o segundo dedo na tela mantendo o primeiro encostado. Ao arrastar o segundo dedo, o objeto muda de escala.
* Levante o segundo dedo e continue arrastando o primeiro: o objeto volta ao modo mover.

Você também pode mudar o segundo modo com um toque do segundo dedo:

* Arraste o objeto para posicioná-lo, pare de mover, mas não tire o dedo da tela.
* Toque com o segundo dedo mantendo o primeiro encostado.
* A ferramenta passa para o modo de rotação. Arraste o primeiro dedo para definir a rotação.
* Toque com o segundo dedo como antes: a ferramenta volta ao modo mover.

Isso permite um fluxo rápido para clonar objetos sobre outro, por exemplo pedras sobre uma paisagem. Repare que o botão de clonar também fica na barra de ferramentas da esquerda, à mão:

* Use a ferramenta Transformar para colocar uma pedra no lugar.
* Solte e toque no botão de clonar.
* Mova essa pedra, gire/redimensione como precisar.
* Solte e toque no botão de clonar.
* Mova essa pedra e repita.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Esta ferramenta permite mover, girar e redimensionar objetos, além de alterar os pivôs deles.

A alça da viewport tem os seguintes recursos:

* `Mover` - Arraste a linha com seta para mover em X/Y/Z. Arraste o ponto cor de pêssego no meio do gizmo para mover livremente no espaço da tela. Arraste os quadrados vermelho, verde e azul para mover nos planos X/Y/Z.
* `Girar` - Arraste os círculos vermelho/verde/azul para girar em X/Y/Z. Arraste a esfera dentro dos círculos para girar livremente.
* `Escala` - Arraste os pontos externos vermelho/verde/azul para mudar a escala em X/Y/Z. Arraste os cones externos vermelho/verde/azul para mudar a escala nos planos X/Y/Z. Arraste o círculo externo cor de pêssego para uma escala uniforme.

![](/images/tool_gizmo.webp)

#### Nós e vértices {#nodes-and-vertices}

Todo objeto no Nomad é feito de um nó e de vértices:

* `Nó` - A "alça" do objeto, que guarda a translação, a rotação e a escala dele, chamadas de matriz de transformação.
* `Vértices` - Os pontos que definem a superfície de um objeto; eles guardam a posição e as informações de pintura.

Se você tiver uma caixa simples, formada por 8 vértices, pode movê-la alterando a matriz de transformação ou alterando as posições dos vértices. Ao esculpir, normalmente você quer alterar os vértices; ao mover objetos com o gizmo, normalmente quer alterar o nó. O Nomad permite as duas coisas.

#### Barras de ferramentas do Gizmo {#left-menu-toolbar}

A barra de ferramentas da esquerda tem:

* `Clonar` - Faz uma cópia independente do objeto atual, que pode ser afastada com o gizmo.
* `Instância` - Faz uma cópia instanciada do objeto atual. Os objetos ficam vinculados, então o que você esculpir em um aparece em todos os objetos instanciados.
* `Pivô` - (Ícone de cadeado, no lugar do botão `Sub`) Quando ativado, o gizmo pode ser movido e girado sem mover o objeto. Como `Sub`, mantenha pressionado para uma mudança rápida ou toque para deixá-lo ligado.

Uma barra de ferramentas no topo da viewport tem os outros controles:

* `Destino` - Define se o gizmo afeta o nó ou os vértices de um objeto:
    * `Auto` - O padrão: funciona como `Grupo`, mas, se a malha tiver máscara ou a simetria estiver ativada, funciona como `Vértice`.
    * `Vértice` - Aplica a transformação nos vértices, levando em conta a máscara e a simetria. Não funciona em primitivas não validadas, e as instâncias também são afetadas.
    * `Objeto` - Move só o objeto atual, ignorando simetria e máscara. Os objetos filhos ficam parados.
    * `Grupo` - Move o objeto e o resto da hierarquia dele, ignorando simetria e máscara.
    * `Instância` - (Objeto e Grupo) O mesmo, mas todas as instâncias do objeto se movem junto.
* `Pivô` - Uma janela para posicionar o pivô rapidamente, explicada [abaixo](#pivot).
* `Todos` / `Mover` / `Girar` / `Escala` - Mostra todas as alças do gizmo, ou só as de mover, girar ou escala.
* `Fixar` - Por padrão, o gizmo vai para o pivô do objeto selecionado. Com Fixar ativado, o gizmo fica onde está.
* `Alinhar` - Alterna entre o pivô alinhado com o objeto atual ou alinhado com o mundo.
* `Ajustar` (rotação) - Faz os valores de rotação se ajustarem a incrementos; o valor do ajuste aparece e pode ser editado quando o ajuste está ativo. A opção `Ímã` faz a rotação grudar em um passo ao cruzá-lo e depois seguir livre; desative para pular de passo em passo.
* `Ajustar` (translação) - Faz os valores de translação se ajustarem a incrementos; o valor do ajuste aparece e pode ser editado quando o ajuste está ativo.

#### ![](/icons/reset.webp) Pivô {#pivot}
A janela `Pivô` na barra de ferramentas superior permite mudar o pivô rapidamente. A posição e a orientação do pivô comandam o gizmo.

**Redefinir**
* `Auto` - Centro do objeto, alinhado à transformação dele.
* `Centralizado` - Leva o pivô ao centro do objeto, mantendo a orientação.
* `Inferior` - Leva o pivô ao centro da base do objeto. Toque de novo para usar a caixa delimitadora do mundo.
* `Superior` - Leva o pivô ao centro do topo do objeto. Toque de novo para usar a caixa delimitadora do mundo.
* `Objeto` - Leva o pivô à origem do objeto, alinhado à transformação dele.
* `Máscara` - Leva o pivô ao centro da região não mascarada. Toque de novo para passar para a região mascarada.
* `Alinhar` - Redefine as rotações para ficarem alinhadas com o mundo, mantendo a posição.
* `Vista` - Alinha o pivô à vista atual, mantendo a posição. Depois disso ele não acompanha a câmera.

**Toque (modo Pivô)**

Ativo só enquanto `Pivô` está ligado, define o que acontece quando você toca uma vez na superfície da malha:
* `Nenhum` - Não faz nada quando o objeto é tocado.
* `Normal` - Move e gira o pivô para alinhá-lo ao ponto tocado da superfície.
* `Primeira ocorrência` - Move (sem girar) o pivô para o ponto tocado da superfície.
* `Mediana` - Move o pivô para o meio do objeto, sob o ponto tocado da superfície.

#### Ajustes do Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Compacto` - Alterna o layout do gizmo para colocar as alças extras fora ou dentro da esfera de rotação.
* `Tamanho do widget` - O tamanho do gizmo.
* `Espessura` - A espessura das linhas do gizmo.
* `Opacidade` - A opacidade do gizmo.
* `Ocultar ao interagir` - Define se o gizmo some temporariamente enquanto é arrastado.

-----

* `Limite de rolagem da tangente` - Controla como a rotação se comporta ao arrastar os círculos para girar em X/Y/Z. Com o valor 0, girar funciona como um botão giratório: arraste o gizmo em círculos. Com o valor 90, girar funciona como puxar a corda de um ioiô: arraste em linha reta, aproximando ou afastando do ponto onde você tocou primeiro. Valores entre 0 e 90 combinam os dois: abaixo do valor, o movimento é linear; acima, é circular.
* `Entrada numérica` - Quando ativada, um toque no gizmo abre uma janela para digitar um valor exato para o eixo tocado.

::: warning
As ferramentas [Gizmo](#gizmo) e [Transformar](#transform) usam uma opção de simetria própria, separada da simetria de escultura!

Por padrão, essa simetria fica desativada.
:::

##### Matriz {#matrix}
Os valores exatos de transformação do objeto não ficam mais nos ajustes do Gizmo: eles foram para o menu `Transformar`, no menu do canto superior direito. A seção `Matriz` dele tem:

* ![](/icons/target.webp) `Mover origem` - Move o objeto para que o pivô dele fique no centro da cena, chamado de origem.
* ![](/icons/bake.webp)  `Selar` - Congela o objeto onde ele está e zera os valores de translação/rotação, com escala 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivô` - Sela o pivô: faz os valores da matriz corresponderem à posição da alça do gizmo no mundo.
* ![](/icons/reset.webp) `Redefinir` - Um atalho que zera a translação e a rotação e põe a escala em 1, movendo e girando o objeto.

::: tip Selar ou selar no pivô
Crie uma caixa, selecione a ferramenta Gizmo, abra e fixe o menu `Transformar`. Por padrão, a translação e a rotação são 0 e a escala é 1.

Ative o modo pivô, mova a alça para um lado e desative o modo pivô. O pivô mudou, mas repare que os valores de translação continuam 0.

Se quiser ver onde o pivô *realmente* está, toque no botão `Pivô` de selar. Agora os valores de translação são atualizados. Repare que a caixa não se move durante essa operação, nem no modo pivô.

Mova e gire a caixa para algum lugar e toque em `Mover origem`. O objeto é movido para que o pivô fique no centro do mundo, mas a rotação não muda.

Toque em `Redefinir`, e a rotação também volta para 0.

Mova e gire a caixa de novo e, desta vez, toque em `Selar`. O pivô fica onde está, a caixa fica onde está, mas os valores de translação e rotação vão para 0.

Pratique isso algumas vezes! Entenda que os valores do pivô ficam escondidos e o Nomad cuida deles para você, mas, se precisar colocar o pivô em posições reais no espaço, selar o pivô faz isso.

:::

* `Translação` - Os valores de translação X, Y, Z.
* `Rotação` - Os valores de rotação X, Y, Z.
* `Escala` - A escala uniforme, se estiver ativada, ou a escala X, Y, Z, se estiver desativada.
* `Cisalhamento` - Os valores de cisalhamento X, Y, Z; só aparecem quando o objeto já está cisalhado.
* `Escala uniforme` - Alterna entre redimensionar de forma uniforme ou separadamente em cada eixo.

À esquerda você pode mover o pivô do gizmo; veja no vídeo abaixo como funciona.
Isso é útil principalmente para a rotação, já que não muda nada na translação.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grupo de faces {#facegroup}

Os grupos de faces permitem organizar o objeto em faces de cores diferentes. Você pode usar esses grupos de várias formas no Nomad:

* Um jeito rápido de selecionar para máscaras
* Ocultar/mostrar partes do objeto
* Organizar o objeto sem precisar separá-lo em partes
* Definir regiões de UV
* Guiar o quad remesher
* Ter mais controle em ferramentas como Suavizar.

#### Barra de ferramentas da esquerda do Grupo de faces {#facegroup-left-toolbar}

* `Grupo` - O botão mostra o grupo de faces atual. Toque nele para ver os grupos de faces disponíveis como amostras e escolher um. Toque em uma amostra para renomeá-la, mudar a cor ou apagá-la. `Remover não utilizados` apaga as amostras sem uso, `Redefinir` remove todas. O ícone de mais cria novas amostras.
* `Ponto` - Pinte sobre o objeto para definir grupos de faces. Com '+ Grupo de faces' ativado, cada novo traçado cria automaticamente um novo grupo de faces, útil para definir regiões rapidamente. Um toque preenche a região selecionada. O controle define o raio do ponto.
* `Relaxar` - Suaviza as bordas dos grupos de faces. Muito útil para definir bordas limpas antes de remalhar em quads, ou para definir painéis em modelagem hard surface. Os controles definem o raio e a intensidade do relaxamento.
* Formas - Cria grupos de faces com formas em vez de pincel, com `Bloqueio + raio`, `Laço`, `Polígono`, `Linha`, `Retângulo` e `Elipse`. Veja [Controles de seleção](#selection-controls) para mais informações.
* `Escolher` - O modo Sub. Quando ativado, seleciona a amostra onde o traçado começa e aplica essa amostra no resto do traçado. Muito útil para arrumar as regiões dos grupos de faces: se um grupo de faces avançou demais, ative `Escolher`, comece um traçado onde a amostra está correta e arraste até a borda para reatribuir a amostra certa.

#### Barra de ferramentas superior do Grupo de faces {#facegroup-top-toolbar}

Uma barra de ferramentas no topo da viewport tem controles extras:

* `Relaxar (Todos)` - Arraste para relaxar as bordas de todos os grupos de faces de uma vez.
* `Frontal` / `Visível` / `Conectada` - Os mesmos filtros de traçado da barra de ferramentas de [Máscara](#mask).
* `Das normais` - Cria grupos de faces com base no ângulo entre as faces. A janela tem o `Ângulo` e permite pular grupos pequenos com base na `Contagem de faces` ou na `Área de superfície`, com uma `Pré‑visualização` antes de validar.
* `Das partes` - Cria um grupo de faces para cada parte desconectada.
* `Das UVs` - Cria um grupo de faces para cada ilha de UV.
* `Da máscara` - Cria um grupo de faces a partir da área mascarada.
* `Toque` - Escolha o que um toque em um grupo de faces faz: preenche com o grupo de faces atual, oculta, mascara ou faz a `Pose` (o grupo tocado e o que vem depois dele são desmascarados, e o gizmo vai para a articulação, com um controle `Desfocar` para a máscara). Uma segunda opção `Toque`, disponível quando a malha tem máscara, limita o toque às faces do mesmo lado da máscara.
* Botões `Limpar` das ferramentas [Ocultar](#hide) e [Máscara](#mask), para mostrar tudo de novo ou limpar a máscara sem sair da ferramenta.

#### Ajustes do Grupo de faces {#facegroup-settings}

O menu `Ferramenta` extrai grupos de faces em novos objetos, com as mesmas opções de `Extrair` dos [Ajustes de Máscara](#mask-settings). O botão `Grupo de faces` no topo escolhe quais grupos são extraídos, e há um controle extra, `Vão`: ele move cada borda para dentro ao longo da superfície; um valor negativo a move para fora, criando sobreposição. Para painéis vizinhos, use metade do vão desejado.

### ![](/icons/tool_hide.webp) Ocultar {#hide}
Oculta ou isola partes do objeto.

Os modos principais ficam no menu da esquerda:

* `Ponto` - Pinte sobre o objeto para ocultar partes dele.
* Formas - Oculta com formas em vez de pincel, com `Laço`, `Polígono`, `Linha`, `Retângulo` e `Elipse`. Veja [Controles de seleção](#selection-controls) para mais informações.
* `Mostrar` - O modo Sub: inverte a operação, para que o modo escolhido mostre partes do objeto em vez de ocultá-las.

Uma barra de ferramentas aparece no topo da viewport com controles extras:

* `Limpar tudo` - Restaura os objetos: todas as partes ocultas voltam a aparecer. Quando outros objetos também têm partes ocultas, um botão `Limpar` extra restaura só os objetos selecionados.
* `Inverter` - Troca as partes ocultas pelas visíveis.
* `Apagar` - Apaga a parte oculta do objeto.
* `Dividir` - Separa a parte oculta do objeto em uma nova forma.
* `Frontal` / `Visível` / `Conectada` - Os mesmos filtros de traçado da barra de ferramentas de [Máscara](#mask).
* `Toque` (grupo de faces) - Usa os grupos de faces para ocultar partes rapidamente: tocar em um grupo de faces oculta o grupo inteiro.
* `Toque` (máscara) - Se houver uma máscara ativa, tocar oculta a parte mascarada.

### ![](/icons/tool_measure.webp) Medir {#measure}
Arraste para medir a distância entre 2 pontos. Depois de posicionados, você pode arrastar as pontas para ajustar a medida.

A barra de ferramentas da esquerda escolhe como a distância é medida:

* `Linha` - Uma linha reta entre os dois pontos.
* `Superfície` - A distância ao longo da superfície, seguindo o corte pelos dois pontos visto da câmera.
* `Seção` - O perímetro da seção que passa pelos dois pontos, como uma fita métrica em volta de um braço.
* `Vértice` - Ajusta as pontas ao vértice mais próximo.
* `Proporção áurea` - Mostra um ponto amarelo no ponto da proporção áurea da medida.
* O botão `?` mostra o volume, a área de superfície e o tamanho dos objetos selecionados.

### ![](/icons/tool_arrange.webp) Organizar {#arrange}
Alinha e distribui vários objetos de uma vez, como as ferramentas de alinhamento de um app de design 2d. Selecione os objetos primeiro; com um único objeto, Organizar trabalha nas partes separadas dele. Uma caixa é desenhada em volta da seleção: arraste as alças dela para mudar a escala.

Uma barra de ferramentas no topo da viewport tem os controles:

* `Mundo` / `Tela` - Organiza ao longo dos eixos do mundo ou da tela (esquerda, direita, cima, baixo).
* `Alinhar` - Alinha os objetos pelo mínimo, pelo centro ou pelo máximo, em cada eixo.
* `Distribuir` - Espaça os objetos por igual entre os dois das pontas, pelo mínimo, pelo centro ou pelo máximo. Precisa de pelo menos 3 objetos.
* `Linha` - Enfileira os objetos ao longo de um eixo.
* `Grade` - Organiza os objetos em uma grade, com um número de objetos em `X`, `Y` e `Z`.
* `Círculo` - (Só em Mundo) Organiza os objetos em círculo em torno do eixo `X`, `Y` ou `Z`.
* `Esfera` - (Só em Mundo) Organiza os objetos sobre uma esfera.

`Linha`, `Grade`, `Círculo` e `Esfera` têm um controle de `Espaçamento` para o vão entre os objetos.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Esta ferramenta converte o objeto selecionado em uma topologia limpa de quads, com controles de densidade, fluxo de arestas e simetria.

::: tip
O Quad Remesher é desenvolvido pela [Exoside](https://exoside.com/) para iOS e desktop.

No iOS, é uma compra no app dentro do Nomad, com pagamento único de US$ 16.

No desktop, compre uma licença na [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Você pode comprar só para o Nomad desktop ou uma licença cruzada para todos os apps de desktop compatíveis.

Se você já tem o Quad Remesher para outro app de desktop, pode [comprar um upgrade para todas as plataformas por um preço menor.](https://exoside.com/quadremesher/quadremesher-upgrade/)

O Quad Remesher não está disponível para Android. No Android, você pode usar os remalhadores gratuitos e de código aberto da aba de topologia [Remalhar em quads](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), mas saiba que os recursos deles são mais limitados.
:::

Enquanto o Quad Remesher não é desbloqueado, a barra de ferramentas superior começa com um botão de carrinho no lugar dos botões de remalhar. No iOS, ele abre a compra no app. No desktop, mostra `Desbloquear (compra, restaurar, teste)`, que verifica sua licença da Exoside (ou inicia o teste). Depois de ativado, as barras de ferramentas da esquerda e superior ficam disponíveis.

* `Ponto` - Este pincel define a densidade desejada. Com intensidade em 100%, pinta em vermelho, o que usa o dobro da densidade de quads desejada nessas regiões. Com intensidade em 0%, pinta em ciano, o que usa metade da densidade de quads desejada nessas regiões. Com intensidade em 50%, pinta em cinza, o que usa a densidade de quads padrão.
* `Suavizar` - Suaviza as transições de densidade vermelho/cinza/ciano.
* `Borrar` - Borra a pintura de densidade.
* `Curva` - Desenhe curvas sobre a superfície da escultura: o quad remesher as usa como guias para o fluxo de arestas. Toque em uma curva para apagá-la.
* `Caminho` - Desenhe caminhos sobre a superfície da escultura: o quad remesher os usa como guias para o fluxo de arestas. Toque em um caminho para apagá-lo.
* `Retângulo` - Desenhe retângulos sobre a superfície da escultura: o quad remesher os usa como guias para o fluxo de arestas. Toque em um caminho para apagá-lo.
* `Elipse` - Desenhe elipses sobre a superfície da escultura: o quad remesher as usa como guias para o fluxo de arestas. Toque em um caminho para apagá-lo.

#### Barra de ferramentas superior do Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Uma barra de ferramentas aparece no topo da viewport com controles extras:


* `<Contagem>` - Toque aqui para iniciar o processo do quad remesher; o número indica a quantidade de quads desejada.
* `Quads` - Define a quantidade de quads desejada deslizando para a esquerda e para a direita, ou toque para digitar um número exato. Observe que isso é mais uma orientação do que um número fixo: os vários controles do quad remesher muitas vezes fazem o resultado não bater exatamente com esse valor.
* `Metade` - Um atalho para definir o valor desejado como metade da quantidade atual de polígonos.
* `Igual` - Um atalho para definir o valor desejado como a quantidade atual de polígonos.
* `Guias` - Ativa para usar ou ignorar as guias. Quando há guias, um segundo botão `Guias` mostra quantas são; toque nele para apagar todas.
* `Densidade` - Ativa para usar ou ignorar a pintura de densidade. Quando há pintura de densidade, um segundo botão `Densidade` a remove.
* `Grupo de faces` - Ativa para usar ou ignorar os grupos de faces para orientar o quad remesher.
* `Relaxar` - Ativa para relaxar automaticamente as bordas dos grupos de faces durante o remalhamento. Se você já relaxou/suavizou as bordas dos grupos de faces, desative esta opção.
* `Controle Relaxar` - Um controle de atalho para relaxar as bordas dos grupos de faces.
* `Bordas duras` - Ativa para tentar manter as bordas duras.
* `Reprojetar vértice` - Ativa para reprojetar a nova topologia na malha de entrada.
* `Simetria` - Ativa para ter um resultado simétrico. Observe que a simetria é sempre calculada em torno do eixo X do mundo, então deixe o modelo na origem se espera um resultado simétrico.
* `...` - Janela de ajustes do Quad Remesher.

#### Menu de ajustes do Quad Remesher {#quad-remesher-settings-menu}

O botão `...` no fim da barra de ferramentas superior abre uma janela com os demais ajustes:

* `Contagem adaptativa de quads` - Ativa o uso de quads menores nas áreas de curvatura acentuada e maiores nas de curvatura suave.
* `Tamanho adaptativo` - Define o grau de adaptação. 100% permite a adaptação máxima de tamanho; com 0%, os quads ficam uniformes.

::: tip

Uma receita para um bom remalhamento em quads com o mínimo de artefatos:

* Crie grupos de faces na malha para definir o fluxo de quads ideal.
* Relaxe os grupos de faces para ter bordas suaves.
* Dizime. Isso garante que não haja faces finas ou distorcidas na borda dos grupos de faces. Nos ajustes de Dizimar, deixe o grupo de faces ativado: assim as arestas dos triângulos seguem exatamente as bordas dos grupos de faces.

Nas opções do remalhamento em quads, deixe Relaxar desativado (você já relaxou a malha) e você deve ter bons resultados.

:::

### ![](/icons/tool_select.webp) Selecionar {#select}
Use os modos de forma (`Laço`, `Retângulo`, `Elipse`) para selecionar objetos na cena. `Desmarcar` remove objetos da seleção.

### ![](/icons/tool_lattice.webp) Grade {#lattice}
Deforma um objeto com uma gaiola de pontos de controle em volta dele, em vez de esculpir a superfície. Mover alguns pontos da gaiola dobra, torce ou estica o objeto inteiro de forma suave: ótimo para ajustar proporções ou fazer poses sem mexer na topologia. A deformação continua editável até você validá-la.

A barra de ferramentas da esquerda escolhe como você edita a gaiola:

* `Pontos` - Arraste diretamente os pontos e as arestas da gaiola. Toque em um ponto para selecioná-lo.
* `Vista` - Move a câmera sem editar a gaiola.
* `Relaxar` - Um pincel que relaxa os pontos da gaiola sob ele.
* `Elástico` - Um pincel que puxa os pontos da gaiola com uma atenuação elástica, como a ferramenta [Elástico](#elastic).
* `Gizmo` - Move, gira e redimensiona os pontos selecionados com o gizmo. O modo Sub dele é `Pivô`.
* `Laço` - Seleciona pontos da gaiola com um laço; `Desmarcar` os remove da seleção.

A janela de formas também tem `Raio suave`, que faz o arrasto de um ponto mover também os pontos vizinhos (em células da grade; 0 move só a seleção), e `Inverter seleção`.

Uma barra de ferramentas no topo da viewport tem:

* `Validar` - Aplica a deformação ao objeto e remove a gaiola.
* `Redefinir` - Remove a gaiola e a deformação dela.
* `Opacidade` - A opacidade de exibição da gaiola.
* `Lado do espelho` - Com simetria, alterna qual lado espelhado da gaiola é mostrado e pode ser escolhido, com uma `Opacidade` própria para o lado oculto.
* `Pontos da grade` - Quais pontos da gaiola podem ser movidos: a grade inteira, a superfície e o ponto central, ou só a superfície.
* `Rigidez` - O quanto a deformação é rígida, de suave (0%) a rígida e linear (100%).
* `Atenuação` - Até onde a deformação vai diminuindo fora da gaiola.
* `Alinhar` - Alinha a gaiola com o objeto ou com o mundo.
* `X`, `Y`, `Z` `Divisão` - O número de células da gaiola em cada eixo. O botão de modo ao lado define como eles se relacionam: `x = y = z` usa a mesma quantidade nos 3 eixos, `Uniforme` mantém o mesmo espaçamento entre os pontos em todos os eixos, e `Personalizado` permite definir cada eixo livremente.

#### Ajustes da Grade {#lattice-settings}
* `Velocidade de rotação` - As mesmas opções de rotação da ferramenta [Mover](#move-settings), usadas ao arrastar os pontos da gaiola.

### ![](/icons/tool_view.webp) Vista {#view}
Esta "ferramenta" não faz nada em especial: é só um jeito de olhar o modelo sem alterar a cena.

#### Ajustes de Vista {#view-settings}
Enquanto a ferramenta Vista está ativa, estes ajustes substituem algumas opções de exibição, para você ter uma vista limpa ao apresentar ou conferir o modelo:

* `Primitiva (Editar)`, `Repetidor (Editar)`, `Luz (Editar)`, `Câmera (Editar)` - Permitem editar primitivas, repetidores, luzes e câmeras na viewport enquanto a ferramenta Vista está ativa. Desative para não mover as alças deles sem querer.
* `Atalho da câmera (sempre)` - Sempre mostra os botões de atalho da câmera na viewport.
* `Mostrar máscara`, `Contorno`, `Escurecer objetos não selecionados` - Mostra a máscara, o contorno dos objetos selecionados ou escurece os objetos não selecionados. `Auto` segue o seu ajuste habitual; `Não` e `Sim` forçam a opção.
* `Mostrar linha (Simetria)`, `Mostrar plano (Simetria)` - Mostra a linha ou o plano de simetria, com as mesmas opções `Auto`, `Não` e `Sim`.
* `Ícone` - Mostra na viewport os ícones de grupos, repetidores, luzes e câmeras, e a hierarquia, com as mesmas opções.


## Menu de contexto da caixa de ferramentas {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Um clique com o botão direito ou um toque longo em uma ferramenta da caixa de ferramentas abre um menu de contexto. Esse menu tem as seguintes opções:

* `Salvar` - Salva as alterações que você fez na ferramenta.
* `Clonar` - Duplica a ferramenta em um novo atalho de ferramenta.
* `Último salvamento` - Volta para a versão salva anteriormente da ferramenta.
* `Ícone` - Muda o ícone da ferramenta. Quando a ferramenta tem um ícone personalizado, este botão o remove.
* `→ ...` - Move a ferramenta para outra pasta da caixa de ferramentas, ou para uma nova.
* `Redefinir` - Redefine a ferramenta para os padrões.

Ferramentas clonadas também têm `Renomear` e `Apagar`.
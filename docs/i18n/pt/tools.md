# ![](/icons/toolbox.webp) Ferramentas {#tools}

![](/images/tools_menu.webp)

::: tip
Vá para [Ferramentas](#tools-1) para descrições das ferramentas individuais.
:::

## Visão geral {#overview}

As ferramentas são selecionadas na `Caixa de ferramentas` à direita e controladas com os `Controles da ferramenta` à esquerda. Configurações extras são encontradas no menu `Settings`, o primeiro ícone no menu superior direito.

Ferramentas de pincel têm controles de tamanho e intensidade. Ferramentas de seleção têm controles para vários estilos de seleção. A parte inferior dos controles da ferramenta tem atalhos para operações usadas com frequência (Smooth, Mask, Hide, Gizmo, Color, Alpha).

As ferramentas do Nomad são codificadas por cor na caixa de ferramentas:

* <span class=brush>**Ferramentas de pincel**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Ferramentas de mover**</span> (Move, Drag)
* <span class=mask>**Ferramentas de máscara**</span> (Mask, SelMask)
* <span class=paint>**Ferramentas de pintura**</span> (Paint, Smudge)
* <span class=flatten>**Ferramentas de achatamento**</span> (Flatten, Planar)
* <span class=pinch>**Ferramentas de pinçar**</span> (Crease, Pinch)
* <span class=selection>**Ferramentas baseadas em seleção**</span> onde primeiro é desenhada uma máscara 2D e depois uma operação acontece (Trim, Split, Project)
* <span class=creation>**Ferramentas de criação**</span> (Tube, Lathe, Insert)
* <span class=transform>**Ferramentas de transformação**</span> (Transform, Gizmo)
* <span class=misc>**Ferramentas diversas**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Ferramenta de visualização**</span>



Muitas dessas ferramentas podem ser personalizadas com diferentes comportamentos de pincel, pressão, texturas etc via o menu [Stroke](stroke.md). 


### Controles do pincel {#brush-controls}

A barra de ferramentas esquerda tem controles deslizantes para raio e intensidade, e depois controles específicos da categoria da ferramenta, explicados abaixo.

![](/images/tool_left_panel.webp)

::: tip
O controle deslizante de intensidade para muitas ferramentas pode ir acima de 100%, vale a pena experimentar!
:::

### Submodo {#sub-mode}
O botão diretamente abaixo do controle deslizante de intensidade é o botão `Sub`. Seu rótulo e função mudam com cada ferramenta e, quando pressionado, invocará um comportamento alternativo, geralmente oposto. Por exemplo, para [Paint](#paint) ele invocará um modo Erase, para [Crease](#crease) criará bordas elevadas em vez de vincos etc.

Por padrão ele funciona como um botão “pegajoso”; ou seja, você pode mantê‑lo pressionado para invocá‑lo temporariamente, e quando soltar ele será desligado. Se você tocar nele, o modo sub será ativado permanentemente.

### Atalhos {#shortcuts}
Na parte inferior da barra de ferramentas esquerda há atalhos para [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Por padrão todos funcionam como botões “pegajosos”; ou seja, você pode mantê‑los pressionados para invocá‑los temporariamente, e quando soltar serão desligados. Se você tocar, aquele modo de atalho será ativado permanentemente.

### Controles de seleção {#selection-controls}

As ferramentas [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) e [Hide](#hide) usam controles semelhantes para selecionar áreas da malha.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Uma forma desenhada à mão livre
* `Polygon` - Uma forma fechada definida por uma combinação de curvas e/ou linhas retas. Veja [Edição de forma](#shape-editing) abaixo para mais informações.
* `Curve` - (Project apenas) - Uma curva desenhada à mão livre para a projeção
* `Path` - (Project apenas) - Uma curva definida por pontos. Veja [Edição de forma](#shape-editing) abaixo para mais informações.
* `Line` - Arraste uma linha para definir um segmento planar. Por padrão ela operará na malha imediatamente; desligue o auto validate se você não quiser isso (toque longo ou deslize no ícone de linha)
* `Rect` -  Arraste uma linha diagonal, isso definirá os cantos de um retângulo. Toque longo ou deslize para revelar opções de auto validate, forçar forma quadrada e fazer com que o primeiro clique seja o centro do retângulo.
* `Ellipse` - Arraste uma linha diagonal, isso definirá o tamanho de uma elipse. Toque longo ou deslize para revelar opções de auto validate, forçar forma circular e fazer com que o primeiro clique seja o centro da elipse.
* `Flip` - inverte a máscara da forma ou a direção da ferramenta project.

A maioria das ferramentas tem uma opção de auto validate, o que significa que a operação acontecerá assim que você terminar de desenhar a forma. Quando o auto validate está desligado, um botão verde será desenhado ao lado da forma que executará a operação. Isso permite editar a forma, ajustar a visualização e, quando estiver pronto para usar a forma, pressionar o botão verde.

### Edição de formas {#shape-editing}
A edição de polígono e a edição de curva se comportam de maneira semelhante:

* Para começar, arraste uma linha para definir 2 pontos, depois arraste a partir do meio da linha para definir um polígono ou curva.
* Clique nos pontos para alternar entre suave e afiado. 
* Clique e arraste nas seções de curva ou linha para criar novos pontos.
* Para excluir um ponto, arraste um ponto para o seu vizinho até que ele fique vermelho.
* O ícone de lixeira no canto do ícone do polígono ou caminho excluirá a forma.

### Menu de configurações {#settings-menu}

Muitas ferramentas têm configurações extras que são encontradas no menu settings, o primeiro ícone no menu superior direito:

![](/images/tools_settings_menu.webp)

## Ferramentas {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Argila {#clay}
A ferramenta Clay é útil para construir sua escultura. `Sub` removerá material da sua escultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Pincel {#brush}
O pincel padrão. `Sub` removerá material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Mover {#move}
A área sob o pincel ficará presa ao pincel, permitindo deformação elástica. A seleção é mantida durante o movimento, então se você afastar o pincel e depois movê‑lo de volta para onde começou, não verá deformação.

O modo sub é `Normal` e moverá a área sob o pincel ao longo da normal da superfície.

Este pincel é bom tanto para deformação em grande escala quanto para deformação pequena e cuidadosa.

#### Configurações de Mover {#move-settings}

* `Radius (Background)` - Quão longe da borda de um modelo você pode estar e ainda esculpir, útil ao trabalhar na silhueta de um objeto. 
* `Same-side vertex only` - Ignorar vértices que apontam na direção oposta à deformação.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Arrastar {#drag}
A área sob o pincel ficará presa ao pincel, permitindo deformação elástica. Diferente do pincel Move, a seleção é continuamente atualizada durante o traço, então é possível fazer objetos mais longos, como cobras, especialmente quando a Topologia Dinâmica está ativada.

O modo sub é `Normal` e moverá a área sob o pincel ao longo da normal da superfície.

Este pincel é bom para mudanças de forma mais soltas e gestuais.

#### Configurações de Arrastar {#drag-settings}

* `Radius (Background)` - Quão longe da borda de um modelo você pode estar e ainda esculpir, útil ao trabalhar na silhueta de um objeto. 
* `Same-side vertex only` - Ignorar vértices que apontam na direção oposta à deformação.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Suavizar {#smooth}
Suaviza a área fazendo a média das posições dos pontos. Esta ferramenta é altamente dependente da densidade de polígonos.
Então, se você tiver muitos polígonos, o alisamento será menos eficaz.

O modo sub é `Relax`, que apenas suaviza o wireframe, mas tenta reter os detalhes geométricos.

#### Configurações de Suavizar {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grupo de faces {#smooth-facegroup}

* `Relax` - Vai suavizar as bordas dos facegroups. Use intensidade maior que 100% para suavizar rapidamente as bordas. `Auto` suavizará apenas se a visualização de facegroup estiver ativada, `Off` desativará, `On` ativará. 

##### Vértice {#vertex}
* `Sticky vertex on border` - Para malhas com bordas abertas, por exemplo um plano, é possível suavizar os cantos. Ativar esta opção bloqueará as bordas abertas.
* `Relax` - o mesmo que o modo alternativo relax na barra de ferramentas esquerda.
* `Stable smoothing` - Tenta tornar o alisamento independente da topologia. Funciona melhor com densidade de topologia variável e com um valor alto de intensidade de alisamento.

##### Pintura {#painting}
* `Screen Smoothing` - Use esta opção para obter alisamento independente da topologia, mesmo em contagens altas de polígonos.
* `Screen samples` - A qualidade do alisamento; valores mais altos serão mais suaves, mas mais lentos.

::: tip
Densidades mais altas de polígonos podem exigir aumentar a intensidade acima de 100%. Valores muito altos (300%, 500%) também podem funcionar bem como ferramenta de escultura, forçando áreas a ficarem planas e suaves rapidamente sob o pincel, como bater argila com um malho!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Máscara {#mask}
Esta ferramenta permite mascarar vértices. Vértices mascarados são protegidos de escultura ou pintura. 

O modo sub é `Unmask` e apagará onde a máscara foi pintada.

Semelhante a seleções em programas de pintura 2D, máscaras podem ser pintadas com um pincel ou feitas com seleções de forma, desfocadas ou acentuadas. 

Diferente de programas de pintura 2D, elas também podem ser feitas via facegroups, e máscaras podem ser usadas para criar nova geometria via operações de extrusão/extração. 

![](/videos/tool_mask1.mp4)

 Uma barra de ferramentas aparecerá na parte superior da viewport com controles extras. 

![](/images/tool_mask_toolbar.webp)

O título da barra pode ser tocado para expandir/recolher, ou a seta no canto superior direito pode ser tocada para movê‑la para o topo ou base da interface.

| Ação                                              | Descrição                                                                                  |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear             | Limpa a máscara                                                                            |
| ![](/icons/invert.webp)        Invert            | Inverte a máscara                                                                          |
| ![](/icons/sharpen.webp)       Sharpen           | Acentua a borda da máscara                                                                 |
| ![](/icons/blur.webp)          Blur              | Desfoca a borda da máscara                                                                 |
|                                 Blur ->           | Arraste para a esquerda/direita para desfocar interativamente a máscara                   |
| ![](/icons/culling.webp)       Front             | Alterna para mascarar apenas vértices voltados para a frente                              |
|                                 Convert           | Converte a máscara em um facegroup                                                        |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Quando ativado, os facegroups serão mostrados; tocar em um facegroup irá mascará‑lo       |
|                                 On tap (mask)     | Quando ativado, tocar em uma “ilha” de polígonos mascarados ou não mascarados fará um preenchimento daquela ilha. |
| ![](/icons/vertex.webp)        Connected         | Quando ativado, permite que traços de máscara afetem apenas topologia conectada.          |

##### Gesto rápido de Máscara {#mask-quick-gesture}
Você pode realizar gestos ao estilo ZBrush enquanto segura o botão de máscara rápida na barra esquerda:
| Ação   | Gesto (segure o atalho inferior esquerdo) |
| :----: | :----------------------------------------: |
| Invert | Toque no fundo                             |
| Clear  | Arraste no fundo                           |
| Blur   | Toque na área mascarada                    |
| Sharpen| Toque na área não mascarada                |


#### Configurações de Máscara {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - O menu de configurações de Mask é usado principalmente para criar geometria a partir da máscara. Por causa disso, o comportamento padrão é pré‑visualizar como será a nova geometria. Você pode escolher não ter preview, ter preview de extract, de split e se essa geometria será mostrada em modo raio‑X.

##### Espessura {#thickness}
* `Height` - A altura da forma extraída. O ícone Plus/Minus permite alternar entre extrusão para fora, para dentro ou centralizada. 
* `Height/Height+Mask` - Alterna entre a altura ser constante ou se partes desfocadas da máscara devem afetar a altura, permitindo formas suaves e com alturas variadas. 

##### Suavidade {#smoothness}
Quando ativo, suaviza a borda da forma extraída; funciona melhor com contagens altas de polígonos. 
* `Iterations` - A quantidade de suavização aplicada. Valores altos produzirão bordas curvas muito suaves, mas começarão a se afastar da forma da máscara.
* `All/Sharp border/Borders only` - A suavização pode funcionar em todas as direções, suavizando tanto os lados quanto o topo da forma extraída; ou suavizar o topo e os lados, mas manter uma borda afiada; ou apenas suavizar a borda, deixando a superfície superior inalterada.

##### Loop de borda (lado) {#edge-loop-side}
* `Auto Edge-loop (side)` - Calculará a quantidade de divisões nos lados da forma extraída para fazer polígonos quadrados que correspondam aos polígonos da área mascarada. Quando desativado, você pode definir o número de edge loops com o controle deslizante.

----

##### Extrair {#extract}
* `Extract` - Cria a geometria extraída.
* `Closing action` - Como o extract deve se comportar. “None” duplicará os polígonos mascarados em uma nova forma. “Fill” fará o mesmo e tentará fechar a superfície de trás. “Shell” extrudará na quantidade definida em “thickness” e é o padrão.

::: tip

Se o preview estiver em modo “Extract” com “X-ray” ativado, clicar no botão Extract pode ser confuso no início. Como o menu está ativo, ele tentará pré‑visualizar uma extração na sua nova forma e colocar a superfície original em raio‑X. Porém, como você não tem máscara na nova superfície, ele não pode pré‑visualizar a extração, e o Nomad avisará “Nothing to Extract!”.

Isso é normal; feche o menu de configurações de máscara para ver a nova forma e a original, e selecione a superfície original novamente se precisar limpar a máscara ou desenhar novas máscaras.
:::

##### Dividir {#split-mask}
* `Split` - Extrairá as regiões mascaradas E não mascaradas em novas formas. 
* `Closing action (masked)` - Como a extração da parte mascarada deve se comportar. “None” duplicará os polígonos mascarados em uma nova forma. “Fill” fará o mesmo e tentará fechar a superfície de trás. “Shell” extrudará na quantidade definida em “thickness” e é o padrão.
* `Closing action (unmasked)` - Como a extração da parte não mascarada deve se comportar. “None” duplicará os polígonos não mascarados em uma nova forma. “Fill” fará o mesmo e tentará fechar a superfície de trás. “Shell” extrudará na quantidade definida em “thickness” e é o padrão.
* `Sync border` - Garante que a borda entre as formas extraídas mascarada e não mascarada permaneça próxima. Quando desativado, como a operação shell extrudará cada face ao longo de sua normal, pode se formar um vão entre as formas.

##### Esculpir em baixo-relevo {#carve}
* `Carve` - No modo padrão, se comporta como se você tivesse recortado a superfície pela quantidade de “thickness”, como cortar uma seção de casca de laranja. 



### ![](/icons/tool_maskSelector.webp) Seleção de máscara {#selection-mask}
Esta ferramenta é em grande parte semelhante à ferramenta [Mask](#mask); a principal diferença é que você não usa traços para pintar a máscara, mas sim os [Controles de seleção](#selection-controls).

O modo sub é `Unmask` e apagará a máscara usando os controles de seleção.

Selection mask compartilha as mesmas configurações de ferramenta que a ferramenta `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Pintar {#paint}
Aplica cor e propriedades de material. Para saber mais sobre material, visite a seção [Painting](painting.md).

O modo sub é `Erase` e removerá a pintura.

#### Configurações de Pintar {#paint-settings}
* `Layer fitering` - Funciona como o bloqueio de alfa de camada no Photoshop ou Procreate. Se você estiver pintando em uma camada, quando isso estiver ativado, só poderá modificar onde já existe pintura; áreas não pintadas serão protegidas.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Borrar {#smudge}
Borra propriedades de cor e material. O menu de configurações de smudge contém um controle deslizante `Quality`; valores mais baixos significam traços mais rápidos.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Achatador {#flatten}
Achata a área projetando os pontos no plano médio.

O modo sub é `Fill` e definirá um plano ajustado pelo ponto mais alto, tendendo a puxar os pontos para cima.

#### Configurações de Achatador {#flatten-settings}

* `Lock plane direction` - Usa a direção do plano calculada no primeiro clique. Por padrão está desativado.
* `Lock plane origin`- Usa o primeiro clique como o centro do plano. Por padrão está desativado.

Quando um ou ambos estão desativados, o flatten pode ser gradualmente aprofundado ou o ângulo do plano alterado usando traços longos que se movem sobre diferentes profundidades e curvaturas. Isso, em conjunto com as opções de amostragem de área do menu de pincel, pode oferecer controle muito preciso.

::: tip
Ao trabalhar em áreas de alta curvatura, por exemplo tentando achatar as bochechas, mas a ferramenta continua afetando as laterais do nariz, tente criar uma máscara para proteger áreas que o pincel flatten não deve afetar.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Torna os pontos planares projetando‑os no plano médio, mas com menos acúmulo que o pincel flatten. Isso cria superfícies limpas de bordas duras. Traços rápidos empurrarão e puxarão mais a superfície; traços mais lentos que começam em áreas já planares e se expandem manterão melhor o plano.

O modo sub é `Fill` e definirá um plano ajustado pelo ponto mais alto, tendendo a puxar os pontos para cima.

Planar é na verdade a mesma ferramenta que `Flatten`, mas com `Lock plane direction` ativado, o que significa que tenderá a criar superfícies mais estáveis e de bordas duras, enquanto flatten pode ser mais escultural e usado para criar áreas semi‑planas.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Vincar {#crease}
Ferramentas de crease podem ser úteis para esculpir pequenos cortes ou amassados.

O modo sub é `Invert` e criará um vinco elevado.

#### Configurações de Vincar {#crease-settings}

* `Pinch factor` - Quanto puxar vértices lateralmente em direção ao traço. Se pinch estiver em 1 e offset em 0, a superfície não terá mudanças de profundidade, apenas mudanças de topologia, puxando arestas em direção ao traço.
* `Offset factor` - Quanto empurrar/puxar vértices em profundidade. Se pinch estiver em 0 e offset em 1, serão feitos vincos profundos ou amassados elevados, mas parecerão irregulares porque não há geometria suficiente sendo puxada em direção ao vinco para definir com precisão os lados ou o fundo do vinco.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinçar {#pinch}
Esta ferramenta pode ser usada para afiar bordas.

O modo sub é `Invert` e espalhará os vértices.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Cortar {#trim}
A ferramenta Trim funciona removendo um pedaço da sua malha e oferece opções de como processar o espaço deixado para trás. Ela usa os [Controles de seleção](#selection-controls) para definir o corte.

::: tip
Como esta ferramenta projeta a partir da câmera, você receberá um aviso se a câmera estiver em modo perspectiva.

No modo ortográfico, o corte feito através da malha é paralelo à visualização, que é o que as pessoas geralmente esperam. Quando feito com uma câmera em perspectiva, o corte parecerá diferente no lado distante do objeto em comparação ao lado próximo.
:::

#### Configurações de Cortar {#trim-settings}

* `Stroke painting` - Se a pintura estiver ativada no menu paint, a região preenchida será pintada com a cor atualmente selecionada.
* `Boolean` - Preenche o buraco do corte usando uma região de polígonos quad. A região preenchida será plana.
* `Legacy` - Preenche o buraco do corte com uma região triangulada. A região preenchida será plana.
* `Fill` - Preenche o buraco com uma região triangulada. A região preenchida será uma superfície curva, como o filme de uma bolha de sabão.
* `None` - Não preenche o buraco.
* `Boolean Detail Shape` - O tamanho aproximado dos quads e triângulos usados no lado da forma do corte.
* `Boolean Detail Hole` - O tamanho aproximado dos triângulos ou polígonos usados no buraco preenchido do corte. 
* `Legacy Detail` - O tamanho aproximado dos triângulos usados no corte.
* `Legacy Hole smoothing` - Quanto os triângulos são relaxados na área preenchida.
* `Legacy Threshold espilon` - Um valor que pode ser ajustado para melhorar o algoritmo de preenchimento de buracos legacy.
* `Fill Detail` - O tamanho aproximado dos triângulos usados no corte.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Separar {#split}
Semelhante à ferramenta [Trim](#trim), exceto que enquanto Trim descarta a seleção, Split manterá a seleção como um novo objeto.

#### Configurações de Separar {#split-settings}

* `Stroke painting` - Se a pintura estiver ativada no menu paint, a região preenchida será pintada com a cor atualmente selecionada.
* `Boolean` - Preenche o buraco do split usando uma região de polígonos quad. As regiões preenchidas serão planas.
* `Legacy` - Preenche o buraco do split com uma região triangulada. As regiões preenchidas serão planas.
* `Fill` - Preenche os buracos com uma região triangulada. As regiões preenchidas serão superfícies curvas, como o filme de uma bolha de sabão.
* `None` - Não preenche os buracos.
* `Boolean Detail Shape` - O tamanho aproximado dos quads e triângulos usados no lado da forma do split.
* `Boolean Detail Hole` - O tamanho aproximado dos triângulos ou polígonos usados no buraco preenchido do split. 
* `Legacy Detail` - O tamanho aproximado dos triângulos usados no split.
* `Legacy Hole smoothing` - Quanto os triângulos são relaxados na área preenchida.
* `Legacy Threshold espilon` - Um valor que pode ser ajustado para melhorar o algoritmo de preenchimento de buracos legacy.
* `Fill Detail` - O tamanho aproximado dos triângulos usados no split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Projetar {#project}
A ferramenta Project se parece com a ferramenta [Trim](#trim), mas não exclui nem cria geometria; ela apenas move vértices para se conformarem à seleção.

![](/videos/tool_project.mp4)

::: tip
Se você usar Project enquanto estiver em uma layer, poderá misturar entre a forma original e a projetada com o controle deslizante da layer.
:::

### ![](/icons/tool_layer.webp) Camada {#layer}
Eleva a superfície, mas limita a altura.

Se você mantiver o lápis pressionado e continuar pincelando sobre uma área, Layer elevará até certa altura e não irá além, ao contrário de outras ferramentas que continuarão acumulando altura.

Note que, por padrão, o limite é definido apenas por traço! Se você iniciar um novo traço, ele será construído a partir da nova altura da superfície.

Para definir uma altura máxima constante em muitos traços, use a ferramenta Layer com o sistema de [Layers](layers.md) do Nomad.

Crie uma layer e use esta ferramenta. A altura máxima agora é definida pela layer, então você pode aplicar muitos traços de pincel e a altura será sempre a mesma.

`Sub` usará uma profundidade mínima, criando sulcos.

#### Configurações de Camada {#layer-settings}

* `Use layer data` - Quando ativo, e quando uma layer está selecionada, usa os dados da layer para definir a altura máxima.
* `Inflate`- Quando ativo, ajusta a direção em que layer funciona para obter resultados mais suaves.
* `Relax (Normal)` - A quantidade de suavização aplicada às normais.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflar {#inflate}
Move os vértices ao longo de suas próprias normais. `Sub` moverá os vértices ao longo de suas normais invertidas.

#### Configurações de Inflar {#inflate-setings}
* `Relax (Normal)` - A quantidade de suavização aplicada às normais.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Empurrar {#nudge}
Move ou “borrifa” pontos na direção do traço.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Carimbo {#stamp}

Clique e arraste para elevar uma área da escultura no formato do Alpha selecionado.

Isto é simplesmente a ferramenta [Brush](#brush) com o tipo de stroke definido para `Lock + radius`. 

`Sub` empurrará o stamp para dentro em vez de puxá‑lo para fora da superfície.

::: tip
Stamp geralmente funciona melhor com geometria de alta resolução. Se você procurar online por “wrinkles alpha”, “pores alpha”, “scales alpha” etc., essas texturas alpha e Stamp podem ser uma ótima maneira de adicionar detalhes orgânicos a uma escultura de personagem.

Os dois modos de stroke são úteis para coisas diferentes. 

* `Lock + radius` tem uma *altura* fixa; arrastar ajusta a largura e a rotação do stamp. Bom para texturas de pele em que precisam ter a mesma profundidade/altura, mas rotações e escalas diferentes para esconder padrões repetidos.
* `Lock + intensity` tem uma *largura* fixa; arrastar ajusta a rotação e a altura do stamp. Bom para rebites, em que todos precisam ter o mesmo tamanho, mas rotações e alturas diferentes. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Apagar camada {#delete-layer}
Esta ferramenta pode redefinir layers localmente; você precisa de uma layer ativa, caso contrário nada acontecerá.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tubo {#tube}
Crie um tubo desenhando uma curva. 
![](/images/tool_tube_new.webp)

Uma vez criado o tubo, o caminho pode ser editado em espaço 3D usando controles semelhantes às ferramentas padrão de [Edição de forma](#shape-editing) e edição de curva. 

![](/videos/tool_tube.mp4)

#### Barra lateral esquerda do Tubo {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

A barra de ferramentas esquerda tem as seguintes opções:

* `Sync` - Se o tubo atual for instanciado e houver nós filhos do tubo que diferem entre as instâncias, isso irá resincronizá‑los.
* `Snap` - Quando ativo, os modos curve e path irão se encaixar em outros objetos enquanto você desenha. Quando inativo, o primeiro ponto irá se encaixar, depois o resto do tubo será desenhado naquela profundidade. Tem um pequeno menu suspenso:
    * `Offset` - Define a profundidade do snap; 0% fará com que o meio da seção transversal do tubo se encaixe na superfície, valores positivos o levantarão da superfície, valores negativos o abaixarão.
* `Curve` - Esboce livremente um tubo. Tem um pequeno menu suspenso:
    * `Auto-validate` - Criará o tubo assim que o traço for concluído. Quando desativado, um círculo verde de validação ficará visível próximo ao caminho da curva; pressione‑o para validar ou use o link `Reset` que aparece neste menu para remover o caminho.
    * `Closed` - transforma o tubo em um loop.
    * `Screen` - Disponível apenas quando Auto-validate está desativado. Quando ativo, o caminho é “fixado” na tela, permitindo mover a visualização e o objeto enquanto o caminho permanece no lugar. Quando inativo, o caminho faz parte da cena 3D e se moverá com a câmera e os objetos.
    * `Accuracy` - Quantos pontos de curva serão usados para converter o caminho desenhado em um tubo. 0% usará o menor número de pontos, mas perderá pequenas mudanças de curvatura. 100% será muito preciso e usará muitos pontos.
* `Path` - Cria um tubo clicando para definir pontos de curva. Toque no círculo verde para validar o caminho. Tem um pequeno menu suspenso:
    * `B-spline` - Um método alternativo de desenho de curva em que os pontos geralmente não ficam diretamente sobre a curva, mas podem produzir resultados mais suaves que o método padrão.
    * `Closed` - transforma o tubo em um loop
    * `Screen` - Quando ativo, o caminho é “fixado” na tela, permitindo mover a visualização e o objeto enquanto o caminho permanece no lugar. Quando inativo, o caminho faz parte da cena 3D e se moverá com a câmera e os objetos.

##### Barra superior do Tubo {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Quando um tubo é selecionado, uma barra de ferramentas aparecerá na parte superior da viewport com controles extras. Clique no título da barra para recolher/expandir a barra de ferramentas e clique na seta no canto superior direito para mover a barra para o topo ou base da viewport.

* `Validate` - converte o tubo em polígonos regulares para que possa ser esculpido.
* `Edit` - exibe os pontos da curva para que possam ser manipulados
* `Mirror` - adiciona um repetidor de espelho como pai desta curva
* `Snap` - encaixa pontos da curva em superfícies próximas
* `Closed` - Une o início e o fim da curva para formar um loop
* `B-spline` - Alterna entre interpolação Catmull-rom e B-spline.
* `Cap` - Alterna entre tampas em ambas as extremidades do tubo, apenas no início ou fim, ou sem tampas.
* `Hole` - Adiciona espessura ao tubo, convertendo‑o em um cano. Alterna entre ter um furo em ambas as extremidades, apenas no fim ou sem furos. 
* `Radius` - Alterna entre raio uniforme, raio no início e fim ou raio por ponto de curva. Estes são editados com alças laranja na curva.
* `Twist` - Alterna entre sem torção, torção uniforme, torção no início e fim ou torção por ponto de curva. Estes são editados com alças rosas na curva.
* `Profile` - Alterna entre sem perfil (portanto, perfil circular), perfil uniforme, perfil no início e fim ou perfil por ponto.
* `Profile edit` - Exibe um editor de perfil. Funciona de forma semelhante às ferramentas de [Edição de forma](#shape-editing), pode salvar e carregar predefinições de perfil e tem uma alternância para permitir editar o perfil em espaço 3D.
* `Spiral` - Alterna um menu para adicionar uma torção em espiral ao tubo. Este menu tem opções para `Twist Angle`, `Offset`, `Scale` e `Angle offset`.
* `X Divisions` - o número de divisões ao redor do tubo; 4 divisões farão um tubo quadrado, por exemplo. 
* `Constant density` - quando ativo, manterá os polígonos quadrados; quando desativado, permitirá definir `Y divisions` ao longo do comprimento do tubo.
* `...` - Menu de configurações do Tube.

#### Alternância de apagar ponto da curva {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Abaixo da barra de ferramentas há uma alternância de exclusão de ponto de curva. Quando você arrasta um ponto de curva próximo a outro, ele ficará vermelho, indicando que, se soltar, o ponto será excluído. Se você estiver fazendo pequenas edições e não quiser excluir pontos, este botão desativará o comportamento de exclusão.

#### Configurações de Tubo {#tube-settings}
* `Primitive` - botões para permitir ativar/desativar UVs ou validar o tubo.
* `Post subdivision` - um atalho para definir o nível de multiresolution antes de validar.
* `Linear subdivision` - atalho para definir o nível de subdivisão linear antes de validar. 
* `Division X` - igual a X Divisions na barra de ferramentas.
* `Division Y` - igual a Y Divisions na barra de ferramentas.
* `Curve (Repeater)` - converte o tubo em um [Curve Repeater](scene.md#curve)

::: tip
Divisions em 4 e Post subdivision em 3 farão tubos de pontas arredondadas suaves, bons para vermes, cobras, partes do corpo.
:::


### ![](/icons/tool_lathe.webp) Torno {#lathe}
Crie uma superfície de revolução desenhando uma curva.

Esta ferramenta é ótima para formas como vasos, taças de vinho.

![](/videos/tool_lathe.mp4)

#### Barra lateral esquerda do Torno {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

A barra de ferramentas esquerda tem as seguintes opções:

* `Sync` - Se o lathe atual for instanciado e houver nós filhos do lathe que diferem entre as instâncias, isso irá resincronizá‑los.
* `Fixed` - Quando ativado, o centro do lathe é fixo e exibido na tela. Esta linha central tem pontos de edição que podem ser ajustados. Quando desativado, o centro do lathe será atualizado dinamicamente para coincidir com o início e o fim da curva desenhada.
* `Curve` - Desenhe o perfil do lathe em um traço. Tem um pequeno menu suspenso:
    * `Auto-validate` - Quando ativado, o lathe será criado quando o lápis for levantado da tela. Quando desativado, um círculo verde próximo à curva pode ser pressionado para criar o lathe. A curva pode ser excluída com o botão `Reset`.
    * `Closed` - Une o início e o fim da curva para formar um loop
    * `Screen` - Disponível apenas quando Auto-validate está desativado. Quando ativo, o caminho é “fixado” na tela, permitindo mover a visualização e o objeto enquanto o caminho permanece no lugar. Quando inativo, o caminho faz parte da cena 3D e se moverá com a câmera e os objetos.
    * `Accuracy` - Quantos pontos de curva serão usados para converter o caminho desenhado em um tubo. 0% usará o menor número de pontos, mas perderá pequenas mudanças de curvatura. 100% será muito preciso e usará muitos pontos.
* `Path` - Cria um lathe clicando para definir pontos de curva. Toque no círculo verde para validar o caminho. Tem um pequeno menu suspenso:
    * `B-spline` - Um método alternativo de desenho de curva em que os pontos geralmente não ficam diretamente sobre a curva, mas podem produzir resultados mais suaves que o método padrão.
    * `Closed` - transforma o tubo em um loop
    * `Screen` - Quando ativo, o caminho é “fixado” na tela, permitindo mover a visualização e o objeto enquanto o caminho permanece no lugar. Quando inativo, o caminho faz parte da cena 3D e se moverá com a câmera e os objetos.

#### Barra superior do Torno {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Quando um lathe é selecionado, uma barra de ferramentas aparecerá na parte superior da viewport com controles extras. Clique no título da barra para recolher/expandir a barra de ferramentas e clique na seta no canto superior direito para mover a barra para o topo ou base da viewport.

* `Validate` - converte o lathe em polígonos regulares para que possa ser esculpido.
* `Edit` - exibe os pontos da curva para que possam ser manipulados
* `Mirror` - adiciona um repetidor de espelho como pai deste lathe
* `Snap` - encaixa pontos da curva em superfícies próximas
* `Stable` - Quando ativado, o perfil da curva será parentado à linha central do lathe. Quando desativado, a linha central pode ser editada e não moverá a curva, permitindo formas mais complexas.
* `Focus` - Rotaciona a visualização para ver o perfil da curva perfeitamente plano para a câmera.
* `Closed` - Une o início e o fim da curva para formar um loop
* `Cap` - Se Closed estiver desativado, alterna entre tampas em ambas as extremidades do tubo, apenas no início ou fim, ou sem tampas.
* `Hole` - Adiciona espessura ao lathe, convertendo‑o em um cano. Alterna entre ter um furo em ambas as extremidades, apenas no fim ou sem furos. 
* `B-spline` - Alterna entre interpolação Catmull-rom e B-spline.
* `X Divisions` - o número de divisões ao redor do lathe; 4 divisões farão, por exemplo, um lathe com perfil quadrado. 
* `Constant density` - quando ativo, manterá os polígonos quadrados; quando desativado, permitirá definir `Y divisions` ao longo do comprimento do tubo.
* `...` - Menu de configurações do Lathe.

#### Configurações de Torno {#lathe-settings}
* `Primitive` - botões para permitir ativar/desativar UVs ou validar o tubo.
* `Post subdivision` - um atalho para definir o nível de multiresolution antes de validar.
* `Linear subdivision` - atalho para definir o nível de subdivisão linear antes de validar. 
* `Division X` - igual a X Divisions na barra de ferramentas.
* `Division Y` - igual a Y Divisions na barra de ferramentas.
* `Curve (Repeater)` - converte o perfil da curva em um [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Inserir {#insert}
Coloca um objeto na superfície de outro. No uso é semelhante à ferramenta stamp, mas para formas 3D completas.

Se você selecionar uma primitiva na barra de ferramentas esquerda, um clique‑arraste em qualquer superfície colocará uma primitiva onde você clicar; o arraste definirá o tamanho. Assim que terminar de arrastar, Insert trocará para o modo [Transform](#transform).

No modo Instance, arrastar criará e deslizará uma nova instância sobre a superfície. O tamanho será duplicado a partir da primeira forma; dessa forma você pode colocar muitas instâncias de mesmo tamanho de um objeto sobre outras superfícies.

Você não precisa apenas inserir primitivas! Selecione *qualquer* forma no outliner; se Insert estiver em modo Instance ou Clone, você pode arrastar cópias do objeto selecionado sobre qualquer outra superfície.

Se um objeto tiver um pivot personalizado, ele será usado como ponto de ancoragem. Veja o vídeo abaixo.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformar {#transform}
Move/Rotaciona/Escala um modelo diretamente com 1 e 2 dedos, geralmente sobre a superfície de outro objeto.

A ferramenta é controlada pela barra de ferramentas esquerda e tem 5 botões:

* `Snap` - encaixa o modelo em outras superfícies
* `Group` - Se o objeto selecionado tiver uma combinação de objetos e instâncias, isso permite determinar o comportamento da ferramenta.
* `Move` - Arrastar com um dedo moverá o objeto. Quando snap está ativo, isso deslizará o objeto ao longo da superfície sob o seu dedo.
* `Rotate` - Arrastar com um dedo rotacionará o objeto. Quando snap está ativo, rotacionará em torno da normal da superfície sob o seu dedo.
* `Scale` - Arrastar com um dedo escalará o objeto.

Transform pode ser usado para operar rapidamente 2 desses modos usando 2 dedos:

* Arraste um objeto para posicioná‑lo. Pare de mover o primeiro dedo, mas não o levante da tela.
* Toque o segundo dedo na tela enquanto mantém o primeiro dedo pressionado. À medida que o segundo dedo é arrastado, o objeto será escalado.
* Levante o segundo dedo e continue arrastando o primeiro dedo; o objeto estará novamente em modo move.

Você também pode mudar o segundo modo com um gesto de toque do segundo dedo:

* Arraste o objeto para posicioná‑lo, pare de mover, mas não levante o dedo da tela.
* Toque com o segundo dedo enquanto mantém o primeiro dedo pressionado
* A ferramenta é trocada para o modo rotation. Arraste o primeiro dedo para definir a rotação.
* Toque com o segundo dedo como antes; a ferramenta é trocada de volta para o modo move.

Isso oferece um fluxo de trabalho rápido para clonar objetos sobre outro, por exemplo rochas sobre uma paisagem. Note que o botão clone também está na barra de ferramentas esquerda para fácil acesso:

* Use a ferramenta transform para mover uma rocha para o lugar.
* Solte, pressione o botão clone
* Mova esta rocha, rotacione/escale conforme necessário
* Solte, pressione o botão clone
* Mova esta rocha, repita.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Esta ferramenta permite mover, rotacionar e escalar objetos, além de alterar pivots de objetos.

O manipulador da viewport tem as seguintes funções:

* `Move` - Arraste na linha+seta para mover em X/Y/Z. Arraste no ponto pêssego no meio do gizmo para transladar livremente em espaço de tela. Clique nos quadrados vermelho, verde, azul para transladar nos planos X/Y/Z.
* `Rotate` - Arraste nos círculos vermelho/verde/azul para rotacionar em X/Y/Z. Arraste a esfera dentro dos círculos para rotação livre.
* `Scale`- Arraste nos pontos externos vermelho/verde/azul para escalar em X/Y/Z. Arraste nos cones externos vermelho/verde/azul para escalar nos planos X/Y/Z. Arraste no círculo pêssego externo para escalar uniformemente.

![](/images/tool_gizmo.webp)

#### Nós e vértices {#nodes-and-vertices}

Todo objeto no Nomad é composto por um node e vértices:

* `Node` - O “manipulador” do objeto, que armazena sua translação, rotação e escala, chamado de matriz de transformação.
* `Vertices` - Os pontos que definem a superfície de um objeto; armazenam posição e informações de pintura.

Se você tiver uma caixa simples composta por 8 vértices, poderá transladá‑la modificando sua matriz de transformação ou modificando as posições dos vértices. Ao esculpir você geralmente quer modificar os vértices; ao mover objetos com o gizmo, geralmente quer modificar o node. O Nomad permite fazer ambos. 

#### Barra de ferramentas do menu esquerdo {#left-menu-toolbar}

A barra de ferramentas esquerda controla se o gizmo funcionará no node ou nos vértices, além de outras funções:

* `Clone` - Faz uma cópia independente do objeto atual, que pode ser arrastada com o gizmo.
* `Instance` - Faz uma cópia instanciada do objeto atual. Os objetos são vinculados, então mudanças de escultura em um aparecerão em todos os instanciados.
* `Group/Object/Vertex/Auto` - Define se o gizmo afetará o node ou os vértices de um objeto. O modo padrão “auto” tentará um melhor palpite. Se houver vários objetos parentados em uma hierarquia, “Object” moverá apenas o objeto atual; objetos filhos permanecerão estacionários. O gizmo também pode levar em conta máscara e simetria.
* `Pin` - Por padrão o gizmo se moverá para o pivot do objeto selecionado. Quando pin está ativado, o gizmo permanecerá onde está.
* `Align` - Alterna o pivot alinhado com o objeto atual ou alinhado com o mundo.
* `Snap rotation` - Ativa valores de rotação encaixados em incrementos; o valor de snap é exibido e pode ser editado quando o snap está ativo.
* `Snap translation` - Ativa valores de translação encaixados em incrementos; o valor de snap é exibido e pode ser editado quando o snap está ativo.
* `Pivot` - Quando ativado, o gizmo pode ser movido e rotacionado sem mover o objeto. Tem um menu extra explicado abaixo.

#### Pivô {#pivot}
Quando o modo pivot está ativo, um menu é exibido para permitir mudanças rápidas de pivot:

**Reset** 
* `Center` - Move o pivot para o centro do objeto
* `Bottom` - Move o pivot para a base do objeto
* `Align` - Redefine as rotações para ficarem alinhadas ao mundo.
* `Mask` - Move o pivot para o centro da região não mascarada.

**On Tap**
* `None` - não faz nada quando o objeto é tocado
* `Normal` - Move e rotaciona o pivot para alinhar onde a superfície é tocada
* `First` - Move (mas não rotaciona) o pivot para onde a superfície é tocada
* `Medial` - Move o pivot para o meio do objeto, sob onde a superfície é tocada.

#### Configurações de Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Matriz {#matrix}
* ![](/icons/target.webp) `Move origin` - Move o objeto para que seu pivot fique no centro da cena, chamado de origem.
* ![](/icons/bake.webp)  `Bake` - Congela o objeto onde está atualmente e define os valores de translate/rotate para 0 e scale para 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Faz com que os valores da matriz correspondam a onde o manipulador do gizmo está no mundo.
* ![](/icons/reset.webp) `Reset` - Um atalho que define os valores de translação para 0, rotação para 0 e escala para 1, movendo e rotacionando o objeto.

::: tip Bake vs bake to pivot
Crie uma caixa, selecione a ferramenta Gizmo, abra e fixe o menu de configurações. Por padrão, a translação e rotação são 0, a escala é 1.

Ative o modo pivot, mova o manipulador para um lado, desative o modo pivot. O pivot mudou, mas note que os valores de translação ainda são 0. 

Se você quiser ver onde o pivot *realmente* está, clique em `Bake Pivot`. Agora os valores de translação são atualizados. Note que a caixa não se move durante esta operação, nem no modo pivot.

Mova e rotacione a caixa para algum lugar, então toque em `Move Origin`. Ela move o objeto para que seu pivot fique no centro do mundo, mas deixa a rotação inalterada.

Clique em `Reset` e a rotação será definida para 0 também.

Mova e rotacione a caixa novamente; desta vez clique em `Bake`. O pivot permanece onde está, a caixa permanece onde está, mas os valores de translação e rotação são definidos para 0.

Pratique isso algumas vezes! Entenda que os valores de pivot são ocultos; o Nomad cuida disso para você, mas se precisar definir o pivot em locais reais no espaço, Bake Pivot fará isso por você.

:::

* `Translation` - os valores de translação X, Y, Z
* `Rotation` - os valores de rotação X, Y, Z
* `Scale` - A escala uniforme se isso estiver ativado, ou a escala X, Y, Z se desativado.
* `Uniform scale` - Alterna a capacidade de escalar uniformemente ou independentemente em cada eixo

-----

* `Compact` - alterna o layout do gizmo para colocar os manipuladores extras fora ou dentro da esfera de rotação
* `Widget size` - o tamanho do gizmo
* `Thickness` - o tamanho das linhas do gizmo
* `Opacity` - a opacidade do gizmo
* `Hide on interaction` - alterna se o gizmo deve ser temporariamente ocultado ao ser arrastado

-----

* `Tangent roll threshold` - Controla como a interface de rotação se comporta ao arrastar nos círculos para rotacionar em X/Y/Z. Se este valor for 0, a rotação funciona como um dial; arraste o gizmo em círculos. Se este valor for 90, a rotação funciona como puxar o barbante de um ioiô; arraste em linha reta em direção ou para longe de onde você clicou primeiro. Valores entre 0 e 90 farão uma combinação de ambos; abaixo do valor será o movimento linear, acima será o movimento circular.
* `Numerical input` - quando ativado, um único toque no gizmo exibirá uma janela para inserir um valor exato para o eixo do widget tocado.

::: warning
O [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) e [Scale](#scale) usam sua própria caixa de seleção de simetria!

Por padrão essa simetria está desligada.
:::

À esquerda você pode mover o pivot do gizmo; você pode ver o vídeo abaixo em ação.
Isso é especialmente útil para rotação, pois não muda nada para translação.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grupo de faces {#facegroup}

Facegroups permitem organizar seu objeto em faces de cores diferentes. Você pode usar esses grupos de muitas maneiras no Nomad:

* Um método rápido de seleção para máscaras
* Ocultar/mostrar seções do seu objeto
* Organizar seu objeto sem ter que dividi‑lo em partes separadas
* Definir regiões de UV
* Guiar o quad remesher
* Controle adicional para ferramentas como smooth.

#### Barra lateral esquerda de Grupo de faces {#facegroup-left-toolbar}

* `Patch ` - Exibe os facegroups disponíveis como patches. Patches não usados podem ser excluídos. Toque em um patch para renomeá‑lo ou mudar sua cor. O ícone de mais permite criar novos patches.
* `Dot` - Pinte no objeto para definir facegroups. Quando “+ Face Group” está ativado, cada novo traço criará automaticamente um novo facegroup, útil para definir rapidamente regiões. Um toque fará um preenchimento da região selecionada. O controle deslizante define o raio do ponto.
* `Relax` - Suaviza as bordas dos facegroups. Muito útil para definir bordas limpas para quad remeshing ou para definir painéis para modelagem hard surface. Os controles deslizantes controlam o raio e a intensidade da operação relax.
* `Shape selector` - Cria facegroups com formas em vez de um pincel, via `Lock+Radius`, `Lasso`, `Polygon`, `Rect` e `Ellipse`. Veja [Shape Selector](#shape-selector) para mais informações.
* `Auto-pick` - Quando ativado, selecionará o patch onde o traço começa e aplicará esse patch para o resto do traço. Muito útil para limpar regiões de facegroup; se um facegroup se estendeu demais, ative auto-pick, comece um traço de onde o patch do facegroup está correto e arraste até a borda para reatribuir o patch correto.

### ![](/icons/tool_hide.webp) Ocultar {#hide}
Oculta ou isola partes do objeto. 

Os modos principais são controlados pelo menu esquerdo:

* `Dot` - Pincele no objeto para ocultar partes do objeto.
* `Shape selector` -  Oculta com formas em vez de um pincel, via `Lasso`, `Polygon`, `Line`, `Rect` e `Ellipse`. Veja [Shape Selector](#shape-selector) para mais informações.
* `Show` - inverte a operação, então o modo selecionado mostrará em vez de ocultar partes do objeto.

Uma barra de ferramentas aparecerá na parte superior da viewport com controles extras:

* `Clear` - Restaura o objeto; todas as partes ocultas serão reveladas.
* `Invert` - Troca as partes ocultas e visíveis.
* `Facegroup` - Usa facegroups para ocultar rapidamente seções; tocar em um facegroup ocultará todo o facegroup.
* `Mask` - Se uma máscara estiver ativa, tocar neste botão ocultará a seção mascarada.
* `Delete` - Exclui a parte oculta do objeto
* `Split` - Divide a parte oculta do objeto em uma nova forma.

### ![](/icons/tool_measure.webp) Medir {#measure}
Arraste para medir a distância entre 2 pontos.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Esta ferramenta converterá o objeto selecionado em um layout limpo de topologia quad, com controles de densidade, fluxo de arestas e simetria. 

::: tip
Quad Remesher é desenvolvido pela [Exoside](https://exoside.com/) para iOS e desktop. 

Para iOS é uma compra dentro do app no Nomad, um pagamento único de US$ 16.

Para desktop, compre uma licença na [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Você pode comprá‑la apenas para o Nomad desktop ou uma licença cruzada para todos os apps desktop suportados.

Se você já possui o Quad Remesher para outro app desktop, pode [comprar um upgrade para todas as plataformas com menor custo.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher não está disponível para Android.  Android pode usar o “Quad Remesh - Instant” gratuito e open source disponível no menu Topology -> Misc, mas entenda que seu conjunto de recursos é muito limitado.
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - Este pincel definirá a densidade alvo. Intensidade em 100% pintará em vermelho, o que usará o dobro da densidade de quads alvo nessas regiões. Intensidade em 0% pintará em ciano, o que usará metade da densidade de quads alvo nessas regiões. Intensidade em 50% pintará em cinza, o que usará a densidade de quads alvo padrão.
* `Smooth` - Suaviza as transições de densidade vermelho/cinza/ciano.
* `Curve` - Esboce curvas na superfície da escultura; o quad remesher usará essas curvas como guias para o fluxo das arestas. Toque em uma curva para apagá-la.
* `Path` - Desenhe caminhos na superfície da escultura; o quad remesher usará esses caminhos como guias para o fluxo das arestas. Toque em um caminho para apagá-lo. 
* `Rect` - Desenhe retângulos na superfície da escultura; o quad remesher usará esses retângulos como guias para o fluxo das arestas. Toque em um caminho para apagá-lo.
* `Ellipse` - Desenhe elipses na superfície da escultura; o quad remesher usará essas elipses como guias para o fluxo das arestas. Toque em um caminho para apagá-lo.

#### Barra superior do Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

A toolbar aparecerá na parte superior da viewport com controles extras:


* `<Count>` - Clique aqui para iniciar o processo de quad remesher; este número indica qual será a contagem alvo de quads.
* `Quads` - Defina a contagem alvo de quads deslizando para a esquerda e direita, ou toque para definir um número exato. Note que isto é mais um guia do que um número fixo; os vários controles do quad remesher frequentemente farão com que o resultado não corresponda exatamente a esse alvo.
* `Half` - Atalho para definir a contagem alvo para metade da contagem de polígonos atual.
* `Same` - Atalho para definir a contagem alvo para a contagem de polígonos atual.
* `Guides` - indica o número total de guias, ou toque para apagar todas as guias.
* `Density X` - toque para remover toda a pintura de densidade.
* `Density (painting)` - alterna para usar ou ignorar a pintura de densidade.
* `Face Group` - alterna para usar ou ignorar facegroups para orientar o quad remesher.
* `Relax` - alterna para relaxar automaticamente as bordas dos facegroups durante o quad remeshing. Se você já tiver relaxado/suavizado as bordas dos seus facegroups, desative esta opção.
* `Relax Slider` - Um atalho em forma de slider para relaxar as bordas dos facegroups.
* `Hard Edges` - alterna para tentar manter arestas duras.
* `Reproject Vertex` - alterna para reprojetar o novo layout na malha de entrada.
* `Symmetry` - Alterna para habilitar um resultado simétrico. Note que a simetria é sempre calculada em torno do eixo X do mundo, então certifique-se de que seu modelo esteja na origem se você espera um resultado simétrico.
* `...` - Menu de configurações do Quadremesher. 

#### Menu de configurações do Quad Remesher {#quad-remesher-settings-menu}

A maioria dessas configurações está disponível na toolbar superior.

* `<Count>, Half, Same` - Iguais aos botões Remesh, Half, Same na toolbar superior.
* `Target Quads` - Igual ao botão `Quads` na toolbar superior
* `Adaptive quad count` - alterna para permitir o uso de quads menores em áreas de alta curvatura e quads maiores em áreas de baixa curvatura.
* `Adaptive size` - Define a quantidade de adaptatividade. 100% permitirá o tamanho adaptativo máximo; em 0% os quads serão uniformes.
* `Auto-Detect Hard Edges` - alterna para adaptar o layout do quad remesh para seguir melhor superfícies com cantos vivos.
* `Density (painting)` - Igual ao botão `Density (painting)` na toolbar superior
* `Reproject Vertex` - alterna para reprojetar o novo layout na malha de entrada.
* `Face Group` - Igual ao botão `Face Group` na toolbar superior
* `Relax Slider` - Um atalho em forma de slider para relaxar as bordas dos facegroups.

::: tip

Uma receita para obter um bom quad remesh com artefatos mínimos:

* Crie facegroups na malha para definir o fluxo ideal de quads.
* Use o relax de facegroup para obter bordas de facegroup suaves.
* Faça um decimate. Isso garantirá que você não tenha faces finas ou distorcidas na borda do facegroup. Nas configurações de decimate, certifique-se de que facegroup esteja habilitado. Isso fará com que as arestas dos triângulos sigam precisamente as bordas dos seus facegroups. 

Nas opções de quad remesh, certifique-se de que o relax esteja desativado (já que você já relaxou a malha) e você deverá obter bons resultados.

:::

### ![](/icons/tool_select.webp) Selecionar {#select}
Use os modos de forma para selecionar objetos na cena. `Unselect` removerá objetos da seleção.

### ![](/icons/tool_view.webp) Visualizar {#view}
Esta "ferramenta" não faz nada em particular; é simplesmente uma forma de visualizar o modelo sem modificar sua cena.


## Menu de contexto da caixa de ferramentas {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Um clique com o botão direito ou um toque longo em uma ferramenta na toolbox abrirá um menu de contexto. Este menu tem as seguintes opções:

* `Save` - salva quaisquer alterações feitas na ferramenta
* `Clone` - duplica a ferramenta em um novo atalho de ferramenta
* `Last save` - reverte para a versão previamente salva da ferramenta
* `Icon` - altera o ícone da ferramenta
* `Reset` - restaura a ferramenta para seus padrões
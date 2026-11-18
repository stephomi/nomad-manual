# ![](/icons/brush.webp) Traçado {#stroke}

---
![](/images/stroke_overview.webp) 

## Visão geral {#overview}

Você pode personalizar o comportamento do traçado da maioria dos pincéis das ferramentas.
Os ajustes são parecidos com os dos aplicativos de pintura 2d, mas algumas opções são específicas da escultura e do 3d.

As opções estão divididas em 5 submenus:

| Nome     | Ícone                        | Descrição                                                          |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Traçado  | ![](/icons/brush.webp)      | Controla como o traçado é aplicado ao modelo                       |
| Alfa     | ![](/icons/alpha.webp)      | Como uma textura em tons de cinza é usada no carimbo do pincel     |
| Decaimento | ![](/icons/falloff.webp)  | Controla como a força do pincel varia do centro até a borda        |
| Filtro   | ![](/icons/filter.webp)     | Como o pincel é afetado pela geometria do modelo                   |
| Pressão  | ![](/icons/pressure.webp)   | Controla a resposta à pressão da caneta                            |

::: tip
Nem todas as opções de traçado se aplicam a todas as ferramentas. As opções que a ferramenta atual não usa ficam desativadas ou ocultas.
:::


## ![](/icons/brush.webp) Traçado {#stroke-1}

### ![](/icons/radius.webp) Raio {#radius}

![](/images/stroke_radius.webp)

As opções de raio são ajustes globais: valem para todas as ferramentas.

#### Espaço {#size}

* `Tela` - o raio é definido em unidades da tela. Se você deixar o raio com 100 pixels de largura, ele continua com 100 pixels, quer você aproxime ou afaste a câmera.
* `Mundo (3D)` - o raio é definido em unidades 3d. Por exemplo, se você criar uma esfera e deixar o raio do mesmo tamanho dela, o raio continua do tamanho da esfera quando você aproxima ou afasta a câmera.

#### ![](/icons/link.webp) Sincronizar atalho {#sync-shortcut}

Quando ativado, os ajustes de raio e de silhueta ficam sincronizados ao passar para os pincéis de atalho (`Suavizar`, `Máscara` ou `Ocultar`). Assim, uma passada rápida de suavização ou de máscara usa o mesmo tamanho de pincel da ferramenta que você estava usando.

#### ![](/icons/link.webp) Raio compartilhado {#share-radius}

Quando ativado, todas as ferramentas usam o mesmo raio. Por padrão, cada ferramenta tem o seu próprio raio.


### Tipo de traçado {#stroke-type}

![](/images/stroke_strokemode.webp)

Os traçados podem funcionar de vários modos:

### ![](/icons/stroke_dot.webp) Ponto {#dot}
Arraste como em um traçado de pintura comum.
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rolar {#roll}
O alfa do pincel gira para acompanhar a direção do traçado, o que é útil para fazer costuras em tecidos.
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Bloqueio + raio {#lock-radius}
Carimba um traçado com **_altura_** fixa. Arrastar define a escala e a rotação.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Bloqueio + intensidade {#lock-intensity}
Carimba um traçado com **_raio_** fixo. Arrastar define a altura e a rotação.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Os modos `Bloqueio + raio` e `Bloqueio + intensidade` ignoram os ajustes de [Pressão](#pressure), já que o próprio arrasto define o tamanho e a força.
:::

![](/images/stroke_strokemodemove.webp)

As ferramentas `Mover` e `Arrastar` têm as suas próprias 3 opções:

### ![](/icons/snake.webp) Arrasto {#drag}

Atualiza continuamente o que está dentro do raio do pincel durante o traçado. Um traçado rápido deixa a superfície para trás, enquanto um traçado lento segura o material, criando formas mais longas. É o modo padrão da ferramenta `Arrastar`. Com a `Topologia dinâmica`, dá para fazer extrusões parecidas com cobras.
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Seguro {#grab}
Seleciona o que está dentro do raio do pincel no início do traçado e mantém essa seleção. É útil para movimentos mais precisos, já que você pode ajustar com cuidado a distância do movimento sem mover sem querer mais do que selecionou no início. É o modo padrão da ferramenta `Mover`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Bloqueio + raio (arrasto) {#lock-radius-drag}
O raio definido por você é ignorado: ele é ajustado dinamicamente conforme a distância que você arrasta a partir do ponto inicial. Uma distância pequena dá um raio pequeno, uma distância maior dá um raio maior. Use o controle de intensidade para ajustar a forma do decaimento. Útil para esboçar formas orgânicas e borrachudas.
![](/videos/stroke_lockradius_drag.mp4) 

Algumas outras ferramentas mostram aqui os seus próprios tipos de traçado, por exemplo `Relaxar`, `Suavizar` e `Borrar` nas ferramentas de suavização, ou formas como `Laço` e `Curva` nas ferramentas baseadas em seleção. Eles são descritos junto com cada [ferramenta](tools.md).


### Ajustar intensidade do espaçamento {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Traçados com espaçamento baixo (abaixo de 50%) se acumulam rápido e ficam mais intensos do que com valores de espaçamento maiores. Esta opção compensa isso, para que os traçados tenham mais ou menos a mesma intensidade, seja qual for o espaçamento.

### Espaçamento do traçado {#stroke-spacing}
A distância entre cada aplicação do pincel durante um arrasto. Valores abaixo de 100% se sobrepõem e dão a impressão de um traçado contínuo. Valores acima de 100% começam a deixar espaços, o que é útil para esculpir detalhes como costuras ou zíperes.

### Estabilizador por corda {#lazy-rope-stabilizer}
O traçado segue o ponteiro com um certo atraso, a uma certa distância. Isso ajuda a desenhar linhas suaves.
![](/videos/stroke_lazy_rope.mp4) 

### Suavização do traçado {#stroke-smoothing}
Faz a média de várias posições do ponteiro para obter um traçado mais suave.
Com valores altos, o traçado fica atrás do ponteiro, mas acaba alcançando.
É útil para desenhar linhas suaves.

### Raio de ajuste {#snap-radius}
Encaixa o traçado no anterior quando o ponteiro começa perto de onde o último traçado terminou. O raio define até que distância procurar o fim do traçado anterior. Isso ajuda a desenhar linhas longas e contínuas fazendo pausas frequentes.

### ![](/icons/trail.webp) Rastro {#trail}

Quando ativado, cada novo carimbo também reaplica os pontos mais recentes do traçado que ficaram para trás. `Contagem de rastro` define quantos pontos são reaplicados, `Intensidade do rastro` a força deles, e `Raio do rastro` o quanto eles crescem.

O rastro só funciona com o tipo de traçado `Ponto`, e não com a [influência do decaimento](#influence) `Crista`.

### ![](/icons/silhouette.webp) Silhueta {#silhouette}
![](/images/stroke_silhouette.webp)
Por padrão, os traçados só afetam a superfície do modelo dentro do raio do pincel. Com a silhueta ativada, o traçado é projetado através de todo o modelo. Isso é muito útil para esboçar as formas iniciais de um modelo, ou para formas cujos lados precisam continuar perpendiculares.

A direção da projeção pode ser definida explicitamente:

* `X`, `Y`, `Z` - projeta ao longo de um eixo fixo.
* `Vista` - projeta na direção da câmera.
* `Se alinhado` - projeta na direção da câmera, mas apenas enquanto a câmera está alinhada a uma vista. Caso contrário, o traçado continua sendo um traçado comum.
* `Mais próximo` - projeta ao longo do eixo mais próximo da direção da câmera. É o padrão.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomizar {#randomize}

![](/images/stroke_randomize.webp)

A `Intensidade`, o `Deslocamento`, a `Rotação` e a `Escala` do traçado podem ser randomizados, cada um separadamente. Use a caixa de seleção de cada linha para ligá-la ou desligá-la. Isso permite criar vários efeitos: por exemplo, randomizar com a ferramenta de pintura cria cores manchadas, e randomizar com a ferramenta de vinco ajuda a criar detalhes de pele.

`Período (mais lento)` define a duração do ciclo aleatório: aumente-o para variações lentas e suaves, diminua-o para um ruído rápido. O pequeno botão ao lado de cada linha ajusta o período só daquela linha.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Randomizar - HSV {#randomize-hsv}

Nas ferramentas que pintam, o `Matiz`, a `Saturação` e o `Valor` da cor da pintura também podem ser randomizados, com o seu próprio período. Ótimo para dar uma variação sutil de cor à pele ou à pedra.

### Deslocamento do traçado {#stroke-offset}

Aplica um deslocamento constante ao traçado, para que o seu dedo não o cubra. É útil em telas pequenas. É um ajuste global: ative-o pela caixa de seleção, e ele vale para todas as ferramentas.

## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

O `Alfa` é uma textura que modula o comportamento do pincel.
É uma imagem em tons de cinza, em que os pixels pretos não deformam nada e os pixels brancos deformam ao máximo.

Toque na imagem do alfa para trocá-lo. Além dos alfas incluídos e das suas próprias importações, a lista de alfas também pode baixar mapas de deslocamento do Poly Haven.

Toque na pré-visualização do material para carregar um alfa a partir de um pré‑ajuste de material. Aqui você também pode salvar pré‑ajustes de material e escolher incorporar as texturas à ferramenta.

::: tip
A textura nunca é redimensionada, então texturas grandes podem deixar tudo mais lento.
:::

### ![](/icons/blend_contrast.webp) Corrigir alfa {#invert-pixels}
O botão `Corrigir...` de um alfa importado abre uma janela que corrige a própria imagem: o valor médio, a inversão dos pixels (o preto vira branco e o branco vira preto), uma rotação de 90° e um espelhamento horizontal ou vertical. O arquivo da imagem é reescrito, então os outros aplicativos também passam a ver a imagem corrigida.

::: tip

Os alfas incluídos no Nomad não podem ser corrigidos.

:::

### Projeção {#projection}

Como o alfa é projetado no modelo:

* `Superfície` - o alfa fica sobre a superfície sob o pincel, seguindo a orientação dela.
* `Tela` - o alfa é projetado diretamente a partir da vista.
* `Ladrilho` - o alfa é projetado a partir da vista e fica parado enquanto você pinta por cima, como um estêncil, para que um padrão repetido se encaixe sem emendas. A rotação fica travada, e a pressão da caneta não altera o tamanho do padrão.
* `Triplano` - o alfa é projetado ao longo dos 3 eixos. As opções de dimensionamento, rotação e matrização abaixo são substituídas pelos ajustes da textura triplanar.

### ![](/icons/diagonal.webp) Dimensionamento {#scaling}

No Nomad, o pincel é um círculo com um raio definido por você. As texturas costumam ser quadradas ou retangulares, e os parâmetros de `Dimensionamento` permitem decidir como a textura se encaixa no círculo. Para uma textura quadrada, um valor de 0,7 a deixa dentro do círculo. Um valor de 1 aumenta a textura para que o círculo fique dentro dela, cortando as bordas.

![](/images/alpha_scaling.webp) 

Ativar `Dimensionamento Y` permite esticar o alfa verticalmente. O primeiro controle passa então a ser `Dimensionamento X`.

![](/images/alpha_scaling_y.webp) 

`Inverter horizontalmente` espelha o alfa da esquerda para a direita.

### Rotação {#rotation}

A textura do alfa gira para acompanhar a direção do traçado. Você pode somar um deslocamento de rotação e, se o ícone de cadeado estiver ativado, a textura fica travada nessa rotação em relação à tela.

O botão de caneta ao lado gira o alfa quando você gira a caneta no próprio eixo (barrel roll), com os traçados `Bloqueio + raio` e `Bloqueio + intensidade`, enquanto a rotação está destravada. Só funciona com canetas compatíveis.

### Matrização {#tiling}
![](/images/stroke_tiling.webp) 

Quantas vezes a textura se repete dentro do perfil do pincel. Os modos `Matrização - X` e `Matrização - Y` permitem limitar a uma única textura no traçado (`Nenhum`), repetir a textura (`Repetir`) ou espelhá-la, invertendo uma textura a cada duas para criar padrões ou ajudar a fazer texturas sem emendas (`Espelhar`). Eles estão disponíveis com o traçado `Rolar`, a projeção `Ladrilho` ou uma `Matrização` acima de 1.

`Ajuste preciso (imagens não quadradas)` só faz diferença para alfas e texturas de pincel não quadrados. Quando ativado, cada imagem se repete por conta própria, sem espaçamento. Desative-o para manter o alfa e as outras imagens sincronizados quando as proporções forem diferentes.

![](/videos/alpha_tiling.mp4) 



### Valor médio {#mid-value}

Por padrão, os pixels pretos não deformam nada e os pixels brancos aplicam a deformação positiva máxima. Assim, por exemplo, um pincel de argila com um alfa de pedras só puxa a superfície para fora onde o alfa não é preto.

Se você quiser que o pincel afunde a superfície, ou que ao mesmo tempo afunde E puxe para fora, pode alterar o valor médio. Com o valor em 0,5, um cinza médio no alfa não faz nada, o preto afunda e o branco puxa para fora.

Dois botões ajudam a encontrar o valor certo: o botão quadrado lê o valor médio na borda da imagem, e o seletor permite escolhê-lo diretamente no alfa.




## ![](/icons/falloff.webp) Decaimento {#falloff}

![](/images/falloff_menu.webp) 

Funciona como o [Alfa](#alpha), só que você controla a intensidade com uma única curva. Ele é combinado com o alfa, para que você use uma textura para os detalhes e o decaimento para controlar o esmaecimento na borda e a intensidade no centro da ferramenta.

Quando a curva está no alto, a deformação é máxima; quando está embaixo, o pincel não tem efeito.

Pense na curva como um corte transversal da ponta do pincel. A parte de baixo mostra como ficaria um único "carimbo" do pincel na superfície do modelo e, se o pincel tiver uma textura de alfa, ela também aparece, para você ver como o decaimento e o alfa vão interagir.

### ![](/icons/fx.webp) Pré‑ajuste {#preset}
Com `Pré‑ajuste...` selecionado, tocar no gráfico da curva abre um menu de pré‑ajustes. Curvas arredondadas dão resultados mais suaves, curvas angulosas dão resultados mais marcados. O botão `Sub` na barra de ferramentas à esquerda inverte o decaimento, de modo que o alto da curva afunda a superfície em vez de puxá-la para fora, ou vice-versa.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Quando selecionado, você pode desenhar as suas próprias curvas de decaimento. O editor funciona como as curvas no resto do Nomad:

* Toque na curva para criar um ponto novo
* Arraste um ponto para reposicioná-lo
* Toque em um ponto para alternar entre anguloso e suave
* Arraste um ponto sobre um ponto vizinho para removê-lo

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Quando selecionado, você pode desenhar as suas próprias curvas de decaimento. O editor funciona como o Catmull-Rom, mas os pontos influenciam a curva em vez de ficarem sobre ela, o que ajuda a criar curvas mais suaves.

### ![](/icons/curve_bevel.webp) Chanfro {#bevel}
Os pontos são ligados por retas, com cantos arredondados cujo tamanho depende da nitidez de cada ponto. Prático para pincéis de topo plano com um chanfro limpo na borda.

O editor de curvas tem 3 botões:

| Item     | Ícone                       | Descrição                                    |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximizar | ![](/icons/maximize.webp) | Amplia o editor de curvas                    |
| Redefinir | ![](/icons/reset.webp)    | Volta a curva ao estado padrão               |
| Simetria | ![](/icons/symmetric.webp) | Mostra a curva como uma "ponta de pincel" simétrica |


### Influência {#influence}

* `Esfera` (3d) - a influência é calculada pela distância entre o vértice e o centro do pincel.
* `Círculo` (2d) - o vértice é primeiro projetado no plano da área, e só então se mede a distância até o centro do pincel. É parecido com a forma como os alfas são amostrados.
* `Cilindro` - a influência é projetada através da área como um cilindro. É o mesmo que ativar a [Silhueta](#silhouette-1) abaixo.
* `Crista` - o decaimento é medido de um lado ao outro do traçado, então a curva vira o corte transversal do traçado inteiro. O botão `Simetria` espelha então o perfil de um lado ao outro do traçado: edite um lado e o outro acompanha. Quando ele está desligado, a curva vai do lado esquerdo do traçado até o lado direito. Não está disponível para as ferramentas baseadas em achatamento.

### ![](/icons/silhouette.webp) Silhueta {#silhouette-1}
Por padrão, os traçados só afetam a superfície do modelo dentro do raio do pincel. Com a silhueta ativada, o traçado é projetado através de todo o modelo. Isso é muito útil para esboçar as formas iniciais de um modelo, ou para formas cujos lados precisam continuar perpendiculares. Ela tem as mesmas opções de projeção que a [Silhueta](#silhouette) da aba Traçado.

## ![](/icons/filter.webp) Filtro {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Acumular traçado {#accumulate-stroke}
Remove o limite de quanto material pode ser adicionado ou removido por traçado. Por exemplo, a ferramenta `Argila` tem esta opção ativada, então o material continua se acumulando, enquanto a ferramenta `Pincel` a tem desativada, então o traçado para de adicionar material se você continuar passando pela mesma região da malha.

### ![](/icons/culling.webp) Apenas vértice da face frontal {#front-facing-vertex-only}
Esta opção ignora os vértices voltados para trás.
É útil para pintar parte de uma geometria fina sem atingir o outro lado.
Também funciona na escultura, mas podem aparecer alguns artefatos.

### ![](/icons/eye_open.webp) Só vértices visíveis {#visible-vertex-only}
Ignora os vértices escondidos atrás de outras superfícies, do ponto de vista da câmera. Esta opção aparece nos traçados de forma (laço, retângulo...) das ferramentas de máscara, de pintura, `Grupo de faces` e `Ocultar`.

### ![](/icons/dynamic.webp) Permitir topologia dinâmica {#allow-dynamic-topology}
Esta opção só está disponível se a sua malha estiver no modo [Topologia dinâmica](topology.md#dynamic-topology). Você pode ativar ou desativar a topologia dinâmica para cada ferramenta.

### ![](/icons/connect.webp) Topologia conectada {#connected-topology}
Esculpe apenas os vértices ligados à superfície que você toca com a ferramenta. Por exemplo, com a ferramenta `Mover`, isso permite mover uma parte mesmo que ela atravesse outra parte.
![](/videos/connected_topology.mp4)

### Proteger área {#protect-area}
![](/images/filter_protect_area.webp) 

Estas opções impedem que as ferramentas afetem partes da malha em certas condições. Cada uma pode ficar em `Auto`, `Não` ou `Sim`, e a pequena seta mostra o que o `Auto` está valendo no momento.

* `Ocultar` - se partes da malha estiverem ocultas com a ferramenta de ocultar, define se elas ficam protegidas. Em `Auto`, as faces ocultas ficam protegidas, a não ser que a armação delas esteja visível (veja os ajustes de [Armação](settings.md#wireframe)).
* `Máscara` - se partes da malha estiverem mascaradas, define se elas ficam protegidas. Em `Auto`, as partes mascaradas ficam protegidas enquanto a máscara estiver visível no menu [Sombreamento](shading).
* `Grupo de faces` - define se a ferramenta só pode ser usada dentro do primeiro grupo de faces tocado. Em `Auto`, segue a visibilidade dos grupos de faces no menu [Sombreamento](shading).

O botão `(Todos)` define se essas proteções são globais, compartilhadas por todas as ferramentas, ou definidas para cada ferramenta.


### Amostragem de área {#area-sampling}
Alguns pincéis ou opções de traçado precisam de uma normal e de uma posição de plano na superfície para funcionar.

Você pode controlar como esse plano médio é calculado definindo a área de amostragem como uma proporção do raio da ferramenta.

Em 100%, todos os pontos dentro do círculo de seleção são levados em conta.

Em 0%, apenas o vértice ou triângulo mais próximo é levado em conta. Esses valores podem ficar vinculados para `Raio normal` e `Raio de posição`, ou desvinculados e ajustados separadamente.

### Filtro de normal por área {#keep-sharp-edges}
Exclui os pontos cuja normal se afasta demais da normal da superfície.

Isso muda o cálculo da área do plano (Amostragem de área), então é útil principalmente para as ferramentas de argila ou baseadas em achatamento, ou para colorir uma superfície quase plana sem transbordar.

Os ângulos `Mín.` e `Máx.` controlam a transição entre os pontos excluídos e os totalmente afetados, como mostra o pequeno disco colorido ao lado deles.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtro de normal por queda {#falloff-normal-filter}
Assim como o [Filtro de normal por área](#keep-sharp-edges), exclui os pontos cuja normal se afasta demais da normal da superfície, mas age sobre o decaimento do pincel em vez do cálculo do plano. É útil para pintar vincos ou relevos.


### Filtro de profundidade {#depth-masking}
![](/images/stroke_depthmask.webp)

Exclui os pontos que estão acima ou abaixo de uma certa distância do plano calculado (Amostragem de área).

Isso permite pintar só nas regiões em relevo, ou só nas cavidades.

O gráfico representa um corte transversal da superfície: a linha horizontal é onde fica a superfície, e o círculo representa o raio de decaimento da pintura, acima e abaixo da superfície. `Deslocamento de altura` é uma porcentagem acima ou abaixo da superfície a partir da qual começa o cálculo da máscara. Com `Decaimento de profundidade` ativado, `Área superior` e `Área inferior` permitem dimensionar o decaimento acima e abaixo do ponto de deslocamento.

#### Exemplo: pintar nas cavidades {#example-paint-in-cavities}
Para pintar só as cavidades, coloque o deslocamento de altura em -100% e ajuste o controle da área superior para que ela se afaste da linha horizontal. Assim, o primeiro toque define a profundidade "zero", e só as áreas abaixo dessa profundidade são afetadas.

![](/videos/stroke_depth_cavity.mp4)

#### Exemplo: pintar nos relevos {#example-paint-on-bumps}
Para pintar só as regiões altas, coloque o deslocamento de altura em +90%, para que a parte de baixo do círculo cruze um pouco a linha horizontal. Quando você toca no alto de uma zona "alta", isso define a profundidade: tudo o que estiver nessa profundidade, um pouco abaixo dela ou mais alto será pintado. As cavidades profundas ficam de fora.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Pressão {#pressure}
![](/images/pressure_menu.webp) 

Controla como a pressão da caneta afeta os pincéis.

### Usar ajustes globais {#use-global-settings}

Por padrão, `Usar ajustes globais` está ativado, ou seja, todos os pincéis compartilham os mesmos valores de pressão. Desmarque-o para dar à ferramenta atual os seus próprios ajustes de pressão.

### ![](/icons/radius.webp) Raio {#pressure-radius}

Esta curva controla como a pressão afeta o raio do pincel. O padrão é uma relação linear: se a sua caneta tiver uma resposta suave, a variação do raio também deve parecer suave. Dito isso, muitas canetas têm uma resposta não linear, que você pode compensar com esta curva. Por exemplo, se o raio parecer não chegar ao valor máximo com pressão alta, use um pré‑ajuste de curva como "out-pow3", com uma curvatura voltada para cima, para aumentar o raio mais cedo.

Esta janela é parecida com a da curva de decaimento: você pode usar um pré‑ajuste tocando na janela da curva, ou desenhar as suas próprias curvas com os modos `Catmull-Rom`, `B-spline` e `Chanfro`.

Se quiser um raio constante, desative esta seção.

### ![](/icons/intensity.webp) Intensidade {#pressure-intensity}

Parecida com a curva de raio, mas para controlar a intensidade. Se quiser uma intensidade constante, desative esta seção.

### Limitar pressão a 100% {#limit-pressure}

Garante que a pressão da caneta nunca passe de 100%. É um ajuste global.

### Suavização de pressão {#pressure-smoothing}

Faz a média dos eventos de pressão da caneta para obter resultados mais suaves.

# ![](/icons/pencil.webp) Traço {#stroke}

---
![](/images/stroke_overview.webp) 

## Visão geral {#overview}

Você pode personalizar o comportamento do traço da maioria dos pincéis de ferramenta.
As configurações devem ser semelhantes às presentes em aplicativos de pintura 2D, porém algumas opções são específicas para escultura e 3D.

As opções são divididas em 5 submenus:

| Nome     | Ícone                        | Descrição                                                         |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Controla como o traço é aplicado ao modelo                        |
| Alpha    | ![](/icons/alpha.webp)      | Como uma textura em escala de cinza é usada para o carimbo do pincel |
| Falloff  | ![](/icons/falloff.webp)    | Controla como a força do pincel muda do centro para a borda       |
| Filter   | ![](/icons/filter.webp)     | Como o pincel é afetado pela geometria do modelo                  |
| Pressure | ![](/icons/pressure.webp)   | Controla a resposta à pressão da caneta                           |

::: tip
Nem todas as opções de traço se aplicam a todas as ferramentas. Opções de traço que não são usadas pela ferramenta atual serão desativadas ou ocultadas. 
:::


## Traço {#stroke-1}

### Raio {#radius}

![](/images/stroke_radius.webp)

#### Compartilhar raio {#share-radius}

Quando ativado, todas as ferramentas usarão o mesmo raio; o padrão é cada ferramenta ter seu próprio raio.

#### Tamanho {#size}

* Screen - o raio é definido em unidades de tela. Se você definir o raio para 100 pixels de largura, ele permanecerá com 100 pixels de largura independentemente do zoom.
* Constant (3d) - o raio é definido em unidades 3D. Por exemplo, se você criar uma esfera e definir o raio com o mesmo tamanho da esfera, o raio permanecerá do mesmo tamanho da esfera ao dar zoom in e out.


### Traço {#stroke-type}

![](/images/stroke_strokemode.webp)

Os traços podem atuar em vários modos:

### ![](/icons/stroke_dot.webp) Ponto {#dot}
Arraste como um traço de pintura comum. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rolagem {#roll}
O alpha do pincel será girado para seguir a direção do traço, útil para fazer costuras de tecido. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
Carimba um traço de pincel com **_altura_** fixa. Arrastar define a escala e a rotação.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Travar + intensidade {#lock-intensity}
Carimba um traço de pincel com **_raio_** fixo. Arrastar define a altura e a rotação.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

As ferramentas `Move` e `Drag` têm suas próprias 3 opções:

### ![](/icons/snake.webp) Arrastar {#drag}

Continuará atualizando o que está dentro do raio do pincel durante o traço. Um traço rápido deixará a superfície para trás, enquanto um traço lento “segura” o material, criando formas mais longas. Este é o modo padrão da ferramenta `Drag`. Com `Dynamic Topology` isso pode ser usado para fazer extrusões em forma de cobra. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Puxar {#grab}
Seleciona o que está dentro do raio do pincel quando o traço é iniciado e mantém essa seleção. Isso é útil para operações de mover mais precisas, pois você pode ajustar cuidadosamente a distância do movimento sem mover acidentalmente mais do que selecionou originalmente. Este é o modo padrão da ferramenta `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Travar + raio (arrastar) {#lock-radius-drag}
O raio definido pelo usuário é ignorado e é definido dinamicamente com base em quão longe o traço é arrastado a partir do ponto inicial. Distância pequena = raio pequeno, distância maior = raio maior. Use o controle deslizante de intensidade para controlar o formato do falloff. Útil para bloquear formas orgânicas e “borrachudas”.
![](/videos/stroke_lockradius_drag.mp4) 



### Ajustar intensidade do espaçamento {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Traços com espaçamento baixo (menor que 50%) podem se acumular rapidamente, tornando os traços mais intensos do que valores de espaçamento maiores. Esta opção irá compensar isso, para que os traços tenham aproximadamente a mesma intensidade independentemente do espaçamento.

### Espaçamento do traço {#stroke-spacing}
Quão distantes serão aplicados os carimbos do pincel durante uma operação de arraste. Valores menores que 100% se sobrepõem, dando a aparência de um traço contínuo. Valores maiores que 100% começam a deixar espaços, útil para esculpir detalhes como costuras ou zíperes.

### Estabilizador de corda lenta {#lazy-rope-stabilizer}
Os traços ficarão atrasados em relação à posição do ponteiro por uma certa distância. Isso pode ser usado para desenhar linhas suaves.
![](/videos/stroke_lazy_rope.mp4) 

### Suavização do traço {#stroke-smoothing}
Faz a média de múltiplas posições do ponteiro para obter um traço mais suave.
Com valores altos, o traço ficará atrasado em relação ao ponteiro, mas eventualmente o alcançará.
Isso é útil para desenhar linhas suaves.

### Raio de encaixe {#snap-radius}
Faz o início do traço “grudar” no final do traço anterior. O raio determina até que distância procurar o final do traço anterior. Isso pode ser útil ao desenhar linhas longas e contínuas, fazendo pausas frequentes.

### ![](/icons/silhouette.webp) Silhueta {#silhouette}
![](/images/stroke_silhouette.webp)
Por padrão, os traços afetarão apenas a superfície do modelo dentro do raio do pincel. Quando Silhouette está ativado, o traço será projetado através de todo o modelo. Isso pode ser muito útil ao fazer o bloqueio inicial de um modelo ou para formas que exigem que as laterais permaneçam perpendiculares.

A direção da projeção pode ser definida explicitamente; o método padrão “Closest” detectará o melhor ângulo em relação à vista. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Aleatorizar {#randomize}

![](/images/stroke_randomize.webp)

A intensidade, a translação, a rotação e a escala do traço podem ser randomizadas individualmente. Isso pode ser usado para criar uma variedade de efeitos; por exemplo, randomizar com a ferramenta de pintura pode criar cores manchadas, ou randomizar com a ferramenta de vinco pode ser usado para criar detalhes de pele.

![](/videos/stroke_randomize.mp4) 

### Deslocamento do traço {#stroke-offset}

Aplica um deslocamento constante no traço. Isso é útil em telas pequenas onde o seu dedo cobriria o traço. 


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

O `Alpha` é uma textura que irá modular o comportamento do seu pincel.
É uma imagem em escala de cinza, onde pixels pretos significam nenhuma deformação e pixels brancos significam deformação total.

Toque na imagem do alpha para alterá-la.

Toque na pré-visualização do material para carregar um alpha de um preset de material. Você também pode salvar presets de material aqui e escolher incorporar texturas com a ferramenta.

::: tip
A textura nunca é redimensionada, então texturas grandes podem deixar o desempenho mais lento.
:::

### Inverter pixels {#invert-pixels}
Isso irá inverter os valores da imagem, então pixels pretos se tornarão brancos e pixels brancos se tornarão pretos.

::: tip

Os alphas internos que acompanham o Nomad não podem ser invertidos.

:::

### Escala {#scaling}

O tamanho do pincel no Nomad é um círculo com um raio definido pelo usuário. Texturas costumam ser quadradas ou retangulares; os parâmetros de `Scaling` permitem decidir como a textura deve se ajustar dentro do círculo. Para uma textura quadrada, um valor de 0.7 caberá dentro do círculo. Um valor de 1 ampliará a textura de forma que o círculo caiba dentro dela, cortando as bordas.

![](/images/alpha_scaling.webp) 

Ativar `Scaling - Y` permite esticar o alpha verticalmente.

![](/images/alpha_scaling_y.webp) 

### Rotação {#rotation}

A textura alpha será girada para seguir a direção do traço. Você pode adicionar um deslocamento de rotação e, se o ícone de cadeado estiver ativado, a textura permanecerá travada nessa rotação em relação à tela.

### Repetição {#tiling}
![](/images/stroke_tiling.webp) 

Com que frequência a textura se repete dentro do perfil do pincel. Os modos de tiling permitem limitar a um único uso da textura dentro do traço, repetições da textura ou espelhamento, onde cada segunda textura é invertida para criar padrões ou ajudar a fazer texturas contínuas.

![](/videos/alpha_tiling.mp4) 



### Valor médio {#mid-value}

Por padrão, pixels pretos significam nenhuma deformação e pixels brancos significam deformação positiva total; então, por exemplo, um pincel de argila com uma textura alpha de rochas só puxará a superfície para fora onde o alpha não for preto.

Se você quiser que o pincel empurre a superfície para dentro, ou tanto empurre quanto puxe, você pode modificar o valor médio. Assim, se você definir o valor para 0.5, um cinza médio no alpha não fará nada, um valor preto empurrará para dentro e branco puxará para fora.




## Atenuação {#falloff}

![](/images/falloff_menu.webp) 

Isto é semelhante ao [Alpha](#alpha), exceto que você controla a intensidade com uma única curva. Isso é combinado com o alpha para que você possa usar uma textura para detalhes e o falloff para controlar o desvanecimento da borda e a intensidade no centro da ferramenta.

Quando a curva está na parte superior, isso significa deformação total; quando está na parte inferior, o pincel não tem efeito.

Você pode pensar na curva como um corte transversal pela ponta do pincel. A seção inferior mostra uma pré-visualização de como seria um único “carimbo” do pincel na superfície do modelo e, se houver uma textura alpha para o pincel, ela também será mostrada para pré-visualizar como o falloff e o alpha irão interagir.

### Predefinição {#preset}
Com esta opção selecionada, tocar no gráfico da curva abrirá um menu de presets. Curvas arredondadas darão resultados mais suaves; curvas angulares terão resultados mais nítidos. O botão `Sub` na barra de ferramentas à esquerda efetivamente inverte o falloff, então o topo da curva empurrará a superfície para dentro em vez de puxar para fora, ou vice-versa.

### Catmull-Rom {#catmull-rom}
Quando selecionado, o usuário pode desenhar suas próprias curvas de falloff. O editor de curvas funciona da mesma forma que as curvas no restante do Nomad:

* Toque na curva para criar um novo ponto
* Arraste um ponto para reposicioná-lo
* Toque em um ponto para alternar entre “sharp” e “smooth”
* Arraste um ponto até um ponto vizinho para removê-lo

### B-spline {#b-spline}
Quando selecionado, o usuário pode desenhar suas próprias curvas de falloff. O editor funciona da mesma forma que o Catmull-Rom, mas os pontos da curva influenciam a curva em vez de estarem diretamente sobre ela, o que pode ajudar a criar formas de curva mais suaves.

O editor de curvas possui 3 botões:

| Item     | Ícone                       | Descrição                                   |
| :------: | :-------------------------: | :-----------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Expande o editor de curvas                  |
| Reset    | ![](/icons/reset.webp)     | Restaura a curva para o estado padrão       |
| Symmetry | ![](/icons/symmetric.webp) | Exibe a curva como uma “ponta de pincel” simétrica |


### Influência {#influence}

* Sphere (3d) - A influência é calculada pela distância do vértice ao centro do pincel.
* Circle (2d) - O vértice é primeiro projetado no plano da área, antes de calcular sua distância ao centro do pincel. Isso é semelhante a como os alphas são amostrados. 
* Cylinder - A influência é projetada através da área como um cilindro, usado pelo modo Silhouette abaixo.

### Silhueta {#silhouette-1}
Por padrão, os traços afetarão apenas a superfície do modelo dentro do raio do pincel. Quando Silhouette está ativado, o traço será projetado através de todo o modelo. Isso pode ser muito útil ao fazer o bloqueio inicial de um modelo ou para formas que exigem que as laterais permaneçam perpendiculares.



## Filtro {#filter}

![](/images/filter_menu.webp) 

### Acumular traço {#accumulate-stroke}
Ativa a ausência de limite para quanto material pode ser adicionado/removido por traço. Por exemplo, a ferramenta `Clay` tem isso ativado, então o material pode continuar se acumulando, enquanto a ferramenta `Brush` tem isso desativado, então os traços param de adicionar material se você continuar passando o mesmo traço sobre a mesma região da malha. 

### Apenas vértice voltado para a frente {#front-facing-vertex-only}
Esta opção irá ignorar vértices voltados para trás.
Pode ser útil se você quiser pintar parte de uma geometria fina sem afetar o outro lado.
Também funciona para escultura, mas você pode notar alguns artefatos.

### Permitir topologia dinâmica {#allow-dynamic-topology}
Esta opção só está disponível se sua malha estiver no modo [Dynamic Topology](topology.md#dynamic-topology). Você pode desativar ou ativar a topologia dinâmica por ferramenta.

### Topologia conectada {#connected-topology}
Ativa a escultura apenas nos vértices que estão ligados à superfície que você toca com a ferramenta. Por exemplo, quando usado com a ferramenta `Move`, isso permitirá mover uma parte mesmo que ela se interseccione com outra parte.
![](/videos/connected_topology.mp4)

### Proteger área {#protect-area}
![](/images/filter_protect_area.webp) 

Essas opções impedem que as ferramentas afetem partes da sua malha em várias condições. 

A opção “Auto” significa que, se você tiver hide, mask ou facegroup visível no menu [Shading](shading), eles serão protegidos, mas se estiverem desativados nesse menu, a proteção é desativada.

* `All` - Alterna se os filtros de proteção são globais ou por ferramenta.
* `Hide` - Se partes da malha estiverem ocultas com a ferramenta hide, define se elas devem ser protegidas.
* `Mask` - Se partes da malha estiverem mascaradas, define se elas devem ser protegidas.
* `Facegroup` - Define se você só pode usar uma ferramenta dentro do primeiro facegroup tocado.


### Manter arestas vivas {#keep-sharp-edges}
Exclui pontos cujas normais diferem demais da normal da superfície.

Isso mudará como a área do plano é calculada (Area sampling).

Essa opção pode ser útil para ferramentas baseadas em flatten ou se você quiser colorir uma superfície majoritariamente plana sem “vazar” para fora.

![](/videos/filter_keep_sharp_edges.mp4)

### Amostragem de área {#area-sampling}
Alguns pincéis ou opções de traço exigem uma normal de plano e uma posição de plano na superfície para funcionar.

Você pode controlar como calcular esse plano médio definindo a área de amostragem como uma proporção do raio da ferramenta.

Em 100%, todos os pontos dentro do círculo de seleção são levados em conta.

Em 0%, apenas o vértice ou triângulo mais próximo é levado em conta. Esses valores podem ser vinculados tanto para `Normal radius` quanto para `Position radius`, ou destravados e definidos de forma independente.


### Mascaramento de profundidade {#depth-masking}
![](/images/stroke_depthmask.webp)

Exclui pontos que estão acima ou abaixo de uma certa distância do plano calculado (Area sampling).

Isso pode ser usado para pintar apenas em regiões salientes ou apenas em regiões de cavidade.

O gráfico representa um corte transversal da superfície; a linha horizontal é onde a superfície está, o círculo representa o raio de falloff da pintura relativo acima e abaixo da superfície. `Height offset` é uma porcentagem acima ou abaixo da superfície para iniciar o cálculo de mascaramento. `Top area` e `Bottom area` permitem escalar o falloff acima e abaixo do ponto de offset.

#### Exemplo: Pintar em cavidades {#example-paint-in-cavities}
Para pintar apenas regiões de cavidade, defina o height offset para -100% e ajuste o controle deslizante de top area para que ele fique afastado da linha horizontal. Isso significa que o primeiro clique define a profundidade “zero” e então apenas áreas abaixo dessa profundidade serão afetadas.

![](/videos/stroke_depth_cavity.mp4)

#### Exemplo: Pintar em relevos {#example-paint-on-bumps}
Para pintar apenas em regiões altas, defina o height offset para +90%, de forma que a parte inferior do círculo intercepte a linha horizontal por uma pequena quantidade. Quando você clicar no topo de uma zona “alta”, isso definirá a profundidade, de modo que qualquer coisa nessa profundidade, mais um pouco abaixo dela, e qualquer coisa acima dela, será pintada. Cavidades profundas serão ignoradas.
![](/videos/stroke_depth_bump.mp4)


## Pressão {#pressure}
![](/images/pressure_menu.webp) 

Controla como a pressão da caneta/stylus afeta os pincéis.

Por padrão, `Use global settings` está ativado, o que significa que todos os pincéis compartilharão os mesmos valores de pressão.

### Pressão - Raio {#pressure-radius}

Esta curva controla como o raio do pincel é afetado pela pressão. O padrão é uma relação linear, então, se o seu stylus tiver uma resposta suave, a mudança de raio também deve parecer suave. Dito isso, muitas canetas têm uma resposta não linear, que você pode compensar com essa curva. Por exemplo, se o raio não parecer atingir seu valor máximo em alta pressão, use um preset de curva como “out-pow3”, com uma curvatura voltada para cima, para aumentar o raio mais cedo.

Esta janela é semelhante à exibição da curva de falloff; você pode usar um preset tocando na janela da curva ou desenhar suas próprias curvas com os modos Catmull-Rom e B-Spline.

Se quiser um raio constante, desative esta seção.

### Pressão - Intensidade {#pressure-intensity}

Semelhante ao controle de raio, mas para controlar a intensidade. Se quiser intensidade constante, desative esta seção.

### Suavização da pressão {#pressure-smoothing}

Faz a média dos eventos de pressão da caneta para resultados mais suaves.
# ![](/icons/sliders.webp) Menu Interface {#interface-menu}

Este menu reúne muitas opções para personalizar a interface do Nomad.

![](/images/interface_overview2.webp)

O Nomad pode ser personalizado a fundo. Este menu é dividido em 5 abas: Interface, Atalhos, Gesto, Vínculos e Depurar (no app, as abas de atalhos e de vínculos aparecem ambas como `Atalhos`).

![](/images/interface_menu.webp)


::: tip
Esta página trata do menu Interface, não da interface em si! A interface geral é descrita em [Primeiros passos](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interface {#interface}

A aba Interface controla a cor, o tamanho e a disposição da interface do Nomad. Ela tem duas subabas, `Aparência` e `Layout`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Cores {#presets}

![](/images/interface_presets.webp)

A subaba `Aparência` começa com uma coleção de predefinições de cores para a interface. Toque em uma para aplicá-la e depois faça o ajuste fino com as opções abaixo.

#### Destaque e Base {#color-widgetcolor-base}
As cores principais da interface: `Destaque` para os botões selecionados e as barras dos controles deslizantes, `Base` para os painéis.

#### Opacidade do texto {#text-opacity}
Suaviza o texto e os ícones sobre os painéis.

#### Alternadores, Caixa de seleção, Abas {#high-contrast-button}
O estilo dos botões de alternância (`Suave` ou `Sólido`), das caixas de seleção (`Contorno`, `Destaque` ou `Preenchimento`) e das abas (`Sublinhado`, `Suave` ou `Sólido`).

#### Ferramentas coloridas {#colored}
Colore os ícones por categoria: por exemplo, todas as ferramentas de máscara ficam marrons, as de divisão vermelhas, as de achatamento verdes etc.

#### Sombra dos painéis {#material-color-preview}
Os painéis projetam uma sombra para se destacar da cena.

#### Painel transparente {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Quando ativado, aparecem opções extras para controlar a aparência dos menus e painéis do Nomad: `Cor dos painéis` define a cor deles, `Intensidade do desfoque` o quanto a cena por trás fica desfocada, e `Vidro` adiciona refração nas bordas e reflexos, mais visíveis com pouco desfoque.

::: tip
Em dispositivos pequenos, pode ser útil deixar a cor dos painéis quase branca, transparente e com pouco desfoque, para que os menus não escondam a cena.
:::

#### ![](/icons/reset.webp) Redefinir aparência {#reset-style}
Volta todas as opções de aparência aos valores padrão.

### ![](/icons/panel_detach.webp) Layout {#layout}

A subaba `Layout` controla onde ficam os elementos e qual o tamanho deles.

#### Caixa de ferramentas {#toolbox}

Opções para o menu de ferramentas à direita da interface do Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Redimensionar {#ui-resize-corner}

Mostra ou esconde uma alça de redimensionamento no canto inferior da caixa de ferramentas.

##### Oculta {#hidden}
Normalmente, o ícone da caixa de ferramentas na barra superior alterna entre uma única coluna comprida e uma lista de ferramentas em várias colunas. Com esta opção, ele alterna entre a lista em várias colunas e a caixa oculta.

##### Redefinir ordem {#reset-order}
Volta as ferramentas padrão da caixa de ferramentas à ordem original. Os ícones personalizados continuam na caixa, no fim da lista.

#### Área superior {#rows-auto-1}
`Adaptável` escolhe o que a barra superior faz quando não cabe na tela, o que importa sobretudo em telas pequenas: `Multilinha` distribui os menus em várias linhas, `Rolar` mantém uma única linha que você pode rolar.

#### Espelhar barra superior {#mirror-top-bar}
Inverte a ordem dos menus na barra superior.

#### Espelhar barras laterais {#mirror-side-bars}
Troca as barras laterais de lado, para que a caixa de ferramentas fique à esquerda e as opções da ferramenta à direita.

#### Espelhar barra inferior {#mirror-bottom-bar}
Move a barra inferior para o canto inferior direito e inverte a ordem dos botões.

#### ![](/icons/move.webp) Arrastar painel {#drag-panel}
Um painel flutuante sempre pode ser movido arrastando sua barra; esta opção permite arrastar também o corpo dele. Em `Auto`, um dedo ou uma stylus só move o painel quando o arrasto é mais horizontal do que vertical, assim um arrasto vertical continua rolando o conteúdo. Escolha `Sim` para arrastar também com o mouse, em qualquer direção.

#### ![](/icons/pencil.webp) Usar diálogo do Nomad {#use-nomad-dialog}
Mostra a caixa de texto do próprio Nomad em vez da caixa nativa quando você digita um nome ou um valor.

#### ![](/icons/stylus.webp) Ponto ao pairar {#hover-dot}
Mostra um pequeno ponto na interface quando uma stylus pairando sobre a tela é detectada.

#### ![](/icons/help.webp) Ajuda pop-up ao passar o mouse {#help-popup-on-hover}

Em dispositivos que detectam o cursor pairando, escolhe se a ajuda contextual do Nomad, representada pelo ícone ![](/icons/help.webp), aparece ao passar o cursor por cima ou só quando você clica.

#### Tamanho global {#overall-scale}
Um multiplicador de tamanho para todos os elementos da interface.
#### Largura do painel {#panel-width}
A largura dos menus e painéis.
#### Tamanho da fonte {#font-scale}
Ajusta o tamanho das fontes.
#### Espaçamento vertical {#vertical-spacing}
O espaçamento entre os elementos nos menus e painéis.
#### Espaçamento vertical (esquerda) {#vertical-spacing-left}
O espaçamento entre os elementos na barra de ferramentas da esquerda.

#### Deslocamento da borda {#edge-offset}
Altere esses valores apenas se tiver problemas para interagir com os botões nas bordas da tela. Se esses controles estiverem desativados, o Nomad usa os valores de área segura informados pelo próprio dispositivo.

::: tip
Ao migrar o Nomad para um novo dispositivo (por exemplo, trocar um iPhone 12 por um iPhone 15), lembre-se de redefinir as opções de borda para os valores padrão!
:::

#### ![](/icons/reset.webp) Redefinir layout {#reset-layout}
Volta todas as opções de layout aos valores padrão.

## ![](/icons/window.webp) Atalhos {#shortcuts}

A aba Atalhos escolhe quais botões rápidos aparecem em volta da viewport e permite montar suas próprias barras de ferramentas flutuantes.

### Barra lateral {#side-bar}
Os botões de ferramenta rápida na parte de baixo da barra lateral esquerda: `Suavizar`, `Máscara`, `Ocultar`, `Grupo de faces` e `Gizmo`. Arraste-os para mudar a ordem.

### Barra inferior {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Toque em um atalho para adicioná-lo à barra inferior ou removê-lo. Estes vêm ativados por padrão:
* `Desfazer` - desfaz a operação anterior
* `Refazer` - restaura a última operação desfeita
* `Solo` - Esconde temporariamente todos os outros objetos, deixando visível só o selecionado. Toque de novo para mostrar todos os objetos.
* `Raio-X` - Deixa temporariamente todos os outros objetos semitransparentes, mantendo só o selecionado sólido. Toque de novo para voltar aos materiais padrão.
* `Voxel` - Remalha o objeto atual com a última resolução de voxel usada. Um toque longo ou um deslize para cima mostra um controle de resolução e a opção de bordas nítidas.
* `Grade` - Mostra ou esconde a grade da vista. Um toque longo ou um deslize para cima permite mudar a cor e a opacidade da grade.
* `Armação` - Mostra ou esconde a sobreposição de armação. Um toque longo ou um deslize para cima permite mudar a cor e a opacidade da armação.
* `Inspecionar` - mostra propriedades da sua malha, como as UVs, as texturas seladas e outras, sobrepostas ao fundo do Nomad.
* `Grupo de faces` - Mostra ou esconde a sobreposição dos grupos de faces; veja mais em [Ferramentas->Grupo de faces](tools.md#facegroup)

Outros atalhos muito usados também estão disponíveis: `Contorno`, `Projeção` (perspectiva ou ortográfica), `MatCap`, `TopoDin` e os botões de [Multirresolução](topology.md#multiresolution) `Subdividir`, `Inverter` e de nível.

#### ![](/icons/more.webp) Vínculos {#bindings-list}

Quase todas as funções do Nomad podem ser adicionadas à barra inferior pelo botão de vínculos, que mostra quantos atalhos a barra contém. Ao clicar nele, aparece um menu de vínculos:

![](/images/interface_bindings_search.webp)

Você pode procurar por categoria pelos ícones no topo ou usar o campo de busca para encontrar as funções pelo nome. Clique em uma função para adicioná-la à barra. Clique de novo para removê-la.

#### ![](/icons/eye_open.webp) Visível {#order}

Mostra ou esconde a barra inferior inteira.

#### ![](/icons/reset.webp) Redefinir {#reset}

Redefinir volta a barra inferior às configurações padrão.

### Janelas flutuantes {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Clicar no + adiciona uma barra de ferramentas flutuante. Ela só fica visível depois que você clica no botão de vínculos e adiciona alguns atalhos; aí você pode torná-la visível.

Você pode criar várias barras, e cada uma tem uma linha com estas opções:

* Arraste a alça à esquerda de uma linha para reordenar as barras.
* `Nome` - O nome da barra de ferramentas.
* `Visível` - Mostra ou esconde a barra.
* `Barra` - Mostra uma barra de título na barra de ferramentas.
* `Compacta` - Mantém a barra na tela quando a interface está minimizada.
* `Atalhos` - Abre a janela de vínculos para escolher as funções a adicionar ou remover da barra.
* `Apagar` - Apaga a barra de ferramentas.


## ![](/icons/gesture.webp) Gesto {#gesture}
O menu Gesto controla como seu dedo, a stylus, o mouse e o trackpad comandam o Nomad.

![](/images/interface_gesture.webp)

### Opções de gesto {#gesture-options}
![](/images/interface_gesture_matrix.webp)

O Nomad pode limitar as operações conforme o dispositivo de entrada. Por exemplo, arrastar o dedo pode só mover a câmera, enquanto arrastar a stylus só esculpe. Se você tiver um mouse ou trackpad, ele também pode ser atribuído a operações específicas.

Cada linha é uma operação: ative `Dedo`, `Stylus` e `Mouse` para escolher quais entradas podem fazê-la.

* `Câmera` - Move a câmera.
* `Edição de nó` - Arrasta as alças desenhadas na tela, por exemplo para editar uma primitiva, uma curva, um repetidor ou uma luz.
* `Esculpir` - Esculpe com os pincéis. As ferramentas que têm sua própria linha abaixo seguem essa linha.
* `Selecionar objeto` - Toque em um objeto para selecioná-lo.
* `Seleção de material` - Mantenha pressionado na tela para pegar a cor ou o material sob o cursor. Só funciona se o pincel atual tiver a pintura ativada.
* `Toque` - Os atalhos de toque de ferramentas como Máscara, Ocultar e Grupo de faces (veja abaixo).
* `Pintura` - As ferramentas Pintar e Borrar.
* `Máscara` - A ferramenta Máscara.
* `Face` - As ferramentas Ocultar e Grupo de faces.
* `Criar` - As ferramentas Tubo, Torno e Inserir.
* `Cortar` - As ferramentas Aparar, Dividir e Projetar.
* `Selecionar` - As ferramentas Selecionar e Medir.
* `Gizmo` - As ferramentas Gizmo e Grade.
* `Transformar` - As ferramentas Transformar e Organizar.

::: tip
Uma configuração comum em tablet é deixar só a stylus esculpir e pintar, e reservar os dedos para a câmera. Assim, a palma da mão ou um dedo distraído nunca deixa um traçado no seu modelo.
:::

### ![](/icons/tool_smooth.webp) Dedo sempre suaviza {#finger-always-smooths}
Quando ativado, seu dedo sempre suaviza enquanto uma ferramenta de escultura está ativa, seja qual for o pincel. Ativar esta opção remove `Dedo` da linha `Esculpir`: a stylus esculpe e o dedo suaviza.

### Permitir traço no ar {#allow-air-stroke}
Deixa um traçado começar mesmo que o cursor toque primeiro fora da malha. Escolha as ferramentas a que isso se aplica: `Ferramenta` (todos os outros pincéis), `Suavizar`, `Máscara` e `Ocultar`. Só funciona para entradas que podem esculpir mas não mover a câmera, por isso esses botões ficam desativados até que uma das suas entradas esteja configurada assim.

### ![](/icons/stroke.webp) Ajuste do traçado {#stroke-snap}
Segure o cursor parado no fim de um traçado para transformá-lo em uma linha reta ou em uma curva suave. Continue arrastando para girar e redimensionar o traçado ajustado em torno do ponto inicial.

`Tempo de espera` define quanto tempo você precisa ficar parado antes que o traçado seja ajustado, ou antes que uma forma passe para o modo de edição.

### ![](/icons/stylus.webp) Use amostras de entrada extras {#use-extra-input-samples}
Usa as amostras de entrada adicionais informadas pelo dispositivo. Desative se seus traçados ficarem serrilhados ou se a pressão se comportar de forma estranha. Esta opção não aparece no iOS.

### ![](/icons/tool_mask.webp) Máscara {#mask}

![](/images/interface_gesture_mask.webp)

`Atalhos de um toque` - Ativa os atalhos de um toque abaixo sem precisar segurar o botão de máscara. Eles permitem os seguintes gestos:
* toque no fundo para inverter a máscara
* toque em uma área com máscara para desfocar a máscara
* toque em uma área sem máscara para tornar a máscara mais nítida

#### Manter pressionado {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Manter pressionado com a ferramenta Máscara alterna entre o pincel de máscara e o laço (SelMask):
* `Manter pressionado - Esculpir` - Mantenha pressionado e continue arrastando: o traçado é feito com o outro modo, e o anterior volta no fim do traçado.
* `Manter pressionado - Alternar` - Mantenha pressionado e solte sem mover para alternar entre os dois.

### ![](/icons/tool_smooth.webp) Suavizar {#smooth}
`Manter pressionado - Laço` - Manter pressionado com a ferramenta Suavizar muda para a ferramenta Selecionar durante o traçado de seleção.

### ![](/icons/tool_hide.webp) Ocultar {#hide}
![](/images/interface_gesture_hide.webp)

`Atalhos de um toque` ativa os seguintes atalhos com a ferramenta Ocultar:
* Toque em um grupo de faces para ocultá-lo
* Toque em um espaço vazio para inverter os polígonos ocultos

### ![](/icons/finger3.webp) Três dedos {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Se o seu dispositivo aceita gestos com 3 dedos, configure atalhos para esse gesto aqui.

A matriz de opções permite definir arrastos verticais e horizontais como atalhos separados, ou `Não` para deixá-los desligados. Se o mesmo gesto for escolhido para 2 opções, uma delas é desativada e seu nome aparece riscado.

* `Girar iluminação` - Gira o ambiente, as luzes e o MatCap.
* `Raio da Ferramenta` - Ajusta o raio da ferramenta.
* `Intensidade da Ferramenta` - Ajusta a intensidade da ferramenta.

### ![](/icons/fingerprint.webp) Histórico 2/3 {#history-23}
`Atalhos do histórico` - quando ativado, os seguintes gestos ficam disponíveis:
* Desfazer - toque com 2 dedos
* Refazer - toque com 3 dedos

`Manter pressionado` - quando ativado, manter 2/3 dedos na tela desfaz/refaz rapidamente.

### ![](/icons/mouse.webp) Roda do mouse {#mouse-wheel}
`Velocidade (zoom 3d)` define a velocidade com que a roda aproxima a vista, e `Velocidade (interface 2d)` a velocidade com que ela rola os menus e painéis. O botão de menos ao lado de cada controle inverte a direção.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
No Mac, `Dois dedos` escolhe o que dois dedos fazem no trackpad. A pinça sempre aproxima a vista e o giro dos dedos sempre rola a vista.
* `Desativado` - Rolar com dois dedos aproxima a vista, como a roda do mouse. Os dedos não são lidos individualmente.
* `Deslocar` - Dois dedos deslocam a vista, e levantar um deles orbita. Igual ao tablet.
* `Orbitar` - Dois dedos orbitam a vista, e levantar um deles desloca.

### Acessibilidade {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Janela auxiliar` abre uma barra de ferramentas flutuante para controlar as operações de arrastar, pinçar, rolar e de câmera.

### Câmera {#camera}
Um atalho para o menu `Câmera` (as opções de câmera ficavam aqui, mas foram movidas para o menu Câmera).

### Dois toques no lápis -> Atalhos {#pencil-tap}

Um atalho para o menu `Atalhos` de vínculos, onde você define o que os dois toques no Pencil fazem. Fora do iOS, ele aparece como `Botão do lápis → Atalhos`, para o botão da stylus.

### Rejeição de palma {#palm-rejection}
Em celulares e tablets, ignora os toques cuja área de contato é maior que `Limite de tamanho máximo`, como a palma da mão apoiada na tela. Pode não funcionar em todos os dispositivos, então desative se tiver problemas para interagir com a tela.

## ![](/icons/keyboard.webp) Vínculos {#bindings}
Os atalhos de teclado e de botões são definidos no menu de vínculos:

![](/images/interface_bindings.webp)
Quase todas as funções do Nomad podem ser vinculadas a atalhos de teclado, se o seu dispositivo tiver teclado, aos botões extras da stylus ou até a controles de videogame.

Para criar um vínculo, clique no retângulo ao lado da função e pressione a tecla/o botão.

Encontre as funções pelos ícones de categoria no topo ou pela barra de busca, pelo nome.

Cada vínculo pode ser desativado pela caixa de seleção ao lado do nome. Mantenha a caixa pressionada e arraste para reordenar a lista.

Quando dois vínculos ativos usam o mesmo atalho, um ícone ![](/icons/help.webp) aparece ao lado deles, listando as funções em conflito.

### ![](/icons/more.webp) Menu de contexto {#context-menu}
O ícone ![](/icons/more.webp) depois de cada vínculo abre um menu de contexto:

![](/images/interface_bindings_context.webp)

* `Clonar` - Clona o vínculo, por exemplo para dar um segundo atalho a uma função.
* `Redefinir` - Redefine o vínculo
* `Apagar` - Apaga o vínculo. Só é possível quando a função tem mais de um vínculo.

Abaixo deles, alguns vínculos têm opções extras:

* `Teclas fixas` - Para os atalhos de ferramentas e os atalhos rápidos (Máscara, Suavizar, Gizmo, Ocultar, Grupo de faces, Adicionar/Subtrair), escolhe como apertar a tecla troca de ferramenta. `Auto` usa o padrão definido nas opções [Avançado](#advanced).
  * `Segurar` - Segure a tecla para usar a ferramenta e solte para voltar à ferramenta anterior.
  * `Alternar` - Pressione uma vez para trocar de ferramenta.
  * `Pressão rápida` - Segure para usar a ferramenta temporariamente, ou dê um toque rápido para mudar para ela.
* `Segurar e Reverter` - Para os atalhos rápidos, escolhe se soltar uma tecla segurada sempre volta à ferramenta anterior, mesmo quando essa ferramenta já estava ativa.
* `Alternar ferramenta anterior` - Para os atalhos de ferramentas, pressionar o atalho da ferramenta atual volta para a última ferramenta. Precisa de `Teclas fixas` em `Alternar` ou `Pressão rápida`.
* `Posição` - Para os atalhos de janelas flutuantes, abre a janela onde ela estava (`Reter anterior`) ou sob o cursor (`No cursor`).
* `Translação (ao soltar)` / `Zoom (ao soltar)` - Para os vínculos de zoom e deslocamento da câmera, passa para o outro quando você solta a tecla.
* Direção do arrasto - Para `Girar iluminação`, `Raio da Ferramenta` e `Intensidade da Ferramenta`, escolhe um arrasto horizontal ou vertical.
* `Sincronizar` - Para as funções que adicionam, clonam ou instanciam objetos, escolhe se o resultado é sincronizado. Por padrão, usa o valor de sincronização definido no menu Cena.
* `No fundo` - Para os atalhos rápidos Suavizar e Máscara, arraste no fundo enquanto segura a tecla para desenhar um laço: um laço de seleção para Suavizar, um laço de máscara para Máscara.
* `Forçar câmera` - Para os vínculos de câmera, move a câmera mesmo que o mesmo atalho também seja usado por outro vínculo, normalmente um atalho de ferramenta ou Adicionar/Subtrair.
* `Rotação linear` - Para o vínculo de rolagem, rola a vista com um arrasto horizontal, vertical ou diagonal, em vez de girar em torno do pivô.

::: tip
Com `Pressão rápida`, uma única tecla faz as duas coisas: segure-a para suavizar ou mascarar rapidinho e voltar ao seu pincel quando soltar, ou dê um toque para ficar nessa ferramenta.
:::

### ![](/icons/cog.webp) Avançado {#advanced}
No fim do menu de vínculos há um menu de engrenagem com opções avançadas:

![](/images/interface_bindings_advanced.webp)

* `Atalhos rápidos` - Os valores padrão de `Teclas fixas` e `Segurar e Reverter` para os atalhos Máscara, Suavizar, Gizmo, Ocultar, Grupo de faces e Adicionar/Subtrair.
* `Atalhos de ferramentas` - Os valores padrão de `Teclas fixas` e `Alternar ferramenta anterior` para os atalhos de ferramentas. Com `Alternar ferramenta anterior`, você pode ficar alternando entre duas ferramentas com a mesma tecla.
* `Janela de atalho` - O modo de `Teclas fixas` dos atalhos que mostram as janelas flutuantes.
* `Inverter o zoom Y` - Inverte a direção do arrasto vertical ao dar zoom com um vínculo.
* `Rotação linear` - Rola a vista com um arrasto horizontal, vertical ou diagonal, em vez de girar em torno do pivô.
* `SpaceMouse` - Ativa o suporte ao SpaceMouse da 3Dconnexion. Em alguns sistemas, aparecem opções extras: o que ele move (`Objeto`, `Câmera`, `Primeira Pessoa`, `Drone`), `Atualizar pivô automaticamente` para levar o pivô até a superfície sob o cursor quando ele começa a se mover, e suas velocidades de `Translação`, `Zoom` e `Rotação`.
* `Zonas mortas (deriva)` - Para controles `Gamepad`, `Joystick` e `Botão`. Aumente esses valores se a câmera se mexer enquanto o controle está parado.
* `Raio da Ferramenta` - Como um arrasto com o vínculo de raio redimensiona o pincel (`Círculo`, `Centralizado` ou `dx`), e depois quanto os vínculos de raio somam (em pixels) ou multiplicam a cada toque.
* `Intensidade da Ferramenta` - Quanto os vínculos de intensidade somam ou multiplicam a cada toque.
* `Câmera - Velocidade` - A velocidade de `Translação` e de `Rotação` dos vínculos que deslocam e giram a vista.
* `Redefinir vínculos` - volta todos os vínculos aos valores padrão.
* `Redefinir ordem` - restaura a ordem padrão da lista de vínculos.


## Lista de atalhos de teclado ⌘ no iOS {#ios-keyboard-shortcuts-display}

Em dispositivos iOS com teclado, segure a tecla ⌘ (cmd) para ver uma lista de atalhos.

O suporte a teclado no Android ainda é um pouco experimental.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Depurar {#debug}
Algumas opções experimentais e de depuração ficam neste menu. Muitas delas devem ficar nos valores padrão e só ser alteradas depois de falar com o suporte do Nomad. Os ícones no topo levam a cada seção.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalizar UVs` - O Nomad normaliza as UVs da malha selecionada dentro do quadrado [0-1].

### ![](/icons/sun.webp) Sombreamento {#render}
* `Gravar profundidade de refração (atrás)` - A face de trás das malhas com refração é gravada no buffer de profundidade.
* `Normais suavizadas ponderadas por ângulo` - Um ajuste no funcionamento do sombreamento suave que pode evitar vincos em certos casos.

### ![](/icons/speed.webp) FPS alvo {#target-fps}
Quando desativado, o Nomad sincroniza seus quadros por segundo com a taxa de atualização da tela.

Quando ativado, você pode definir quantos quadros por segundo o Nomad renderiza.

### ![](/icons/window.webp) Interface {#debug-interface}
* `Ferramentas: mostrar todas` - O Nomad esconde as ferramentas que não servem para a seleção atual: por exemplo, todos os pincéis de escultura ficam ocultos em primitivas que não foram validadas. Esta opção escurece as ferramentas desativadas em vez de escondê-las.

As outras opções de interface que ficavam aqui agora estão na aba [Interface](#interface).

### ![](/icons/turntable.webp) Mesa giratória {#gif-turntable}
O Nomad pode exportar um GIF animado de mesa giratória. Por causa das limitações do formato GIF, a qualidade é baixa. Gravar a tela costuma ser uma opção melhor.

* `Duração` - a duração da mesa giratória, em segundos
* `Amostragem máxima de quadros` - Muitos efeitos de renderização de alta qualidade do Nomad vêm da combinação de vários quadros. Este controle define quantos quadros combinar, e a caixa de seleção dele liga ou desliga o recurso.
* `Centro de rotação` - em torno do que a câmera gira: `Manter atual` mantém o pivô atual, `(0, 0, 0)` usa o centro do mundo, `Cena` o centro da cena.
* `Fundo transparente` - Usa a opção de transparência dos GIFs. Os GIFs só aceitam transparência de 1 bit, então as bordas podem ficar bem serrilhadas.
* `Exportar (GIF)` - inicia a exportação do GIF.

### ![](/icons/postprocess.webp) Pós-processamento {#post-process}
* `Filtragem` - Opção de depuração
* `Formato` - Opção de depuração
* `Reutilizar buffers` - Opção de depuração

### ![](/icons/ram.webp) Desempenho {#performance}
* `Multithread: geral` - Opção de depuração
* `Multithread: escultura` - Opção de depuração
* `Desenhar repetições por instâncias` - Desenha todas as cópias de um repetidor em uma única chamada de desenho. Opção de depuração.

### ![](/icons/star.webp) Recurso {#feature}
* `nom: comprimir multirresolução` - Reduz o tamanho dos projetos e das exportações Nomad que usam multirresolução. Esses arquivos não podem ser abertos por versões mais antigas do Nomad. Esta opção pode ser removida e ficar ativada por padrão no futuro.
* `Inverter diagonal dos quads (ao tocar)` - Opção de depuração

### ![](/icons/bug.webp) Depurar {#dev}
* `Registros` - Abre uma janela de registros
* `Registrar eventos` - Grava seus eventos de ponteiro (dedo, stylus, mouse) na janela de registros, para investigar problemas de entrada.
* `FPS` - adiciona um contador de quadros por segundo às estatísticas da viewport.
* `Janela de avaliação do app` - Opção de depuração, no iOS e no Android.

### ![](/icons/image.webp) Ícones personalizados {#custom-icons}
Substitua os ícones do Nomad pelos seus próprios arquivos png.
* `Importar ícones` - Importa arquivos png para `tmp_session/icons`. Cada um substitui o ícone original de mesmo nome. Eles são descartados quando o Nomad reinicia.
* `Exportar ícones de ferramentas` - Copia os ícones originais `tool_<tool>.png` para `tmp_session/icons`, sem sobrescrever. Você pode editá-los lá e aplicá-los com `Recarregar ícones`.
* `Recarregar ícones` - Aplica os ícones de `tmp_session/icons`.

### Remalhar em quads {#quad-remesh}
As opções de remalhagem em quads não ficam mais neste menu: veja [Remalhar em quads](topology.md#quad-remesh-instant) no menu Topologia e a ferramenta [Quad Remesher](tools.md#quad-remesher).

### Criar miniaturas da loja {#make-store-thumbnails}
Renderiza capturas de tela nos tamanhos da App Store do iOS.

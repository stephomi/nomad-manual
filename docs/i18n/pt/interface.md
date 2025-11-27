# ![](/icons/interface.webp) Menu Interface 

Este menu controla muitas opções para personalizar a interface do Nomad. 

![](/images/interface_overview2.webp)

O Nomad pode ser personalizado em um nível bastante profundo; este menu é dividido em 4 seções: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Esta página é sobre o menu de interface, não sobre a interface em si! A interface geral é descrita em [Getting Started](gettingstarted.md).
:::

## Interface 

A seção Interface permite adicionar atalhos, criar barras de ferramentas flutuantes e controlar a cor, tamanho e aparência da interface do usuário do Nomad.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

A barra inferior tem estes atalhos ativados por padrão:
* `Undo` - desfaz a operação anterior
* `Redo` - restaura a operação desfeita anteriormente
* `Solo` - Oculta temporariamente todos os outros objetos, deixando visível apenas o selecionado. Pressione novamente para restaurar todos os objetos.
* `X-ray` - Torna temporariamente todos os outros objetos semitransparentes, deixando apenas o selecionado sólido. Pressione novamente para restaurar os materiais padrão.
* `Voxel remesh` - Refaz o remesh do objeto atual usando a última resolução de voxel utilizada. Um toque longo ou deslizar para cima exibirá um controle deslizante de resolução e a opção de bordas nítidas.
* `Grid` - Alterna a visualização da grade. Um toque longo ou deslizar para cima permite alterar a cor e a opacidade da grade.
* `Wireframe` - Alterna uma sobreposição de wireframe. Um toque longo ou deslizar para cima permite alterar a cor e a opacidade do wireframe.
* `Inspector` - permite visualizar propriedades da malha, como UVs, texturas bakeadas e outras propriedades, sobrepostas ao fundo do Nomad.
* `Face Group` - Alterna a sobreposição de facegroup, mais informações em [Tools->FaceGroup](tools.md#facegroup) 

Outros atalhos comuns estão disponíveis neste menu; muitos mais podem ser encontrados dentro do botão bindings.

#### ![](/icons/more.webp) Bindings

Quase todas as funções do Nomad podem ser adicionadas à barra de atalhos através do botão bindings. Um menu de bindings será exibido quando o botão for clicado:

![](/images/interface_bindings_search.webp)

Você pode pesquisar por categoria através dos ícones na parte superior ou usar o campo de busca para encontrar funções pelo nome. Clique em uma função para adicioná-la à barra de ferramentas. Clique novamente para removê-la.

#### ![](/icons/list.webp) Order

Exibe uma lista dos atalhos. Pressione e segure e depois arraste para reordenar os atalhos.

#### ![](/icons/reset.webp) Reset

Reset restaura a barra inferior para suas configurações padrão.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

Clicar no + adicionará uma barra de ferramentas flutuante. Ela não ficará visível até que você clique no botão bindings e adicione alguns atalhos a ela; então você poderá torná-la visível. 

Você pode criar várias barras de ferramentas; cada barra tem as seguintes opções neste menu:

* ![](/icons/checked.webp) `Visible` - Alterna a visibilidade da barra de ferramentas
* ![](/icons/more.webp)`Bindings` - Exibe a janela de bindings para selecionar funções a serem adicionadas ou removidas da barra.
* ![](/icons/list.webp)`Order` - Exibe um menu para reordenar a barra de ferramentas.
* ![](/icons/reset.webp) `Reset` - Restaura a barra de ferramentas ao seu estado padrão.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Alterna um controle de redimensionamento no canto inferior direito da barra.
* ![](/icons/sort_down.webp) `Collapsable` - Alterna um controle de recolhimento no canto superior direito.
* ![](/icons/trash.webp) `Delete` - Exclui a barra de ferramentas.

### Toolbox

Opções para o menu de ferramentas à direita da interface do Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Alterna um controle de redimensionamento no canto inferior da barra de ferramentas.

#### Hidden
Normalmente o ícone da toolbox na barra superior alterna entre uma única coluna longa ou uma lista de ferramentas em várias colunas. Esta opção alterna entre a lista em várias colunas ou ficar oculta.

#### Colored
Codifica por cor os ícones por categoria; por exemplo, todas as ferramentas de máscara são marrons, ferramentas de split são vermelhas, ferramentas de flatten são verdes etc.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Restaura as ferramentas padrão da toolbox para a ordem padrão. Ícones personalizados permanecerão na toolbox ao final da lista.


### Presets

![](/images/interface_presets.webp)

Uma coleção de presets de cores para a interface.

#### High-contrast button
Um estilo alternativo para botões que os torna mais visíveis quando estão ativados. Se definido como Auto, o Nomad usará este modo quando o contraste de cor da UI entre ativado/desativado for baixo.

#### Color widget/Color base
As cores primárias usadas na interface.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Quando ativado, opções extras aparecerão para controlar como menus e painéis são exibidos no Nomad. Sua cor, transparência e quantidade de desfoque podem ser ajustadas.

::: tip
Em dispositivos pequenos pode ser útil deixar o painel de cor quase branco, transparente e com baixo blur strength, para que os menus não ocultem a cena.
:::

----

### Mirror top bar
Inverte a ordem dos menus na barra superior.

### Mirror side bars
Troca as barras laterais para que a toolbox fique à esquerda e as opções da ferramenta à direita.

### Mirror bottom bar
Move a barra inferior para o canto inferior direito e inverte a ordem dos botões.

### Material color preview
Quando você seleciona uma cor para um material, uma pré-visualização desse material é exibida no objeto atualmente selecionado.

----
### Help popup on hover

Para dispositivos que suportam hover, define se a ajuda contextual no Nomad, representada pelo ícone ![](/icons/help.webp), aparecerá ao passar o cursor ou apenas quando clicada.

----

### Overall scale
Um multiplicador de tamanho para todos os elementos da UI.
### Panel width
A largura dos menus e painéis.
### Font scale
Escala das fontes.
### Vertical spacing
O espaçamento entre elementos em menus e painéis.
### Vertical spacing (left)
O espaçamento entre elementos na barra de ferramentas esquerda.

----

### Edge offset
Você só deve alterar esses valores se tiver problemas ao interagir com os botões nas bordas da tela. Se esses controles deslizantes estiverem desativados, o Nomad usará os valores de área segura retornados pelo próprio dispositivo.

::: tip
Ao migrar o Nomad para um novo dispositivo (por exemplo, trocar um iPhone 12 por um iPhone 15), certifique-se de redefinir as opções de borda para os padrões!
:::

### Reset style
Restaura todos os elementos da UI para seus valores padrão.


## Gesture
O menu Gesture controla como toques de caneta e dedo controlam o Nomad.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

O Nomad pode limitar operações com base no dispositivo de entrada. Por exemplo, um arrasto com o dedo pode apenas mover a câmera, enquanto um arrasto com a caneta pode apenas esculpir. Se você tiver um mouse ou trackpad, ele também pode ser atribuído para controlar operações específicas.

Atualmente o Nomad permite definir estes modos para serem controlados em qualquer combinação de gestos de dedo, caneta ou mouse:

* Camera
* Sculpt
* Gizmo
* Material picking (via toque longo)
* Select object


`Finger always smooths` - Smooth pode ser configurado para funcionar apenas com arrasto de dedo.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Ativa os seguintes atalhos de um toque sem precisar manter o botão de máscara pressionado. Isso permitirá os seguintes gestos:
* toque no fundo para inverter a máscara
* toque em uma área mascarada para desfocar a máscara
* toque em uma área não mascarada para deixar a máscara mais nítida

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Um toque longo alternará entre Mask e SelMask e iniciará um novo traço. Ao final do traço, a ferramenta anterior é reselecionada. 
* `Tool` - Toque longo e soltar sem mover para alternar entre Mask e SelMask. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` ativará os seguintes atalhos com a ferramenta Hide:
* Toque em um face group para ocultá-lo
* Toque em espaço vazio para inverter os polígonos ocultos

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Se o seu dispositivo suportar gestos com 3 dedos, configure atalhos para esse gesto. 

A matriz de opções permite definir arrastos verticais e horizontais como atalhos separados. Observe que, se o mesmo gesto for escolhido para 2 opções, uma delas será desativada.

* `Rotate lighting` - Gira o ambiente, luzes e Matcap.
* `Tool Radius` - Edita o raio da ferramenta.
* `Tool Intensity` - Edita a intensidade da ferramenta. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - quando ativado, os seguintes gestos ficam ativos:
* Undo - toque com 2 dedos
* Redo - toque com 3 dedos

`Long press` - quando ativado, manter 2/3 dedos pressionados desfará/refará rapidamente.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` exibirá uma barra de ferramentas flutuante para controlar operações de arrasto, pinça, rotação e câmera.

### Camera
Um atalho para ir ao menu `Camera` (as opções de câmera ficavam aqui, mas foram movidas para o menu Camera).

### Pencil double tap -> Bindings 

Um atalho para ir ao menu `Bindings` (as opções de toque e toque duplo do Pencil ficavam aqui, mas foram movidas para o menu bindings).


## Bindings
Atalhos de teclado e botões podem ser definidos no menu bindings:

![](/images/interface_bindings.webp)
Quase todas as funções do Nomad podem ser associadas a atalhos de teclado se o seu dispositivo tiver um teclado, ou a botões extras da caneta, ou até a controles de gamepad.

Para criar um binding, clique no retângulo ao lado da função e pressione a tecla/botão. 

Encontre funções pelos ícones de categoria na parte superior ou pela barra de busca para encontrar pelo nome. 

Bindings individuais podem ser desativados pela caixa de seleção ao lado do nome do binding.

### ![](/icons/more.webp) Context menu
O ícone ![](/icons/more.webp) após cada binding abre um menu de contexto:

![](/images/interface_bindings_context.webp)

* `Clone` - Clona o binding
* `Reset` - Restaura o binding
* `Delete` - Exclui o binding
* `Toggle shortcut on key tap` - Configura se toque rápido e toque longo são tratados de forma diferente. Quando ativado, um toque rápido ativará a ferramenta. Um toque longo ativará a ferramenta apenas enquanto a tecla estiver pressionada; ao soltar, retornará à ferramenta anterior. Às vezes chamado de “sticky keys” em outros aplicativos 3D.

### Advanced
Na parte inferior do menu bindings há um menu de engrenagem para opções avançadas:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Um toque das teclas padrão para mask, smooth, gizmo, hide, sub alternará para esse modo, mas manter a tecla pressionada mudará para esse modo e, quando a tecla for solta, o modo voltará ao modo anterior. Às vezes chamado de “sticky keys” em outros aplicativos 3D.
* `Toggle tool shortcuts` - Ao usar um dos atalhos de ferramenta, se o mesmo atalho for pressionado duas vezes, ele alternará para a ferramenta anterior. Dessa forma, você pode ficar trocando entre duas ferramentas com a mesma tecla de atalho.
* `Invert Y (Zooming)` - Inverte o zoom
* `Reset bindings` - restaura todos os bindings para seus padrões.


## iOS ⌘ Keyboard shortcuts display

Em dispositivos iOS com teclado, mantenha pressionada a tecla ⌘ (cmd) para exibir uma lista de atalhos.

O suporte a teclado no Android ainda é um pouco experimental.

![](/images/shortcuts.webp)


## Debug
Algumas opções experimentais e de depuração ficam armazenadas neste menu. Muitas dessas opções devem ser deixadas em seus padrões e só alteradas após entrar em contato com o suporte do Nomad.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - O Nomad normalizará as UVs dentro do tile [0-1].

### Quad Remesh
* `Instant Mesh` - Ativa o algoritmo de remesh instantâneo
* `Quadriflow` - Um método alternativo de quad remesh.

### Render
* `Heightmap` - Altera o viewport para renderizar a profundidade da cena. Isso pode ser usado para criar alpha maps para usar em pincéis.
* `Refraction write depth (back)` - A face traseira de malhas com refração será escrita no depth buffer.
* `Flip Y (normal map)` - Inverte o canal Y ao fazer bake de normal maps, necessário para certos motores de jogo e render.
* `Angle weighted smooth normals` - Um ajuste em como o sombreamento suave funciona, que pode evitar vincos em certos casos.

### Target FPS
Quando desativado, o Nomad sincronizará seus frames por segundo com a taxa de atualização da sua tela.

Quando ativado, você pode definir o número de frames por segundo que o Nomad irá renderizar.

### Interface
* `Top: layout` 
  * Collapse: Em dispositivos pequenos, a barra superior será recolhida em mais submenus. 
  * Scroll: Se você está acostumado ao Nomad em telas grandes e prefere o layout normal, ativar isto usará a barra superior larga padrão, que poderá ser rolada.
  * Multiline: Exibe todo o menu superior em várias linhas.
* `Bottom: draggable popup` - A barra inferior tem vários botões que exibem um diálogo. Se esta opção estiver ativada, esses diálogos podem ser movidos para outro lugar na tela.  
* `Toolbox: show all` - O Nomad ocultará ferramentas que não são relevantes para a seleção atual; por exemplo, todos os pincéis de escultura são ocultados em primitivas que não foram validadas. Esta opção escurece as ferramentas desativadas em vez de ocultá-las.
* `Toolbox: colored` - Codifica por cor os ícones da toolbox com base em seu tipo.
* `Panel: Drop shadows` - Desenha sombras projetadas ao redor de menus e painéis. Em alguns dispositivos mais antigos isso pode impactar o desempenho.
* `Panel: Blending` - Opção de depuração
* `Pointer: hovering dot` - Para dispositivos que suportam hover da caneta, exibe um ponto quando a caneta está pairando sobre menus e painéis.

### Gif turntable
O Nomad pode exportar um turntable animado em gif. Observe que, devido a limitações do formato gif, a qualidade é baixa. Gravação de tela geralmente é um método melhor.

* `Duration` - quanto tempo, em segundos, o turntable terá
* `Rotation center` - onde está o pivô da câmera, portanto em torno de qual parte da cena a câmera irá girar
* `Transparent background` - Usa a opção de transparência para gifs. Observe que gifs só suportam transparência de 1 bit, então as bordas podem ficar bastante serrilhadas.
* `Max frame sampling` - Muitos dos efeitos de renderização de alta qualidade do Nomad vêm da combinação de vários frames. Este controle define quantos frames combinar.
* `Export (GIF)` - inicia o processo de exportação do gif.

### Post Process
* `Filtering` - Opção de depuração
* `Format` - Opção de depuração
* `Buffer reuse` - Opção de depuração

### Performance
* `Multicore general` - Opção de depuração
* `Multicore sculpting` - Opção de depuração
* `Partial Drawing` - Recurso experimental! Use se você estiver esculpindo uma parte relativamente pequena de uma malha de alta contagem de polígonos. Deve tornar a escultura mais suave, mas você não deve ativar o wireframe! Também pode adicionar artefatos visuais durante os traços do pincel.

### Feature
* `Flip quad split (on tap)` -  Opção de depuração
* `Join: merge radius` - Vértices serão automaticamente soldados se estiverem próximos o suficiente quando malhas forem unidas. Você pode ajustar o raio com este controle.

### Debug
* `Logs` - Exibe uma janela de log
* `App review popup` - Opção de depuração
* `FPS` - adiciona um contador de frames por segundo às estatísticas do viewport.

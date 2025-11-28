# ![](/icons/cog.webp) Configurações {#reset-to-default}

O menu de configurações contém muitas opções para controlar a aparência e o comportamento do Nomad.

![](/images/settings_overview.webp)

## Configurações de exibição {#display-settings}
Esta seção contém atalhos de lançamento rápido para a maioria das configurações mais abaixo neste menu.

![](/images/settings_display_settings.webp)

### Sombreamento suave {#smooth-shading}
Alterna entre sombreamento suave e facetado. Quando facetado, os polígonos são sombreados de forma independente, então você pode ver a topologia subjacente.
Pode ser útil ver o sombreamento facetado durante a etapa de escultura e depois mudar para sombreamento suave para renderização.

Desativar o Sombreamento Suave melhora um pouco o desempenho.

### Contorno {#outline-quick}
Ativa um contorno na sua seleção atual.

Isso é útil para obter feedback visual sobre a(s) malha(s) atualmente selecionada(s) caso [Escurecer não selecionados](#darken-unselected-objects) esteja desativado.

Do ponto de vista de desempenho, usar [Escurecer não selecionados](#darken-unselected-objects) é muito melhor do que usar a solução de contorno.

### Grade {#grid-quick}
Ativa uma grade de fundo, útil para entender o posicionamento e a escala dos objetos.

### Dois lados {#two-sided-quick}
Ativa a exibição de polígonos com duas faces. Todas as faces apontam em uma certa direção.
Faces consideradas *backface* são aquelas que apontam “para longe” do ponto de vista da câmera.

Por exemplo, a esfera simples inicial terá suas faces apontando para fora.
Se você mover a câmera para dentro da esfera, verá então o backface dessas faces.

Na maior parte do tempo você não deveria ver o lado de backface das faces, então colorir essas faces pode ajudar a detectar problemas potenciais ou topologia incorreta.

Desativar a renderização `two sided` pode melhorar um pouco o desempenho de renderização.


### Wireframe {#wireframe-quick}
Ativa uma sobreposição de wireframe. 

Note que ativar o wireframe reduzirá o desempenho.

### Cubo de encaixe {#snap-cube-quick}
Ativa um ícone auxiliar no canto da cena, útil para se orientar no espaço e alternar rapidamente entre as vistas frente/costas/esquerda/direita/cima/baixo.

### Mostrar pintura {#show-painting}
Ativa a exibição da pintura. A pintura padrão usada é um material branco não metálico, com 25% de rugosidade.

### Usar ocultar {#use-hide}
Ativa o modo de ocultar. Quando desligado ele ainda existe, apenas fica desativado. Este botão fica desabilitado se você estiver usando a ferramenta de ocultar no momento.

### Mostrar máscara {#show-mask}
Ativa o modo de máscara. Quando desligado ele ainda existe, apenas fica desativado. Pressione este botão novamente para reativá-lo.

Se você precisar ocultar a máscara E ainda assim mantê-la ativa, use a cor da máscara abaixo e defina-a como branco. Lembre-se de voltar para um cinza quando terminar!

Note que este botão fica desabilitado se você estiver usando uma ferramenta de máscara no momento. 

### Máscara -> Opaca {#mask-opaque}
Máscara -> opaco irá ignorar vértices transparentes para máscara mascarada. Isso só é relevante para opacidade de vértice e textura; faces ocultas por “hide” continuarão ocultas.

### Realce {#highlight-quick}
Ativa o flash de destaque da seleção. Ao selecionar objetos, pisca temporariamente o objeto selecionado em rosa choque por 500 milissegundos. A cor e a duração do flash podem ser personalizadas abaixo.

### Estatísticas {#stats-quick}
Ativa o texto de status na viewport 3D. Isso exibe informações sobre a memória do sistema, a contagem total de vértices da cena e a contagem de vértices da seleção atual.

----- 

### Escurecer objetos não selecionados {#darken-unselected-objects}
Os objetos que não estão selecionados serão escurecidos para que a seleção atual se destaque.

### Máscara {#mask}
A cor usada para mascaramento, por padrão um cinza médio, multiplicada pela cor do seu objeto. Defina isto como branco para tornar a máscara invisível, mas lembre-se de voltar para um cinza quando terminar!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Mostrar círculo ao esculpir {#show-circle-while-sculpting}
Continua mostrando o raio do pincel ao esculpir.

### Mostrar pequeno ponto {#show-small-dot}
Exibe um ponto no centro do traço do pincel ao esculpir, ou quando o pivô da câmera é alterado.

### Mostrar estabilizador de corda {#show-rope-stabilizer}
Desenha uma linha para indicar o comprimento da corda quando o estabilizador de corda preguiçosa está ativo nas configurações de traço.

## ![](/icons/cursor.webp) Indicador {#indicator}
![](/images/settings_indicator.webp)

Exibe indicador(es) visual(is) para tutoriais e capturas de tela.

Os botões `Finger`, `Stylus` e `Mouse` ativarão a exibição de um ícone quando esse tipo de entrada for detectado.

### Cor {#indicator-color}
A cor do indicador.

### Tamanho/Ícone/Círculo {#indicator-shape}
Controles para ajustar o tamanho do indicador e as formas dentro do indicador.

## ![](/icons/wireframe.webp) Wireframe {#wireframe}
![](/images/settings_wireframe.webp)
Ativa a sobreposição de wireframe.

### Alvo {#target}
Define se objetos não selecionados exibirão wireframe, ou apenas objetos selecionados, ou todos os objetos.

### Ocultar {#hide}
Define se o wireframe ainda será mostrado para polígonos ocultos.

### Multiresolução: apenas nível 0 {#multiresolution-level-0-only}
Multirresolução exibirá wireframes para o nível 0 mais escuros, e níveis mais altos progressivamente mais claros. Quando ativada, esta opção exibirá apenas o wireframe do nível 0.

### Cor {#wireframe-color}
Define a cor e a opacidade do wireframe.

## ![](/icons/grid.webp) Grade {#grid}
![](/images/settings_grid.webp)
Ativa a grade.

### Cor {#grid-color}
Define a cor e a opacidade da grade.

### Encaixar {#snap}
Ativa o encaixe das ferramentas baseadas em curva na grade.

## ![](/icons/culling.webp)Two sided {#two-sided}
Ativa a visualização das faces do polígono de ambos os lados.

### Colorir face traseira, Cor da face traseira {#backface-color}
Ativa a coloração dos backfaces e a cor dessa coloração.

## ![](/icons/outline.webp)Outline {#outline}
Ativa um contorno ao redor do objeto ativo.

### Cor do contorno, Espessura {#outline-color-thickness}
Define a cor e a espessura do contorno.


## ![](/icons/bang.webp) Highlight {#highlight}
Ativa um breve flash quando o objeto ativo é alterado.
### Cor, Duração {#color-duration}
Define a cor e o tempo de duração do flash em milissegundos.

## ![](/icons/snap_cube.webp) Snap cube {#snap-cube}
![](/images/settings_snapcube.webp)

Exibe um ícone auxiliar no canto da cena, útil para alternar rapidamente entre as vistas frente/costas/esquerda/direita/cima/baixo. Toque nos lados do cubo para alternar entre vistas ortográficas.

### Forma {#shape}
Escolha entre um cubo, uma esfera ou uma forma de gnômon para o cubo de encaixe.

### Restringir alinhamento {#restrict-alignment}
Ativa o bloqueio de rotação da câmera ao arrastar no cubo de encaixe. Quando ativo, um movimento de arrasto no cubo de encaixe irá apenas para esquerda/direita ou cima/baixo.

### Tamanho {#size}
Define o tamanho do cubo de encaixe.

### Virar 180 {#flip-180}
Ativa um comportamento de toque para que, se a vista estiver encaixada, tocar no centro do cubo gire a vista em 180 graus. Por exemplo, se a vista estiver encaixada na frente, tocar no cubo de vista irá girar para a vista de costas.

### Posição {#snap-position}
Define em qual canto o cubo de encaixe ficará.


## ![](/icons/edit_radius_n.webp) Stats {#stats}
![](/images/settings_stats.webp)

Exibe informações sobre a memória do sistema, a contagem total de vértices da cena e a contagem de vértices da seleção atual.

### Posição {#stats-position}
Define em qual canto as estatísticas ficarão.

## Primtive/Repeaters {#primitive-repeaters}
## Entrada numérica {#gizmo-input}
Permite entrada numérica ao tocar nos widgets do gizmo.

## Multiresolução {#multires}
### Contagem máxima de vértices {#multires-lowres-count}
Define um limite para não permitir uma operação de subdivisão de multirres acima desta contagem de polígonos, o que provavelmente travaria o Nomad. O padrão é 10 milhões.
### Limite de baixa resolução {#multires-lowres-threshold}
Uma resolução mais baixa da malha pode ser exibida quando você move a câmera. Você pode aumentar este valor se quiser exibir uma resolução mais alta da malha.

## Configurações {#advanced}
### Restaurar padrão {#reset}
Redefine todas as configurações para seus valores padrão.
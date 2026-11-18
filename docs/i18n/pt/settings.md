# ![](/icons/cog.webp) Ajustes {#reset-to-default}

O menu de ajustes reúne muitas opções para controlar a aparência e o comportamento do Nomad.

![](/images/settings_overview.webp)

A fileira de botões no topo do menu leva direto a uma seção: `Cursor`, `Indicador`, `Armação`, `Grade`, `Dois lados`, `Contorno`, `Destaque`, `Cubo de ajuste`, `Estatísticas`, `Manipuladores`, `Forma`, `Repetidores` e `Multirres`.

## Ajustes de exibição {#display-settings}
Esta seção traz atalhos rápidos para a maioria dos ajustes que aparecem mais abaixo neste menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Sombreamento suave {#smooth-shading}
Alterna entre sombreamento suave e facetado. No facetado, os polígonos são sombreados de forma independente, então dá para ver a topologia por baixo.
Pode ser útil ver o sombreamento facetado durante a escultura e depois mudar para o suave na hora de renderizar.

Desativar o sombreamento suave melhora um pouco o desempenho.

### ![](/icons/outline.webp) Contorno {#outline-quick}
Mostra ou oculta um contorno na seleção atual.

Isso ajuda a ver qual malha (ou quais malhas) está selecionada caso [Escurecer objetos não selecionados](#darken-unselected-objects) esteja desativado.

Em termos de desempenho, usar [Escurecer objetos não selecionados](#darken-unselected-objects) é muito melhor que usar o contorno.

### ![](/icons/grid.webp) Grade {#grid-quick}
Mostra ou oculta uma grade de fundo, útil para entender a posição e a escala dos objetos.

### ![](/icons/culling.webp) Dois lados {#two-sided-quick}
Ativa ou desativa a exibição dos polígonos dos dois lados. Todas as faces apontam para uma direção.
As faces consideradas *verso* são as que apontam "para longe" do ponto de vista da câmera.

Por exemplo, a esfera simples do início tem as faces apontando para fora.
Se você levar a câmera para dentro da esfera, vai ver o verso dessas faces.

Na maior parte do tempo você não deveria ver o verso das faces, então colori-lo ajuda a detectar possíveis problemas ou uma topologia incorreta.

Desativar a renderização em `Dois lados` pode melhorar um pouco o desempenho.


### ![](/icons/wireframe.webp) Armação {#wireframe-quick}
Mostra ou oculta uma sobreposição de armação.

Ativar a armação reduz o desempenho.

### ![](/icons/snap_cube.webp) Cubo de ajuste {#snap-cube-quick}
Mostra ou oculta um ícone auxiliar no canto da cena, útil para se orientar no espaço e alternar rapidamente entre as vistas frontal/traseira/esquerda/direita/superior/inferior.

### ![](/icons/palette.webp) Mostrar pintura {#show-painting}
Mostra ou oculta a pintura. Quando desligado, os objetos aparecem com um material branco não metálico, com 25% de aspereza, em vez da pintura deles.

### ![](/icons/tool_hide.webp) Usar Ocultar {#use-hide}
Ativa ou desativa o modo de ocultação. Quando desligado, a ocultação continua lá, só fica desativada. Este botão fica indisponível se você estiver usando a ferramenta de ocultar.

### ![](/icons/shield.webp) Mostrar máscara {#show-mask}
Ativa ou desativa o modo de máscara. Quando desligado, a máscara continua lá, só fica desativada. Toque de novo neste botão para reativá-la.

Se precisar esconder a máscara E ainda mantê-la ativa, use a cor da máscara mais abaixo e defina-a como branco. Lembre-se de voltar para um cinza quando terminar!

Este botão fica indisponível se você estiver usando uma ferramenta de máscara.

### ![](/icons/shield.webp) Máscara → Opaco {#mask-opaque}
`Máscara → Opaco` ignora os vértices transparentes na máscara. Só tem efeito na opacidade de vértices e de textura; as faces ocultadas com "ocultar" continuam ocultas. Só está disponível enquanto `Mostrar máscara` estiver ligado.

### ![](/icons/bang.webp) Destaque {#highlight-quick}
Ativa ou desativa o flash de destaque da seleção. Ao selecionar objetos, o objeto selecionado pisca por 500 milissegundos. A cor e a duração do flash podem ser personalizadas mais abaixo.

### ![](/icons/list.webp) Estatísticas {#stats-quick}
Mostra ou oculta o texto de estado no visor 3d. Ele mostra informações sobre a memória do sistema, o total de vértices da cena e o número de vértices da seleção atual.

----- 

### ![](/icons/cube.webp) Escurecer objetos não selecionados {#darken-unselected-objects}
Os objetos que não estão selecionados ficam mais escuros, para que a seleção atual se destaque.

### ![](/icons/shield.webp) Máscara {#mask}
A cor usada na máscara, por padrão um cinza médio, multiplicada pela cor do objeto. Defina como branco para deixar a máscara invisível, mas lembre-se de voltar para um cinza quando terminar!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Círculo {#show-circle-while-sculpting}
Quando mostrar o círculo do raio do pincel:

* `Auto` - mostra o círculo, mas o esconde enquanto você esculpe.
* `Não` - nunca mostra o círculo.
* `Sim` - sempre mostra o círculo, mesmo enquanto você esculpe.

### Mostrar ponto pequeno {#show-small-dot}
Mostra um ponto no centro do traço do pincel enquanto você esculpe, ou quando o pivô da câmera muda.

### Mostrar estabilizador de corda {#show-rope-stabilizer}
Desenha uma linha indicando o comprimento da corda quando o [Estabilizador por corda](stroke.md#lazy-rope-stabilizer) está ativo nos ajustes de traçado.

### Mostrar dica de giro {#show-roll-hint}
Mostra o guia da direção de giro enquanto você usa um atalho de rolagem.

### ![](/icons/radius.webp) Tamanho {#dot-size}
O tamanho do ponto pequeno.

### Cores {#cursor-colors}
O cursor muda de cor conforme o que você está fazendo: `Esculpir`, `Fundo` (passando sobre o fundo), `Máscara`, `Suavizar`, `Câmera` e `Raio`. Cada cor pode ser personalizada aqui.

## ![](/icons/cursor.webp) Indicador {#indicator}
![](/images/settings_indicator.webp)

Mostra indicadores visuais para tutoriais e gravações de tela. Defina como `Sim` para ativar (no iOS também existe a opção `Auto`).

Os botões `Dedo`, `Stylus` e `Mouse` mostram um ícone quando esse tipo de entrada é detectado.

### Cor {#indicator-color}
A cor do indicador.

### Tamanho/Ícone/Círculo {#indicator-shape}
Controles para ajustar o tamanho do indicador e a opacidade do ícone e do círculo dentro dele.

## ![](/icons/wireframe.webp) Armação {#wireframe}
![](/images/settings_wireframe.webp)
Ativa a sobreposição de armação.

### Destino {#target}
Define se a armação aparece nos objetos não selecionados, só nos selecionados ou em todos os objetos.

### Ocultar {#hide}
Define se a armação continua aparecendo nos polígonos ocultos.

### Multirresolução: Apenas nível 0 {#multiresolution-level-0-only}
Na multirresolução, a armação do nível 0 aparece mais escura e a dos níveis mais altos vai ficando mais clara. Quando ativada, esta opção mostra apenas a armação do nível 0.

### Cor {#wireframe-color}
Define a cor e a opacidade da armação.

## ![](/icons/grid.webp) Grade {#grid}
![](/images/settings_grid.webp)
Ativa a grade.

### Ajuste {#snap}
Estas opções fazem os pontos das ferramentas baseadas em curvas e formas (`Torno`, `Tubo`, formas de polígono e de caminho...) se encaixarem enquanto você desenha:

* `Ajustar à grade` - encaixa na grade.
* `Ajustar aos pontos (visualização alinhada)` - encaixa nos pontos existentes próximos quando a câmera está alinhada a um eixo.
* `Ajustar aos pontos (vista livre)` - encaixa nos pontos existentes próximos quando a câmera não está alinhada.

### Cor {#grid-color}
Define a cor e a opacidade da grade. Estas opções aparecem quando a grade está visível.

`Vinheta` faz a grade sumir aos poucos em direção às bordas. `Limite de divisão por encaixe` define, em pixels, o quanto as linhas da grade podem ficar densas na tela antes de a grade mudar para outro nível de subdivisão.

## ![](/icons/culling.webp)Dois lados {#two-sided}
Permite ver as faces dos polígonos dos dois lados.

### Cor do verso {#backface-color}
`Verso colorido` ativa a coloração dos versos, e `Cor do verso` define a cor.

## ![](/icons/outline.webp)Contorno {#outline}
Ativa um contorno em volta dos objetos selecionados.

### Cor do contorno, Espessura {#outline-color-thickness}
Define a cor e a `Espessura` do contorno.


## ![](/icons/bang.webp) Destaque {#highlight}
Ativa um flash curto quando a seleção muda.
### Cor, Duração {#color-duration}
Define a cor e a duração do flash, em milissegundos.

## ![](/icons/snap_cube.webp) Cubo de ajuste {#snap-cube}
![](/images/settings_snapcube.webp)

Mostra um ícone auxiliar no canto da cena, útil para alternar rapidamente entre as vistas frontal/traseira/esquerda/direita/superior/inferior. Toque nos lados do cubo para alternar entre as vistas ortográficas.

### Forma {#shape}
Escolha entre uma esfera, um cubo ou um gnômon como forma do cubo de ajuste.

### Restringir alinhamento {#restrict-alignment}
Alinha as vistas de encaixe aos eixos do mundo. Quando ativado, só as 6 vistas principais são possíveis. Em `Auto`, essa restrição só vale quando a câmera está no modo `Mesa giratória`.

### Tamanho {#size}
Define o tamanho do cubo de ajuste.

### Virar 180° {#flip-180}
Ativa um comportamento de toque: se a vista estiver encaixada, tocar no centro do cubo gira a vista em 180 graus. Por exemplo, se a vista estiver encaixada na frente, tocar no cubo leva para a vista de trás.

### Arestas e cantos {#edges-corners}
Adiciona vistas de encaixe nas arestas e nos cantos do cubo (as zonas âmbar). Não disponível com a forma de gnômon.

### Arrastar em mesa giratória {#turntable-drag}
Arrastar o cubo gira a vista sem rolar a câmera, e para em cada vista de encaixe. Desative para arrastar o cubo com a rotação `Trackball`. De um jeito ou de outro, o arraste fica horizontal ou vertical. Com uma câmera em `Mesa giratória`, o cubo sempre é arrastado desse jeito.

### Posição {#snap-position}
Define em qual canto fica o cubo de ajuste.


## ![](/icons/list.webp) Estatísticas {#stats}
![](/images/settings_stats.webp)

Mostra informações sobre a memória do sistema, o total de vértices da cena e o número de vértices da seleção atual.

### Posição {#stats-position}
Define em qual canto ficam as estatísticas.

## ![](/icons/edit_radius.webp) Manipulador {#handle}
Ajustes dos manipuladores que você arrasta no visor, como o gizmo.

### Entrada numérica {#gizmo-input}
Permite digitar valores ao tocar em um dos controles do gizmo.

### Ocultar ao interagir {#hide-on-interaction}
Esmaece o gizmo enquanto você interage com ele, para que não atrapalhe.

### ![](/icons/opacity.webp) Opacidade {#handle-opacity}
A opacidade dos manipuladores.

## ![](/icons/shape_lasso.webp) Forma {#shape-settings}
Como as formas que você desenha com traçados de forma (laço, retângulo, curva...) aparecem na tela.

### ![](/icons/opacity.webp) Preenchimento, Contorno {#shape-fill-outline}
A opacidade do interior da forma e da linha em volta dela.

### Cores {#shape-colors}
A cor da forma para cada tipo de ferramenta: `Máscara`, `Ocultar`, `Grupo de faces` e `Aparar`.

## ![](/icons/array.webp) Repetidores {#primitive-repeaters}
Limites para as cópias feitas pelos [repetidores](scene#repeaters) (matriz, radial, curva, superfície). Eles mantêm o Nomad responsivo quando um repetidor sai do controle.

### ![](/icons/cube.webp) Máx. cópias {#repeater-max-copies}
O número máximo de cópias que um único repetidor faz. O Nomad sofre com muitos objetos, seja qual for o tamanho deles.

### ![](/icons/cube.webp) Cópias na cena {#repeater-scene-copies}
O limite de cópias para a cena inteira. Uma cópia com poucos polígonos custa pouca geometria, mas continua sendo um objeto completo, então este é o limite que as cópias pequenas atingem primeiro.

### ![](/icons/triangle.webp) Máximo de faces {#repeater-max-faces}
O limite de faces para todas as cópias da cena. Acima dele, os objetos mais pesados perdem cópias primeiro.

## ![](/icons/multires.webp) Multirresolução {#multires}
### Contagem máxima de vértices {#multires-lowres-count}
Define um limite para impedir uma subdivisão de multirresolução acima desse número de vértices, que provavelmente faria o Nomad travar: o Nomad não verifica a memória disponível antes de subdividir. O padrão é 10 milhões.
### Limite de baixa resolução {#multires-lowres-threshold}
Uma resolução mais baixa da malha pode ser mostrada quando você move a câmera. Aumente este valor se quiser mostrar uma resolução maior da malha.

## Ajustes {#advanced}
### ![](/icons/reset.webp) Redefinir padrão {#reset}
Redefine todas as preferências do app para os valores padrão.

Alguns recursos são salvos separadamente e NÃO são redefinidos: projetos, atalhos de teclado, pré-ajustes de ferramentas, ambientes HDR, MatCaps, alfas, texturas de pincel e imagens de referência. Tudo o que é salvo com o projeto, como a iluminação, o pós-processamento ou as vistas de câmera, também fica intacto.

# ![](/icons/operation.webp) Operação {#operation}

Este menu aplica uma operação a toda a superfície dos objetos selecionados de uma só vez: suavizar, relaxar, polir, inflar, ajustar as cores, desfocar ou aumentar a nitidez da pintura e da máscara.

![](/images/operation_overview.webp)

## Visão geral {#overview}

Enquanto um pincel age onde você passa o traço, uma operação age em todos os vértices dos objetos selecionados de uma vez. O título mostra o nome do objeto, ou o número de objetos quando vários estão selecionados.

Cada operação é um controle deslizante: arraste para a direita para aplicar mais, e para a esquerda para aplicar menos (ou a operação oposta, nos controles com uma seta dos dois lados). O controle volta a zero quando você solta, e cada arraste é um único passo no [Histórico](history.md), então você pode aplicar uma operação várias vezes em pequenas doses.

::: tip
As operações são um jeito rápido de limpar uma malha inteira depois de um remalhamento por voxels ou de uma booleana: um pouco de `Relaxar` uniformiza os triângulos, um pouco de `Suavizar` remove o ruído, sem precisar caçar cada ponto com um pincel.
:::

## Filtros {#filters}

Os botões no topo limitam onde as operações se aplicam:

* `Máscara` - As áreas mascaradas não são afetadas.
* `Ocultar` - As áreas ocultas não são afetadas.
* `Deslocamento` - (Com uma [camada](layers.md) selecionada) Só as áreas onde a camada ativa tem escultura são afetadas, assim você pode suavizar ou inflar o conteúdo de uma camada sem mexer no resto.

## Suavização {#smoothing}

* `Manter volume` - Suaviza sem encolher a superfície. O botão de engrenagem guarda os valores de `Encolher` e `Inflar` usados para isso.
* `Manter bordas` - Os vértices na borda da malha (a beirada de um buraco) ficam parados.
* `Suavização estável` - Tenta tornar a suavização independente da topologia. Funciona melhor quando a densidade de polígonos varia muito.
* `Suavizar` - Suaviza a superfície. Arraste para a esquerda para `Aumentar nitidez` em vez disso.
* ![](/icons/group.webp) `Suavizar` - Suaviza as bordas entre os [grupos de faces](tools.md#facegroup), endireitando contornos de grupo serrilhados. Arraste para a esquerda para deixá-los mais nítidos.
* `Relaxar` - Uniformiza os polígonos, mantendo a forma.
* ![](/icons/group.webp) `Relaxar` - Relaxa os polígonos ao longo das bordas dos grupos de faces.
* `Manter cantos` - Com `Suavizar` e `Relaxar` de grupos de faces, as bordas ficam fixas onde fazem uma curva maior que este ângulo, de modo que os cantos continuam vivos enquanto os lados são suavizados. Use a caixa de seleção para ativá-lo.

## Polir {#polish}

Achata a superfície em facetas limpas, como a ferramenta [Polir](tools.md#polish). `Ângulo` define quais faces são achatadas juntas: faces que se curvam menos que esse ângulo viram uma única faceta. Um ângulo menor mantém mais vincos e facetas menores.

## Inflar {#inflate}

Empurra a superfície para fora ao longo das normais, ou para dentro quando você arrasta para a esquerda. `Normal (Relaxar)` relaxa os polígonos ao mesmo tempo, para que não se estiquem; use a caixa de seleção para desativá-lo.

## Ajustes de cor {#color-adjustments}

Escolha o canal a ajustar, `Cor`, `Aspereza`, `Metalidade`, `Opacidade`, `Densidade` (a pintura de densidade do [Quad Remesher](tools.md#quad-remesher), quando o objeto tem alguma) ou `Máscara`, e depois:

* `Exposição` - Clareia ou escurece os valores.
* `Saturação` - (Só `Cor`) Cores mais ou menos vivas.
* `Contraste` - Afasta os valores entre si, ou os aproxima.
* `Matiz` - Desloca as cores ao longo do círculo cromático.

## Desfoque {#blur}

Desfoca os canais selecionados pela superfície: ative `Cor`, `Aspereza`, `Metalidade`, `Opacidade`, `Densidade` ou `Máscara` e arraste `Desfocar`. Arraste para a esquerda para `Aumentar nitidez` em vez disso.

Para a máscara, é o mesmo que o controle `Desfocar` da ferramenta [Máscara](tools.md#mask). Aqui você também pode desfocar os canais de pintura.

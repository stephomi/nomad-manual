# ![](/icons/transform.webp) Transformar {#transform}

Este menu mostra em números a transformação do objeto selecionado: onde ele está, como está girado e escalado, e qual é o seu tamanho. Digite valores exatos, redefina-os ou sele-os na malha.

![](/images/transform_overview.webp)

## Visão geral {#overview}

Todo objeto tem um nó que guarda sua translação, rotação e escala (sua matriz), além dos vértices. As ferramentas [Gizmo](tools.md#gizmo) e [Transformar](tools.md#transform) alteram essa matriz quando você arrasta no visor; este menu permite ler a matriz e digitar os valores. Veja [Nós e vértices](tools.md#nodes-and-vertices) para entender a diferença entre mover o nó e mover os vértices.

Arraste um valor para a esquerda ou para a direita para alterá-lo, ou toque nele para digitar um número. Os valores X, Y e Z são coloridos de vermelho, verde e azul, como os eixos do gizmo.

::: tip
Digitar valores é prático para posicionar objetos com precisão, por exemplo para colocar várias peças exatamente na mesma altura, ou para voltar uma rotação a um número redondo depois de girar livremente com o gizmo.
:::

## Matriz {#matrix}

O título indica em que espaço os valores estão expressos: `local` (relativo ao objeto pai) ou `mundo`.

### Objeto e Pivô {#object-pivot}

* `Objeto` - Os valores são a própria transformação do objeto.
* `Pivô` - Os valores controlam a seleção a partir do seu [pivô](tools.md#pivot), do mesmo jeito que as alças do gizmo: as linhas mostram zero, e alterá-las move, gira ou escala a seleção em torno do pivô. Ative `Editar` (o ícone de cadeado) para mover só o pivô, sem mexer nos objetos.

### Local e Mundo {#local-world}

Quando o objeto tem um pai ou filhos, ou vários objetos estão selecionados, você pode escolher em que espaço os valores são mostrados: `Local` (relativo ao pai) ou `Mundo`.

### Ações {#actions}

| Ação          | Ícone                         | Descrição |
| :-----------: | :---------------------------: | :---------- |
| Mover origem  | ![](/icons/target.webp)      | Move o objeto para a origem do mundo. |
| Selar         | ![](/icons/bake.webp)        | Aplica a matriz aos vértices e redefine a matriz. Visualmente nada muda, mas a origem do objeto passa a ser a origem do mundo. |
| Pivô          | ![](/icons/gizmo.webp)       | Sela o pivô no objeto: a origem e a orientação do objeto passam a ser as do pivô. Visualmente nada muda. |
| Editar        | ![](/icons/lock.webp)        | (Modo `Pivô`) Move só o pivô. |
| Redefinir     | ![](/icons/reset.webp)       | Redefine a transformação para a identidade. No modo `Pivô`, recoloca o pivô no lugar. |

Quando o objeto selecionado tem instâncias, selar pede confirmação, com uma opção `Desinstanciar`: selar altera os vértices, que são compartilhados pelas instâncias.

### Translação, Rotação, Escala {#translation-rotation-scale}

A posição, a rotação (em graus) e a escala do objeto, em X, Y e Z. Os dois botões no fim de cada linha selam apenas essa parte da transformação nos vértices, ou a redefinem.

Uma linha `Cisalhamento` também aparece quando o objeto está cisalhado, por exemplo depois de uma escala não uniforme de um pai girado.

### Escala uniforme {#uniform-scale}

Quando ativada, a escala é um único valor, igual nos três eixos. Desative para escalar X, Y e Z separadamente.

## Dimensão {#dimension}

O tamanho e o centro da caixa delimitadora da seleção, em unidades do mundo. Com vários objetos selecionados, ela abrange todos.

* `Tamanho` - A largura, a altura e a profundidade. Com o botão de corrente ativado, mudar um tamanho escala os outros dois na mesma proporção, mantendo as proporções.
* `Centralizado` - O centro da caixa delimitadora. O botão de alvo move a seleção para que o centro dela fique na origem do mundo.

::: tip
`Tamanho` é o jeito mais rápido de dar a um objeto um tamanho real, por exemplo antes de uma impressão 3d: defina a altura desejada e a corrente mantém as proporções.
:::

# ![](/icons/history.webp) Histórico {#history}
![](/images/history_overview.webp)

Como na maioria das ferramentas de criação, você pode desfazer/refazer qualquer edição no Nomad.
O histórico pode ficar grande, então você controla quanto dele fica na memória, quanto é guardado no armazenamento e se ele é salvo com o projeto.

::: tip
Você pode usar gestos rápidos para desfazer/refazer:
- Toque com 2 dedos para desfazer
- Toque com 3 dedos para refazer
:::

## ![](/icons/history.webp) Histórico {#history-panel}
![](/images/history_history.webp)

Este painel mostra a pilha do histórico: o número de etapas, o nome da operação, o objeto em que ela foi aplicada e quanta memória cada etapa ocupa.

Toque em uma entrada para voltar (ou avançar) até aquele estado. Mantenha uma entrada pressionada para apagar definitivamente ela e todo o histórico mais antigo: um jeito rápido de liberar memória quando você estiver satisfeito com a escultura.

### ![](/icons/speed.webp) Reproduzir {#replay}
O botão de play no canto inferior esquerdo volta até a raiz e depois refaz as operações uma a uma, um jeito divertido de ver sua escultura sendo construída. O controle define a velocidade em operações por segundo. Toque no botão de novo para parar; desfazer/refazer ou tocar em uma entrada também interrompe a reprodução.

Antes de começar, uma janela permite escolher:
* `Inverter` - Desfaz do estado atual até a raiz, em vez de reproduzir a partir da raiz.
* `Restaurar câmera` - A câmera acompanha as operações reproduzidas, mesmo com [Restaurar câmera](#restore-camera) desativado.
* `Suavização da câmera` - A câmera desliza entre as vistas em vez de pular de uma para outra. Valores mais altos deixam a câmera mais calma.

::: warning
A reprodução é experimental.
:::

## Incluir ações {#include-actions}

Os ícones na parte inferior do painel Histórico escolhem que tipo de edição é registrado no histórico:

| Ação        | Ícone                         | Descrição                                                                           |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Luzes       | ![](/icons/light.webp)        | Edições de luzes. Mover uma luz com o Gizmo é sempre registrado, pois pode afetar outros objetos na hierarquia da cena |
| Sombreamento | ![](/icons/sun.webp)         | Os modos PBR, MatCap e Sem iluminação, as MatCaps e os HDRIs                        |
| Pós-processamento | ![](/icons/postprocess.webp) | Edições de pós-processamento                                                  |
| Seleção     | ![](/icons/tool_lattice.webp) | Edições da seleção da Grade, como cliques, seleções com laço e desseleção        |

## Ajustes {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Restaurar câmera {#restore-camera}
Para cada operação, o ponto de vista da câmera é salvo.
Se você ativar esta opção, desfazer ou refazer uma operação leva a câmera de volta ao ponto de vista salvo.

### ![](/icons/history.webp) Salvar histórico {#save-history}
Mantém o histórico de desfazer quando o projeto é salvo, para que ele continue lá ao reabrir o projeto. Desative para deixar seus arquivos de projeto menores.

### ![](/icons/ram.webp) Limite de RAM {#history-limit-mb}
A quantidade máxima de histórico mantida na RAM. Os estados mais antigos vão para o armazenamento e são carregados de novo quando necessário; eles não são apagados.

### ![](/icons/save.webp) Limite de armazenamento {#storage-limit}
A quantidade máxima de armazenamento usada pelo histórico deste projeto. Quando o limite é atingido, as operações mais antigas são apagadas definitivamente.

::: tip
Um novo limite passa a valer após a próxima edição, desfazer ou refazer.
:::

### ![](/icons/undo.webp) Aviso ao desfazer {#maximum-undoable}
Voltar mais do que esse número de operações de uma só vez pede uma confirmação antes. Se você fizer uma edição depois disso, todas as operações após aquele ponto são perdidas; então isso protege você de um toque acidental lá no fim da lista.

## Estatísticas de memória {#memory-stats}

Esta seção mostra em detalhes a memória usada pelo Nomad.

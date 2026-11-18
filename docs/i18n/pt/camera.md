# ![](/icons/camera.webp) Câmera {#camera}

Este menu permite criar e modificar câmeras, além de controlar como você interage com elas.

![](/images/camera_overview2.webp)

As câmeras no Nomad têm vários usos:

* Preparar vistas para esculpir a partir de ângulos precisos
* Enquadrar seus objetos, como uma câmera fotográfica
* Navegar pela cena como uma câmera em primeira pessoa
* Servir de câmera ortográfica para jogos isométricos ou renderizações em estilo industrial.

## Controlar a câmera {#control}

### Rotação {#rotation}
Você gira a câmera arrastando *um* dedo sobre o fundo.
Se arrastar o dedo sobre o modelo, você vai começar a esculpir.

::: tip Dá para girar a câmera se eu não tiver acesso ao fundo?
Sim, coloque *dois* dedos na tela, como se fosse começar um gesto de mover/zoom, e depois solte *um* dos dedos.
:::

### Focar / Redefinir {#focus}
*Toque duas vezes* no modelo para focar no ponto tocado.
Se *tocar duas vezes* no fundo, a câmera vai focar na malha selecionada ou na cena inteira, veja [Toque duas vezes no fundo](#dtap-tap-background).


### Translação {#translation}
Movendo *dois* dedos, você desloca a câmera lateralmente.


### Zoom {#zooming}
Use o gesto de pinça para aproximar ou afastar.


### Rolagem {#rolling}
Você pode *rolar* a vista girando *dois* dedos.
::: warning
Este gesto só está disponível nos modos de rotação `Trackball`.
:::

### Controles no computador {#desktop}

No computador, a tecla alt/opt é usada para controlar a câmera:

* arrastar a ponta em um espaço vazio = girar a câmera
* alt + arrastar a ponta = mover lateralmente
* alt + arrastar a ponta, depois soltar o alt = zoom (como no ZBrush)

Com tablets Wacom que têm 2 ou mais botões na caneta, use os ajustes da Wacom para configurar a ponta e os botões assim:

* ponta = clique esquerdo
* botão inferior = clique do meio
* botão superior = clique direito

Com esses ajustes, você consegue controlar a câmera só com a caneta:

* botão superior e movimento sem encostar = girar a câmera
* botão inferior e movimento sem encostar = mover lateralmente

## Controles da câmera {#camera-controls}

![](/images/camera_list.webp)

### Vistas {#views}
Você pode salvar pontos de vista da câmera com `Adicionar Visualização`.
Se clicar no nome da vista, a câmera volta para essa vista.


::: tip
Uma vista salva guarda os ajustes de [Tipo de projeção](#projection) e também a [Imagem de referência](background.md).  
Isso é útil se você quiser alternar entre vistas de referência frontal/esquerda/traseira com fundos diferentes.
:::

| Ação                   | Ícone                         | Descrição                                                                    |
| :--------------------: | :---------------------------: | :--------------------------------------------------------------------------: |
| Visibilidade           | ![](/icons/eye_open.webp)    | Ativa ou desativa a câmera. Câmeras ocultas são puladas pelos botões anterior/próxima |
| Nome                   |                               | Seleciona a câmera                                                           |
| Imagem                 | ![](/icons/image.webp)       | Uma miniatura da imagem de referência, se houver uma ligada à câmera         |
| Projeção               | ![](/icons/perspective.webp) | A projeção da câmera, com o campo de visão quando em perspectiva             |
| Atualizar visualização | ![](/icons/update_view.webp) | Atualiza a vista salva com o ponto de vista atual                            |
| Editar nome            | ![](/icons/pencil.webp)      | Edita o nome da câmera                                                       |
| Apagar                 | ![](/icons/trash.webp)       | Apaga a câmera                                                               |

### ![](/icons/camera_add.webp) Adicionar Visualização {#add}
Cria uma nova câmera a partir da vista atual.

### ![](/icons/camera.webp) Ícones {#icons-test}

Mostra ou oculta os ícones das câmeras no visor. O botão aparece ao lado de `Adicionar Visualização` assim que você tiver uma câmera. O ícone de uma câmera selecionada fica sempre visível.

### Tipo de projeção {#projection}
Escolha entre `Perspectiva` e `Ortográfica`.

Em perspectiva, você pode mudar o `Campo de visão vertical` (FoV) da câmera. A distância focal equivalente de uma câmera 35mm aparece acima do controle deslizante, prático se você estiver acostumado com fotografia.
Para esculpir, costuma-se recomendar um FoV baixo, pois ajuda a manter as proporções.  
O modo `Ortográfica` equivale mais ou menos a um FoV igual a 0.

### Primeira Pessoa {#fps}
Só em perspectiva. Coloca o pivô diretamente na câmera, em vez de na escultura. Arrastar um dedo no fundo mantém a posição da câmera fixa e muda apenas a rotação, como nos jogos em primeira pessoa. Útil para esculpir ambientes em vez de objetos isolados.

![](/images/camera_rotation_ortho_view.webp)

### Tipo de rotação {#rotation-type}
Por padrão, a câmera usa o modo de rotação `Mesa giratória`.
Isso significa que você tem apenas dois graus de liberdade: é mais intuitivo, mas em alguns casos você vai querer mais flexibilidade.  
Você pode mudar para `Trackball` e assim *rolar* a vista girando *dois* dedos no visor. Há dois modos `Trackball`: o primeiro rola a vista como uma bola sob o seu dedo, enquanto o segundo (com o ícone de setas) gira a vista a partir do movimento horizontal e vertical do arraste, o que pode ser mais familiar para alguns usuários.

### Ajuste ortográfico {#orthographic}

Quando ativado, se você tiver um teclado, segurar Shift enquanto gira a vista encaixa a câmera na vista frontal/traseira/superior/inferior/esquerda/direita mais próxima e deixa a câmera ortográfica. A câmera também fica ortográfica quando você clica no navegador para ir à vista frontal/traseira/esquerda/direita/superior/inferior.

### Redefinir visualização {#reset}

Leva a câmera para a frente e enquadra a cena inteira na vista.

### Ajustar visualização {#snap}
Encaixa na vista frontal/traseira/esquerda/direita/superior/inferior mais próxima. Se você já estiver em uma dessas vistas, clicar de novo gira 180 graus para o lado oposto.

### Velocidade {#speed}

Se achar que a câmera se move devagar ou rápido demais, você pode definir um multiplicador de velocidade para `Rotação`, `Zoom` e `Translação`. Útil se a sua escultura for muito grande ou muito pequena.

### Visão geral do pivô {#pivot}

Ao girar a câmera, você vê um pequeno ponto rosa: é o ponto de pivô da câmera.  
É muito importante entender onde está o pivô, para não se perder nem se frustrar com a câmera.

Por padrão, o pivô é atualizado por estas operações:
- tocar duas vezes no modelo
- tocar duas vezes no fundo (o novo pivô fica no centro da sua malha)
- colocar *dois* dedos na tela (mover/zoom/rolar) atualiza o pivô para o centro entre os *dois* dedos

### Atualizar pivô... {#update-pivot}

Você pode personalizar ainda mais quando o pivô é atualizado com estas opções:

* `Ao mover a câmera` - Atualiza o pivô quando você começa a interagir com a câmera.
* `Permitir pivô no ar` - Permite um novo pivô mesmo quando você dá zoom fora da superfície do objeto. Requer `Ao mover a câmera`.
* `Ao tocar duas vezes` - Atualiza o pivô de rotação quando você toca duas vezes na superfície do objeto.
* `Esculpir (Traçado)` - Atualiza o pivô quando você esculpe.

::: tip
Quando estiver acostumado, você pode ocultar o ponto rosa (a dica) no menu [Ajustes](settings.md).
:::

### Centralizar a visão ao afastar o zoom {#center-view-when-zooming-out}
Ao afastar o zoom, a câmera não se desloca para os lados: ela só recua, então a vista continua centralizada.

### Toque duas vezes no objeto {#dtap-object}
Quando ativado, tocar duas vezes em um objeto foca a câmera no ponto tocado.

### Toque duas vezes no fundo {#dtap-tap-background}
Quando ativado, tocar duas vezes no fundo foca a câmera em:
* `Seleção` - Os objetos selecionados.
* `Cena` - A cena inteira.
* `Alternar` - Alterna entre os dois a cada toque duplo. Há duas opções `Alternar`, que diferem por qual vem primeiro, como os ícones mostram.

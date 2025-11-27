# ![](/icons/camera.webp) Câmera

Este menu permite criar e modificar câmeras, além de controlar como você interage com elas.

![](/images/camera_overview2.webp)

As câmeras no Nomad têm vários usos:

* Configurar vistas para esculpir a partir de ângulos precisos
* Usar como uma câmera fotográfica para enquadrar seus objetos
* Como uma câmera em primeira pessoa para navegar na sua cena
* Como uma câmera ortográfica para jogos isométricos ou renderização em estilo industrial.

## Controlando a câmera

### Rotação
Você rotaciona a câmera arrastando *um* dedo no fundo.
Se você arrastar o dedo sobre o seu modelo, em vez disso será iniciada a operação de escultura.

::: tip Posso rotacionar a câmera se não consigo acessar o fundo?
Sim, você pode colocar *dois* dedos na tela – como se quisesse iniciar um gesto de pan/zoom – e então soltar *um* dedo.
:::

### Foco / Reset
*Toque duplo* no modelo para focar o ponto selecionado.
Se você der *toque duplo* no fundo, a câmera focará na malha selecionada.

### Translação
Movendo *dois* dedos, você pode fazer pan com a câmera.

### Zoom
Usando o gesto de pinça você pode dar zoom in/out.

### Rolagem
Você pode *rolar* a vista rotacionando *dois* dedos.
::: warning
Este gesto só está disponível para o modo de rotação `trackball`.
:::

### Controles no desktop

No desktop, a tecla alt/opt é usada para controlar a câmera:

* ponta arrastar em espaço vazio = rotacionar câmera
* alt+ponta arrastar = pan
* alt+ponta arrastar, depois soltar alt = zoom (igual ao zbrush)

Com mesas digitalizadoras Wacom que têm 2 ou mais botões na caneta, use as configurações da Wacom para configurar a ponta e os botões assim:

* ponta = clique esquerdo
* rocker inferior = clique do meio
* rocker superior = clique direito

Com essas configurações, você pode manipular a câmera apenas com a caneta:

* rocker superior e movimento em hover = rotacionar câmera
* rocker inferior e movimento em hover = pan

## Controles da câmera

![](/images/camera_list.webp)

### Vistas
Você pode salvar pontos de vista de câmera usando `Add View`.
Se você clicar no nome da vista, a câmera restaurará essa vista.

::: tip
Uma vista salva também salvará as configurações de [Projection Type](#projection-type) e também a [Reference image](background.md).  
Isso pode ser útil se você quiser alternar entre vistas de referência frente/esquerda/costas com fundos diferentes.
:::

| Ação        | Ícone                         | Descrição                                                                   |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilidade| ![](/icons/eye_open.webp)    | Alternar a câmera. Câmeras ocultas serão ignoradas pelos botões anterior/próximo |
| Nome        |                               | Selecionar a câmera                                                        |
| Imagem      | ![](/icons/image.webp)       | Uma miniatura de uma imagem de referência se ela estiver vinculada à câmera |
| Update View | ![](/icons/update_view.webp) | Atualizar a vista salva com o ponto de vista atual                         |
| Edit Name   | ![](/icons/pencil.webp)      | Editar o nome da câmera                                                    |
| Delete      | ![](/icons/trash.webp)       | Excluir a câmera                                                           |

### ![](/icons/tool_view.webp) Add View
Criar uma nova câmera baseada na vista atual.

### ![](/icons/camera.webp) Icons

Alternar se os ícones de câmera são visíveis no viewport. Se uma câmera estiver selecionada, seu ícone estará sempre visível.

### Projection Type
Você pode alterar o `Field of View` (FOV / distância focal) da sua câmera.
Geralmente é recomendado usar um FOV baixo para fins de escultura, pois isso pode ajudar na proporção.  
Você também pode usar o modo `Orthographic`, que é mais ou menos similar a um FOV igual a 0.

### First Person
Ativa a definição do pivô diretamente na câmera, em vez de na escultura. Arrastar um dedo no fundo manterá a posição da câmera travada, mas mudará a rotação, de forma semelhante a como funcionam jogos em primeira pessoa. Útil ao esculpir ambientes em vez de objetos únicos.

![](/images/camera_rotation_ortho_view.webp)

### Rotation Type
Por padrão a câmera usa o modo de rotação `Turntable`.
Isso significa que você tem apenas dois graus de liberdade; é mais intuitivo, mas em alguns casos você vai querer mais flexibilidade.  
Você pode alternar para `Trackball`; você poderá *rolar* a vista rotacionando *dois* dedos no viewport. No desktop há um modo alternativo de trackball que pode ser mais familiar para alguns usuários.

### Orthographic snap

Quando ativado, se você tiver um teclado, manter pressionado shift enquanto rotaciona a vista fará a câmera encaixar na vista frontal/traseira/superior/inferior/esquerda/direita mais próxima e tornará a câmera ortográfica. A câmera também será tornada ortográfica quando o cubo de vista for clicado para encaixar em frente/costas/esquerda/direita/topo/base.

### Reset view

Mover a câmera para a frente e enquadrar a cena na vista.

### Snap view
Encaixar na vista frontal/traseira/esquerda/direita/superior/inferior mais próxima. Se você já estiver em uma dessas vistas, clicar novamente fará o encaixe em 180 graus para o lado oposto.

### Speed

Se você achar que a câmera se move muito devagar ou muito rápido, pode definir um multiplicador de velocidade para `rotation`, `translation` e `zooming`. Útil se sua escultura for muito grande ou muito pequena.

### Pivot overview

Quando você rotaciona a câmera, pode ver um pequeno ponto rosa: este é o ponto de pivô da câmera.  
É muito importante entender onde está o seu pivô para que você não se perca ou fique frustrado com a câmera.

Por padrão o pivô é atualizado através destas operações:
- toque duplo no modelo
- toque duplo no fundo (o novo pivô ficará no centro da sua malha)
- colocar *dois* dedos na tela (pan/zoom/rolagem) atualizará o pivô para o centro dos *dois* dedos

### Update Pivot...

Você pode personalizar ainda mais a atualização do pivô com estas opções:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Quando você estiver acostumado, pode ocultar o ponto rosa (dica) se for nos menus de [Settings](settings.md).
:::

### Double tap on object
Quando `Focus` está ativado, o toque duplo moverá o pivô para o objeto tocado.

### Double tap on background
Quando ativado, define o pivô para ser um entre Selection, Scene, ou alternar entre eles.

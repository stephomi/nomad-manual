# ![](/icons/image.webp) Plano de fundo

Este menu controla a cor de fundo do Nomad, bem como quaisquer imagens de referência a serem usadas.

![](/images/background_overview.webp)

## Plano de fundo 
![](/images/background_selector.webp)

Há três opções para o plano de fundo da viewport.

* `Environment` - Mostra o mapa de ambiente selecionado em [Shading](shading). Isso pode ser controlado adicionalmente com os controles de Blur e Exposure (brilho). 
* `Color` - Uma cor chapada que você pode escolher
* `Gradient` - Um degradê de cor de cima para baixo. O controle deslizante Factor permite determinar o ponto médio do degradê.  

## Imagem de referência

![](/images/background_reference.webp)

Você pode adicionar uma imagem de sua escolha no plano de fundo para ser usada como referência.
Você pode alterar a posição e a escala, por exemplo, se quiser movê-la para o canto da tela.

### ![](/icons/tool_transform.webp) Transform 

Este botão permite posicionar a imagem de referência de forma interativa. Use 2 dedos para mover, redimensionar e girar a imagem de referência até o lugar desejado. A posição final será refletida nos controles deslizantes abaixo:

* `Overlay` - em 0% a imagem de referência ficará sempre atrás dos seus objetos, em 100% ela ficará na frente. 
* `Opacity` - Quão transparente é a imagem.
* `Position` - A posição X e Y da imagem.
* `Rotation` - Rotação da imagem.
* `Scale` - Escala da imagem.


::: tip

Câmeras e imagens de referência são vinculadas. 

Isso significa que, se você configurar sua imagem de referência para se alinhar com a sua escultura e criar uma câmera a partir do [menu Camera](camera), a posição, rotação e escala da imagem de referência também serão armazenadas com a câmera. Você pode desativar a imagem de referência, girar para outra viewport. Se você voltar a olhar pela câmera, a imagem de referência será ativada com as configurações que você usou.

Isso inclui até escolher imagens diferentes para câmeras diferentes!

 ![](/videos/reference_camera.mp4)

:::

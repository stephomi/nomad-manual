# ![](/icons/image.webp) Fundo {#background}

Este menu controla a cor de fundo do Nomad e as imagens de referência que você quiser usar.

![](/images/background_overview.webp)

## Tipo {#type}
![](/images/background_selector.webp)

Há três opções para o fundo da viewport.

* `Ambiente` - Mostra o mapa de ambiente escolhido em [Sombreamento](shading.md). Você pode ajustá-lo com os controles `Desfoque` e `Exposição` (brilho).
* `Cor` - Uma cor sólida, à sua escolha.
* `Gradiente` - Uma transição entre duas cores. O controle `Fator` move o ponto médio do gradiente.

### Tipo de gradiente {#gradient-type}
Com `Gradiente`, escolha o formato:
* `Linear` - Um gradiente reto, com a direção definida pelo controle `Ângulo`.
* `Radial` - Um gradiente circular que parte do centro da tela.
* `Céu` - Um gradiente preso ao horizonte do mundo, que acompanha a câmera quando você olha para cima ou para baixo.

Cada cor tem um botão de redefinir e um conta-gotas, para pegar uma cor da tela.

## ![](/icons/lock.webp) Sincronizar com bloqueio da câmera {#sync-on-camera-lock}
Quando a câmera está bloqueada pelo [Navegador](settings.md#snap-cube), a imagem de referência acompanha o movimento da câmera e continua alinhada com a sua escultura.

* `Permitir giro (trackball)` - Permite que a câmera gire sobre o próprio eixo quando você sai do bloqueio da câmera.
* `Redefinir vista ao desbloquear` - Redefine a vista quando você sai do bloqueio da câmera.

## Imagem de referência {#reference}

![](/images/background_reference.webp)

Você pode colocar no fundo uma imagem da sua escolha para usar como referência. Toque em `Importar...` para adicionar uma e marque `Imagem de referência` para exibi-la.
Dá para mudar a posição e a escala, por exemplo para levá-la a um canto da tela.

### ![](/icons/tool_transform.webp) Transformar {#transform}

Este botão permite posicionar a imagem de referência de forma interativa. Use 2 dedos para mover, redimensionar e girar a imagem até o lugar certo. `Redefinir ajustes` devolve a imagem à posição padrão. O posicionamento final aparece nos controles abaixo:

* `Sobreposição` - Em 0%, a imagem de referência fica sempre atrás dos objetos; em 100%, fica na frente.
* `Opacidade` - O quanto a imagem é transparente.
* `Pós-processamento` - Aplica os efeitos de pós-processamento à imagem de referência. Desative para manter as cores originais.
* `Posição X` / `Posição Y` - A posição X e Y da imagem.
* `Escala` - A escala da imagem.
* `Rotação` - A rotação da imagem.


::: tip

Câmeras e imagens de referência são vinculadas.

Ou seja: se você alinhar a imagem de referência com a sua escultura e depois criar uma câmera no [menu Câmera](camera.md), a posição, a rotação e a escala da imagem de referência ficam salvas junto com a câmera. Você pode desligar a imagem de referência e girar para outro ponto de vista. Ao olhar de novo pela câmera, a imagem de referência volta a ser ativada com os ajustes que você usou.

Dá até para escolher imagens diferentes para câmeras diferentes!

 ![](/videos/reference_camera.mp4)

:::

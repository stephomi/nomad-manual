# ![](/icons/sun.webp) Sombreamento {#shading}

Este menu controla os modos de sombreamento usados pelo Nomad, as propriedades da iluminação, o ambiente e o matcap, e a névoa.

![](/images/shading_overview.webp)



Você pode escolher entre vários modos de renderização:

| Modo                        | Significado                | Descrição                                                       |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Iluminado (PBR)](#pbr)     | Renderização baseada em física (Physically Based Rendering) | Luzes, sombras, ambiente e metalidade/aspereza pintadas |
| [MatCap](#matcap)           | Captura de material (Material Capture) | Modo rápido para esculpir, que usa menos a GPU/CPU do que o PBR |
| [Sem iluminação](#unlit)    | Cor da superfície          | Só a cor da superfície, sem sombreamento nem iluminação         |
| [ID do objeto](#object-id)  | ID do objeto               | Uma cor aleatória por objeto, útil em aplicativos de pintura.   |
| [ID da instância](#instance-id) | ID da instância        | Uma cor aleatória por instância, útil para identificar malhas compartilhadas |

Para saber mais sobre metalidade e aspereza, veja a seção [Pintura](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Grupo de faces {#face-group}
Mostra as cores dos grupos de faces por cima do modelo. Os grupos de faces são seleções coloridas de polígonos, que podem ser criadas com a ferramenta [Grupo de faces](tools#facegroup) e são feitas automaticamente pela maioria das primitivas.

Algumas ferramentas filtram automaticamente pelos grupos de faces quando eles estão visíveis.

### ![](/icons/palette.webp) Mostrar pintura {#show-paint}
O Nomad pode guardar a cor, a aspereza e a metalidade nos vértices da sua escultura. Esta caixa de seleção liga ou desliga a exibição dessas propriedades de forma global.

Note que, se você tiver ao mesmo tempo propriedades de vértices e texturas, e as duas estiverem ativadas, os valores são multiplicados.

### ![](/icons/shield.webp) Mostrar máscara {#show-mask}
Liga ou desliga a sobreposição em tons de cinza das [ferramentas de máscara](tools#mask). Quando está desativada, a máscara também fica desativada: é útil para fazer mudanças rápidas sem a máscara e depois reativá-la sem perder nada.

### ![](/icons/tool_hide.webp) Usar Ocultar {#use-hide}

Liga ou desliga as faces ocultas. Note que isso só funciona se você NÃO estiver na ferramenta Ocultar!

### ![](/icons/image.webp) Usar texturas {#use-textures}

O Nomad permite atribuir texturas aos objetos pelo menu [Material](material). Se houver texturas atribuídas, esta caixa de seleção as liga ou desliga de forma global.

Não é possível criar nem editar texturas no Nomad, mas as texturas de arquivos importados funcionam. As texturas de opacidade funcionam nos modos Iluminado, MatCap e Sem iluminação, os mapas de normais em Iluminado e MatCap, a cor em Iluminado e Sem iluminação, e a emissão, a aspereza e a metalidade só em Iluminado. O botão fica acinzentado quando a cena não tem nenhuma textura.

### Visão geral do PBR e das luzes {#pbr}
Este manual não vai entrar nos detalhes da renderização baseada em física (PBR).

Uma coisa importante para ter em mente é que a iluminação e o material são totalmente separados.
Isso significa que você pode pintar a cor, a aspereza e a metalidade do objeto enquanto a iluminação é tratada de forma independente.
Assim, você pode pintar o objeto e ajustar a iluminação depois, sem estragar a aparência geral do modelo.

As luzes, o ambiente e a névoa só estão disponíveis no [modo PBR](#pbr).
Por questões de desempenho, o limite é de 4 luzes no celular e no tablet, e de 6 no computador.

::: tip
Você pode abrir um arquivo glTF com mais luzes, e o Nomad mantém todas elas.
Mas o desempenho não vai necessariamente ser bom.
:::

::: tip
Você pode simular muitas luzes deixando objetos sem iluminação/emissivos e ativando a iluminação global no menu [Pós-processamento](postprocess).
:::

### Visão geral dos tipos de luz {#light-types-overview}

Estes são os tipos de luz disponíveis no momento:

| Modo                        | Descrição                                               | Projeta sombras |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Direcional](#directional)  | Luz do sol, infinitamente distante                      | Sim              |
| [Ambiente](#env-light)      | Uma luz distante alinhada ao HDR do ambiente            | Sim              |
| [Spot](#spot)               | Luzes em forma de cone                                  | Sim              |
| [Ponto](#point)             | Ponto de luz que ilumina em todas as direções           | Sim              |

#### ![](/icons/sun.webp) Direcional {#directional}
Emite luz de uma distância infinita, com intensidade uniforme.
A posição 3d dela na cena não importa, só a orientação.

Você pode conectar esta luz à câmera, para ter uma iluminação sempre igual.
Por exemplo, dá para usá-la como luz de recorte (uma luz forte que vem de trás do modelo, apontada para a câmera) que sempre ilumina a parte de trás do modelo.

#### ![](/icons/panorama.webp) Luz de ambiente {#env-light}
Um [HDR de ambiente](#environment) funciona bem para uma iluminação geral suave, mas, se houver uma luz forte e nítida visível no HDR, a sombra que ela cria fica muito suave, muitas vezes nem aparece. Usar uma luz direcional junto com o HDR do ambiente ajuda, mas pode ser difícil deixar as duas alinhadas.

Esta luz faz esse trabalho por você. Ela gira automaticamente para se alinhar com a parte mais clara do HDR, e você controla separadamente a intensidade e o ângulo (a suavidade da sombra).

#### ![](/icons/spotlight.webp) Spot {#spot}
A luz spot emite luz em uma única direção, limitada por um cone.

#### ![](/icons/light.webp) Ponto {#point}
A luz de ponto emite luz em todas as direções e também pode projetar sombras.

#### Sombras {#shadows}
Cada luz pode projetar sombras, e você escolhe como elas são calculadas nos [ajustes](#light-extra-controls) dela. Se aparecerem artefatos nas sombras, os controles de `Tolerância` de lá podem ajudar.

A qualidade das sombras depende do tamanho dos objetos em relação à cena inteira.
Se houver na cena um objeto grande que não precisa projetar sombras (um plano grande, por exemplo), desative a projeção de sombras nos [ajustes do material](material.md#casts-shadows) dele.

## ![](/icons/sun.webp) Luzes {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Caixa de seleção Luzes {#lights-checkbox}

Liga ou desliga todas as luzes diretas da cena.



### Adicionar luz {#add-light}

Adiciona uma luz à cena, até 4 luzes no celular e no tablet, e 6 no computador. Quando uma luz é adicionada, a lista de luzes aparece com botões, e uma barra de ferramentas de luz surge no alto da vista.

![](/images/shading_lights_icons.webp)

* O texto mostra o nome da luz e o brilho. Toque nele para selecionar a luz.
* O ícone de olho liga ou desliga a visibilidade.
* O ícone de lápis permite renomear a luz.
* O ícone de lixeira apaga a luz.
* O ícone de cópia duplica a luz.
* O ícone de 3 pontos abre o editor completo da luz. A maior parte dessas funções também está na barra de ferramentas que aparece na vista.

Você também pode arrastar uma luz na lista para mudar a ordem.

### ![](/icons/spotlight.webp)  Ícones {#icons}

Liga ou desliga a exibição dos ícones das luzes na vista.

### Barra de ferramentas da luz {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Esta barra aparece no alto da vista quando uma luz está selecionada.

* `Visível` liga ou desliga a visibilidade da luz.
* Direcional/Ambiente/Spot/Ponto muda o tipo da luz. Toque para alternar entre eles, ou mantenha pressionado para ver um menu.
* A intensidade controla a força da luz. O valor pode passar de 1,0 para luzes muito intensas, o que é útil com a Iluminação Global do Pós-processamento.
* Tocar na amostra de cor abre um seletor de cor. O Nomad oferece várias formas de escolher a cor. O controle em Kelvin é uma forma natural de escolher uma iluminação quente ou fria.
* Sombra liga ou desliga as sombras.
* Ângulo (_direcional e ambiente_) ou Tamanho (_spot e ponto_) define a largura da luz. Luzes mais largas projetam sombras suaves, iluminam de forma suave e criam brilhos mais suaves nos objetos.
* Conexão (_só direcional_), Ângulo do cone e Suavidade (_só spot_) estão descritos no [editor de luz](#light-extra-controls) abaixo.
* ... abre `Clonar`, `Recentralizar` e `Apagar`, junto com os ajustes de sombra.

### Controles extras da luz {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

O ícone de 3 pontos de uma luz na lista abre o editor completo dela. Note que algumas opções são específicas de certos tipos de luz.

* `Direcional/Ambiente/Spot/Ponto` permite mudar o tipo da luz.
* Tocar na `amostra de cor` abre um seletor de cor.
* `Intensidade` controla a força da luz.
* `Conexão` (_só direcional_) prende a luz ao mundo (`Fixa`) ou à câmera (`Câmera`). Por exemplo, se você usar uma luz direcional atrás do personagem como luz de recorte, com a conexão em câmera, girar a câmera sempre mantém a luz atrás do personagem.
* `Suavidade` (_só spot_) controla a nitidez da borda do cone da luz spot. 0 dá uma borda bem nítida. 1 dá uma borda bem suave, com um gradiente até o centro do cone de luz. Na vista, o pequeno ponto azul no cone da luz spot permite ajustar a suavidade de forma interativa.
* `Ângulo do cone` (_só spot_) controla a abertura da luz spot. Um ângulo pequeno dá um feixe de luz bem fino, 170 dá uma luz bem aberta. Na vista, o ponto laranja permite ajustar o ângulo do cone de forma interativa.
* `Ângulo` (_só direcional e ambiente_) é o tamanho aparente da luz: pense em como o sol parece grande no céu. Ângulos maiores projetam sombras mais suaves e brilhos mais largos.
* `Tamanho` (_só spot e ponto_) é a largura da luz. Luzes maiores projetam sombras mais suaves.
* `Sombra` liga ou desliga as sombras da luz atual.
* O tipo de sombra define como as sombras são calculadas. O `Mapeamento de sombra` renderiza a cena a partir da luz, então também projeta sombra da geometria que a câmera não vê. O `Espaço da tela` usa só o que já está visível na tela: é mais leve, mas experimental. Em geral, o mapeamento de sombra é mais confiável.
* `Tolerância` (_só espaço da tela_): se aparecerem artefatos nas sombras (as sombras parecem não tocar as superfícies, ou há ruído e padrões dentro delas), ajustar a tolerância pode resolver.
* `Contato` adiciona sombras mais precisas em distâncias curtas, onde os objetos se tocam. Em `Auto`, só a luz mais dominante da cena recebe sombras de contato; `Não` e `Sim` forçam a opção para esta luz. O controle de `Tolerância` dela funciona como o de cima.

O botão `...` da barra de ferramentas da vista tem os mesmos ajustes de sombra, e também:

* `Clonar` duplica a luz.
* `Recentralizar` move a luz para a frente da câmera, mantendo a orientação dela.
* `Apagar` apaga a luz.


## ![](/icons/panorama.webp) Ambiente {#environment}

![](/images/shading_environment.webp)

No mundo real, a luz vem de todas as direções: o azul do céu, o verde da grama, o vermelho de um prédio. Toda essa luz do "ambiente" pode ser simulada com um mapa de ambiente.

Use a caixa de seleção ao lado do título para ligar ou desligar a iluminação do ambiente.

O Nomad vem com vários mapas de ambiente de exemplo, de lugares internos e externos, com tons e níveis de brilho diferentes. Experimente mapas diferentes para ver qual realça melhor os detalhes das suas esculturas.

Toque na imagem para ver os mapas de ambiente disponíveis. Nessa janela, escolha `Importar...` para carregar os seus. O ideal é usar imagens de alto alcance dinâmico (HDR), no formato latlong ou equiretangular, em arquivos .hdr ou .exr. O navegador também pode baixar ambientes direto do [Poly Haven](https://polyhaven.com/hdris), que tem uma boa coleção de mapas de ambiente gratuitos.

### Exposição {#env-exposure}
Ajusta o brilho do mapa de ambiente. Muitas vezes os mapas ficam claros demais quando usados com luzes comuns, e baixar a exposição ajuda a equilibrar, principalmente com a Iluminação Global dos ajustes de [Pós-processamento](postprocess).

### Rotação {#env-rotation}

Como os mapas de ambiente capturam a luz de todas as direções, você pode girá-los para que os reflexos e a iluminação geral combinem bem com a sua escultura. Também dá para girar o ambiente arrastando 3 dedos na horizontal pela vista.

### Conectado à câmera {#env-attached}
Prende o ambiente à câmera.

Isso força uma iluminação sempre igual, o que pode ser útil enquanto você esculpe.

### Desfoque (fundo) {#env-background-blur}
Este controle só aparece quando o [fundo](background.md) está definido como o ambiente. Ele desfoca a imagem do ambiente atrás do modelo, sem mudar a iluminação.


## ![](/icons/fog.webp) Névoa {#fog}

A névoa dá profundidade atmosférica à cena e torna os feixes de luz visíveis. Ative-a pela caixa de seleção ao lado do título. Assim como as luzes e o ambiente, ela só está disponível no modo [Iluminado (PBR)](#pbr).

::: tip Feixes de luz mais fortes
Diminua o `Ambiente` da névoa e use uma luz spot ou de ponto bem forte. Aumente a `Densidade` até a névoa ficar bem visível. Para ter feixes visíveis em uma névoa mais leve, coloque a `Direção da dispersão` em um valor positivo alto e aponte a câmera para a luz.
:::

### Cor {#fog-color}
A cor da névoa e da luz que ela dispersa.

### Densidade {#fog-density}
A rapidez com que a névoa fica mais espessa com a distância.

### Opacidade máxima {#fog-opacity}
Limita o quanto a névoa pode cobrir a cena, mesmo com densidade alta.

### Direção da dispersão {#fog-scattering}
A direção em que a névoa dispersa a luz (também chamada de anisotropia). Valores positivos clareiam a névoa quando você olha na direção de uma luz, valores negativos quando você olha para o lado oposto, e zero dispersa a luz por igual em todas as direções.

### ![](/icons/panorama.webp) Ambiente {#fog-environment}
O quanto o [ambiente](#environment) ilumina a névoa. Fica acinzentado quando o ambiente está desligado.

### Ruído {#fog-noise}
Mistura ruído à névoa para dividi-la em manchas, sem mudar a densidade geral. Quando o ruído está acima de 0, um controle de `Tamanho` define o tamanho do padrão.

### Forma {#fog-shape}
Onde a névoa preenche a cena:

* `Uniforme` - preenche a cena inteira.
* `Vertical` - mantém a névoa dentro de uma faixa vertical com bordas suaves. Os controles `Base` e `Topo` definem a altura das bordas inferior e superior, e o botão de olho deles mostra a faixa na vista enquanto você os ajusta.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Como o nome sugere (MATerial CAPture, captura de material), um matcap cuida ao mesmo tempo da iluminação e do material em uma única imagem.
Como o material já está no próprio matcap, os canais de pintura de aspereza e metalidade são ignorados.
A cor da pintura é multiplicada pelo matcap, ou seja, se você tiver um matcap preto ou cinza, pintar de branco não vai deixá-lo mais claro.

Os artistas costumam preferir este modo para esculpir, porque ele permite se concentrar na forma e na própria geometria.

Tocar na esfera abre um navegador de imagens. Você também pode adicionar o seu próprio matcap: em geral, qualquer foto, renderização ou até pintura de uma esfera, recortada bem justa em um quadrado, serve. Há muitas bibliotecas de matcaps na internet, e um bom recurso é a [biblioteca de matcaps nidorx](https://github.com/nidorx/matcaps).

### Usar MatCap global {#matcap-global}

Normalmente, os artistas usam um único matcap para a escultura inteira, mas, se esta opção estiver desativada, o objeto selecionado pode ter o seu próprio matcap. Isso pode ser usado de forma artística para conseguir resultados marcantes.

::: tip
Desative esta opção e use a imagem de um globo ocular para os olhos dos seus personagens!
:::

### Rotação {#matcap-rotation}
Um matcap é uma forma especial de mapa de ambiente, então, assim como um mapa de ambiente, ele pode ser girado. Você também pode fazer isso a qualquer momento na vista, arrastando 3 dedos para a esquerda e para a direita.

O botão de cadeado ao lado do controle trava a rotação, para que um arrasto com 3 dedos não gire o matcap sem querer.



## ![](/icons/circle_fill.webp) Sem iluminação {#unlit}

Este modo mostra só a cor da superfície. É útil para conferir se a cor da superfície dos objetos está como você espera, sem se distrair com luzes, sombras, reflexos ou transparência.

Este modo também serve para renderizações não fotorrealistas, com uma aparência chapada, de desenho animado.

## ![](/icons/cube.webp) ID do objeto {#object-id}

Todas as informações de iluminação e de superfície são ignoradas, e cada objeto recebe uma cor chapada única. Se você renderizar isso junto com uma renderização PBR, pode usar essa imagem em um programa de pintura para selecionar por cor e, assim, fazer correções de cor em objetos específicos.

Note que essas cores também aparecem na [árvore do menu Cena](scene#tree-view).

### Aleatorizar id {#object-random}

Gera um novo conjunto de cores aleatórias.

## ![](/icons/link.webp) ID da instância {#instance-id}

Igual ao ID do objeto, mas as instâncias têm a mesma cor.

### Aleatorizar id {#instance-random}

Gera um novo conjunto de cores aleatórias.

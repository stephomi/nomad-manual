# ![](/icons/sun.webp) Sombras {#shading}

Este menu controla os modos de sombreamento usados pelo Nomad, as propriedades de iluminação e as propriedades de luz de ambiente/matcap.

![](/images/shading_overview.webp)



Você pode escolher entre vários modos de renderização:

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | Pintura com metalness/roughness                                |
| [Matcap](#matcap)           | Material Capture           | Usado durante a escultura com menor uso de GPU/CPU que PBR     |
| [Unlit](#unlit)             | Surface Color              | Apenas cor da superfície, sem sombreamento ou iluminação       |
| [Object Id](#object-id)      | Object ID                  | Uma cor aleatória por objeto, útil para aplicações de pintura. |
| [Instance Id](#instance-id)  | Instance ID                | Uma cor aleatória por instância, útil para identificar malhas compartilhadas |

Se quiser saber mais sobre metalness e roughness, veja a seção [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Grupo de faces {#face-group}
Sobrepõe as cores dos facegroups. Facegroups são seleções coloridas de polígonos que podem ser criadas com a ferramenta [Face group](tools#facegroup) e são criadas automaticamente com a maioria dos primitivos.

Algumas ferramentas irão automaticamente filtrar por facegroups quando os facegroups estiverem visíveis.

### Mostrar pintura {#show-paint}
O Nomad pode armazenar cor, roughness e metalness nos vértices da sua escultura. Você pode alternar a exibição dessas propriedades globalmente com esta caixa de seleção.

Note que, se você tiver tanto propriedades de vértice quanto texturas, e ambas estiverem ativadas, os valores serão multiplicados entre si.

### Mostrar máscara {#show-mask}
Alterna a sobreposição em tons de cinza da máscara das [ferramentas de máscara](tools#mask). Quando isto está desativado, a máscara também é desativada, o que é útil para fazer alterações rápidas sem a máscara; depois você pode ativá-la novamente sem perder a máscara.

### Usar ocultar {#use-hide}

Alterna faces ocultas. Note que isto só funciona se você NÃO estiver na ferramenta de esconder (hide)!

### Usar texturas {#use-textures}

O Nomad permite que texturas sejam atribuídas a objetos a partir do menu [material](material). Se texturas forem atribuídas, elas podem ser alternadas globalmente com esta caixa de seleção.







### Visão geral de PBR e luzes {#pbr}
Este manual não entrará em detalhes sobre Physically Based Rendering.

Uma coisa importante a ter em mente é que iluminação e material são totalmente separados.
Isso significa que você pode pintar a cor, roughness e metalness do seu objeto enquanto a iluminação é tratada de forma independente.
Isso permite que você pinte seu objeto e depois ajuste a iluminação mais tarde, sem quebrar o visual geral do seu modelo.

Luzes só estão disponíveis com o [modo PBR](#pbr).
Por motivos de desempenho, você está limitado a apenas 4 luzes.

::: tip
Você pode carregar um arquivo glTF com mais de 4 luzes e o Nomad manterá todas elas.
No entanto, isso não terá necessariamente um bom desempenho.
:::

::: tip
Você pode simular muitas luzes tornando objetos unlit/emissive e então ativando a iluminação global no menu de [pós-processo](postprocess).
:::

### Visão geral dos tipos de luz {#light-types-overview}

Aqui estão os tipos de luz atualmente suportados:

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Luz solar infinitamente distante                       | yes                                                    |
| [Environment](#environment) | Uma luz distante que corresponde ao HDR do ambiente    | yes                                                    |
| [Spot](#spot)               | Luzes em forma de cone				                    | Yes                                                    |
| [Point](#point)             | Ponto de luz omnidirecional                            | Yes, but only through less robust screen-space shadows |

#### Direcional {#directional}
Emite luz de uma distância infinitamente grande, com intensidade uniforme.
Sua posição 3D na cena não importa, apenas sua orientação.

Você pode anexar esta luz à câmera, assim ela terá iluminação consistente.  
Por exemplo, você pode usá-la para fazer uma rim light (uma luz forte que emite por trás do seu modelo, apontando em direção à câmera) que sempre ilumina a parte de trás do seu modelo.

#### Luz de ambiente {#env-light}
Usar um [environment hdr](#environment) funciona bem para iluminação geral suave, mas se houver uma luz forte e nítida visível no HDR, a sombra criada por ela será muito suave, muitas vezes nem visível. Usar uma luz direcional em combinação com o HDR de ambiente pode ajudar, mas pode ser difícil alinhá-las.

Esta luz faz o trabalho por você. A luz será automaticamente rotacionada para se alinhar com a parte mais brilhante do HDR; então você pode controlar sua intensidade e ângulo (maciez da sombra) separadamente. 

#### Spot {#spot}
A luz spot emite luz em uma única direção, restrita por uma forma de cone.

#### Ponto {#point}
A luz point emite luz em todas as direções.  
No momento, a luz point não oferece suporte a sombras.

#### Sombras {#shadows}
A opção `normal bias` pode ser usada para reduzir artefatos comuns de sombra (acne/peter-panning).

A qualidade das sombras depende do tamanho dos objetos em relação à cena inteira.  
Se você tiver um objeto grande na sua cena que não precisa projetar sombras (por exemplo, um grande plano), certifique-se de desativar o lançamento de sombras nas [configurações de material](material.md#cast-shadows) dele.

## Luzes {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Caixa de seleção Luzes {#lights-checkbox}

Alterna todas as luzes diretas na cena.



### Adicionar luz {#add-light}

Adiciona uma luz à cena, até um máximo de 4. Quando uma luz é adicionada, a lista de luzes é exibida com botões, e uma barra de ferramentas de luz é adicionada ao topo da viewport.

![](/images/shading_lights_icons.webp)

* O texto mostra o nome da luz e o brilho.
* O ícone de olho alterna a visibilidade.
* O ícone de lápis permite renomear a luz.
* O ícone de lixeira apaga uma luz.
* O ícone de cópia duplica uma luz. 
* O ícone de 3 pontos abre um editor completo de luz. A maior parte dessa funcionalidade também está disponível na barra de ferramentas que aparece na viewport. 

### ![](/icons/spotlight.webp) Ícones {#icons}

Alterna a exibição dos ícones de luz na viewport.

### Barra de ferramentas de luz {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Esta barra de ferramentas aparecerá no topo da viewport quando uma luz estiver selecionada.

* Show alterna a visibilidade da luz.
* Directional/Environment/Spot/Point altera o tipo de luz. Toque para alternar ou pressione e segure para ver um menu.
* Intensity controla a força da luz; o valor pode ir acima de 1.0 para luzes muito intensas, útil quando usado com Global Illumination em Post Process.
* O seletor de cor, quando clicado, abrirá um seletor de cores. O Nomad oferece várias maneiras de escolher cor. O controle Kelvin oferece uma forma natural de selecionar iluminação quente/fria.
* Shadow alterna sombras.
* Size define a largura de uma luz. Luzes mais largas projetam sombras suaves, iluminação suave e um highlight mais suave nos objetos.
* ... abre controles extras.

### Controles extras de luz {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Note que algumas opções são específicas de certos tipos de luz.

* `Clone` duplica a luz.
* `Recenter` move a luz de volta para a origem.
* `Delete` apaga a luz.
* `Directional/Environment/Spot/Point` permitem alterar o tipo de luz.
* O `colour swatch`, quando clicado, abrirá um seletor de cores. 
* `Intensity` controla a força da luz.
* `Attachment` (_apenas directional_) define se a luz será filha do mundo ou da câmera. Ex.: se você usar uma luz direcional atrás do seu personagem como rim light, quando Attachment como camera estiver selecionado, girar a câmera fará com que a luz esteja sempre atrás do personagem.
* `Angle` (_apenas directional e environment_) é o tamanho aparente da luz; pense em quão grande o sol parece no céu. Ângulos maiores projetam sombras mais suaves e highlights mais largos.
* `Softness` (_apenas spotlight_) controla a nitidez da borda do cone da luz spot. 0 é uma borda muito nítida. 1 é muito suave, com um gradiente até o centro do cone de luz. Na viewport, o pequeno ponto azul no cone da luz spot pode ser usado para definir a suavidade de forma interativa.
* `Cone angle` (_apenas spotlight_) controla o ângulo de abertura da luz spot. Um ângulo pequeno é um feixe de luz muito fino; 170 é uma abertura muito ampla. Na viewport, o ponto laranja pode ser usado para definir o cone angle de forma interativa.
* `Shadow` alterna sombras para a luz atual.
* `Shadow map` e `screenspace` são maneiras diferentes de calcular sombras; em geral, shadow map é mais confiável.
* `Contact` ajusta como as sombras são calculadas. Sombras são um problema difícil em computação gráfica e podem causar artefatos na renderização. Sombras mais precisas podem ser selecionadas para a luz mais importante de uma cena; este controle determina se a luz mais importante é selecionada automaticamente pelo Nomad ou pelo usuário.
* `Tolerance` se artefatos de sombra forem visíveis (ou as sombras não parecem tocar as superfícies, ou há ruído e padrões dentro das sombras), ajustar tolerance pode ajudar a corrigir esses problemas.


## Ambiente {#environment}

![](/images/shading_environment.webp)

A luz no mundo real vem de todas as direções; o azul do céu, o verde da grama, o vermelho de um prédio — toda essa luz do “ambiente” pode ser simulada com um mapa de ambiente. 

O Nomad vem com vários mapas de ambiente de exemplo para áreas internas e externas, com diferentes tonalidades e níveis de brilho. Experimente mapas diferentes para ver qual traz mais detalhes às suas esculturas.

Toque na imagem para ver os mapas de ambiente disponíveis. Nesse diálogo, escolha “Import...” para carregar o seu próprio. É melhor usar imagens High Dynamic Range (HDR), no formato latlong ou equiretangular, como arquivos .hdr ou .exr. O site [www.polyhaven.com](https://polyhaven.com/hdris) tem uma boa coleção de mapas de ambiente gratuitos; em geral, os mapas HDR 1k têm bom tamanho e boa qualidade.

### Exposição {#env-exposure}
Ajusta o brilho do mapa de ambiente. Muitas vezes os mapas podem ser brilhantes demais quando usados com luzes regulares; reduzir a exposição pode ajudar a equilibrar, especialmente quando usado com Global Illumination nas configurações de [Post Process](postprocess).

### Rotação {#env-rotation}

Como os mapas de ambiente capturam luz de todas as direções, você pode rotacioná-los para fazer com que os reflexos e a iluminação geral combinem bem com a sua escultura.

### Anexado à câmera {#env-attached}
Anexa o ambiente à câmera.

Isso forçará a iluminação a ser consistente, o que pode ser útil durante a escultura.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Como o nome sugere (MATerial CAPture), um matcap cuida tanto da iluminação quanto da informação de material em uma única imagem.
Como o material em si já está presente no matcap, os canais de pintura de roughness e metalness serão ignorados.
A cor de pintura será multiplicada pelo matcap, o que significa que, se você tiver um matcap preto/cinza, usar tinta branca não o deixará mais brilhante.

Artistas tendem a preferir este modo para fins de escultura, pois ele permite focar na forma e na geometria em si.

Tocar na esfera abrirá um navegador de imagens. Você também pode adicionar seu próprio matcap; em geral, qualquer foto, render ou até uma pintura de uma esfera recortada de forma justa em um quadrado pode ser usada. Muitas bibliotecas de matcap estão disponíveis online; um recurso útil é a [biblioteca de matcaps do nidorx](https://github.com/nidorx/matcaps).

### Usar Matcap global {#matcap-global}

Normalmente artistas usam um único matcap para toda a escultura, mas se este alternador estiver desativado, cada objeto pode ter seu próprio matcap. Isso pode ser usado artisticamente para obter resultados marcantes.

::: tip
Desative esta opção e use uma imagem de um globo ocular para os olhos dos seus personagens!
:::

### Rotação {#matcap-rotation}
Um matcap é uma forma especializada de mapa de ambiente, então, como um mapa de ambiente, ele pode ser rotacionado. Você também pode fazer isso a qualquer momento na viewport arrastando com 3 dedos para a esquerda e para a direita.



## ![](/icons/circle_fill.webp) Sem iluminação {#unlit}

Este modo mostrará apenas a cor da superfície. Pode ser útil para verificar se a cor da superfície dos seus objetos é a que você espera, sem distração de luzes, sombras, reflexão ou transparência. 

Este modo também pode ser usado para renders não fotorrealistas, obtendo um visual plano e cartunesco.

## ![](/icons/cube.webp) ID do objeto {#object-id}

Todas as informações de iluminação e superfície são ignoradas, e cada objeto é sombreado com uma cor chapada única. Se isto for renderizado junto com um render PBR, pode ser usado em um programa de pintura para selecionar por cor e, assim, poder fazer correções de cor em objetos específicos.

Note que essas cores também aparecerão na [visualização em árvore do menu Scene](scene#tree-view).

### Aleatorizar id {#object-random}

Gera um novo conjunto de cores aleatórias. 

## ![](/icons/link.webp) ID de instância {#instance-id}

Igual ao Object ID, mas instâncias terão a mesma cor. 

### Aleatorizar id {#instance-random}

Gera um novo conjunto de cores aleatórias.
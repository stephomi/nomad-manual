# ![](/icons/material.webp) Material {#material}

Este menu permite alterar o material do objeto atual, as propriedades de renderização do objeto/material e atribuir texturas ao material.

![](/images/material_overview.webp)

Os materiais definem como um objeto aparenta, controlando como ele reage à luz e a outros objetos. A aparência de um objeto é controlada por estas propriedades:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Combinações dessas propriedades podem alcançar uma grande variedade de resultados, de fotorrealistas a cartunescos ou experimentais.

Cor, roughness, metalness e opacity podem ser pintadas, veja [Vertex Paint options](painting.md) para mais informações.

Material type, reflectance, emssive/unlit são propriedades de material explicadas abaixo.

Os botões de copiar/colar no topo deste menu permitem copiar materiais de um objeto para outro.

Note que o renderizador do Nomad é em tempo real; embora poderoso, ele favorece velocidade em detrimento de precisão para certos efeitos. 

## Tipos de material {#material-types}

![](/images/material_types.webp)

Os tipos de material do Nomad são Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaco {#opaque}
O modo padrão que trata superfícies como um material simples que suporta cor, roughness, metalness e opacity pintadas.

### ![](/icons/material_subsurface.webp) Subsuperfície {#subsurface}
Este modo pode simular material que permite que a luz se difunda e se espalhe internamente, como pele, cera, jade.

Para obter o melhor resultado, mude para o modo de sombreamento PBR e use pelo menos uma luz direcional ou spot, idealmente com um ambiente escuro.

`Depth` controla quão longe a luz se espalha da frente para sob a superfície e então sai novamente pela frente. Isso tem o efeito de suavizar sombras duras e desfocar detalhes de superfície.

`Translucency` controla como a luz se espalha da frente para a parte de trás de uma forma, como a luz atravessando a parte inferior de uma folha ou quando orelhas são fortemente iluminadas por trás. 

### ![](/icons/material_blending.webp) Mesclagem {#blending}

Similar a Opaque, mas suporta o controle deslizante de opacity para permitir que o material varie entre sólido e transparente. Este é um controle simples de opacidade único, em contraste com a opacity pintável suportada pelo material Opaque. 

::: warning
O modo Blending pode causar cintilação e estalos em formas complexas ou que se intersectam.
:::

### ![](/icons/material_additive.webp) Aditivo {#additive}
Você pode deixar sua malha semitransparente com este material. É similar ao material Blending, mas enquanto Blending se mistura com o entorno, Additive será sempre mais brilhante do que os objetos atrás dele, bom para efeitos intensos como raios de luz, fogo, explosões.

Você pode definir um valor de opacity maior que 1, o que significa que o objeto ficará mais brilhante.  
Isso pode ser útil se você quiser usar o [bloom](postprocess.md#bloom) e o `threshold parameter` para fazer apenas este objeto brilhar como um objeto emissivo.

Este modo tende a ter menos artefatos do que o [Blending](#blending) (transparência independente de ordem).

### ![](/icons/material_refraction.webp) Refração {#refraction}
Este modo pode ser usado para simular material de vidro. Devido a limitações de tempo real, autorrefração e refração em múltiplas camadas são um tanto limitadas.

A pintura de roughness do modelo afeta o quão borrada é a refração.
Por padrão, todo objeto criado no Nomad tem uma roughness em torno de 25%, portanto a refração não será perfeita, mas um pouco borrada.
Você pode usar o botão `paint glossy` para repintar seu modelo com roughness e metalness em 0 (as cores não serão afetadas).

Há 2 roughness diferentes em jogo: uma controla o quão borrada é a reflexão na superfície, e a outra controla o interior (refração).  
No entanto, como há apenas um canal de roughness de pintura no Nomad, tanto a roughness interna quanto a externa compartilharão o mesmo valor.  
Para ter valores diferentes (por exemplo um pirulito com superfície nítida, mas interior borrado) use os controles deslizantes `Surface glossiness` e `Interior roughness` para substituir a roughness pintada.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Deixa o objeto semitransparente descartando alguns pixels de forma aleatória.

### ![](/icons/material_shadow_catcher.webp) Captura de sombra {#shadow-catcher}

Deixa o objeto invisível e apenas recebe sombras. Útil para combinar renders do Nomad com outras imagens. 

::: tip

Mais informações sobre transparência e modos de blending podem ser encontradas em https://support.fab.com/s/article/Transparency-Opacity

:::

## Controles {#controls}

![](/images/material_controls.webp)

### Sempre sem luz {#always-unlit}
Se ativado, o objeto ignorará PBR e Matcap e simplesmente exibirá sua cor pintada sem sombreamento.
Note que se você usar [Additive](#additive), pode pintar transparência diretamente usando a cor preta.

### Opacidade {#opacity}
Quão sólido ou opaco um objeto irá parecer; 100% é sólido, 0% é transparente. Você também pode pintar opacity para controle mais fino.

### Reflectância {#reflectance}
Controla a quantidade de reflexão que o material receberá para materiais não metálicos. Na maioria das vezes o valor padrão deve ser usado (que corresponde aos 4% padrão de luz refletida em ângulo normal), mas pode ser aumentado para reforçar reflexos e brilhos nos olhos de um personagem, por exemplo.

### Inversão de face (culling) {#inverse-culling}
Inverte as normais de uma superfície. Normalmente não é necessário, mas pode ser usado se um modelo parecer invertido ou, em combinação com `Two sided` desativado, pode ser usado para fazer interiores onde a parede mais próxima da câmera fica sempre oculta.

### Sombreamento suave {#smooth-shading}
Veja a [opção global](settings.md#smooth-shading).  
O valor `Auto` usará a opção global.

### Duas faces {#two-sided}
Veja a [opção global](settings.md#two-sided).  
O valor `Auto` usará a opção global.

### Face posterior colorida {#coloured-backface}
Veja a [opção global](settings#two-sided).
O valor `Auto` usará a opção global.

### Lança sombras {#casts-shadows}
Por enquanto `Auto` é o mesmo que `On`.
Objetos transparentes também projetam sombras (em um padrão de dithering para emular sombras blendadas).  
Certifique-se de desativar a projeção de sombras se você tiver um objeto grande na cena que não precisa projetar sombras (por exemplo um grande piso).

### Recebe sombras {#recieve-shadows}
Por enquanto `Auto` é o mesmo que `On`.

### Wireframe {#wireframe}
Veja a [opção global](settings.md#wireframe).  
O valor `Auto` usará a opção global.


## Texturas {#textures}

![](/images/material_textures.webp)

Se um objeto tiver UVs, então texturas podem ser aplicadas ao material além da cor/roughness/metalness/opacity de vértice. Normalmente estas são o resultado de um bake de textura, mas imagens criadas fora do Nomad também podem ser usadas.

Texturas podem ser aplicadas a

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Clicar em um slot de textura abrirá um seletor. Depois que uma textura tiver sido atribuída a um slot de material, clicar novamente abrirá um painel de textura:

### Opções do painel de textura {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Abrir {#open}
Selecionar outra textura

### Nenhum {#none}
Remover a textura

### Opacidade {#texture-opacity}

Se a imagem tiver um canal alfa, isso permitirá usá-lo para Opacity ou ignorá-lo.

### ![](/icons/link.webp) Ícone de corrente/ligação {#chainlink-icon}

O ícone de link nas seções a seguir, quando ativado, fará com que quaisquer opções usadas sejam compartilhadas com as outras texturas (color, normal, roughness, metalness, opacity, emissive) que também tiverem seu ícone de link ativado. 

Isso permite garantir que, se você tiver texturas alinhadas, elas permaneçam alinhadas mesmo quando alterar parâmetros ou tipos de projeção.


### Projeção {#projection}
![](/images/material_projection.webp)

Define como a textura deve ser aplicada ao objeto.

* `Auto` - Se o objeto tiver UVs, UV, caso contrário Triplanar
* `UV` - Usa as coordenadas UV da malha para aplicar a textura. Se a malha e a textura vierem de fora do Nomad, ou forem exportadas do Nomad para uso em outro lugar, UV é a opção correta.
* `Triplanar` - Projeta a textura ao longo dos eixos X, Y, Z e mistura as emendas. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Projeções triplanares são uma forma poderosa e simples de aplicar texturas a objetos.

Triplanar é como ter 6 projetores de vídeo, todos com a mesma imagem, iluminando a frente, trás, esquerda, direita, topo e base do seu objeto.

Isso pode então ser assado em UVs ou cores de vértice, se necessário.


![](/images/material_triplanar_example.webp)

#### Método {#method}

* `Local` - A projeção se moverá com a transformação do objeto
* `World` - A projeção permanece fixa; mover o objeto irá deslizá-lo através da projeção.

#### Dureza {#hardness}

Como as projeções se misturam. 100% não fará mistura alguma, e as bordas das projeções serão nítidas. 0% irá misturar as bordas em um ângulo amplo. O padrão é 90%, mistura suficiente para esconder as bordas e deixar o restante das projeções nítido.

### Uniforme {#uniform}

Quando marcado, a mesma hardness é usada para todas as projeções. Quando desmarcado, controles extras de hardness são exibidos para as projeções X, Y, Z.


### Parâmetro {#parameter}
![](/images/material_parameter.webp)

#### Filtragem {#filtering}
O método de filtragem de textura a ser usado, `Auto` é o padrão; os métodos são `Nearest`, `Linear`, `Mipmap`. Nearest não faz filtragem, então texturas podem apresentar artefatos serrilhados quando vistas de perto. Linear e Mipmap fazem uma filtragem melhor, então as texturas parecem borradas em vez de serrilhadas de perto.

#### Repetição-X {#tiling-x}
Se o parâmetro Scale for maior que 1, tornando a textura menor que os UVs do objeto, como a textura será repetida ao longo do eixo X. `None` significa sem repetições. `Repeat` fará cópias da textura. `Mirror` fará cópias da textura, com cada segunda cópia invertida, o que pode ajudar a esconder artefatos de repetição.

#### Repetição-Y {#tiling-y}
O mesmo que Tiling-X, mas para o eixo Y.

### Transformar {#transform}
![](/images/material_transform.webp)

Transformações 2D extras aplicadas à textura no espaço UV. O botão de reset restaura os padrões; o ícone de corrente (quando texturas diferentes de color estão selecionadas) vincula ou desvincula a transformação para ser a mesma da textura de color.

#### Translação {#translation}
O deslocamento X e Y da textura

#### Rotação {#rotation}
A rotação da textura

#### Escala {#scale}
A escala da textura; números maiores deixarão a textura menor no objeto, use os controles deslizantes Tiling-X e Tiling-Y para controlar o que acontece.

### Escala uniforme {#uniform-scale}
Quando desativado, o Nomad mostrará controles separados para Scale-X e Scale-Y.
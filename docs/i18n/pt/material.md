# ![](/icons/material.webp) Material {#material}

Este menu permite mudar o material do objeto atual, as propriedades de renderização do objeto/material e atribuir texturas ao material.

![](/images/material_overview.webp)

Os materiais definem a aparência de um objeto, controlando como ele reage à luz e aos outros objetos. A aparência de um objeto é controlada por estas propriedades:

* `Tipo de material`
* `Cor`
* `Aspereza`
* `Metalidade`
* `Opacidade`
* `Reflexividade`
* `Emissiva/sem iluminação`

Combinando essas propriedades, você consegue uma grande variedade de resultados, do fotorrealista ao cartunesco e ao experimental.

A cor, a aspereza, a metalidade e a opacidade podem ser pintadas, veja as [opções de pintura de vértices](painting.md) para mais informações.

O tipo de material, a reflexividade e a emissão/sem iluminação são propriedades do material explicadas abaixo.

Os botões `Copiar` e `Colar` no topo deste menu permitem copiar materiais de um objeto para outro.

O renderizador do Nomad é um renderizador em tempo real: embora poderoso, ele prioriza a velocidade em vez da precisão em certos efeitos.

## Tipos de material {#material-types}

![](/images/material_types.webp)

Os tipos de material do Nomad são Opaco, Subsuperfície, Mistura, Aditiva, Refração, Pontilhamento e Capturador de sombras.

### ![](/icons/material_opaque.webp) Opaco {#opaque}
O modo padrão, que trata a superfície como um material simples com suporte a cor, aspereza, metalidade e opacidade pintadas. A opacidade pintada, uma textura de opacidade ou o canal alfa da textura de cor ainda deixam o objeto transparente, usando pontilhamento. Só o controle principal de opacidade é ignorado.

### ![](/icons/material_subsurface.webp) Subsuperfície {#subsurface}
Este modo simula materiais em que a luz se espalha e se difunde por dentro, como pele, cera ou jade.

Ele exige o modo de sombreamento PBR. Para obter o melhor resultado, use pelo menos uma luz direcional ou spot, de preferência com um ambiente pouco iluminado.

A amostra de cor define a cor da luz espalhada.

`Profundidade` controla o quanto a luz se espalha a partir da frente, por baixo da superfície, saindo de novo pela superfície frontal. Isso suaviza as sombras duras e desfoca os detalhes da superfície.

`Translucidez` controla como a luz atravessa a forma da frente para trás, como a luz passando pelo verso de uma folha, ou orelhas com uma forte luz de fundo. Você precisa de uma luz que projete sombras para ver o efeito.

### ![](/icons/material_blending.webp) Mistura {#blending}

Parecido com Opaco, mas aceita o controle de opacidade para misturar o material entre sólido e transparente. É um controle único e simples de opacidade, diferente da opacidade pintável do material opaco.

::: warning
O modo de mistura pode causar cintilação e falhas em formas complexas ou que se cruzam.
:::

### ![](/icons/material_additive.webp) Aditiva {#additive}
Com este material, sua malha fica semitransparente. É parecido com o material de mistura, mas enquanto a mistura se combina com o entorno, o aditivo sempre fica mais claro que os objetos atrás dele: bom para efeitos luminosos como raios de luz, fogo ou explosões.

Você pode definir uma opacidade maior que 1, o que deixa o objeto mais claro.  
Isso é útil se você quiser usar a [incandescência](postprocess.md#bloom) e o `parâmetro de limite` para fazer só este objeto brilhar, como um objeto emissivo.

Este modo costuma ter menos artefatos que a [Mistura](#blending) (transparência independente da ordem).

### ![](/icons/material_refraction.webp) Refração {#refraction}
Este modo serve para simular vidro. Ele exige o modo de sombreamento PBR. Por causa das limitações do tempo real, a autorrefração e a refração em várias camadas são um tanto limitadas.

A pintura de aspereza do modelo influencia o quanto a refração fica desfocada.
Por padrão, todo objeto criado no Nomad tem uma aspereza de cerca de 25%, então a refração não fica perfeita, e sim um pouco desfocada.
Você pode usar o botão `Pintar brilho` para repintar o modelo com aspereza e metalidade 0 (as cores não são afetadas).

Há 2 asperezas diferentes em jogo: uma controla o quanto o reflexo na superfície fica desfocado, e a outra controla o interior (a refração).  
Mas como o Nomad tem um único canal de pintura de aspereza, o interior e o exterior compartilham o mesmo valor.  
Para ter valores diferentes (por exemplo um pirulito com superfície nítida mas interior desfocado), use os controles `Superfície` e `Interior` em `Substituir aspereza` para substituir a aspereza pintada.

![](/videos/refraction.mp4)

#### Índice de Refração {#index-of-refraction}
O quanto a luz se curva ao entrar no objeto. Valores mais altos curvam mais a luz, como uma lente grossa.

#### Absorção {#absorption}
Simula a luz sendo absorvida enquanto atravessa o volume, tingida pela amostra de cor, com `Fator` definindo a intensidade. As partes finas ficam mais claras porque deixam passar mais luz, enquanto as áreas grossas ficam mais escuras. Só uma aproximação da espessura do objeto é usada, então o efeito depende muito da forma.


### ![](/icons/material_dithering.webp) Pontilhamento {#dithering}
Deixa o objeto semitransparente descartando alguns pixels de forma aleatória.

### ![](/icons/material_shadow_catcher.webp) Capturador de sombras {#shadow-catcher}

Deixa o objeto invisível, recebendo apenas as sombras das luzes. Útil para combinar renderizações do Nomad com outras imagens, normalmente em um plano. A amostra de cor define a cor da sombra.

É preciso haver uma luz que projete sombras na cena, senão o capturador de sombras não faz nada. Os botões `Metalidade → 0%` e `Metalidade → 100%` repintam o objeto: totalmente metálico, o capturador de sombras também pode refletir a cena quando o pós-processamento [Reflexão (SSR)](postprocess.md#reflection-ssr) está ativado.

::: tip

Mais informações sobre transparência e modos de mistura em https://support.fab.com/s/article/Transparency-Opacity

:::

## Controles {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Sempre não iluminado {#always-unlit}
Se ativado, o objeto ignora o PBR e o MatCap e mostra apenas a cor pintada, sem sombreamento.
Se você usar [Aditiva](#additive), pode pintar a transparência diretamente usando a cor preta.

### Opacidade {#opacity}
O quanto um objeto parece sólido ou opaco: 100% é sólido, 0% é transparente. O controle aparece nos tipos Mistura, Aditiva, Pontilhamento e Capturador de sombras. Você também pode pintar a opacidade para um controle mais fino.

### Pré-passe de refração {#pre-refract-pass}
Só para Mistura e Aditiva. Desenha este objeto transparente antes da passagem de refração. Útil quando um objeto com refração está na frente de outras superfícies transparentes.

### Reflexividade {#reflectance}
Controla a quantidade de reflexo que o material recebe, nos materiais não metálicos. Na maioria das vezes, o valor padrão deve ser usado (que corresponde aos 4% padrão de luz refletida em ângulo normal), mas ele pode ser aumentado para reforçar os reflexos e os brilhos nos olhos de um personagem, por exemplo. Exige o modo de sombreamento PBR.

### ![](/icons/culling.webp) Inverter culling {#inverse-culling}
Inverte as normais de uma superfície. Normalmente não é necessário, mas pode ser usado se um modelo parecer estar do avesso, ou, junto com `Dois lados` desativado, para criar interiores em que a parede mais próxima da câmera fica sempre oculta.

As opções a seguir podem ser definidas como `Auto`, `Não` ou `Sim`. Com `Auto`, a seta mostra o valor que está sendo realmente usado.

### ![](/icons/sphere_smooth.webp) Sombreamento suave {#smooth-shading}
Veja a [opção global](settings.md#smooth-shading).  
O valor `Auto` usa a opção global.

### ![](/icons/culling.webp) Dois lados {#two-sided}
As faces ficam visíveis dos dois lados. Veja a [opção global](settings.md#two-sided-quick).  
O valor `Auto` usa a opção global.

### ![](/icons/culling.webp) Verso colorido {#coloured-backface}
Veja a [opção global](settings.md#two-sided-quick).
O valor `Auto` usa a opção global.

### ![](/icons/shadow_cast.webp) Projetar sombras {#casts-shadows}
Os objetos transparentes também projetam sombras (num padrão pontilhado, para imitar sombras misturadas).  
Lembre-se de desativar a projeção de sombras se houver na cena um objeto grande que não precise projetá-las (por exemplo um chão enorme).

### ![](/icons/shadow_receive.webp) Receber sombras {#recieve-shadows}
Define se as sombras dos outros objetos são desenhadas sobre este objeto.

### ![](/icons/wireframe.webp) Armação {#wireframe}
Veja a [opção global](settings.md#wireframe).  
O valor `Auto` usa a opção global.

### ![](/icons/trash.webp) Redefinir normais {#reset-normals}
Só aparece quando um objeto importado traz as suas próprias normais (por exemplo com `Manter topologia`). Remove essas normais, para que o sombreamento use as normais calculadas a partir da superfície.


## Texturas {#textures}

![](/images/material_textures.webp)

Se um objeto tiver UVs, é possível aplicar texturas ao material além da cor/aspereza/metalidade/opacidade dos vértices. Normalmente elas vêm de um bake de textura, mas imagens criadas fora do Nomad também podem ser usadas. `UV:✓` ou `UV:✗` ao lado do título indica se o objeto tem UVs.

As texturas podem ser aplicadas a

* Cor
* Normal
* Aspereza
* Metalidade
* Opacidade
* Deslocamento
* Emissiva

Uma linha `Oclusão` também aparece quando um objeto importado tem uma textura de oclusão, mas o Nomad não a usa.

O controle de cada linha define com que força a textura é aplicada, de nada até totalmente. `Cor` e `Emissiva` também têm uma amostra de cor que tinge a textura, e `Emissiva` define a intensidade do brilho.

`Deslocamento` define o quanto o mapa de deslocamento empurra a superfície. O botão `Aplicar` move os vértices pelo deslocamento e depois remove o mapa. O resultado vai para a camada ativa.

O botão de paleta ao lado do título abre os pré-ajustes de material do menu [Pintura](painting.md): toque em um para copiar as texturas dele para o objeto. No computador, as imagens importadas são sincronizadas com o arquivo original quando você volta para o Nomad, e um botão de sincronização ao lado do título as recarrega.

Clicar em um espaço de textura abre um seletor. Depois que uma textura foi atribuída a um espaço do material, clicar de novo abre um painel de textura:

### Opções do painel de textura {#texture-panel-options}

![](/images/material_texture_panel.webp)

O painel mostra o tamanho da imagem e uma pré-visualização da textura.

### ![](/icons/open.webp) Abrir {#open}
Escolhe outra textura. No computador, `Explorar` mostra o arquivo de imagem no seu navegador de arquivos.

### ![](/icons/circle_cross.webp) Nenhum {#none}
Remove a textura

### Opacidade {#texture-opacity}

Só para a textura de cor. Se a imagem tiver um canal alfa, permite usá-lo como opacidade ou ignorá-lo.

### Formato {#normal-format}
Só para a textura normal. Os mapas normais existem em duas variantes, `OpenGL (+Y)` e `DirectX (-Y)`. Se os detalhes parecerem invertidos, experimente a outra.

### Altura {#displacement-height}
Só para a textura de deslocamento.
* `Local` - A altura cresce e diminui com a escala do objeto.
* `Mundo` - A altura fica igual, seja qual for a escala do objeto.

### Multiplicar {#multiply}
Só para as texturas de aspereza, metalidade e opacidade. Multiplica os valores da textura. Quando não está em 100%, o valor aparece no espaço de textura.

### ![](/icons/link.webp) Ícone de corrente/elo {#chainlink-icon}

O ícone de corrente nas seções a seguir, quando ativado, faz com que as opções usadas sejam compartilhadas com as outras texturas (cor, normal, aspereza, metalidade, opacidade, emissiva) que também têm o ícone de corrente ativado.

Assim, se você tiver texturas alinhadas, elas continuam alinhadas mesmo quando você muda os parâmetros ou os tipos de projeção.


### Projeção {#projection}
![](/images/material_projection.webp)

Define como a textura é aplicada ao objeto.

* `Auto` - Se o objeto tiver UVs, UV; senão, Triplano
* `UV` - Usa as coordenadas UV da malha para aplicar a textura. Se a malha e a textura vierem de fora do Nomad, ou se forem ser exportadas do Nomad para uso em outro lugar, UV é a opção certa.
* `Triplano` - Projeta a textura ao longo dos eixos X, Y e Z e mistura as emendas.

### Triplano {#triplanar}
![](/images/material_triplanar.webp)

As projeções triplano são uma maneira poderosa e ao mesmo tempo simples de aplicar texturas aos objetos.

O triplano é como ter 6 projetores de vídeo com a mesma imagem, iluminando a frente, o fundo, a esquerda, a direita, o topo e a base do seu objeto.

Depois, isso pode ser selado em UVs ou em cores de vértices, se necessário.


![](/images/material_triplanar_example.webp)

#### Método {#method}

* `Local` - A projeção se move junto com a transformação do objeto
* `Mundo` - As projeções ficam fixas: mover o objeto o faz deslizar através da projeção.

#### Dureza {#hardness}

Como as projeções se misturam. 100% não faz mistura nenhuma, e as bordas das projeções ficam nítidas. 0% mistura as bordas em um ângulo amplo. O padrão é 90%, mistura suficiente para esconder as bordas e deixar o resto das projeções nítido.

### Uniforme {#uniform}

Quando marcado, a mesma dureza é usada em todas as projeções. Quando desmarcado, aparecem controles de dureza separados para as projeções X, Y e Z.


### Parâmetro {#parameter}
![](/images/material_parameter.webp)

#### Filtragem {#filtering}
O método de filtragem da textura: `Auto` é o padrão, e os métodos são `Mais próximo`, `Linear` e `Mipmap`. Mais próximo não faz filtragem, então as texturas podem ficar serrilhadas vistas de perto. Linear e Mipmap filtram melhor, então de perto as texturas ficam desfocadas em vez de serrilhadas.

#### Matrização - X {#tiling-x}
Se o parâmetro Escala for maior que 1, deixando a textura menor que as UVs do objeto, define como a textura se repete ao longo do eixo X. `Nenhum` não faz repetições. `Repetir` faz cópias da textura. `Espelhar` faz cópias da textura, invertendo uma a cada duas, o que pode ajudar a esconder os artefatos da repetição.

#### Matrização - Y {#tiling-y}
Igual a Matrização - X, mas para o eixo Y.

### Transformar {#transform}
![](/images/material_transform.webp)

Transformações 2d extras aplicadas à textura no espaço UV. O botão de redefinir volta aos valores padrão, e o ícone de corrente (quando outras texturas além da cor estão selecionadas) liga ou desliga a transformação para que fique igual à da textura de cor.

#### Translação {#translation}
O deslocamento X e Y da textura

#### Rotação {#rotation}
A rotação da textura

#### Escala {#scale}
A escala da textura: números maiores deixam a textura menor no objeto. Use as opções Matrização - X e Matrização - Y para controlar o que acontece.

### Escala uniforme {#uniform-scale}
Quando desativada, o Nomad mostra controles separados para Escala X e Escala Y.

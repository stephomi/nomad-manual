# ![](/icons/postprocess.webp) Pós-processamento 

Este menu controla muitos aspectos do Nomad que afetam a aparência do render.

![](/images/postprocess_overview_drac.webp)

Usar pós-processamento pode mudar substancialmente o visual final da sua cena.

![](/images/postprocess_overview.webp)
*A mesma cena antes e depois do pós-processamento, sem luzes adicionais ou mudanças de material.*

O pós-processamento pode impactar bastante a performance dependendo do seu dispositivo.
Há uma caixa de seleção global para desativar todo o pós-processamento, para que você possa voltar rapidamente à escultura/modelagem sem perder seus presets.
Para renderização PBR, [Oclusão de Ambiente](#ambient-occlusion-ssao), [Reflexão](#reflection-ssr) e [Tone Mapping](#tone-mapping) devem estar ativados.

No entanto, na maior parte do tempo você vai querer o pós-processamento desativado enquanto estiver esculpindo, para focar na própria forma do modelo.

## Qualidade

![](/images/postprocess_quality.webp)
### Amostragem máxima por frame
O Nomad calculará uma certa quantidade de pós-processamento para um único frame, o que pode parecer ruidoso. Este controle determina quantos frames serão renderizados e depois mesclados para remover a maior parte dos artefatos de ruído. Alguns efeitos não exigem amostras extras (por exemplo, color grading), enquanto outros, como iluminação global, podem exigir centenas de amostras para ficarem livres de ruído. 

No viewport isso pode ser visto sempre que o Nomad é deixado parado: a qualidade da imagem será gradualmente refinada até o número máximo de amostras, então para. Esse número de cálculos também é usado na seção de render do [menu Files](files) quando “export png” é clicado.

### Multiplicador de resolução
Este controle deslizante controla a resolução do pós-processamento. Um valor de x1.0 significa que os renders são feitos na resolução de pixels do dispositivo. Um valor de x0.5 renderizará em meia resolução, o que será rápido, mas de baixa qualidade. Um valor maior que 1 renderizará em um tamanho maior e depois reduzirá a escala. Isso resulta em maior qualidade, menos ruído, mas tempos de render mais longos.

### Amostras máximas

Isso aumentará a qualidade do pós-processamento, mas geralmente `Full resolution` terá mais impacto. 

### Full resolution
Quando ativado, força o multiplicador de resolução para x1.0

### Denoiser (oidn)

Aplica um denoiser à imagem. Isso pode permitir que você use um número muito menor de amostras. Só funciona se `Full Resolution` estiver ativado. Note que a remoção de ruído acontece depois que todas as amostras foram calculadas e pode ser intensiva para o processador.

## Navegador de presets
![](/images/postprocess_presets.webp)
Clicar na imagem exibirá uma coleção de presets de pós-processamento. Para definir seus próprios presets, selecione um, clique em “clone” e faça alterações. Para salvar, clique na imagem do preset, clique novamente dentro do navegador de presets e escolha “save”.

## Reflexão (SSR)
Com esta opção, objetos podem refletir outros objetos na cena, desde que os objetos estejam visíveis na tela.
Se você tiver objetos metálicos e brilhantes na sua cena, então esta opção provavelmente deve ser usada.
Esta opção só é efetiva com o modo PBR.

| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Iluminação Global (SSGI)

A iluminação global simula como a luz rebate entre superfícies, por exemplo, uma parede vermelha lançará vermelho sobre um objeto branco próximo. Isso pode aumentar enormemente o realismo de um render quando usado com oclusão de ambiente e reflexões. 

`Strength` - A intensidade da iluminação global. 

| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Um spotlight está atrás da esfera, apontado para o teto. Com SSGI desligado, apenas o teto é iluminado. Com SSGI ligado, a luz rebate do teto para as paredes e para a esfera._

## Oclusão de Ambiente (SSAO)
A oclusão de ambiente escurece áreas onde a luz tem menos chance de alcançar (cantos, etc.).
O efeito depende apenas da geometria do modelo.

* `Strength` - Intensidade do efeito.
* `Size` - Quão amplo é o efeito.
* `Curvature bias` - Quão sensível o efeito é em relação à variação da superfície.
* `Color` - Um tom multiplicado na oclusão, usado para efeitos criativos.

| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
A AO será mais visível em áreas iluminadas principalmente pela luz de ambiente. Áreas sob luz direta forte receberão um efeito de AO muito mais fraco.

:::

## Profundidade de Campo (DOF)
Adiciona um efeito de desfoque na região que está fora de foco.

Basta tocar no seu modelo para mudar o ponto de foco.

* `Far blur` - A quantidade de desfoque a ser aplicada no lado distante do ponto de foco.
* `Near blur` - A quantidade de desfoque a ser aplicada entre o ponto de foco e a câmera.

| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |

## Bloom
Bloom fará com que as áreas brilhantes da sua cena brilhem.

* `Intensity` - Força do efeito.
* `Radius` - A propagação do efeito.
* `Threshold` - Quão brilhantes os pixels precisam ser na cena antes de começarem a gerar bloom. Definir esse valor baixo fará tudo brilhar; definir alto permitirá que apenas os pixels mais brilhantes gerem bloom.
* `Color` - Um tom que pode ser adicionado ao bloom para efeitos criativos.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |

## Tone Mapping
Tone Mapping é uma operação que remapeia valores HDR para o intervalo `[0, 1]`.
Se você não usá-lo (ou selecionar `none`), qualquer componente de cor maior que 1 será recortado.
Quaisquer variações de cor acima desse intervalo serão então perdidas.

* `None/Neutral/Agx/ACES` - qual tonemapper usar. `None` não faz remapeamento (mas os outros controles ainda funcionam). As outras opções são semelhantes a escolher diferentes tipos de filme: elas lidarão com valores superexpostos e cores de maneiras diferentes. Este é um tópico muito profundo; pesquise tone mapping, Agx, ACES para mais informações!
* `Exposure` - brilho geral das imagens, semelhante a ajustar a abertura em uma câmera. Pode ser uma forma rápida de clarear ou escurecer globalmente uma imagem.
* `Saturation` - força da cor. 1 é neutro, 0 é monocromático, valores acima de 1 são cada vez mais saturados.
* `Contrast` - Deixa os escuros mais escuros e os claros mais claros. Use com cuidado, pode introduzir artefatos em valores altos.

Note que com o `Tone Mapping` desativado, alguns detalhes desaparecem porque os pixels estão brilhantes demais.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
O tone mapping pode realçar o efeito da iluminação global. Se você diminuir a intensidade do mapa de ambiente e aumentar a fonte de luz primária, pode aumentar a `exposure` do tone mapping para ver mais dos efeitos de luz rebatida.
:::

## Color Grading
Semelhante à ferramenta de curvas no Photoshop, isso permite controlar o equilíbrio e a distribuição de cor na imagem. O controle `main` afeta todo o balanço de cor; os controles `red`/`green`/`blue` permitem um controle fino. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Detecta onde há mudanças rápidas de curvatura e aplica uma cor a essas regiões.

* `Factor` - intensidade geral do efeito
* `Bump` - quanto ele encontrará mudanças convexas acentuadas e colocará a cor selecionada ali (branco por padrão)
* `Cavity` - quanto ele detectará mudanças côncavas e colocará a cor selecionada ali (preto por padrão)

| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |

## Aberração Cromática
Simula artefatos de lente com a luz sendo decomposta ao redor das bordas da tela.

* `Strength` - quanto as partes vermelha/verde/azul da imagem são separadas em direção às bordas da tela

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |

## Vinheta
Simula artefatos de lente escurecendo as bordas da tela.

* `Size` - O tamanho de uma elipse invertida colocada sobre a imagem
* `Hardness` - Quão borrada ou nítida a elipse é misturada sobre a imagem.

| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Granulação
Adiciona um efeito de granulação; pode ajudar a deixar a imagem um pouco menos artificial.

* `Strength` - a quantidade de grão/ruído adicionada à imagem.

| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |

## Nitidez
Um efeito de nitidez semelhante ao encontrado no Photoshop ou em apps de processamento de fotos.

* `Strength` - a quantidade de nitidez aplicada à imagem.

| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Simula pixel art de jogos retrô.

* `Slider` - tamanho dos pixels
* `Allow frame sampling` - se você estiver obtendo muitos pixels pretos, tente ativar isto, o que substituirá a amostragem padrão.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Simula a aparência de antigos monitores CRT.

* `Factor` - força das linhas
* `Spacing` - tamanho das linhas

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

## Dithering

Aplica dithering aos pixels para reduzir artefatos de banding. Normalmente isso deve estar ativado, mas pode ser desligado para operações específicas (por exemplo, exportar mapas de profundidade ou outras operações específicas de dados).

# ![](/icons/postprocess.webp) Pós-processamento {#post-process}

Este menu controla vários aspectos do Nomad que afetam a aparência da renderização.

![](/images/postprocess_overview_drac.webp)

Usar o pós-processamento pode mudar bastante a aparência final da sua cena.

![](/images/postprocess_overview.webp)
*A mesma cena antes e depois do pós-processamento, sem luzes extras nem mudanças de material.*

O pós-processamento pode pesar bastante no desempenho, dependendo do seu dispositivo.
Há uma caixa de seleção global `Pós-processamento` que desativa todo o pós-processamento, para você voltar rapidamente a esculpir/modelar sem perder seus pré-ajustes.
Para a renderização PBR, a [Oclusão Ambiente](#ambient-occlusion-ssao), a [Reflexão](#reflection-ssr) e o [Mapeamento de Tons](#tone-mapping) devem estar ativados.

Mas, na maior parte do tempo, é melhor deixar o pós-processamento desativado enquanto esculpe, para se concentrar na forma em si e não na renderização.


## Qualidade {#quality}

![](/images/postprocess_quality.webp)

Estas opções melhoram a qualidade da renderização, ao custo do desempenho.

### Amostragem máxima de quadros {#max-frame-sampling}
O Nomad calcula uma certa quantidade de pós-processamento em cada quadro renderizado, o que pode parecer ruidoso. Este controle define quantos quadros serão renderizados e depois combinados para remover a maior parte do ruído. Alguns efeitos não precisam de amostras extras (por exemplo a gradação de cores), enquanto outros, como sombras suaves e iluminação global, podem precisar de centenas de amostras para ficarem sem ruído.

No visor, isso aparece sempre que o Nomad fica parado: a qualidade da imagem vai se refinando aos poucos até o máximo de amostras e então para. Quando para, o Nomad não faz mais nada, o que economiza bateria. Esse número de cálculos também é usado na seção de renderização do [menu Arquivo](files) quando você clica em 'exportar png'.

A caixa de seleção ao lado do controle liga ou desliga a amostragem de quadros.

### Resolução da renderização {#resolution-multiplier}
Este controle define a resolução da renderização. Um valor de x1.0 significa que a renderização é feita na resolução em pixels do dispositivo. Um valor de x0.5 renderiza na metade da resolução, o que é rápido mas de baixa qualidade. Um valor maior que 1 renderiza em um tamanho maior e depois reduz. O resultado é uma qualidade maior, com menos ruído, mas com renderizações mais demoradas.

Ele tem um grande impacto no desempenho, então tente mantê-lo em x1.25 ou menos. Esse valor não é salvo nos ajustes, e o efeito [Pixel Art](#pixel-art) o substitui.

### ![](/icons/intensity.webp) Máximo de amostras {#max-samples}

Melhora a qualidade dos efeitos de pós-processamento, ao custo do desempenho.

### ![](/icons/material_dithering.webp) Pontilhamento {#dithering}

Pontilha os pixels para reduzir os artefatos de faixas (em degradês ou na vinheta, por exemplo). Normalmente deve ficar ativado, mas pode ser desligado em operações específicas (por exemplo ao exportar mapas de profundidade ou outros dados).

### ![](/icons/denoise.webp) Removedor de Ruído (oidn) {#oidn}

Aplica um removedor de ruído à imagem depois que todos os quadros foram acumulados. Isso permite usar muito menos amostras. A remoção de ruído exige bastante do processador, então só ative se a sua imagem estiver ruidosa. Não está disponível em todos os dispositivos.

## Navegador de pré-ajustes {#preset-browser}
![](/images/postprocess_presets.webp)
Clicar na imagem abaixo do título `Pós-processamento` mostra uma coleção de pré-ajustes de pós-processamento. Use `Novo` para criar um pré-ajuste a partir dos seus ajustes atuais. Os pré-ajustes embutidos só podem ser clonados: para criar o seu, selecione um, clique em `Clonar` e faça as alterações. Quando um pré-ajuste tem alterações ainda não salvas, ele mostra `Alterações não salvas!`; para salvar, clique na imagem do pré-ajuste, clique de novo dentro do navegador de pré-ajustes e escolha `Salvar`.

## Barra de atalhos {#shortcut-bar}
Quando o pós-processamento está ativado, uma barra na parte de baixo do menu lista todos os efeitos (`SSR`, `SSGI`, `SSAO`, `DoF`, `Incandescência`...). Toque em um para ir direto à seção dele. Os efeitos desligados ficam acinzentados, então a barra também serve como um resumo rápido do que o pré-ajuste atual faz.

## ![](/icons/postprocess_ssr.webp) Reflexão (SSR) {#reflection-ssr}
Com esta opção, os objetos podem refletir outros objetos da cena, desde que esses objetos estejam visíveis na tela.
Se você tiver objetos metálicos e brilhantes na cena, provavelmente vale a pena usar esta opção.
Esta opção exige o modo de sombreamento [Iluminado (PBR)](shading.md#pbr).


| SSR desligado              | SSR ligado                |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Iluminação Global (SSGI) {#global-illumination-ssgi}

A iluminação global simula como a luz rebate entre as superfícies; por exemplo, uma parede vermelha projeta vermelho sobre um objeto branco próximo. Isso pode aumentar muito o realismo de uma renderização quando usado junto com a oclusão ambiente e os reflexos. Assim como os reflexos, exige o modo de sombreamento [Iluminado (PBR)](shading.md#pbr).

`Intensidade` - A intensidade da iluminação global.



| SSGI desligado             | SSGI ligado               |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Um spot está atrás da esfera, apontado para o teto. Com o SSGI desligado, só o teto fica iluminado. Com o SSGI ligado, a luz rebate do teto para as paredes e para a esfera._

## ![](/icons/postprocess_ssao.webp) Oclusão Ambiente (SSAO) {#ambient-occlusion-ssao}
A oclusão ambiente escurece as áreas onde a luz tem menos chance de chegar (cantos, etc.).
O efeito depende apenas da geometria do modelo.

* `Intensidade`- Intensidade do efeito.
* `Tamanho`- O quanto o efeito se espalha.
* `Espessura` - A espessura de profundidade assumida para os oclusores, em porcentagem do `Tamanho`.
* `Matiz` - Uma cor multiplicada na oclusão, para efeitos criativos.


| SSAO desligado              | SSAO ligado                |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
A AO fica mais visível nas áreas iluminadas principalmente pela luz do ambiente. As áreas sob uma luz direta forte recebem um efeito de AO bem mais fraco.

:::

## ![](/icons/postprocess_dof.webp) Profundidade de Campo {#depth-of-field-dof}
Adiciona um efeito de desfoque na região fora de foco.

Basta tocar no seu modelo para mudar o ponto de foco.

* `Modo de abertura` - Controla o desfoque com uma única abertura de câmera, em vez dos dois controles de desfoque abaixo.
* `Abertura` (_só no modo de abertura_) - O número f da lente, como em uma câmera real. Um valor menor abre mais a lente e desfoca mais.
* `Desfoque longe` - A quantidade de desfoque aplicada atrás do ponto de foco.
* `Desfoque perto` - A quantidade de desfoque aplicada entre o ponto de foco e a câmera.


| DOF desligado             | DOF focado no anel distante | DOF focado no anel próximo |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Incandescência {#bloom}
A incandescência faz as áreas claras da cena brilharem.

* `Intensidade` - força do efeito.
* `Raio` - O alcance do efeito.
* `Limite` - O quanto os pixels precisam ser claros para começar a brilhar. Em 0 tudo brilha; um valor alto faz só os pixels mais claros brilharem.
* `Matiz` - uma cor que pode ser adicionada à incandescência para efeitos criativos.

| Incandescência desligada     | Incandescência com raio 0   | Incandescência com raio 1   |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mapeamento de Tons {#tone-mapping}
O mapeamento de tons é uma operação que remapeia os valores HDR para o intervalo `[0, 1]`.
Se você não usá-lo (ou escolher `Nenhum`), qualquer componente de cor maior que 1 será cortado.
Qualquer variação de cor acima desse intervalo será perdida.

* `Nenhum/Neutro/Agx/ACES` - qual mapeador de tons usar. `Nenhum` não faz nenhum remapeamento (mas os outros controles continuam funcionando). As outras opções são como escolher filmes fotográficos diferentes: cada uma lida de um jeito com os valores e as cores superexpostos. É um assunto bem profundo, pesquise sobre tone mapping, Agx e ACES para saber mais!
* `Exposição` - brilho geral da imagem, parecido com ajustar a abertura de uma câmera. É um jeito rápido de clarear ou escurecer a imagem inteira.
* `Saturação` - força das cores. 1 é neutro, 0 é monocromático, e valores acima de 1 são cada vez mais saturados.
* `Contraste` - Deixa os escuros mais escuros e os claros mais claros. Use com cuidado, pois pode gerar artefatos em valores altos.

Repare que, com o `Mapeamento de Tons` desativado, alguns detalhes desaparecem porque os pixels ficam claros demais.

| Mapeamento de Tons desligado | Mapeamento de Tons ligado  |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
O mapeamento de tons pode reforçar o efeito da iluminação global. Se você diminuir a intensidade do mapa de ambiente e aumentar a da fonte de luz principal, pode subir a `Exposição` do mapeamento de tons para ver melhor os efeitos da luz rebatida.
:::

## ![](/icons/postprocess_tone_curve.webp) Gradação de Cores {#color-grading}
Parecido com a ferramenta de curvas do Photoshop, permite controlar o equilíbrio e a distribuição das cores na imagem. O controle `Principal` afeta o equilíbrio de cores inteiro, e os controles `Vermelho`/`Verde`/`Azul` permitem ajustes finos.

| Gradação de Cores desligada   | Gradação de Cores ligada     |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Curvatura {#curvature}
Detecta onde há mudanças bruscas de curvatura e aplica uma cor nessas regiões.

* `Fator` - intensidade geral do efeito
* `Protuberância` - o quanto ele detecta mudanças convexas bruscas e coloca ali a cor escolhida (branco por padrão)
* `Cavidade` - o quanto ele detecta mudanças côncavas e coloca ali a cor escolhida (preto por padrão)
* `Espessura` - a largura das bordas detectadas.

Ao lado de `Protuberância` e `Cavidade`, uma amostra de cor escolhe a cor, e um pequeno botão escolhe como essa cor se mistura com a imagem.


| Curvatura desligada              | Curvatura ligada               |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberração Cromática {#chromatic-aberration}
Simula os artefatos de lente em que a luz se decompõe perto das bordas da tela.

* `Intensidade` - o quanto as partes vermelha/verde/azul da imagem se separam em direção às bordas da tela

| Cromática desligada           | Cromática ligada             |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinheta {#vignette}
Simula os artefatos de lente escurecendo as bordas da tela.

* `Tamanho` - O tamanho de uma elipse invertida colocada sobre a imagem
* `Dureza` - O quanto a elipse se mistura de forma suave ou nítida sobre a imagem.
* `Matiz` - A cor da vinheta, preta por padrão.


| Vinheta desligada               | Vinheta ligada                 |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Granulação {#grain}
Adiciona um efeito de granulação, que pode deixar a imagem um pouco menos artificial.

* `Intensidade` - a quantidade de granulação/ruído adicionada à imagem.


| Granulação desligada         | Granulação ligada          |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Nitidez {#sharpness}
Um efeito de nitidez parecido com o do Photoshop ou de apps de edição de fotos.

* `Intensidade` - a quantidade de nitidez aplicada à imagem.


| Nitidez desligada              | Nitidez ligada               |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Simula a pixel art dos jogos retrô. Este efeito substitui a [Resolução da renderização](#resolution-multiplier).

* `Controle deslizante` - tamanho dos pixels
* `Permitir amostragem de quadros` - se aparecerem muitos pixels pretos, tente ativar esta opção. Sem ela, o efeito pixel art desliga a [amostragem de quadros](#max-frame-sampling).

| Pixel desligado             | Pixel ligado               |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Linha de escaneamento {#scanline}
Simula a aparência dos antigos monitores CRT.

* `Fator` - força das linhas
* `Espaçamento` - tamanho das linhas

| Linha de escaneamento desligada | Linha de escaneamento ligada |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

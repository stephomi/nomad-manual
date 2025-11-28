# ![](/icons/paint.webp) Pintura {#painting}

Controle a cor, rugosidade, metalicidade dos traços de pintura, permita o preenchimento global dos atributos de pintura e defina como as ferramentas de pintura interagem com camadas, máscaras e seleções ocultas.

![](/images/paint_overview.webp)  

## Visão geral {#overview}

O Nomad usa pintura de vértices PBR. O que isso significa?

### PBR {#pbr}
PBR, ou Renderização Baseada Fisicamente (Physically Based Rendering), é uma técnica popular de computação gráfica para cinema, televisão, jogos e dispositivos móveis. Ao basear as luzes em propriedades físicas e definir superfícies por meio de cor, rugosidade e metalicidade, é possível obter uma grande variedade de visuais fotorrealistas.

### Pintura de vértices {#vertex-painting}

Pintura por vértices significa que as informações de pintura são armazenadas nos vértices do modelo, em vez de em texturas. Como o Nomad consegue lidar com modelos com centenas de milhares, frequentemente milhões de vértices, seus modelos devem ser capazes de ter pintura de superfície altamente detalhada; se você consegue esculpir o detalhe, também consegue pintá‑lo.

Isso também significa que pintar no Nomad não exige mapeamento UV, frequentemente um processo lento e técnico em outros aplicativos 3D. Muitos outros aplicativos 3D não suportam as altas contagens de vértices que o Nomad suporta; no entanto, o Nomad também possui boas ferramentas de bake de textura e de decimação para ajudar.

### Texturização {#texturing}

O Nomad oferece suporte a texturas, mas elas precisam estar presentes em um modelo importado ou serem geradas por meio do bake da pintura de vértices em texturas. 

Uma textura é simplesmente uma imagem, mas no contexto 3D geralmente se refere a uma imagem atribuída a um objeto.
Para envolver uma imagem em torno de um modelo, o modelo precisa de coordenadas de textura (UV).

O Nomad pode [calculá‑las automaticamente](topology.md#uv-unwrap), mas você não tem muito controle sobre a qualidade geral.

::: tip
Um exemplo de fluxo de trabalho:
- Esculpir no Nomad, depois fazer o [UV unwrap](topology.md#uv-unwrap)
- Se você já começou a pintar no Nomad, pode [transferir a pintura de vértices para texturas](topology.md#bake-vertex-colors-to-texture)
- Exportar para o Procreate
- Texturizar no Procreate
- Exportar de volta para o Nomad para fins de renderização
:::

Essa é a visão geral, agora vamos explorar as seções do menu de pintura:


## Pintura por traço {#stroke-painting}
![](/images/paint_intensity.webp)  

Ativa a pintura para esta ferramenta, útil se você precisar esculpir e pintar ao mesmo tempo.

Para ferramentas em que a pintura é a função principal (por exemplo, Paint, Smudge, Mask), essa caixa de seleção não existe.

### Intensidade da pintura {#paint-intensity}

Um controle deslizante que permite usar uma intensidade diferente da intensidade principal da ferramenta.

As caixas de seleção `Alpha`, `Falloff` e `Randomize` determinam se esses recursos afetarão a pintura. Por exemplo, você pode ter randomize ativado para a ferramenta Clay, mas a cor não será randomizada.


## Material {#material}
![](/images/paint_material.webp) 

O primeiro ícone é uma forma de pré‑visualização de material. Arrastar na pré‑visualização 3D do material irá girá‑la. 

O segundo ícone é uma pré‑visualização do traço de pintura com o alpha e o falloff selecionados.

O botão de pré‑visualização ao lado do título Material permite alternar entre none, Material ou Triplanar. Isso determina o que acontecerá quando você alterar interativamente as propriedades de pintura:

* `None` - Nenhuma pré‑visualização será mostrada no modelo ao ajustar as propriedades
* `Material` - Os valores do material serão pré‑visualizados no objeto ao ajustar as propriedades. Se você usar texturas e o modelo tiver UVs, os UVs serão usados.
* `Triplanar` - O material será pré‑visualizado como uma projeção Triplanar. 

O conta‑gotas pode ser usado para amostrar todas as propriedades de um objeto na sua cena.

## Predefinições de material {#material-presets}
Tocar na forma de pré‑visualização 3D abrirá um menu de presets de materiais, que podem ser clonados para definir seus próprios presets.

![](/images/paint_presets.webp) 

As alternâncias `Embed Textures` e `Alpha`, quando ativadas, armazenarão quaisquer texturas usadas por esse material dentro do preset. Isso é explicado com mais detalhes abaixo.

## Deslizadores PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

A pintura [PBR](shading.md#pbr) usa 4 canais:
- `Color` A cor que será pintada. O conta‑gotas pode ser usado para selecionar cor de outras partes do modelo ou de imagens de referência.
- `Roughness` Indica quão "áspera" ou "lisa" é uma superfície. Um valor baixo de rugosidade significa que os reflexos serão nítidos.
- `Metalness` Indica simplesmente se a superfície é metálica ou não. O valor deve ser 0% ou 100% na maior parte do tempo; valores intermediários devem ser excepcionais.
- `Opacity` Quanto o material pode ser visto através. Estritamente falando, não faz parte da especificação PBR, mas é útil em muitas situações. 1 é totalmente opaco, 0 é transparente. Note que opacidade e refração são coisas diferentes; a refração no Nomad é tratada via o material de refração. 

Se você selecionar um preset de material, 3 canais são pintados simultaneamente (a opacidade é frequentemente excluída de propósito). Isso significa que, em vez de apenas pintar "vermelho", você pode estar pintando "um metal vermelho áspero" ou "um plástico branco liso".

O quadrado é um slot de textura; clique nele para usar uma textura para essa propriedade em vez de um valor sólido.

O ícone de pincel ao lado dos deslizantes fará um preenchimento global dessa propriedade em seu objeto.

A caixa de seleção ativará ou desativará aquela propriedade específica, então você pode, por exemplo, pintar apenas cor, ou apenas rugosidade e opacidade. 

Aqui estão alguns exemplos de diferentes propriedades de rugosidade e metalicidade:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Apenas cor é suportada no modo [Matcap rendering](shading.md#matcap); metalness e roughness são ignorados.
:::

::: tip
Ao usar texturas para pintura PBR, muitas vezes é útil trocar para algo como a ferramenta `Stamp`, ou usar o menu Stroke para usar um modo diferente de dot, que pode borrar a textura.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Você pode considerar ativar o `Smooth Shading` [globalmente](settings.md#smooth-shading) ou [por objeto](material.md#smooth-shading) se estiver pintando uma superfície metálica em um objeto com baixa contagem de polígonos.
:::

## Pintar tudo {#paint-all}

![](/images/paint_paint_all.webp)

Aplica o material atual ao objeto, seja no modo padrão com 'Paint All', seja como uma projeção Triplanar.

As caixas de seleção ao lado dos deslizantes de color/metalness/roughness/opacity são respeitadas; quaisquer propriedades desativadas não serão preenchidas.

Os botões extras controlam como o Paint All pode ser ainda mais afetado:

| Icon                        | Description                                      |
| :-------------------------: | :----------------------------------------------: |
| ![](/icons/tool_mask.webp) | Áreas mascaradas não serão afetadas.             |
| ![](/icons/tool_hide.webp) | Áreas ocultas não serão afetadas.                |
| ![](/icons/opacity.webp)   | Usar o fator de pintura da ferramenta acima.     |
| ![](/icons/layer.webp)     | Áreas não pintadas de uma camada não serão afetadas. |
| ![](/icons/triplanar.webp) | Indicador das configurações de triplanar         |
| ![](/icons/cog.webp)       | Abre as configurações de Triplanar               |

### Configurações triplanares {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Semelhante às [configurações de triplanar no menu de material](material.md#triplanar), você pode controlar a mesclagem das projeções, repetição (tiling) e deslocamentos. 

Use a caixa de seleção de pré‑visualização no topo deste menu para ativar uma pré‑visualização persistente enquanto ajusta os valores.

## Material global {#global-material}
Se esta opção estiver ativada, o material selecionado será o mesmo das outras ferramentas. Note que ela leva em conta apenas as configurações de roughness, metalness e color.
# ![](/icons/paint.webp) Pintura {#painting}

Controla a cor, a aspereza e a metalidade dos traços de pintura, permite preencher o objeto inteiro com esses atributos e define como as ferramentas de pintura interagem com as camadas, as máscaras e as áreas ocultas.

![](/images/paint_overview.webp)  

## Visão geral {#overview}

O Nomad usa pintura de vértices PBR. O que isso significa?

### PBR {#pbr}
PBR, ou Physically Based Rendering (renderização baseada em física), é uma técnica de computação gráfica muito usada em cinema, televisão, jogos e dispositivos móveis. Ao basear a iluminação em propriedades físicas e definir as superfícies por cor, aspereza e metalidade, é possível obter uma grande variedade de aparências fotorrealistas.

### Pintura de vértices {#vertex-painting}

Pintura de vértices significa que as informações de pintura ficam guardadas nos vértices do modelo, e não em texturas. Como o Nomad lida com modelos de centenas de milhares, muitas vezes milhões de vértices, seus modelos podem ter uma pintura de superfície muito detalhada: se você consegue esculpir o detalhe, também consegue pintá-lo.

Isso também significa que pintar no Nomad não exige mapeamento UV, um processo muitas vezes lento e técnico em outros aplicativos 3d. Muitos aplicativos 3d não suportam a quantidade de vértices que o Nomad suporta, mas o Nomad também tem boas ferramentas de bake de textura e de decimação para ajudar.

### Texturização {#texturing}

O Nomad suporta texturas, mas elas precisam vir em um modelo importado, ou ser criadas fazendo o bake da pintura de vértices em texturas.

Uma textura é simplesmente uma imagem, mas no contexto 3d costuma se referir a uma imagem atribuída a um objeto.
Para envolver um modelo com uma imagem, o modelo precisa de coordenadas de textura (UV).

O Nomad consegue [calculá-las automaticamente](topology.md#uv-unwrap), mas você não tem muito controle sobre a qualidade geral.

::: tip
Um exemplo de fluxo de trabalho:
- Esculpa no Nomad e depois faça o [desdobramento UV](topology.md#uv-unwrap)
- Se você já começou a pintar no Nomad, pode [transferir a pintura de vértices para texturas](topology.md#bake-texture)
- Exporte para o Procreate
- Texturize no Procreate
- Exporte de volta para o Nomad para renderizar
:::

Essa é a visão geral, agora vamos explorar as seções do menu de pintura:


## Pintura com traçado {#stroke-painting}
![](/images/paint_intensity.webp)  

Ativa a pintura para esta ferramenta, útil se você precisa esculpir e pintar ao mesmo tempo. Quando uma ferramenta pode pintar mas esta caixa está desmarcada, um ícone de aviso ao lado do título lembra você disso.

Nas ferramentas cuja função principal é pintar (por exemplo Pintar, Borrar, Máscara), essa caixa de seleção não existe.

### ![](/icons/opacity.webp) Intensidade da pintura {#paint-intensity}

Um controle deslizante para usar uma intensidade diferente da intensidade principal da ferramenta.

O botão de controles deslizantes ao lado adiciona um controle rápido de intensidade da pintura à barra lateral, para as ferramentas que esculpem e pintam ao mesmo tempo.

Os botões `Alfa`, `Decaimento` e `Randomizar intensidade` determinam se esses recursos afetam a pintura. Por exemplo, você pode ter a randomização ativada na ferramenta argila, sem que a cor seja randomizada.

* `Alfa` - quando desativado, a pintura ignora o alfa e cobre toda a área do pincel. Na ferramenta VDM, este botão é substituído por `Material do carimbo`, que liga ou desliga o material guardado no carimbo.
* `Decaimento` - quando desativado, a pintura fica com intensidade total até a borda do pincel.
* `Randomizar intensidade` - define se a parte de intensidade da randomização do traço afeta a pintura. A randomização de posição, rotação e escala sempre move o carimbo inteiro.

Essas opções são ignoradas por [Pintar tudo](#paint-all), mas o alfa é usado pela variante triplano.

### ![](/icons/link.webp) Material global {#global-material}
Se esta opção estiver ativada, o material selecionado será o mesmo das outras ferramentas. Ela só leva em conta os ajustes de aspereza, metalidade e cor. Desative-a para dar a esta ferramenta o seu próprio material.


## Material {#material}
![](/images/paint_material.webp) 

O primeiro ícone é uma forma de pré-visualização do material. Arrastar sobre a pré-visualização 3d do material faz ela girar.

O segundo ícone é uma pré-visualização do traço de pintura com as opções de alfa e decaimento selecionadas.

### ![](/icons/falloff.webp) Curvas {#curves}

Abre um editor de curvas para os espaços de textura dos [controles PBR](#pbr-sliders). Ele remapeia os valores da textura antes de serem pintados, sem alterar o arquivo de imagem. Um pequeno ícone de curva em um espaço de textura indica que a curva dele foi editada.

### ![](/icons/cog.webp) Opções de material {#material-options}

O botão `Material` ao lado do título guarda dois ajustes.

`Pré-visualização no visor` determina o que acontece no objeto selecionado enquanto você mexe nos controles de cor, aspereza, metalidade, opacidade e intensidade:

* `Nenhum` - Nenhuma pré-visualização aparece no modelo quando você ajusta as propriedades
* `Material` - Os valores do material são pré-visualizados no objeto quando você ajusta as propriedades.
* `Triplano` - O material é pré-visualizado como uma projeção triplano.

As caixas de seleção de cor, aspereza, metalidade e opacidade abaixo escolhem quais canais o [Seletor de material](#material-picker) substitui.

### ![](/icons/dropper.webp) Seletor de material {#material-picker}

O conta-gotas pega o material sob o cursor, de qualquer objeto da cena. Só os canais marcados nas [Opções de material](#material-options) são substituídos.

## Pré-ajustes de material {#material-presets}
Tocar na forma de pré-visualização 3d abre um menu de pré-ajustes de material, que podem ser clonados para criar os seus próprios.

![](/images/paint_presets.webp) 

A opção `Incorporar texturas` guarda dentro do pré-ajuste uma cópia das texturas usadas por esse material. Sem ela, o pré-ajuste só faz referência às texturas da pasta textures/ do Nomad. Ative-a quando quiser compartilhar um pré-ajuste com texturas sem precisar enviar as texturas separadamente.

`Incluir Alpha` também salva o alfa do pincel no pré-ajuste de material.

## Controles PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

A pintura [PBR](shading.md#pbr) usa 4 canais:
- `Cor` A cor que será pintada. O conta-gotas pode ser usado para pegar a cor de outras partes do modelo ou de imagens de referência.
- `Aspereza` Indica o quanto uma superfície é "áspera" ou "lisa". Um valor de aspereza baixo significa reflexos nítidos.
- `Metalidade` Indica simplesmente se a superfície é metálica ou não. Na maioria das vezes o valor deve ser 0% ou 100%; valores intermediários devem ser exceção.
- `Opacidade` O quanto dá para ver através do material. A rigor, não faz parte da especificação PBR, mas é útil em muitas situações. 1 é totalmente opaco, 0 é transparente. Opacidade e refração são coisas diferentes: no Nomad, a refração é feita pelo material de refração.

Se você selecionar um pré-ajuste de material, 3 canais são pintados ao mesmo tempo (a opacidade costuma ficar de fora de propósito). Assim, em vez de pintar apenas 'vermelho', você pode pintar 'um metal vermelho áspero' ou 'um plástico branco liso'.

O quadrado é um espaço de textura: clique nele para usar uma textura nessa propriedade em vez de um valor fixo. Uma textura de cor tinge a cor, enquanto uma textura de aspereza, metalidade ou opacidade substitui o valor do controle (o rótulo dele aparece riscado para indicar isso). Para a textura de opacidade, `Usar Alpha como valor` lê o canal alfa da textura em vez do seu valor em tons de cinza.

Na ferramenta VDM, quando o carimbo traz o seu próprio material, um espaço extra aparece ao lado do espaço de textura para mostrá-lo. Toque nele para usar ou ignorar esse canal do carimbo.

O ícone de pincel ao lado dos controles preenche o objeto inteiro com essa propriedade.

A caixa de seleção ativa ou desativa cada propriedade, então você pode, por exemplo, pintar só a cor, ou só a aspereza e a opacidade.

Aqui estão alguns exemplos de diferentes valores de aspereza e metalidade:

|                | Metalidade 0%                     | Metalidade 100%              |
| :------------: | :-------------------------------: | :--------------------------: |
| Aspereza 0%    | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Aspereza 50%   | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Aspereza 100%  | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
A aspereza e a metalidade exigem o modo de sombreamento [Iluminado (PBR)](shading.md#pbr). Nos modos [MatCap](shading.md#matcap) ou [Sem iluminação](shading.md#unlit) elas são ignoradas, e o menu mostra um aviso.
:::

::: tip
Ao usar texturas na pintura PBR, muitas vezes vale a pena trocar para uma ferramenta como `Carimbo`, ou usar no menu de traçado um modo diferente de ponto, que pode borrar a textura.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Considere ativar o `Sombreamento suave` [globalmente](settings.md#smooth-shading) ou [por objeto](material.md#smooth-shading) se estiver pintando uma superfície metálica em um objeto com poucos polígonos.
:::

## ![](/icons/paint.webp) Pintar tudo {#paint-all}

![](/images/paint_paint_all.webp)

Aplica o material atual aos objetos selecionados, no modo padrão com `Pintar tudo`, ou como uma projeção triplano com `Pintar tudo + Triplano`. A variante triplano não está disponível em primitivas que ainda não foram validadas.

As caixas de seleção ao lado dos controles de cor/metalidade/aspereza/opacidade são respeitadas: as propriedades desativadas não serão preenchidas.

Os botões extras controlam como o preenchimento pode ser afetado. A maioria mostra uma porcentagem, e eles ficam acinzentados quando não teriam efeito:

| Ícone                       | Descrição                                     |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | As áreas mascaradas não serão afetadas.       |
| ![](/icons/tool_hide.webp) | As áreas ocultas não serão afetadas.          |
| ![](/icons/opacity.webp)   | Usa o fator de pintura da ferramenta acima.   |
| ![](/icons/layer.webp)     | As áreas não pintadas de uma camada não serão afetadas. |
| ![](/icons/triplanar.webp) | `Vértice`: a variante triplano também desloca a superfície com o alfa, pela intensidade da ferramenta mostrada. |
| ![](/icons/cog.webp)       | Abre os ajustes do triplano                   |

### ![](/icons/cog.webp) Ajustes do triplano {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Assim como nos [ajustes de triplano do menu Material](material.md#triplanar), você pode controlar a mistura das projeções, a repetição e os deslocamentos.

Use a caixa de pré-visualização no topo deste menu para manter uma pré-visualização enquanto ajusta os valores.

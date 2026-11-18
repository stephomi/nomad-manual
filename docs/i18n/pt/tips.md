# ![](/icons/manual.webp) Dicas {#tips}

[[toc]]

## Como começar um modelo {#how-to-start-a-model}

Quem está começando na escultura 3d costuma perguntar qual é o melhor jeito de começar um modelo. Não existe um jeito melhor: cada pessoa tem as suas preferências. Aqui estão algumas das abordagens mais comuns.

### Esculpir em uma esfera, com multirresolução {#sculpt-on-sphere-multires}

O modelo padrão quando o Nomad abre é o jeito mais comum. Use as ferramentas de mover, argila e vinco para empurrar e puxar a esfera até chegar à forma, use os níveis de subdivisão mais baixos quando quiser fazer grandes mudanças rapidamente e os níveis mais altos para os detalhes.

Um problema comum é que muitas vezes faltam polígonos onde você precisa deles, enquanto sobram em outros lugares. Por exemplo, se você transformar a esfera padrão em um corpo inteiro, provavelmente não vai ter detalhe suficiente para os dedos, enquanto vai desperdiçar muitos polígonos na parte de trás da cabeça. Para formas quase esféricas, como uma cabeça, isso pode funcionar bem.

### TopoDin {#dyntopo}

Ativar a TopoDin adiciona e remove polígonos de forma adaptativa enquanto você esculpe. Esses polígonos são triângulos, e quem está começando muitas vezes não gosta da distribuição bagunçada em comparação com o visual limpo da multirresolução. Vale a pena insistir! Se você ligar o sombreamento suave, desligar a armação e parar de se preocupar com a distribuição, este modo dá uma sensação muito parecida com argila. Não esqueça que, com um pincel grande ou um pincel de suavizar, este modo também pode remover polígonos, então a ferramenta continua sempre rápida e responsiva. Quando a primeira versão da escultura estiver pronta, você pode cloná-la, passá-la pelo Quad Remesher para ter uma boa distribuição e reprojetar os detalhes originais em um nível alto de subdivisão.

### Remalhar voxels {#voxel-remesh}

Remalhar voxels aplica uma topologia quase toda em quads à sua escultura. A operação é rápida em resoluções baixas e serve para trocar rapidamente polígonos esticados ou densos demais por uma distribuição uniforme. É um ótimo jeito de começar um corpo inteiro a partir de uma esfera: digamos que você comece por uma cabeça; estique um pescoço e remalhe com voxels. Estique um corpo, remalhe com voxels, depois os braços, remalhe com voxels, e assim por diante, até ter as formas básicas.

### Usar vários objetos {#use-multiple-objects}

Muitos guias de anatomia representam o corpo com esferas, cilindros e cubos simples. Você também pode esculpir assim no Nomad. A vantagem é poder aparentar os objetos na hierarquia da cena, para que, por exemplo, a cabeça acompanhe quando você gira o pescoço. Poder usar a ferramenta gizmo para translações, rotações e escalas precisas também é muito útil, e você pode definir o pivô de cada forma para que ela se mova exatamente como você espera. Quando os blocos básicos estiverem no lugar certo, selecione todos e use o remalhar voxels ou a booleana para juntá-los em uma única superfície e esculpir os detalhes.

Uma dica prática para trabalhar assim é começar com uma esfera, esticá-la em forma de salsicha, apertar pivô, tocar em "inferior" e apertar pivô de novo. Agora você tem uma parte do corpo que pode ser clonada, deslocada ao longo do comprimento da primeira esfera, clonada, girada, clonada, deslizada, clonada etc., para montar um corpo rapidamente.

### Tubos {#tubes}

A ferramenta tubo é um ótimo jeito de começar uma escultura. Caudas de répteis, braços, pernas, dedos, sobrancelhas: tudo isso pode ser esboçado rapidamente com a ferramenta tubo e editado com facilidade depois. Ela também permite alterar o perfil do corte transversal, o que deixa mudar a forma rapidamente. Você pode validar a forma para começar a esculpir nela e remalhá-la com voxels junto com outros objetos para obter a malha de um corpo inteiro.

### Usar outros aplicativos {#use-other-apps}

Algumas pessoas preferem começar um modelo em outros aplicativos, e tudo bem. Ferramentas como o Blender ou o Valence permitem começar os modelos com técnicas low poly, e depois eles podem ser importados no Nomad para esculpir.

### Usar os pré‑ajustes incluídos {#use-the-built-in-presets}

No menu [Arquivo](files.md), toque em `Pré‑ajuste…` à esquerda da seção do projeto. Lá você encontra vários pré‑ajustes de cabeças e corpos da Blender Foundation. Selecione um de que você goste, toque nele de novo e adicione-o à cena.

### Usar modelos da internet {#use-online-models}

Há muitos modelos gratuitos na internet, por exemplo no Poly Haven, no Sketchfab e no TurboSquid. Em geral, esses modelos podem ser importados no Nomad e esculpidos diretamente ou usados como referência.

### Sem regras! {#no-rules}

No fim das contas, você pode usar qualquer combinação dessas técnicas, ou nenhuma! O Nomad é muito flexível nesse ponto: usuários avançados podem começar com tubos, passar para a TopoDin, juntar com um pé baixado da internet, depois passar tudo pelo Quad Remesher e usar a multirresolução para os detalhes finais. O que funcionar para você.

## Grupos de faces {#facegroups}

A ferramenta de grupo de faces pode ser usada para muitas coisas, como explica este vídeo do YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Este é um resumo em texto dos recursos mostrados no vídeo.

### Por que grupos de faces? {#why-facegroups}

Os grupos de faces permitem organizar e selecionar faces ("faces" e "polígonos" são usados como sinônimos neste manual). Fica mais fácil explicar comparando com as outras ferramentas de seleção e organização do Nomad. O Nomad permite criar objetos, dar nomes a eles e aparentá-los, então é fácil montar uma estrutura de objetos para definir um cômodo com piso, paredes, cadeira, mesa e assim por diante.

Para um personagem, você pode fazer um primeiro esboço com objetos separados para a cabeça, os braços e as pernas, mas, depois de juntar todas as peças em uma única malha, essa estrutura se perde. Você pode trabalhar em partes do personagem com máscaras, mas fica cansativo pintar uma máscara para as mãos, depois para o nariz, depois para as mãos de novo.

É aí que os grupos de faces são úteis. Eles permitem marcar as faces dos polígonos com uma cor e depois selecionar e manipular os polígonos que têm a mesma cor. Note que a cor do grupo de faces e a cor dos vértices são coisas diferentes.

A comparação mais próxima seria pintar cores em um mapa e depois poder selecionar países ou regiões pela cor.

Na cabeça de um personagem, você pode pintar zonas para marcar as órbitas dos olhos, o nariz, os lábios, o queixo e as orelhas, e depois selecioná-las com facilidade. Em esculturas de superfícies rígidas e mecânicas, é útil para definir painéis e seções.

### Criar e editar grupos de faces {#creating-and-editing-facegroups}

Os grupos de faces podem ser aplicados com um pincel, em que cada novo traçado cria um novo grupo de faces, ou podem selecionar o grupo de faces sob o cursor e estendê-lo. Também podem ser criados com formas.

* Ponto, modo padrão - um único arrasto define uma nova cor de grupo de faces e a atribui às faces por onde você passa. Cada novo arrasto define um novo grupo de faces. Um toque preenche uma área inteira com um novo grupo de faces.
* Ponto, modo `Escolher` - quando o botão `Escolher` da barra de ferramentas à esquerda está ativo, o Nomad seleciona o grupo de faces sob o cursor e o aplica durante o resto do arrasto. É útil para refinar os grupos de faces sem precisar selecioná-los manualmente.

### Máscara {#masking}

Com a ferramenta de máscara ativa e o botão de grupo de faces ativo na barra de ferramentas dela, tocar em um grupo de faces aplica a máscara nele.


### Ocultar {#hiding}

Com a ferramenta de ocultar ativa e o botão de grupo de faces ativo na barra de ferramentas dela, tocar em um grupo de faces o oculta.

### Organizar {#organizing}

Como dito antes, os grupos de faces podem organizar a malha sem que você precise criar objetos separados. Talvez você não queira dividir uma cabeça em objetos separados para o nariz, o queixo e as orelhas, mas é muito útil tê-los definidos por grupos de faces.

### Regiões de UV {#uv-regions}

A ferramenta UV Atlas tenta definir as costuras automaticamente, mas às vezes as coloca onde você não quer. Se o objeto tiver grupos de faces e a opção de grupo de faces estiver ativa nas opções do UV Atlas, ela usa as bordas dos grupos de faces como costuras de UV.

### Quad Remesher {#quad-remesher}

O plugin Quad Remesher geralmente distribui bem as arestas do modelo, mas você pode usar grupos de faces para ajudar a guiá-lo quando a opção de grupo de faces estiver ativada. Isso facilita definir um fluxo de arestas limpo em volta dos olhos, de uma arcada das sobrancelhas, dos lábios ou de uma dobra da bochecha, por exemplo.

### Filtrar com outras ferramentas {#filter-with-other-tools}

Muitas ferramentas têm opções para levar em conta os grupos de faces, seja no próprio menu da ferramenta, seja no menu Traçado -> Filtro. Por exemplo, a ferramenta de suavizar com força acima de 100% pode apagar os detalhes de forma agressiva dentro de um grupo de faces, mantendo a borda do grupo de faces relativamente intacta.

### Relaxar e suavizar as bordas dos grupos de faces {#relax-and-smooth-facegroup-borders}

A opção `Relaxar` da ferramenta de grupo de faces faz um ótimo trabalho ao suavizar as bordas dos grupos de faces mantendo o resto intacto. É um ótimo jeito de definir bordas suaves de grupos de faces antes de usar o Quad Remesher.

## Limitações em tablets e celulares {#limitations-on-tabletmobile}

Os tablets e celulares atuais são muito potentes, mas têm diferenças importantes em relação aos computadores de mesa e notebooks:

### Sem resfriamento ativo {#no-active-cooling}

Os computadores têm ventoinhas e/ou grandes dissipadores para se manterem frios, e são feitos para funcionar em temperaturas altas. Os aparelhos móveis geralmente são feitos primeiro para serem finos, não para ajudar a resfriar os componentes internos. Se o Nomad for levado aos ajustes de qualidade mais altos (modo de iluminação PBR, materiais complexos, muitos objetos, muitas opções de pós-processamento ativadas), o aparelho pode superaquecer e a bateria pode acabar muito rápido.

Uma abordagem melhor é usar um modo de iluminação com matcap e uma `Resolução da renderização` mais baixa (no alto do menu Pós-processamento). Essas escolhas mantêm o aparelho frio e permitem esculpir por mais tempo.

### Memória limitada {#limited-memory}

O Nomad consegue resultados à altura da maioria dos aplicativos de escultura para computador, mas não consegue mudar as leis da física! A maioria dos computadores tem o dobro da memória dos aparelhos móveis, e as estações de trabalho feitas para animação 3d muitas vezes têm 4 ou 8 vezes mais. Por isso, é bom ficar de olho em quantos polígonos você está usando e fazer alguns testes no seu aparelho para ver quando ele começa a travar. Quase todos os aparelhos que rodam o Nomad aguentam 1 milhão de polígonos com bastante facilidade. Um iPad Pro M2 aguenta 8 milhões tranquilamente, e há quem tenha testado bem acima disso nos iPads mais recentes.

Dito isso, só as esculturas mais detalhadas precisam de mais de 4 milhões de polígonos; se você está fazendo objetos relativamente simples e se pega passando com frequência de 500.000, 1 milhão, 4 milhões, está usando polígonos demais! Confira se o `Sombreamento suave` está ativado nos [Ajustes](settings.md).

### O sistema é menos tolerante com aplicativos pesados {#os-is-less-forgiving-with-intensive-apps}

A Apple e o Android esperam que os aplicativos salvem e abram arquivos pequenos muito rapidamente. Eles também esperam que os aplicativos consigam alternar de tarefa muito rápido. Mais uma vez, o Nomad usa alguns truques espertos para manter os arquivos relativamente pequenos e salvá-los muito rápido, mas, se o sistema do aparelho achar que o Nomad está demorando demais, ele simplesmente o encerra antes que a tarefa termine. Esse é outro motivo para manter os arquivos pequenos; é possível trabalhar com esculturas de 37 milhões de polígonos, como um usuário contou no Discord, mas não é recomendado!

## Trabalhar em telas pequenas {#working-on-small-screens}

O Nomad foi feito para tablets, mas também funciona bem em celulares. Esculpir em uma tela pequena, como a de um celular, fica mais fácil com alguns ajustes na interface e no jeito de trabalhar:

* Um toque com 4 dedos esconde ou mostra toda a interface, deixando mais espaço para esculpir.
* Arrastar 3 dedos para cima e para baixo muda o raio do pincel.
* A escala da interface pode ser reduzida para caber mais botões, se você enxerga bem, ou aumentada, se não enxerga tão bem!
* Os menus mais largos às vezes atrapalham a visão da escultura; você pode deixá-los transparentes e sem desfoque para ver a escultura por baixo do menu.
* Se você esculpe com o dedo, use a opção [`Deslocamento do traçado`](stroke.md#stroke-offset) para afastar um pouco o centro do pincel do seu dedo.
* Essas e muitas outras opções estão no [menu Interface](./interface.md).


## Deformador de inflar ou de pico {#inflate-or-peak-deformer}

Muitos aplicativos 3d têm um deformador de inflar, que empurra todos os vértices ao longo da normal deles em uma quantidade ajustável. O Nomad ainda não tem deformadores, mas é possível imitar esse comportamento com o pincel de inflar:

* Selecione o pincel de inflar.
* No [menu Traçado](./stroke.md#stroke), mude o tipo de traçado para `Bloqueio + raio`.
* Deixe o raio do pincel maior que a escultura, afastando a câmera da escultura se precisar.
* Toque e arraste um traçado na superfície do objeto; quando o raio é maior que o objeto, a forma inteira é inflada por igual, em uma quantidade fixa.
* Ajuste a intensidade do pincel para controlar o quanto inflar.
* Use máscaras se precisar, para proteger certas áreas ou reduzir o efeito de inflar nelas.

## Remover os caroços ou "espinhas" de um remalhar voxels {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

O remalhar voxels é ótimo para criar polígonos uniformes, mas às vezes gera uma topologia que forma pequenos caroços ou espinhas ao suavizar. Por exemplo:

* Use o pincel de vincar na esfera padrão e faça um redemoinho.
* Remalhe com voxels com `Construir multirresolução` em 3.
* Suavize com intensidade alta.
* Aparecem artefatos (mais fáceis de ver com um material matcap de alto contraste):

![](/videos/tip_pimples_before.mp4)

Para corrigir esculpindo, experimente a opção `Suavização estável` nos ajustes de suavização. Ela lida bem com a topologia irregular do remalhar voxels e dá resultados limpos.

![](/videos/tip_pimples_stable_smooth.mp4)

Para corrigir a própria topologia, use uma nova primitiva, as ferramentas de remalha em quads ou um modelador 3d externo, e projete os detalhes da malha original na nova por `Topologia -> Selar -> Reprojetar → Vértice`.

![](/videos/tip_pimples_reproject.mp4)

## Iluminação de luz do dia {#daylight-lighting}

A renderização PBR padrão é, como o nome diz, baseada em física, e, assim como uma foto digital sem tratamento, pode parecer um pouco lavada e sem graça. As luzes e o pós-processamento do Nomad podem deixar as renderizações mais vibrantes.

Aqui está uma renderização padrão. Vamos ver se dá para melhorá-la:
![](/images/tips_lighting_default.webp)

Ativar o pós-processamento e o mapeamento de tons acrescenta brilho e contraste:

![](/images/tips_lighting_tonemap.webp)

Agora as luzes: a luz de ambiente padrão é boa para esculpir, mas pode ser melhorada para uma renderização final. Uma forma de pensar nisso é separar a luz direta (o sol, por exemplo) da luz de ambiente (a luz que vem do azul do céu e do chão, por exemplo). Diminuindo a luz de ambiente e girando-a, começamos a captar como seria a iluminação se o modelo estivesse na sombra:

![](/images/tips_lighting_env.webp)

Dá para adicionar uma luz direta e aumentar a intensidade dela para simular a luz forte do sol. Equilibrar essa luz com a luz de ambiente dá um resultado agradável:

![](/images/tips_lighting_sunlight.webp)

Os personagens ficam melhores com o material trocado para subsuperfície e uma luz spot atrás deles, apontada para as orelhas, para fazê-las brilhar:

![](/images/tips_lighting_sss.webp)

Depois, experimente o resto dos ajustes de pós-processamento! A Iluminação Global e a Oclusão Ambiente ajudam a ter uma iluminação mais realista. A Curvatura e o Aumentar nitidez ajudam a realçar os detalhes da escultura. A Aberração Cromática, a Profundidade de Campo, a Granulação, a Incandescência e a Vinheta ajudam a simular efeitos de câmera. Note que, conforme você ativa os recursos, é preciso ajustar a iluminação e os outros valores de pós-processamento para compensar.

Aqui está a renderização com um conjunto completo de ajustes de pós-processamento:
![](/images/tips_lighting_final.webp)

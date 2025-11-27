# ![](/icons/manual.webp) Dicas

[[toc]]

## Como começar um modelo

Iniciantes em escultura 3D frequentemente perguntam qual é a melhor maneira de começar um modelo. Não existe uma melhor maneira, pessoas diferentes têm preferências diferentes. Aqui estão algumas das abordagens mais comuns.

### Esculpir em esfera, multires

O modelo padrão quando o Nomad é iniciado é a forma mais comum. Use as ferramentas mover, clay e crease para empurrar e puxar a esfera até a forma desejada, use os níveis de subdivisão mais baixos quando quiser fazer grandes mudanças rapidamente, use níveis de subdivisão mais altos para trabalho de detalhe.

Um problema comum é que você frequentemente ficará sem polígonos onde precisa deles, enquanto terá polígonos demais em outros lugares. Por exemplo, se você empurrar a esfera padrão até virar um corpo inteiro, é provável que não tenha detalhes suficientes para fazer os dedos, enquanto terá muitos polígonos desperdiçados na parte de trás da cabeça. Para formas principalmente esféricas como uma cabeça, porém, isso pode ser aceitável.

### Dyntopo

Ativar o Dyntopo irá adicionar e remover polígonos de forma adaptativa enquanto você esculpe. Esses polígonos serão triângulos, e iniciantes muitas vezes não gostam do layout bagunçado em comparação com o visual limpo do multires. Vale a pena insistir! Se você ativar o sombreamento suave, desativar o wireframe e parar de se preocupar com o layout, esse modo pode dar uma sensação muito parecida com argila. Não se esqueça de que, se você usar um pincel grande ou um pincel de suavização, esse modo também pode remover polígonos, então a ferramenta sempre parece rápida e responsiva. Quando você tiver um primeiro passe da escultura finalizado, pode cloná-la e rodar o quad remesher para obter um bom layout, e reprojetar os detalhes originais em um nível de subdivisão alto.

### Voxel remesh

O voxel remesh aplicará uma topologia baseada principalmente em quads na sua escultura. Essa operação é rápida em resoluções mais baixas e pode ser usada para substituir rapidamente polígonos esticados ou excessivamente densos por um layout espaçado de forma uniforme. Isso pode ser uma ótima maneira de começar um corpo inteiro a partir de uma esfera; digamos que você comece com uma cabeça, pode esticar um pescoço, fazer voxel remesh. Esticar um corpo, voxel remesh, braços, voxel remesh, e assim por diante, até ter as formas básicas.

### Usar múltiplos objetos

Muitos guias de anatomia representam um corpo com esferas, cilindros e cubos simples. Você também pode esculpir dessa forma no Nomad. Isso tem a vantagem de permitir que você faça parentesco entre objetos na hierarquia da cena, para que você possa rotacionar o pescoço e a cabeça o siga, por exemplo. Poder usar a ferramenta gizmo para translações/rotações/escalas precisas também é muito útil, e você também pode definir pivôs por forma para que se movam exatamente como espera. Quando os blocos básicos estiverem no lugar certo, você pode selecioná-los todos e fazer voxel remesh ou boolean neles para obter uma única superfície para escultura mais detalhada.

Uma dica útil para esse modo de trabalho é começar com uma esfera, escalá-la em uma salsicha alongada, pressionar pivot, clicar em “bottom”, pressionar pivot novamente. Agora você tem uma parte do corpo que pode ser clonada, transladada ao longo do comprimento da primeira esfera, clonada, rotacionada, clonada, deslizada, clonada etc. para montar um corpo rapidamente.

### Tubes

A ferramenta tube é uma ótima maneira de começar uma escultura. Caudas de répteis, braços, pernas, dedos, sobrancelhas, tudo isso pode ser rapidamente esboçado com a ferramenta tube e facilmente editado depois. Ela também permite modificar o perfil da seção transversal, possibilitando mudanças rápidas de forma. Você pode validar a forma para começar a esculpir nela e fazer voxel remesh junto com outros objetos para obter uma malha de corpo inteiro.

### Usar outros apps

Algumas pessoas preferem começar um modelo em outros apps, o que também é válido. Ferramentas como Blender ou Valence permitem que modelos sejam iniciados usando técnicas de low poly, podendo depois ser importados para o Nomad para escultura.

### Usar os presets embutidos

No menu de projeto clique em `Preset...` no canto superior direito. Aqui você encontrará vários presets de formas de cabeça e corpo da Blender Foundation. Selecione um de que goste, toque nele novamente e adicione à sua cena. 

### Usar modelos online

Há muitos modelos gratuitos disponíveis online, por exemplo Polyhaven, Sketchfab, Turbosquid. Normalmente esses modelos podem ser importados para o Nomad e ou esculpidos diretamente, ou usados como referência.

### Sem regras!

No fim das contas você pode usar qualquer combinação dessas técnicas, ou nenhuma delas! O Nomad é muito flexível nesse aspecto; usuários avançados podem começar com tubes, depois dyntopo, depois combinar com um pé baixado da internet, depois fazer quad remesh em tudo, depois multires para o detalhe final. O que funcionar para você.

## Facegroups

A ferramenta facegroup pode ser usada para muitas coisas, como explicado neste vídeo do YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Este é um resumo em texto dos recursos abordados nesse vídeo.

### Por que facegroups?

Facegroups permitem organizar e selecionar faces (“faces” e “polígonos” são usados de forma intercambiável neste manual). Isso é mais fácil de explicar em comparação com as outras ferramentas de seleção e organização do Nomad. O Nomad permite criar objetos, nomeá-los, fazer parentesco entre eles; é fácil criar uma estrutura de objetos para definir um cômodo composto de piso, paredes, cadeira, mesa e assim por diante.

Para um personagem você pode fazer um block-out inicial usando objetos separados para cabeça, braço, perna, mas uma vez que você una todas as peças em uma única malha, essa estrutura é perdida. Você pode trabalhar em subseções de um personagem com máscaras, mas pode ficar cansativo ficar pintando uma máscara para as mãos, depois o nariz, depois as mãos de novo.

É aqui que os facegroups são úteis. Eles permitem marcar faces de polígonos com uma cor e então poder selecionar e manipular polígonos que tenham a mesma cor. Note que cor de facegroup e cor de vértice são coisas diferentes.

A analogia mais próxima seria pintar cores em um mapa e depois poder selecionar países ou regiões com base na cor.

Para cabeças de personagem você poderia pintar zonas para marcar as cavidades dos olhos, nariz, lábios, queixo, orelhas, e então selecionar facilmente essas zonas depois. Para escultura hard surface e mecânica pode ser útil definir painéis e seções.

### Criando e editando facegroups

Facegroups podem ser aplicados com um pincel, onde cada novo traço cria um novo facegroup, ou podem selecionar o facegroup sob o cursor e estendê-lo. Eles também podem ser criados usando formas.

* Dot, auto-pick ativado – um único arrasto definirá uma nova cor de facegroup e a atribuirá às faces sobre as quais você arrastar. Cada novo arrasto definirá um novo facegroup. Um toque fará um preenchimento total com um novo facegroup.
* Dot, auto-pick desativado – quando o botão auto-pick está no modo “sub”, o Nomad selecionará o facegroup sob o cursor e o aplicará durante o restante do arrasto. Isso é útil para refinar facegroups sem precisar selecioná-los manualmente.

### Mascaramento

Quando a ferramenta mask está ativa e o botão facegroup está ativo na barra de ferramentas dela, tocar em um facegroup irá mascará-lo.

### Ocultando

Quando a ferramenta hide está ativa e o botão facegroup está ativo na barra de ferramentas dela, tocar em um facegroup irá ocultá-lo.

### Organização

Como mencionado antes, facegroups podem ser usados para organizar sua malha sem exigir que você crie objetos separados. Você pode não querer dividir uma cabeça em objetos separados para nariz, queixo, orelhas, mas é muito útil tê-los definidos via facegroups.

### Regiões de UV

A ferramenta UV Atlas tentará definir seams automaticamente, mas às vezes colocará seams onde você não as quer. Se existirem facegroups em um objeto e a opção facegroup estiver ativa nas opções do UV Atlas, ela usará as bordas dos facegroups como seams de UV.

### Quad remesher

O plugin quad remesher normalmente fará o fluxo de arestas ficar bom no seu modelo, mas você pode usar facegroups para ajudar a guiá-lo quando a opção facegroup estiver ativada. Isso pode facilitar a definição de um fluxo de arestas limpo ao redor dos olhos, uma crista de sobrancelha, lábios, dobra da bochecha, por exemplo.

### Filtrar com outras ferramentas

Muitas ferramentas terão opções para serem sensíveis a facegroups, seja em seu menu principal de ferramenta, seja via menu stroke -> filtering. Por exemplo, a ferramenta smooth em intensidades acima de 100% pode suavizar agressivamente detalhes dentro de um facegroup, mas manter a borda do facegroup relativamente intacta.

### Relaxar e suavizar bordas de facegroup

A opção relax dentro da ferramenta facegroup faz um excelente trabalho de suavizar bordas de facegroup mantendo outros recursos intactos. Isso pode ser uma ótima maneira de definir regiões de borda de facegroup suaves antes de fazer quad remesh.

## Limitações em tablet/celular

Tablets e celulares atuais são muito poderosos, mas têm diferenças importantes em relação a computadores desktop e laptops:

### Sem resfriamento ativo

Computadores têm ventoinhas e/ou grandes dissipadores de calor para mantê-los frios e são projetados para operar em altas temperaturas. Hardware móvel geralmente é projetado priorizando a espessura reduzida, não para ajudar a manter o interior frio. Se o Nomad for levado às suas configurações de qualidade mais altas (modo de iluminação PBR, materiais complexos, muitos objetos, muitas opções de pós-processamento ativadas), isso pode tanto superaquecer o dispositivo quanto drenar a bateria muito rapidamente. 

Uma abordagem melhor é usar um modo de iluminação matcap e usar um render multiplier mais baixo (topo do menu de pós-processo). Essas escolhas manterão o dispositivo frio e permitirão que você esculpa por mais tempo.

### Memória limitada

O Nomad pode alcançar resultados equivalentes à maioria dos apps de escultura desktop, mas não pode dobrar as leis da física! A maioria dos computadores desktop tem o dobro da memória dos dispositivos móveis; workstations construídas para animação 3D frequentemente têm 4x ou 8x a memória. Por causa disso, é bom estar atento a quantos polígonos você está usando, fazer alguns testes no seu dispositivo para ver quando ele começa a ficar lento. Quase todos os dispositivos que conseguem rodar o Nomad lidam com 1 milhão de polígonos com bastante facilidade. Um iPad Pro M2 consegue lidar confortavelmente com 8 milhões; pessoas testaram nos iPads mais recentes indo bem acima disso.

Dito isso, só as esculturas mais detalhadas precisam de mais de 4 milhões de polígonos; se você estiver fazendo objetos relativamente simples e se pegar frequentemente passando de 500.000, 1 milhão, 4 milhões, você está usando polígonos demais! Certifique-se de ter o modo de sombreamento suave ativado nas opções.

### O sistema operacional é menos tolerante com apps intensivos

Apple e Android esperam que apps salvem e carreguem arquivos pequenos muito rapidamente. Eles também assumem que apps podem alternar de tarefa muito rapidamente. Novamente, o Nomad faz alguns truques inteligentes para manter os arquivos relativamente pequenos e salvá-los muito rapidamente, mas se o sistema operacional móvel decidir que o Nomad está demorando demais, simplesmente o encerrará antes de ele terminar sua tarefa. Esse é outro motivo para manter os arquivos menores; é possível trabalhar com esculturas de 37 milhões de polígonos, como um usuário relatou no Discord, mas não é recomendado!

## Trabalhando em telas pequenas

O Nomad é projetado para funcionar em tablets, mas também funciona bem em celulares. Esculpir em uma tela pequena como a de um celular pode ser facilitado com alguns ajustes de interface e fluxo de trabalho:

* Um toque com 4 dedos alternará toda a interface, dando mais espaço para esculpir.
* Um arrasto com 3 dedos para cima e para baixo mudará o raio do pincel.
* A escala da interface pode ser reduzida para caber mais botões se você tiver boa visão, ou aumentada se tiver visão ruim.
* Os menus mais largos às vezes podem atrapalhar a escultura; você pode torná-los transparentes e sem desfoque para permitir ver a escultura sob o menu.
* Se estiver esculpindo com o dedo, use a opção offset para mover o centro do pincel um pouco para longe do seu dedo.
* Essas e muitas outras opções podem ser encontradas no [menu Interface](./interface.md). 

## Deformador de inflate ou peak

Muitos apps 3D possuem um deformador de inflate, que empurra todos os vértices ao longo de suas normais por uma quantidade controlável. Embora o Nomad atualmente não tenha deformadores, é possível emular esse comportamento com o pincel inflate:

* Selecione o pincel inflate
* No [menu Stroke](./stroke.md#stroke) mude o método de stroke para `Lock + Radius'
* Deixe o raio do pincel maior que sua escultura, afaste a câmera da escultura se necessário.
* Clique e arraste um stroke na superfície do seu objeto; quando o raio for maior que o objeto, toda a forma será inflada de maneira uniforme por uma quantidade fixa.
* Ajuste a intensidade do pincel para controlar a quantidade de inflação.
* Use mascaramento se necessário para proteger ou reduzir o efeito do inflate em certas áreas.

## Remover caroços ou “espinhas” de uma operação de voxel remesh

O voxel remesh é ótimo para criar polígonos espaçados de forma uniforme, mas às vezes cria uma topologia que causará pequenos caroços ou espinhas quando suavizada. Por exemplo:

* Use o pincel crease na esfera padrão e faça um redemoinho
* Faça voxel remesh com “build multiresolution at 3”
* Suavize com alta intensidade
* artefatos aparecem (mais fácil de ver com um material matcap de alto contraste):

![](/videos/tip_pimples_before.mp4)

Para corrigir via escultura, tente a opção `Stable smoothing` nas configurações de smooth. Ela consegue lidar com o layout de topologia irregular do voxel remesh e obter resultados limpos.

![](/videos/tip_pimples_stable_smooth.mp4)

Para corrigir a própria topologia, use uma nova primitiva, ou as ferramentas de quad remesh, ou um modelador 3D externo, e projete o detalhe da malha original na nova via `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Iluminação de luz do dia

O render PBR padrão é, como o nome sugere, fisicamente baseado, o que, como uma foto digital sem tratamento, pode parecer um pouco lavada e sem contraste. As luzes e o pós-processamento do Nomad podem ser usados para deixar os renders mais vibrantes.

Aqui está um render padrão, vamos ver se conseguimos deixá-lo melhor:
![](/images/tips_lighting_default.webp)

Ativar pós-processamento e tonemapping pode adicionar brilho e contraste:

![](/images/tips_lighting_tonemap.webp)

Para focar nas luzes, a luz de ambiente padrão é boa para esculpir, mas pode ser melhorada para um render final. Uma forma de pensar nisso é separar luz direta (por exemplo, o sol) da luz de ambiente (por exemplo, luz do azul do céu, do chão). Ao reduzir a luz de ambiente e rotacioná-la, começamos a capturar como a iluminação deveria parecer se o sujeito estivesse em uma área sombreada:

![](/images/tips_lighting_env.webp)

Uma luz direta pode ser adicionada e sua intensidade aumentada para simular luz solar forte. Equilibrar isso com a luz de ambiente produzirá um resultado agradável:

![](/images/tips_lighting_sunlight.webp)

Personagens podem se beneficiar ao trocar seu material para subsurface e posicionar um spotlight atrás do personagem apontando para as orelhas para fazê-las brilhar:

![](/images/tips_lighting_sss.webp)

Depois, experimente o restante das configurações de pós-processo! Global Illumination e Ambient Occlusion ajudam com iluminação mais realista. Curvature e Sharpen podem ajudar a destacar mais detalhes na escultura. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette ajudam a simular efeitos de câmera. Note que, à medida que recursos são ativados, a iluminação e outros valores de pós-processamento precisam ser ajustados para compensar.

Aqui está o render com um conjunto completo de ajustes de pós-processamento:
![](/images/tips_lighting_final.webp)

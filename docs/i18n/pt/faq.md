# ![](/icons/faq.webp) Perguntas frequentes {#faq}

[[toc]]

## Plataforma {#platform}
### Onde ficam os meus projetos no aparelho? {#locate}
Os projetos ficam na pasta `projects`, dentro da pasta principal do Nomad.

No iOS, você acessa a pasta do Nomad pelo app Arquivos do iOS.

No Android, a pasta do Nomad fica em `Android/data/com.stephaneginier.nomad/files/`.  
Nas versões recentes do Android (10/11), você não tem mais acesso à pasta `Android/data`.
Você pode acessá-la por um aplicativo separado, por exemplo [este aqui](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Tem como testar a versão beta? {#beta}
Para Windows e MacOS, pode haver uma beta disponível na [página inicial](https://nomadsculpt.com).
<br>
Para iOS, há um TestFlight privado: entre no [Discord](https://discord.com/invite/8h7BwpRz29), no canal #beta-ios.
<br>
A [demo na web](https://nomadsculpt.com/demo) geralmente está atualizada com os recursos mais recentes.

### Por que existe um teste grátis no Android, mas não no iOS? {#android-trial}
Porque os aparelhos Android antigos são péssimos (e alguns recentes também...), e eu não queria que as pessoas comprassem o aplicativo e dessem de cara com uma tela preta.
Mas o principal motivo é que eu sentia que aplicativos pagos não são bem a norma no Android.

### Qual é o melhor tablet para rodar o Nomad? {#best-tablet}

Resumindo: um iPad.

A resposta um pouco mais longa é

> "O iPad mais novo _que você puder pagar_, a não ser que você odeie mesmo a Apple; nesse caso, o tablet Samsung mais novo que você puder pagar. Qualquer outro, teste antes."

As pessoas sempre querem mais detalhes, então aqui vai um resumo.

O Nomad roda melhor nos iPads mais novos:

* iPads e iPhones têm acesso ao plugin [Quad Remesher](tools#quad-remesher) da [Exoside](https://exoside.com/)
* os iPads recentes com a caneta mais nova aceitam o [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0): você pode girar a caneta no próprio eixo em certas ferramentas do Nomad.
* o desempenho dos chips mais recentes da série M é muito alto.

O iPad mais novo e mais caro disponível consegue renderizar imagens finais muito rápido e permite esculpir muitos detalhes.

Mas a queda de desempenho com iPads mais baratos e mais antigos não é tão grande quanto as pessoas imaginam. Qualquer iPad compatível com o Apple Pencil roda o Nomad muito bem. Por exemplo:

* Um iPad Pro de 2023 aguenta esculturas de 5 milhões de polígonos com boa resposta, e uma imagem com qualidade final renderiza em 5 segundos.
* Um iPad Pro de 2015 aguenta um objeto de 1,2 milhão de polígonos com um pouco de atraso, e uma imagem com qualidade final renderiza em 20 segundos.

É uma diferença de desempenho grande, mas também é preciso levar o preço em conta:

* O iPad Pro de 2025 custa *US$ 2.500* novo, com todas as opções.
* O iPad Pro de 2023 custa hoje *US$ 400* no eBay.
* O iPad Pro de 2015 custa *US$ 250* no eBay.

Ganhar 4 milhões de polígonos a mais e economizar 15 segundos vale US$ 2.100? Isso é com você.

Os modelos que não são Pro podem ser ainda mais baratos e oferecem uma grande variedade de tamanhos e desempenhos. O iPad Air atual aceita a caneta de 2ª geração com barrel roll e é bem mais barato que o Pro. O mercado de usados e recondicionados tem ainda mais opções.

Ou seja, qualquer que seja o seu orçamento, você deve encontrar um iPad para você. E lembre-se de que a maioria das esculturas não tem milhões de polígonos! Se você ficar abaixo de 500.000 polígonos, até iPads antigos permitem esculpir com rapidez.

`E o Android?`

O desempenho gráfico do Android fica abaixo do dos iPads. Segundo o desenvolvedor do Nomad, "Um Samsung Galaxy Tab S9 roda o Nomad uma ordem de grandeza mais devagar que um iPad Air". Dito isso, muitos usuários estão muito satisfeitos com os seus tablets Samsung, e o Nomad roda bem para a maior parte da escultura.

Com outros tablets Android, tome cuidado. O desempenho do hardware Android varia muito, e não é fácil prever como o Nomad vai rodar.

Use primeiro a versão gratuita do Nomad, sem salvamento, para testar.

`E a memória e o armazenamento?`

A maioria dos arquivos do Nomad tem 100 MB ou menos. Ou seja, quase qualquer tablet que você comprar hoje em dia, iPad ou Android, terá espaço de sobra para os seus projetos do Nomad.


### Comprei o Nomad para um aparelho, posso usá-lo em outro? {#multi-devices}
Sim, desde que use a mesma loja de aplicativos e a mesma conta.

Por exemplo, se você comprou na App Store do iOS, pode usá-lo nos seus outros aparelhos iOS.

Se comprou para o seu tablet Android no Google Play, pode usá-lo nos seus outros aparelhos Android.

Mas, se você comprou o Nomad no Android e depois comprar um iPad, vai precisar comprá-lo de novo.

Isso acontece porque o Nomad não tem um servidor de licenças próprio nem um modelo de assinatura. Não existe nenhum acordo entre Apple/Google/AppGallery para compartilhar licenças.


### Como restaurar a minha compra? {#restore}
O Google Play e a AppGallery cuidam da sincronização automaticamente.

- Abra o menu Sobre (ícone do Nomad no canto superior esquerdo) e toque em `Restaurar compra`
- Confira se você está conectado à mesma conta usada para comprar o Nomad (no Google Play).
- Reinicie o aparelho
- Às vezes é preciso esperar algumas horas
- Verifique se o aplicativo Google Play está atualizado
- Reinstale o Nomad (faça [backup dos seus arquivos](#locate) antes, se não quiser perder nada)
- Você pode tentar comprar de novo para ver o que acontece (observação: não é possível comprar o mesmo item duas vezes na mesma conta)

:::tip
Você pode entrar em contato comigo em <support@nomadsculpt.com>, mas a *única* coisa que vou poder fazer é confirmar se um e-mail tem uma compra associada.

Recebo com frequência relatos de licenças que não se atualizam direito depois da troca de aparelho.
Não tenho nenhum controle sobre o pagamento e a sincronização das contas: tudo isso é feito pelo Google/AppGallery!

No fim, a compra sempre acaba sendo restaurada, mas não se sabe bem o que fazer para acelerar o processo.
:::

::: warning
Os aparelhos Huawei recentes não têm acesso aos serviços do Google.
Nesse caso, você vai precisar comprar o aplicativo de novo na AppGallery (a loja de aplicativos da Huawei).
:::

### Você pode traduzir ou corrigir [meu-idioma]? {#locale}
Consigo adicionar outro idioma com relativa facilidade, mas uso tradução por IA, porque é muito mais fácil de manter com as atualizações frequentes.
Os arquivos de tradução estão [aqui](https://github.com/stephomi/nomad-translation).

## Recursos {#features}

### Por que o gizmo não se move? {#gizmo-not-moving}
Talvez você esteja com [o fixar ativado na barra de ferramentas do menu da esquerda](tools#left-menu-toolbar).

### Dá para animar no Nomad? {#animate}
Por enquanto, não. Uma linha do tempo que animasse as camadas poderia ser interessante, mas não está nos planos no momento.

Eu gostaria de oferecer rigging/skinning no futuro, mas isso traz alguns desafios (principalmente a interação com as ferramentas de escultura...), então nada garantido por enquanto.


### Dá para fazer modelagem low poly de verdade? {#lowpoly}
Por enquanto, não.
Isso não é bem o foco do Nomad *Sculpt*, mas talvez eu ofereça algumas ferramentas no futuro.


### Dá para fazer UV e texturização? {#texturing}
Resposta curta: sim. Resposta longa: não diretamente, mas há várias formas de combinar as excelentes ferramentas de pintura de vértices do Nomad com UVs e texturas.

* O Nomad permite pintar a cor, a aspereza e as propriedades do material diretamente nos vértices da escultura.
* O Nomad aceita uma quantidade muito alta de vértices, para você pintar sem se preocupar com UVs.
* O Nomad pode carregar texturas para usar nos pincéis, o que permite carimbar e pintar com texturas.
* O Nomad pode carregar objetos que já têm texturas atribuídas, para renderizá-los.
* O Nomad pode [desdobrar os UVs](topology.md#uv-unwrap-uvatlas) de objetos com menos polígonos.
* A cor, a aspereza e a metalidade podem ser transferidas das texturas para os vértices pelas [opções de projeção](topology.md#reproject-to-vertex).
* A cor, a aspereza, a metalidade e as normais podem ser seladas dos vértices para as texturas pelas [opções de selagem](topology.md#bake-texture)
* A selagem e a projeção podem ser feitas entre objetos individuais ou entre muitos objetos, ou entre o nível de subdivisão mais alto e o mais baixo de um mesmo objeto, o que permite vários fluxos de trabalho de selagem e projeção.
* Depois da selagem, exportar um OBJ também exporta as texturas, que podem ser levadas para um aplicativo como o Procreate para pintar diretamente nelas.

### Posso gravar um vídeo de mesa giratória? {#video}
Não está nos planos por enquanto: o iOS tem um [recurso de gravação de tela](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) muito fácil de usar.

No iOS, deslize para baixo a partir do canto superior esquerdo e toque no botão de gravar. Aparece uma contagem regressiva de 3 segundos: feche o menu deslizando para mostrar o Nomad e use a mesa giratória. Quando terminar, deslize para baixo de novo a partir do canto superior direito e toque outra vez no botão de gravar. Edite o vídeo na biblioteca de fotos para cortar as sobras do começo e do fim.

### Você pode colocar [recurso-favorito] como um botão principal? {#interface}
Sim, agora a barra de ferramentas de baixo pode ser personalizada no menu [Interface](interface.md#shortcuts), e também é possível criar barras de ferramentas flutuantes.

### Quais são os próximos recursos? {#next-features}
Para o médio e o longo prazo, tenho muitas ideias, mas ainda não sei.

Corrigir bugs e melhorar os recursos existentes sempre terá prioridade sobre adicionar recursos novos.


### Dá para fazer rigging no Nomad? {#rigging}
Não, mas está nos planos. Por enquanto, você pode aparentar formas entre si e mudar os pontos de pivô, o que permite esculturas simples que podem ser posadas.

### Dá para usar mais de 4 luzes? {#lights}
Você pode usar até 4 luzes no celular e no tablet, e até 6 no computador. É uma limitação do motor de renderização em tempo real do Nomad. Dá para simular mais luzes com objetos emissivos e a iluminação global do pós-processamento, como mostra [este tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Dá para importar as ferramentas do ZBrush? {#zbrush-import}
Não, o ZBrush usa um formato proprietário. Você deve conseguir extrair os mapas de alfa e usá-los no Nomad.

### Por que as cores não ficam iguais às que eu pintei? Por que não consigo branco na renderização? {#paint-pbr}
Imagine tirar uma foto de uma folha de papel, de uma luminária de mesa e do sol. As câmeras e telas mais antigas deixam tudo simplesmente "branco". Os sistemas mais modernos conseguem mostrar a diferença entre o branco refletido pelo papel, a luz emitida pela luminária e o brilho intenso do sol.

A computação gráfica moderna tenta funcionar de um jeito parecido, imitando a física da luz e das superfícies. Isso se chama `renderização baseada em física`, ou PBR, e o renderizador PBR do Nomad se baseia nisso. O resultado parece realista e equilibrado, mas muitas vezes as cores pintadas bem claras parecem mais escuras.

Se você precisa que a renderização fique mais perto das cores pintadas, há como resolver isso tanto sem quanto com renderização baseada em física:

Sem PBR:
* `Use o modo "Sem iluminação" no menu Sombreamento`. As cores aparecem exatamente como foram pintadas, mas você também perde todo o sombreamento. Prático para conferências rápidas e para um resultado mais gráfico.
* `Use o modo "MatCap" no menu Sombreamento`. Escolha um matcap mais claro, quase todo branco, sem tom de cor.

Com PBR:
* `Use um ambiente neutro`. Você pode [trocar o ambiente](shading.md#environment) por um mais neutro. Evite ambientes internos, que costumam ser mais coloridos. Prefira um ambiente externo com luz do dia ou de estúdio.
* `Reforce a iluminação`. Se você estivesse fotografando um papel branco em um quarto escuro, simplesmente acrescentaria mais luz. Na luz de ambiente, aumente o controle de exposição até as cores parecerem certas para você, ou adicione mais luzes com mais intensidade.
* `Aumente a exposição da câmera`. Se o quarto escuro não tivesse mais nenhuma luz, você poderia deixar o obturador da câmera aberto por mais tempo ou usar um ISO mais sensível. No Nomad, dá para conseguir um resultado parecido com o pós-processamento. Abra o Pós-processamento, ative-o, desça até Mapeamento de Tons, ative-o e aumente o controle de exposição até as cores parecerem certas.
* `Use uma cor emissiva`. No menu Material, você pode ativar "Emissiva" nas texturas, o que faz o objeto parecer uma fonte de luz. Se você ligar a iluminação global nos ajustes de pós-processamento, ele ilumina os outros objetos da cena. Você também pode ativar "Sempre não iluminado" para esse material, o que dá uma aparência parecida sem textura.

## Travamentos {#crashes}

### O app trava quando salvo ou remalho o modelo! {#crash-remesh}
O seu aparelho está ficando sem memória (RAM).  
Para reduzir o uso de memória da cena, você pode usar algumas opções de [Topologia](topology.md) para diminuir o número de polígonos.

::: tip RAM/armazenamento
O que importa é a quantidade de RAM, não o armazenamento (que geralmente é bem maior).
:::


### O app trava quando abro o meu projeto! {#crash-load}
Se o arquivo for pequeno, você pode me enviar para eu dar uma olhada (pelo e-mail <support@nomadsculpt.com>).

Caso contrário, o aparelho provavelmente está ficando sem memória RAM.

- Feche todos os outros aplicativos abertos no aparelho.
- Comece um projeto novo no Nomad em vez de ficar com um projeto aberto.
- Se ainda travar, a única solução é abrir o [arquivo do seu projeto](#locate) em um aparelho com mais memória.

::: tip
Se o seu aparelho móvel não consegue abrir o projeto, experimente a [versão para computador](https://nomadsculpt.com). Você pode usá-la de graça no modo Demo para importar e exportar projetos, embora só algumas ferramentas de edição estejam disponíveis.

Se o seu projeto usa [Camadas](layers.md), vale a pena mesclá-las para reduzir o uso de memória.
:::

### O app trava quando abro o Nomad! {#crash-start}
Se ele trava ao carregar, significa que o Nomad está com problemas com algum arquivo da pasta do Nomad.

Na maioria das vezes, isso acontece porque o projeto é pesado e, infelizmente, passa do limite de RAM.

Encontre a [pasta do Nomad](#locate) e renomeie ou mova alguns arquivos para achar o culpado.

Primeiro, tente renomear `settings.json`. Assim o Nomad deixa de carregar o último projeto.

Se não funcionar, tente mover alguns arquivos recentes para fora das pastas de recursos deles (`projects`, `matcaps`, `environments` etc.).

Você também pode renomear as próprias pastas para que o Nomad as ignore completamente.
Se você renomear ou mover todos os arquivos da pasta do Nomad, o resultado é o mesmo de uma instalação limpa.

::: tip
Quando o Nomad abre um arquivo na inicialização, ele sempre move o arquivo para a pasta `can_be_deleted/`.
Se a operação der certo, o arquivo volta para a pasta original.

Se o app travar antes de terminar de carregar, o Nomad abre normalmente na próxima vez, porque ignora a pasta `can_be_deleted/`.

Você pode simplesmente tentar abrir esse arquivo de novo se achar que vai dar certo.
:::

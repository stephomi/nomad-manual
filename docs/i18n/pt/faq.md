# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Plataforma {#platform}
### Onde estão localizados meus projetos no meu dispositivo? {#locate}
Os projetos estão localizados na pasta `projects` dentro da pasta principal do Nomad.

No iOS, você pode acessar a pasta do Nomad com o app Arquivos do iOS.

No Android, a pasta do Nomad fica em `Android/data/com.stephaneginier.nomad/files/`.  
Nas versões recentes do Android (10/11), você não tem mais acesso à pasta `Android/data`.
Você pode acessá-la por meio de um app separado, por exemplo [este aqui](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Existe uma forma de testar a versão beta? {#beta}
Para Windows e MacOS, uma versão beta pode estar disponível na [Homepage](https://nomadsculpt.com).
<br>
Para iOS há um TestFlight privado, visite o [Discord](https://discord.com/invite/8h7BwpRz29) no canal #beta-ios.
<br>
A [Demo Web](https://nomadsculpt.com/demo) geralmente é atualizada com os recursos mais recentes.

### Por que há um teste gratuito no Android, mas não no iOS? {#android-trial}
Porque dispositivos Android antigos são ruins (e alguns recentes também...), e eu não queria que as pessoas comprassem o app e fossem recebidas com uma tela preta.
Mas o principal motivo é que eu sinto que apps pagos no Android não são exatamente a norma.

### Qual é o melhor tablet para rodar o Nomad? {#best-tablet}

Resumo: Um iPad.

A resposta um pouco mais longa é 

> "O iPad mais novo _que você puder pagar_, a menos que você realmente odeie a Apple, nesse caso o tablet Samsung mais novo que você puder pagar. Qualquer outra coisa, teste antes." 

As pessoas sempre querem mais informações, então aqui vai um resumo.

O Nomad roda melhor em iPads mais novos:

* iPads e iPhones podem acessar o plugin [Quad Remesher](tools#quad-remesher) da [Exoside](https://exoside.com/)
* iPads recentes com o pencil mais novo suportam [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), você pode girar o pencil em certas ferramentas no Nomad. 
* o desempenho dos chips mais recentes da série M é muito rápido. 

O iPad mais novo e mais caro disponível será capaz de renderizar imagens finais muito rapidamente e permitir que você esculpa muitos detalhes.

No entanto, a queda de desempenho com iPads mais baratos e antigos não é tão grande quanto as pessoas esperam. Qualquer iPad que suporte Apple Pencil roda o Nomad muito bem. Por exemplo:

* Um iPad Pro de 2023 consegue lidar com esculturas de 5 milhões de polígonos e continuar responsivo, uma imagem em qualidade final pode ser renderizada em 5 segundos.
* Um iPad Pro de 2015 consegue lidar com um objeto de 1,2 milhão de polígonos com um pouco de atraso, uma imagem em qualidade final pode ser renderizada em 20 segundos.

É uma grande diferença de desempenho, mas você também precisa levar em conta o preço:

* O iPad Pro de 2025 custa *US$ 2500* novo com todas as opções. 
* O iPad Pro de 2023 atualmente custa *US$ 400* no eBay.
* O iPad Pro de 2015 custa *US$ 250* no eBay.

Conseguir 4 milhões de polígonos extras e economizar 15 segundos vale US$ 2100? Isso depende de você.

Modelos não Pro podem ser ainda mais baratos e oferecem uma grande variedade de tamanhos e desempenhos para escolher. O iPad Air atual suporta o pencil de 2ª geração com barrel roll, e é substancialmente mais barato que o Pro. O mercado de usados e recondicionados tem ainda mais opções. 

Isso significa que, qualquer que seja o seu orçamento, você deve conseguir encontrar um iPad para você. E lembre-se de que a maioria das esculturas não tem milhões de polígonos! Se você conseguir ficar abaixo de 500.000 polígonos, até iPads antigos permitirão que você esculpa rapidamente.

`E quanto ao Android?`

O desempenho gráfico do Android é inferior ao dos iPads. Segundo o desenvolvedor do Nomad, "Um Samsung Galaxy Tab S9 rodará o Nomad uma ordem de grandeza mais lento que um iPad Air". Dito isso, muitos usuários ficam muito satisfeitos com seus tablets Samsung, o Nomad roda bem para a maior parte da escultura. 

Para outros tablets Android, tenha cuidado. O hardware Android pode variar muito em desempenho, não é fácil prever como o Nomad vai rodar.

Use primeiro a versão gratuita sem salvamento do Nomad para testar. 

`E quanto à memória e armazenamento?`

A maioria dos arquivos do Nomad tende a ter 100 MB ou menos. Isso significa que praticamente qualquer tablet que você compre hoje em dia, iPad ou Android, terá espaço de sobra para seus projetos do Nomad.


### Comprei o Nomad para um dispositivo, posso usá-lo em outro? {#multi-devices}
Desde que use a mesma loja de apps e a mesma conta, sim.

Por exemplo, se você comprou na App Store do iOS, pode usá-lo em seus outros dispositivos iOS.

Se você comprou para seu tablet Android na Google Play, pode usá-lo em seus outros dispositivos Android.

No entanto, se você comprou o Nomad no Android e depois adquirir um iPad, será necessário comprá-lo novamente.

Isso acontece porque o Nomad não tem seu próprio servidor de licença ou modelo de assinatura. Não há acordo entre Apple/Google/AppGallery para lidar com compartilhamento de licença. 


### Como restaurar minha compra? {#restore}
A Google Play e a AppGallery lidam com a sincronização automaticamente.

- Vá no menu About (ícone do nomad no canto superior esquerdo) e toque em `restore purchase`
- Verifique duas vezes se você está conectado na mesma conta que usou para comprar o Nomad (na Google Play).
- Reinicie o dispositivo
- Às vezes é preciso esperar algumas horas
- Certifique-se de que o app Google Play está atualizado
- Reinstale o Nomad (certifique-se de [fazer backup dos seus arquivos](#where-are-my-projects-located-on-my-device) se não quiser perder nada)
- Você pode tentar comprar novamente para ver o que acontece (observação: você não pode comprar o mesmo item duas vezes na mesma conta)

:::tip
Você pode entrar em contato comigo em <support@nomadsculpt.com>, mas a *única* coisa que vou poder fazer é confirmar se um e-mail tem uma compra associada a ele.

Note que recebo regularmente relatos sobre licenças que não atualizam corretamente após adquirir um novo dispositivo.
Eu não tenho nenhum controle sobre o pagamento e a sincronização de contas, tudo é gerenciado pela Google/AppGallery!

Eventualmente a compra sempre é restaurada, mas os passos necessários para acelerar o processo não são claros.
:::

::: warning
Dispositivos Huawei recentes não têm acesso aos serviços da Google.
Nesse caso você precisará comprar o app novamente na AppGallery (loja de apps da Huawei).
:::

### Você pode traduzir ou corrigir [minha-língua]? {#locale}
Eu posso adicionar outra língua relativamente fácil, mas estou contando com tradução por IA, pois é muito mais fácil de lidar para atualizações regulares.
Os arquivos de tradução podem ser encontrados [aqui](https://github.com/stephomi/nomad-translation).

## Funcionalidades {#features}

### Por que o gizmo não se move? {#gizmo-not-moving}
Você pode estar com o [pin ativado na barra de ferramentas do menu esquerdo](tools#left-menu-toolbar). 

### Podemos animar dentro do Nomad? {#animate}
Por enquanto não. Um recurso de linha do tempo que pudesse animar as camadas poderia ser interessante, mas não está realmente planejado no momento.  

Eu gostaria de dar suporte a rigging/skinning no futuro, mas isso traz alguns desafios (notadamente a interação com as ferramentas de escultura...) então nada certo por enquanto.


### Podemos fazer modelagem low-poly de verdade? {#lowpoly}
Por enquanto não.
Isso não é exatamente o foco do Nomad *Sculpt*, mas talvez eu forneça algumas ferramentas no futuro.


### Podemos fazer UV e texturização? {#texturing}
Resposta curta: Sim. Resposta longa: Não diretamente, mas há várias maneiras de combinar as excelentes ferramentas de pintura por vértice do Nomad com UVs e texturas.

* O Nomad permite pintar cor, rugosidade e propriedades de material diretamente nos vértices da sua escultura.
* O Nomad permite contagens de vértices muito altas para que você possa pintar sem se preocupar com UVs.
* O Nomad pode carregar texturas para usar em pincéis, permitindo carimbos e pintura com texturas.
* O Nomad pode carregar objetos que já tenham texturas atribuídas, para fins de renderização.
* O Nomad pode fazer [UV unwrap](topology.md#uv-unwrap) em objetos de baixa contagem de polígonos.
* Cor/rugosidade/metalness podem ser transferidos de texturas para vértices por meio [das opções de projeção](topology.md#reproject-to-vertex).
* Cor/rugosidade/metalness/normais podem ser assados de vértices para texturas por meio [das opções de baking](topology.md#bake-to-texture)
* Baking e projeção podem ser feitos entre objetos únicos ou muitos objetos, ou entre os níveis de subdivisão mais alto e mais baixo de um único objeto, permitindo uma variedade de fluxos de trabalho de bake e projeção.
* Após o baking, exportar um obj também exportará as texturas, que podem ser levadas para um app como o Procreate para pintar diretamente nas texturas.

### Posso gravar um vídeo de turntable? {#video}
Não está planejado por enquanto, o iOS tem um [recurso de gravação de vídeo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) que é muito fácil de usar.

No iOS, isso é feito deslizando para baixo a partir do canto superior esquerdo e tocando no botão de gravação. Ele dará uma contagem regressiva de 3 segundos, deslize o menu para fora para revelar o Nomad e use o recurso de turntable. Quando terminar, deslize novamente para baixo a partir do canto superior direito e toque no botão de gravação novamente. Edite o vídeo na biblioteca de fotos para remover o excesso de filmagem no início e no fim do vídeo.

### Você pode adicionar [insira-função-favorita] como um botão de nível superior? {#interface}
Sim, a barra de ferramentas inferior agora pode ser personalizada a partir do menu de [interface](interface.md), e barras de ferramentas flutuantes agora podem ser criadas.

### Quais são as próximas funcionalidades? {#next-features}
Para o roadmap de médio/longo prazo eu tenho muitas ideias, mas ainda não sei.  

Correções de bugs e melhorias em recursos existentes sempre terão prioridade maior do que adicionar novos recursos.


### Podemos fazer rig no Nomad? {#rigging}
Não, mas está planejado. Por enquanto você pode fazer parentesco entre formas e alterar pontos de pivô, permitindo esculturas simples posáveis.

### Podemos usar mais de 4 luzes? {#lights}
Não, isso é uma limitação do motor de renderização em tempo real dentro do Nomad. É possível simular isso usando objetos emissivos e iluminação global em pós-processamento, como mostrado [neste tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Podemos importar tools do ZBrush? {#zbrush-import}
Não, o Zbrush usa um formato proprietário. Você deve conseguir extrair os mapas de alpha e usá-los no Nomad. 

### Por que as cores não correspondem ao que pintei? Por que não consigo obter branco no render? {#paint-pbr}
Imagine tirar uma foto de uma folha de papel, de uma luminária de mesa e do sol. Câmeras e telas mais antigas simplesmente deixariam tudo “branco”. Sistemas mais modernos conseguem mostrar a diferença entre o branco refletido do papel, a luz emitida da lâmpada e o super brilho do sol.

A computação gráfica moderna tenta funcionar de forma semelhante, emulando a física da luz e das superfícies. Isso é chamado de `Renderização Baseada Fisicamente`, ou PBR, e o renderizador PBR do Nomad é baseado nisso. Isso parece realista e equilibrado, mas muitas vezes cores pintadas muito brilhantes vão parecer mais escuras.

Se você precisa que o render corresponda mais de perto às cores pintadas, você pode corrigir isso de formas tanto não fisicamente baseadas quanto fisicamente baseadas:

Não PBR:
* `Use o modo 'Unlit' no menu de iluminação`. As cores serão mostradas exatamente como foram pintadas, mas você também perde toda a sombra. Útil para verificações rápidas e saídas mais gráficas.
* `Use o modo 'Matcap' no menu de iluminação`. Escolha um matcap mais brilhante que seja majoritariamente branco, sem tonalidade de cor.

PBR:
* `Use um ambiente neutro`. Você pode [mudar o ambiente](shading.md#environment) para um mais neutro. Evite ambientes internos, pois tendem a ser mais coloridos. Prefira um ambiente externo de luz do dia ou de estúdio.
* `Aumente a iluminação`. Se você estivesse tirando uma foto de papel branco em um quarto escuro, simplesmente adicionaria mais luz. Na luz de ambiente, aumente o controle deslizante de exposição até que as cores comecem a parecer certas para você, ou adicione mais luzes individuais com mais intensidade.
* `Aumente a exposição da câmera`. Se o quarto escuro não tivesse luzes extras, você poderia fazer a câmera manter o obturador aberto por mais tempo ou usar um ISO mais sensível. No Nomad você pode obter um resultado semelhante com pós-processamento. Vá em pós-processamento, ative, desça até tone mapping, ative e aumente o controle deslizante de exposição até que as cores pareçam corretas.
* `Use cor emissiva`. No menu de material, você pode ativar “emissive” em texturas, o que fará um objeto parecer uma fonte de luz. Se você ativar iluminação global nas configurações de pós-processamento, ele lançará luz sobre outros objetos na cena. Você também pode ativar “unlit” para esse material, o que alcançará um visual semelhante sem textura.

## Travamentos {#crashes}

### Ele trava quando salvo ou faço remesh do meu modelo! {#crash-remesh}
Seu dispositivo está ficando sem memória (RAM).  
Para reduzir o uso de memória na sua cena, você pode usar algumas das opções de [Topologia](topology.md) para reduzir o número de polígonos.

::: tip RAM/Armazenamento
O que importa é a quantidade de RAM, não o armazenamento (que geralmente é muito maior).
:::


### Ele trava quando carrego meu projeto! {#crash-load}
Se o arquivo for pequeno, você pode me enviar e eu darei uma olhada (por e-mail <support@nomadsculpt.com>).

Caso contrário, o dispositivo provavelmente está ficando sem memória RAM.

- Certifique-se de fechar quaisquer outros apps abertos no seu dispositivo.
- Inicie um novo projeto no Nomad em vez de ter um projeto atualmente aberto.
- Se ainda travar, a única solução é carregar [seu arquivo de projeto](#where-are-my-projects-located-on-my-device) em um dispositivo com mais memória.

::: tip
Em um navegador de desktop, você pode tentar carregar seu arquivo [nesta URL](https://nomadsculpt.com/demo_save/) e então exportá-lo de volta após simplificar sua cena.

Alguns navegadores limitam a quantidade de RAM que uma única aba pode usar, então é possível que essa técnica não funcione.

Se seu projeto estiver usando [Layers](layers.md), talvez você queira achatá-las para reduzir o uso de memória.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Ele trava quando inicio o Nomad! {#crash-start}
Se ele trava ao carregar, significa que o Nomad está tendo problemas com algum arquivo presente na pasta do Nomad.

Na maioria das vezes isso acontece porque o projeto é pesado e infelizmente excederá o limite de RAM.

Localize a [pasta do Nomad](#where-are-my-projects-located-on-my-device) e então renomeie ou mova alguns arquivos para encontrar o culpado.

Primeiro, tente renomear `settings.json`. Assim ele deixará de carregar o último projeto.

Se não funcionar, tente mover alguns arquivos recentes para fora de suas respectivas pastas de recursos (`projects`, `matcaps`, `environments`, etc).

Você também pode renomear as próprias pastas para que o Nomad as ignore completamente.
Se você renomear ou mover todos os arquivos da pasta do Nomad, isso terá o mesmo efeito de uma instalação limpa.

::: tip
Quando o Nomad carrega um arquivo na inicialização, ele sempre move o arquivo para a pasta `can_be_deleted/`.
Se a operação for bem-sucedida, então ele é movido de volta para sua pasta original.

Se o app travar antes de terminar o carregamento, o Nomad será iniciado com sucesso na próxima vez, pois ele ignora a pasta `can_be_deleted/`.

Você pode simplesmente tentar carregar esse arquivo novamente se achar que pode dar certo.
:::
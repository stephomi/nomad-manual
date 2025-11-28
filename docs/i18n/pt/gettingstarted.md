# Primeiros Passos {#getting-started}

## Bem-vindo ao Nomad! {#welcome-to-nomad}

Nomad é um aplicativo de escultura 3D que funciona em muitos dispositivos, e funciona melhor em tablets com caneta sensível à pressão, por exemplo um iPad com Apple Pencil, ou um Samsung Galaxy Tab com caneta.

Ele é inspirado em aplicativos de escultura para desktop como ZBrush e Blender, com foco em uma interface fácil de entender, sem sacrificar recursos. Se você já usou aplicativos de escultura 3D antes, o Nomad será muito familiar.

Se esta é a sua primeira vez fazendo escultura 3D, é bom conhecer alguns conceitos básicos.

::: tip Prefere vídeo?
O YouTube agora tem MUITOS tutoriais em vídeo para iniciantes, aqui vão alguns ótimos links:

* [Nomad Sculpt Crash Course by Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial by Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS series by SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Vale a pena conferir o canal principal desses criadores, eles frequentemente publicam novos tutoriais.
:::

## Sua primeira escultura {#your-first-sculpt}

Quando você inicia o Nomad pela primeira vez verá uma esfera na tela. Basta arrastar a caneta sobre a esfera para começar a esculpir. A simetria é ativada por padrão para facilitar a escultura.

![](/videos/gettingstarted_01.mp4)

Para deixar o pincel maior ou menor, use o controle deslizante de raio à esquerda.

![](/videos/gettingstarted_02.mp4)

Para deixar o pincel mais forte ou mais fraco, use o controle deslizante de intensidade à esquerda.

![](/videos/gettingstarted_03.mp4)

A ferramenta padrão é a `Clay tool`, e ela adiciona material à superfície. Para subtrair da superfície, toque no botão `Sub` à esquerda. Para voltar a adicionar à superfície, toque no botão Sub novamente.

![](/videos/gettingstarted_04.mp4)

Para suavizar a superfície, toque no botão `Smooth`. Para voltar à escultura normal, toque no botão Smooth novamente.

![](/videos/gettingstarted_05.mp4)

Para girar em torno do modelo, arraste em um espaço vazio fora do modelo.

![](/videos/gettingstarted_06.mp4)

Para dar zoom, use o gesto de pinça com dois dedos.

![](/videos/gettingstarted_07.mp4)

Para mover a câmera (pan), pressione 2 dedos na tela e arraste.

![](/videos/gettingstarted_08.mp4)

Se você cometer um erro, um toque com 2 dedos desfaz a ação, ou use o botão de desfazer no canto inferior esquerdo. 

![](/videos/gettingstarted_09.mp4)

::: tip Versão desktop
No desktop, a tecla alt/opt é usada para controlar a câmera:

* toque e arraste em espaço vazio = girar a câmera
* alt+toque e arraste = pan
* alt+toque e arraste, depois solte o alt = zoom (igual ao ZBrush)

Com mesas digitalizadoras Wacom que têm 2 ou mais botões na caneta, use as configurações da Wacom para configurar a ponta e os botões assim:

* ponta = clique esquerdo
* botão inferior (rocker) = clique do meio
* botão superior (rocker) = clique direito

Com essas configurações, você pode manipular a câmera apenas com a caneta:

* botão superior e movimento em hover = girar a câmera
* botão inferior e movimento em hover = pan
:::

## Adicionar cor {#add-color}

O Nomad permite pintar a superfície da sua escultura. No menu de ferramentas à direita, encontre a ferramenta `Paint` e clique nela. Na barra de ferramentas à esquerda aparecerá uma esfera colorida. Clique nela, isso abrirá um seletor de cores. Escolha uma cor e pinte no seu modelo.

![](/videos/gettingstarted_10.mp4)

Para apagar, toque no botão `Erase` na barra de ferramentas à esquerda, depois apague na superfície. Toque no botão Erase novamente para voltar ao modo de pintura.

![](/videos/gettingstarted_11.mp4)

Usando o pincel de clay nos modos add/sub, smooth e paint, veja se você consegue fazer uma cabeça de desenho animado simples:

![](/images/gettingstarted_head1.webp)

## Outras ferramentas {#other-tools}

A paleta de ferramentas tem muitas ferramentas para ajudar na escultura. Até agora você usou o pincel de clay (a ferramenta padrão inicial), smooth e paint. Como o smooth é usado com frequência, ele tem um atalho extra na barra de ferramentas à esquerda.

As ferramentas no Nomad podem fazer uma grande variedade de coisas, desde ferramentas relacionadas à escultura como move, crease, inflate, até ferramentas como split e trim que são mais parecidas com ferramentas de carpintaria ou metalurgia. A página [Tools](tools.md) tem mais informações.

Veja se você consegue usar as ferramentas move, crease, inflate e smooth para adicionar mais detalhes à sua cabeça, mudando sua forma:

![](/images/gettingstarted_head2.webp)

Agora que você conhece o básico do Nomad, vamos ver o resto da interface.

## Interface {#interface}

![](/images/interface_overview1.webp)

* `Top menus` - Os menus para acessar a maioria dos recursos do Nomad. Os menus no canto superior esquerdo cobrem principalmente recursos de cena e objeto, os menus no canto superior direito estão relacionados às ferramentas. Em telas menores esses menus serão agrupados para economizar espaço.
* `Stats` - Informações sobre a cena, o objeto atual, status da máscara, uso de memória.
* `Nav Cube` - Um auxiliar para mostrar de que lado da escultura você está olhando, além de um atalho para pular para diferentes vistas. Tocar no cubo fará a vista pular para o lado tocado. Arrastar o cubo irá girá‑lo. Toque nos pequenos ícones ao lado do cubo para enquadrar o objeto atual ou redefinir para a vista inicial padrão.
* `Toolbox` - As ferramentas do Nomad estão disponíveis nesta região rolável.
* `Left toolbar` - Controles deslizantes para raio e intensidade para a maioria das ferramentas, botões específicos de contexto para outras ferramentas e atalhos para simetria, o modo alt/sub da ferramenta, máscara, suavização, gizmo e opções de pintura.
* `Bottom toolbar` - Atalhos para recursos usados com frequência, explicados abaixo.

::: tip Canhoto?
Você pode espelhar a posição e a ordem de todas as barras de ferramentas, veja [Mirror top bar](interface.md#mirror-top-bar) e outras opções relacionadas.
:::

## Barra de ferramentas inferior {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Undo` - reverte a última operação
* `Redo` - restaura a última operação desfeita
* `History` - acessa as opções de histórico, explicadas no menu [History](history.md).
* `Solo` - Alterna entre mostrar apenas o objeto atual ou todos os objetos
* `X-Ray` - Faz com que todos os outros objetos sejam renderizados em modo raio‑X, e o objeto atual fique sólido. Um toque longo ou deslizar para cima permite definir a cor e a opacidade do modo raio‑X.
* `Voxel` - Um atalho para o botão de remesh do [Voxel Remesher](topology.md#voxel-remesher). Um toque longo ou deslizar para cima revela atalhos para definir a qualidade do voxel remesh.
* `Grid` - Alterna a exibição da grade. Um toque longo ou deslizar para cima revela opções para a grade.
* `Wire` - Alterna uma sobreposição de wireframe. Um toque longo ou deslizar para cima revela opções para o wireframe.
* `Inspect` - Alterna a visualização de dados extras sobre a malha atual. Por padrão exibirá UVs, mas um toque longo ou deslizar para cima permite inspecionar outras propriedades, se existirem, e se isso é exibido no fundo ou na própria malha.

## Próximos passos {#next-steps}

O que você deve aprender em seguida depende de você e do que achar interessante! Aqui vão algumas sugestões:

Quer aprender mais sobre as ferramentas de escultura? Vá para a seção [Tools](tools.md).

Quer exportar seus modelos? Ou importar modelos para esculpir? Ou criar imagens das suas esculturas? Vá para a seção [Files](files.md).

Quer aprender mais sobre como controlar o nível de detalhe na sua escultura? Vá para a seção [Topology](topology.md) e aprenda sobre multires e decimation.

Quer trabalhar com mais objetos? Combinar objetos simples e primitivas em uma cena maior? Vá para a seção [Scene](scene.md).

Quer aprender *tudo* sobre o Nomad? Boa escolha! Este manual cobre todo o Nomad, inclui muitas dicas e truques e tem uma ótima função de busca no topo. Use a navegação à esquerda para aprender mais.

Se você prefere vídeo, Holger Schönischka fez uma enorme coleção de dicas e truques para o Nomad no YouTube: https://www.youtube.com/@ProcreateFX/videos


## Obtendo ajuda {#getting-help}

Se você ainda tiver dúvidas depois de ler o manual e assistir aos vídeos tutoriais, há três maneiras principais de falar com outros usuários do Nomad ou com o desenvolvedor do Nomad:

* Visite os fóruns: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Entre no chat do Discord do Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contate o desenvolvedor diretamente em support@nomadsculpt.com
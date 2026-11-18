# ![](/icons/open.webp) Arquivo {#files}

O menu Arquivo permite salvar e abrir projetos do Nomad, importar e exportar modelos 3d, exportar imagens renderizadas e conectar o Nomad a outros aplicativos. Ele tem três abas: `Arquivo`, `Renderizar` e `Vincular`.

![](/images/file_menu.webp)

## Projeto {#project}
![](/images/file_project.webp)

A miniatura no alto mostra o projeto atual, com o tamanho do arquivo, o salvamento automático e o histórico salvo ao lado. Toque na miniatura para abrir um pequeno navegador dos seus projetos e depois toque em um projeto para ver um menu que permite abrir, adicionar, substituir, clonar, renomear ou apagar o projeto.

Quando o projeto tem alterações que ainda não foram salvas, `Alterações não salvas!` aparece embaixo da miniatura.

### Âmbito {#scope}
No computador, escolha onde os seus projetos são salvos:
* `Interno` - o padrão, igual ao do celular e do tablet. Os projetos são salvos apenas dentro da pasta principal do Nomad.
* `No local` - quando você abre um projeto de fora da pasta do Nomad, salvar substitui o arquivo original. O salvamento automático não funciona para esses projetos externos.

### ![](/icons/nomad.webp) Pré‑ajuste {#preset}
Dá acesso a uma coleção de demonstrações e de partes de personagens. Selecione um item e depois selecione de novo para escolher entre `Abrir` ou `Adicionar à cena`. Você também pode baixar modelos gratuitos do Poly Haven por esse navegador.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Histórico... {#history}
Acesso rápido às opções de histórico do projeto, como `Salvar histórico`, que mantém o histórico de desfazer quando o projeto é salvo. Um selo verde no botão indica que o histórico é salvo com o projeto. Veja [Histórico](history.md#save-history) para mais detalhes.

### ![](/icons/save.webp) Salvar {#save}
Salva o projeto do Nomad. Se o projeto nunca foi salvo, o Nomad pede um nome.

### ![](/icons/save_as.webp) Salvar Como... {#save-as}
Salva o projeto com outro nome, como um projeto novo.

### ![](/icons/save_as.webp) Substituir... {#overwrite}
Mostra o navegador de projetos para salvar a cena atual por cima de outro projeto. Ative `Incluir apenas objetos selecionados` para salvar só os objetos selecionados em vez da cena inteira. O navegador também tem um botão `Salvar Como...` para salvar como um projeto novo.

### ![](/icons/pencil.webp) Renomear {#rename}
Mostra uma caixa de texto para renomear o projeto atual.

### ![](/icons/open.webp) Abrir... {#open}
Mostra o navegador de projetos para abrir um projeto.

### ![](/icons/add_file.webp) Adicionar à cena... {#add}
Mostra o navegador de projetos: ao selecionar um projeto, o conteúdo dele é mesclado à cena atual.

### ![](/icons/trash.webp) Apagar... {#delete}
Mostra o navegador de projetos: os projetos selecionados são apagados do sistema de arquivos.

### ![](/icons/new_file.webp) Novo {#new}
Começa um projeto novo. Se houver alterações não salvas, o Nomad pede uma confirmação. Nela, você pode `Manter` ou `Redefinir` os ajustes de `Fundo`, `Ambiente`, `MatCap` e `Raio-X`, e escolher se o novo projeto usa `Salvar histórico`.

### ![](/icons/autosave.webp) Salvamento automático... {#auto-save}
Menu com as opções de salvamento automático. Ative `Salvamento automático` para salvar o projeto em um arquivo separado a intervalos regulares. O selo no botão indica se ele está ligado.

O Nomad não salva em segundo plano porque os arquivos 3d podem ser bem grandes, o que causaria travadas perceptíveis enquanto você esculpe.

Além disso, para evitar falta de memória, a cena normalmente é compactada antes de ser salva.
Essa compactação e descompactação também deixa o salvamento mais lento.

### Intervalo de salvamento {#timer-pop-up}
Quantos minutos o Nomad espera entre um salvamento automático e outro.

### Mostrar contagem regressiva {#popup-timeout}
Mostra uma contagem regressiva antes de cada salvamento automático, para que você possa cancelá-lo se estiver no meio de alguma coisa. Quando desativado, o Nomad salva assim que você para de esculpir.

### ![](/icons/trash.webp) Descartar salvamento automático {#discard-autosave}
Se existir um arquivo de salvamento automático para um projeto, ele é carregado automaticamente no lugar do projeto original. Se você não quiser isso, este botão apaga o salvamento automático. Abrir o arquivo carrega então o último salvamento manual do projeto.

### ![](/icons/open.webp) Abrir salvamento desatualizado {#open-outdated-save}
Quando um projeto tem ao mesmo tempo um salvamento automático e um salvamento manual, este botão abre o mais antigo dos dois (`Abrir salvamento automático desatualizado` ou `Abrir salvamento manual desatualizado`), com a data dele. Prático se o salvamento mais recente não for o que você queria.

### ![](/icons/storage.webp) Apagados recentemente... {#recently-deleted}
O Nomad guarda por alguns dias os dados dos projetos que saíram da pasta de projetos, e os arquivos substituídos por uma importação, antes de apagá-los de vez. Os arquivos que falharam ao importar ficam até você apagá-los. Esta lista mostra esses arquivos com o tamanho e a data, para você apagá-los um por um ou com `Apagar tudo`.

## Importar {#import}

### ![](/icons/add_file.webp) Importar {#import-button}
Serve para importar arquivos 3d que não são projetos do Nomad.

Ao importar um arquivo de cena externo no Nomad, você pode *adicioná-lo* ou começar um projeto *novo* com ele.

Adicionar um arquivo simplesmente coloca os objetos na cena atual.
Escolher `Novo` cria um novo projeto do Nomad com os novos objetos.

A janela de importação lista todos os arquivos que você escolheu, cada um com as suas opções de importação. Também dá para importar imagens assim: escolha para cada uma se ela vira um `HDRI`, um `MatCap`, uma `Referência`, um `Alfa`, `Texturas` ou um `VDM`.

O Nomad pode importar estes formatos:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), nas plataformas compatíveis

### ![](/icons/cog.webp) Ajustes {#advanced}
O botão `Ajustes...` ao lado da miniatura do projeto mostra as principais opções de importação. Esses ajustes não são salvos, e a janela de importação mostra as opções que se aplicam aos arquivos que você está importando.

### Todos os formatos {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Manter topologia {#keep-topology}
Por padrão, o Nomad tenta corrigir geometrias problemáticas ao abrir o arquivo. Ativar esta opção impede o Nomad de reordenar vértices e faces, mesclar duplicatas e remover vértices não usados.

::: warning
Com `Manter topologia`, operações como booleana, unir, decimar ou manifold podem não mesclar os vértices duplicados.
:::

#### ![](/icons/image.webp) Ignorar texturas {#skip-textures}
Não carrega as texturas incorporadas ao arquivo, nos formatos que permitem isso, como o glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Carregar ajustes da IU {#keep-gui-settings}
Ao abrir ou importar um arquivo de projeto, carrega todos os ajustes da interface que foram salvos nele.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Dividir OBJ em grupos {#split-obj-by-groups}
Separa os grupos do OBJ em objetos diferentes.

#### ![](/icons/vertex.webp) Mesclar posições duplicadas {#merge-duplicate-positions}
Mescla os vértices que estão na mesma posição.

#### ![](/icons/uv.webp) Mesclar UVs duplicados {#merge-duplicate-uvs}
Mescla as coordenadas de textura que têm o mesmo UV.

#### ![](/icons/paint.webp) Espaço de cor {#color-space}
Define como as cores do arquivo são interpretadas: `Auto`, `Linear` ou `sRGB`. Experimente trocar esta opção se as cores parecerem erradas.

#### ![](/icons/image.webp) Formato {#normal-format}
O formato do mapa de normais das texturas: `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`. Experimente o outro se os detalhes do mapa de normais parecerem invertidos.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Espaço de cor {#color-space-ply}
Define como as cores do arquivo são interpretadas: `Auto`, `Linear` ou `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Mesclar UVs duplicados {#merge-duplicate-uvs-fbx}
Mescla as coordenadas de textura que têm o mesmo UV.

#### ![](/icons/paint.webp) Espaço de cor {#color-space-fbx}
Define como as cores do arquivo são interpretadas: `Auto`, `Linear` ou `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-fbx}
O formato do mapa de normais das texturas: `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Espaço de cor {#color-space-usd}
Define como as cores do arquivo são interpretadas: `Auto`, `Linear` ou `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-usd}
O formato do mapa de normais das texturas: `Auto`, `OpenGL (+Y)` ou `DirectX (-Y)`.



## Exportar {#export}
Salva em um formato de geometria 3d que pode ser usado em outros programas.

![](/images/file_export.webp)

Cada formato de arquivo aceita recursos diferentes, e as opções disponíveis mudam conforme o tipo de arquivo selecionado.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Cores dos vértices](#vertex-colors) | ✅ | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR dos vértices](#pbr-paint)  | ✅     | Nomad ✅<br>Outros ⚠️ | ❌  | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Outros ⚠️ | ✅  | ✅ | ✅    | ❌    | ✅                     |
| [Camadas](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objetos                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Grupo de faces                  | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarquia                      | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Luzes                           | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texturas                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitivas, pós-processamento etc. | ✅  | Nomad ✅<br>Outros ❌ | ❌  | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Botão Exportar {#export-button}
Toque nele para exportar a geometria com os ajustes selecionados. O botão mostra o formato escolhido e uma estimativa do tamanho do arquivo. No Android, um botão `Compartilhar` ao lado envia o arquivo direto para outro aplicativo.

### Formato do arquivo {#file-format}
Escolha o formato de exportação: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` ou `USD`. NOMAD é o formato próprio do Nomad e não abre em outros programas, então serve principalmente para reimportar no Nomad.

### Incluir {#allvisibleselected}
Escolha quais objetos serão exportados: `Todos`, `Visível` ou `Selecionados`. O número ao lado de cada opção mostra quantos objetos serão exportados.

### Um arquivo por objeto {#one-file-per-object}
Exporta cada objeto em um arquivo separado. O número mostra quantos arquivos serão gravados.

### Tipo {#type}
Quando a exportação gera vários arquivos (um arquivo por objeto, ou OBJ com texturas), salve-os em uma `Pasta` ou em um `Zip`. Alguns aplicativos (Google Drive, One Drive etc.) não aceitam importar pastas, então você pode usar o Zip no lugar.

### Incorporar histórico {#embed-history}
Só no NOMAD. Inclui o histórico de desfazer no arquivo, e ele é restaurado quando o arquivo é aberto no Nomad. Isso aumenta o tamanho do arquivo e exige que a cena inteira seja exportada como um único arquivo.

### Incorporar recursos {#embed-assets}
Só no NOMAD. Inclui no arquivo os seus matcaps, ambientes e fontes personalizados. Os recursos incluídos no app não são incorporados.

### Cores dos vértices {#vertex-colors}
Exporta as cores dos vértices, se o formato do arquivo aceitar. Alguns programas 3d conseguem lê-las, mas não todos.

No OBJ, você pode escolher:
* `Nenhum` - sem cores.
* `RGB` - as cores são adicionadas depois dos vértices.
* `MRGB (ZBrush)` - outra forma de codificar a cor, que também aceita os dados de máscara.

### Espaço de cor {#color-space-export}
Só no OBJ, com cores de vértices `RGB`. Grava as cores em `Linear` ou `sRGB`.

### Pintura PBR {#pbr-paint}
Exporta a pintura de aspereza, de metalidade e de máscara. Outros programas podem ignorar esses dados.
As cores PBR dos vértices são exportadas como atributos secundários de cor de vértice.
Os canais são organizados assim:

|           | Canal    |
| :-------: | :------: |
| Aspereza  | R        |
| Metalidade | G       |
| Máscara   | B        |


### Camadas {#layers}
As camadas são exportadas como morph targets do glTF. Isso faz parte oficialmente do glTF, então deve funcionar também em outros programas.
O Nomad também exporta as cores, a aspereza e a metalidade de cada camada, mas outros programas vão ignorá-las.

### Pintura da camada {#layer-painting}
Exporta a pintura das camadas, que geralmente é ignorada por outros programas.

### Grupo de faces {#face-group}
Exporta os grupos de faces. Às vezes isso pode causar problemas em outros programas.

### Escrever objetos {#write-objects}
Só no OBJ. Mantém os objetos separados. Desative para exportar tudo como um único objeto, por exemplo para usar o recurso "Mesh ID / Polygroup" do Substance Painter.

### Normais {#normals}
Exporta as informações de normais. Note que o Nomad sempre calcula as suas próprias normais ao importar outros formatos de arquivo.

### Tangentes {#tangents}
Exporta as informações de tangentes, usadas quando o modelo tem mapas de normais.

### Texturas {#textures}
Se houver texturas adicionadas ao material, elas são exportadas. Note que isso não faz o bake das texturas: isso é feito pelas opções de bake do menu Topologia.

### Formato {#fbx-format}
Só no FBX. `Binário` é menor, mas pode não funcionar em todos os aplicativos; `ASCII` é um arquivo de texto.

### Compactado {#compressed}
Só no FBX. Reduz o tamanho do arquivo, mas deixa a exportação e a importação mais lentas.

### Pré‑ajuste {#usd-preset}
Só no USD. Escolha o aplicativo para o qual você está exportando: `OpenUSD`, `Apple`, `Procreate` ou `Zbrush`. Algumas opções só existem em alguns pré‑ajustes.

### Instância {#instance}
Só no USD. Exporta os objetos instanciados como instâncias, em vez de duplicar a geometria deles.

### Permitir inclinação {#allow-skew}
Só no USD. Permite inclinação nas transformações das matrizes. Quando desativado, o Nomad divide as transformações inclinadas em transformações separadas de escala e de rotação.

### Repetidor {#repeater}
Só no USD. Exporta as cópias feitas pelos repetidores como instâncias.

### Unir cópias {#join-copies}
Cada objeto e as cópias do seu repetidor viram um único objeto.

::: tip Dica: importar a aspereza e a metalidade no Blender

O Blender importa glTF/glb, mas não entende sozinho os atributos de vértice de metalidade e aspereza. Para usá-los, crie um nó Vertex Color no editor de materiais e defina a propriedade dele para o atributo de cor seguinte (geralmente Col.001). Ligue um nó "Separate XYZ" e mande o X para Roughness e o Y para Metallic.

Este vídeo mostra o processo:

![](/videos/blender_pbr.mp4)

::: 

::: tip Dica: recursos aceitos no USD

O USD é um formato complexo: a especificação dele prevê muitos recursos, mas nem todos os programas 3d os aceitam. O OSX/iOS não aceita cores de vértices, por exemplo. Os pré‑ajustes do exportador USD tentam chegar à melhor compatibilidade possível com OpenUSD, Apple, Procreate e Zbrush.

::: 

## ![](/icons/screen.webp) Renderizar {#render}

Exporta uma imagem que combina todos os ajustes do projeto (luzes, materiais, pós-processamento etc.).

![](/images/file_render.webp)
### ![](/icons/preview.webp) Pré‑visualização {#preview}

O botão `Pré‑visualização` ao lado do título do menu deixa a interface transparente, para ajudar a conferir o enquadramento do resultado final.

### ![](/icons/home.webp) Foco {#focus}
Enquadra a cena ou a seleção para caber no tamanho da renderização. Toque de novo para alternar entre as duas.

### ![](/icons/map.webp) Mapa de altura {#heightmap}
Renderiza a cena como um mapa de altura em tons de cinza visto da câmera, com as partes mais próximas mais claras. Ativá-lo passa para o tamanho `Quadrado` e enquadra a seleção. Uma pequena barra na vista permite ajustar o `Foco` do gradiente.

Com o `Mapa de altura` ligado, um botão `Salvar como alfa` aparece ao lado do botão de exportação, para salvar a renderização como um novo alfa de pincel em vez de exportar um arquivo.

### ![](/icons/opacity.webp) Fundo transparente {#transparent-background}
Ativa um canal alfa na renderização, útil para combiná-la com outras imagens em programas 2d. Note que a transparência parcial não é suportada.

### ![](/icons/sliders.webp) Mostrar interface {#show-interface}
Inclui a interface do Nomad na renderização.

### Tamanho final {#final-size}
A resolução da renderização: `Tela`, `720`, `1080`, `4096`, `Quadrado` ou `Personalizado`.

Com o menu Arquivo aberto, um contorno tracejado aparece na vista para indicar a região da renderização, se ela não corresponder à resolução da tela.

### Largura / Altura {#render-ratio}
Com `Personalizado`, defina a largura e a altura da imagem. O botão de vínculo entre os dois controles mantém a proporção quando você altera um deles. Com `Quadrado`, só a largura pode ser definida.

### ![](/icons/export.webp) Exportar → PNG {#export-png}
Toque neste botão para começar a renderização. Quando ela terminar, você escolhe como salvar ou compartilhar a imagem. Tamanhos muito grandes pedem uma confirmação antes: salve o seu projeto primeiro, caso o aparelho fique sem memória.

## ![](/icons/network.webp) Vincular {#link}

Conecta o Nomad a outro aparelho ou aplicativo, para enviar e receber objetos ou sincronizar as suas edições ao vivo. Um aparelho hospeda a sessão, e os outros entram nela.

### Ativar GoZ {#enable-goz}
Só no computador. Troca malhas com o ZBrush no mesmo computador. `Enviar` as importa no ZBrush, `Obter` importa do ZBrush aberto: `Seleção` pega a subtool ativa, `Cena` pega todas as subtools. Você também pode apertar GoZ no ZBrush a qualquer momento.

### Modo {#link-mode}
* `Desativado` - sem vínculo.
* `Host` - este aparelho hospeda a sessão e espera os outros entrarem.
* `Entrar` - procura os aparelhos próximos; depois, toque no nome do host para entrar.

Para conectar dois Nomad, escolha `Host` em um aparelho e `Entrar` nos outros. Para conectar ao Blender, o Nomad deve ser o host: o botão de ajuda ao lado do título `Vincular` mostra como instalar a extensão Nomad Blender Link.

### ![](/icons/network.webp) Porta de rede {#network-port}
A porta de rede usada pelo vínculo. Só a altere se outro aplicativo já estiver usando essa porta.

### Enviar / Obter {#send-get}
Depois de conectado, use `Enviar` para mandar a sua `Seleção` ou a `Cena` inteira para o outro aparelho, ou `Obter` para recebê-las dele. `Substituir` apaga a cena atual e depois obtém a cena do outro aparelho.

### ![](/icons/link.webp) Sincronização ao vivo {#live-sync}
Transmite as suas edições para o outro aparelho enquanto você trabalha. `Vista de trabalho` também sincroniza a câmera. `Edições da cena` define qual aparelho envia as edições: `Auto` dá a direção ao aparelho com a atividade mais recente. Depois, escolha o que é sincronizado: `Objetos e geometria`, `Materiais`, `Luzes`, `Câmeras` e, quando o outro lado aceitar, `Sombreamento` e `Pós-processamento`.

::: tip
Os objetos que já existem precisam de um `Enviar` ou `Obter` antes, para ficarem vinculados e a sincronização ao vivo poder atualizá-los.
:::

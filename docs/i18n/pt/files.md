# ![](/icons/open.webp) Arquivos {#files}

O menu Arquivos permite salvar e carregar projetos do Nomad, importar e exportar modelos 3D e exportar imagens renderizadas.

![](/images/file_menu.webp)

## Projeto {#project}
![](/images/file_project.webp)

Uma miniatura da última gravação é exibida na parte superior deste menu. Clicar nessa miniatura abre um mini navegador; toque duas vezes em outro projeto para abrir um mini menu com as opções de abrir, adicionar, salvar, clonar, renomear ou excluir esse projeto.

### ![](/icons/nomad.webp) Predefinição {#preset}
Acesse uma coleção de demos e componentes de personagens. Selecione um, depois selecione novamente para escolher Abrir, Adicionar à Cena ou Clonar a entrada para a sua pasta de projetos.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Salvar {#save}
Salva o projeto do Nomad.

### ![](/icons/save_as.webp) Salvar como... {#save-as}
Exibe o navegador de projetos para permitir salvar o projeto do Nomad com um novo nome.

### ![](/icons/pencil.webp) Renomear {#rename}
Exibe uma caixa de texto para renomear o projeto atual.

### ![](/icons/open.webp) Abrir... {#open}
Exibe o navegador de projetos para abrir um projeto.

### ![](/icons/add_file.webp) Adicionar à cena... {#add}
Exibe o navegador de projetos; quando um projeto é selecionado, seu conteúdo será mesclado com a cena atual.

### ![](/icons/trash.webp) Excluir... {#delete}
Exibe o navegador de projetos; quaisquer projetos selecionados serão excluídos do sistema de arquivos.

### ![](/icons/new_file.webp) Novo {#new}
Inicia um novo projeto; se houver alterações não salvas, será perguntado se você deseja salvar.

### ![](/icons/autosave.webp) Salvamento automático... {#auto-save}
Menu para controlar as opções de salvamento automático.

Se você ativar o salvamento automático, poderá configurar um temporizador para que um pop-up apareça em intervalos regulares.
O motivo pelo qual o Nomad não salva em segundo plano é que arquivos 3D podem ser bem grandes, o que pode causar uma latência significativa enquanto você está esculpindo.

Além disso, para evitar problemas de falta de memória, a cena normalmente é compactada antes da operação de salvamento.
Essa compactação/descompactação também tornará a operação de salvamento mais lenta.

### Timer pop up {#timer-pop-up}
Com que frequência o pop-up do temporizador aparecerá.

### Tempo limite do pop‑up {#popup-timeout}
Ativar tempo limite do pop-up.

### Descartar salvamento automático {#discard-autosave}
Se existir um arquivo de salvamento automático para um projeto, ele será carregado automaticamente em vez do projeto original. Se isso não for necessário, este botão excluirá o salvamento automático. Carregar o arquivo então carregará o último salvamento manual do projeto.


## Importar {#import}

### ![](/icons/add_file.webp) Importar {#import-button}
Para importar arquivos 3D que não são projetos do Nomad.

Ao importar um arquivo de cena externa para o Nomad, você pode *importar* ou *adicionar*.

Adicionar um arquivo simplesmente adicionará os objetos à cena atual.
Importar um arquivo criará um novo projeto do Nomad com os novos objetos nele.

O Nomad pode importar estes formatos:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimental)

### ![](/icons/cog.webp) Avançado {#advanced}
Exibe opções avançadas de importação:

### Projeto/ glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### Manter topologia {#keep-topology}
Por padrão, o Nomad tentará corrigir geometrias problemáticas ao carregar. Ativar isto impedirá o Nomad de reordenar vértices/faces, remover vértices/faces duplicados e remover vértices não utilizados.

#### Ignorar texturas {#skip-textures}
Ignora o carregamento de texturas para formatos que as suportam, como glTF.

### Projeto / glTF {#project-gltf}
#### Manter configurações da interface {#keep-gui-settings}
Ativa o salvamento da interface gráfica e das configurações do projeto dentro do arquivo .nom do Nomad ou do arquivo glTF.

### OBJ {#obj}
#### Dividir OBJ por grupos {#split-obj-by-groups}
Ativa a divisão de grupos OBJ em objetos separados.

#### Espaço de cor {#color-space}
Define o modo de cor interpretado a partir do OBJ como Linear, sRGB ou Automático.

### PLY {#ply}
#### Espaço de cor {#color-space-ply}
Define o modo de cor interpretado a partir do PLY como Linear, sRGB ou Automático.


### FBX {#fbx}
#### Espaço de cor {#color-space-fbx}
Define o modo de cor interpretado a partir do OBJ como Linear, sRGB ou Automático.



## Exportar {#export}
Salva em um formato de geometria 3D que pode ser usado em outros softwares. 

![](/images/file_export.webp)

Diferentes formatos de arquivo suportam recursos diferentes; as opções disponíveis mudarão com base no tipo de arquivo selecionado.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Tudo/Visível/Selecionado {#allvisibleselected}
O estado ativo do botão define quais objetos serão exportados. O número ao lado dos ícones indica quantos objetos serão exportados para essa opção.

### Cores de vértice {#vertex-colors}
Exporta cores de vértice se forem suportadas pelo formato de arquivo.

### PBR Paint {#pbr-paint}
As cores de vértice PBR são exportadas como atributos secundários de cores de vértice.
Os canais são organizados da seguinte forma:

|           | Canal   |
| :-------: | :-----: |
| Rugosidade | R      |
| Metalicidade | G    |
| Masking   | B       |


### Camadas {#layers}
Camadas são suportadas por meio de morph targets do glTF.
O Nomad também exporta cores, rugosidade e metalicidade por camada, mas isso será ignorado por outros softwares.

### Pintura em camadas {#layer-painting}
Exporta pintura de camada, geralmente ignorada por outros softwares.

### Grupo de faces {#face-group}
Exporta facegroups; a exportação às vezes pode interferir com outros softwares.

### Normais {#normals}
Exporta informações de normais. Observe que o Nomad sempre calculará suas próprias normais ao importar outros formatos de arquivo.

### Tangentes {#tangents}
Exporta informações de tangentes, usadas se o modelo tiver mapas de normais. 

### Texturas {#textures}
Se texturas tiverem sido adicionadas ao material, elas serão exportadas. Observe que isso não fará bake das texturas; isso é feito pelas opções de bake em topologia.

### Botão Exportar {#export-button}
Clique aqui para exportar a geometria usando as configurações selecionadas.

::: tip Dica: importar rugosidade e metalicidade para o Blender

O Blender pode importar glTF/glb, mas não entende automaticamente atributos de vértice para metalicidade e rugosidade. Para usá-los, no editor de materiais crie um nó Vertex Color, defina sua propriedade para o próximo atributo de cor (geralmente Col.001). Conecte um nó 'Separate XYZ', envie X para Roughness e Y para Metallic.

Este vídeo mostra o processo:

![](/videos/blender_pbr.mp4)

::: 

::: tip Dica: suporte a recursos USD

USD é um formato complexo; sua especificação suporta muitos recursos, mas nem todos os softwares 3D os suportarão. macOS/iOS, por exemplo, não suportam cor de vértice. Os modos predefinidos dentro do exportador USD tentam uma melhor estimativa de compatibilidade com OpenUSD, Apple, Procreate e ZBrush.

::: 

## Renderizar {#render}

Exporta uma imagem que é a combinação de todas as configurações do projeto (luzes, materiais, pós-processamento etc). 

![](/images/file_render.webp)
### Pré-visualização {#preview}

O pequeno botão de pré-visualização ao lado do título do menu escurece as barras de ferramentas para ajudar a pré-visualizar o resultado final.

### Fundo transparente {#transparent-background}
Ativa um canal alfa para o render, útil para combinar o render com outras imagens em programas 2D. Observe que transparência parcial não é suportada.

### Mostrar interface {#show-interface}
Ativa a inclusão da interface do Nomad no render.

### Proporção de renderização {#render-ratio}
Um multiplicador na resolução da imagem.

### Tamanho final {#final-size}
A resolução a ser usada para o render. Quando `Custom` é selecionado, os controles deslizantes de largura e altura serão ativados. 

Quando o menu Arquivos está ativo, uma sobreposição tracejada será desenhada na viewport para indicar a região de render se ela não corresponder à resolução da tela (observe que você deve estar no modo paisagem para que isso esteja correto).

### Exportar PNG {#export-png}
Clique neste botão para iniciar o processo de renderização. Quando concluído, você poderá escolher como salvar ou compartilhar a imagem.
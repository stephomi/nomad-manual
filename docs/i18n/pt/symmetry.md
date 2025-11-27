# ![](/icons/symmetry.webp) Simetria

Este menu controla como os traços serão repetidos através de um plano espelhado ou radialmente, e maneiras de restaurar a simetria em objetos não simétricos.

![](/images/symmetry_overview.webp) 

## Visão geral 
Você pode usar simetria de várias maneiras:

* Como um espelho, invertendo o trabalho nos eixos X (esquerda/direita), Y (topo/base), Z (trás/frente), ou uma combinação deles. 
* A simetria radial pode ser definida em X Y Z com um número de repetições, por exemplo, esculpir uma estrela-do-mar. 
* Espelhos podem operar em torno da origem (chamado modo mundo) ou em torno do centro de um objeto (chamado modo local).
* Esculturas que começaram não simétricas podem ser forçadas a se tornarem simétricas.

Um atalho para ativar/desativar a simetria também pode ser encontrado no painel rápido à esquerda (*"Sym"*). O pequeno 'L/W' indica se o Nomad está em modo de simetria Local ou Mundo. Você também pode pressionar e segurar ou deslizar para o centro da tela para abrir um menu.

![](/images/symmetry_button.webp) 

Esta é uma opção global, então o estado será mantido entre as diferentes ferramentas.
As únicas exceções são as ferramentas de transformação ([Mover](#translate), [Rotacionar](#rotate), [Escalar](#scale) e [Gizmo](#gizmo)) que têm seu próprio estado de simetria.

::: tip
O menu de simetria é principalmente para controlar a simetria de traços. Você também pode espelhar e repetir objetos via [repetidores encontrados no menu de cena](scene#repeaters). 
:::

## Ativado
Alterna o modo espelho, é o mesmo que o botão `Sym` no painel rápido à esquerda. 

## Planos

Ativa plano(s) de simetria e o número de repetições para simetria radial. Note que você não precisa escolher apenas um único plano; pode ter 1, 2 ou 3 planos ativados para simetrias complexas.

O eixo e a contagem de repetições para a simetria radial. Note que estes também não são restritos a um único eixo, e podem até funcionar em combinação com a simetria de plano para gerar resultados detalhados muito rapidamente. (O número total de repetições é limitado a 150)

![](/videos/symmetry_demo.mp4) 

## Método
O espelho pode ser 'Local', movendo-se com o objeto, ou 'Mundo', permanecendo fixo. Se você não tiver certeza de qual modo precisa, observe o plano de espelho e os indicadores radiais sobrepostos ao objeto. Quando em modo local, se você usar o gizmo de transformação e mover o modelo, os indicadores de espelho também se moverão. Quando em modo mundo, os indicadores de espelho permanecerão fixos, e o objeto deslizará através deles.

## Espelhamento
![](/images/symmetry_mirroring.webp)

Ao esculpir perto dos planos de simetria, alguns pincéis terão um comportamento de simetria imperfeito. Esta seção permite restaurar a simetria copiando um lado da sua escultura para o outro. 

`Direction` - Os botões `<<` e `>>` determinam qual lado será copiado para o outro. O Nomad calcula isso a partir da sua viewport atual, então, por exemplo, definir para `<<` sempre copiará da direita da tela para a esquerda da tela.

![](/icons/shield.webp) `Mask` - O botão de máscara permite isolar o que será espelhado; mascarar o lado de destino protegerá essa região, mascarar o lado de origem impedirá que essa área seja espelhada para o destino. 

![](/icons/tool_hide.webp) `Hide` - Quando ativo, áreas que estiverem ocultas no lado de origem não serão espelhadas para o destino. 

`Mirror` tentará identificar se a topologia é a mesma em ambos os lados do espelho e, se for, apenas moverá vértices. Este é o cenário mais comum.

`Split & Mirror` basicamente cortará o objeto ao longo do espelho, copiará um lado, o espelhará para o outro e soldará os vértices ao longo do espelho. É uma opção mais destrutiva e apagará multirresolução, mas às vezes esse método é necessário se o modelo for muito diferente através do espelho.

### Inverter objeto
![](/images/symmetry_flip.webp)
Faz o lado esquerdo virar o lado direito, e vice-versa. Similar, em aparência, a usar o menu da ferramenta gizmo e definir a escala para -1 em X.

## Redefinir e Editar

![](/images/symmetry_edit.webp)

É possível editar a localização e a orientação da simetria (mas não é recomendado!). Se necessário, `World center` e `Orientation` redefinirão a localização e a orientação da simetria para seus valores padrão.

O Nomad geralmente sabe onde colocar o plano de simetria. Não é recomendado ajustar isso manualmente, mas o botão `Gizmo (Edit)` permite isso para usuários avançados. Quando este botão é clicado, um gizmo é exibido para permitir que você traduza e rotacione o plano de simetria. Se quiser restaurar o centro e a orientação padrão, os botões `object center` e `orientation` farão isso.

O comportamento dessas opções mudará dependendo de em qual espaço (*Local/Mundo*) você está.
Portanto, se não funcionar como você espera, verifique se está no espaço correto.

::: tip
O botão `Gizmo (Edit)` é propositalmente esmaecido como um lembrete de que você provavelmente não deveria usá-lo!
:::

## Opções de exibição
![](/images/symmetry_show.webp)


`Show line` e `Show plane` alternarão uma sobreposição no viewport das localizações de simetria. Note que desativar essas opções só terá efeito quando o menu de simetria for fechado.

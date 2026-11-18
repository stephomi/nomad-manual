# ![](/icons/symmetry.webp) Simetria {#symmetry}

Este menu controla como os traços são repetidos em relação a um plano de espelho, radialmente ou em ladrilhos, e oferece maneiras de restaurar a simetria em objetos não simétricos.

![](/images/symmetry_overview.webp) 

## Visão geral {#overview}
Você pode usar a simetria de várias formas:

* Como espelho, refletindo o trabalho em X (esquerda/direita), Y (cima/baixo), Z (trás/frente) ou numa combinação deles.
* A simetria radial pode ser definida em X, Y e Z com um número de repetições, por exemplo para esculpir uma estrela-do-mar.
* O ladrilhamento repete seus traços ao longo do objeto, para que a escultura se repita sem emendas.
* Os espelhos podem funcionar em torno da origem (modo mundo) ou em torno do centro de um objeto (modo local).
* Esculturas que começaram sem simetria podem ser forçadas a ficar simétricas.

Também há um atalho para ativar/desativar a simetria no painel rápido à esquerda (*"Simetria"*). O pequeno 'L/W' indica se o Nomad está no modo de simetria Local ou Mundo. Você também pode tocar longamente ou deslizar em direção ao centro da tela para abrir um menu.

![](/images/symmetry_button.webp) 

Os ajustes de simetria são salvos em cada objeto, e o título do menu mostra o nome do objeto que você está editando.
As ferramentas de escultura compartilham o mesmo estado ligado/desligado, enquanto as ferramentas de transformação ([Transformar](tools.md#transform) e [Gizmo](tools.md#gizmo)) têm o seu próprio.

::: tip
O menu de simetria serve principalmente para controlar a simetria dos traços. Você também pode espelhar e repetir objetos com os [repetidores do menu Cena](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Ativada {#enabled}
Ativa ou desativa o modo espelho, igual ao botão `Simetria` do painel rápido à esquerda. Um ícone de aviso lembra quando ela está desligada, e o menu também avisa quando a ferramenta atual ignora a simetria.

## Planos {#planes}

Ative os planos de simetria e o número de repetições da simetria radial. Você não precisa escolher um único plano: pode ativar 1, 2 ou os 3 planos para uma simetria complexa.

A linha `Radial` define o número de repetições da simetria radial em torno de cada eixo. Ela também não se limita a um único eixo, e pode até ser combinada com a simetria por planos para gerar resultados detalhados muito rapidamente. (O total de repetições é limitado a 200.)

![](/videos/symmetry_demo.mp4) 

## Ladrilho {#tile}

Repete seus traços ao longo de um eixo, a uma distância regular, para que a escultura se repita sem emendas. Prático para padrões, tijolos ou uma textura que você pretende repetir.

Ative o ladrilhamento em cada eixo com os botões `Ladrilho` e depois defina uma `Contagem` (quantas repetições cobrem o objeto) ou uma `Distância` (o espaço entre duas repetições). Toque no seletor à esquerda para alternar entre as duas.

## Método {#method}
O espelho pode ser `Local`, movendo-se junto com o objeto, ou `Mundo`, ficando parado. Se não tiver certeza de qual modo precisa, observe os indicadores do plano de espelho e radiais sobrepostos ao objeto. No modo local, se você usar as ferramentas de transformação (`Gizmo` ou `Transformar`) e mover o modelo, os indicadores do espelho se movem também. No modo mundo, os indicadores ficam parados e o objeto desliza através deles.

## Espelho {#mirroring}
![](/images/symmetry_mirroring.webp)

Ao esculpir perto dos planos de simetria, alguns pincéis podem não respeitar a simetria perfeitamente. Esta seção permite restaurar a simetria copiando um lado da escultura para o outro.

`Direção` - Os dois botões de seta ao lado do título `Espelho` determinam qual lado será copiado para o outro. O Nomad calcula isso a partir do visor atual, então o lado continua o mesmo na tela, seja qual for o ângulo de onde você olha o modelo.

![](/icons/shield.webp) `Máscara` - O botão de máscara permite isolar o que será espelhado: mascarar o lado de destino protege essa região, e mascarar o lado de origem impede que essa área seja espelhada no destino.

![](/icons/tool_hide.webp) `Ocultar` - Quando ativo, as áreas ocultas do lado de origem não são espelhadas no destino.

`Espelho` (Manter topologia) tenta identificar se a topologia é a mesma dos dois lados do espelho e, nesse caso, apenas move os vértices. Esse é o cenário mais comum. A simetria radial é ignorada. Se a topologia não for simétrica, o Nomad oferece forçar o espelhamento com `Cortar • Espelho`.

Os botões `Cortar` cortam o objeto ao longo do(s) plano(s) de simetria. Eles alteram a topologia, então são mais destrutivos que `Espelho`. O número em cada botão indica quantos objetos você obtém:

* `Cortar` - remove um lado do objeto.
* `Cortar • Espelho` - corta o objeto, copia um lado, espelha esse lado no outro e solda os vértices ao longo do espelho. Às vezes esse método é necessário quando o modelo é muito diferente de um lado para o outro.
* `Cortar • Dividir` - corta o objeto e mantém cada lado como um objeto separado.
* `Cortar • Espelho • Dividir` - como `Cortar • Espelho`, mas cada lado vira um objeto separado.

Se vários objetos estiverem selecionados, `Espelho` e [Virar objeto](#flip-object) se aplicam a todos eles.

### Virar objeto {#flip-object}
![](/images/symmetry_flip.webp)
Troca o lado esquerdo pelo direito, e vice-versa, ao longo de `X`, `Y` ou `Z`. O resultado é parecido com usar o menu da ferramenta gizmo e definir a escala como -1 em X.

## Redefinir e editar {#reset-and-edit}

![](/images/symmetry_edit.webp)

É possível editar a posição e a orientação da simetria (mas não é recomendado!). Se precisar, `Centro do mundo` (`Centro do objeto` no modo local) e `Orientação` redefinem a posição e a orientação da simetria para os valores padrão.

O Nomad normalmente sabe onde colocar o plano de simetria. Não é recomendado ajustá-lo manualmente, mas o botão `Editar Gizmo` permite isso para usuários avançados. Ao clicar nesse botão, aparece um gizmo para mover e girar o plano de simetria. Se quiser restaurar o centro e a orientação padrão, use os botões de redefinição acima.

`Do pivô` coloca o plano de simetria no pivô da ferramenta [Gizmo](tools.md#gizmo). Só está disponível enquanto a ferramenta `Gizmo` estiver ativa.

O comportamento dessas opções muda conforme o espaço (*Local/Mundo*) em que você está.
Então, se não funcionar como esperado, verifique se você está no espaço certo.

::: tip
Editar o plano de simetria com o gizmo é um recurso um pouco experimental, você provavelmente não vai precisar dele!
:::

## Opções de exibição {#show-options}
![](/images/symmetry_show.webp)


`Mostrar linha` e `Mostrar plano` mostram ou ocultam no visor uma sobreposição com as posições da simetria. Desligar essas opções só tem efeito quando o menu de simetria é fechado.

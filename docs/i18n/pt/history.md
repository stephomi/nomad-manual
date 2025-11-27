# ![](/icons/history.webp) Histórico
![](/images/history_overview.webp)

Como na maioria das ferramentas de criação de conteúdo, você pode desfazer/refazer todas as edições no Nomad.
Há um limite para quantas operações podem ser desfeitas, mas você pode controlar esse comportamento.

::: tip
Você pode usar gestos rápidos para desfazer/refazer:
- Toque com 2 dedos para desfazer
- Toque com 3 dedos para refazer
:::

## Histórico
![](/images/history_history.webp)

Este painel exibe a pilha de histórico, mostrando o número de etapas, o nome da operação e a quantidade de memória que essa etapa está usando.

## Configurações
![](/images/history_settings.webp)

### Limite de histórico (Mb)
Se a pilha de histórico exceder esse valor, as operações mais antigas serão removidas para que o orçamento de memória se encaixe nesse limite.


### Máximo de desfazer
Você pode controlar o número máximo de operações.

## Restaurar câmera
Para cada operação, o ponto de vista da câmera é salvo.
Se você ativar esta opção, desfazer ou refazer uma operação irá redefinir a câmera para o ponto de vista salvo.

## Incluir ações

* `Luzes` - Quando desativado, operações de luz (exceto movimentos de gizmo) serão ignoradas pela pilha de histórico
* `Matcaps & HDRIs` - Quando desativado, alterações em matcaps e HDRIs serão ignoradas pela pilha de histórico
* `Pós-processo` - Quando desativado, alterações nas opções de pós-processo serão ignoradas pela pilha de histórico

## Estatísticas de memória

Esta seção fornece uma análise da memória usada pelo Nomad.

# Codlogs - Revisoes de Modelagem

## Inconsistencias identificadas na documentacao da V1.0

Este arquivo registra pontos de inconsistencia encontrados entre os documentos de requisitos, modelagem de dominio, modelo relacional e os modelos iniciais do projeto.

A intencao desta lista nao e corrigir automaticamente a modelagem, mas servir como material de revisao para entender cada decisao antes de alterar a documentacao.

### 1. Relacionamento entre Sale, SaleItem e SalePayment

Em `Modelagem do Dominio`, `Sale` possui `sale_item_id` e `sale_payment_id`.

No modelo relacional, porem, quem deve apontar para `Sale` sao `SaleItem` e `SalePayment`.

Conceitualmente, uma venda possui varios itens e varios pagamentos. Portanto, a chave estrangeira deve estar nas tabelas filhas:

- `SALE_ITEM.sale_id`
- `SALE_PAYMENT.sale_id`

### 2. Inconsistencia entre `sell_date` e `sale_date`

Em `Modelagem do Dominio`, aparece `sell_date`.

Em `Modelo Relacional`, aparece `sale_date`.

E melhor escolher um unico padrao. A sugestao e usar `sale_date`, pois `sale` e o substantivo da entidade e combina melhor com o restante da nomenclatura.

### 3. Inconsistencia no identificador de SalePayment

Em `Modelagem do Dominio`, aparece `sale_payment_id`.

Em `Modelo Relacional`, aparece `payment_item_id`.

Esses nomes representam a mesma entidade, entao devem ser padronizados. A sugestao e usar `sale_payment_id`.

### 4. Erro de nomenclatura em `sell_id`

Em `Modelo Relacional`, `SALE_PAYMENT` possui `sell_id`.

O correto seria `sale_id`, mantendo consistencia com a entidade `SALE`.

### 5. Categoria existe no dominio, mas nao no relacional

Em `Modelagem do Dominio`, `Product` possui `product_category`.

Em `Modelo Relacional`, `PRODUCT` nao possui campo de categoria.

Isso gera conflito com os requisitos, pois existe a funcionalidade de filtrar produtos por categoria.

### 6. Requisito de filtro por categoria sem suporte no banco

Em `Levantamento de Requisitos`, existe o requisito de filtrar por categorias.

Para esse requisito ser possivel, o modelo precisa ter uma forma de representar categoria, seja como:

- campo simples em `PRODUCT`, por exemplo `category`;
- tabela separada, por exemplo `PRODUCT_CATEGORY`.

Para V1.0, um campo simples pode ser suficiente.

### 7. Saida manual exige motivo, mas Movement nao possui campo para isso

A regra `RNGE03` diz que saidas manuais devem registrar motivo.

No modelo relacional, `MOVEMENT` nao possui campo como:

- `reason`;
- `description`;
- `note`;
- `observation`.

Sem esse campo, a regra de negocio nao pode ser persistida corretamente.

### 8. Remover produto precisa de regra mais clara

Em requisitos, existe a funcionalidade `Remover Produto`.

Em sistemas com vendas e historico de estoque, remover fisicamente um produto pode quebrar o historico.

E preciso decidir se remover significa:

- exclusao fisica do registro;
- inativacao do produto com um campo como `is_active`.

Para preservar historico, a inativacao tende a ser mais segura.

### 9. Desconto ainda nao tem local conceitual definido

A regra `RNGV04` diz que descontos serao em dinheiro, nao em porcentagem.

Porem, ainda nao esta claro se o desconto pertence:

- a venda inteira;
- a cada item da venda;
- aos dois casos.

Essa decisao impacta diretamente `SALE`, `SALE_ITEM` e o calculo do total.

### 10. Desconto aparece em lugares diferentes

No modelo relacional, `discount` aparece em `SALE_ITEM`.

No codigo atual, `Sale` tambem possui `discount`.

Isso representa duas interpretacoes diferentes:

- desconto por item;
- desconto geral da venda.

Para V1.0, pode ser mais simples usar desconto geral na venda.

### 11. Titulo de relacionamento entre venda e pagamento esta impreciso

Em `Modelagem do Dominio`, existe o titulo `Toda Venda contem Pagamento`.

Logo abaixo, porem, a explicacao fala sobre `Item_Venda`.

Esse trecho mistura dois relacionamentos diferentes:

- `Sale` com `SaleItem`;
- `Sale` com `SalePayment`.

O ideal e separar esses dois blocos.

### 12. Frase sobre formas de pagamento esta conceitualmente imprecisa

A frase `Todo pagamento pode ter uma ou varias formas de pagamento` pode gerar confusao.

Na modelagem atual, o mais correto seria:

- uma venda pode ter varios pagamentos;
- cada pagamento utiliza exatamente um metodo de pagamento;
- um metodo de pagamento pode ser usado em varios pagamentos.

Exemplo:

```text
Venda de R$ 100,00
- R$ 60,00 em PIX
- R$ 40,00 em dinheiro
```

Nesse caso, existem dois `SalePayment`, cada um com um `PaymentMethod`.

### 13. Mistura de portugues e ingles nos nomes das entidades

A maior parte da modelagem usa nomes em ingles, como:

- `Product`;
- `Sale`;
- `PaymentMethod`.

Mas tambem aparecem nomes em portugues, como:

- `Movimentacao`;
- `Item_Movimentacao`;
- `Usuario`.

Para manter consistencia com padroes comuns de codigo, a sugestao e padronizar em ingles:

- `Movement`;
- `MovementItem`;
- `User`.

### 14. `id_produto_movimentacao` parece estar na entidade errada

Em `Modelagem do Dominio`, `Movimentacao` possui `id_produto_movimentacao`.

Porem, uma movimentacao pode ter um ou varios itens. Portanto, o produto movimentado pertence ao item da movimentacao, nao necessariamente a movimentacao principal.

O mais coerente e:

- `Movement` representa o evento;
- `MovementItem` representa os produtos e quantidades movimentados.

### 15. Conflito entre `id_produto_movimentacao` e `movement_item_id`

Em `Modelagem do Dominio`, `Item_Movimentacao` possui `id_produto_movimentacao`.

Em `Modelo Relacional`, a entidade aparece com `movement_item_id`.

`id_produto_movimentacao` parece indicar um produto, enquanto `movement_item_id` identifica o item da movimentacao.

Esses conceitos precisam ser separados:

- `movement_item_id`: identificador do item da movimentacao;
- `product_id`: produto movimentado.

### 16. Nome da tabela `USER` pode ser problematico

No modelo relacional, existe a tabela `USER`.

Em alguns bancos de dados, `user` pode ser palavra reservada ou sensivel.

Alternativas mais seguras:

- `APP_USER`;
- `USERS`;
- `SYSTEM_USER`.

### 17. Permissoes citadas nos requisitos nao estao formalizadas no modelo

Em requisitos, aparecem os perfis:

- Atendimento;
- Tecnico;
- Administrador.

No modelo, existe `user_role`, mas os valores possiveis ainda nao foram definidos formalmente.

Seria interessante documentar uma enum ou lista de papeis permitidos.

### 18. Nomes de atributos de Product variam entre documentos e codigo

Nos documentos e no codigo aparecem variacoes como:

- `product_name`;
- `name`;
- `stock_quantity`;
- `quantity`;
- `value`;
- `sale_price`;
- `buy_price`;
- `cost_price`.

E importante escolher uma linguagem unica para evitar confusao entre:

- preco de custo;
- preco de venda;
- quantidade em estoque.

### 19. Entrada de notas ainda nao esta modelada

Em requisitos, existe `Entrada de Notas`.

Porem, o modelo ainda nao representa informacoes como:

- nota fiscal;
- fornecedor;
- numero da nota;
- data da entrada;
- origem da entrada.

Para V1.0, isso pode ser simplificado como uma movimentacao de entrada, mas essa decisao precisa ficar explicita.

### 20. Lista de compras em PDF nao possui criterio de geracao

Em requisitos, existe `Gerar Lista de Compras em PDF`.

Porem, ainda nao existe regra para decidir quais produtos entram nessa lista.

Possiveis criterios:

- produto abaixo de estoque minimo;
- produto zerado;
- produto com alta quantidade de vendas;
- produto selecionado manualmente.

Sem esse criterio, a funcionalidade ainda nao esta suficientemente modelada.

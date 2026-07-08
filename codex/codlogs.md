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

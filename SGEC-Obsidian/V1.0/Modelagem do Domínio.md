### Entidades e Atributos

**V1.0 - Domínio Atual

- **Product**
	product_id
	product_name
	stock_quantity
	product_category
	cost_price
	sale_price

- **Sale**
	sale_id
	user_id
	sale_date
	total_value

	- **Sale_Item**
		sale_item_id
		product_id
		quantity
		unitary_value
		
	- **Sale_Payment**
		sale_payment_id
		sale_id
		payment_method_id
		value

- **Payment_Method**
		payment_method_id
		payment_method_name
		payment_method_is_active

- **Movimentação**
	id_movimentação
	id_produto_movimentação
	tipo
	usuário

	- **Item_Movimentação**
		id_produto_movimentação
		produto
		quantidade

- **Usuário**
	id_usuário
	nome_usuário
	email_usuário
	senha_usuário
	perfil_usuário

****

### Relacionamentos

**Toda Venda contêm Pagamento**
- Toda venda pode ter um ou vários Item_Venda.
- Todo Item_Venda só pode estar atrelado no máximo a uma Venda

**Todo Pagamento contêm Método de Pagamento**
- Todo pagamento pode ter uma ou várias formas de pagamento.
- Toda forma de pagamento pode estar atrelado a um e vários pagamentos.

**Toda Venda gera Movimentação**
- Toda venda pode gerar uma ou várias movimentações.
- Nem toda movimentação é gerada por uma venda.

**Toda Venda contêm Usuário**
- Toda venda possui no máximo um Usuário responsável.
- Um usuário pode ser responsável por N vendas.

**Toda Movimentação contêm um Item_Movimentação**
- Uma movimentação pode ter um ou vários Item_Movimentação.
- Um Item_Movimentação só pode estar atrelado a no máximo uma movimentação.

**Toda Movimentação contêm um Usuário**
- Uma movimentação só pode ter no máximo um usuário atrelado.
- Um usuário pode estar atrelado a um ou várias movimentações.
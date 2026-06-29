### **Entidades e Atributos**

**V1.0 - Sistema Atual**

- **Produto**
	id_produto
	nome_produto
	quantidade_produto
	categoria_produto
	valor_de_compra
	preço_de_venda

- **Venda**
	id_venda
	id_Item_venda
	id_forma_pagamento
	usuário_responsável
	data_venda
	valor_total

	- **Item_Venda**
		id_item_venda
		produto
		quantidade
		valor_unitário
	- **Forma_Pagamento**
		id_forma_pagamento
		método
		valor

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

**V2.0 - Entidades Futuras**

- **Auditoria_Venda**
	id_auditoria_venda
	id_usuário_responsável
	id_venda
	motivo

- **Auditoria_Movimentação**
	id_auditoria_movimentação
	id_usuário_responsável
	id_movimentação
	motivo

---

### Relacionamentos

**Toda Venda contêm Item_Venda
- Toda venda pode ter um ou vários Item_Venda.
- Todo Item_Venda só pode estar atrelado no máximo a uma Venda

**Toda Venda contêm Forma de Pagamento**
- Toda venda pode ter uma ou várias formas de pagamento.
- Toda forma_de_pagamento pode estar atrelado no máximo a uma venda

**Toda Venda gera Movimentação**
- Toda venda pode gerar uma ou várias movimentações.
- Nem toda movimentação é gerada por uma venda.

**Toda Venda contêm Usuário**
- Toda venda possui no máximo um Usuário responsável.

**Todo Item_Venda está em uma Venda**
- Um Item_Venda pode estar atrelado no máximo a uma venda.

**Toda Movimentação contêm um Item_Movimentação**
- Uma movimentação pode ter um ou vários Item_Movimentação.
- Um Item_Movimentação só pode estar atrelado a no máximo uma movimentação.

Toda Movimentação contêm um Usuário
- Uma movimentação só pode ter no máximo um usuário atrelado.
- Um usuário pode estar atrelado a um ou várias movimentações.
## Regras de Negócio

- Toda venda só poderá ser concluída, se caso, o total da venda for igual ao total do pagamento.

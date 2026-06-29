VENDA
-------------------
id_venda (PK)
id_usuario (FK)
data
valor_total

ITEM_VENDA
-------------------
id_item_venda (PK)
id_venda (FK)
id_produto (FK)
quantidade
preco_unitario
desconto

FORMA_PAGAMENTO
-------------------
id_forma_pagamento (PK)
id_venda (FK)
método
valor
PRODUTO
-------------------
id_produto (PK)
nome
preco_compra
preco_venda
quantidade
MOVIMENTAÇÃO
-------------------
id_movimentação (PK)
id_usuário (FK)
tipo
data
ITEM_MOVIMENTAÇÃO
-------------------
id_item_movimentação (PK)
id_movimentação (FK)
id_produto (FK)
quantidade
USUÁRIO
-------------------
id_usuário (PK)
nome_usuário
email_usuário
senha_usuário
perfil_usuário
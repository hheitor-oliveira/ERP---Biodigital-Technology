- #### **O que o sistema precisa fazer?**

	Nesta primeira versão do sistema, seu objetivo é comportar o controle do estoque e de vendas. Permitindo a gestão completa do cadastro de produtos, entradas de notas, saída de produtos, vendas realizadas, entrada monetária, resumos diários/mensais/anuais, e que essa comunicação de entrada e saída através das vendas seja automática. Além disso, ele precisa em todos os processos como movimentações e registros, conseguir registrar o responsável por realizar.

---

- #### **Requisitos funcionais.**
	***V1.0*** - Cadastros, Registro
		**Estoque**
			- Cadastrar Produto
			- Editar Produto
			- Remover Produto
			- Consultar Quantidades
			- Filtrar por Categorias
			- Filtrar por Quantidade de Vendas
			- Entrada de Notas
			- Saída Manual
			- Monitoramento Automático de Quantidades
			- Gerar Lista de Compras em PDF

		**Vendas**
			- Registrar Vendas
			- Consultar Vendas
			- Listar todas as vendas
			- Imprimir extrato de caixa diário
			- Aplicar desconto por valor
			- Aplicar desconto por porcentagem
---

- #### **Requisitos não funcionais.**
	***V1.0*** - Terminal Simples
		**PostgreSQL**: Para garantir eficiência e persistência dos dados.
		Pensando...

---

- #### **Regras de negócio.**
	**Vendas**
	RNGV01 - Uma venda só poderá ser concluída quando o total dos pagamentos for igual ao valor total da venda.
	RNGV02 - Uma venda deverá ser cancelada caso o estoque não permitir a retirada de um produto.
	RNGV03 - Qualquer produto adicionado a uma venda vira com 1 por padrão.
	RNGV04 - Uma venda é iniciada quando é adicionado um produto.
	RNGV05 - Os descontos serão aplicados na venda inteira, não em produtos individualmente.

	**Estoque**
	RNGE01 - Uma movimentação deve ser barrada sempre que a quantidade requisitada não estiver disponível.
	RNGE02 - A quantidade de um produto nunca pode ser negativa.
	RNGE03 - Saídas manuais devem ser registradas o motivo.
	RNGE04 - Os produtos não podem ser excluídos para haver persistência no sistema. Neste caso, apenas desativá-los.

---

- #### **Casos de uso**
	- CRIAR NO ANDAMENTO DO SISTEMA
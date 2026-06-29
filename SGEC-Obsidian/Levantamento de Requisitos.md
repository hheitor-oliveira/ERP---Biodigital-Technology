- #### **O que o sistema precisa fazer?**

	O sistema precisar funcionar como uma **Central**, isso significa que quero que ele centralize módulos como: *Caixa, Estoque, Automações, Monitoramento, etecetera*. Isso dependerá da versão do sistema e o que ele propor desenvolver. E ele precisará haver comunicação interna, ou seja, integração entre esses módulos, mesmo que independentes.

---

- #### **Requisitos funcionais.**
	***V1.0*** - Cadastros, Registro e Interface no Terminal
		**Interface**
			- Painel interativo para escolher entre módulos
			- Painel próprio para cada módulo
			- Break via comando
		**Estoque**
			- Cadastrar Produto
			- Editar Produto
			- Remover Produto
			- Consultar Estoque
		**Caixa**
			- Registrar Venda
			- Consultar Venda
			- Listar todas as vendas

	***V2.0*** - Usuários, Relatórios e Listagem Persistente.
		**Caixa**
			- Relatório persistente do caixa - > Diário, Mensal e Anual
		**Estoque**
			- Relatório do estoque -> Produtos que faltam, Produtos que mais saem
		**Usuários**
			- Login de usuários
			- Cadastro de usuários
			- Hierarquia de Permissões

---

- #### **Requisitos não funcionais.**
	***V1.0*** - Terminal Simples
		**Integração**: Entre os módulos
		**Interface**: Terminal.
		**Persistência**: Nenhuma até o momento.
		**Bibliotecas:** *analisar*.

	***V2.0*** - Aplicação Web, API, Banco de Dados
		**Integração**: API Back-End e Front-End
		**Interface**: Aplicação Web.
		**Persistência**: PostGreeSQL, rodar na nuvem, banco compartilhado.
		**Bibliotecas:** *analisar*.

	***V3.0*** - Adição de novos módulos
		*desenvolvimento*

---

- #### **Regras de negócio.**
	- CRIAR NO ANDAMENTO DO SISTEMA

---

- #### **Casos de uso.**
	- CRIAR NO ANDAMENTO DO SISTEMA
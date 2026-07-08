### Entidades e Atributos

**V1.0 - Domínio Atual

- **Product**
	product_id
	product_name
	stock_quantity
	product_category
	cost_price
	sale_price
	product_status

- **Sale**
	sale_id 
	user_id
	sale_date
	total_value
	sale_discount
	sale_date

	- **SaleItem**
		sale_item_id
		sale_id
		product_id
		quantity
		unitary_value
		
	- **SalePayment**
		sale_payment_id
		sale_id
		payment_method_id
		value

- **PaymentMethod**
		payment_method_id
		payment_method_name
		payment_method_is_active

- **Movement**
	movement_id
	type
	note
	user

	- **MovementItem**
		movement_item_id
		movement_id
		product
		quantity

- **SystemUser**
	user_id
	user_name
	user_email
	password_hash
	role

****

### Relacionamentos


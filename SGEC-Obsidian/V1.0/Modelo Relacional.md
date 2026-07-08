SALE
-------------------
sale_id (PK)
user_id (FK)
total_value
sale_date

SALE_ITEM
-------------------
sale_item_id(PK)
sale_id (FK)
product_id (FK)
quantity
unitary_value
discount

SALE_PAYMENT
-------------------
payment_item_id (PK)
sale_id (FK)
payment_method_id (FK)
value

PAYMENT_METHOD
-------------------
payment_method_id (PK)
name
active
PRODUCT
-------------------
product_id (PK)
name
cost_price
sale_price
stock_quantity
MOVEMENT
-------------------
movement_id (PK)
user_id (FK)
type
movement_date
MOVEMENT_ITEM
-------------------
movement_item_id (PK)
movement_id (FK)
product_id (FK)
quantity
USER
-------------------
user_id (PK)
username
user_email
password_hash
user_role
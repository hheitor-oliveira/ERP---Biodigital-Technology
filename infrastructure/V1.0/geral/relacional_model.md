## SALE
 - sale_id (PK)
 - user_id (FK)
 - total_value
 - sale_date
 - discount

---

## SALE_ITEM
 - sale_item_id(PK)
 - sale_id (FK)
 - product_id (FK)
 - quantity
 - unitary_value

---

## SALE_PAYMENT
 - sale_payment_id (PK)
 - sale_id (FK)
 - payment_method_id (FK)
 - value

---

## PAYMENT_METHOD
 - payment_method_id (PK)
 - name
 - active

---

## PRODUCT
 - product_id (PK)
 - name
 - cost_price
 - sale_price
 - category
 - stock_quantity
 - product_status

---

## MOVEMENT
 - movement_id (PK)
 - user_id (FK)
 - type
 - note
 - movement_date

---

## MOVEMENT_ITEM
 - movement_item_id (PK)
 - movement_id (FK)
 - product_id (FK)
 - quantity

---

## SYSTEM_USER

 - user_id (PK)
 - user_name
 - user_email
 - password_hash
 - role
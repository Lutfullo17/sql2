# -- select product_id, product_name, category_id from products
# -- where category_id > 3
# -- order by product_name asc
#
#
# -- select company_name, country from customers
# -- where country = 'Brazil'
# -- and company_name like '__n%'
#
#
# -- select company_name, region from customers
# -- where region = 'Britan'
# -- and company_name like '__a%'
#
#
# -- select avg(unit_price) as average_price
# -- where products;
#
# -- select count(*) as kechikkan from orders
# -- where to_char(order_date,  'YYYY-MM')='1997-07'
# -- and shipped_date > required_date;
#
#
# -- select * from product
# -- where category_id = 1
# -- and price = (
# -- select max(price) from product
# -- where category_id = 1
# -- );
#
#

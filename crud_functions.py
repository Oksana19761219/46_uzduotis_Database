from sqlalchemy.orm import sessionmaker
from data_base import Customer, Status, Order, Product, ProductOrder, engine


Session = sessionmaker(bind=engine)
session = Session()

def create_customer(f_name:str, l_name:str, email:str):
    customer = Customer(f_name = f_name, l_name = l_name, email = email)
    session.add(customer)
    session.commit()

def create_product(name:str, price:float):
    product = Product(name = name, price = price)
    session.add(product)
    session.commit()

def create_status(name:str):
    status = Status(name = name)
    session.add(status)
    session.commit()


def add_order(customer_id:int, products_quantities:list):
    order = Order(customer_id = customer_id, status_id = 5)
    session.add(order)
    session.commit()
    order_id = _get_order_id()
    _add_ordered_products(order_id, products_quantities)


def _get_order_id():
    last_order = session.query(Order)[-1]
    return last_order.id


def _add_ordered_products(order_id:int, products_quantities:list):
    for product in products_quantities:
        product_id, quantity = product
        product_order = ProductOrder(order_id = order_id, product_id = product_id, quantity = quantity)
        session.add(product_order)
        session.commit()


def change_status(order_id:int, new_status_id:int):
    order = session.query(Order).filter_by(id=order_id)[0]
    order.status_id = new_status_id
    session.commit()




# change_status(2, 3)



# products_quantities = [[2, 15], [4, 19], [5, 24], [3, 1], [1, 10]]
# add_order(3, products_quantities)
# customers = session.query(Customer)
# for customer in customers:
#     print(customer.id, customer.f_name, customer.l_name, customer.email)



# create_status('priimtas')
# create_product('pieštukai', 1.78)
# create_product('liniuotė', 2.58)
# create_product('flomasteriai', 4.15)
# create_product('atvirukas', 1.46)
# create_product('CD diskai', 8.45)
# create_product('magnetukas,suvenyrinis', 0.59)
# create_customer('Antanas', 'Antanaitis', 'antanaitis@mail.lt')
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///46_uzduotis_DB.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column('f_name', String)
    l_name = Column('l_name', String)
    email = Column('email', String)
    orders = relationship('Order')


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    orders = relationship('Order')


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customer.id'))
    date = Column('date_', DateTime, default=datetime.now)
    status_id = Column('status_id', Integer, ForeignKey('status.id'))
    customer = relationship('Customer')
    status = relationship('Status')
    product_order = relationship('ProductOrder')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', Float)
    product_orders = relationship('ProductOrder')


class ProductOrder(Base):
    __tablename__ = 'product_order'
    id = Column(Integer, primary_key=True)
    order_id = Column('order_id', Integer, ForeignKey('order.id'))
    product_id = Column('product_id', Integer, ForeignKey('product.id'))
    quantity = Column('quantity', Integer)
    order = relationship('Order')
    product = relationship('Product')


Base.metadata.create_all(engine)
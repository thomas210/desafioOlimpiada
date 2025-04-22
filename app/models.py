from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    categories = relationship("CustomerCategory", back_populates="customer", cascade="all, delete")

class CustomerCategory(Base):
    __tablename__ = "customer_categories"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    category_name = Column(String)
    customer = relationship("Customer", back_populates="categories")
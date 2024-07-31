from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
import enum


from db.db import engine
from model.entity.admin import Base
from sanad.view import root


class Role(enum.Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(Role))
    records = relationship("FinancialRecord", back_populates="user")

class FinancialRecord(Base):
    __tablename__ = 'financial_records'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    description = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="records")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




root.mainloop()
admin_user = User(username='admin', password='admin_pass', role=Role.ADMIN)
session.add(admin_user)
session.commit()

customer_user = User(username='customer', password='customer_pass', role=Role.CUSTOMER)
session.add(customer_user)
session.commit()

new_record = FinancialRecord(first_name='John', last_name='Doe', description='Test Transaction', amount=100.0, user=customer_user)
session.add(new_record)
session.commit()

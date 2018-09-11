import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#Mohab Ashraf Mohamed Nazmy
#9/9/2018
# sqllite configuration 
Base = declarative_base()
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Base.metadata_create_all(engine) 

#Mohab Ashraf
#11/9/2018
#Create Tower Class
class Towel(Base):
__tablename__ = 'toweles'
name = Column('name', String(80), nullable = False)
id = Column(Integer, primary_key = True)
price = Column('price', Numeric)
description = Column('description', String(200))
in_stock = Column('in_stock', Boolean)
quantity = Column('quantity', Integer)
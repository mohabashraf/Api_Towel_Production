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

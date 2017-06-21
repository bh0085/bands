#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

import sqlite3
from decimal import Decimal
from datetime import date, datetime, timedelta
import dateparser

from sqlalchemy.orm import relationship, backref, configure_mappers, synonym
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, Numeric, String, Unicode, Text, Date, DateTime, Time, Boolean, ForeignKey, UniqueConstraint, func
from sqlalchemy.engine import Engine
from sqlalchemy import event

Base = declarative_base()

class Band(Base):
    __tablename__="rows"
    id = Column(Integer,primary_key=True) 
    bandfacebook=Column(Unicode(255))
    timestamp = Column(Date)
    bandgenre=Column(Unicode(255))
    banddescription=Column(Unicode(255))
    contactemail=Column(Unicode(255))
    bandrecording=Column(Unicode(255))
    bandtwitter=Column(Unicode(255))
    contactname=Column(Unicode(255))
    bandwebsite=Column(Unicode(255))
    bandphoto=Column(Unicode(255))
    bandname=Column(Unicode(255))

                    

    
       
def main():  
    print "CURRENTLY ALL DATA INGESTION IS DONE WITH PACKAGE GSHEETS-IO"
    

if __name__ == "__main__":
    main()


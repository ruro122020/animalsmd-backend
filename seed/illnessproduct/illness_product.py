from config import app
from .illnesses_products_data import illness_product_data
from models.models import IllnessMedication


def seed_illness_product_table():
   with app.app_context():
      illness_medication_table_data = IllnessMedication.query.all()
      print('illness medications data',illness_medication_table_data[0].illness.name)
      print('illness medications data',illness_medication_table_data[1].illness.name)
      print('illness medications data',illness_medication_table_data[2].illness.name)
      print('illness medications data',illness_medication_table_data[3].illness.name)


      #use the illness name
      #if illness name in illness_product_data matches the illness name in illness_medication_table 
        #query the illness table by using the illness name 
        #grab the illness medication id
        #query the medication by id in the database
        #query the products table by using the medication name

        #We want to locate the product instance from the product table by using the product that 
        # matches the medication
        #We want to locate the illness instance from the illness table by using the illness name 
        # in illness_product_data

      pass
   


seed_illness_product_table()
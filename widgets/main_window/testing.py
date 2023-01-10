import sys, os
sys.path.append( os.path.dirname( __file__ ).replace("widgets", ""))
from functions.db_Helper import Db_helper

helper = Db_helper("Alfa.db")
inf = helper.get_list("SELECT name, price, category, image FROM Menu")
for i in inf:
    print(i)
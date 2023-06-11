#pip install py_edamam
from py_edamam import PyEdamam
from py_edamam import Edamam

whole = ''

def info(name):
  e = Edamam(recipes_appid='ecxxxb',
           recipes_appkey='83347a87xxxde8106646')

#recipes_list = e.search_recipe("onion")

# keys scrapped from web demo, but you can provide yours above
  nutrient_data = e.search_nutrient(" orange is my best fruit")

  foods_list = e.search_food(name)
  print("Nutrition information extrated from video")
  whole = foods_list['parsed']
  # print(foods_list['parsed'])
  return whole
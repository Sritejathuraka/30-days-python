##** Lists in Python ** ##

## Creating a Empty List
saradha_food_menu = []
## How to append elements in list
saradha_food_menu.append("chicken curry")
saradha_food_menu.append("Mutton curry")
saradha_food_menu.append("CHicken Fry")
saradha_food_menu.append("Fish Fry")
saradha_food_menu.append("Rice")
saradha_food_menu.append("curd")

## How to access elements in list
saradha_food_menu[2]

## How to modify elements in list
saradha_food_menu[0] = "kadai chicken"

## How to insert elements in list at particular place
saradha_food_menu.insert(2, 'liver Fry')
saradha_food_menu.insert(6, 'raitha')


## How to remove elements in list - removes element by value
saradha_food_menu.remove('kadai chicken')
saradha_food_menu.remove('Fish Fry')
saradha_food_menu.remove('curd')


## How to pop elements in list - removes element by index values and returns removed element
removed_item = saradha_food_menu.pop(1)
removed_another_item = saradha_food_menu.pop()## by default remove last element
print("removed item", removed_item)
print("removed another item", removed_another_item)

## How to del elements in list

saradha_food_menu.append("Fried rice")
saradha_food_menu.append("Gobi 65")
saradha_food_menu.append("chicken pakoda")

del saradha_food_menu[2]
del saradha_food_menu[1:3]
print(saradha_food_menu)

## How to clear elements in list
saradha_food_menu.clear()





# Maximum record value key in dictionary
# Using loop
  
# initializing dictionary
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# initializing search key
key = 'Himani'
  
# Maximum record value key in dictionary
# Using loop
res = None
res_max = 0
for sub in test_dict:
    if test_dict[sub][key] > res_max:
        res_max = test_dict[sub][key]
        res = sub
  
# printing result 
print("The required key is : " + str(res)) 

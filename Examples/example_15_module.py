## 3 different ways of importing module in python

# 1. Import module from a sub-directory in same level
# if myfunction module is in a subdirectory like functions
# import functions.myfunction as f
# area = f.rectangle_area(12,5)
# print(area)

# 2. Import module from a separate local in machine
# if myfunction module is placed in folder /Users/philips/Documents
# import sys
# sys.path.append("/Users/philips/Documents")
# import myfunction as f
# area = f.rectangle_area(12,5)
# print(area)

# 3. Import module from same folder
# if myfunction module is at the same folder as example_15_module
# import myfunction as f
# area = f.rectangle_area(12,5)
# print(area)

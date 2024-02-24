# def my_decorator(func):
#     def wrapper():
#         2 == 2
#         return func
#     return wrapper


# @my_decorator
# def my_function(a, b):
#     return a+ b

import time
import math
def calculate_time(func):
	def inner1(*args, **kwargs):
		begin = time.time()
		func(*args, **kwargs)
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)
	return inner1

@calculate_time
def factorial(num):
	time.sleep(2)
	print(math.factorial(num))

factorial(10)

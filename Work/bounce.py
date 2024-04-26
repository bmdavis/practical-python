# bounce.py
#
# Exercise 1.5

height = 100 * (3/5)
bounce = 1

while bounce <= 10:
    print (bounce, round(height,4))
    height = height * (3/5)
    bounce = bounce + 1

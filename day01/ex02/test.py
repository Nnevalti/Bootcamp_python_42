from vector import Vector
import datetime

print("str : ", str(datetime.datetime.now()))
print("repr : ", repr(datetime.datetime.now()))

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(4)
v3 = Vector((10, 15))

print("Vetor str : ", str(v1))
print("Vector repr : ", repr(v1))

print("v1 : ", v1)
print("v2 : ", v2)
print("v3 : ", v3)
print()
print("v1 + v2 : ", v1 + v2)
print("5 + v1 : ", 5 + v1)
print("v2 + 5 : ", v2 + 5)
print()
print("v1 - v2 : ", v1 - v2)
print("5 - v1 : ", 5 - v1)
print("v2 - 5 : ", v2 - 5)
print()
print("v1 / v2 : ", v1 / v2)
print("0 / v3 : ", 0 / v3)
print("v3 / 0 : ", v3 / 0)
print()
print("v1 * v2 : ", v1 * v2)
print("5 * v1 : ", 5 * v1)
print("v2 * 5 : ", v2 * 5)

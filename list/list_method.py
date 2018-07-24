cars = ['bmw', 'honda', 'audi']
print(len(cars))

cars.append('benz')
print(cars)

cars.insert(2, 'jeep')
print(cars)

x = cars.index('jeep')
print(x)

y = cars.pop()  # removes last item from the list
print(y)  # benz
print(cars)

cars.remove('jeep')
print(cars)

a = cars[0:2]
b = cars[1:]
c = cars[:]
print(a, b, c)

print('---------------------')
print(cars)
cars.sort()
print(cars)
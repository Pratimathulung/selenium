# Create a dictionary 'car'. Create 3 keys - make, model, year.
# Try to access the color key, so it's going to throw an exception using the try, except and finally block.


def exception_handling():
    cars = {'make': 'bmw', 'model': '550i', 'year': '2016'}
    try:
        print(cars['color'])
    except:
        print('We dont have color key')
    finally:
        print('Please find different key')


exception_handling()

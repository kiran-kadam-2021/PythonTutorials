a = 5
b = 2

try:
    print('resource open')
    print(a/b)
    k = int(input('Enter a number: '))
    print(k)
except ZeroDivisionError:
    print('Error : Hey you can not divide by zero')
except ValueError:
    print('Error : u should enter a integer')
except Exception as e:
    print('Error : ', e)
finally:
    print('resource close')

print('bye')

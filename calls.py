from functions import is_even, factorial, reverse_string, is_palindrome
from classes import Book, Temperature, Timer


print("Is 10 even?", is_even(10))
print("Factorial of 5:", factorial(5))
print("Reverse of 'hello':", reverse_string("hello"))
print("Is 'madam' a palindrome?", is_palindrome("madam"))


b = Book("1984", "Emmanuel")
print("Book Info:", b.get_info())

t = Temperature(25)
print("25°C in Fahrenheit:", t.to_fahrenheit())

timer = Timer()
timer.tick()
timer.tick()
print("Current time:", timer.current_time())
timer.reset()
print("Time after reset:", timer.current_time())

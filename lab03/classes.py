
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully. New balance: {self.balance}")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    s = StringManipulator()
    s.getString()
    s.printString()

    square = Square(5)
    print("Area of Square:", square.area())

    rectangle = Rectangle(4, 6)
    print("Area of Rectangle:", rectangle.area())

    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point1.show()
    point2.show()
    print("Distance between points:", point1.dist(point2))


    acc = Account("John", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(2000)


    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    prime_numbers = list(filter(lambda x: is_prime(x), numbers))
    print("Prime numbers in the list:", prime_numbers)

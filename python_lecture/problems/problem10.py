# oops concepts
#question1
class programmer:
    def __init__(name,dept,role,developer):
        name.name=name
        name.dept=dept
        name.role=role
        name.developer=developer
    def info(name):
        print(f"Name of the programmer is {name.name}")
        print(f"Department of the programmer is {name.dept}")
        print(f"Role of the programmer is {name.role}")
        print(f"Developer of the programmer is {name.developer}")
    
p1=programmer("Alice","IT","Backend Developer","Python")
p1.info()

#question2
class square:
    def __init__(self, num):
        self.num=num
    def square(self):
        return self.num*self.num
    def cube(self):
        return self.num*self.num*self.num
    def squareroot(self):
        return self.num**0.5
    s1=square(4)
    print("Square is:",s1.square())
    print("Cube is:",s1.cube())
    print("Square root is:",s1.squareroot())

#question3
class Test:
    a = 5   # class attribute

obj = Test()
obj.a = 0  # creates an instance attribute
print(Test.a)  # 5
print(obj.a)   # 0

#question 4

class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked")
        else:
            print("No seats available")

    def get_status(self):
        print(f"Seats available: {self.seats}")

    def get_fare_info(self):
        print(f"Fare: ₹{self.fare}")


train1 = Train("Express", 100, 500)
train1.get_status()      # Seats available: 100
train1.get_fare_info()   # Fare: ₹500
train1.book_ticket()     # Ticket booked
train1.get_status()      # Seats available: 99

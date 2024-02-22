#1

def square_generator(N):
    for i in range(N):
        yield i ** 2


#2
    
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_nums = even_numbers(n)
print(*even_nums, sep=", ")


#3

def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i



#4
    
def squares(a, b):
  for num in range(a, b + 1):
    yield num ** 2

#5
    
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


    

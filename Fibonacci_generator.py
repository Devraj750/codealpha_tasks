def fibonacci_generator(num):
    a , b = 0 , 1
 
    print("Fibonacci Series:")
    for _ in range(num):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
        
num = int(input("Enter the number :")) 
fibonacci_generator(num) 

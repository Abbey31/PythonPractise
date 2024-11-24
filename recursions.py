# def EvenNums(num):
#     print(num)
#     if num % 2 != 0:
#         print("Please enter an even number")
#     elif num == 2:
#         return num
#     else:
#         return EvenNums(num-2)
    

# EvenNums(8)
# FIBONACCI
def fibonacci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1) +Fibonacci(idx-2)
    
print(Fibonacci(8)) 
print(fibonacci(8)) 
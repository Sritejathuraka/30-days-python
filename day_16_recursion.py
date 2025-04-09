## Example One
def count_down(n):
    if n == 0:
        print("Timer Stopped")
    else:
        print(n)
        count_down(n-1)

## Example Two
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print("factorial result is", result)

    
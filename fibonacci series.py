def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series);
        num1 = num2;
        num2 = series;
        series = num1 + num2;
 
num = int(input('Enter total no of terms in fibonacci series: '))
fibonacci(num)

print('연산자를 먼저 입력하고 숫자를 입력해주세요')
operator = input()


if operator == "+":
    from plus import plus_function
    plus_function()
elif operator == "-":
    from minus import minus_function
    minus_function()
elif operator == "/":
    from division import  division_function
    division_function()
elif operator == "*":
    from product import  product_function
    product_function()

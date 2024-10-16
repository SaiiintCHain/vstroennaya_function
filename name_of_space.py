def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
#inner_function - выдается ошибка, т.к. функция принадлежит встроенному пространству
def test_function(*args):
    def inner_function(*args):
        print('Я в области видимости вункции test_function')
    inner_function()
test_function()
inner_function() #выдает ошибку


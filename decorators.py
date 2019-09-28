def cough_dec(func):

    def func_wrapper():
        #code before func
        print("*Cough*")
        func()
        #code after func
        print("*Cough*")
    return func_wrapper

@cough_dec
def question():
    print("Can you give me a discount on that ?")

@cough_dec
def answer():
    print("It's only 50 DZD you cheap motherfucker !")

question()
answer()
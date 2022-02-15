
import complex_calc
import float_calc
import view

def complex():
    number1 = view.number_complex()
    number2 = view.number_complex()
    operation = view.opern()
    result = complex_calc.calc(number1, number2, operation)
    view.out_data(result)

def float():
    number1 = view.number_float()
    number2 = view.number_float()
    operation = view.opern()
    result = float_calc.calc(number1, number2, operation)
    view.out_data(result)
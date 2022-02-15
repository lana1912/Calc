
import complex_calc
import float_calc
import view
import logic

def complex():
    number1 = view.number_complex()
    number2 = view.number_complex()
    operation = view.opern()
    result = complex_calc.calc(number1, number2, operation)
    logic.log_in_file(number1, number2, operation, result)
    view.out_data(result)

def float():
    number1 = view.number_float()
    number2 = view.number_float()
    operation = view.opern()
    result = float_calc.calc(number1, number2, operation)
    logic.log_in_file(number1, number2, operation, result)
    view.out_data(result)
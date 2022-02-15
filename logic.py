def log_in_file(number_1, number_2, operation, result):
    with open('./logging.csv','a') as file:
        file.write(f'{number_1};{operation};{number_2};{result};\n')
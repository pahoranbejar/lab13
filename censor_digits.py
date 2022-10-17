def censor_digits(input_file, output_file):
    with open(input_file) as file:
        new_line = ""
        lines_of_file = list(file)
        for line in lines_of_file:
            for letter in line:
                if letter.isdigit():
                    new_line += '*'
                else:
                    new_line += letter

            with open(output_file, "w") as f:
                f.write(new_line)


print(censor_digits("test_files/censor_digits_complex_sample.txt", "test_files/complex_test.txt"))

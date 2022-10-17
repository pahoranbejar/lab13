def cougars(filename, new_filename):
    with open(filename) as file:
        new_line = ""
        lines_of_file = list(file)
        for line in lines_of_file:
            if "Cougars" in line or 'COUGARS' in line or "cougars" in line:
                new_line += line

        with open(new_filename, "w") as f:
            f.write(new_line)


print(cougars("test_files/cougars_extra_lines_sample.txt", "test_files/cougars_complex_test.txt"))

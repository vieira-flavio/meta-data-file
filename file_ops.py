def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
            return content
    except:
        raise NotImplementedError()


def read_file_into_list(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            return lines
    except:
        raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    try:
        first_line = file_contents.split('\n')[0]
        with open(output_filename, "w") as file:
            file.write(first_line)
    except:
        raise NotImplementedError()
                

def read_even_numbered_lines(file_name):
    try:
        with open(file_name, "r") as file:
            even_lines = [line for i, line in enumerate(file, start=1) if i % 2 == 0]
            return even_lines
    except:
        raise NotImplementedError()

def read_file_in_reverse(file_name):
    try:
        with open(file_name, "r",) as f:
            lines = f.readlines()
            return [line for line in lines[::-1]]
    except:
        raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
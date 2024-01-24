def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    contenido_string = ''
    with open(file_name, 'r') as file:
        contenido_lista = file.readlines()
        for x in contenido_lista:
            contenido_string = contenido_string + x

    return(contenido_string)


def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE

    contenido_final = []
    with open(file_name, 'r') as file:
        contenido_lista2 = file.readlines()
        for x in contenido_lista2:
            contenido_final.append(x)
    
    return(contenido_final)


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE

    output_string = ''
    for caracter in file_contents:
        output_string = output_string + caracter
        if caracter == '\n':
            break

    with open(output_filename, 'w') as file:
        file.writelines(output_filename)


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    lista_filas_pares = []
    with open(file_name, 'r') as file:
        lista_contenido = file.readlines()
        for indice, linea in enumerate(lista_contenido):
            indice_final = indice + 1
            
            print("Indice: ", indice_final)
            if indice_final % 2 == 0:
                print(linea)
                lista_filas_pares.append(linea) 
    

    return(lista_filas_pares)
                

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    reverse_list = []
    with open(file_name) as file:
        lineas = file.readlines()
        for indice, linea in enumerate(lineas):
            indice_reverso = -(indice + 1) 
            print(indice_reverso)
            print(lineas[indice_reverso])
            reverse_list.append(lineas[indice_reverso])

    return reverse_list     


    #raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print('file contents', file_contents)
    print(read_file_into_list("sampletext.txt"))

    write_first_line_to_file(file_contents, "online.txt")
    
    print(read_even_numbered_lines("sampletext.txt"))
    
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
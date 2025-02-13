PARAMETER = "todos.txt"


def read_todos(parameter=PARAMETER):
    """Read the text file and 
    return todos list """
    with open(parameter, "r") as file_local:
            todos_local = file_local.readlines()
            return todos_local

def write_todos(todos_arg,parameter=PARAMETER):
    """Write the todos item list 
    in a text file
     """
    with open(parameter,"w") as file_local:
            file_local.writelines(todos_arg) 
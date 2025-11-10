def get_todos(filepath = "todo.txt"):
    """ Read todo.txt file and Return the list of iteams in it """
    with open(filepath,'r') as file:
        todos=file.readlines()
    return todos 

def write_todos(todos_arg, filepath = "todo.txt"):
     """ Write the to-do items list in the todo.txt file"""
     with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("Functions imported...!")

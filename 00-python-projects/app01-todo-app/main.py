
while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # User Input for To do List
            todo = input("Enter a todo: ") + "\n"
            # Proof of existing text
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # Append new Text behind existing Text 
            todos.append(todo)       
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            # Gives each item a row of numbers and the item self
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            
        case 'edit':
            # Choose the number of exiting Todo to edit 
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break 

print('Bye')
 
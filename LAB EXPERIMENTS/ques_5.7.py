'''7.Create a Todo list Manager where users can add, view, and remove tasks.
Use List for storing tasks.'''

tasks = []

while True:
    print("\n--- TODO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #  Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    #  View Tasks
    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)
        else:
            print("No tasks available!")

    # Remove Task
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number!")
        else:
            print("No tasks to remove!")

    # Exit
    elif choice == "4":
        print("Exiting Todo List Manager...")
        break

    else:
        print("Invalid choice! Please try again.")
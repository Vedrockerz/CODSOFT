tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.\n")
    else:
        print("\n**** Your To-Do List ****")

        for i in range(len(tasks)):
            status = "Done" if tasks[i]["completed"] else "Not Done"
            print(f"{i + 1}. {tasks[i]['task']} [{status}]")
        
        print(f"\nTotal tasks: {len(tasks)}\n")


def add_task():
    task_name = input("Enter task: ")
    new_task = {
        "task": task_name,
        "completed": False
    }
    tasks.append(new_task)
    print("Task added successfully.\n")

def completed_task():
    show_tasks()
    user_input = input("Enter task numbers to mark as completed : ")
    print("")
    task_number = user_input.replace(" " , "").split(",")

    updated = False

    for num in task_number:
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print(f"Task {index + 1} marked as completed.\n")
            else:
                print(f"Task {num} is invalid task number.\n")
        else:
            print(f"'{num}' is not a valid number.\n")

def delete_task():
    show_tasks()
    user_input = input("Enter task numbers to be deleted : ")
    print("")
    task_numbers = user_input.replace(" " , "").split(",")

    updated = False
    removed_tasks = []
    removing_indexes = []

    for num in task_numbers:
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(tasks):
                removing_indexes.append(index)
                updated = True
            else:
                print(f"Task {num} is invalid task number.\n")
        else:
            print(f"'{num}' is not a valid number.\n")

    for i in sorted(removing_indexes , reverse=True):
        removed = tasks.pop(i);
        removed_tasks.append(removed["task"])
        print(f"Deleted : {removed['task']}")

    if updated:
        print("\nSelected Tasks Deleted Successfully !\n")
    else:
        print("\nNo Valid tasks were deleted.\n")

def main():
    while True:
        print("----- TO-DO LIST MENU -----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print("")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            completed_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! \n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

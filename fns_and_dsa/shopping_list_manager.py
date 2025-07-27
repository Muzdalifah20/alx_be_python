def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(user_item)
        elif choice == '2':
            # Prompt for and remove an item
            user_item = input("Enter the item to remove: ").strip().lower()
            if user_item in shopping_list:
                shopping_list.remove(user_item)
            else:
                print(f"Item '{user_item}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"\t{item}")
            else:
                print("The shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

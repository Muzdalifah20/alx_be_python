Task = input("Enter your task: ").strip()
Priority = input("Priority (high/medium/low): ").strip().lower()
Time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: {Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority input. Please enter high, medium, or low.")
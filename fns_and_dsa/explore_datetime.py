from datetime import datetime , timedelta
 
def  display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time {formatted}"

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date:"))

    current_date = datetime.now().date()
    future_date = current_date + timedelta(days=days)
    return (f"Future date after {days} days: {future_date.strftime('%Y-%m-%d')}")

print(display_current_datetime())
print(calculate_future_date())

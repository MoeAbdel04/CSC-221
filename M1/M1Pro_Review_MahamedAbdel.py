# Date conversions
# 9/06/24
# CSC221 M1Pro– Review
# Mahamed Abdel



def dateToLabel(indate):
    # List of month names and days in each month
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the input format is correct
    fields = indate.split('/')
    if len(fields) != 3:
        raise Exception('Incorrect format for date. Please use mm/dd/yyyy.')

    mm, dd, yyyy = fields

    # Check if mm, dd, yyyy are numeric
    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
        raise Exception('Month, day, and year must be numeric.')

    # Convert mm, dd, yyyy to integers
    mm = int(mm)
    dd = int(dd)
    yyyy = int(yyyy)

    # Validate the month
    if mm < 1 or mm > 12:
        raise Exception('Invalid month.')

    # Validate the day
    if dd < 1 or dd > max_days[mm - 1]:
        raise Exception(f'Invalid day for {months[mm - 1]}.')

    # Construct and return the formatted date
    return f"{months[mm - 1]} {dd}, {yyyy}"

# Main program to prompt the user for a date
def main():
    while True:
        try:
            indate = input("Enter a date (mm/dd/yyyy) or type 'stop' to quit: ").strip()
            
            # Sentinel to stop the loop
            if indate.lower() == "stop":
                print("Program terminated.")
                break
            
            formatted_date = dateToLabel(indate)
            print(f"Formatted Date: {formatted_date}")

        except Exception as e:
            print(f"Error: {e}")

# Call the main function
if __name__ == "__main__":
    main()
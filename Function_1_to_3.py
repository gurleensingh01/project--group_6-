import appointment as ap

DASH_37 = "=" * 37

VALID_SELECTION = ['1', '2', '3', '4', '9']
WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def create_weekly_calender(appt_list):
    '''
    Creates an appointment list from Monday to Saturday, from 9 AM to 4 PM

    Arguments:
    None

    Returns:
    The appointment list
    '''
    for day in WORKING_DAYS:
        for hour in range(9,17):
            appointment = ap.Appointment(day,hour)
            appt_list.append(appointment)
    print("Weekly calendar created")

#Loads previously booked appointments into the calendar
def load_scheduled_appointments(appt_list):
    '''
    Retrieves appointments from the appointments1.csv file and assigns values to the appointment list

    Arguments:
    Appointment list

    Returns:
    The number of scheduled appointments
    '''
    filename = input("Enter appointment filename: ")
    while filename != "appointments1.csv":
        filename = input("File not found. Re-enter appointment filename: ")
    file = open(r"C:\temp\appointments1.csv", "r")
 
    number_of_scheduled_appointments = 0
 
    for line in file:
        values = line.rstrip().split(",")
        name = values[0]
        phone_number = values[1]
        appt_type = int(values[2])
        day = values[3]
        start_time = int(values[4])
        appointments = find_appointment_by_time(appt_list, day, start_time)
        if appointments != None:
            appointments.schedule(name, phone_number, appt_type)
            number_of_scheduled_appointments += 1
 
    file.close()
    return number_of_scheduled_appointments

#Displays the menu of application options
def print_menu():
    '''
    Prints the menu options and checks the valid input options from users

    Arguments:
    None

    Returns:
    The selected option 
    '''
    print("Jojo's Hair Salon Appointment Manager")
    print(DASH_37)
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) cancel an appointment")
    print(" 9) Exit the system")
    selection = input("Enter your selection: ")

    while selection not in VALID_SELECTION:
        print("Invalid selection! please try again. ")
        selection = input("Enter your selection: ")
    
    print()
    return int(selection)

def find_appointment_by_time(appt_list, day, start_time):
    '''
    Finds the appointments that matched input day and start time

    Arguments:
    Appointment List
    Day
    Start

    Returns:
    Matched appointment
    '''
    for appointment in appt_list:
        if (
            appointment.get_day_of_week() == day
            and appointment.get_start_time_hour() == start_time
        ):
            return appointment
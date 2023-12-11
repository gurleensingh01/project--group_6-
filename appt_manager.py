# Jojo's Hair Salon - Appointment Management System
#
# This program manages appointments for Jojo's Hair Salon, tracking client information,
# appointment details, and providing functionality to schedule, find, print, cancel appointments,
# and exit the system. It includes a dedicated Appointment class with specific properties and methods.
#
# Inputs
#    Filename
#    Day on which the appointments needs to be
#    Time on which the appointments needs to be
#    Client name
#    Client phone
#    Selections

# Process
#    Loading previously scheduled appointments
#    Creating calendar in appointment list
#    Making appointments and adding it to the appointment list
#    Finding appointments by name
#    Finding appointments by day and time
#    Printing calendar for a specific day
#    Cancelling an appointment
#    Saving the appointments to the file

# Output
#    Number of preiously loaded appointments
#    Appointments for a specific name
#    Calendar for a specific day
#    Number of saved appointments
#
# Authors: Tan Nguyen, Gurleen Singh and Jashanpreet Singh
# Version: 12-08-2023


import appointment as ap
import os
import os.path

DASH_37 = "=" * 37
DASH_85 = "-" * 85
VALID_SELECTION = ['1', '2', '3', '4', '9']
VALID_APPOINTMENT_TYPE = [1 , 2, 3, 4]
WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Creates a one-week calendar of available appointments
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

#Finds an appointment by day and start hour
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
            appointment.get_day_of_week() == day.capitalize()
            and appointment.get_start_time_hour() == start_time
        ):
            return appointment


# Displays appointments matching a client name
def show_appointments_by_name(appt_list, name):
    '''
    Finds the appointments that matched input name and display them 

    Argument:
    Appointment List
    Customer's name: Allowing for partial and non-case sensitive matches

    Returns:
    found appointments
    '''
    found_appointments = ""
    for appointment in appt_list:
        if name.upper() in appointment.get_client_name().upper():
            found_appointments = appointment.__str__()
            print(found_appointments)
    return found_appointments              

# Displays appointments for a specific day
def show_appointments_by_day(appt_list, day):
    '''
    Finds the appointments that matched input day and display them

    Arguments:
    Appointment List
    Day

    Returns:
    None
    '''
    for appointment in appt_list:
        if day.capitalize() in appointment.get_day_of_week():
            print(appointment.__str__())


# Saves scheduled appointments to a file
def save_scheduled_appointments(appt_list):
    ''' 
    Checks the file's existence and writes the scheduled appointments to a csv file 

    Arguments:
    Appointment List

    Returns:
    The number of scheduled appointments saved
    '''
    nbr_of_saved_appointment = 0
    file_name = input("Enter appointment filename: ")
    file_path = os.path.join("C:\\temp", file_name)
    file_overwrite = True
    while os.path.exists(file_path) and file_overwrite:
        overwrite = input("File already exists. Do you want to overwrite it? (Y/N): ").upper()
        while overwrite not in ("Y", "N"):
            overwrite = input("Invalid input. Do you want to overwrite it? (Y/N): ").upper()
        if overwrite == "Y":
            file_overwrite = False
        elif overwrite == "N":
            file_name = input("Enter a different file name: ")
            file_path = os.path.join("C:\\temp", file_name)
 
    file_name_f = open(file_path, "w")
    for appointment in appt_list:
        if 0 != appointment.get_appt_type() and appointment.get_appt_type() in (1,2,3,4):
            file_name_f.write(appointment.format_record() + "\n")
            nbr_of_saved_appointment += 1
    file_name_f.close()
    print(f"{nbr_of_saved_appointment} scheduled appointments have been sucessfully saved")    
    return nbr_of_saved_appointment

def main():
    '''
    Print the starting message
    Calls the create_weekly_calendar to create a weekly calendar in appt_list
    Ask the user if they want to load previously loaded appointments
    If yes, calls the load_scheduled_appointments() to load previously loaded appointments
    Call the print_menu() to print the menu and prompt the user for valid selection
    If the selection is 1, calls the get_day_of_week, get_start_time_hour and get_appt_type to find if the slot is available and use schedule method to schedule the appointment if the slot is available
    If the selection is 2, calls the function show_appointments_by_name() to find the appointments by name
    If the selection is 3, calls the function show_appointments_by_day() to print calendar for the chosen day
    If the selection is 4, calls the cancel method to cancel the appointment 
    If the selection is 9, Exit the system
    Ask the user if they want to save the records in the file
    If yes, calls the function save_scheduled_appointments() to save it in the chosen file by user
    Print the ending message

    '''
    appt_list = []
    
    print("Starting the Appointment Manager System")
    create_weekly_calender(appt_list)
    load_schedule_appointments_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")

    while load_schedule_appointments_option.upper() not in ("Y", "N"):
        load_schedule_appointments_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")

    if load_schedule_appointments_option.upper() == "Y":
        loaded_appointments = load_scheduled_appointments(appt_list)
        print(f"{loaded_appointments} previously scheduled appointments have been loaded")
        print()
        print()

    else:
        print()
        print()
    
    selection = print_menu()

    while selection != 9:
        
        if selection == 1:
            print("** Schedule an appointment **")

            day = input("What day: ")
            start_hour = int(input("Enter start hour (24 hour clock): "))
            
            found = False
            index = 0 
            
            while index < len(appt_list) and not found:
                current_appointment = appt_list[index]

                if current_appointment.get_day_of_week() == day.capitalize() and current_appointment.get_start_time_hour() == start_hour and current_appointment.get_appt_type() == 0:
                    found = True
                index += 1  

            if found:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")

                print("Appointment types")
                print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")

                type_of_appointment = int(input("Type of Appointment: "))

                if type_of_appointment in VALID_APPOINTMENT_TYPE:
                    current_appointment.schedule(client_name.capitalize(), client_phone, type_of_appointment)
                    print(f"Ok, {client_name.capitalize()}'s appointment is scheduled!")

                else:
                    print("Sorry that is not a valid appointment type!")
            
            
            elif day.capitalize() not in WORKING_DAYS or start_hour not in range(9, 17):
                print("Sorry that time slot is not in the weekly calendar")     

            else:
                print("Sorry that time slot is booked already!")        
        
        elif selection == 2:
            print('** Find appointment by name **')
            client_name = input("Enter Client Name: ")
            print(f"Appointments for {client_name}")
            print()
            print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
            print(DASH_85)
            
            found_appointments = show_appointments_by_name(appt_list, client_name)

            if found_appointments == "":
                print("No appointments found.")

        elif selection == 3:
            print('** Print calendar for a specific day **')
            day = input("Enter the day of week: ")
            print(f"Appointments for {day}")
            print()
            print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
            print(DASH_85)

            show_appointments_by_day(appt_list, day)

        else:
            print('** Cancel an appointment **')
            day = input("What day: ")
            start_hour = int(input("Enter start hour (24 hour clock): "))

            found = False
            index = 0
            while index < len(appt_list) and not found:
                current_appointment = appt_list[index]

                if current_appointment.get_day_of_week() == day.capitalize() and current_appointment.get_start_time_hour() == start_hour and current_appointment.get_appt_type() != 0:
                    found = True
                index += 1    
            if found:
                print("Appointment: {} {} - {} for {} has been cancelled!".format(current_appointment.get_day_of_week(), str(current_appointment.get_start_time_hour()).zfill(2) + ":00", str(current_appointment.get_end_time_hour()).zfill(2) + ":00", current_appointment.get_client_name()))
                current_appointment.cancel()

            elif day.capitalize() not in WORKING_DAYS or start_hour not in range(9, 17):
                print("Sorry that time slot is not in the weekly calendar")     

            else:
                print("That time slot isn't booked and doesn't need to be cancelled")

        print()
        selection = print_menu()   
    
    print("** Exit the system **")
    save_option = input("Would you like to save all scheduled appointments to a file (Y/N)? ")

    while save_option.upper() not in ('Y', 'N'):
        print("Invalid Option! please try again")
        save_option = input("Would you like to save all scheduled appointments to a file (Y/N)? ")

    if save_option.upper() == 'Y':
        save_scheduled_appointments(appt_list)
        print("Good Bye!")

    else:
        print("Good Bye!")

if __name__ == "__main__":
    main()      


import os
import os.path

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
        if day.capitalize() == appointment.get_day_of_week():
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
            file_name = input("Enter appointment filename: ")
            file_path = os.path.join("C:\\temp", file_name)
 
    file_name_f = open(file_path, "w")
    for appointment in appt_list:
        if 0 != appointment.get_appt_type() and appointment.get_appt_type() in (1,2,3,4):
            file_name_f.write(appointment.format_record() + "\n")
            nbr_of_saved_appointment += 1
    file_name_f.close()
    print(f"{nbr_of_saved_appointment} scheduled appointments has successfully been saved")    
    return nbr_of_saved_appointment
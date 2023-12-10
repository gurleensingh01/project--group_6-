class Appointment:

    # Constructor to initialize properties
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    # Getter for client name
    def get_client_name(self):
        return self.__client_name
    
    # Getter for client phone
    def get_client_phone(self):
        return self.__client_phone
    
    # Getter for appt type
    def get_appt_type(self):
        return self.__appt_type

    # Getter for day of the week
    def get_day_of_week(self):
        return self.__day_of_week
    
    # Getter for start time hour
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    # Getter for appointment type description
    def get_appt_type_desc(self):
        appt_type_desc = {0:"Available", 1:"Mens Cut", 2:"Ladies Cut", 3:"Mens Colouring", 4:"Ladies Colouring"}   
        return appt_type_desc.get(self.__appt_type)   
    
    # Getter for end time hour
    def get_end_time_hour(self):
        return str(self.__start_time_hour + 1)
    
    # Setter for client name
    def set_client_name(self, new_client_name):
        self.__client_name = new_client_name
     
    # Setter for client phone 
    def set_client_phone(self, new_client_phone):
        self.__client_phone = new_client_phone
    
    # Setter for appointment type
    def set_appt_type(self, new_appt_type):
        self.__appt_type = new_appt_type
    
    # Method to schedule appointment
    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
    
    # Method to cancel the appointment
    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    # Method to format the appointment in csv format
    def format_record(self):
        return str(self.__client_name) + "," + str(self.__client_phone) + "," + str(self.__appt_type) + "," + str(self.__day_of_week) + "," + str(self.__start_time_hour).zfill(2)

    # Method to format the appoinment as a string
    def __str__(self): 
        return "{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format(str(self.__client_name),
        str(self.__client_phone), str(self.__day_of_week), str(self.__start_time_hour).zfill(2) + ":00", str(self.__start_time_hour + 1).zfill(2) + ":00", self.get_appt_type_desc())
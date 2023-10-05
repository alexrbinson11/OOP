class Patient:

    def __init__(self, patient_id, patient_name, patient_address, patient_phone, patient_veteran_status):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__patient_address = patient_address
        self.__patient_phone = patient_phone
        self.__patient_veteran_status = patient_veteran_status

    def get_patient_id(self):
        return self.__patient_id
    
    def get_patient_name(self):
        return self.__patient_name
    
    def get_patient_address(self):
        return self.__patient_address
    
    def get_patient_phone(self):
        return self.__patient_phone
    
    def get_patient_veteran_status(self):
        return self.__patient_veteran_status
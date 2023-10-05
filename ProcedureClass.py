class Procedure:

    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charge, patient_id):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner_name = practitioner_name
        self.__procedure_charge = procedure_charge
        self.__patient_id = patient_id

    def get_procedure_name(self):
        return self.__procedure_name
    
    def get_procedure_date(self):
        return self.__procedure_date
    
    def get_practitioner_name(self):
        return self.__practitioner_name
    
    def get_procedure_charge(self):
        return self.__procedure_charge
    
    def get_patient_id(self):
        return self.__patient_id

import PatientClass as patient
import ProcedureClass as procedure

def main():

    #Enter Patient Info
    patient_id = int(input('\nEnter Patient ID: '))
    patient_name = input('Enter Patient Name: ')
    patient_address = input('Enter Patient Address: ')
    patient_phone = input('Enter Patient Phone Number: ')
    patient_veteran_status = input("Is the patient a Veteran? (True/False): ").upper()

    patient1 = patient.Patient(patient_id, patient_name, patient_address, patient_phone, patient_veteran_status)

   #Print Patient Info
    print('\n*** Patient Bill ***')
    print(f'Name: {patient1.get_patient_name()}')
    print(f'Address: {patient1.get_patient_address()}')
    print(f'Phone: {patient1.get_patient_phone()}\n')

    #Enter Procedure Info

    physical = procedure.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    mri = procedure.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    ct = procedure.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)
    
    total_charge = 0

    if physical.get_patient_id() == patient1.get_patient_id():
        print(f'Procedure: {physical.get_procedure_name()}')
        print(f'Date: {physical.get_procedure_date()}')
        print(f'Practitioner: {physical.get_practitioner_name()}')
        print(f'Charge: ${physical.get_procedure_charge():,.2f}\n')
        total_charge += physical.get_procedure_charge()

    if mri.get_patient_id() == patient1.get_patient_id():
        print(f'Procedure: {mri.get_procedure_name()}')
        print(f'Date: {mri.get_procedure_date()}')
        print(f'Practitioner: {mri.get_practitioner_name()}')
        print(f'Charge: ${mri.get_procedure_charge():,.2f}\n')
        total_charge += mri.get_procedure_charge()
 
    if ct.get_patient_id() == patient1.get_patient_id():
        print(f'Procedure: {ct.get_procedure_name()}')
        print(f'Date: {ct.get_procedure_date()}')
        print(f'Practitioner: {ct.get_practitioner_name()}')
        print(f'Charge: ${ct.get_procedure_charge():,.2f}\n')
        total_charge += ct.get_procedure_charge()

    if patient1.get_patient_veteran_status() == 'TRUE':
        total_charge *= .6
        print(f'Total charges: ${total_charge:,.2f}')
    else:
        print(f'Total charges: ${total_charge:,.2f}\n')

main()


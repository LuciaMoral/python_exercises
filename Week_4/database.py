from peewee import *
import csv

db = SqliteDatabase("clinic.db")

class ClinicalEntry(Model):
    patient_name = CharField()
    doctor = CharField()
    specialty = CharField()
    medical_history = CharField()


    class Meta:
        database = db


def connect():
    db.connect()
    db.create_tables([ClinicalEntry], safe=True)

class Medical(object):
    def __init__(self, patient_name=None, doctor=None, specialty=None, medical_history=None):
        self.patient_name = patient_name
        self.doctor = doctor
        self.specialty = specialty
        self.medical_history = medical_history

    def create_doctor_profile(self):
        entry = ClinicalEntry(doctor = self.doctor, specialty = self.specialty)
        entry.save()

    def create_history(self):
        entry = ClinicalEntry(patient_name = self.patient_name, doctor= self.doctor, medical_history = self.medical_history, specialty = self.specialty)
        entry.save()

    def view_doctors(self):
        for entry in ClinicalEntry.select():
            print(f"Doctor: {entry.doctor} - Specialty: {entry.specialty}")

    def update_medical_history(self, id, patient_name, doctor, specialty, medical_history):
        query = ClinicalEntry.update(patient_name = patient_name, doctor = doctor, specialty = specialty, medical_history = medical_history)
        query.execute()
        print("The patient's history has been saved.")

    def delete_medical_history(self, id):
        query = ClinicalEntry.delete().where(ClinicalEntry.id == id)
        deleted_records = query.execute()
        print(f"Deleted records: {deleted_records}")

    def export_medical_records(self, data=[]):
        with open("file.csv", "w+") as file:
            file = csv.DictWriter(file, fieldnames=["id","patient_name", "doctor", "speciality","medical_history" ])
        file.writeheader()

        for line in data:
                file.writerow(line)


def menu():
    while True:
        print("Choose one of the following options: ")
        print("1. Create a new doctor's profile")
        print("2. Create patient's medical history")
        print("3. Update patient's medical history")
        print("4. Delete patient's medical history")
        print("5. View doctors")
        print("6. Export records to a csv file")
        print("0. Exit")

        option = int(input(" "))

        if option == 1:
            doctor_name = input("enter doctor's full name: ")
            specialty = input("enter doctor's specialty: ")
            profile = Medical(doctor_name, specialty)
            profile.create_doctor_profile()
        elif option == 2:
            patient_name = input("enter patient's full name: ")
            doctor_name = input("enter doctor's full name: ")
            specialty = input("enter doctor's specialty: ")
            history = input("enter patient's medical history: ")
            patient = Medical(patient_name, doctor_name, specialty, history)
            patient.create_history()
        elif option == 3:
            id = int(input("enter patient's id"))
            patient_name = input("enter patient's full name: ")
            doctor_name = input("enter doctor's full name: ")
            specialty =  input("enter doctor's specialty: ")
            medical_history = input("Enter new medical history for patient: ")
            history = Medical(id, patient_name, doctor_name, specialty, medical_history)
        elif option == 4:
            id = int(input("enter patient's id you wish to delete: "))
            patient = Medical()
            patient.delete_medical_history(id)
        elif option == 5:
            doctors = Medical()
            doctors.view_doctors()
        elif option == 6:
            csv_file = Medical()
            csv_file.export_medical_records()
        elif option == 0:
            break
        else:
            print("Option not available in menu")

def main():
    connect()
    menu()



if __name__ == "__main__":
    main()

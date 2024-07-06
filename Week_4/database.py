from datetime import datetime
from peewee import *
import csv

db = SqliteDatabase("clinic.db")

class BaseModel(Model):
    class Meta:
        database = db

class PatientModel(BaseModel):
    id = AutoField(primary_key = True)
    name = CharField(unique = True)
    last_name = CharField(unique = True)
    treating_doctor = CharField(unique = True)
    specialty = CharField(unique = True)
    medical_history = CharField(unique = True)

def connect():
    db.connect()
    db.create_tables([PatientModel], safe= True)

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Doctor(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.specialty = PatientModel.specialty

    def add_doctor(self):
        entry = PatientModel(name = self.name, last_name = self.last_name)
        entry.save()

    @staticmethod
    def view_doctors():
        for entry in PatientModel.select():
            print(f"id: {entry.id} - name: {entry.name} {entry.last_name} - specialty: {entry.specialty}")

class Patient(Person):
    def __init__(self, name, last_name, medical_history):
        super().__init__(name, last_name)
        self.medical_history = PatientModel.medical_history
        self.treating_doctor = PatientModel.treating_doctor

    def create_history(self):
        entry = PatientModel(name = self.name, last_name = self.last_name)
        entry.save()

    def update_medical_history(self):
        query = PatientModel.update(name = self.name, last_name = self.last_name)
        query.execute()
        print("the patient's history has been updated")

    @staticmethod
    def delete_medical_history(patient_id):
        query = PatientModel.delete().where(PatientModel.id == patient_id)
        query.execute()
        print(f"Deleted patient with ID {patient_id}")

    @staticmethod
    def view_patients():
        for entry in PatientModel.select():
            print(f"ID: {entry.id}, Name: {entry.name} {entry.last_name}")

    @staticmethod
    def export_medical_records():
        with open("clinic.csv", "w+") as csv_file:
            fields = ["id", "name", "last_name", "treating_doctor"]
            csv_output = csv.DictWriter(csv_file, delimiter= ",", quotechar='"')
            csv_output.writeheader()

            for line in PatientModel.select().dicts():
                csv_output.writerow(line)
        print("Medical history has been exported")

def menu():
    while True:
        print("Choose one of the following options: ")
        print("1. Create patient's medical history")
        print("2. Update patient's medical history")
        print("3. Delete patient's medical history")
        print("4. List patients")
        print("5. Export records to a csv file")
        print("6. Add a new doctor")
        print("7. List all doctors")
        print("0. Exit")

        option = int(input(" "))

        if option == 1:
            name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            medical_history = input("enter patient's medical history")
            patient = Patient(name, last_name, medical_history)
            patient.create_history()
        elif option == 2:
            patient_id = int(input("Enter patient's id number: "))
            name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            medical_history = input("enter patient's new medical history: ")
            patient = Patient(name, last_name, medical_history)
            patient.update_medical_history(patient_id)
        elif option == 3:
            patient_id = int(input("Enter patient's id number: "))
            Patient.delete_medical_history(patient_id)
        elif option == 4:
            Patient.view_patients()
        elif option == 5:
            Patient.export_medical_records()
        elif option == 6:
            name = input("Enter doctor's first name: ")
            last_name = input("Enter doctor's last name: ")
            specialty = input("enter doctor's specialty: ")
            doctor = Doctor(name, last_name, specialty)
            doctor.add_doctor()
        elif option == 7:
            Doctor.view_doctors()
        elif option == 0:
            break
        else:
            print("please enter valid option")

def main():
    connect()
    menu()

if __name__ == "__main__":
    main()

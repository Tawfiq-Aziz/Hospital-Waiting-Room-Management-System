import tkinter as tk

class Patient:
    def __init__(self, id, name, age, blood):
        self.id = id
        self.name = name
        self.age = age
        self.blood = blood
        self.next = None
        self.prev = None

class WRM:
    def __init__(self):
        self.head = Patient(None, None, None, None)
        self.head.next = self.head
        self.head.prev = self.head

    def registerPatient(self, id, name, age, bloodgroup):
        p1 = Patient(id, name, age, bloodgroup)
        p1.next = self.head
        p1.prev = self.head.prev
        self.head.prev.next = p1
        self.head.prev = p1

    def servePatient(self):
        if self.head.next == self.head:
            return None
        else:
            served = self.head.next
            self.head.next = served.next
            served.next.prev = self.head
            return served

    def showAllPatient(self):
        current = self.head.next
        while current != self.head:
            print(f'Patient: {current.name} {current.id}')
            current = current.next

    def canDoctorGoHome(self):
        if self.head.next == self.head:
            return True
        else:
            return False

    def cancelAll(self):
        self.head.next = self.head
        self.head.prev = self.head

    def ReverseTheLine(self):
        current = self.head.prev
        while current != self.head:
            print('Patient ID:', current.id, end=" ")
            current = current.prev
        print()

def register_patient():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    blood = blood_entry.get()
    w.registerPatient(id, name, age, blood)
    result_label.config(text="Success. Patient added.")

def serve_patient():
    serve = w.servePatient()
    if serve == None:
        result_label.config(text="No patient in the waiting room.")
    else:
        result_label.config(text="Patient served")

def show_all_patients():
    result_label.config(text="Patients remaining")
    w.showAllPatient()

def can_doctor_go_home():
    if w.canDoctorGoHome():
        result_label.config(text="Yes doctor can go home")
    else:
        result_label.config(text="No, patients waiting")

def cancel_all():
    w.cancelAll()
    result_label.config(text="All patients cancelled. Doctor can go to Lunch.")

def reverse_the_line():
    result_label.config(text="Reversed line:")
    w.ReverseTheLine()

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Waiting Room Management System")

id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

blood_label = tk.Label(root, text="Blood Group:")
blood_label.grid(row=3, column=0)
blood_entry = tk.Entry(root)
blood_entry.grid(row=3, column=1)

register_button = tk.Button(root, text="Register Patient", command=register_patient)
register_button.grid(row=4, column=0)

serve_button = tk.Button(root, text="Serve Patient", command=serve_patient)
serve_button.grid(row=4, column=1)

show_button = tk.Button(root, text="Show All Patients", command=show_all_patients)
show_button.grid(row=5, column=0)

doctor_button = tk.Button(root, text="Can Doctor go Home", command=can_doctor_go_home)
doctor_button.grid(row=5, column=1)

cancel_button = tk.Button(root, text="Cancel all Appointment", command=cancel_all)
cancel_button.grid(row=6, column=0)

reverse_button = tk.Button(root, text="ReverseTheLine", command=reverse_the_line)
reverse_button.grid(row=6, column=1)

exit_button = tk.Button(root, text="Exit the Program", command=exit_program)
exit_button.grid(row=7, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=8, column=0, columnspan=2)

w = WRM()

root.mainloop()
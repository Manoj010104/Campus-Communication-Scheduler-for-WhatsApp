import tkinter as tk
from tkinter import messagebox
import pywhatkit
from datetime import datetime, timedelta

class StudentEngagementMessenger:
    def __init__(self):
        """
        Initialize with some predefined deadlines messages.
        """
        self.deadlines = [
            "Registration deadline for the upcoming semester is approaching.",
            "Don't forget to submit your assignments on time.",
            "Midterm exams are scheduled for next week.",
        ]

    def generate_message(self, student_name, pending_assignments, pending_fee, less_attendance,
                         seminar, library_hours, scholarship, cultural_event,
                         online_course, gym_membership, blood_donation, job_fair, vaccination):
        """
        Generate a customized message based on student information and events.
        """
        message = f"Hello {student_name},\n\n"

        # Add specific reminders based on the inputs
        if pending_assignments:
            message += "You have pending assignments. Please complete them as soon as possible.\n"

        if pending_fee:
            message += "You have pending fee. Please settle it as soon as possible.\n"

        if less_attendance:
            message += "Your attendance is less than the required percentage. Please attend classes regularly.\n"

        if seminar:
            message += "Don't forget to attend the upcoming seminar on career development.\n"

        if library_hours:
            message += "The library is open for extended hours during the exam period.\n"

        if scholarship:
            message += "The deadline for the scholarship application is approaching. Apply now.\n"

        if cultural_event:
            message += "The student council is organizing a cultural event. Join and showcase your talents.\n"

        if online_course:
            message += "The university is offering a free online course on mental health. Enroll now.\n"

        if gym_membership:
            message += "The gym is offering a discounted membership for students. Avail the offer now.\n"

        if blood_donation:
            message += "The university is organizing a blood donation drive. Participate and make a difference.\n"

        if job_fair:
            message += "The placement cell is organizing a job fair. Attend and explore job opportunities.\n"

        if vaccination:
            message += "The university is offering a free vaccination drive. Get vaccinated and stay healthy.\n"

        message += "\nBest regards,\n[Your Name] 👋"
        return message

    def send_message(self, student_name, mobile, message, hour, minute):
        """
        Schedule and send a WhatsApp message at the specified time.
        """
        try:
            pywhatkit.sendwhatmsg(f"+{mobile}", message, hour, minute, wait_time=20)
            messagebox.showinfo("Success", f"Message for {student_name} sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending message for {student_name}: {str(e)}")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.student_name_label = tk.Label(self, text="Enter Student Name:", font=("Arial", 12, "bold"))
        self.student_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.student_name_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.mobile_label = tk.Label(self, text="Enter Mobile No of Student (including country code):", font=("Arial", 12, "bold"))
        self.mobile_label.grid(row=1, column=0, padx=10, pady=10)

        self.mobile_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.mobile_entry.grid(row=1, column=1, padx=10, pady=10)

        self.pending_assignments_label = tk.Label(self, text="Pending Assignments? (y/n):", font=("Arial", 12, "bold"))
        self.pending_assignments_label.grid(row=2, column=0, padx=10, pady=10)

        self.pending_assignments_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.pending_assignments_entry.grid(row=2, column=1, padx=10, pady=10)

        self.pending_fee_label = tk.Label(self, text="Pending Fee? (y/n):", font=("Arial", 12, "bold"))
        self.pending_fee_label.grid(row=3, column=0, padx=10, pady=10)

        self.pending_fee_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.pending_fee_entry.grid(row=3, column=1, padx=10, pady=10)

        self.less_attendance_label = tk.Label(self, text="Less Attendance? (y/n):", font=("Arial", 12, "bold"))
        self.less_attendance_label.grid(row=4, column=0, padx=10, pady=10)

        self.less_attendance_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.less_attendance_entry.grid(row=4, column=1, padx=10, pady=10)

        self.seminar_label = tk.Label(self, text="Seminar on Career Development? (y/n):", font=("Arial", 12, "bold"))
        self.seminar_label.grid(row=5, column=0, padx=10, pady=10)

        self.seminar_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.seminar_entry.grid(row=5, column=1, padx=10, pady=10)

        self.library_hours_label = tk.Label(self, text="Extended Library Hours? (y/n):", font=("Arial", 12, "bold"))
        self.library_hours_label.grid(row=6, column=0, padx=10, pady=10)

        self.library_hours_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.library_hours_entry.grid(row=6, column=1, padx=10, pady=10)

        self.scholarship_label = tk.Label(self, text="Scholarship Application Deadline? (y/n):", font=("Arial", 12, "bold"))
        self.scholarship_label.grid(row=7, column=0, padx=10, pady=10)

        self.scholarship_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.scholarship_entry.grid(row=7, column=1, padx=10, pady=10)

        self.cultural_event_label = tk.Label(self, text="Cultural Event? (y/n):", font=("Arial", 12, "bold"))
        self.cultural_event_label.grid(row=8, column=0, padx=10, pady=10)

        self.cultural_event_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.cultural_event_entry.grid(row=8, column=1, padx=10, pady=10)

        self.online_course_label = tk.Label(self, text="Free Online Course on Mental Health? (y/n):", font=("Arial", 12, "bold"))
        self.online_course_label.grid(row=9, column=0, padx=10, pady=10)

        self.online_course_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.online_course_entry.grid(row=9, column=1, padx=10, pady=10)

        self.gym_membership_label = tk.Label(self, text="Discounted Gym Membership? (y/n):", font=("Arial", 12, "bold"))
        self.gym_membership_label.grid(row=10, column=0, padx=10, pady=10)

        self.gym_membership_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.gym_membership_entry.grid(row=10, column=1, padx=10, pady=10)

        self.blood_donation_label = tk.Label(self, text="Blood Donation Drive? (y/n):", font=("Arial", 12, "bold"))
        self.blood_donation_label.grid(row=11, column=0, padx=10, pady=10)

        self.blood_donation_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.blood_donation_entry.grid(row=11, column=1, padx=10, pady=10)

        self.job_fair_label = tk.Label(self, text="Job Fair? (y/n):", font=("Arial", 12, "bold"))
        self.job_fair_label.grid(row=12, column=0, padx=10, pady=10)

        self.job_fair_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.job_fair_entry.grid(row=12, column=1, padx=10, pady=10)

        self.vaccination_label = tk.Label(self, text="Free Vaccination Drive? (y/n):", font=("Arial", 12, "bold"))
        self.vaccination_label.grid(row=13, column=0, padx=10, pady=10)

        self.vaccination_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.vaccination_entry.grid(row=13, column=1, padx=10, pady=10)

        self.hour_label = tk.Label(self, text="Enter Hour (24hr format):", font=("Arial", 12, "bold"))
        self.hour_label.grid(row=14, column=0, padx=10, pady=10)

        self.hour_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.hour_entry.grid(row=14, column=1, padx=10, pady=10)

        self.minute_label = tk.Label(self, text="Enter Minute:", font=("Arial", 12, "bold"))
        self.minute_label.grid(row=15, column=0, padx=10, pady=10)

        self.minute_entry = tk.Entry(self, width=30, font=("Arial", 12))
        self.minute_entry.grid(row=15, column=1, padx=10, pady=10)

        self.send_button = tk.Button(self, text="Send", font=("Arial", 12, "bold"), bg="green", fg="white")
        self.send_button["command"] = self.send_message
        self.send_button.grid(row=16, column=1, padx=10, pady=10)

    def send_message(self):
        messenger = StudentEngagementMessenger()
        student_name = self.student_name_entry.get()
        mobile = self.mobile_entry.get()

        pending_assignments = self.pending_assignments_entry.get().lower() == 'y'
        pending_fee = self.pending_fee_entry.get().lower() == 'y'
        less_attendance = self.less_attendance_entry.get().lower() == 'y'
        seminar = self.seminar_entry.get().lower() == 'y'
        library_hours = self.library_hours_entry.get().lower() == 'y'
        scholarship = self.scholarship_entry.get().lower() == 'y'
        cultural_event = self.cultural_event_entry.get().lower() == 'y'
        online_course = self.online_course_entry.get().lower() == 'y'
        gym_membership = self.gym_membership_entry.get().lower() == 'y'
        blood_donation = self.blood_donation_entry.get().lower() == 'y'
        job_fair = self.job_fair_entry.get().lower() == 'y'
        vaccination = self.vaccination_entry.get().lower() == 'y'

        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())

        message = messenger.generate_message(student_name, pending_assignments, pending_fee, less_attendance,
                                         seminar, library_hours, scholarship, cultural_event,
                                         online_course, gym_membership, blood_donation, job_fair, vaccination)
        messenger.send_message(student_name, mobile, message, hour, minute)


root = tk.Tk()
root.title("Student Engagement Messenger")
root.geometry("400x600")
app = Application(master=root)
app.mainloop()
import tkinter as tk
from Backend import create_employee

class Frontend :
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("My App")
        
        self.create_employee_label = tk.Label(self.root,text="CREATE EMPLOYEE",font=(20))
        self.create_employee_label.pack(pady=5)

        self.first_name_label = tk.Label(self.root,text="First Name:")
        self.first_name_label.pack(pady=5)
        self.first_name_text = tk.Text(self.root,height=1,font=("Arial",16))
        self.first_name_text.pack(padx=200,pady=10)

        self.last_name_label = tk.Label(self.root,text="Last Name:")
        self.last_name_label.pack(pady=5)
        self.last_name_text = tk.Text(self.root,height=1,font=("Arial",16))
        self.last_name_text.pack(padx=200,pady=10)

        self.rank_label = tk.Label(self.root,text="Rank:")
        self.rank_label.pack(padx=5)
        self.rank_text = tk.Text(self.root,height=1,font=("Arial",16))
        self.rank_text.pack(padx=200,pady=10)

        self.email_label = tk.Label(self.root,text="Email:")
        self.email_label.pack(padx=5)
        self.email_text = tk.Text(self.root,height=1,font=("Arial",16))
        self.email_text.pack(padx=200,pady=10)

        self.password_label = tk.Label(self.root,text="Password:")
        self.password_label.pack(padx=5)
        self.password_text = tk.Text(self.root,height=1,font=("Arial",16))
        self.password_text.pack(padx=200,pady=10)

        self.submit_button = tk.Button(self.root,text="Submit Employee",font=("Arial",10),command=self.fun_create_employee)
        self.submit_button.pack(pady=10)

        self.root.mainloop()

    def fun_create_employee(self):
        self.first_name = self.first_name_text.get("1.0",tk.END)
        self.last_name = self.last_name_text.get("1.0",tk.END)
        self.rank = self.rank_text.get("1.0",tk.END)
        self.email = self.email_text.get("1.0",tk.END)
        self.password = self.password_text.get("1.0",tk.END)

        create_employee(self,self.first_name, self.last_name, self.rank, self.email, self.password)
        

Frontend()

from tkinter import *
from tkinter import messagebox as tmsg
import mysql.connector


class project:
    def __init__(self,top):
        self.top = top
        self.top.geometry("500x500")
        self.top.config(bg="lightblue")
        self.top.title("Record Manager")
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 500) // 2
        self.top.geometry(f"500x500+{x}+{y}")

        self.button1 = Button(self.top,text="ADD RECORD",bg="orange",font=("Arial",13,"bold"),highlightthickness=1, highlightcolor="black", command=self.Add_record)
        self.button1.place(x=140,y=70,width=200)

        self.button2 = Button(self.top,text=" SEARCH RECORD",bg="orange",font=("Arial",13,"bold"),highlightthickness=1, highlightcolor="black",command=self.search_record)
        self.button2.place(x=140,y=140,width=200)

        self.button3 = Button(self.top,text="SHOW DETAILS",bg="orange",font=("Arial",13,"bold"),highlightthickness=1, highlightcolor="black",command=self.show_details)
        self.button3.place(x=140,y=210,width=200)

        self.button4 = Button(self.top,text="DELETE RECORD",bg="orange",font=("Arial",13,"bold"),highlightthickness=1, highlightcolor="black",command=self.delete)
        self.button4.place(x=140,y=280,width=200)

        self.button5 = Button(self.top,text="EXIT",bg="red",font=("Arial",13,"bold"),highlightthickness=1, highlightcolor="black",command=self.close)
        self.button5.place(x=185,y=350,width=100)

    def Add_record(self):
        self.top.geometry("500x500")
        self.top.config(bg="lightblue")

        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()

        x = (screen_width - 500) // 2
        y = (screen_height - 500) // 2

        self.top.geometry(f"500x500+{x}+{y}")
        self.frame_0 = Frame(self.top,bg="cyan")
        self.frame_0.pack(side="left",fill="both",expand=True)

        self.name = Label(self.frame_0,text="REGISTRATION FOR NEW USER ",bg="orange",font=("arial",12,"bold"))
        self.name.place(x=25,y=10,)
        self.l1=Label(self.frame_0,text="Name :",bg="cyan",font=("arial",12,"bold"),borderwidth=5)
        self.l1.place(x=30,y=50,width=60)
        self.e1 = Entry(self.frame_0,font=("arial",15,"bold"),highlightthickness=1,highlightcolor="black",borderwidth=5)
        self.e1.place(x=200,y=50)
        self.l2 = Label(self.frame_0,text="E-mail :",bg="cyan",font=("arial",12,"bold"),borderwidth=5)
        self.l2.place(x=25,y=100)
        self.e2 = Entry(self.frame_0, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black",borderwidth=5)
        self.e2.place(x=200, y=100)
        self.l3 = Label(self.frame_0, text="Password :", bg="cyan", font=("arial", 12, "bold"), borderwidth=5)
        self.l3.place(x=25, y=150)
        self.e3 = Entry(self.frame_0, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black", borderwidth=5,show="*",)
        self.e3.place(x=200, y=150)
        self.l4 = Label(self.frame_0, text="CONTACT NUMBER :", bg="cyan", font=("arial", 12, "bold"), borderwidth=5)
        self.l4.place(x=25, y=200)
        self.e4 = Entry(self.frame_0, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black", borderwidth=6)
        self.e4.place(x=200, y=200)
        self.l5 = Label(self.frame_0, text="Blood Group :", bg="cyan", font=("arial", 12, "bold"), borderwidth=5)
        self.l5.place(x=25, y=250)
        self.e5 = Entry(self.frame_0, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black", borderwidth=6)
        self.e5.place(x=200, y=250)
        self.l6 = Label(self.frame_0, text="Address :", bg="cyan", font=("arial", 12, "bold"), borderwidth=5)
        self.l6.place(x=25, y=300)
        self.e6 = Entry(self.frame_0, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black", borderwidth=6)
        self.e6.place(x=200, y=300)

        self.e7 = Button(self.frame_0, text="REGISTER",font=("arial", 12, "bold"), bg="white",highlightthickness=1, highlightcolor="black", borderwidth=10,command=self.register)
        self.e7.place(x=130, y=380,width=130)
        self.e8 = Button(self.frame_0, text="BACK", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10, command=self.back1)
        self.e8.place(x=300, y=380, width=100)

    def back1(self):
        self.frame_0.pack_forget()
        self.button31 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button31.place(x=140, y=70, width=200)

        self.button32 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button32.place(x=140, y=140, width=200)

        self.button33 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button33.place(x=140, y=210, width=200)

        self.button34 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button34.place(x=140, y=280, width=200)

        self.button35 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button35.place(x=185, y=350, width=100)
        self.frame_0.destroy()

    def back(self):
        self.frame_1.pack_forget()
        self.button21 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button21.place(x=140, y=70, width=200)

        self.button22 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button22.place(x=140, y=140, width=200)

        self.button23 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button23.place(x=140, y=210, width=200)

        self.button24 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button24.place(x=140, y=280, width=200)

        self.button25 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button25.place(x=185, y=350, width=100)
        self.frame_1.destroy()

    def search_record(self):
        self.top.geometry("600x500")
        self.top.config(bg="lightblue")

        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()

        x = (screen_width - 600) // 2
        y = (screen_height - 500) // 2

        self.top.geometry(f"600x500+{x}+{y}")
        self.frame_1 = Frame(self.top, bg="cyan")
        self.frame_1.pack(side="left", fill="both", expand=True)

        self.l11 = Label(self.frame_1, text="Search NAME of User ", bg="cyan", font=("arial", 14, "bold"), borderwidth=10)
        self.l11.place(x=2, y=20, width=500)
        self.e12 = Entry(self.frame_1, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black", borderwidth=6)
        self.e12.place(x=120, y=90,width=300)
        self.e13 = Button(self.frame_1, text="show ", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10,command=self.Search_Record)
        self.e13.place(x=210, y=150, width=100)
        self.e14 = Button(self.frame_1, text="BACK", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10, command=self.back)
        self.e14.place(x=210, y=210, width=100)

    def Search_Record(self):
        search_name = self.e12.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="#####",
            password="######",
            database="Register"
        )

        cursor = connection.cursor()

        search_query = "SELECT * FROM Add_Data WHERE name = %s"

        cursor.execute(search_query, (search_name,))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            self.display_results(results)
        else:
            tmsg.showinfo("Not Found", "Name not found in the database.")

    def display_results(self, results):
        self.frame_1.destroy()

        self.frame_4 = Frame(self.top, bg="cyan")
        self.frame_4.pack(side="left", fill="both", expand=True)

        self.l21 = Label(self.frame_4, text="Here are Details..", font=("arial", 16, "bold"), bg="yellow")
        self.l21.place(x=10, y=10)

        l22 = Listbox(self.frame_4, width=100, height=15,bg="cyan",font=("arial",10,"bold"),highlightthickness=0,borderwidth=0)
        l22.place(x=10,y=100)
        self.l23 = Button(self.frame_4, text="Back", bg="orange",command=self.back4,fg="black",font=("arial",13,"bold"))
        self.l23.place(x=280, y=220,width=100)

        for result in results:
            l22.insert(END, result)

    def back4(self):
        self.frame_4.pack_forget()
        self.button61 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button61.place(x=140, y=70, width=200)

        self.button62 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button62.place(x=140, y=140, width=200)

        self.button63 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button63.place(x=140, y=210, width=200)

        self.button64 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button64.place(x=140, y=280, width=200)

        self.button65 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button65.place(x=185, y=350, width=100)
        self.frame_4.destroy()

    def delete(self):
        self.top.geometry("500x500")
        self.top.config(bg="lightblue")

        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()

        x = (screen_width - 500) // 2
        y = (screen_height - 500) // 2

        self.top.geometry(f"500x500+{x}+{y}")
        self.frame_2 = Frame(self.top, bg="cyan")
        self.frame_2.pack(side="left", fill="both", expand=True)

        self.l11 = Label(self.frame_2, text="Name :", bg="cyan", font=("arial", 14, "bold"), borderwidth=5)
        self.l11.place(x=100, y=150, width=60)
        self.e12 = Entry(self.frame_2, font=("arial", 15, "bold"), highlightthickness=1, highlightcolor="black",borderwidth=5)
        self.e12.place(x=200, y=150)
        self.l13 = Label(self.frame_2, text="DELETE DATA", bg="cyan", font=("arial", 14, "bold"),borderwidth=10)
        self.l13.place(x=2, y=20, width=500)
        self.l14 = Button(self.frame_2, text="BACK", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10, command=self.back2)
        self.l14.place(x=200, y=250, width=100)
        self.l15 = Button(self.frame_2, text="DELETE", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10,command=self.Delete_Record)
        self.l15.place(x=200, y=200, width=100)

    def Delete_Record(self):
        name_to_delete = self.e12.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="#####",
            password="#####",
            database="Register"
        )

        cursor = connection.cursor()

        select_query = "SELECT * FROM Add_Data WHERE name = %s"
        values = (name_to_delete,)
        cursor.execute(select_query, values)
        record = cursor.fetchone()

        if record:
            delete_query = "DELETE FROM Add_Data WHERE name = %s"
            cursor.execute(delete_query, values)
            connection.commit()

            cursor.close()
            connection.close()

            tmsg.showinfo("Record Deleted", f"Record for {name_to_delete} has been deleted.")
        else:
            tmsg.showinfo("Record Not Found", f"Record for {name_to_delete} was not found in the database.")

    def back2(self):
        self.frame_2.pack_forget()
        self.button41 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button41.place(x=140, y=70, width=200)
        self.button42 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button42.place(x=140, y=140, width=200)
        self.button43 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button43.place(x=140, y=210, width=200)
        self.button44 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button44.place(x=140, y=280, width=200)
        self.button45 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button45.place(x=185, y=350, width=100)
        self.frame_2.destroy()

    def show_details(self):
        self.top.geometry("500x500")
        self.top.config(bg="lightblue")
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()

        x = (screen_width - 500) // 2
        y = (screen_height - 500) // 2

        self.top.geometry(f"500x500+{x}+{y}")
        self.frame_3 = Frame(self.top, bg="cyan")
        self.frame_3.pack(side="left", fill="both", expand=True)
        self.l51 = Label(self.frame_3, text="Click the button to get Record ", bg="cyan", font=("arial", 14, "bold"),borderwidth=10)
        self.l51.place(x=2, y=20, width=500)
        self.l52 = Button(self.frame_3, text="SHOW DETAILS", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10,command=self.show_all_details)
        self.l52.place(x=120, y=100, width=250)
        self.l52 = Button(self.frame_3, text="BACK", font=("arial", 12, "bold"), bg="white", highlightthickness=1,highlightcolor="black", borderwidth=10, command=self.back3)
        self.l52.place(x=200, y=200, width=100)

    def back3(self):
        self.frame_3.pack_forget()
        self.button51 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button51.place(x=140, y=70, width=200)
        self.button52 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button52.place(x=140, y=140, width=200)
        self.button53 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button53.place(x=140, y=210, width=200)
        self.button54 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button54.place(x=140, y=280, width=200)
        self.button55 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button55.place(x=185, y=350, width=100)
        self.frame_3.destroy()

    def show_all_details(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="#####",
            password="",
            database="Register"
        )

        cursor = connection.cursor()

        search_query = "SELECT * FROM Add_Data"

        cursor.execute(search_query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            self.display_results1(results)
        else:
            tmsg.showinfo("Not Found", "Name not found in the database.")

    def display_results1(self, results):
        self.frame_3.destroy()

        self.frame_5 = Frame(self.top, bg="cyan")
        self.frame_5.pack(side="left", fill="both", expand=True)

        self.l21 = Label(self.frame_5, text="Here are Details..", font=("arial", 16, "bold"), bg="yellow")
        self.l21.place(x=10, y=10)

        result_listbox = Listbox(self.frame_5, width=100, height=15,bg="cyan",font=("arial",10,"bold"),highlightthickness=0,borderwidth=0)
        result_listbox.place(x=10,y=100)
        self.back_btn_return2 = Button(self.frame_5, text="Back", bg="orange",command=self.back5,fg="black",font=("arial",13,"bold"))
        self.back_btn_return2.place(x=300, y=420,width=100)

        for result in results:
            result_listbox.insert(END, result)

    def back5(self):
        self.frame_5.pack_forget()
        self.button51 = Button(self.top, text="ADD RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.Add_record)
        self.button51.place(x=140, y=70, width=200)
        self.button52 = Button(self.top, text="SEARCH RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.search_record)
        self.button52.place(x=140, y=140, width=200)
        self.button53 = Button(self.top, text="SHOW DETAILS", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.show_details)
        self.button53.place(x=140, y=210, width=200)
        self.button54 = Button(self.top, text="DELETE RECORD", bg="orange", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black",command=self.delete)
        self.button54.place(x=140, y=280, width=200)
        self.button55 = Button(self.top, text="EXIT", bg="red", font=("Arial", 13, "bold"), highlightthickness=1,highlightcolor="black", command=self.close)
        self.button55.place(x=185, y=350, width=100)
        self.frame_5.destroy()

    def register(self):
        name = self.e1.get()
        email = self.e2.get()
        password = self.e3.get()
        contact_no = self.e4.get()
        blood_group = self.e5.get()
        address = self.e6.get()
        connection = mysql.connector.connect(
            host="localhost",
            user="#####",
            password="#####",
            database="Register")

        cursor = connection.cursor()
        insert_query = "INSERT INTO Add_data (name, email, password,contact_no, blood_group,address) VALUES (%s, %s, %s, %s, %s,%s)"
        cursor.execute(insert_query, (name, email,password, contact_no, blood_group, address))
        connection.commit()
        cursor.close()
        connection.close()
        tmsg.showinfo("Success", "Record saved successfully!")

    def close(self):
        exit()

top = Tk()
a = project(top)
top.mainloop()

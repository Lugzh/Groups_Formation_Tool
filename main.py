import random
from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class ListaAlunos:
    def __init__(self):
        self.list_students = []
        self.list_groups = []

    def read_students(self):
        with open('alunos_0069.txt', 'r', encoding='utf-8') as archive:
            self.list_students = archive.read().splitlines()
            random.shuffle(self.list_students)

    def calculate_group(self, max_students):
        return len(self.list_students) / max_students


    def create_groups(self, num_groups):
        self.list_students = sorted(self.list_students, key=lambda skill: int(skill.split(" - ")[1]),
                                   reverse=True)

        group = 0
        while group < num_groups:
            self.list_groups.append([])
            group += 1

        while self.list_students:
            group = 0
            while group < num_groups:
                if len(self.list_students) > 0:
                    self.list_groups[group].append(self.list_students.pop())
                    group += 1
                else:
                    break

        group = 0
        while group < num_groups:

            group += 1

        with open('grupos.txt', 'w', encoding='utf-8') as archive:
            group = 0
            while group < num_groups:
                archive.write(f'Grupo: {group + 1}\n'
                              f'Total de Alunos: {len(self.list_groups[group])}\n'
                              f'{self.list_groups[group]}\n')
                group += 1
        os.startfile("grupos.txt")

class Interface:
    def __init__(self,master = None):
        self.object = ListaAlunos()

        self.lf_first = LabelFrame(root, text='Information entry', fg="#0b0d8c")
        self.lf_first.grid(pady=3, padx=30)
        self.lf_first.configure(bg="#b7a5c4")
        self.first_Contanier = Frame(master)
        self.first_Contanier.grid(row=0,column=0)

        self.lf_second= LabelFrame(root, text='Selector', fg="#0b0d8c")
        self.lf_second.grid(pady=3, padx=30)
        self.lf_second.configure(bg="#b7a5c4")
        self.second_Contanier = Frame(master)
        self.second_Contanier.grid(row=1,column=0)

        self.lf_third= LabelFrame(root, text='Numbers entry', fg="#0b0d8c")
        self.lf_third.grid(pady=3, padx=3)
        self.lf_third.configure(bg="#b7a5c4")
        self.third_Contanier = Frame(master)
        self.third_Contanier.grid(row=2,column=0)

        self.lf_fourth= LabelFrame(root, text='Information output', fg="#0b0d8c")
        self.lf_fourth.grid(pady=3, padx=3)
        self.lf_fourth.configure(bg="#b7a5c4")
        self.fourth_Contanier = Frame(master)
        self.fourth_Contanier.grid(row=3,column=0)

        self.select_archive = Button(self.lf_first,text="Choice a archive",command=self.way_of_archive)
        self.select_archive.grid(row=0,column=0,padx=3)

        def edit_archive_txt():
            os.startfile("alunos_0069.txt")

        self.edit_archive = Button(self.lf_first, text="Edit Archive", command= edit_archive_txt)
        self.edit_archive.grid(row=0,column=1,padx=3)

        label = ttk.Label(self.lf_second,text="Choose a group formation option:")
        label.grid(row=2,columnspan=3)

        self.choice = tk.StringVar()
        self.combobox = ttk.Combobox(self.lf_second, textvariable=self.choice)
        self.combobox['values'] = ('Students Quantity', 'Groups Quantity')
        self.combobox['state'] = 'readonly'
        self.combobox.grid(row=3,columnspan=3)

        def redirect(event):
            """ handle the month changed event """

            if self.choice.get() == 'Students Quantity':
                for widget in self.lf_third.winfo_children():
                    widget.destroy()
                for widget in self.lf_fourth.winfo_children():
                    widget.destroy()

                label = Label(self.lf_third, text="Enter the number of students per group:")
                label.grid(row=4,columns=3,)
                qtt_students = Entry(self.lf_third)
                qtt_students["width"] = 30
                qtt_students.grid(row=5,columns=3)
                def to_execute():
                    qtt_students_int = int(qtt_students.get())
                    num_group = self.object.calculate_group(qtt_students_int)
                    self.object.create_groups(num_group)
                button = Button(self.lf_fourth, text="Random Now", command=to_execute)
                button.pack(pady=7)
            elif self.choice.get() == 'Groups Quantity':
                for widget in self.lf_third.winfo_children():
                    widget.destroy()
                for widget in self.lf_fourth.winfo_children():
                    widget.destroy()
                label = Label(self.lf_third, text="Enter the number of groups: ",anchor = "e")
                label.grid(row=4,columnspan=4,sticky="we")
                qtt_students = Entry(self.lf_third)
                qtt_students["width"] = 30
                qtt_students.grid(row=5,columnspan=4,sticky="we")
                def to_execute():
                    num_group = int(qtt_students.get())
                    self.object.create_groups(num_group)
                button = Button(self.lf_fourth, text="Random Now", command=to_execute)
                button.pack(pady=7)

        self.combobox.bind('<<ComboboxSelected>>',redirect)

    def way_of_archive(self):
        default_window = Tk().withdraw()
        way_of_archive = askopenfilename(filetypes=(("Text files", "*.txt"), ("Files csv", "*.csv")))
        self.object.read_students()
        selected = Label(self.lf_first,text=f"Registered successfully")
        selected.grid(row=1,columnspan=3,pady=5)

root = Tk()
root.resizable(False, False)
root.geometry("250x300")
root.configure(background="#40BFDB")
root.title("Sorteia.ai")
Interface(root)
root.mainloop()

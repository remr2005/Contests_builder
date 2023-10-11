from cryptography.fernet import Fernet
import base64
code = bytes("""
import customtkinter as ctk
import os
from tkinter import filedialog
import shutil

class App(ctk.CTk):
    in_entry = None
    out_entry = None
    link_entry = None
    num_entry = None
    def __init__(self):
        ctk.CTk.__init__(self)
        # Настройки окна
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.geometry("800x800")
        self.title("Contests builder(ft morpeh2005ka)")

        # НАСТРОЙКИ
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="НАСТРОЙКИ").place(relx=0.43, rely=0.01, relwidth=0.2, relheight=0.03)
        self.link_entry = ctk.CTkEntry(self, textvariable="")

        # Входные файлы
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="Входные файлы").place(relx=0, rely=0.05, relwidth=0.25, relheight=0.1)
        Button_in = ctk.CTkButton(self,text = "...")
        Button_in.bind("<ButtonPress-1>",self.in_file_d)
        Button_in.place(relx=0.77, rely=0.05, relwidth=0.227, relheight=0.1)
        self.in_entry = ctk.CTkEntry(self, textvariable="")
        self.in_entry.place(relx=0.26, rely=0.05, relwidth=0.5, relheight=0.1)

        # Выходные файлы
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="Папка назначения").place(relx=0, rely=0.16, relwidth=0.25, relheight=0.1)
        Button_out = ctk.CTkButton(self, text="...")
        Button_out.bind("<ButtonPress-1>",self.out_file_d)
        Button_out.place(relx=0.77, rely=0.16, relwidth=0.227, relheight=0.1)
        self.out_entry = ctk.CTkEntry(self, textvariable="")
        self.out_entry.place(relx=0.26, rely=0.16, relwidth=0.5, relheight=0.1)

        # Ссылка на контест
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="Ссылка на контест(необязательна)").place(relx=0, rely=0.27, relwidth=0.3, relheight=0.1)
        self.link_entry = ctk.CTkEntry(self, textvariable="")
        self.link_entry.place(relx=0.31, rely=0.27, relwidth=0.688, relheight=0.1)

        # Номер контеста
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="№ контеста").place(relx=0, rely=0.38, relwidth=0.3, relheight=0.1)
        self.num_entry = ctk.CTkEntry(self, textvariable="")
        self.num_entry.place(relx=0.31, rely=0.38, relwidth=0.688, relheight=0.1)

        # Кнопка создания проекта
        Button_run = ctk.CTkButton(self, text="Создать проект для гита")
        Button_run.place(relx=0.26, rely=0.49, relwidth=0.5, relheight=0.1)
        Button_run.bind("<ButtonPress-1>",self.make_project)

        # Пост-скриптум
        ctk.CTkLabel(self,
                     bg_color="black",
                     text="Программа рассчитана на то, что вы нумеруйте свои файлы, например: 1.cpp,2.go и т.д.\\nКроме того ручная работа всё ещё присутствует, так как вам нужно будет вводить  наз-\\nвание заданий самостоятельно(мне лень заниматься парсингом)"
                     ).place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.39)
        self.link_entry = ctk.CTkEntry(self, textvariable="")

        self.mainloop()
    def in_file_d(self,event):
        self.in_entry.delete(0, len(self.in_entry.get()))
        path = filedialog.askopenfilenames()
        self.in_entry.insert(0,"".join([i+";" for i in path]))
    def out_file_d(self,event):
        self.out_entry.delete(0, len(self.out_entry.get()))
        path = filedialog.askdirectory()
        self.out_entry.insert(0, path)
    def make_project(self,event):
        i = 1
        md_txt = "|[Контест " + self.num_entry.get() +"](" + self.link_entry.get() + ") |  | \\n| --- | :-: |\\n"
        pat = self.out_entry.get()
        #pat = pat.replace("/","\\\\")
        os.chdir(pat)
        path = "contest_" + self.double_num(int(self.num_entry.get()))
        #path = path.replace("/","\\\\")
        os.mkdir(path)
        arrs = sorted(self.in_entry.get().split(";"))
        for string in arrs:
            if string == '':continue
            a = string.split(".")
            if len(a) == 1:break
            os.chdir(pat + '/' + path)
            str_i = self.double_num(i)
            os.mkdir(str_i)
            shutil.copy(string,pat + '/'+ path + '/' +str_i + '/' + "main."+a[1])
            md_txt+="| [" + str(i) +". Название](./contest_" + self.double_num(int(self.num_entry.get())) + "/"+ str_i +"/main."+a[1]+") | ![](./img/" + a[1] + ".png) |\\n"
            i+=1
        os.chdir(pat)
        my_file = open("ReadMe.txt", "w+")
        my_file.write(md_txt)
        my_file.close()
    def double_num(self,a):
        return a if a>9 else "0" + str(a)
def main():
    App()

if __name__ == '__main__':
    main()
""", 'utf-8')
key = Fernet.generate_key()
encruption_type = Fernet(key)
encrypted_message = encruption_type.encrypt(code)
dec_message = encruption_type.decrypt(encrypted_message)
exec(dec_message)

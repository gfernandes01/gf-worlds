from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
import os
from PIL import Image


class ConverterWindow:
    if __name__ == '__main__':
        img = ''
        import_file_path = ''
        root = Tk()
        obj = ConverterWindow
        root.mainloop()

    def __init__(self, root):
        self.root = root
        self.root.title('Converter ICO')
        self.root.geometry('500x240')
        self.root.resizable(False, False)

        self.title = Label(self.root, text='Converter ICO', font=('helvetica', 24), fg='blue')
        self.title.place(x=150, y=4)
        Label(self.root, text="Select Input Image", font=('helvetica', 11), fg='blue').place(x=43, y=70)

        self.input = Entry(self.root, width=42, font=('helvetica', 10), bg='lightgrey', relief=GROOVE, borderwidth=2)
        self.input.place(x=45, y=100, height=33)

        btn_convert = Button(self.root, relief=FLAT, text='Choose file', font=('helvetica', 10, 'bold'), bg='blue',
                             fg='white', command=self.openfile)
        btn_convert.place(x=355, y=100, width=95, height=32)
        btn_convert = Button(self.root, relief=FLAT, text='Convert to ICO', font=('helvetica', 12, 'bold'), bg='blue',
                             fg='white', command=self.convertToICO)
        btn_convert.place(x=182, y=163, wigth=130, height=40)

    def openfile(self):
        # Função para abrir o dialogbox e fazer a entrada da imagem
        global img, import_file_path
        import_file_path = tkinter.filedialog.askopenfilename(defaultextension='.png', filetypes=[(
            'PNG Files', '*.png'), ('JPEG Files', '*.jpg'), ('ALL Files', '*.')])
        self.input.delete(0, END)
        self.input.insert(0, import_file_path)
        img = Image.open(import_file_path)

    def convertToICO(self):
        # Função para transformar o arquivo de imagem em .ico
        global img, import_file_path
        print(os.path.exists(import_file_path))
        if os.path.exists(import_file_path) == True:
            if os.path.isfile(import_file_path) == True:
                export_file_path = tkinter.filedialog.asksaveasfilename(defaultextension='.ico', filetypes=[(
                    'ICO Files', '*.ico')])
                img.save(export_file_path)
                messagebox.showinfo('Success', 'File converted and saved')
            else:
                messagebox.showerror('Failed', 'Image file`s path does not exists')



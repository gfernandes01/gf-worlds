from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd

class Demo(object):
	def __init__(self, master):
		frame = Frame(master)
		frame.grid()
		tabControl = ttk.Notebook(root)
		tabControl.configure(width=550, height=350)

		self.option = StringVar()
		self.options = ["Option Menu", "Combo Box"]
		self.option.set(0)

		self.divPrimeira = ttk.Frame(tabControl)
		tabControl.add(self.divPrimeira, text="Tab 1")
		tabControl.grid()

		self.divSegunda = ttk.Frame(tabControl)
		tabControl.add(self.divSegunda, text="Tab 2")
		tabControl.grid()

		self.widgets()


	def widgets(self):
		labelFrame = LabelFrame(self.divPrimeira, text="Label Frame", width=550, height=350)
		labelFrame.grid(column=0, row=0)
		labelFrame.grid_propagate(0)

		label = Label(labelFrame, text="Label - TEXTO PURO")
		label.grid(column=1, row=0)

		entry = Entry(labelFrame, width=45)
		entry.grid(column=0, row=1, columnspan=3)
		entry.insert(0, "Entry field")

		radioButton1 = Radiobutton(labelFrame, text="RADIO SELECT 1", value=0)
		radioButton1.grid(column=0, row=2)
		radioButton2 = Radiobutton(labelFrame, text="RADIO SELECT 2", value=1)
		radioButton2.grid(column=1, row=2)
		checkButton = Checkbutton(labelFrame, text="Check")
		checkButton.grid(column=2, row=2)

		button = Button(labelFrame, text="Butão")
		button.grid(column=0, row=3)

		menuButton = Menubutton(labelFrame, text="Menu Button")
		menuButton.grid(column=1, row=3)
		menuButton.menu = Menu(menuButton, tearoff=0)
		menuButton["menu"] = menuButton.menu
		menuButton.menu.add_checkbutton(label="primeiro", variable=None)
		menuButton.menu.add_checkbutton(label="ultimo", variable=None)

		escala = Scale(labelFrame, from_=0, to=100, orient=HORIZONTAL)
		escala.grid(column=2, row=4)

		barraDeRolagem = Scrollbar(labelFrame)
		barraDeRolagem.grid(column=2, row=4)

		list = Listbox(labelFrame, yscrollcommand=barraDeRolagem.set, height=5)
		for line in range(5):
			list.insert(END, "ELEMENTO da CAIXA da LISTA "+str(line))
		list.grid(column=2, row=4)
		barraDeRolagem.config(command=list.yview)

		optionMenu = OptionMenu(labelFrame, self.option, self.options)
		optionMenu.grid(column=0, row=5)

		comboBox = ttk.Combobox(labelFrame, values=self.options)
		comboBox.grid(column=1, row=5)
		comboBox.current(0)

		barraDeProgresso = Progressbar(labelFrame, orient=HORIZONTAL, length=100, mode='determinate')
		barraDeProgresso["value"] = 25
		barraDeProgresso.grid(column=2, row=5)

		treeview = ttk.Treeview(self.divSegunda)
		treeview["columns"] = ("1", "2", "3")
		treeview.column("1", width=25)
		treeview.column("2", width=25)
		treeview.column("3", width=25)
		treeview.heading("1", text="primeiro")
		treeview.heading("2", text="segundo")
		treeview.heading("3", text="terceiro")
		treeview.insert("", 'end', text="LINHA 1", values=("TREE", "_", "View"))
		treeview.insert("", 'end', text="LINHA 2", values=("TREE", "_", "View"))
		treeview.insert("", 'end', text="LINHA 3", values=("TREE", "_", "View"))
		treeview.grid(column=0, row=0)
		treeview.grid_propagate(0)

if __name__ =='__main__':
	root = Tk()
	root.title("TKINTER - DEMONSTRAÇÃO")
	Demo(root)
	root.mainloop()
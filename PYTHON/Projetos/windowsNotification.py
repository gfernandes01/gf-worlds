import os
from win10toast import ToastNotifier

def notification():
	# MUDAR DIRETORIO para a LOCALIZAÇÃO dos SCRIPTS
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	toast = ToastNotifier() # Instancia do Modulo ToastNotifier
	title = "Notification" # TITULO da MENSAGEM EXIBIDA
	message = "Me siga no LINKED-IN : https://clck.ru/VJqzg"
	# COLOCAR UMA IMAGEM NO DIRETORIO DO SCRIPT
	icon = "icon.ico"
	length = 30
	toast.show_toast(title, message, duration=length, icon_path=icon)

notification()
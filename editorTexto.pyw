from functools import partial
from Tkinter import *
from tkFileDialog import *

def compilar_arquivo():
	texto = sheet.get("1.0",END)
		
	#Criacao da Janela de Codigo Compilado

	janelaComp = Tk()
	janelaComp.title("Codigo Compilado ASM")
	janelaComp.geometry("500x600+300+100")

	#Criacao do codigo de maquina
	sheetCompiled = Text(janelaComp, height=35, width=66)
	sheetCompiled.place(x = 14, y = 50)
	sheetCompiled.insert(INSERT, texto)
	
	#Botao de salvar arquivo em Disco
	saveFileButton = Button(janelaComp, width = 10, text = "Salvar", command = salvamento_de_arquivoASM)
	saveFileButton.place(x = 200, y = 12)
	
	janelaComp.mainloop()
	
def salvamento_de_arquivoASM():
	place = asksaveasfile(mode='w', defaultextension=".asm")
	if place is None:
		return None 
	text = str(sheet.get(1.0,END))
	place.write(text)
	place.close()

def salvamento_de_arquivo():### Problema aqui###
	place = asksaveasfile(mode='w', defaultextension=".txt")
	if place is None:
		return None 
	text = str(sheet.get(1.0,END))
	place.write(text)
	place.close()
	
def abertura_de_arquivo():
	fileName = askopenfilename( filetypes = (("*","*.txt"), ("All files","*.*")))
	if fileName is None:
		return None
	sheet.delete("1.0",END)
	arq = open(fileName)
	for linha in arq:
		sheet.insert(INSERT, linha)
	arq.close()
	
#Janela de amostra do Codigo compilado
def Functions_click(Botao):
	try:
		if(Botao["text"] == "Compilar"):
			compilar_arquivo()
			print(Botao["text"])
		if(Botao["text"] == "Abrir"):
				abertura_de_arquivo()
		if(Botao["text"] == "Salvar"):
			salvamento_de_arquivo() 
			
	except:
		pass
#Criacao da Janela

janelaPrin = Tk()

janelaPrin.title("Editor de Texto - Por: Joselito Junior")

janelaPrin.geometry("500x600+300+100")

#Criacao do espaco de entrada de texto

sheet = Text(janelaPrin, height=35, width=66)

sheet.place(x = 14, y = 50)

#Botao de Compilar Texto
#compilebutton = Button(janelaPrin, width = 10, text = "Compilar")

#compilebutton["command"] = partial(Functions_click, compilebutton)

#compilebutton.place(x = 200, y = 550)

#Botao de abrir arquivo em Disco

openFileButton = Button(janelaPrin, width = 10, text = "Abrir")

openFileButton["command"] = partial(Functions_click, openFileButton)

openFileButton.place(x = 14, y = 12)

#Botao de salvar arquivo em Disco

saveFileButton = Button(janelaPrin, width = 10, text = "Salvar")

saveFileButton["command"] = partial(Functions_click, saveFileButton)

saveFileButton.place(x = 130, y = 12)

#Texto de identificacao de alunos 

textID = Label(janelaPrin, text = "Editor de Texto - Por: Joselito Junior")

textID.place(x = 270, y = 12)

janelaPrin.mainloop()


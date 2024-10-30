import tkinter as tk
from tkinter import messagebox

alunos = {}

def cadastrar_aluno():
    nome = entry_nome.get()
    if nome and nome not in alunos:
        alunos[nome] = []
        messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
    elif nome in alunos:
        messagebox.showwarning("Atenção", f"Aluno {nome} já está cadastrado.")
    else:
        messagebox.showwarning("Atenção", "Por favor, insira o nome do aluno.")

def adicionar_nota():
    nome = entry_nome.get()
    try:
        nota = float(entry_nota.get())
        if nome in alunos:
            if len(alunos[nome]) < 2: 
                if 0 <= nota <= 10:
                    alunos[nome].append(nota)
                    messagebox.showinfo("Sucesso", f"Nota {nota} adicionada ao aluno {nome}.")
                    entry_nota.delete(0, tk.END)
                else:
                    messagebox.showwarning("Atenção", "A nota deve estar entre 0 e 10.")
            else:
                messagebox.showwarning("Atenção", f"O aluno {nome} já possui 2 notas cadastradas.")
        else:
            messagebox.showwarning("Atenção", f"Aluno {nome} não encontrado.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para a nota.")

def consultar_notas():
    nome = entry_nome.get()
    if nome in alunos:
        notas = alunos[nome]
        if notas:
            media = sum(notas) / len(notas)
            resultado = f"Notas do aluno {nome}: {notas}\nMédia do aluno {nome}: {media:.2f}"
            messagebox.showinfo("Consulta de Notas", resultado)
        else:
            messagebox.showwarning("Atenção", f"O aluno {nome} não possui notas cadastradas.")
    else:
        messagebox.showwarning("Atenção", f"Aluno {nome} não encontrado.")

window = tk.Tk()
window.title("Sistema de Notas de Alunos")

label_nome = tk.Label(window, text="Nome do Aluno:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(window)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_nota = tk.Label(window, text="Nota:")
label_nota.grid(row=1, column=0, padx=10, pady=10)
entry_nota = tk.Entry(window)
entry_nota.grid(row=1, column=1, padx=10, pady=10)

btn_cadastrar = tk.Button(window, text="Cadastrar Aluno", command=cadastrar_aluno)
btn_cadastrar.grid(row=2, column=0, padx=10, pady=10)

btn_adicionar = tk.Button(window, text="Adicionar Nota", command=adicionar_nota)
btn_adicionar.grid(row=2, column=1, padx=10, pady=10)

btn_consultar = tk.Button(window, text="Consultar Notas", command=consultar_notas)
btn_consultar.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
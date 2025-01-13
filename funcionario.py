import tkinter as tk
from tkinter import messagebox

funcionarios = []

def cadastrar_funcionario(entry_nome_funcionario, entry_cargo_funcionario, frame_lista_funcionarios):
    nome = entry_nome_funcionario.get().strip()
    cargo = entry_cargo_funcionario.get().strip()

    if not nome or not cargo:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    funcionario = {"nome": nome, "cargo": cargo}
    funcionarios.append(funcionario)

    entry_nome_funcionario.delete(0, tk.END)
    entry_cargo_funcionario.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Funcionário '{nome}' cadastrado com sucesso!")
    atualizar_lista_funcionarios(frame_lista_funcionarios)

def atualizar_lista_funcionarios(frame_lista_funcionarios):
    for widget in frame_lista_funcionarios.winfo_children():
        widget.destroy()

    for i, funcionario in enumerate(funcionarios):
        tk.Label(frame_lista_funcionarios, text=f"{funcionario['nome']} - {funcionario['cargo']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)
        tk.Button(frame_lista_funcionarios, text="Remover", command=lambda i=i: remover_funcionario(i, frame_lista_funcionarios)).pack(pady=2)

def remover_funcionario(index, frame_lista_funcionarios):
    del funcionarios[index]
    atualizar_lista_funcionarios(frame_lista_funcionarios)
    messagebox.showinfo("Sucesso", "Funcionário removido com sucesso!")
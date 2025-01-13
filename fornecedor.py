import tkinter as tk
from tkinter import messagebox

fornecedores = []

def cadastrar_fornecedor(entry_nome_fornecedor, entry_telefone_fornecedor, frame_lista_fornecedores):
    nome = entry_nome_fornecedor.get().strip()
    telefone = entry_telefone_fornecedor.get().strip()

    if not nome or not telefone:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    fornecedor = {"nome": nome, "telefone": telefone}
    fornecedores.append(fornecedor)

    entry_nome_fornecedor.delete(0, tk.END)
    entry_telefone_fornecedor.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Fornecedor '{nome}' cadastrado com sucesso!")
    atualizar_lista_fornecedores(frame_lista_fornecedores)

def atualizar_lista_fornecedores(frame_lista_fornecedores):
    for widget in frame_lista_fornecedores.winfo_children():
        widget.destroy()

    for fornecedor in fornecedores:
        tk.Label(frame_lista_fornecedores, text=f"{fornecedor['nome']} - {fornecedor['telefone']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)
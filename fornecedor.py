import tkinter as tk
from tkinter import messagebox

fornecedores = []

def cadastrar_fornecedor(entry_nome_fornecedor, entry_telefone_fornecedor, entry_email_fornecedor, frame_lista_fornecedores):
    nome = entry_nome_fornecedor.get().strip()
    telefone = entry_telefone_fornecedor.get().strip()
    email = entry_email_fornecedor.get().strip()

    if not nome or not telefone or not email:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    fornecedor = {"nome": nome, "telefone": telefone, "email": email}
    fornecedores.append(fornecedor)

    entry_nome_fornecedor.delete(0, tk.END)
    entry_telefone_fornecedor.delete(0, tk.END)
    entry_email_fornecedor.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Fornecedor '{nome}' cadastrado com sucesso!")
    atualizar_lista_fornecedores(frame_lista_fornecedores)

def atualizar_lista_fornecedores(frame_lista_fornecedores):
    for widget in frame_lista_fornecedores.winfo_children():
        widget.grid_forget()  # Remove os widgets existentes sem destruí-los

    # Exibe os fornecedores com grid para garantir uma organização mais controlada
    for i, fornecedor in enumerate(fornecedores):
        label_fornecedor = tk.Label(frame_lista_fornecedores, text=f"{fornecedor['nome']} - {fornecedor['telefone']} - {fornecedor['email']}", font=("Arial", 10), anchor="w")
        label_fornecedor.grid(row=i, column=0, sticky="w", pady=2, padx=10)  # Organiza a exibição dos fornecedores no grid

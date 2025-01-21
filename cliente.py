import tkinter as tk
from tkinter import messagebox

clientes = []

# Função para validar o telefone
def validar_telefone(telefone):
    telefone = telefone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) != 11 or not telefone.isdigit():
        return False
    return True

def cadastrar_cliente(entry_nome_cliente, entry_telefone_cliente, entry_email_cliente, frame_lista_clientes):
    nome = entry_nome_cliente.get().strip()
    telefone = entry_telefone_cliente.get().strip()
    email = entry_email_cliente.get().strip()

    if not nome or not telefone or not email:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido! Deve ter 11 dígitos numéricos.")
        return

    cliente = {"nome": nome, "telefone": telefone, "email": email}
    clientes.append(cliente)

    entry_nome_cliente.delete(0, tk.END)
    entry_telefone_cliente.delete(0, tk.END)
    entry_email_cliente.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Cliente '{nome}' cadastrado com sucesso!")
    atualizar_lista_clientes(frame_lista_clientes)

def atualizar_lista_clientes(frame_lista_clientes):
    for widget in frame_lista_clientes.winfo_children():
        widget.destroy()

    for i, cliente in enumerate(clientes):
        tk.Label(frame_lista_clientes, text=f"{cliente['nome']} - {cliente['telefone']} - {cliente['email']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)
        tk.Button(frame_lista_clientes, text="Remover", command=lambda i=i: remover_cliente(i, frame_lista_clientes)).pack(pady=2)

def remover_cliente(index, frame_lista_clientes):
    del clientes[index]
    atualizar_lista_clientes(frame_lista_clientes)
    messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")

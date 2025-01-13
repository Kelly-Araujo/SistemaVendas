import tkinter as tk
from tkinter import messagebox

clientes = []

def cadastrar_cliente(entry_nome_cliente, entry_telefone_cliente, frame_lista_clientes):
    nome = entry_nome_cliente.get().strip()
    telefone = entry_telefone_cliente.get().strip()

    if not nome or not telefone:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)

    entry_nome_cliente.delete(0, tk.END)
    entry_telefone_cliente.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Cliente '{nome}' cadastrado com sucesso!")
    atualizar_lista_clientes(frame_lista_clientes)

def atualizar_lista_clientes(frame_lista_clientes):
    for widget in frame_lista_clientes.winfo_children():
        widget.destroy()

    for i, cliente in enumerate(clientes):
        tk.Label(frame_lista_clientes, text=f"{cliente['nome']} - {cliente['telefone']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)
        tk.Button(frame_lista_clientes, text="Remover", command=lambda i=i: remover_cliente(i, frame_lista_clientes)).pack(pady=2)

def remover_cliente(index, frame_lista_clientes):
    del clientes[index]
    atualizar_lista_clientes(frame_lista_clientes)
    messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
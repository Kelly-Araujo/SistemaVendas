import tkinter as tk
from tkinter import messagebox

produtos = []

def cadastrar_produto(entry_nome_produto, entry_preco_produto, entry_estoque_produto, frame_lista_produtos):
    nome = entry_nome_produto.get().strip()
    preco = entry_preco_produto.get().strip()
    estoque = entry_estoque_produto.get().strip()

    if not nome or not preco or not estoque:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        estoque = float(estoque)
    except ValueError:
        messagebox.showerror("Erro", "Preço e estoque devem ser valores numéricos!")
        return

    produto = {"nome": nome, "preco": preco, "estoque": estoque}
    produtos.append(produto)

    entry_nome_produto.delete(0, tk.END)
    entry_preco_produto.delete(0, tk.END)
    entry_estoque_produto.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado com sucesso!")
    atualizar_lista_produtos(frame_lista_produtos)

def atualizar_lista_produtos(frame_lista_produtos):
    for widget in frame_lista_produtos.winfo_children():
        widget.destroy()

    for produto in produtos:
        tk.Label(frame_lista_produtos, text=f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}, Estoque: {produto['estoque']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)
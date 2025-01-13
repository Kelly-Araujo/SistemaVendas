import tkinter as tk
from tkinter import messagebox, ttk

# Listas para armazenar produtos, vendas, clientes e fornecedores
produtos = []
vendas = []
clientes = []
fornecedores = []
funcionarios = []

# Função para cadastrar produtos
def cadastrar_produto():
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
    atualizar_lista_produtos()

# Função para registrar vendas
def registrar_venda():
    nome_produto = entry_nome_venda.get()
    quantidade = entry_quantidade_venda.get()

    if not nome_produto or not quantidade:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser numérica!")
        return

    produto_encontrado = None
    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        messagebox.showerror("Erro", "Produto não encontrado!")
        return

    if produto_encontrado["estoque"] < quantidade:
        messagebox.showerror("Erro", "Estoque insuficiente!")
        return

    produto_encontrado["estoque"] -= quantidade
    total_venda = produto_encontrado["preco"] * quantidade
    vendas.append({"produto": nome_produto, "quantidade": quantidade, "total": total_venda})

    entry_nome_venda.delete(0, tk.END)
    entry_quantidade_venda.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Venda registrada com sucesso! Total: R${total_venda:.2f}")
    atualizar_lista_produtos()

# Função para gerar relatório
def gerar_relatorio():
    relatorio = "Relatório de Vendas:\n\n"
    if not vendas:
        relatorio += "Nenhuma venda registrada.\n"
    else:
        for venda in vendas:
            relatorio += f"Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Total: R${venda['total']:.2f}\n"
    
    relatorio += "\nEstoque Atual:\n"
    for produto in produtos:
        relatorio += f"{produto['nome']}: {produto['estoque']} unidades\n"

    messagebox.showinfo("Relatório", relatorio)

# Função para cadastrar clientes
def cadastrar_cliente():
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

# Função para cadastrar fornecedores
def cadastrar_fornecedor():
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

# Função para cadastrar funcionários
def cadastrar_funcionario():
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

# Função para atualizar a lista de produtos
def atualizar_lista_produtos():
    for widget in frame_lista_produtos.winfo_children():
        widget.destroy()

    for produto in produtos:
        tk.Label(frame_lista_produtos, text=f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}, Estoque: {produto['estoque']}", font=("Arial", 10), anchor="w").pack(fill='x', pady=2)

# Função para mostrar o cadastro de produtos
def mostrar_cadastro_produtos():
    frame_produtos.pack(fill='both', padx=10, pady=10)
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()

# Função para mostrar o cadastro de vendas
def mostrar_registro_vendas():
    frame_produtos.pack_forget()
    frame_vendas.pack(fill='both', padx=10, pady=10)
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()

# Função para mostrar o cadastro de clientes
def mostrar_cliente():
    frame_cliente.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()

# Função para mostrar o cadastro de fornecedores
def mostrar_fornecedor():
    frame_fornecedor.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_funcionario.pack_forget()

# Função para mostrar o cadastro de funcionários
def mostrar_funcionario():
    frame_funcionario.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()



# Função para exibir a aba de Relatório
def mostrar_relatorio():
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()
    frame_relatorio.pack(fill='both', padx=10, pady=10)

# Janela principal
root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("1000x700")

# Frame de navegação lateral
frame_nav = tk.Frame(root, bg="#2196F3", width=200)
frame_nav.pack(side="left", fill="y")

# Botões do menu lateral
btn_cadastrar_produtos = tk.Button(frame_nav, text="Cadastro de Produtos", command=mostrar_cadastro_produtos, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_cadastrar_produtos.pack(fill='x', pady=5)

btn_registrar_vendas = tk.Button(frame_nav, text="Registro de Vendas", command=mostrar_registro_vendas, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_registrar_vendas.pack(fill='x', pady=5)

btn_cliente = tk.Button(frame_nav, text="Cadastro de Clientes", command=mostrar_cliente, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_cliente.pack(fill='x', pady=5)

btn_fornecedor = tk.Button(frame_nav, text="Cadastro de Fornecedores", command=mostrar_fornecedor, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_fornecedor.pack(fill='x', pady=5)

btn_funcionario = tk.Button(frame_nav, text="Cadastro de Funcionários", command=mostrar_funcionario, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_funcionario.pack(fill='x', pady=5)

btn_relatorio = tk.Button(frame_nav, text="Relatório", command=mostrar_relatorio, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
btn_relatorio.pack(fill='x', pady=5)

# Frames principais para cada aba
frame_produtos = tk.Frame(root)
frame_vendas = tk.Frame(root)
frame_cliente = tk.Frame(root)
frame_fornecedor = tk.Frame(root)
frame_funcionario = tk.Frame(root)
frame_relatorio = tk.Frame(root)
frame_lista_produtos = tk.Frame(frame_produtos)

# Campos para cadastro de produtos
tk.Label(frame_produtos, text="Nome do Produto", font=("Arial", 12)).pack(pady=5)
entry_nome_produto = tk.Entry(frame_produtos, font=("Arial", 12))
entry_nome_produto.pack(pady=5)

tk.Label(frame_produtos, text="Preço", font=("Arial", 12)).pack(pady=5)
entry_preco_produto = tk.Entry(frame_produtos, font=("Arial", 12))
entry_preco_produto.pack(pady=5)

tk.Label(frame_produtos, text="Estoque", font=("Arial", 12)).pack(pady=5)
entry_estoque_produto = tk.Entry(frame_produtos, font=("Arial", 12))
entry_estoque_produto.pack(pady=5)

btn_cadastrar_produto = tk.Button(frame_produtos, text="Cadastrar Produto", command=cadastrar_produto, font=("Arial", 12))
btn_cadastrar_produto.pack(pady=10)

# Campos para registrar vendas
tk.Label(frame_vendas, text="Nome do Produto", font=("Arial", 12)).pack(pady=5)
entry_nome_venda = tk.Entry(frame_vendas, font=("Arial", 12))
entry_nome_venda.pack(pady=5)

tk.Label(frame_vendas, text="Quantidade", font=("Arial", 12)).pack(pady=5)
entry_quantidade_venda = tk.Entry(frame_vendas, font=("Arial", 12))
entry_quantidade_venda.pack(pady=5)

btn_registrar_venda = tk.Button(frame_vendas, text="Registrar Venda", command=registrar_venda, font=("Arial", 12))
btn_registrar_venda.pack(pady=10)

# Campos para cadastrar cliente
tk.Label(frame_cliente, text="Nome do Cliente", font=("Arial", 12)).pack(pady=5)
entry_nome_cliente = tk.Entry(frame_cliente, font=("Arial", 12))
entry_nome_cliente.pack(pady=5)

tk.Label(frame_cliente, text="Telefone", font=("Arial", 12)).pack(pady=5)
entry_telefone_cliente = tk.Entry(frame_cliente, font=("Arial", 12))
entry_telefone_cliente.pack(pady=5)

btn_cadastrar_cliente = tk.Button(frame_cliente, text="Cadastrar Cliente", command=cadastrar_cliente, font=("Arial", 12))
btn_cadastrar_cliente.pack(pady=10)

# Campos para cadastrar fornecedor
tk.Label(frame_fornecedor, text="Nome do Fornecedor", font=("Arial", 12)).pack(pady=5)
entry_nome_fornecedor = tk.Entry(frame_fornecedor, font=("Arial", 12))
entry_nome_fornecedor.pack(pady=5)

tk.Label(frame_fornecedor, text="Telefone", font=("Arial", 12)).pack(pady=5)
entry_telefone_fornecedor = tk.Entry(frame_fornecedor, font=("Arial", 12))
entry_telefone_fornecedor.pack(pady=5)

btn_cadastrar_fornecedor = tk.Button(frame_fornecedor, text="Cadastrar Fornecedor", command=cadastrar_fornecedor, font=("Arial", 12))
btn_cadastrar_fornecedor.pack(pady=10)

# Campos para cadastrar funcionário
tk.Label(frame_funcionario, text="Nome do Funcionário", font=("Arial", 12)).pack(pady=5)
entry_nome_funcionario = tk.Entry(frame_funcionario, font=("Arial", 12))
entry_nome_funcionario.pack(pady=5)

tk.Label(frame_funcionario, text="Cargo", font=("Arial", 12)).pack(pady=5)
entry_cargo_funcionario = tk.Entry(frame_funcionario, font=("Arial", 12))
entry_cargo_funcionario.pack(pady=5)

btn_cadastrar_funcionario = tk.Button(frame_funcionario, text="Cadastrar Funcionário", command=cadastrar_funcionario, font=("Arial", 12))
btn_cadastrar_funcionario.pack(pady=10)

# Exibir o primeiro frame
mostrar_cadastro_produtos()

root.mainloop()

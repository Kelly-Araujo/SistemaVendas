import tkinter as tk
from produto import cadastrar_produto, atualizar_lista_produtos
from venda import registrar_venda, gerar_relatorio
from cliente import cadastrar_cliente, atualizar_lista_clientes
from fornecedor import cadastrar_fornecedor, atualizar_lista_fornecedores
from funcionario import cadastrar_funcionario, atualizar_lista_funcionarios

# Funções para mostrar cada aba
def mostrar_cadastro_produtos():
    frame_produtos.pack(fill='both', padx=10, pady=10)
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()
    frame_relatorio.pack_forget()

def mostrar_registro_vendas():
    frame_produtos.pack_forget()
    frame_vendas.pack(fill='both', padx=10, pady=10)
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()
    frame_relatorio.pack_forget()

def mostrar_cliente():
    frame_cliente.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_fornecedor.pack_forget()
    frame_funcionario.pack_forget()
    frame_relatorio.pack_forget()

def mostrar_fornecedor():
    frame_fornecedor.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_funcionario.pack_forget()
    frame_relatorio.pack_forget()

def mostrar_funcionario():
    frame_funcionario.pack(fill='both', padx=10, pady=10)
    frame_produtos.pack_forget()
    frame_vendas.pack_forget()
    frame_cliente.pack_forget()
    frame_fornecedor.pack_forget()
    frame_relatorio.pack_forget()

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
frame_lista_clientes = tk.Frame(frame_cliente)
frame_lista_funcionarios = tk.Frame(frame_funcionario)
frame_lista_fornecedores = tk.Frame(frame_fornecedor)

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

btn_cadastrar_produto = tk.Button(frame_produtos, text="Cadastrar Produto", command=lambda: cadastrar_produto(entry_nome_produto, entry_preco_produto, entry_estoque_produto, frame_lista_produtos), font=("Arial", 12))
btn_cadastrar_produto.pack(pady=10)

frame_lista_produtos.pack(fill='both', expand=True)

# Campos para registrar vendas
tk.Label(frame_vendas, text="Nome do Produto", font=("Arial", 12)).pack(pady=5)
entry_nome_venda = tk.Entry(frame_vendas, font=("Arial", 12))
entry_nome_venda.pack(pady=5)

tk.Label(frame_vendas, text="Quantidade", font=("Arial", 12)).pack(pady=5)
entry_quantidade_venda = tk.Entry(frame_vendas, font=("Arial", 12))
entry_quantidade_venda.pack(pady=5)

tk.Label(frame_vendas, text="Desconto (%)", font=("Arial", 12)).pack(pady=5)
entry_desconto_venda = tk.Entry(frame_vendas, font=("Arial", 12))
entry_desconto_venda.pack(pady=5)

btn_registrar_venda = tk.Button(frame_vendas, text="Registrar Venda", command=lambda: registrar_venda(entry_nome_venda, entry_quantidade_venda, entry_desconto_venda, frame_lista_produtos), font=("Arial", 12))
btn_registrar_venda.pack(pady=10)

# Campos para cadastrar cliente
tk.Label(frame_cliente, text="Nome do Cliente", font=("Arial", 12)).pack(pady=5)
entry_nome_cliente = tk.Entry(frame_cliente, font=("Arial", 12))
entry_nome_cliente.pack(pady=5)

tk.Label(frame_cliente, text="Telefone", font=("Arial", 12)).pack(pady=5)
entry_telefone_cliente = tk.Entry(frame_cliente, font=("Arial", 12))
entry_telefone_cliente.pack(pady=5)

btn_cadastrar_cliente = tk.Button(frame_cliente, text="Cadastrar Cliente", command=lambda: cadastrar_cliente(entry_nome_cliente, entry_telefone_cliente, frame_lista_clientes), font=("Arial", 12))
btn_cadastrar_cliente.pack(pady=10)

frame_lista_clientes.pack(fill='both', expand=True)

# Campos para cadastrar fornecedor
tk.Label(frame_fornecedor, text="Nome do Fornecedor", font=("Arial", 12)).pack(pady=5)
entry_nome_fornecedor = tk.Entry(frame_fornecedor, font=("Arial", 12))
entry_nome_fornecedor.pack(pady=5)

tk.Label(frame_fornecedor, text="Telefone", font=("Arial", 12)).pack(pady=5)
entry_telefone_fornecedor = tk.Entry(frame_fornecedor, font=("Arial", 12))
entry_telefone_fornecedor.pack(pady=5)

btn_cadastrar_fornecedor = tk.Button(frame_fornecedor, text="Cadastrar Fornecedor", command=lambda: cadastrar_fornecedor(entry_nome_fornecedor, entry_telefone_fornecedor, frame_lista_fornecedores), font=("Arial", 12))
btn_cadastrar_fornecedor.pack(pady=10)

frame_lista_fornecedores.pack(fill='both', expand=True)

# Campos para cadastrar funcionário
tk.Label(frame_funcionario, text="Nome do Funcionário", font=("Arial", 12)).pack(pady=5)
entry_nome_funcionario = tk.Entry(frame_funcionario, font=("Arial", 12))
entry_nome_funcionario.pack(pady=5)

tk.Label(frame_funcionario, text="Cargo", font=("Arial", 12)).pack(pady=5)
entry_cargo_funcionario = tk.Entry(frame_funcionario, font=("Arial", 12))
entry_cargo_funcionario.pack(pady=5)

btn_cadastrar_funcionario = tk.Button(frame_funcionario, text="Cadastrar Funcionário", command=lambda: cadastrar_funcionario(entry_nome_funcionario, entry_cargo_funcionario, frame_lista_funcionarios), font=("Arial", 12))
btn_cadastrar_funcionario.pack(pady=10)

frame_lista_funcionarios.pack(fill='both', expand=True)

# Exibir o primeiro frame
mostrar_cadastro_produtos()

root.mainloop()
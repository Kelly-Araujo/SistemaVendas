import tkinter as tk
from produto import cadastrar_produto, atualizar_lista_produtos
from venda import registrar_venda
from cliente import cadastrar_cliente, atualizar_lista_clientes
from fornecedor import cadastrar_fornecedor, atualizar_lista_fornecedores
from funcionario import cadastrar_funcionario, atualizar_lista_funcionarios

# Funções para mostrar cada aba
def mostrar_frame(frame_atual):
    for frame in frames:
        frame.pack_forget()
    frame_atual.pack(fill="both", expand=True, padx=20, pady=20)

# Janela principal
root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("1100x750")
root.configure(bg="#f5f5f5")

# Frame de navegação lateral
frame_nav = tk.Frame(root, bg="#1E88E5", width=220)
frame_nav.pack(side="left", fill="y")

# Título do menu
tk.Label(frame_nav, text="Menu", font=("Arial", 18, "bold"), bg="#1E88E5", fg="white").pack(pady=20)

# Botões do menu lateral
menu_options = [
    ("Cadastro de Produtos", lambda: mostrar_frame(frame_produtos)),
    ("Registro de Vendas", lambda: mostrar_frame(frame_vendas)),
    ("Cadastro de Clientes", lambda: mostrar_frame(frame_cliente)),
    ("Cadastro de Fornecedores", lambda: mostrar_frame(frame_fornecedor)),
    ("Cadastro de Funcionários", lambda: mostrar_frame(frame_funcionario)),
]

for text, command in menu_options:
    btn = tk.Button(frame_nav, text=text, command=command, font=("Arial", 14), bg="#42A5F5", fg="white", relief="flat")
    btn.pack(fill="x", pady=10, padx=10)

# Frames principais para cada aba
frames = []
frame_produtos = tk.Frame(root, bg="#ffffff")
frame_vendas = tk.Frame(root, bg="#ffffff")
frame_cliente = tk.Frame(root, bg="#ffffff")
frame_fornecedor = tk.Frame(root, bg="#ffffff")
frame_funcionario = tk.Frame(root, bg="#ffffff")

frames.extend([frame_produtos, frame_vendas, frame_cliente, frame_fornecedor, frame_funcionario])

# Função para criar um campo de entrada com rótulo
def criar_campo(frame, texto_label):
    tk.Label(frame, text=texto_label, font=("Arial", 12), bg="#ffffff").pack(pady=5, anchor="w")
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.pack(pady=5, fill="x")
    return entry

# Cadastro de Produtos
frame_produtos_title = tk.Label(frame_produtos, text="Cadastro de Produtos", font=("Arial", 20, "bold"), bg="#ffffff")
frame_produtos_title.pack(pady=10)

entry_nome_produto = criar_campo(frame_produtos, "Nome do Produto")
entry_preco_produto = criar_campo(frame_produtos, "Preço")
entry_estoque_produto = criar_campo(frame_produtos, "Estoque")

btn_cadastrar_produto = tk.Button(
    frame_produtos,
    text="Cadastrar Produto",
    command=lambda: cadastrar_produto(entry_nome_produto, entry_preco_produto, entry_estoque_produto, frame_lista_produtos),
    font=("Arial", 12), bg="#42A5F5", fg="white"
)
btn_cadastrar_produto.pack(pady=20)

frame_lista_produtos = tk.Frame(frame_produtos, bg="#f5f5f5", relief="groove", bd=2)
frame_lista_produtos.pack(fill="both", expand=True, pady=10)

# Registro de Vendas
frame_vendas_title = tk.Label(frame_vendas, text="Registro de Vendas", font=("Arial", 20, "bold"), bg="#ffffff")
frame_vendas_title.pack(pady=10)

entry_nome_venda = criar_campo(frame_vendas, "Nome do Produto")
entry_quantidade_venda = criar_campo(frame_vendas, "Quantidade")
entry_desconto_venda = criar_campo(frame_vendas, "Desconto (%)")

btn_registrar_venda = tk.Button(
    frame_vendas,
    text="Registrar Venda",
    command=lambda: registrar_venda(entry_nome_venda, entry_quantidade_venda, entry_desconto_venda, frame_lista_produtos),
    font=("Arial", 12), bg="#42A5F5", fg="white"
)
btn_registrar_venda.pack(pady=20)

# Cadastro de Clientes
frame_cliente_title = tk.Label(frame_cliente, text="Cadastro de Clientes", font=("Arial", 20, "bold"), bg="#ffffff")
frame_cliente_title.pack(pady=10)

entry_nome_cliente = criar_campo(frame_cliente, "Nome do Cliente")
entry_telefone_cliente = criar_campo(frame_cliente, "Telefone")

btn_cadastrar_cliente = tk.Button(
    frame_cliente,
    text="Cadastrar Cliente",
    command=lambda: cadastrar_cliente(entry_nome_cliente, entry_telefone_cliente, frame_lista_clientes),
    font=("Arial", 12), bg="#42A5F5", fg="white"
)
btn_cadastrar_cliente.pack(pady=20)

frame_lista_clientes = tk.Frame(frame_cliente, bg="#f5f5f5", relief="groove", bd=2)
frame_lista_clientes.pack(fill="both", expand=True, pady=10)

# Cadastro de Fornecedores
frame_fornecedor_title = tk.Label(frame_fornecedor, text="Cadastro de Fornecedores", font=("Arial", 20, "bold"), bg="#ffffff")
frame_fornecedor_title.pack(pady=10)

entry_nome_fornecedor = criar_campo(frame_fornecedor, "Nome do Fornecedor")
entry_telefone_fornecedor = criar_campo(frame_fornecedor, "Telefone")

btn_cadastrar_fornecedor = tk.Button(
    frame_fornecedor,
    text="Cadastrar Fornecedor",
    command=lambda: cadastrar_fornecedor(entry_nome_fornecedor, entry_telefone_fornecedor, frame_lista_fornecedores),
    font=("Arial", 12), bg="#42A5F5", fg="white"
)
btn_cadastrar_fornecedor.pack(pady=20)

frame_lista_fornecedores = tk.Frame(frame_fornecedor, bg="#f5f5f5", relief="groove", bd=2)
frame_lista_fornecedores.pack(fill="both", expand=True, pady=10)

# Cadastro de Funcionários
frame_funcionario_title = tk.Label(frame_funcionario, text="Cadastro de Funcionários", font=("Arial", 20, "bold"), bg="#ffffff")
frame_funcionario_title.pack(pady=10)

entry_nome_funcionario = criar_campo(frame_funcionario, "Nome do Funcionário")
entry_cargo_funcionario = criar_campo(frame_funcionario, "Cargo")

btn_cadastrar_funcionario = tk.Button(
    frame_funcionario,
    text="Cadastrar Funcionário",
    command=lambda: cadastrar_funcionario(entry_nome_funcionario, entry_cargo_funcionario, frame_lista_funcionarios),
    font=("Arial", 12), bg="#42A5F5", fg="white"
)
btn_cadastrar_funcionario.pack(pady=20)

frame_lista_funcionarios = tk.Frame(frame_funcionario, bg="#f5f5f5", relief="groove", bd=2)
frame_lista_funcionarios.pack(fill="both", expand=True, pady=10)

# Exibir o primeiro frame
mostrar_frame(frame_produtos)

root.mainloop()
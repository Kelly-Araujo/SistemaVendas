import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from produto import cadastrar_produto, atualizar_lista_produtos
from venda import registrar_venda
from cliente import cadastrar_cliente, atualizar_lista_clientes
from fornecedor import cadastrar_fornecedor, atualizar_lista_fornecedores
from funcionario import cadastrar_funcionario, atualizar_lista_funcionarios

def mostrar_frame(frame_atual):
    for frame in frames:
        frame.grid_forget()
    frame_atual.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Função de validação para o telefone
def validar_telefone(telefone):
    telefone = telefone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(telefone) != 11 or not telefone.isdigit():
        return False
    return True

# Função para gerar o relatório
# Função para gerar o relatório
def gerar_relatorio():
    # Exemplo de dados - no seu código, esses dados seriam dinamicamente coletados
    vendas_today = 0  # Exemplo de número de vendas do dia
    clientes_novos_today = 0  # Exemplo de novos clientes do dia
    descontos_today = 0  # Exemplo de desconto total dado
    estoque_restante = 100  # Exemplo de estoque restante

    # Verifica se houve alguma ação no dia
    if vendas_today == 0 and clientes_novos_today == 0 and descontos_today == 0:
        relatorio = "Sem relatório disponível, nada ocorreu no dia."
    else:
        # Geração do relatório
        relatorio = f"Relatório do Dia ({datetime.now().strftime('%d/%m/%Y')})\n"
        relatorio += "="*30 + "\n"
        relatorio += f"Total de Vendas: {vendas_today}\n"
        relatorio += f"Novos Clientes: {clientes_novos_today}\n"
        relatorio += f"Descontos Concedidos: R${descontos_today}\n"
        relatorio += f"Estoque Restante: {estoque_restante} unidades\n"
        relatorio += "="*30 + "\n"

    # Exibe o relatório em uma nova janela
    messagebox.showinfo("Relatório do Dia", relatorio)

# Janela principal
root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("1100x750")
root.configure(bg="#f8f9fa")

# Estilo global
STYLE_BG = "#ffffff"
STYLE_HIGHLIGHT = "#1E88E5"
STYLE_TEXT = "#212529"
STYLE_BUTTON = "#007bff"
STYLE_HOVER = "#0056b3"
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 12, "bold")

# Configuração do grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Frame de navegação lateral
frame_nav = tk.Frame(root, bg=STYLE_HIGHLIGHT, width=220)
frame_nav.grid(row=0, column=0, sticky="ns")

tk.Label(frame_nav, text="Menu", font=("Segoe UI", 18, "bold"), bg=STYLE_HIGHLIGHT, fg="white").pack(pady=20)

menu_options = [
    ("Cadastro de Produtos", lambda: mostrar_frame(frame_produtos)),
    ("Registro de Vendas", lambda: mostrar_frame(frame_vendas)),
    ("Cadastro de Clientes", lambda: mostrar_frame(frame_cliente)),
    ("Cadastro de Fornecedores", lambda: mostrar_frame(frame_fornecedor)),
    ("Cadastro de Funcionários", lambda: mostrar_frame(frame_funcionario)),
    ("Relatório", gerar_relatorio),  # Botão de Relatório adicionado aqui
]

for text, command in menu_options:
    btn = tk.Button(
        frame_nav, text=text, command=command, font=FONT_BUTTON,
        bg=STYLE_BUTTON, fg="white", relief="flat", activebackground=STYLE_HOVER, activeforeground="white",
        height=2, bd=0
    )
    btn.pack(fill="x", pady=10, padx=10)

# Frames principais para cada aba
frames = []
frame_produtos = tk.Frame(root, bg=STYLE_BG, relief="groove", bd=2)
frame_vendas = tk.Frame(root, bg=STYLE_BG, relief="groove", bd=2)
frame_cliente = tk.Frame(root, bg=STYLE_BG, relief="groove", bd=2)
frame_fornecedor = tk.Frame(root, bg=STYLE_BG, relief="groove", bd=2)
frame_funcionario = tk.Frame(root, bg=STYLE_BG, relief="groove", bd=2)
frames.extend([frame_produtos, frame_vendas, frame_cliente, frame_fornecedor, frame_funcionario])

def criar_campo(frame, texto_label, placeholder=""):
    tk.Label(frame, text=texto_label, font=FONT_LABEL, bg=STYLE_BG, fg=STYLE_TEXT).pack(pady=5, anchor="w")
    
    # Função para limpar o placeholder
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=STYLE_TEXT)

    # Função para restaurar o placeholder
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry = tk.Entry(frame, font=FONT_LABEL, relief="groove", bd=2, fg="gray")
    entry.insert(0, placeholder)
    
    # Vincula eventos de foco ao campo
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    
    entry.pack(pady=5, fill="x")
    return entry

# Cadastro de Produtos
frame_produtos_title = tk.Label(frame_produtos, text="Cadastro de Produtos", font=FONT_TITLE, bg=STYLE_BG)
frame_produtos_title.pack(pady=10)

entry_nome_produto = criar_campo(frame_produtos, "Nome do Produto", "Ex: Produto A")
entry_preco_produto = criar_campo(frame_produtos, "Preço", "Ex: R$ 100,00")
entry_estoque_produto = criar_campo(frame_produtos, "Estoque", "Ex: 50")

btn_cadastrar_produto = tk.Button(
    frame_produtos, text="Cadastrar Produto",
    command=lambda: cadastrar_produto(entry_nome_produto, entry_preco_produto, entry_estoque_produto, frame_lista_produtos),
    font=FONT_BUTTON, bg=STYLE_BUTTON, fg="white", activebackground=STYLE_HOVER, activeforeground="white"
)
btn_cadastrar_produto.pack(pady=20)

frame_lista_produtos = tk.Frame(frame_produtos, bg="#e9ecef", relief="sunken", bd=2)
frame_lista_produtos.pack(fill="both", expand=True, pady=10)

# Registro de Vendas
frame_vendas_title = tk.Label(frame_vendas, text="Registro de Vendas", font=FONT_TITLE, bg=STYLE_BG)
frame_vendas_title.pack(pady=10)

entry_nome_venda = criar_campo(frame_vendas, "Nome do Produto", "Ex: Produto A")
entry_quantidade_venda = criar_campo(frame_vendas, "Quantidade", "Ex: 1")
entry_desconto_venda = criar_campo(frame_vendas, "Desconto (%)", "Ex: 10")

btn_registrar_venda = tk.Button(
    frame_vendas, text="Registrar Venda",
    command=lambda: registrar_venda(entry_nome_venda, entry_quantidade_venda, entry_desconto_venda, frame_lista_produtos),
    font=FONT_BUTTON, bg=STYLE_BUTTON, fg="white", activebackground=STYLE_HOVER, activeforeground="white"
)
btn_registrar_venda.pack(pady=20)

frame_lista_vendas = tk.Frame(frame_vendas, bg="#e9ecef", relief="sunken", bd=2)
frame_lista_vendas.pack(fill="both", expand=True, pady=10)

# Cadastro de Clientes
frame_cliente_title = tk.Label(frame_cliente, text="Cadastro de Clientes", font=FONT_TITLE, bg=STYLE_BG)
frame_cliente_title.pack(pady=10)

entry_nome_cliente = criar_campo(frame_cliente, "Nome do Cliente", "Ex: João da Silva")
entry_telefone_cliente = criar_campo(frame_cliente, "Telefone", "Ex: (11) 98765-4321")

btn_cadastrar_cliente = tk.Button(
    frame_cliente, text="Cadastrar Cliente",
    command=lambda: cadastrar_cliente(entry_nome_cliente, entry_telefone_cliente, frame_lista_clientes) if validar_telefone(entry_telefone_cliente.get()) else messagebox.showerror("Erro", "Telefone deve ser numérico e ter 11 dígitos!"),
    font=FONT_BUTTON, bg=STYLE_BUTTON, fg="white", activebackground=STYLE_HOVER, activeforeground="white"
)
btn_cadastrar_cliente.pack(pady=20)

frame_lista_clientes = tk.Frame(frame_cliente, bg="#e9ecef", relief="sunken", bd=2)
frame_lista_clientes.pack(fill="both", expand=True, pady=10)

# Cadastro de Fornecedores
frame_fornecedor_title = tk.Label(frame_fornecedor, text="Cadastro de Fornecedores", font=FONT_TITLE, bg=STYLE_BG)
frame_fornecedor_title.pack(pady=10)

entry_nome_fornecedor = criar_campo(frame_fornecedor, "Nome do Fornecedor", "Ex: Fornecedor X")
entry_telefone_fornecedor = criar_campo(frame_fornecedor, "Telefone", "Ex: (11) 98765-4321")

btn_cadastrar_fornecedor = tk.Button(
    frame_fornecedor, text="Cadastrar Fornecedor",
    command=lambda: cadastrar_fornecedor(entry_nome_fornecedor, entry_telefone_fornecedor, frame_lista_fornecedores) if validar_telefone(entry_telefone_fornecedor.get()) else messagebox.showerror("Erro", "Telefone deve ser numérico e ter 11 dígitos!"),
    font=FONT_BUTTON, bg=STYLE_BUTTON, fg="white", activebackground=STYLE_HOVER, activeforeground="white"
)
btn_cadastrar_fornecedor.pack(pady=20)

frame_lista_fornecedores = tk.Frame(frame_fornecedor, bg="#e9ecef", relief="sunken", bd=2)
frame_lista_fornecedores.pack(fill="both", expand=True, pady=10)

# Cadastro de Funcionários
frame_funcionario_title = tk.Label(frame_funcionario, text="Cadastro de Funcionários", font=FONT_TITLE, bg=STYLE_BG)
frame_funcionario_title.pack(pady=10)

entry_nome_funcionario = criar_campo(frame_funcionario, "Nome do Funcionário", "Ex: Maria Souza")
entry_telefone_funcionario = criar_campo(frame_funcionario, "Telefone", "Ex: (11) 98765-4321")

btn_cadastrar_funcionario = tk.Button(
    frame_funcionario, text="Cadastrar Funcionário",
    command=lambda: cadastrar_funcionario(entry_nome_funcionario, entry_telefone_funcionario, frame_lista_funcionarios) if validar_telefone(entry_telefone_funcionario.get()) else messagebox.showerror("Erro", "Telefone deve ser numérico e ter 11 dígitos!"),
    font=FONT_BUTTON, bg=STYLE_BUTTON, fg="white", activebackground=STYLE_HOVER, activeforeground="white"
)
btn_cadastrar_funcionario.pack(pady=20)

frame_lista_funcionarios = tk.Frame(frame_funcionario, bg="#e9ecef", relief="sunken", bd=2)
frame_lista_funcionarios.pack(fill="both", expand=True, pady=10)

# Exibe o primeiro frame
mostrar_frame(frame_produtos)

# Inicia a janela principal
root.mainloop()

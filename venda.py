import tkinter as tk
from tkinter import messagebox
from produto import produtos, atualizar_lista_produtos

vendas = []

def registrar_venda(entry_nome_venda, entry_quantidade_venda, entry_desconto_venda, frame_lista_produtos):
    nome_produto = entry_nome_venda.get()
    quantidade = entry_quantidade_venda.get()
    desconto = entry_desconto_venda.get()

    if not nome_produto or not quantidade:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        quantidade = int(quantidade)
        desconto = float(desconto) if desconto else 0.0
    except ValueError:
        messagebox.showerror("Erro", "Quantidade e desconto devem ser numéricos!")
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
    total_com_desconto = total_venda * ((100 - desconto) / 100)
    vendas.append({"produto": nome_produto, "quantidade": quantidade, "total": total_com_desconto})

    entry_nome_venda.delete(0, tk.END)
    entry_quantidade_venda.delete(0, tk.END)
    entry_desconto_venda.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Venda registrada com sucesso! Total com desconto: R${total_com_desconto:.2f}")
    
    # Atualizando a lista de produtos após a venda
    atualizar_lista_produtos(frame_lista_produtos)

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

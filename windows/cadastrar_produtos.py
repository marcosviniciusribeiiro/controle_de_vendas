from tkinter import Tk, StringVar, Label, Entry, Button, ttk
from tkinter.messagebox import showinfo ,showerror
from models.produtos_dao import Produtos

class P_Window:
    def __init__(self):
        self.produtos = Produtos()

        self.__new_preco__ = 0.0
        self.__new_estoque__ = 0

        self.window = Tk()
        self.window.geometry('600x600')
        self.window.resizable(False, False)
        self.window.title('Cadastro de Produtos')

        self.id = StringVar()
        self.nome = StringVar()
        self.preco = StringVar()
        self.estoque = StringVar()


        nome_label = Label(self.window, {'text': 'Nome do Produto:'})
        nome_label.pack()

        nome_entry = Entry(self.window, textvariable=self.nome, width=20)
        nome_entry.pack()

        preco_label = Label(self.window, {'text': 'Preço do Produto:'})
        preco_label.pack(pady=8)

        preco_entry = Entry(self.window, textvariable=self.preco, width=15)
        preco_entry.pack()

        estoque_label = Label(self.window, {'text': 'Estoque do Produto:'})
        estoque_label.pack(pady=8)

        estoque_entry = Entry(self.window, textvariable = self.estoque, width = 10)
        estoque_entry.pack()

        insert_button = Button(
            self.window, {'text': 'Adicionar Produto', 'bg': 'green', 'fg': 'white'},
            command=lambda: self.cadastrar_produto(self.nome.get(), self.preco.get(), self.estoque.get())
            if self.nome.get() != '' and self.preco.get() != '' and self.estoque.get() != '' else ''
        )
        insert_button.pack(pady=10)

        update_button = Button(
            self.window, {'text': 'Atualizar Produto', 'bg': '#FA5E09', 'fg': 'white'},
            command=lambda: self.atualizar_produto(self.id.get(), self.nome.get(), self.preco.get(), self.estoque.get())
            if self.id.get() != '' and self.nome.get() != '' and self.preco.get() != '' and self.estoque.get() != '' else ''
        )
        update_button.pack(pady=5)


        self.treeview = ttk.Treeview(self.window)
        self.treeview.bind('<Double-1>', self.populate_variables)

        table_label = Label(self.window, {'text': '___ Tabela de Produtos ___'})
        table_label.pack()

        self.treeview['columns'] = ('ID', 'Produto', 'Preço', 'Estoque')
        self.treeview.column('#0', width=75, minwidth=30)
        self.treeview.column('ID', width=40, minwidth=3)
        self.treeview.column('Produto', width=100, minwidth=20)
        self.treeview.column('Preço', width=75, minwidth=20)
        self.treeview.column('Estoque', width=60, minwidth=20)

        self.treeview.heading('#0', text='Label')
        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Produto', text='Produto')
        self.treeview.heading('Preço', text='Preço')
        self.treeview.heading('Estoque', text='Estoque')
        self.treeview.pack()

        delete_button = Button(
            self.window, {'text': 'Deletar Produto', 'bg': '#ED0000', 'fg': 'white'},
            command=lambda: self.deletar_produto()
        )
        delete_button.pack(pady=5)

        refresh_button = Button(
            self.window, {'text': 'Carregar Tabela', 'bg': '#1634FA', 'fg': 'white'},
            command=lambda: self.recarregar_tabela()
        )
        refresh_button.pack(pady=5)

    def cadastrar_produto(self, nome: str, preco: str, estoque: str) -> None:
        if self.validar_preco_estoque(preco, estoque):
            if self.produtos.insert(nome, self.__new_preco__, self.__new_estoque__):
                self.nome.set('')
                self.preco.set('')
                self.estoque.set('')
                self.populate_table()
                showinfo('Dados Cadastrados', 'O produto foi cadastrado com sucesso.')
            
            else:
                showerror('Erro', 'Não foi possivel cadastrar o produto.')

    def atualizar_produto(self, id: str, nome: str, preco: str, estoque: str) -> None:
        if self.validar_preco_estoque(preco, estoque):
            if self.produtos.update(int(id), nome, self.__new_preco__, self.__new_estoque__):
                self.id.set('')
                self.nome.set('')
                self.preco.set('')
                self.estoque.set('')
                self.populate_table()
                showinfo('Dados Atualizados', 'O produto foi atualizado com sucesso.')
            else:
                showerror('Erro', 'Não foi possivel atualizar o produto.')

    def deletar_produto(self) -> None:
        table_data = self.treeview.selection()
        if len(table_data) > 0:
            if self.produtos.delete(int(table_data[0])):
                self.id.set('')
                self.nome.set('')
                self.preco.set('')
                self.estoque.set('')
                self.populate_table()
                showinfo('Dados Excluidos', 'O produto foi excluido com sucesso.')
            else:
                showerror('Erro', 'Não foi possível excluir o produto.')
  
    def recarregar_tabela(self):
        self.populate_table()


    def validar_preco_estoque(self, preco: str, estoque: str) -> bool:
        preco = preco.replace(',', '.')
        try:
            self.__new_preco__ = float(preco)
            self.__new_estoque__ = int(estoque)

        except:
            showerror(f'Valor Incorreto', 'Digite um valor numérico no campo de preço.')
            return False
        
        else:
            return True

    def populate_variables(self, event=None):
        table_data = self.treeview.selection()
        if len(table_data) > 0:
            produto = self.produtos.select_by_id(int(table_data[0]))

            if produto is not None:
                self.id.set(produto[0])
                self.nome.set(produto[1])
                self.preco.set(str(produto[2]))
                self.estoque.set(str(produto[3]))
            else:
                showerror('Error', 'Não foi possível encontrar o produto com este ID.')

    def populate_table(self) -> None:
        self.clear_table_data()
        selecao_de_produtos = self.produtos.select_all()
        for produto in selecao_de_produtos:
            self.treeview.insert('', index='end', text='Produto', iid=str(produto[0]),
                                 values=(produto[0], produto[1], produto[2], produto[3]))

    def clear_table_data(self) -> None:
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
    def run(self) -> None:
        self.window.mainloop()
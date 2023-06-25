import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


class Biblioteca:
        def __init__(self):
            self.livros_comuns = []
            self.livros_raros = []


class Livro:
        def __init__(self, titulo, autor, isbn, ano_publicacao, categoria):
            self.titulo = titulo
            self.autor = autor
            self.isbn = isbn
            self.ano_publicacao = ano_publicacao
            self.categoria = categoria


class LivroComum(Livro):
        def __init__(self, titulo, autor, isbn, ano_publicacao, categoria, numero_de_copias):
            super().__init__(titulo, autor, isbn, ano_publicacao, categoria)
            self.numero_de_copias = numero_de_copias
            self.emprestado = False
            self.nome_usuario = ""
            self.email_usuario = ""


class LivroRaro(Livro):
        def __init__(self, titulo, autor, isbn, ano_publicacao, categoria, edicao, estado, numero_de_copias):
            super().__init__(titulo, autor, isbn, ano_publicacao, categoria)
            self.edicao = edicao
            self.estado = estado
            self.numero_de_copias = numero_de_copias
            self.emprestado = False
            self.nome_usuario = ""
            self.email_usuario = ""



class InterfaceGrafica:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("SGB")
        self.livros = [] 
        self.livros_comuns = [] 
        self.livros_raros = []  
        self.funcionarios_cadastrados = []
        self.clientes_cadastrados = []

        self.botao_funcionario = tk.Button(janela, text="Funcionário", command=self.abrir_tela_funcionario)
        self.botao_funcionario.pack(pady=10)

        self.botao_cliente = tk.Button(janela, text="Cliente", command=self.abrir_tela_cliente)
        self.botao_cliente.pack(pady=10)


    #########################################################################################################
    #-----------------------------------inicio menu funcionario--------------------------------------------#

    def abrir_tela_menu_funcionario(self):
        tela_menu_funcionario = tk.Toplevel(self.janela)
        tela_menu_funcionario.title("Menu do Funcionário")
        tela_menu_funcionario.geometry("500x400")

        botao_adicionar_comum = tk.Button(tela_menu_funcionario, text="Adicionar um livro comum à biblioteca", command=self.adicionar_livro_comum)
        botao_adicionar_comum.pack(pady=10)

        botao_adicionar_raro = tk.Button(tela_menu_funcionario, text="Adicionar um livro raro à biblioteca", command=self.adicionar_livro_raro)
        botao_adicionar_raro.pack(pady=10)

        botao_remover = tk.Button(tela_menu_funcionario, text="Remover um livro da biblioteca", command=self.obter_isbn_remover_livro)
        botao_remover.pack(pady=10)
            
        botao_emprestimo = tk.Button(tela_menu_funcionario, text="Registrar um empréstimo de um livro", command=self.registrar_emprestimo)
        botao_emprestimo.pack(pady=10)

        botao_devolucao = tk.Button(tela_menu_funcionario, text="Registrar a devolução de um livro", command=self.registrar_devolucao)
        botao_devolucao.pack(pady=10)

        botao_listar_emprestados = tk.Button(tela_menu_funcionario, text="Listar todos os livros emprestados", command=self.listar_livros_emprestados)
        botao_listar_emprestados.pack(pady=10)

        botao_listar_cadastrados = tk.Button(tela_menu_funcionario, text="Listar todos os livros cadastrados", command=self.listar_livros_cadastrados)
        botao_listar_cadastrados.pack(pady=10)

        botao_fechar = tk.Button(tela_menu_funcionario, text="Fechar", command=tela_menu_funcionario.destroy)
        botao_fechar.pack(pady=10)

    def adicionar_livro_comum(self):
            titulo = simpledialog.askstring("Adicionar livro comum", "Digite o título do livro:")
            autor = simpledialog.askstring("Adicionar livro comum", "Digite o autor do livro:")
            isbn = simpledialog.askstring("Adicionar livro comum", "Digite o ISBN do livro:")
            ano_publicacao = simpledialog.askstring("Adicionar livro comum", "Digite o Ano de publicação do livro:")
            categoria = simpledialog.askstring("Adicionar livro comum", "Digite a categoria do livro:")
            numero_de_copias = simpledialog.askinteger("Adicionar livro comum", "Digite o número de cópias do livro:")

            livro = LivroComum(titulo, autor, isbn, ano_publicacao, categoria, numero_de_copias)

            # Add the livro to your library
            self.livros_comuns.append(livro)

            print("Livro comum adicionado com sucesso!")


    def adicionar_livro_raro(self):
            titulo = simpledialog.askstring("Adicionar livro raro", "Digite o título do livro:")
            autor = simpledialog.askstring("Adicionar livro raro", "Digite o autor do livro:")
            isbn = simpledialog.askstring("Adicionar livro raro", "Digite o ISBN do livro:")
            ano_publicacao = simpledialog.askstring("Adicionar livro raro", "Digite o Ano da publicação do livro:")
            categoria = simpledialog.askstring("Adicionar livro raro", "Digite a categoria do livro:")
            edicao = simpledialog.askstring("Adicionar livro raro", "Digite a edição do livro:")
            estado = simpledialog.askstring("Adicionar livro raro", "Digite o estado do livro:")
            numero_de_copias = simpledialog.askstring("Adicionar livro raro", "Digite o número de cópias do livro:")

            livro = {
                "titulo": titulo,
                "autor": autor,
                "isbn": isbn,
                "ano_publicacao": ano_publicacao,
                "categoria": categoria,
                "edicao": edicao,
                "estado": estado,
                "numero_de_copias": numero_de_copias
            }

            self.livros_raros.append(livro)

            print("Livro raro adicionado:")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("ISBN:", livro["isbn"])
            print("Ano de Publicação:", livro["ano_publicacao"])
            print("Categoria:", livro["categoria"])
            print("Edição:", livro["edicao"])
            print("Estado:", livro["estado"])
            print("Número de Cópias:", livro["numero_de_copias"])



    def remover_livro(self, isbn):
            livro_removido = False

            for livro in self.livros_comuns:
                if livro.isbn == isbn:
                    print("Livro comum encontrado:")
                    print("Título:", livro.titulo)
                    print("Autor:", livro.autor)
                    print("ISBN:", livro.isbn)
                    print("Ano de Publicação:", livro.ano_publicacao)
                    self.livros_comuns.remove(livro)
                    print("Livro comum removido com sucesso!")
                    livro_removido = True
                    break

            if not livro_removido:
                for livro in self.livros_raros:
                    if livro["isbn"] == isbn:
                        print("Livro raro encontrado:")
                        print("Título:", livro["titulo"])
                        print("Autor:", livro["autor"])
                        print("ISBN:", livro["isbn"])
                        print("Ano de Publicação:", livro["ano_publicacao"])
                        self.livros_raros.remove(livro)
                        print("Livro raro removido com sucesso!")
                        livro_removido = True
                        break

            if not livro_removido:
                print("Livro não encontrado.")

    def obter_isbn_remover_livro(self):
            isbn = simpledialog.askstring("Remover livro", "Digite o ISBN do livro que deseja remover:")
            self.remover_livro(isbn)


    def registrar_emprestimo(self):
            isbn = simpledialog.askstring("Registrar empréstimo", "Digite o ISBN do livro que deseja emprestar:")
            nome_usuario = simpledialog.askstring("Registrar empréstimo", "Digite o nome do usuário que está emprestando o livro:")
            email_usuario = simpledialog.askstring("Registrar empréstimo", "Digite o email do usuário:")

            livro_encontrado = False

            for livro in self.livros_comuns + self.livros_raros:
                if isinstance(livro, LivroComum) and livro.isbn == isbn:
                    if not livro.emprestado:
                        livro.emprestado = True
                        livro.nome_usuario = nome_usuario
                        livro.email_usuario = email_usuario
                        print("Empréstimo registrado com sucesso!")
                    else:
                        print("O livro já está emprestado.")
                    livro_encontrado = True
                    break
                elif isinstance(livro, LivroRaro) and livro.isbn == isbn:
                    if not livro.emprestado:
                        livro.emprestado = True
                        livro.nome_usuario = nome_usuario
                        livro.email_usuario = email_usuario
                        print("Empréstimo registrado com sucesso!")
                    else:
                        print("O livro já está emprestado.")
                    livro_encontrado = True
                    break

            if not livro_encontrado:
                print("Livro não encontrado.")

    def registrar_devolucao(self):
            isbn = simpledialog.askstring("Registrar devolução", "Digite o ISBN do livro que está sendo devolvido:")
            nome_usuario = simpledialog.askstring("Registrar devolução", "Digite o nome do usuário que está devolvendo o livro:")
            email_usuario = simpledialog.askstring("Registrar devolução", "Digite o e-mail do usuário que está devolvendo o livro:")

            livro_encontrado = False

            for livro in self.livros_comuns:
                if livro.isbn == isbn:
                    if livro.emprestado:
                        if livro.nome_usuario == nome_usuario and livro.email_usuario == email_usuario:
                            livro.emprestado = False
                            livro.nome_usuario = ""
                            livro.email_usuario = ""
                            print("Devolução registrada com sucesso para o livro comum!")
                        else:
                            print("As informações do usuário não correspondem ao empréstimo registrado.")
                    else:
                        print("O livro comum não está emprestado.")
                    livro_encontrado = True
                    break

            if not livro_encontrado:
                for livro in self.livros_raros:
                    if livro.isbn == isbn:
                        if livro.emprestado:
                            if livro.nome_usuario == nome_usuario and livro.email_usuario == email_usuario:
                                livro.emprestado = False
                                livro.nome_usuario = ""
                                livro.email_usuario = ""
                                print("Devolução registrada com sucesso para o livro raro!")
                            else:
                                print("As informações do usuário não correspondem ao empréstimo registrado.")
                        else:
                            print("O livro raro não está emprestado.")
                        livro_encontrado = True
                        break

            if not livro_encontrado:
                print("Livro não encontrado.")


    def listar_livros_emprestados(self):
            borrowed_books = []

            for livro in self.livros_comuns:
                if livro.emprestado:
                    borrowed_books.append(f"Livro comum: {livro.titulo} (ISBN: {livro.isbn})")

            for livro in self.livros_raros:
                if livro['emprestado']:
                    borrowed_books.append(f"Livro raro: {livro['titulo']} (ISBN: {livro['isbn']})")

            if borrowed_books:
                messagebox.showinfo("Livros Emprestados", "\n".join(borrowed_books))
            else:
                messagebox.showinfo("Livros Emprestados", "Nenhum livro está emprestado.")

            print("Livros emprestados:")
            for book in borrowed_books:
                print(book)


    def listar_livros_cadastrados(self):
            book_list = []

            for livro in self.livros_comuns:
                book_info = f"Título: {livro.titulo}\n"
                book_info += f"Autor: {livro.autor}\n"
                book_info += f"ISBN: {livro.isbn}\n"
                book_info += f"Ano de Publicação: {livro.ano_publicacao}\n"
                book_info += f"Número de Cópias: {livro.numero_de_copias}\n"
                book_info += "---"
                book_list.append(book_info)

            for livro in self.livros_raros:
                book_info = f"Título: {livro['titulo']}\n"
                book_info += f"Autor: {livro['autor']}\n"
                book_info += f"ISBN: {livro['isbn']}\n"
                book_info += f"Ano de Publicação: {livro['ano_publicacao']}\n"
                book_info += f"Categoria: {livro['categoria']}\n"
                book_info += f"Edição: {livro['edicao']}\n"
                book_info += f"Estado: {livro['estado']}\n"
                book_info += f"Número de Cópias: {livro['numero_de_copias']}\n"
                book_info += "---"
                book_list.append(book_info)

            if book_list:
                messagebox.showinfo("Livros Cadastrados", "\n".join(book_list))
            else:
                messagebox.showinfo("Livros Cadastrados", "Nenhum livro foi cadastrado.")

            print("Livros cadastrados:")
            for book in book_list:
                print(book)

                
    def menu_funcionario(self):
            self.abrir_tela_menu_funcionario()

    def run(self):
            self.janela.mainloop()


    # Desabilitar a edição do widget de texto
            texto_listagem.configure(state="disabled")

    def adicionar_livro_comum_backend(self, titulo, autor, isbn, ano_publicacao, categoria, numero_de_copias):
            print("Adicionar um livro comum à biblioteca...")
            # Substitua esta parte do código com a lógica do seu programa para adicionar um livro comum

    def adicionar_livro_raro_backend(self, titulo, autor, isbn, ano_publicacao, categoria, edicao, estado, numero_de_copias):
            print("Adicionar um livro raro à biblioteca...")
            # Substitua esta parte do código com a lógica do seu programa para adicionar um livro raro

    def remover_livro_backend(self, isbn):
            print("Remover um livro da biblioteca...")
            # Substitua esta parte do código com a lógica do seu programa para remover um livro

    def registrar_emprestimo_backend(self, isbn, nome_usuario, email_usuario):
            print("Registrar um empréstimo de um livro...")
            # Substitua esta parte do código com a lógica do seu programa para registrar um empréstimo

    def registrar_devolucao_backend(self, isbn, nome_usuario, email_usuario):
            print("Registrar a devolução de um livro...")
            # Substitua esta parte do código com a lógica do seu programa para registrar uma devolução

    def listar_livros_emprestados_backend(self):
            print("Listar todos os livros emprestados...")
            # Substitua esta parte do código com a lógica do seu programa para listar os livros emprestados


##########################################################################################################
##########################fim menu funcionario###################################################



###################################################################################################
#_________________________________abrir tela funcionario----------------------------------------

    def abrir_tela_funcionario(self):
        # Código para abrir a tela de funcionário
        tela_funcionario = tk.Toplevel(self.janela)
        tela_funcionario.title("Tela do Funcionário")
        tela_funcionario.geometry("300x300")

        # Centralizar os botões na tela do funcionário
        tela_funcionario.pack_propagate(0)
        tela_funcionario.grid_rowconfigure(0, weight=1)
        tela_funcionario.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do funcionário
        botao_cadastro = tk.Button(tela_funcionario, text="Cadastro", command=self.abrir_tela_cadastro)
        botao_cadastro.pack(pady=10)

        botao_login = tk.Button(tela_funcionario, text="Login", command=self.abrir_tela_login)
        botao_login.pack(pady=10)





#####################################################################################################
#-------------------------------------------abrir tela cadastro--------------------------------------------


    def abrir_tela_cadastro(self):
        # Código para abrir a tela de cadastro
        tela_cadastro = tk.Toplevel(self.janela)
        tela_cadastro.title("Cadastro de Funcionário")
        tela_cadastro.geometry("300x200")

        # Centralizar os campos de email e senha
        tela_cadastro.pack_propagate(0)
        tela_cadastro.grid_rowconfigure(0, weight=1)
        tela_cadastro.grid_columnconfigure(0, weight=1)

        # Campos de email e senha
        label_email = tk.Label(tela_cadastro, text="Email:")
        label_email.pack(pady=5)
        entry_email = tk.Entry(tela_cadastro)
        entry_email.pack(pady=5)

        label_senha = tk.Label(tela_cadastro, text="Senha:")
        label_senha.pack(pady=5)
        entry_senha = tk.Entry(tela_cadastro, show="*")
        entry_senha.pack(pady=5)

        botao_confirmar = tk.Button(tela_cadastro, text="Confirmar", command=lambda: self.cadastrar_funcionario(entry_email.get(), entry_senha.get()))
        botao_confirmar.pack(pady=10)



#####################################################################################################
#------------------------------------------- tela login  --------------------------------------------



    def abrir_tela_login(self):
        # Código para abrir a tela de login
        tela_login = tk.Toplevel(self.janela)
        tela_login.title("Login de Funcionário")
        tela_login.geometry("300x200")

        # Centralizar os campos de email e senha
        tela_login.pack_propagate(0)
        tela_login.grid_rowconfigure(0, weight=1)
        tela_login.grid_columnconfigure(0, weight=1)

        # Campos de email e senha
        label_email = tk.Label(tela_login, text="Email:")
        label_email.pack(pady=5)
        entry_email = tk.Entry(tela_login)
        entry_email.pack(pady=5)

        label_senha = tk.Label(tela_login, text="Senha:")
        label_senha.pack(pady=5)
        entry_senha = tk.Entry(tela_login, show="*")
        entry_senha.pack(pady=5)

        botao_confirmar = tk.Button(tela_login, text="Login", command=lambda: self.validar_login(entry_email.get(), entry_senha.get()))
        botao_confirmar.pack(pady=10)


#############################################################################################################
#---------------------------------------------tela cliente--------------------------------------------


    def abrir_tela_cliente(self):
        # Código para abrir a tela de cliente
        tela_cliente = tk.Toplevel(self.janela)
        tela_cliente.title("Tela do Cliente")
        tela_cliente.geometry("300x200")

        # Centralizar os botões na tela do cliente
        tela_cliente.pack_propagate(0)
        tela_cliente.grid_rowconfigure(0, weight=1)
        tela_cliente.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do cliente
        botao_cadastro_cliente = tk.Button(tela_cliente, text="Cadastro", command=self.abrir_tela_cadastro_cliente)
        botao_cadastro_cliente.pack(pady=10)

        botao_login_cliente = tk.Button(tela_cliente, text="Login", command=self.abrir_tela_login_cliente)
        botao_login_cliente.pack(pady=10)


#############################################################################################
#------------------------------------------



    def abrir_tela_cadastro_cliente(self):
        # Código para abrir a tela de cadastro do cliente
        tela_cadastro_cliente = tk.Toplevel(self.janela)
        tela_cadastro_cliente.title("Cadastro de Cliente")
        tela_cadastro_cliente.geometry("300x200")

        # Centralizar os campos de email e senha do cliente
        tela_cadastro_cliente.pack_propagate(0)
        tela_cadastro_cliente.grid_rowconfigure(0, weight=1)
        tela_cadastro_cliente.grid_columnconfigure(0, weight=1)

        # Campos de email e senha do cliente
        label_email_cliente = tk.Label(tela_cadastro_cliente, text="Email:")
        label_email_cliente.pack(pady=5)
        entry_email_cliente = tk.Entry(tela_cadastro_cliente)
        entry_email_cliente.pack(pady=5)

        label_senha_cliente = tk.Label(tela_cadastro_cliente, text="Senha:")
        label_senha_cliente.pack(pady=5)
        entry_senha_cliente = tk.Entry(tela_cadastro_cliente, show="*")
        entry_senha_cliente.pack(pady=5)

        botao_confirmar_cliente = tk.Button(tela_cadastro_cliente, text="Confirmar", command=lambda: self.cadastrar_cliente(entry_email_cliente.get(), entry_senha_cliente.get()))
        botao_confirmar_cliente.pack(pady=10)



##############################################################################################
#------------------------------------------------------------------------------------------------------




    def abrir_tela_login_cliente(self):
        # Código para abrir a tela de login do cliente
        tela_login_cliente = tk.Toplevel(self.janela)
        tela_login_cliente.title("Login de Cliente")
        tela_login_cliente.geometry("300x200")

        # Centralizar os campos de email e senha do cliente
        tela_login_cliente.pack_propagate(0)
        tela_login_cliente.grid_rowconfigure(0, weight=1)
        tela_login_cliente.grid_columnconfigure(0, weight=1)

        # Campos de email e senha do cliente
        label_email_cliente = tk.Label(tela_login_cliente, text="Email:")
        label_email_cliente.pack(pady=5)
        entry_email_cliente = tk.Entry(tela_login_cliente)
        entry_email_cliente.pack(pady=5)

        label_senha_cliente = tk.Label(tela_login_cliente, text="Senha:")
        label_senha_cliente.pack(pady=5)
        entry_senha_cliente = tk.Entry(tela_login_cliente, show="*")
        entry_senha_cliente.pack(pady=5)

        botao_confirmar_cliente = tk.Button(tela_login_cliente, text="Login", command=lambda: self.validar_login_cliente(entry_email_cliente.get(), entry_senha_cliente.get()))
        botao_confirmar_cliente.pack(pady=10)




##########################################################################################################
#--------------------------------------------

    def cadastrar_funcionario(self, email, senha):
        # Verifica se o e-mail termina com "@funcionario"
        if email.endswith("@funcionario"):
            # Adiciona as informações do funcionário à lista de funcionários cadastrados
            self.funcionarios_cadastrados.append((email, senha))
            print("Cadastro de funcionário realizado com sucesso!")
            print("Email:", email)
            print("Senha:", senha)
        else:
            print("E-mail inválido! O e-mail deve terminar com '@funcionario'")



#########################################################################################
#-------------------------------------------




    def validar_login(self, email, senha):
        # Verifica se as informações de login correspondem a um funcionário cadastrado
        for funcionario in self.funcionarios_cadastrados:
            if email == funcionario[0] and senha == funcionario[1]:
                print("Login de funcionário realizado com sucesso!")
                print("Email:", email)
                print("Senha:", senha)
                self.abrir_tela_menu_funcionario()  # Abre a tela do menu do funcionário
                return
                
        print("Login inválido! Verifique suas informações.")


################################################################################
#-----------------------------------------



    def cadastrar_cliente(self, email, senha):
        # Verifica se o e-mail termina com "@cliente"
        if email.endswith("@cliente"):
            # Adiciona as informações do cliente à lista de clientes cadastrados
            self.clientes_cadastrados.append((email, senha))
            print("Cadastro de cliente realizado com sucesso!")
            print("Email:", email)
            print("Senha:", senha)
        else:
            print("E-mail inválido! O e-mail deve terminar com '@cliente'")


################################################################################
#-----------------------------------------




    def validar_login_cliente(self, email, senha):
        # Verifica se as informações de login correspondem a um cliente cadastrado
        for cliente in self.clientes_cadastrados:
            if email == cliente[0] and senha == cliente[1]:
                print("Login de cliente realizado com sucesso!")
                print("Email:", email)
                print("Senha:", senha)
                self.abrir_tela_menu_cliente()  # Abre a tela do menu do cliente
                return
                return
        print("Login inválido! Verifique suas informações.")


##########################################################################
#---------------------------------------------------------------


    def abrir_tela_menu_cliente(self):
        # Código para abrir a tela do menu do cliente
        tela_menu_cliente = tk.Toplevel(self.janela)
        tela_menu_cliente.title("Menu do Cliente")
        tela_menu_cliente.geometry("300x300")

        # Centralizar os botões na tela do menu do cliente
        tela_menu_cliente.pack_propagate(0)
        tela_menu_cliente.grid_rowconfigure(0, weight=1)
        tela_menu_cliente.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do menu do cliente
        botao_buscar = tk.Button(tela_menu_cliente, text="Buscar um livro na biblioteca", command=self.buscar_livro)
        botao_buscar.pack(pady=10)

        botao_listar = tk.Button(tela_menu_cliente, text="Listar todos os livros da biblioteca", command=self.listar_livros_cadastrados)
        botao_listar.pack(pady=10)

        

        botao_sair = tk.Button(tela_menu_cliente, text="Sair do programa", command=self.janela.quit)
        botao_sair.pack(pady=10)

    def buscar_livro(self):
        # Código para buscar um livro na biblioteca
        tela_buscar_livro = tk.Toplevel(self.janela)
        tela_buscar_livro.title("Buscar Livro")
        tela_buscar_livro.geometry("300x200")

        # Centralizar os campos de busca
        tela_buscar_livro.pack_propagate(0)
        tela_buscar_livro.grid_rowconfigure(0, weight=1)
        tela_buscar_livro.grid_columnconfigure(0, weight=1)

        # Campo de busca
        label_busca = tk.Label(tela_buscar_livro, text="Digite o título do livro:")
        label_busca.pack(pady=5)
        entry_busca = tk.Entry(tela_buscar_livro)
        entry_busca.pack(pady=5)

        # Botão de busca
        botao_buscar = tk.Button(tela_buscar_livro, text="Buscar", command=lambda: self.exibir_livro(entry_busca.get()))
        botao_buscar.pack(pady=10)

    def exibir_livro(self, titulo):
        # Procurar o livro na biblioteca pelo título
        livro_encontrado = None

        # Procurar nos livros comuns
        for livro in self.livros_comuns:
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
                break

        # Se o livro comum não for encontrado, procurar nos livros raros
        if not livro_encontrado:
            for livro in self.livros_raros:
                if livro.titulo.lower() == titulo.lower():
                    livro_encontrado = livro
                    break

        # Criar uma nova janela para exibir as informações do livro
        tela_exibir_livro = tk.Toplevel(self.janela)
        tela_exibir_livro.title("Livro Encontrado")
        tela_exibir_livro.geometry("400x300")

        # Centralizar os campos de exibição
        tela_exibir_livro.pack_propagate(0)
        tela_exibir_livro.grid_rowconfigure(0, weight=1)
        tela_exibir_livro.grid_columnconfigure(0, weight=1)

        # Exibir as informações do livro na nova janela
        if livro_encontrado:
            # Exibir as informações do livro
            texto_livro = f"Título: {livro_encontrado.titulo}\n"
            texto_livro += f"Autor: {livro_encontrado.autor}\n"
            if isinstance(livro_encontrado, LivroRaro):  # Verifica se o livro é do tipo LivroRaro
                texto_livro += f"Edição: {livro_encontrado.edicao}\n"
                texto_livro += f"Estado: {livro_encontrado.estado}\n"
            texto_livro += f"ISBN: {livro_encontrado.isbn}\n"
            texto_livro += f"Ano de Publicação: {livro_encontrado.ano_publicacao}\n"
            texto_livro += f"Categoria: {livro_encontrado.categoria}\n"
            texto_livro += f"Número de Cópias: {livro_encontrado.numero_de_copias}\n"
        else:
            # Se o livro não for encontrado, exiba uma mensagem de erro
            texto_livro = "Livro não encontrado."

        # Criação de um widget de rótulo para exibir as informações do livro
        label_livro = tk.Label(tela_exibir_livro, text=texto_livro)
        label_livro.pack(pady=10)







        

    def listar_livros_cadastrados(self):
            book_list = []

            for livro in self.livros_comuns:
                book_info = f"Título: {livro.titulo}\n"
                book_info += f"Autor: {livro.autor}\n"
                book_info += f"ISBN: {livro.isbn}\n"
                book_info += f"Ano de Publicação: {livro.ano_publicacao}\n"
                book_info += f"Número de Cópias: {livro.numero_de_copias}\n"
                book_info += "---"
                book_list.append(book_info)

            for livro in self.livros_raros:
                book_info = f"Título: {livro['titulo']}\n"
                book_info += f"Autor: {livro['autor']}\n"
                book_info += f"ISBN: {livro['isbn']}\n"
                book_info += f"Ano de Publicação: {livro['ano_publicacao']}\n"
                book_info += f"Categoria: {livro['categoria']}\n"
                book_info += f"Edição: {livro['edicao']}\n"
                book_info += f"Estado: {livro['estado']}\n"
                book_info += f"Número de Cópias: {livro['numero_de_copias']}\n"
                book_info += "---"
                book_list.append(book_info)

            if book_list:
                messagebox.showinfo("Livros Cadastrados", "\n".join(book_list))
            else:
                messagebox.showinfo("Livros Cadastrados", "Nenhum livro foi cadastrado.")

            print("Livros cadastrados:")
            for book in book_list:
                print(book)


    def executar(self):
        self.janela.mainloop()

########################################################################
#-------------------------------------------------------------------------------------


# Criar a janela principal
janela_principal = tk.Tk()

# Definir o tamanho da janela
janela_principal.geometry("300x300")


# Centralizar os botões na janela
janela_principal.pack_propagate(0)
janela_principal.grid_rowconfigure(0, weight=1)
janela_principal.grid_columnconfigure(0, weight=1)

# Criar a instância da interface gráfica
interface = InterfaceGrafica(janela_principal)

# Iniciar o loop principal da aplicação
janela_principal.mainloop()




# Criação da janela principal
janela = tk.Tk()

# Criação da instância da classe InterfaceGrafica
minha_instancia = InterfaceGrafica(janela)

# Início do loop principal da interface gráfica
janela.mainloop()
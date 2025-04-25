# Importa bibliotecas
import streamlit as st  # Streamlit para interface web
from fpdf import FPDF  # FPDF para geração do PDF
import os  # Biblioteca para manipulação de arquivos
from PIL import Image   # Biblioteca para manipulação de imagens

# Configuração da página Streamlit
st.set_page_config(page_title="Relatório de Inspeção", layout="centered")  # Título e layout da página
st.title("📄 Relatório de Inspeção de Pás")  # Título principal

# Classe PDF personalizada
class PDF(FPDF):
    def header(self):
        # Verifica se o arquivo da logo existe e insere a imagem no canto superior esquerdo (x=10, y=10, largura=30mm)
        if os.path.exists("logo_iqony.png"):
            self.image("logo_iqony.png", x=15, y=15, w=25)  # Adiciona a logo da empresa

        # Define a posição e fonte do título central do relatório
        self.set_xy(10, 10)                       # Define a posição (x=40, y=10) para o título
        self.set_font("Arial", "B", 16)           # Define a fonte Arial, negrito, tamanho 12
        self.cell(190, 40, "Relatório de Inspeção de Pás", border=1, ln=1, align="C")  # Linha 1 do título centralizada
        self.ln(5)                            # Adiciona uma quebra de linha após o título


        self.ln(5)
# ------------------------- Rodapé do PDF Com imagem-------------------------------------
    def footer(self):
        # Adiciona imagem no canto inferior esquerdo
        if os.path.exists("wind_turbine_draw.png"):
            self.image("wind_turbine_draw.png", x=10, y=260, w=40)  # Ajuste 'x', 'y' e 'w' conforme o necessário

        # Texto do rodapé
        self.set_y(-10)
        self.set_font("Arial", "I", 7)
        self.multi_cell(
            0, 4,      # Texto do rodapé, 0 largura, 6 altura
            "Este documento é de propriedade da Iqony Solutions do Brasil LTDA. Nenhuma parte deste documento pode\n"
            "ser distribuída sem sua permissão prévia por escrito.",
            border=0, align="C"
            
        )
        # Número da página centralizado
        # Número da página no formato "Página X de Y"
        self.set_y(-10)  # Ajusta posição
        self.cell(0, 10, f"Página {self.page_no()} de {{nb}}", align="R") # adiciona um rodapé ao documento, mostrando o número da página atual e o total de páginas, como por exemplo: "Página 3 de 10"

# ------------------------------------------- Aera Deparatamento REspon
    def primeira_pagina(self, ambito_aplicacao, codigo_relatorio, revisado_por_1, revisado_por_2, data_revisao):
        self.set_font("Arial", "B", 12)
        self.multi_cell(0, 50, f"Departamento Responsável: O&M.\nÂmbito da aplicação: {ambito_aplicacao}", border=1)
        self.ln(10)
        self.cell(95, 10, f"Número: {codigo_relatorio}", 1)
        self.set_font("Arial", "", 10)
        self.cell(95, 10, "(Revisão) 02", 1, ln=True)

        self.set_font("Arial", "B", 10)
        self.cell(45, 10, "", 1)
        self.cell(80, 10, "(Assinatura):", 1)
        self.cell(65, 10, "Data:", 1, ln=True)

        self.set_font("Arial", "B", 10)
        linhas = [
            ["Elaborado por:", "Ruan Lopes da Silva", "12/04/2025"],
            ["Revisado por:", revisado_por_1, data_revisao],
            ["Revisado por:", revisado_por_2, data_revisao],
            ["Aprovado por:", "", ""]
        ]
        for linha in linhas:
            self.cell(45, 10, linha[0], 1)
            self.cell(80, 10, linha[1], 1)
            self.cell(65, 10, linha[2], 1, ln=True)

# --------------------------------- Sumário ---------------------------------------------------
    def pagina_sumario(self): #
        self.add_page()
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Sumário", ln=True, align="C")
        self.ln(5)

        self.set_font("Arial", "B", 12)
        topicos = [
            "1. Introdução",
            "2. Objetivo",
            "3. Dados Gerais do Aerogerador",
            "4. Dados Gerais das Pás",
            "5. Nomenclaturas",
            "6. Itens das pás a serem inspecionados",
            "7. Referência da Avaliação de defeitos",
            "8. Identificação da Máquina",
            "9. Especificação e identificação das pás",
            "10. Inspeção Externa",
            "  10.1. Classificação de defeitos evidenciados na área externa da pá 1",
            "  10.2. Classificação de defeitos evidenciados na área externa da pá 2",
            "  10.3. Classificação de defeitos evidenciados na área externa da pá 3",
            "11. Inspeção interna",
            "  11.1. Classificação de defeitos evidenciados na área interna da pá 1",
            "  11.2. Classificação de defeitos evidenciados na área interna da pá 2",
            "  11.3. Classificação de defeitos evidenciados na área interna da pá 3",
        ]
        for item in topicos:
            self.cell(0, 8, item, ln=True)

    def pagina_dados(self, dados_gerais, dados_pas):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "1. Introdução", ln=True)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8,
            "A atividade contratada consiste na inspeção das pás, realizada nas cascas externas, bordas de ataque e de fuga, "
            "e em toda a extensão das pás. A análise e classificação dos defeitos, bem como a avaliação dos reparos, foram "
            "realizadas pela equipe de serviços de O&M da IQONY.")
        self.ln(5)

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "2. Objetivo", ln=True)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8,
            "Este relatório tem como objetivo apresentar os dados de uma inspeção de pás, realizada no aerogerador WEG modelo "
            "AGW 110 2.1MW, localizado nos parques eólicos Cutia e Bento Miguel. As evidências têm por finalidade documentar o "
            "estado operacional das pás.")
        self.ln(5)

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "3. Dados Gerais do Aerogerador", ln=True)
        self.set_font("Arial", "", 11)
        for rotulo, valor in dados_gerais.items(): # 
            self.cell(60, 10, rotulo, border=1)
            self.cell(130, 10, valor, border=1, ln=True)

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "4. Dados Gerais das Pás", ln=True)
        self.set_font("Arial", "", 11)
        for rotulo, valor in dados_pas.items():
            self.cell(60, 10, rotulo, border=1)
            self.cell(130, 10, valor, border=1, ln=True)

        self.ln(5)

# ------------------------ 5. Nomenclaturas -------------------------------------
    def pagina_nomenclaturas(self): 
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "5. Nomenclaturas", ln=True)
        if os.path.exists("nomenclaturas.png"):
            self.image("nomenclaturas.png", x=10, w=190)
        else:
            self.set_font("Arial", "I", 11)
            self.multi_cell(0, 10, "Imagem de nomenclaturas não encontrada.")



  # -------------- 6. Itens das Pás a Serem Inspecionados -----------------------------

    def pagina_itens_referencia_identificacao(self, imagem_maquina_path=None):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "6. Itens das Pás a Serem Inspecionados", ln=True)

        
        itens = [
            ("Extradorso", "E.D."),
            ("Intradorso", "I.D"),
            ("Bordo de Ataque", "B.A."),
            ("Bordo de Fuga", "B.F."),
            ("Tip", "T.P."),
            ("Raiz", "R.A."),
            ("Almas (B.A e B.F)", "A.B.A, A.B.F"),
            ("Áreas de Colagens (B.A e B.F)", "B.A.C, B.F.C"),
            ("SPDA", "SPDA")
        ]

        for nome, sigla in itens:   # Cria uma célula para cada item
            self.set_fill_color(220, 230, 241) # Cor de fundo azul claro
            self.set_font("Arial", "B", 12) # Define a fonte para o título
            self.cell(80, 10, nome, border=1, fill=True, align="C") # Cria célula com borda e fundo azul claro
            self.set_font("Arial", "", 11) # Define a fonte para o conteúdo
            self.cell(110, 10, sigla, border=1, ln=True) # Cria célula com borda e quebra de linha (ln=True)

   # ----------------- 7. Referência da Avaliação de Defeitos -----------------------------------------
        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "7. Referência da Avaliação de Defeitos", ln=True)

        referencias = [
            ("1", (144, 238, 144), "Danos leves", "Operação normal"),
            ("2", (255, 255, 0), "Danos médios", "Reparo planejado"),
            ("3", (255, 0, 0), "Danos Graves", "Reparo imediato"),
            ("4", (0, 0, 0), "Danos Críticos", "Parar o aerogerador")
        ]

    
        for ref, cor, desc, acao in referencias:
            self.set_font("Arial", "", 11)
            self.cell(20, 10, ref, border=1, align="C")
            self.set_fill_color(*cor)
            self.cell(20, 10, "", border=1, fill=True, align="C")
            self.cell(70, 10, desc, border=1, align="C")
            self.cell(80, 10, acao, border=1, ln=True, align="C")



 #-------------- 8. Identificação da Máquina ----------------------------------------------------------

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "8. Identificação da Máquina", ln=True)

        if imagem_maquina_path and os.path.exists(imagem_maquina_path):
            w = 190                 # Largura da imagem
            h = w * 0.2             # Altura proporcional
            x = (self.w - w) / 2    # Centraliza horizontalmente
            y = self.get_y()        # Usa posição vertical atual após o título

            self.rect(x, y, w, h)   # Borda ao redor da imagem
            self.image(imagem_maquina_path, x=x + 2, y=y + 2, w=w - 4, h=h - 4)  # Imagem com margens internas
            self.ln(h + 10)         # Espaço abaixo da imagem
        else:
            self.set_font("Arial", "I", 11)
            self.multi_cell(0, 10, "Imagem de identificação da máquina não enviada.")


# ------------------------ 9. Especificação e Identificação das Pás ---------------------
    def pagina_identificacao_pas(self, imagens_pás):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "9. Especificação e Identificação das Pás", ln=True)
        self.ln(1)

        for nome_pa, lista_imgs in imagens_pás.items():
            self.set_font("Arial", "B", 11)
            self.cell(0, 10, nome_pa, ln=True)
            self.ln(2)

            x_inicial = self.get_x()
            y_inicial = self.get_y()
            altura_foto = 60
            largura_foto = 85
            espacamento_x = 10

            for i, img in enumerate(lista_imgs):
                if os.path.exists(img):
                    x = x_inicial + i * (largura_foto + espacamento_x)
                    y = self.get_y()

                    # Desenha o retângulo (quadro) para a foto
                    self.rect(x, y, largura_foto, altura_foto)

                    # Insere a imagem dentro do quadro
                    self.image(img, x=x + 2, y=y + 2, w=largura_foto - 4, h=altura_foto - 4)

            self.ln(altura_foto + 1)  # espaço abaixo das fotos antes da próxima PÁ



      
    #----------------------- 10. Expeção externa e 10.1 Classificação de Defeitos Pa1, Pa2 e Pa3 -------------------

    
    def pagina_inspecao_externa(self, numero_pa, tabela): 
        self.add_page()

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "10. Inspeção Externa", ln=True)
        self.ln(2)

        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"10.{numero_pa}. Classificação de defeitos evidenciados na área externa da pá {numero_pa}", ln=True)
        self.ln(2)

        self.set_font("Arial", "B", 10)
        self.cell(50, 10, "Localização", border=1)
        self.cell(70, 10, "Descrição dos danos/ evidências", border=1)
        self.cell(30, 10, "Área", border=1)
        self.cell(40, 10, "Cod. / Cor", border=1, ln=True)

        self.set_font("Arial", "", 10)
        for linha in tabela:
            self.cell(50, 10, linha["Localizacao"], border=1)
            self.cell(70, 10, linha["Descricao"], border=1)
            self.cell(30, 10, linha["Area"], border=1)
            self.cell(40, 10, linha["CodCor"], border=1, ln=True)
            self.ln(0)  # Adiciona um espaço entre as linhas da tabela


    def pagina_inspecao_fotos(self, numero_pa, imagens_obs): 
        #self.add_page()
        self.set_font("Arial", "B", 12)

        topicos = [
            ("Superfície da pá lado sucção", 2),
            ("Receptores do SPDA lado sucção", 2),
            ("B.A lado da sucção", 2),
            ("Superfície do B.A", 4),
            ("Superfície da pá lado da pressão", 4),
            ("Receptores do SPDA lado da pressão", 2),
            ("Superfície no B.A lado da pressão", 2),
        ]

        for i, (titulo, qtd_max) in enumerate(topicos):
            self.cell(0, 10, f"10.{numero_pa}.{i+1} {titulo}", ln=True)
            self.ln(3)
            imagens, obs = imagens_obs.get(titulo, ([], ""))
            self._inserir_imagens_com_obs(imagens, obs, max_img=qtd_max)


    def pagina_inspecao_externa_pa1(self, tabela_pa1):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "10. Inspeção Externa", ln=True)
        self.ln(3)

        self.set_font("Arial", "B", 11)
        self.cell(0, 10, "10.1. Classificação de defeitos evidenciados na área externa da pá 1", ln=True)
        self.ln(5)

        # Cabeçalhos da tabela
        self.set_font("Arial", "B", 10)
        self.cell(50, 10, "Localização", border=1, align="C")
        self.cell(70, 10, "Descrição dos danos/ evidências", border=1, align="C")
        self.cell(30, 10, "Área", border=1, align="C")
        self.cell(40, 10, "Cod. / Cor", border=1, ln=True, align="C")

        # Linhas da tabela preenchidas a partir do dicionário
        self.set_font("Arial", "", 10)
        for linha in tabela_pa1:
            self.cell(50, 10, linha["Localizacao"], border=1)
            self.cell(70, 10, linha["Descricao"], border=1)
            self.cell(30, 10, linha["Area"], border=1)
            self.cell(40, 10, linha["CodCor"], border=1, ln=True)

    def pagina_inspecao_externa_pa2(self, tabela_pa2):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "10.2. Classificação de defeitos evidenciados na área externa da pá 2", ln=True)
        self.ln(5)

        self.set_font("Arial", "B", 10)
        self.cell(50, 10, "Localização", border=1)
        self.cell(70, 10, "Descrição dos danos/ evidências", border=1)
        self.cell(30, 10, "Área", border=1)
        self.cell(40, 10, "Cod. / Cor", border=1, ln=True)

        self.set_font("Arial", "", 10)
        for linha in tabela_pa2:
            self.cell(50, 10, linha["Localizacao"], border=1)
            self.cell(70, 10, linha["Descricao"], border=1)
            self.cell(30, 10, linha["Area"], border=1)
            self.cell(40, 10, linha["CodCor"], border=1, ln=True)

    def pagina_inspecao_externa_pa3(self, tabela_pa3):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "10.3. Classificação de defeitos evidenciados na área externa da pá 3", ln=True)
        self.ln(5)

        self.set_font("Arial", "B", 10)
        self.cell(50, 10, "Localização", border=1)
        self.cell(70, 10, "Descrição dos danos/ evidências", border=1)
        self.cell(30, 10, "Área", border=1)
        self.cell(40, 10, "Cod. / Cor", border=1, ln=True)

        self.set_font("Arial", "", 10)
        for linha in tabela_pa3:
            self.cell(50, 10, linha["Localizacao"], border=1)
            self.cell(70, 10, linha["Descricao"], border=1)
            self.cell(30, 10, linha["Area"], border=1)
            self.cell(40, 10, linha["CodCor"], border=1, ln=True)



    def _inserir_imagens_com_obs(self, lista_imagens, observacao, max_img=2):
        largura_img = 90 if max_img == 2 else 90
        altura_img = 60
        espacamento = 10

        for i, img in enumerate(lista_imagens[:max_img]):
            if os.path.exists(img):
                x = 10 + i * (largura_img + espacamento)
                y = self.get_y()
                self.rect(x, y, largura_img, altura_img)
                self.image(img, x + 2, y + 2, w=largura_img - 4, h=altura_img - 4)
        self.ln(altura_img + 5)

        self.ln(10)  # Espaço entre as imagens e a observação
        self.set_font("Arial", "I", 11)
        self.multi_cell(0, 8, f"Observações: {observacao or '-'}")
        self.ln(10)

    def pagina_inspecao_completa_pa(self, numero_pa, tabela, imagens_obs):
        self.pagina_inspecao_externa(numero_pa, tabela)
        self.pagina_inspecao_fotos(numero_pa, imagens_obs)

        topicos = [
            ("Superfície da pá lado sucção", 2),
            ("Receptores do SPDA lado sucção", 2),
            ("B.A lado da sucção", 2),
            ("Superfície do B.A", 4),
            ("Superfície da pá lado da pressão", 4),
            ("Receptores do SPDA lado da pressão", 2),
            ("Superfície no B.A lado da pressão", 2),
        ]

        for i, (titulo, max_img) in enumerate(topicos):
            self.cell(0, 10, f"10.{numero_pa}.{i+1} {titulo}", ln=True)
            self.ln(3)
            imagens, obs = imagens_obs.get(titulo, ([], ""))
            self._inserir_imagens_com_obs(imagens, obs, max_img=max_img)

# ------------------------ 11. Inspeção Interna -------------------------------------

    def pagina_inspecao_interna_completa_pa(self, numero_pa, fotos_identificacao, tabela_defeitos, imagens_obs):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"11. Inspeção Interna - Pá {numero_pa}", ln=True)
        self.ln(5)

        # 11.1 Identificação da pá
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, "11.1 Identificação da pá", ln=True)
        self.ln(2)

        largura_img = 90
        altura_img = 60
        espacamento = 10

        for i, img in enumerate(fotos_identificacao[:2]):
            if os.path.exists(img):
                x = 10 + i * (largura_img + espacamento)
                y = self.get_y()
                self.rect(x, y, largura_img, altura_img)
                self.image(img, x + 2, y + 2, w=largura_img - 4, h=altura_img - 4)

        self.ln(altura_img + 5)

        # 11.2 Classificação de defeitos evidenciados
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, f"11.2 Classificação de defeitos evidenciados na área interna da pá {numero_pa}", ln=True)
        self.ln(3)

        self.set_font("Arial", "B", 10)
        self.set_fill_color(220, 230, 241)
        self.cell(50, 10, "Localização", border=1, fill=True, align="C")
        self.cell(70, 10, "Descrição dos danos/ evidências", border=1, fill=True, align="C")
        self.cell(30, 10, "Área", border=1, fill=True, align="C")
        self.cell(40, 10, "Cor", border=1, fill=True, align="C")
        self.ln()

        self.set_font("Arial", "", 10)
        for linha in tabela_defeitos:
            self.cell(50, 10, linha["Localizacao"], border=1)
            self.cell(70, 10, linha["Descricao"], border=1)
            self.cell(30, 10, linha["Area"], border=1)
            self.cell(40, 10, linha["Cor"], border=1)
            self.ln()

        self.ln(5)

        # Subitens com fotos
        topicos = [
            f"11.2.1 B.A Não apresenta falhas de colagem visíveis",
            f"11.2.2 Superfície entre as almas do B.F e Alma do B.A",
            f"11.2.3 Coletores do SPDA",
            f"11.2.4 B.F não apresenta falhas de colagem visíveis"
        ]

        for i, titulo in enumerate(topicos):
            self.set_font("Arial", "B", 11)
            self.cell(0, 10, titulo, ln=True)
            self.ln(3)

            imagens, obs = imagens_obs.get(titulo, ([], ""))
            self._inserir_imagens_com_obs(imagens, obs, max_img=2)



# -----------------------CAMPOS DE ENTRADA PARA O USUÁRIO VIA STREAMLIT-------------------------------

#------------------------ Inputs Primeira pagina --------------------------------
st.subheader("📄 Dados da Capa do Relatório")

ambito_aplicacao = st.text_input("Âmbito da Aplicação:", value="Complexo Eólico Cutia - WTG SM2-09")
codigo_relatorio = st.text_input("Código do Relatório:", value="IQONY-INSP-01")
revisado_por_1 = st.text_input("Revisado por (1ª Revisão):", value="")
revisado_por_2 = st.text_input("Revisado por (2ª Revisão):", value="")
data_revisao = st.text_input("Data da Revisão:", value="12/04/2025")

# ------------------------ Inputs Dados Gerais do Aerogerador ----------------------------

st.subheader("🔧 3. Dados Gerais do Aerogerador")
fabricante_modelo = st.text_input("Fabricante Modelo:")
modelo = st.text_input("Modelo:")
ano_fabricacao = st.text_input("Ano de Fabricação:")
altura_torre = st.text_input("Altura da Torre:")

st.subheader("🔧 4. Dados Gerais das Pás")
fabricante_pas = st.text_input("Fabricante:")
tipo_pa = st.text_input("Tipo de Pá de Rotor:")
num_serie_pas = st.text_input("Número de Série das Pás:")
num_serie_set = st.text_input("Número de Série do Set:")
elementos_fluxo = st.text_input("Elementos de Fluxo de Ar:")
dispositivos_luz = st.text_input("Dispositivos de iluminação:")


#-------------------------------------- Inputs Nomenclaturas -------------------------------------
# 📸 SEÇÃO 8 – IDENTIFICAÇÃO DA MÁQUINA
st.subheader("📸 8. Identificação da Máquina")

with st.container():
    st.markdown("**📷 Envie uma imagem da máquina para o relatório**")
    
    imagem_maquina = st.file_uploader(
        "Selecione a imagem (PNG ou JPG)", 
        type=["jpg", "jpeg", "png"]
    )

    imagem_maquina_path = None
    if imagem_maquina:
        # Detecta a extensão correta a partir do tipo MIME
        extensao = imagem_maquina.type.split("/")[-1]
        imagem_maquina_path = f"imagem_maquina.{extensao}"

        # Salva o arquivo corretamente com a extensão original
        with open(imagem_maquina_path, "wb") as f:
            f.write(imagem_maquina.read())

        # Mostra imagem carregada abaixo
        st.image(imagem_maquina, caption="Imagem carregada", use_column_width=True)

st.subheader("📷 9. Especificação e Identificação das Pás")

imagens_pás = {}

# Loop para as 3 pás
for i in range(1, 4): # Loop de 1 a 3 para as pás
    with st.container(): # Cria um container para cada pá
        st.markdown(f"### 📌 PÁ {i}")   ## Título para cada pá
        fotos = st.file_uploader( # Carrega as fotos da pá
            f"Envie até 2 fotos para a PÁ {i}", # Título do uploader
            type=["jpg", "jpeg", "png"], # Tipo de arquivo aceito
            accept_multiple_files=True, # Aceita múltiplos arquivos
            key=f"foto_pa_{i}" # Chave única para cada pá
        )

        caminhos = [] # Lista para armazenar os caminhos das fotos
        for j, foto in enumerate(fotos[:2]):  # Limita a 2 fotos
            extensao = foto.type.split("/")[-1] # Detecta a extensão correta
            caminho = f"foto_pa_{i}_{j}.{extensao}" # Cria o caminho do arquivo
            with open(caminho, "wb") as f: # Abre o arquivo para escrita
                f.write(foto.read()) # Salva o arquivo
            caminhos.append(caminho) # Adiciona o caminho à lista

        # Exibe as imagens carregadas
        if caminhos: ## Verifica se há imagens carregadas
            st.image(caminhos, width=300, caption=[f"PÁ {i} - Foto {j+1}" for j in range(len(caminhos))]) # Mostra as imagens carregadas, com legenda, witdh=300 (largura 300px)

        imagens_pás[f"PÁ {i}"] = caminhos  # Guarda os caminhos por pá
        




            # - item 10 

       

st.subheader("🔍 10. Inspeção Externa - Classificação de Defeitos (PÁ 1)")

# Lista das localizações da pá
localizacoes = ["R.A Ping Teste", "N/A", "I.D", "E. D", "B. A", "B. F", "TIP", "SPDA"]

# Lista para armazenar os dados preenchidos
tabela_externa_pa1 = []

# Gera campos de entrada para cada linha da tabela
for loc in localizacoes:
    st.markdown(f"**📌 Localização: {loc}**")
    desc = st.text_input(f"Descrição dos danos/evidências - {loc}", key=f"desc_{loc}")
    area = st.text_input(f"Área - {loc}", key=f"area_{loc}")
    cod_cor = st.text_input(f"Cód./Cor - {loc}", key=f"cod_{loc}")
    
    # Armazena os dados para o PDF
    tabela_externa_pa1.append({
        "Localizacao": loc,
        "Descricao": desc,
        "Area": area,
        "CodCor": cod_cor
    })

st.markdown("---")

st.subheader("🔍 10.2. Inspeção Externa - Classificação de Defeitos (PÁ 2)")
tabela_externa_pa2 = []
for loc in localizacoes:
    st.markdown(f"**📌 Localização: {loc} (PÁ 2)**")
    desc = st.text_input(f"Descrição dos danos/evidências - {loc} (PÁ 2)", key=f"desc_pa2_{loc}")
    area = st.text_input(f"Área - {loc} (PÁ 2)", key=f"area_pa2_{loc}")
    cod_cor = st.text_input(f"Cód./Cor - {loc} (PÁ 2)", key=f"cod_pa2_{loc}")
    tabela_externa_pa2.append({
        "Localizacao": loc,
        "Descricao": desc,
        "Area": area,
        "CodCor": cod_cor
    })

st.subheader("🔍 10.3. Inspeção Externa - Classificação de Defeitos (PÁ 3)")
tabela_externa_pa3 = []
for loc in localizacoes:
    st.markdown(f"**📌 Localização: {loc} (PÁ 3)**")
    desc = st.text_input(f"Descrição dos danos/evidências - {loc} (PÁ 3)", key=f"desc_pa3_{loc}")
    area = st.text_input(f"Área - {loc} (PÁ 3)", key=f"area_pa3_{loc}")
    cod_cor = st.text_input(f"Cód./Cor - {loc} (PÁ 3)", key=f"cod_pa3_{loc}")
    tabela_externa_pa3.append({
        "Localizacao": loc,
        "Descricao": desc,
        "Area": area,
        "CodCor": cod_cor
    })

        # 10.1.1

# ----------------------------- PÁ 1 ----------------------------- Fotos e Observações
st.subheader("📸 10.1 Inspeção Externa - PÁ 1")

# 10.1.1
st.subheader("📸 10.1.1 Superfície da pá lado sucção (PÁ 1)")
fotos_pa1_superficie = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_superficie")
obs_pa1_superficie = st.text_area("Observações - Superfície da pá lado sucção (PÁ 1)", key="obs_pa1_superficie")

# 10.1.2
st.subheader("📸 10.1.2 Receptores do SPDA lado sucção (PÁ 1)")
fotos_pa1_spda = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_spda")
obs_pa1_spda = st.text_area("Observações - Receptores SPDA lado sucção (PÁ 1)", key="obs_pa1_spda")

# 10.1.3
st.subheader("📸 10.1.3 B.A lado da sucção (PÁ 1)")
fotos_pa1_ba_succao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_ba_succao")
obs_pa1_ba_succao = st.text_area("Observações - B.A lado da sucção (PÁ 1)", key="obs_pa1_ba_succao")

# 10.1.4
st.subheader("📸 10.1.4 Superfície do B.A (PÁ 1)")
fotos_pa1_ba_surface = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_ba_surface")
obs_pa1_ba_surface = st.text_area("Observações - Superfície do B.A (PÁ 1)", key="obs_pa1_ba_surface")

# 10.1.5
st.subheader("📸 10.1.5 Superfície da pá lado da pressão (PÁ 1)")
fotos_pa1_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_pressao")
obs_pa1_pressao = st.text_area("Observações - Superfície da pá lado da pressão (PÁ 1)", key="obs_pa1_pressao")

# 10.1.6
st.subheader("📸 10.1.6 Receptores do SPDA lado da pressão (PÁ 1)")
fotos_pa1_spda_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_spda_pressao")
obs_pa1_spda_pressao = st.text_area("Observações - Receptores do SPDA lado da pressão (PÁ 1)", key="obs_pa1_spda_pressao")

# 10.1.7
st.subheader("📸 10.1.7 Superfície no B.A lado da pressão (PÁ 1)")
fotos_pa1_ba_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa1_ba_pressao")
obs_pa1_ba_pressao = st.text_area("Observações - Superfície no B.A lado da pressão (PÁ 1)", key="obs_pa1_ba_pressao")


# ----------------------------- PÁ 2 ----------------------------- fotos e Observações
st.subheader("📸 10.2 Inspeção Externa - PÁ 2")

# 10.2.1
st.subheader("📸 10.2.1 Superfície da pá lado sucção (PÁ 2)")
fotos_pa2_superficie = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_superficie")
obs_pa2_superficie = st.text_area("Observações - Superfície da pá lado sucção (PÁ 2)", key="obs_pa2_superficie")

# 10.2.2
st.subheader("📸 10.2.2 Receptores do SPDA lado sucção (PÁ 2)")
fotos_pa2_spda = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_spda")
obs_pa2_spda = st.text_area("Observações - Receptores SPDA lado sucção (PÁ 2)", key="obs_pa2_spda")

# 10.2.3
st.subheader("📸 10.2.3 B.A lado da sucção (PÁ 2)")
fotos_pa2_ba_succao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_ba_succao")
obs_pa2_ba_succao = st.text_area("Observações - B.A lado da sucção (PÁ 2)", key="obs_pa2_ba_succao")

# 10.2.4
st.subheader("📸 10.2.4 Superfície do B.A (PÁ 2)")
fotos_pa2_ba_surface = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_ba_surface")
obs_pa2_ba_surface = st.text_area("Observações - Superfície do B.A (PÁ 2)", key="obs_pa2_ba_surface")

# 10.2.5
st.subheader("📸 10.2.5 Superfície da pá lado da pressão (PÁ 2)")
fotos_pa2_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_pressao")
obs_pa2_pressao = st.text_area("Observações - Superfície da pá lado da pressão (PÁ 2)", key="obs_pa2_pressao")

# 10.2.6
st.subheader("📸 10.2.6 Receptores do SPDA lado da pressão (PÁ 2)")
fotos_pa2_spda_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_spda_pressao")
obs_pa2_spda_pressao = st.text_area("Observações - Receptores do SPDA lado da pressão (PÁ 2)", key="obs_pa2_spda_pressao")

# 10.2.7
st.subheader("📸 10.2.7 Superfície no B.A lado da pressão (PÁ 2)")
fotos_pa2_ba_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa2_ba_pressao")
obs_pa2_ba_pressao = st.text_area("Observações - Superfície no B.A lado da pressão (PÁ 2)", key="obs_pa2_ba_pressao")

# ----------------------------- PÁ 3 ----------------------------- fotos e Observações
st.subheader("📸 10.3 Inspeção Externa - PÁ 3")

# 10.3.1
st.subheader("📸 10.3.1 Superfície da pá lado sucção (PÁ 3)")
fotos_pa3_superficie = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_superficie")
obs_pa3_superficie = st.text_area("Observações - Superfície da pá lado sucção (PÁ 3)", key="obs_pa3_superficie")

# 10.3.2
st.subheader("📸 10.3.2 Receptores do SPDA lado sucção (PÁ 3)")
fotos_pa3_spda = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_spda")
obs_pa3_spda = st.text_area("Observações - Receptores SPDA lado sucção (PÁ 3)", key="obs_pa3_spda")

# 10.3.3
st.subheader("📸 10.3.3 B.A lado da sucção (PÁ 3)")
fotos_pa3_ba_succao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_ba_succao")
obs_pa3_ba_succao = st.text_area("Observações - B.A lado da sucção (PÁ 3)", key="obs_pa3_ba_succao")

# 10.3.4
st.subheader("📸 10.3.4 Superfície do B.A (PÁ 3)")
fotos_pa3_ba_surface = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_ba_surface")
obs_pa3_ba_surface = st.text_area("Observações - Superfície do B.A (PÁ 3)", key="obs_pa3_ba_surface")

# 10.3.5
st.subheader("📸 10.3.5 Superfície da pá lado da pressão (PÁ 3)")
fotos_pa3_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_pressao")
obs_pa3_pressao = st.text_area("Observações - Superfície da pá lado da pressão (PÁ 3)", key="obs_pa3_pressao")

# 10.3.6
st.subheader("📸 10.3.6 Receptores do SPDA lado da pressão (PÁ 3)")
fotos_pa3_spda_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_spda_pressao")
obs_pa3_spda_pressao = st.text_area("Observações - Receptores do SPDA lado da pressão (PÁ 3)", key="obs_pa3_spda_pressao")

# 10.3.7
st.subheader("📸 10.3.7 Superfície no B.A lado da pressão (PÁ 3)")
fotos_pa3_ba_pressao = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="pa3_ba_pressao")
obs_pa3_ba_pressao = st.text_area("Observações - Superfície no B.A lado da pressão (PÁ 3)", key="obs_pa3_ba_pressao")



# ----------------------------- Dicionários de imagens e observações -----------------------------


# Função para salvar imagens
def salvar_imagens(fotos, prefixo, limite=2):
    caminhos = []
    if fotos:
        for i, foto in enumerate(fotos[:limite]):
            if foto is not None:
                extensao = foto.type.split("/")[-1]
                caminho = f"{prefixo}_{i}.{extensao}"
                try:
                    conteudo = foto.read()
                    if conteudo:
                        with open(caminho, "wb") as f:
                            f.write(conteudo)
                        caminhos.append(caminho)
                except Exception as e:
                    st.error(f"Erro ao salvar imagem: {foto.name} - {e}")
    return caminhos

# -------------------------- Salvar imagens por PÁ --------------------------

# Salva imagens da PÁ 1
caminhos_pa1_superficie = salvar_imagens(fotos_pa1_superficie, "pa1_superficie", 2)
caminhos_pa1_spda = salvar_imagens(fotos_pa1_spda, "pa1_spda", 2)
caminhos_pa1_ba_succao = salvar_imagens(fotos_pa1_ba_succao, "pa1_ba_succao", 2)
caminhos_pa1_ba_surface = salvar_imagens(fotos_pa1_ba_surface, "pa1_ba_surface", 2)
caminhos_pa1_pressao = salvar_imagens(fotos_pa1_pressao, "pa1_pressao", 2)
caminhos_pa1_spda_pressao = salvar_imagens(fotos_pa1_spda_pressao, "pa1_spda_pressao", 2)
caminhos_pa1_ba_pressao = salvar_imagens(fotos_pa1_ba_pressao, "pa1_ba_pressao", 2)

# Salva imagens da PÁ 2
caminhos_pa2_superficie = salvar_imagens(fotos_pa2_superficie, "pa2_superficie", 2)
caminhos_pa2_spda = salvar_imagens(fotos_pa2_spda, "pa2_spda", 2)
caminhos_pa2_ba_succao = salvar_imagens(fotos_pa2_ba_succao, "pa2_ba_succao", 2)
caminhos_pa2_ba_surface = salvar_imagens(fotos_pa2_ba_surface, "pa2_ba_surface", 2)
caminhos_pa2_pressao = salvar_imagens(fotos_pa2_pressao, "pa2_pressao", 2)
caminhos_pa2_spda_pressao = salvar_imagens(fotos_pa2_spda_pressao, "pa2_spda_pressao", 2)
caminhos_pa2_ba_pressao = salvar_imagens(fotos_pa2_ba_pressao, "pa2_ba_pressao", 2)

# Salva imagens da PÁ 3
caminhos_pa3_superficie = salvar_imagens(fotos_pa3_superficie, "pa3_superficie", 2)
caminhos_pa3_spda = salvar_imagens(fotos_pa3_spda, "pa3_spda", 2)
caminhos_pa3_ba_succao = salvar_imagens(fotos_pa3_ba_succao, "pa3_ba_succao", 2)
caminhos_pa3_ba_surface = salvar_imagens(fotos_pa3_ba_surface, "pa3_ba_surface", 2)
caminhos_pa3_pressao = salvar_imagens(fotos_pa3_pressao, "pa3_pressao", 2)
caminhos_pa3_spda_pressao = salvar_imagens(fotos_pa3_spda_pressao, "pa3_spda_pressao", 2)
caminhos_pa3_ba_pressao = salvar_imagens(fotos_pa3_ba_pressao, "pa3_ba_pressao", 2)

# -------------------------- Dicionários de imagens e observações por PÁ --------------------------

imagens_obs_pa1 = {
    "Superfície da pá lado sucção": (caminhos_pa1_superficie, obs_pa1_superficie),
    "Receptores do SPDA lado sucção": (caminhos_pa1_spda, obs_pa1_spda),
    "B.A lado da sucção": (caminhos_pa1_ba_succao, obs_pa1_ba_succao),
    "Superfície do B.A": (caminhos_pa1_ba_surface, obs_pa1_ba_surface),
    "Superfície da pá lado da pressão": (caminhos_pa1_pressao, obs_pa1_pressao),
    "Receptores do SPDA lado da pressão": (caminhos_pa1_spda_pressao, obs_pa1_spda_pressao),
    "Superfície no B.A lado da pressão": (caminhos_pa1_ba_pressao, obs_pa1_ba_pressao),
}

imagens_obs_pa2 = {
    "Superfície da pá lado sucção": (caminhos_pa2_superficie, obs_pa2_superficie),
    "Receptores do SPDA lado sucção": (caminhos_pa2_spda, obs_pa2_spda),
    "B.A lado da sucção": (caminhos_pa2_ba_succao, obs_pa2_ba_succao),
    "Superfície do B.A": (caminhos_pa2_ba_surface, obs_pa2_ba_surface),
    "Superfície da pá lado da pressão": (caminhos_pa2_pressao, obs_pa2_pressao),
    "Receptores do SPDA lado da pressão": (caminhos_pa2_spda_pressao, obs_pa2_spda_pressao),
    "Superfície no B.A lado da pressão": (caminhos_pa2_ba_pressao, obs_pa2_ba_pressao),
}

imagens_obs_pa3 = {
    "Superfície da pá lado sucção": (caminhos_pa3_superficie, obs_pa3_superficie),
    "Receptores do SPDA lado sucção": (caminhos_pa3_spda, obs_pa3_spda),
    "B.A lado da sucção": (caminhos_pa3_ba_succao, obs_pa3_ba_succao),
    "Superfície do B.A": (caminhos_pa3_ba_surface, obs_pa3_ba_surface),
    "Superfície da pá lado da pressão": (caminhos_pa3_pressao, obs_pa3_pressao),
    "Receptores do SPDA lado da pressão": (caminhos_pa3_spda_pressao, obs_pa3_spda_pressao),
    "Superfície no B.A lado da pressão": (caminhos_pa3_ba_pressao, obs_pa3_ba_pressao),
}

          
# ----------------------------- INSPEÇÃO INTERNA -----------------------------
st.subheader("📸 11.1 Identificação da pá 1")
fotos_identificacao_pa1 = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="ident_pa1")
caminhos_ident_pa1 = salvar_imagens(fotos_identificacao_pa1, "ident_pa1", limite=2)

st.subheader("📸 11.1 Identificação da pá 2")
fotos_identificacao_pa2 = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="ident_pa2")
caminhos_ident_pa2 = salvar_imagens(fotos_identificacao_pa2, "ident_pa2", limite=2)

st.subheader("📸 11.1 Identificação da pá 3")
fotos_identificacao_pa3 = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="ident_pa3")
caminhos_ident_pa3 = salvar_imagens(fotos_identificacao_pa3, "ident_pa3", limite=2)

def tabela_defeitos_interna(numero_pa):
    st.subheader(f"📋 11.2 Tabela de Defeitos - PÁ {numero_pa}")
    tabela = []
    localizacoes = ["C.E.", "B.F.", "B.F.C.", "I.D.B.F.", "E.D.B. F.", "A.B.F.", 
                    "I.D.E.A.", "A.B.A.", "I.D.B.A.", "E.D.B.A.", "B.A.", "B.A.C"]

    for loc in localizacoes:
        st.markdown(f"**📌 Localização: {loc} (PÁ {numero_pa})**")
        desc = st.text_input(f"Descrição dos danos/evidências - {loc} (PÁ {numero_pa})", key=f"desc_def_pa{numero_pa}_{loc}")
        area = st.text_input(f"Área - {loc} (PÁ {numero_pa})", key=f"area_def_pa{numero_pa}_{loc}")
        cor = st.text_input(f"Cor - {loc} (PÁ {numero_pa})", key=f"cor_def_pa{numero_pa}_{loc}")
        tabela.append({
            "Localizacao": loc,
            "Descricao": desc or "OK",
            "Area": area or "-",
            "Cor": cor or "-"
        })
    return tabela

# Tabelas para cada pá
tabela_defeitos_pa1 = tabela_defeitos_interna(1)
tabela_defeitos_pa2 = tabela_defeitos_interna(2)
tabela_defeitos_pa3 = tabela_defeitos_interna(3)


def bloco_obs_fotos_interna(pa_num):
    st.subheader(f"📷 11.2 Itens com evidências fotográficas - PÁ {pa_num}")
    imagens_obs = {}
    topicos = [
        "11.2.1 B.A Não apresenta falhas de colagem visíveis",
        "11.2.2 Superfície entre as almas do B.F e Alma do B.A",
        "11.2.3 Coletores do SPDA",
        "11.2.4 B.F não apresenta falhas de colagem visíveis"
    ]
    for i, titulo in enumerate(topicos):
        st.subheader(f"📸 {titulo} (PÁ {pa_num})")
        fotos = st.file_uploader("Envie até 2 fotos", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key=f"int_foto_pa{pa_num}_{i}")
        obs = st.text_area(f"Observações - {titulo} (PÁ {pa_num})", key=f"int_obs_pa{pa_num}_{i}")
        caminhos = salvar_imagens(fotos, f"int_pa{pa_num}_{i}", limite=2)
        imagens_obs[titulo] = (caminhos, obs)
    return imagens_obs

# Dicionários com imagens e observações por PÁ
imagens_obs_interna_pa1 = bloco_obs_fotos_interna(1)
imagens_obs_interna_pa2 = bloco_obs_fotos_interna(2)
imagens_obs_interna_pa3 = bloco_obs_fotos_interna(3)



# BOTÃO PARA GERAR O RELATÓRIO

if st.button("📄 Gerar Relatório em PDF"):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.primeira_pagina(
    ambito_aplicacao,
    codigo_relatorio,
    revisado_por_1,
    revisado_por_2,
    data_revisao
)

    pdf.pagina_sumario()

    dados_gerais = {
        "Fabricante Modelo": fabricante_modelo,
        "Modelo": modelo,
        "Ano de Fabricação": ano_fabricacao,
        "Altura do torre": altura_torre
    }

    dados_pas = {
        "Fabricante": fabricante_pas,
        "Tipo de Pá de Rotor": tipo_pa,
        "Número de Série das Pás": num_serie_pas,
        "Número de Série do Set": num_serie_set,
        "Elementos de Fluxo de Ar": elementos_fluxo,
        "Dispositivos de iluminação": dispositivos_luz
    }

    pdf.pagina_dados(dados_gerais, dados_pas)
    pdf.pagina_nomenclaturas()
    pdf.pagina_itens_referencia_identificacao(imagem_maquina_path)
    pdf.pagina_identificacao_pas(imagens_pás)

    # Inspeção completa por pá
    pdf.pagina_inspecao_completa_pa(1, tabela_externa_pa1, imagens_obs_pa1)
    pdf.pagina_inspecao_completa_pa(2, tabela_externa_pa2, imagens_obs_pa2)
    pdf.pagina_inspecao_completa_pa(3, tabela_externa_pa3, imagens_obs_pa3)

    #----------------------------- Inspeção Interna -----------------------------
    pdf.pagina_inspecao_interna_completa_pa(1, caminhos_ident_pa1, tabela_defeitos_pa1, imagens_obs_interna_pa1)
    pdf.pagina_inspecao_interna_completa_pa(2, caminhos_ident_pa2, tabela_defeitos_pa2, imagens_obs_interna_pa2)
    pdf.pagina_inspecao_interna_completa_pa(3, caminhos_ident_pa3, tabela_defeitos_pa3, imagens_obs_interna_pa3)


    caminho_pdf = "relatorio_inspecao.pdf"
    pdf.output(caminho_pdf)

    st.success("✅ Relatório gerado com sucesso!")

    with open(caminho_pdf, "rb") as f:
        st.download_button(
            label="📥 Baixar PDF",
            data=f,
            file_name="relatorio_inspecao.pdf",
            mime="application/pdf"
        )

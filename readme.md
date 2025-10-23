# 🎧 **Projeto Playlist**

Uma aplicação web interativa desenvolvida com **Python** e **Streamlit** para explorar diferentes **gêneros musicais** e **artistas**, exibindo vídeos do YouTube e informações sobre cada um.  

Ideal para praticar conceitos de **dicionários**, **entrada e saída de dados**, **condicionais** e **interfaces lowcode** com Streamlit.

---

## 🧩 **Situação-Problema**

Você foi contratado por uma **startup de música** para desenvolver um protótipo de plataforma interativa cujo objetivo é permitir que os usuários descubram novos artistas a partir de seus **gêneros musicais preferidos**.  

A plataforma deve oferecer:

- Uma **lista de gêneros musicais** (ex: Sertanejo, Pagode, Eletrônica);  
- Uma **lista de artistas** que muda conforme o gênero escolhido;  
- Um **vídeo do YouTube** exibido diretamente na aplicação;  
- Uma aba “**Sobre o artista**” com um pequeno texto descritivo.

Com isso, o usuário pode escolher um gênero, descobrir artistas e assistir a um vídeo, tudo em uma interface simples e divertida.

---

## 🎯 **Objetivo Educacional**

- Praticar o uso de **dicionários em Python**.  
- Trabalhar com **entrada de dados** utilizando componentes do Streamlit.  
- Criar **condicionais** para exibir informações diferentes conforme a escolha do usuário.  
- Desenvolver uma **interface web interativa** com Streamlit (frontend lowcode).  

---

## 📝 **Enunciado**

O projeto consiste em uma aplicação web que realiza os seguintes passos:

1. O usuário escolhe um **gênero musical** em um menu lateral.  
2. A partir do gênero, o sistema exibe uma **lista de artistas** relacionados.  
3. Após escolher o artista, são abertas duas **abas** no corpo da página:  
   - **Vídeo:** mostra um vídeo do YouTube do artista;  
   - **Sobre o artista:** exibe um texto com informações sobre o artista.  

Os links dos vídeos e os textos descritivos estão definidos em um **dicionário Python**, tornando o código simples e fácil de expandir.

---

## 🎬 **Exemplo de uso**

1. O usuário seleciona o gênero **Trap**.  
2. O app exibe as opções: **Matuê** e **Teto**.  
3. Ao escolher **Matuê**, o vídeo e as informações do artista são carregadas automaticamente.

**Saída esperada:**

🎵 “Matuê”  
> Exibe um vídeo incorporado do YouTube e um texto biográfico sobre o artista.

---

## 💻 **Como executar**

**Pré-requisito:** Python 3.8 ou superior

### Passos:

1. Clone este repositório ou baixe os arquivos:

```bash
git clone https://github.com/TJfiles/Projeto_playlist.git
cd Projeto_playlist
```

2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt

```

3. Execute o aplicativo Streamlit:

```bash
python -m streamlit run app.py

```

4. O navegador abrirá automaticamente (ou acesse http://localhost:8501)

--- 

# 🧠 Conceitos trabalhados

- Estrutura de dados Dicionário (dict)

- Entrada e saída de dados com st.selectbox()

- Exibição de vídeos com st.video()

- Uso de condicionais (if/elif)

- Criação de interfaces lowcode com Streamlit



import streamlit as st 

generos = {
    'Trap' : {
        'Matuê' : 'https://www.youtube.com/watch?v=ZPcG9PCfagM',
        'Teto' : 'https://www.youtube.com/watch?v=7AlAYttGnAg'
    },
    'Sertanejo' : {
        'Gustavo Lima' : 'https://www.youtube.com/watch?v=hEBjnXXWgKU',
        'Renner Azevedo' : 'https://www.youtube.com/watch?v=AxGv4RG9DqY'
    },
    'Pagode' : {
        'Zeca Pagodinho' : 'https://www.youtube.com/watch?v=oTREAvZbmME',
        'Tiaguinho' : 'https://www.youtube.com/watch?v=qUqc_cYejX0'
    },
    'Eletronica' : {
        'Alok' : 'https://www.youtube.com/watch?v=JVpTp8IHdEg',
        'Calvin Harris' : 'https://www.youtube.com/watch?v=ebXbLfLACGM'
    }
}

st.sidebar.title('Mago das playlists')
st.sidebar.image('mago.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())

artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)

video, sobre = st.tabs(['Vídeo', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Matuê':
        st.markdown('''
            Matheus Brasileiro Aguiar (Fortaleza, 11 de outubro de 1993), mais conhecido como Matuê, é um rapper, cantor, compositor, guitarrista e empresário brasileiro. Ficou conhecido com o single "Anos Luz", lançado em 2017 e pelo álbum "Máquina do Tempo" lançado em 2020. É considerado um dos símbolos do trap brasileiro.[1][2]

            Foi o único artista de hip hop em 2023 a ter 10 músicas com mais de 100 milhões de streams nas plataformas digitais.[3]
            ''')
    
    elif artista == 'Teto':
        st.markdown('''
            Clériton Sávio Santos Silva (Jacobina, 19 de outubro de 2001), mais conhecido como Teto, é um rapper, cantor e compositor brasileiro. Ficou conhecido por meio das prévias de suas músicas que foram lançadas não oficialmente em vários canais do YouTube, alcançando milhões de visualizações e ganhando fama em redes sociais como o TikTok e Instagram.[1][2]
            ''')
        
    elif artista == 'Gustavo Lima':
        st.markdown(''' 
            Nivaldo Batista Lima (Presidente Olegário, 3 de setembro de 1989), mais conhecido pelo nome artístico Gusttavo Lima, é um cantor, compositor, produtor musical e empresário brasileiro.[2][3]

            Gusttavo Lima possui uma fortuna avaliada em mais de 1 bilhão de reais, consolidando-se como um dos artistas mais ricos do Brasil.[4][5]
            ''')
        
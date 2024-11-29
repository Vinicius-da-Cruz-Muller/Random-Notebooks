import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


def exibir_estrelas():

    st.markdown(
    """
    <style>
        /* Cor do fundo da sidebar */
        [data-testid="stSidebar"] {
            background-color: #7e78d240; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)
    
    

    with st.sidebar:
        selected = option_menu(
            menu_title = None,
            options = ["Equipe", "Estrelas", "Pulsares", "Análise", "Conclusão"],
            icons=['star', 'star-fill', 'star-half', 'stars', 'sun-fill'], 
            styles={
            "container": {"background-color": "#7e78d250"},  
            "icon": {"color": "#01172f70", "font-size": "20px"},  
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "10px",
                "--hover-color": "#6f58c9",
            },
            "nav-link-selected": {"background-color": "#6f58c9", "color": "white"},
        },
        )

    if selected == "Equipe":
        st.session_state.pagina_atual = "home"  
        st.rerun()
    if selected == "Estrelas":
        pass
    if selected == "Pulsares":
        st.session_state.pagina_atual = "pulsares"  
        st.rerun()
    if selected == "Análise":
        st.session_state.pagina_atual = "analise"
        st.rerun()
    if selected == "Conclusão":
        st.session_state.pagina_atual = "conclusao"
        st.rerun()

        
    st.title("Ciclo de Vida das Estrelas")

    # st.write("""
    # Estrelas nascem em nuvens densas de gás e poeira, vivem em diferentes fases de brilho e energia, 
    # e ao final de suas vidas, podem se tornar alguns dos objetos mais intrigantes do cosmos.
    # """)


    st.header("Formação de Estrelas")
    st.write("""
    As estrelas se formam em nuvens gigantes de gás e poeira chamadas nebulosas. A gravidade faz com que essas nuvens colapsem, 
    criando regiões densas que eventualmente se tornam tão quentes que iniciam reações de fusão nuclear — o nascimento de uma estrela.
    """)

    # Código HTML para embutir o vídeo centralizado
    video_url = """
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
        <iframe width="560" height="315" 
        src="https://www.youtube.com/embed/mkktE_fs4NA?start=45&end=68&autoplay=0&mute=1&loop=0&playlist=mkktE_fs4NA" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    """

    st.markdown(video_url, unsafe_allow_html=True)

    st.header("Ciclo de Vida")
    st.write("""
    Após o nascimento, a estrela entra na fase principal de sua vida, chamada sequência principal. Aqui, ela queima hidrogênio em seu núcleo para gerar energia. 
    A duração dessa fase depende da massa da estrela: estrelas maiores vivem menos, enquanto estrelas menores vivem por bilhões de anos.""")

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.image("img\ciclo.png", use_container_width=True, caption="Ciclo de Vida da Estrela")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("""Quando o combustível de hidrogênio se esgota, a estrela evolui, expandindo-se para uma gigante vermelha (se for de baixa massa) ou supergigante (se for de alta massa).
    """)
    # Destinos finais
    st.header("O Fim de uma Estrela")
    st.write("""
    O destino de uma estrela depende de sua massa:
    - **Anãs Brancas**: Estrelas de baixa massa terminam como anãs brancas, resfriando lentamente ao longo de bilhões de anos.
    - **Buracos Negros**: Estrelas muito massivas colapsam sob sua própria gravidade, formando buracos negros.
    - **Pulsares (ou Estrelas de Nêutrons)**: Algumas estrelas massivas deixam para trás núcleos incrivelmente densos, que podem emitir feixes regulares de radiação.
    """)



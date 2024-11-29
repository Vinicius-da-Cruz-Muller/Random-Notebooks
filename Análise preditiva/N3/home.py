import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


def exibir_home():
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
        pass
    if selected == "Estrelas":
        st.session_state.pagina_atual = "estrelas"  
        st.rerun()
    if selected == "Pulsares":
        st.session_state.pagina_atual = "pulsares"  
        st.rerun()
    if selected == "Análise":
        st.session_state.pagina_atual = "analise"
        st.rerun()
    if selected == "Conclusão":
        st.session_state.pagina_atual = "conclusao"
        st.rerun()


    st.title("Equipe")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Vinícius Muller")
        st.image("profile/vini.png",  use_container_width=True)

    with col2:
        st.header("Nathalya Melchert")
        st.image("profile/nat.png",  use_container_width=True)

    with col3:
        st.header("Daniele Orzechowski")
        st.image("profile/dani.jpg",  use_container_width=True)

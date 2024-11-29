import streamlit as st
# from ydata_profiling import ProfileReport
from home import exibir_home
from estrelas import exibir_estrelas
from pulsares import exibir_pulsares
from analise import exibir_analise
from conclusao import exibir_conclusao


st.set_page_config(
    page_title="N3 - Pulsares",
    page_icon="star2",
    layout="wide", 
    initial_sidebar_state="expanded",
)

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "home"  

if st.session_state.pagina_atual == "home":
    exibir_home()
elif st.session_state.pagina_atual == "estrelas":
    exibir_estrelas()
elif st.session_state.pagina_atual == "pulsares":
    exibir_pulsares()
elif st.session_state.pagina_atual == "analise":
    exibir_analise()
elif st.session_state.pagina_atual == "conclusao":
    exibir_conclusao()

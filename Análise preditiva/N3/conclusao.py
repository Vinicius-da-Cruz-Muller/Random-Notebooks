import streamlit as st
from streamlit_option_menu import option_menu


def exibir_conclusao():
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
        st.session_state.pagina_atual = "estrelas"
        st.rerun()
    if selected == "Pulsares":
        st.session_state.pagina_atual = "pulsares"  
        st.rerun()
    if selected == "Análise":
        st.session_state.pagina_atual = "analise"
        st.rerun()
    if selected == "Conclusão":
        pass



    st.title("Projeto N3 - Análise Preditiva de Pulsares")

    st.markdown("""
    Este projeto teve como objetivo a identificação de pulsares (estrelas de nêutrons) através da análise de dados. 
    Utilizamos um conjunto de dados contendo características de objetos estelares, e aplicamos técnicas de aprendizado de máquina 
    para construir um modelo preditivo.
    """)

    st.header("Conclusões e Análises")

    st.markdown("""
    **Análise Exploratória:**

    * O conjunto de dados apresentou um desbalanceamento significativo entre as classes, com a maioria dos objetos sendo não-pulsares.
    * Foram identificados alguns valores ausentes em variáveis específicas, que foram tratados com técnicas de imputação.
    * A análise de correlação revelou a existência de relações entre algumas features, o que pode ser útil para a modelagem.

    **Modelagem:**

    * Utilizamos o algoritmo RandomForest para construir o modelo preditivo.
    * A técnica de oversampling SMOTE foi aplicada para balancear o conjunto de dados de treinamento.
    * O modelo apresentou boa performance, com alta acurácia e precisão na identificação de pulsares.
    * As features mais importantes para o modelo foram identificadas, fornecendo insights sobre as características mais relevantes para a detecção de pulsares.
    """)

    # st.header("Recomendações")
    # st.markdown("""
    # * Explorar outros algoritmos de aprendizado de máquina para comparar a performance com o RandomForest.
    # * Investigar técnicas mais avançadas de tratamento de dados ausentes.
    # * Realizar uma análise mais detalhada das features mais importantes para o modelo.
    # * Coletar mais dados para aumentar a robustez do modelo e generalização.
    # """)

    st.header("Impacto do Projeto")
    st.markdown("""
    O modelo desenvolvido neste projeto pode auxiliar na identificação de pulsares de forma mais eficiente, o que contribui para o avanço da pesquisa 
    em astrofísica. A detecção automatizada de pulsares pode acelerar a descoberta de novos objetos e possibilitar estudos mais aprofundados sobre 
    esses fascinantes corpos celestes.
    """)

    st.header("Considerações Finais")
    st.markdown("""
    Este projeto demonstrou a aplicação prática de técnicas de ciência de dados para a resolução de problemas em astronomia. 
    Acreditamos que os resultados obtidos são promissores e que este trabalho pode servir como base para futuras pesquisas na área.
    """)
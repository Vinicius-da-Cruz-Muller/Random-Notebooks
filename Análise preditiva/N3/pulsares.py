import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


def exibir_pulsares():
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
            menu_title=None,
            options=["Equipe", "Estrelas", "Pulsares", "Análise", "Conclusão"],
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
        pass
    if selected == "Análise":
        st.session_state.pagina_atual = "analise"
        st.rerun()
    if selected == "Conclusão":
        st.session_state.pagina_atual = "conclusao"
        st.rerun()

    # Título da página
    st.title("Pulsares")

    # Introdução
    st.write("""
    Pulsares são estrelas de nêutrons altamente densas e rotacionando rapidamente, resultando na emissão de feixes de radiação eletromagnética, 
    que são observados de maneira periódica como pulsos regulares de luz. Eles são formados quando uma estrela massiva explode em uma supernova,
    deixando para trás um núcleo incrivelmente denso. Esses feixes de radiação são uma das formas mais precisas de medição do tempo e espaço no universo.
    """)

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.image("img/vela_pulsar.gif", use_container_width=True, caption="Pulsar Vela - 800 anos-luz da Terra. GIF consiste de 8 imagens do pulsar")
    st.markdown("</div>", unsafe_allow_html=True)


    # Vídeo embutido
    # video_url = """
    # <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
    #     <iframe width="560" height="315" 
    #     src="https://www.youtube.com/embed/RvD2pWhGmcE" 
    #     frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    # </div>
    # """
    # st.markdown(video_url, unsafe_allow_html=True)

    # Ciclo de vida de um pulsar
    st.header("Ciclo de Vida dos Pulsares")
    st.write("""
    O ciclo de vida de um pulsar começa após a explosão de uma supernova, que resulta na formação de uma estrela de nêutrons. 
    Inicialmente, o pulsar gira a uma velocidade extremamente alta e emite feixes de radiação. À medida que o pulsar envelhece, 
    sua rotação diminui gradualmente e a emissão de radiação também enfraquece. No entanto, alguns pulsares podem continuar emitindo 
    radiação por bilhões de anos.
    """)
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.image("img/pulsar.gif", use_container_width=True, caption="Representação artística de um Pulsar")
    st.markdown("</div>", unsafe_allow_html=True)
    

    # Destinos finais
    st.header("O Fim de um Pulsar")
    st.write("""
    Eventualmente, os pulsares podem perder sua rotação rápida e se tornarem objetos mais estáveis. 
    Alguns podem até desaparecer do radar de observação, mas o estudo de pulsares continua a ser uma das áreas mais fascinantes 
    da astrofísica, permitindo medir distâncias e até mesmo estudar fenômenos extremos como buracos negros e ondas gravitacionais.
    """)

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.image("img/pulse.gif", width=500, caption="Como um pulsar é visto nos registros astronômicos")
    st.markdown("</div>", unsafe_allow_html=True)

    # Conclusão
    st.write("""
    Os pulsares são um dos exemplos mais impressionantes da física extrema do universo, e seu estudo nos ajuda a entender melhor a evolução das estrelas,
    bem como as leis da relatividade e da gravidade em condições extremas.
    """)


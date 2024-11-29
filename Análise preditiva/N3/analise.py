import streamlit as st
import psycopg2
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from sklearn.metrics import roc_curve, roc_auc_score
# from ydata_profiling import ProfileReport
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import SMOTE


from db_connection import get_db_connection, is_connection_open


# Obtendo a conexão
conn = get_db_connection()


def exibir_analise():
    global conn

    if not is_connection_open(conn):
        conn = get_db_connection()
        if conn is None:
            st.error("Erro ao conectar ao banco de dados.")
            return
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
        pass
    if selected == "Conclusão":
        st.session_state.pagina_atual = "conclusao"
        st.rerun()


    st.title('Projeto N3 - Análise Preditiva de Pulsares')

    # st.markdown('### Daniele Orzechowski, Nathalya e Vinícius Muller')

    # Descrição do projeto
    st.markdown('#### O objetivo do projeto é identificar se um objeto é ou não um pulsar (estrela de nêutrons).')
    

    query_test="SELECT * FROM pulsar_data_test"
    df_test = pd.read_sql(query_test, conn)

    query_train="SELECT * FROM pulsar_data_train"
    df_train = pd.read_sql(query_train, conn)

    # conn.close()
    

    with st.expander("Análise Exploratória de Dados"):
        st.subheader("Primeiras Linhas dos Dados")
        st.write("Conjunto de Treinamento:")
        st.dataframe(df_train.head())
        st.write("Conjunto de Teste:")
        st.dataframe(df_test.head())

        # # Mostrar informações gerais dos DataFrames
        # st.subheader("Informações Gerais dos Dados")
        # st.write("Conjunto de Treinamento:")
        # st.write(df_train.info())
        # st.write("Conjunto de Teste:")
        # st.write(df_test.info())

        st.subheader("Estatísticas Descritivas")
        st.write("Conjunto de Treinamento:")
        st.write(df_train.describe())
        st.write("Conjunto de Teste:")
        st.write(df_test.describe())
#-------------------------------------------------------------------------------------------------------
        st.subheader("Valores Nulos")
        st.write("Conjunto de Treinamento:")
        st.write(df_train.isnull().sum())
        st.write("Conjunto de Teste:")
        st.write(df_test.isnull().sum())

        st.subheader("Proporção de Valores Nulos por Coluna")
        st.write("Conjunto de Treinamento:")
        missing_percentage_train = df_train.isnull().mean() * 100
        st.write(missing_percentage_train)
        st.write("Conjunto de Teste:")
        missing_percentage_test = df_test.isnull().mean() * 100
        st.write(missing_percentage_test)


        st.subheader("Mapa de Calor de valores nulos")

        st.write("Conjunto de Treinamento:")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df_train.isnull(), cbar=True, cmap='viridis')
        plt.title("Mapa de Calor dos Valores Faltantes - Conjunto de Treinamento")
        st.pyplot(plt)  
        plt.clf()  

        st.write("Conjunto de Teste:")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df_test.isnull(), cbar=True, cmap='viridis')
        plt.title("Mapa de Calor dos Valores Faltantes - Conjunto de Teste")
        st.pyplot(plt)  
        plt.clf()  

        st.write("Drop dos nulos no DM-SNR_Skewness")
        df_train.dropna(subset=['skewness_dm_snr_curve'], inplace=True)
        df_test.dropna(subset=['skewness_dm_snr_curve'], inplace=True)

        st.write("Conjunto de Treinamento:")
        st.write(df_train.isnull().sum())  
        st.write("Conjunto de Teste:")
        st.write(df_test.isnull().sum()) 


        df_train['stddev_dm_snr_curve'] = df_train['stddev_dm_snr_curve'].fillna(df_train['stddev_dm_snr_curve'].mean())

        df_test['stddev_dm_snr_curve'] = df_test['stddev_dm_snr_curve'].fillna(df_test['stddev_dm_snr_curve'].mean())

        st.write("KNN Imputer com 5 vizinhos")
        imputer=KNNImputer(n_neighbors=5)
        df_train[["kurtosis_integrated_profile"]]=imputer.fit_transform(df_train[['kurtosis_integrated_profile']])
        df_test[["kurtosis_integrated_profile"]]=imputer.fit_transform(df_test[['kurtosis_integrated_profile']])

        st.write("Conjunto de Treinamento:")
        st.write(df_train.isnull().sum())  
        st.write("Conjunto de Teste:")
        st.write(df_test.isnull().sum()) 


        st.subheader("Estatísticas em valores")
        st.write("Conjunto de Treinamento:")
        st.write(round(df_train.describe(),2))
        st.write("Conjunto de Teste:")
        st.write(round(df_train.describe(),2))


        st.subheader("Histogramas das Variáveis")
        fig, ax = plt.subplots(figsize=(12, 10))
        df_train.hist(bins=20, color='skyblue', edgecolor='black', ax=ax)
        plt.suptitle("Distribuições das Variáveis - Conjunto de Treinamento")
        st.pyplot(fig)

        st.subheader("Boxplots das Variáveis")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.boxplot(data=df_train, palette="Set2", ax=ax)
        plt.title("Boxplot das Variáveis - Conjunto de Treinamento")
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.subheader("Matriz de Correlação")
        fig, ax = plt.subplots(figsize=(10, 8))
        correlation_matrix = df_train.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        plt.title("Matriz de Correlação")
        st.pyplot(fig)


    with st.expander("Modelagem Preditiva"):
        X = df_train.drop('target_class', axis=1)
        y = df_train['target_class']

        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        smote = SMOTE(random_state=42)
        X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

        st.write("Distribuição da variável alvo após SMOTE no conjunto de treinamento:")
        st.write(pd.Series(y_train_res).value_counts(normalize=True))

        st.subheader("Distribuição da Variável Alvo Após SMOTE")
        plt.figure(figsize=(8, 6))
        sns.countplot(x=y_train_res, palette="viridis")
        plt.title("Distribuição da Variável Alvo Após SMOTE")
        plt.xlabel('Classes')
        plt.ylabel('Contagem')

        st.pyplot(plt)
        plt.clf()


        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_res, y_train_res)

        y_val_pred = model.predict(X_val)
        cm = confusion_matrix(y_val, y_val_pred)

        st.subheader("Matriz de Confusão - Conjunto de Validação")
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Classe 0', 'Classe 1'], yticklabels=['Classe 0', 'Classe 1'])
        plt.xlabel('Predição')
        plt.ylabel('Valor Real')
        plt.title('Matriz de Confusão - Conjunto de Validação')

        st.pyplot(plt)

        st.write(f"Acurácia no conjunto de validação (distribuição original): {accuracy_score(y_val, y_val_pred)}")
        st.write("\nRelatório de classificação no conjunto de validação:")
        st.text(classification_report(y_val, y_val_pred))


        y_val_proba = model.predict_proba(X_val)[:, 1]
        fpr, tpr, thresholds = roc_curve(y_val, y_val_proba)

        auc_score = roc_auc_score(y_val, y_val_proba)

        st.subheader(f"Curva ROC (AUC = {auc_score:.2f})")
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='blue', label=f'AUC = {auc_score:.2f}')
        plt.plot([0, 1], [0, 1], color='red', linestyle='--')  # Linha de referência
        plt.xlabel('Taxa de Falsos Positivos (FPR)')
        plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
        plt.title('Curva ROC')
        plt.legend(loc='lower right')
        plt.grid()

        st.pyplot(plt)

        plt.clf()


        X_test = df_test.drop(columns=['target_class'])
        y_test_pred = model.predict(X_test)

        df_test['predicted_target_class'] = y_test_pred

        st.subheader("Previsões para o Conjunto de Teste")
        st.write(df_test.head())  

        feature_importance = model.feature_importances_
        features = X_train.columns

        importance_df = pd.DataFrame({'feature': features, 'importance': feature_importance})
        importance_df = importance_df.sort_values(by='importance', ascending=False)

        st.subheader("Importância das Features no Modelo RandomForest")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=importance_df, palette='viridis')
        plt.title('Importância das Features no Modelo RandomForest')

        st.pyplot(plt)

        plt.clf()
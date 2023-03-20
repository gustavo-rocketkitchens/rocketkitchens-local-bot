import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

# conn = init_connection()


# conexão com o banco de dados PostgreSQL
con = psycopg2.connect(host='localhost',
                       database='rocket',
                       # options=f"-c search_path={'rocket_kitchens'}",
                       user='rocket',
                       password='123')
# criando o cursos da conexão para acessar o banco
# cur = con.cursor()


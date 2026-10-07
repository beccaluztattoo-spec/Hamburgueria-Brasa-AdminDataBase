import streamlit as st 
import pandas as pd 
import re

from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

SERVIDOR = r"D11S22-1251880\SQLREBECCAADM"
BANCO = "HamburgueriaBrasa"
DRIVER = "ODBC Driver 18 for SQL Server"

USUARIO = "sa"
SENHA = "Senai@134"


def conectar ():
    # autenticação via windows utilizando ODBC

    odbc = (
        # f"DRIVER={{{DRIVER}}};SERVER={SERVIDOR};DATABASE{BANCO};"
        # f"UID={USUARIO};PWD={SENHA};"
        # "TrustServerCertificate=yes;" 
        
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVIDOR};"
        f"DATABASE={BANCO};"
        f"UID={USUARIO};"
        f"PWD={SENHA};"
        "TrustServerCertificate=yes;"
        
    )
    
    return create_engine("mssql+pyodbc:///?odbc_connect="+ quote_plus(odbc))

def consultar(sql):
    with conectar().connect() as conexao:
        return pd.read_sql(text(sql), conexao)
                         
                         
def mensagem_erro(erro):
    """Tira só a mensagem do SQL Server do meio do texto do erro."""
    achou = re.search(r"\[SQL Server\](.+?)\s*\(\d+\)", str(erro))
    return achou.group(1) if achou else str(erro)

                    
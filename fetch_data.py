"""

Puxar os dados via API Kaggle

"""

import kagglehub
import os
from pathlib import Path

aqui = Path(__file__).resolve().parent  # pasta do .py
diretorio = aqui / "raw"

if os.path.exists(diretorio) == False:
    os.mkdir(diretorio)

lista_diretorios = os.listdir(
    diretorio
)  # os.listdir lista tanto diretorios quanto arquivos existentes

if len(lista_diretorios) == 0:
    # Download latest version
    diretorio = kagglehub.dataset_download("lucaseloi13/brazilian-road-race-results")

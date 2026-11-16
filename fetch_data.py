"""

Puxar os dados via API Kaggle

"""

import os
from pathlib import Path

aqui = Path(__file__).resolve().parent  # pasta do .py
diretorio = aqui / "raw"

if os.path.exists(diretorio) == False:
    os.mkdir(diretorio)

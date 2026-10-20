import os
from pathlib import Path
import logging

Project_name = "Data-science"

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
)

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/utils/common.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/entity/config_entity.py",
    f"src/{Project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "requirements.txt",
    "research/research.ipynb",
    "template/index.html",
    "app.py"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Empty File created: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
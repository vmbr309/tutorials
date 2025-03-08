import os
import subprocess
import logging
import time
from tqdm import tqdm
import argparse  # Import argparse for command-line arguments

def setup_logging():
    logging.basicConfig(
        filename="project_setup.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def create_project_structure(parent_dir):
    try:
        project = input("Qual o título do projeto?\n").title()
        retranca = input("Qual a retranca do projeto?\n").title()
        
        project_path = os.path.join(parent_dir, project)
        
        if not os.path.exists(project_path):
            print(f"Ok, vou criar a raiz: {project_path}")
            logging.info(f"Creating project root: {project_path}")
            os.mkdir(project_path)
        else:
            print("Directory already exists, nothing to do")
            logging.warning(f"Directory already exists: {project_path}")
            return
        
        subdirs = [
            f"[{retranca}] PDF_Expedição",
            f"[{retranca}] Materiais PD",
            f"[{retranca}] Sala de Roteiro"
        ]
        
        print("Criando subdiretórios principais...")
        for folder in tqdm(subdirs, desc="Pastas Principais", unit="pasta"):
            path = os.path.join(project_path, folder)
            os.mkdir(path)
            logging.info(f"Created: {path}")
            time.sleep(0.5)
        
        wrfolder = os.path.join(project_path, f"[{retranca}] Sala de Roteiro")
        os.chdir(wrfolder)
        fls2 = [
            f"[{retranca}] PESQUISA",
            f"[{retranca}] ROTEIROS",
            f"[{retranca}] ATAS",
            f"[{retranca}] TEXTOS PD",
            f"[{retranca}] ARCOS"
        ]
        
        print("Criando subpastas na Sala de Roteiro...")
        for folder in tqdm(fls2, desc="Subpastas da Sala de Roteiro", unit="pasta"):
            os.mkdir(folder)
            logging.info(f"Created: {os.path.join(wrfolder, folder)}")
            time.sleep(0.5)
        
        print("Estrutura do projeto criada com sucesso!")
        print(os.listdir(project_path))
        
        try:
            subprocess.Popen(["open", project_path])
            logging.info(f"Opened Finder at: {project_path}")
        except FileNotFoundError:
            print("Não foi possível abrir o Finder. Este comando é específico para macOS.")
            logging.warning("Could not open Finder. This command is specific to macOS.")

        print("\n🎉 Tudo pronto! O projeto foi criado com sucesso e está aberto no Finder.\n")
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Cria a estrutura de pastas de um projeto.")
    parser.add_argument("parent_dir", help="Diretório raiz onde o projeto será criado.")
    args = parser.parse_args()
    
    create_project_structure(args.parent_dir)
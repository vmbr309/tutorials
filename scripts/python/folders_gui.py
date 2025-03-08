import os
import subprocess
import logging
import time
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def setup_logging():
    logging.basicConfig(
        filename="project_setup.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def create_project_structure(parent_dir, project, retranca, log_display):
    try:
        project_path = os.path.join(parent_dir, project)

        if not os.path.exists(project_path):
            log_display.insert(tk.END, f"Ok, vou criar a raiz: {project_path}\n")
            logging.info(f"Creating project root: {project_path}")
            os.mkdir(project_path)
        else:
            log_display.insert(tk.END, "Directory already exists, nothing to do\n")
            logging.warning(f"Directory already exists: {project_path}")
            return

        subdirs = [
            f"[{retranca}] PDF_Expedição",
            f"[{retranca}] Materiais PD",
            f"[{retranca}] Sala de Roteiro"
        ]

        log_display.insert(tk.END, "Criando subdiretórios principais...\n")
        log_display.update_idletasks()
        for folder in subdirs:
            path = os.path.join(project_path, folder)
            os.mkdir(path)
            logging.info(f"Created: {path}")
            log_display.insert(tk.END, f"Criado: {path}\n")
            log_display.update_idletasks()
            time.sleep(0.2)

        wrfolder = os.path.join(project_path, f"[{retranca}] Sala de Roteiro")
        os.chdir(wrfolder)
        fls2 = [
            f"[{retranca}] PESQUISA",
            f"[{retranca}] ROTEIROS",
            f"[{retranca}] ATAS",
            f"[{retranca}] TEXTOS PD",
            f"[{retranca}] ARCOS"
        ]

        log_display.insert(tk.END, "Criando subpastas na Sala de Roteiro...\n")
        log_display.update_idletasks()
        for folder in fls2:
            os.mkdir(folder)
            logging.info(f"Created: {os.path.join(wrfolder, folder)}")
            log_display.insert(tk.END, f"Criado: {os.path.join(wrfolder, folder)}\n")
            log_display.update_idletasks()
            time.sleep(0.2)

        log_display.insert(tk.END, "Estrutura do projeto criada com sucesso!\n")
        log_display.insert(tk.END, str(os.listdir(project_path)) + "\n")

        try:
            subprocess.Popen(["open", project_path])
            logging.info(f"Opened Finder at: {project_path}")
        except FileNotFoundError:
            log_display.insert(tk.END, "Não foi possível abrir o Finder. Este comando é específico para macOS.\n")
            logging.warning("Could not open Finder. This command is specific to macOS.")

        log_display.insert(tk.END, "\n Tudo pronto! O projeto foi criado com sucesso e está aberto no Finder.\n")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        log_display.insert(tk.END, f"Ocorreu um erro: {str(e)}\n")

def create_project_gui():
    setup_logging()

    window = tk.Tk()
    window.title("Project Structure Creator")

    # Parent Directory
    tk.Label(window, text="Parent Directory:").grid(row=0, column=0, sticky="w")
    parent_dir_entry = tk.Entry(window, width=50)
    parent_dir_entry.grid(row=0, column=1, padx=5, pady=5)

    def browse_directory():
        directory = filedialog.askdirectory()
        parent_dir_entry.delete(0, tk.END)
        parent_dir_entry.insert(0, directory)

    tk.Button(window, text="Browse", command=browse_directory).grid(row=0, column=2, padx=5, pady=5)

    # Project Title
    tk.Label(window, text="Project Title:").grid(row=1, column=0, sticky="w")
    project_title_entry = tk.Entry(window, width=50)
    project_title_entry.grid(row=1, column=1, padx=5, pady=5)

    # Retranca
    tk.Label(window, text="Retranca:").grid(row=2, column=0, sticky="w")
    retranca_entry = tk.Entry(window, width=50)
    retranca_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create Button
    def create_project_button_click():
        parent_dir = parent_dir_entry.get()
        project_title = project_title_entry.get().title()
        retranca = retranca_entry.get().title()
        if not parent_dir or not project_title or not retranca:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        create_project_structure(parent_dir, project_title, retranca, log_display)

    tk.Button(window, text="Create Project", command=create_project_button_click).grid(row=3, column=1, pady=10)

    # Log Display
    log_display = scrolledtext.ScrolledText(window, width=60, height=15)
    log_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_project_gui()
import os
import subprocess

def main():
    pass
## add path to parent folder later as argument

# name the project
project = input("Qual o título do projeto?\n")
project = project.title()
retranca = input("Qual a retranca do projeto?\n")
retranca = retranca.title()

# create the directories for project root folder
if not os.path.exists(project):
print(f"Ok, vou criar a raiz: {project}")
os.mkdir(project)
os.chdir(project)
fls=["[{retranca}] PDF_Expedição", "[{retranca}] Materiais PD", "[{retranca}] Sala de Roteiro"]
[os.mkdir(i) for i in fls]

# create subfolders for folder "Sala de Roteiro"
wrfolder = "[{retranca}] Sala de Roteiro"
os.chdir(wrfolder)
fls2=["[{retranca}] PESQUISA", "[{retranca}] ROTEIROS", "[{retranca}] ATAS", "[{retranca}] TEXTOS PD", "[{retranca}] ARCOS"]
[os.mkdir(i) for i in fls2]

# finish up - show dirs and open explorer
os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))
path = os.listdir(os.getcwd())
subprocess.Popen(f'explorer {os.path.realpath(videos_dir + project)}')
p.wait()
else
print("Directory already exists, nothing to do")


if __name__ == "__main__":
    main()
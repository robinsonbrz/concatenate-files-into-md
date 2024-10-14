import os
import sys

def combinar_arquivos(pasta, saida):
    """Combina o conteúdo de arquivos de texto em um arquivo Markdown, 
       incluindo arquivos em subpastas, e formata o código Python.
    """
    with open(saida, "w") as outfile:
        for diretorio_atual, _, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if arquivo.endswith(".py"):
                    outfile.write(f"### {os.path.join(diretorio_atual, arquivo)}\n")
                    outfile.write("```python\n")
                    with open(os.path.join(diretorio_atual, arquivo), "r") as infile:
                        outfile.write(infile.read())
                    outfile.write("```\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python -m merge-into-md <nome_da_pasta> <nome_do_arquivo_de_saida.md>")
        sys.exit(1)  # Sai com código de erro

    pasta_origem = sys.argv[1]
    arquivo_saida = sys.argv[2]
    combinar_arquivos(pasta_origem, arquivo_saida)






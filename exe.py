import os
import sys
import ctypes
import subprocess
import time

def is_admin():
    """Verifica se o script está sendo executado como administrador"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """Reexecuta o script com privilégios de administrador"""
    script = os.path.abspath(sys.argv[0])
    subprocess.call(['powershell', '-Command',
                    f'Start-Process "{script}" -Verb runAs'])


def remover_galeria():
    print("\nRemovendo a Galeria do Explorador...")
    comando = r'reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{e88865ea-0e1c-4e20-9aa6-edcd0212c87c}" /f'
    os.system(comando)
    print("Galeria removida com sucesso.\n")
    time.sleep(2)


def restaurar_galeria():
    print("\nRestaurando a Galeria do Explorador...")
    comando = r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{e88865ea-0e1c-4e20-9aa6-edcd0212c87c}" /ve /d "Gallery" /f'
    os.system(comando)
    print("Galeria restaurada com sucesso.\n")
    time.sleep(2)


def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================")
        print("    GERENCIAR GALERIA - WIN11")
        print("===============================")
        print("\n[1] REMOVER Galeria do Explorador")
        print("[2] RESTAURAR Galeria do Explorador")
        print("[3] SAIR\n")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            remover_galeria()
        elif opcao == "2":
            restaurar_galeria()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    if not is_admin():
        print("Solicitando permissões de administrador...")
        run_as_admin()
        sys.exit()
    menu()
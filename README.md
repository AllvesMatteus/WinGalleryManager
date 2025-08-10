# WinGalleryManager

## Descrição

O **WinGalleryManager** é uma ferramenta desenvolvida em Python para facilitar o gerenciamento da Galeria do Explorador de Arquivos no Windows 11. Com ele, você pode remover ou restaurar a Galeria do Explorador de forma simples, rápida e segura, sem a necessidade de editar o registro manualmente.

## Diferenciais

- **Automação de tarefas administrativas**: O programa executa comandos no registro do Windows automaticamente, poupando tempo e evitando erros manuais.
- **Interface simples via terminal**: Menu intuitivo para qualquer usuário.
- **Integração total com o Windows**: Utiliza bibliotecas Python para interagir diretamente com recursos do sistema operacional.
- **Distribuição fácil**: Com o PyInstaller, você pode gerar um executável (.exe) para rodar em qualquer máquina Windows, sem precisar instalar o Python.
- **Solução inovadora**: Até o momento, o Windows 11 não oferece uma opção nativa para remover a Galeria do Explorador. Este método foi criado para suprir essa necessidade, diferente de outros métodos existentes que utilizam apenas arquivos `.bat`.

## Bibliotecas Utilizadas

- `ctypes` e `subprocess`: Para interação com permissões administrativas e execução de comandos do sistema.
- `os` e `sys`: Para manipulação de arquivos e argumentos do sistema.
- `time`: Para controle de tempo nas mensagens.
- **PyInstaller**: Para empacotar o programa em um executável Windows.

## Como funciona o `exe.py`

O arquivo `exe.py` (ou `WinGalleryManager/__init__.py` se estiver usando como pacote) contém toda a lógica do programa:

- Verifica se está sendo executado como administrador.
- Exibe um menu para o usuário escolher entre remover, restaurar a galeria ou sair.
- Executa comandos no registro do Windows para remover ou restaurar a Galeria do Explorador.
- Solicita permissões elevadas automaticamente, se necessário.

## Como gerar o executável com PyInstaller

1. **Instale as dependências** (se ainda não fez):

   ```sh
   pip install -r requirements.txt
   ```

2. **Gere o executável** usando o PyInstaller. Execute no terminal, na raiz do projeto:

   ```sh
   pyinstaller --onefile --windowed --icon=assets/remov.ico --name=WinGalleryManager WinGalleryManager/__init__.py
   ```

   - `--onefile`: Gera um único arquivo executável.
   - `--windowed`: Não abre terminal extra (opcional, pode remover se quiser ver o terminal).
   - `--icon=assets/remov.ico`: Define o ícone do executável.
   - `--name=WinGalleryManager`: Nome do executável gerado.

3. O executável estará disponível na pasta `dist/` com o nome `WinGalleryManager.exe`.

## Como usar

1. Execute o `WinGalleryManager.exe` como administrador.
2. Escolha a opção desejada no menu:
   - `[1]` Remover Galeria do Explorador
   - `[2]` Restaurar Galeria do Explorador
   - `[3]` Sair

Pronto! Seu Explorador de Arquivos será modificado conforme sua escolha.

## Download

Se preferir, basta baixar o arquivo **WinGalleryManager.exe** já pronto e usar normalmente, sem necessidade de instalar Python ou outras dependências.

Se você for programador e quiser criar o seu próprio gerenciador do seu jeito, o código é open source e pode ser modificado conforme suas necessidades.

---

# **Atenção:** Sempre faça backup do sistema antes de modificar o registro

Tool to remove or restore the Gallery from Windows 11 Explorer with a simple interface. (Ferramenta para remover ou restaurar a Galeria do Explorador do Windows 11 de forma simples.)

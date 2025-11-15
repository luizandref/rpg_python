"""
Módulo que implementa o sistema de logging do jogo.
Registra eventos importantes em um arquivo .log
"""

import os
from datetime import datetime


class Logger:
    """
    Classe responsável por registrar eventos do jogo em arquivo de log.
    """
    
    def __init__(self, arquivo_log="jogo.log"):
        """
        Inicializa o logger.
        
        Args:
            arquivo_log (str): Nome do arquivo de log
        """
        self.arquivo_log = arquivo_log
        self._criar_arquivo_se_nao_existir()
    
    def _criar_arquivo_se_nao_existir(self):
        """Cria o arquivo de log se ele não existir."""
        if not os.path.exists(self.arquivo_log):
            with open(self.arquivo_log, 'w', encoding='utf-8') as f:
                f.write(f"=== Log do Jogo RPG ===\n")
                f.write(f"Iniciado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
    
    def registrar(self, mensagem):
        """
        Registra uma mensagem no arquivo de log.
        
        Args:
            mensagem (str): Mensagem a ser registrada
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {mensagem}\n"
        
        try:
            with open(self.arquivo_log, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Erro ao escrever no log: {e}")
    
    def limpar_log(self):
        """Limpa o arquivo de log."""
        with open(self.arquivo_log, 'w', encoding='utf-8') as f:
            f.write(f"=== Log do Jogo RPG ===\n")
            f.write(f"Log limpo em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")


"""
Classe base que serve como modelo tanto para o personagem quanto para o inimigo.
Implementa atributos comuns como nome e HP.
"""


class Atributos:
    """Classe base com atributos comuns para personagens e inimigos."""
    
    def __init__(self, nome, hp, hp_maximo=None):
        """
        Inicializa um objeto com atributos básicos.
        
        Args:
            nome (str): Nome do personagem/inimigo
            hp (int): Pontos de vida atuais
            hp_maximo (int, optional): Pontos de vida máximos. Se None, usa hp como máximo.
        """
        self.nome = nome
        self.hp = hp
        self.hp_maximo = hp_maximo if hp_maximo is not None else hp
    
    def esta_vivo(self):
        """Verifica se o personagem/inimigo está vivo."""
        return self.hp > 0
    
    def receber_dano(self, dano):
        """
        Aplica dano ao personagem/inimigo.
        
        Args:
            dano (int): Quantidade de dano a ser aplicada
            
        Returns:
            int: Dano real aplicado (considerando HP não pode ser negativo)
        """
        dano_real = min(dano, self.hp)
        self.hp -= dano_real
        return dano_real
    
    def curar(self, quantidade):
        """
        Restaura pontos de vida.
        
        Args:
            quantidade (int): Quantidade de HP a ser restaurada
        """
        self.hp = min(self.hp + quantidade, self.hp_maximo)
    
    def get_barra_vida(self):
        """
        Retorna uma representação visual da barra de vida.
        
        Returns:
            str: Barra de vida usando caracteres #
        """
        if self.hp_maximo == 0:
            return ""
        
        porcentagem = self.hp / self.hp_maximo
        barras = int(porcentagem * 20)  # 20 caracteres de largura
        return "#" * barras + "-" * (20 - barras)

"""
Módulo que define as classes de inimigos do jogo.
"""

from models.base import Atributos
import random


class Inimigo(Atributos):
    """
    Classe base para inimigos do jogo.
    """
    
    def __init__(self, nome, hp, dano, xp_recompensa=50):
        """
        Inicializa um inimigo.
        
        Args:
            nome (str): Nome do inimigo
            hp (int): Pontos de vida
            dano (int): Dano base do inimigo
            xp_recompensa (int): Experiência concedida ao derrotar
        """
        super().__init__(nome, hp, hp)
        self.dano = dano
        self.xp_recompensa = xp_recompensa
        self.defesa = 2
    
    def atacar(self):
        """
        Realiza um ataque contra o jogador.
        
        Returns:
            int: Dano causado pelo ataque
        """
        # Dano varia entre 80% e 120% do dano base
        dano = int(self.dano * random.uniform(0.8, 1.2))
        return max(1, dano)
    
    def receber_dano_com_defesa(self, dano):
        """
        Recebe dano considerando a defesa.
        
        Args:
            dano (int): Dano bruto recebido
            
        Returns:
            int: Dano real aplicado após defesa
        """
        dano_real = max(1, dano - self.defesa)
        return self.receber_dano(dano_real)


class Goblin(Inimigo):
    """
    Inimigo fraco, comum no início do jogo.
    """
    
    def __init__(self):
        """Inicializa um Goblin."""
        super().__init__("Goblin", 14, 3, xp_recompensa=30)
        self.defesa = 1


class Lobo(Inimigo):
    """
    Inimigo de nível médio, mais rápido e agressivo.
    """
    
    def __init__(self):
        """Inicializa um Lobo."""
        super().__init__("Lobo", 25, 5, xp_recompensa=50)
        self.defesa = 2
    
    def atacar(self):
        """
        Sobrescreve atacar: lobos são mais rápidos e podem atacar duas vezes.
        
        Returns:
            int: Dano causado (com chance de ataque duplo)
        """
        dano_base = super().atacar()
        # 20% de chance de ataque duplo
        if random.random() < 0.2:
            return dano_base + super().atacar()
        return dano_base


class Orc(Inimigo):
    """
    Inimigo forte, com muita vida e defesa.
    """
    
    def __init__(self):
        """Inicializa um Orc."""
        super().__init__("Orc", 40, 7, xp_recompensa=80)
        self.defesa = 4


class Chefao(Inimigo):
    """
    Inimigo poderoso, com habilidades especiais.
    """
    
    def __init__(self):
        """Inicializa um Chefão."""
        super().__init__("Chefão", 80, 10, xp_recompensa=200)
        self.defesa = 6
        self.mana = 50
        self.mana_maxima = 50
    
    def atacar(self):
        """
        Sobrescreve atacar: chefões podem usar habilidades especiais.
        
        Returns:
            int: Dano causado pelo ataque
        """
        # 30% de chance de usar habilidade especial
        if random.random() < 0.3 and self.mana >= 20:
            self.mana -= 20
            return self.ataque_especial()
        return super().atacar()
    
    def ataque_especial(self):
        """
        Ataque especial do chefão: causa muito dano.
        
        Returns:
            int: Dano causado pelo ataque especial
        """
        # Ataque especial causa 200% a 250% do dano base
        dano = int(self.dano * random.uniform(2.0, 2.5))
        return max(1, dano)
    
    def regenerar(self):
        """
        Regenera um pouco de HP a cada turno (apenas chefões).
        """
        if random.random() < 0.2:  # 20% de chance
            self.curar(5)


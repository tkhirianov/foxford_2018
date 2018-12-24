def main():
    name = input("Введите имя игрока:")
    print("Когда игра будет написана, вы сможете поиграть,", name)


class BattleUnit:
    """
    Отвечает за здоровье и атаку.
    """
    def __init__(self, health, attack_force):
        self._health = health
        self._attack_force = attack_force

    def get_health(self):
        return self._health

    def cause_damage(self, other):
        """ Причинить урон другой боевой единице."""
        pass


class Hero(BattleUnit):
    """
    Должен отвечать на заданный вопрос.
    """
    def get_answer(self, question: str) -> str:
        pass


class Dragon(BattleUnit):
    """
    Должен:
      1) загадывать загадку и запоминать ответ,
      2) проверять корректность ответов.
    """
    def get_question(self):
        """ Генерирует новый вопрос и запоминает ответ."""
        pass

    def check_answer(self, answer: str) -> bool:
        """ Проверяет ответ на корректность. """
        pass


class Battle:
    """
    Проводит бой между игроком и драконом до полной победы одного из них.
    """
    def __init__(self, hero, dragon):
        pass

    def fight(self):
        """ Собственно, запускает битву."""
        pass

    def hero_won(self) -> bool:
        """ Правда, если бой выиграл герой."""


class GameRound:
    """ Контролирует один игровой раунд. """

    def __init__(self, hero):
        """ Генерирует список драконов (игровой уровень). """
        pass

    def play(self):
        """ Запускает игровой раунд
          1) Приветствует новый раунд.
          2) Последовательно запускает бои между героем и очередным драконом.
          3) Отображает результаты игрового раунда.
        """
        pass


main()

def main():
    name = input("Введите имя игрока:")
    hero = Hero(name)
    game_round = GameRound(hero)
    game_round.play()
    print("Вы набрали", hero.get_scores(), "очков.")


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
    default_initial_health = 100
    default_attack_force = 10

    def __init__(self, name: str):
        super().__init__(Hero.default_initial_health, Hero.default_attack_force)
        self._name = name
        self._scores = 0

    def get_answer(self, question: str) -> str:
        pass

    def get_name(self) -> str:
        return self._name

    def get_scores(self) -> int:
        return self._scores


class Dragon(BattleUnit):
    """
    Должен:
      1) загадывать загадку и запоминать ответ,
      2) проверять корректность ответов.
    """
    default_initial_health = 30
    default_attack_force = 5

    def __init__(self, color: str):
        super().__init__(Dragon.default_initial_health, Dragon.default_attack_force)
        self._color = color

    def get_question(self) -> str:
        """ Генерирует новый вопрос и запоминает ответ."""
        pass

    def check_answer(self, answer: str) -> bool:
        """ Проверяет ответ на корректность. """
        pass

    def get_color(self) -> str:
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


class GameRound:
    """ Контролирует один игровой раунд. """

    def __init__(self, hero):
        """ Генерирует список драконов (игровой уровень). """
        self._hero = hero
        self._enemy_list = [Dragon("зелёный")]

    def play(self):
        """ Запускает игровой раунд
          1) Приветствует новый раунд.
          2) Последовательно запускает бои между героем и очередным драконом.
          3) Отображает результаты игрового раунда.
        """
        print("Начало раунда!")
        print("Вам предстоит победить", len(self._enemy_list), "врагов!")

        while self._enemy_list and self._hero.get_health() > 0:
            dragon = self._enemy_list.pop(0)
            battle = Battle(self._hero, dragon)
            battle.fight()

        print("Конец раунда!")
        if self._hero.get_health() > 0:
            print("Вы победили! Поздравляем!")
        else:
            print("Вы проиграли... Ваш герой повержен!")


main()

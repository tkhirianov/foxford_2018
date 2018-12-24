from random import randint


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

    @staticmethod
    def get_answer(question: str) -> str:
        answer = input("Введите чему равно: " + question + "= ")
        return answer

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
        self._answer = None

    def get_question(self) -> str:
        """ Генерирует новый вопрос и запоминает ответ."""
        op1 = randint(1, 10)
        op2 = randint(1, 10)

        operation = randint(1, 3)
        if operation == 1:  # plus
            operation_sign = '+'
            answer = op1 + op2
        elif operation == 2:  # minus
            operation_sign = '-'
            answer = op1 - op2
        else:
            operation_sign = '*'
            answer = op1 * op2
        question = str(op1) + ' ' + operation_sign + ' ' + str(op2)

        self._answer = answer
        return question

    def check_answer(self, answer: str) -> bool:
        """ Проверяет ответ на корректность. """
        return answer == self._answer

    def get_color(self) -> str:
        return self._color


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
            self.fight(self._hero, dragon)

        print("Конец раунда!")
        if self._hero.get_health() > 0:
            print("Вы победили! Поздравляем!")
        else:
            print("Вы проиграли... Ваш герой повержен!")

    @staticmethod
    def fight(hero, dragon):
        """
        Проводит бой между игроком и драконом до полной победы одного из них.
        """
        while dragon.get_health() > 0 or hero.get_health() > 0:
            question = dragon.get_question()
            answer = hero.get_answer(question)
            if dragon.check_answer(answer):
                hero.cause_damage(dragon)
            else:
                dragon.cause_damage(hero)


main()

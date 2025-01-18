from __future__ import annotations


class Race:
    speed_list: dict[str, list[Runner]]

    def __init(self):
        self.speed_list = {'20': [], '30': [], '40': [], 'over 40': []}

    def __init__(self, runner_list: list[Runner]):
        for runner in runner_list:
            if runner.speed_category == '20':
                self.speed_list['20'].append(runner)

            elif runner.speed_category == '30':
                self.speed_list['30'].append(runner)

            elif runner.speed_category == '40':
                self.speed_list['40'].append(runner)

            else:
                self.speed_list['over 40'].append(runner)

class Runner:
    name: str
    email: str
    speed_category: int

    def __init__(self, name: str, email: str, speed_category: str):
        self.name = name
        self.email = email
        self.speed_category = speed_category


if __name__ == '__main__':
    r1 = Runner('Marc', 'marc.benedetti@gmail.com', '30')
    r2 = Runner('Romina', 'romina@gmail.com', '40')
    r3 = Runner('Micheal', 'micheal@gmail.com', 'over 40')
    r4 = Runner('Micheal', 'rodoshi.mondal@mail.utoronto.ca', 'over 40')
    r5 = Runner('')
    s1 = Race([r1, r2, r3, r4])
    print(s1.speed_list)

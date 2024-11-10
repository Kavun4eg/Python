class Romb:
    def __init__(self, сторона_а, кут_а):

        if сторона_а <= 0:
            raise ValueError("Сторона повинна бути більшою за 0")

        if not (0 < кут_а < 180):
            raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")

        setattr(self, 'сторона_а', сторона_а)
        setattr(self, 'кут_а', кут_а)

        кут_б = 180 - кут_а
        setattr(self, 'кут_б', кут_б)

ромб = Romb(5, 60)
print(ромб)
class Romb:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а
        self.кут_б = 180 - кут_а

    def __setattr__(self, name, value):
        if name == 'сторона_а':
            if value <= 0:
                raise ValueError("Сторона повинна бути більшою за 0")
            super().__setattr__(name, value)

        elif name == 'кут_а':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")
            super().__setattr__(name, value)

            self.кут_б = 180 - value

        elif name == 'кут_б':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")
            if 180 - value != self.кут_а:
                raise ValueError("Сума кутів повинна бути рівна 180 градусів")
            super().__setattr__(name, value)

    def __str__(self):
        return (
            f"Сторона: {self.сторона_а}\n"
            f"Кут 1 (кут_а): {self.кут_а}°\n"
            f"Кут 2 (кут_б): {self.кут_б}°"
        )
ромб = Romb(1, 179)
print(ромб)

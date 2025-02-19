class Cat:
    MEOW = 3

    def meow(self):
        MEOW = 4
        for _ in range(self.MEOW):
            print("Meow!")


angka = "anbiya"


cat = Cat()
cat.meow()



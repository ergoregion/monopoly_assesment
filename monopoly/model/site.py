class MonopolySite(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def sites():
    ids = [
        ('go', 575, 575),

        ('old kent road', 496, 575),
        ('community chest', 447, 575),
        ('whitechapple road', 398, 575),
        ('income tax', 349, 575),
        ('kings cross station', 300, 575),
        ('angel islington', 251, 575),
        ('chance', 202, 575),
        ('euston road', 153, 575),
        ('pentonville road', 104, 575),

        ('just visiting', 25, 575),

        ('pall mall', 25, 496),
        ('electric company', 25, 447),
        ('whitehall', 25, 398),
        ('nothumberland avenue', 25, 349),
        ('marlyborne station', 25, 300),
        ('bow street', 25, 251),
        ('comunity chest', 25, 202),
        ('malbrought street', 25, 153),
        ('vine street', 25, 104),

        ('free parking', 25, 25),

        ('strand', 104, 25),
        ('chance', 153, 25),
        ('fleet street', 202, 25),
        ('trafalgar square', 251, 25),
        ('fenchurch str station', 300, 25),
        ('leicer square', 349, 25),
        ('coventry street', 398, 25),
        ('water works', 447, 25),
        ('picadilly', 496, 25),

        ('go to jail', 575, 25),

        ('regent street', 575, 104),
        ('oxford street', 575, 153),
        ('comunity chest', 575, 202),
        ('bow street', 575, 251),
        ('liverpool street station', 575, 300),
        ('chance', 575, 349),
        ('park lane', 575, 398),
        ('super tax', 575, 447),
        ('mayfair', 575, 496),

        ('in jail', 60, 540),

    ]
    return [MonopolySite(i[0], i[1], i[2]) for i in ids]

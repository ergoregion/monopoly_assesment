
class MonopolySite(object):
    def __init__(self,name,x,y):
        self.name=name
        self.x = x
        self.y = y


def sites():
    ids = [
        ('go', 560 , 560),

        ('old kent road', 481, 560),
        ('community chest', 432, 560),
        ('whitechapple road', 383, 560),
        ('income tax', 334, 560),
        ('kings cross station',  285, 560),
        ('angel islington',  236, 560),
        ('chance',  187, 560),
        ('euston road', 138, 560),
        ('pentonville road', 89, 560),

        ('just visiting', 10, 560),

        ('pall mall', 10, 481),
        ('electric company', 10 ,432),
        ('whitehall', 10 ,383),
        ('nothumberland avenue', 10 ,334),
        ('marlyborne station', 10 ,285),
        ('bow street', 10 ,236),
        ('comunity chest', 10, 187),
        ('malbrought street', 10 ,138),
        ('vine street', 10 ,89),

        ('free parking', 10 ,10),

        ('strand', 89 ,10),
        ('chance', 138 ,10),
        ('fleet street', 187 ,10),
        ('trafalgar square', 236 ,10),
        ('fenchurch str station', 285 ,10),
        ('leicer square', 334 ,10),
        ('coventry street', 383 ,10),
        ('water works', 432 ,10),
        ('picadilly', 481 ,10),

        ('go to jail', 560, 10),

        ('regent street', 560,89),
        ('oxford street', 560,138),
        ('comunity chest', 560,187),
        ('bow street', 560,236),
        ('liverpool street station', 560,285),
        ('chance', 560,334),
        ('park lane', 560,383),
        ('super tax', 560,432),
        ('mayfair', 560,481),

        ('in jail', 45, 525),

    ]
    return [MonopolySite(i[0],i[1],i[2]) for i in ids]
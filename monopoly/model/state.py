class MonopolyState(object):
    def __init__(self, site: 'MonopolySite'):
        self.site: 'MonopolySite' = site

    def __repr__(self):
        return self.site.name


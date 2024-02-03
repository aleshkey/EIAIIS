class Word:
    normal_form = ''
    forms = []
    number = 0

    def __init__(self):
        self.normal_form = ''
        self.forms = []
        self.number = 0

    def __str__(self):
        return ("Normal form: "+self.normal_form+"\n"+
                "Number: "+str(self.number))


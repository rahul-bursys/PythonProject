class Student :

    def __init__(self,stand):
        self.stand =stand;
        print(self.stand)

    def test(self,user_input):
        if user_input == "3.17":
            return True;
        else:
            return False;
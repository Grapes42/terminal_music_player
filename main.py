class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        string += "-"*self.width
        
        for i in range(self.height-2):
            string += "\n|{}|".format(" "*(self.width-2))

        string += "\n"+"-"*self.width

        return string
    
box = Box(width=100, height=27)
print(box)

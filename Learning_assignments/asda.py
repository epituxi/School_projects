class BackPack:  
    def __init__(self):
        self.__items = ["asd","dasd"]
    
    def add_item(self, item):
        self.__items.append(item)
    
    def get_items(self):
        return self.__items

class Item:
    def __init__(self, item, item_des):
        self.item = item
        self.des = None
        self.item_des = item_des

    def get_item(self):
        return self.item

    def get_des(self):
        return self.item_des

    def set_des(self, item_des):
        self.item_des = item_des
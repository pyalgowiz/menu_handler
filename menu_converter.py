"""
    simple code for converting dict to a Linked List
    I made this sample for telegram bot programming,
    you can custom it for your purposes
"""
class Node:
    def __init__(self, addr, title, text, prev=0):
        """ 
            create Node with custom details
        """
        self.address = addr
        self.title = title
        self.text = text
        self.icons = []
        self.prev = prev

    def add_icon(self, icon:int):
        if icon not in self.icons:
            self.icons.append(icon)

class Menu:
    def __init__(self, menu:dict) -> None:
        """
            crawl the dict and give Node menu
        """
        self.adr=0
        self.converted_menu={}
        self.menu=menu

    def dict_generator(self, indict, parnet_cell:Node=None):
        self.adr+=1
        prev = parnet_cell.address if parnet_cell else 0
        cell = Node(self.adr, indict['title'], indict['text'], prev)
        if isinstance(indict, dict):
            for key, value in indict.items():
                parnet_cell.add_icon(self.adr) if parnet_cell != None else ''
                if isinstance(value, dict):
                    for d in self.dict_generator(value, cell):
                        yield d
                elif isinstance(value, list) or isinstance(value, tuple):
                    for v in value:
                        for d in self.dict_generator(v, cell):
                            yield d
                else:
                    yield self.adr
        else:
            yield self.adr
        self.converted_menu[cell.address] = cell

    def convert(self):
        for x in self.dict_generator(self.menu):
            pass
        return self.converted_menu

    def get_converted(self):
        return self.converted_menu

sample_menu = { # change this part 
  "title":"title 1",
  "text":"text 1",
  "icons":[
    {
        "title":"title 2",
        "text":"text 2",
        "icons":[
            {
                "title":"title 3",
                "text":"text 3",
            },
            {
                "title":"title 4",
                "text":"text 4",
            },
        ]
    },
    {
        "title":"title 5",
        "text":"text 5",
    },
    {
      "title":"title 6",
      "text":"text 6"
    }
  ]
}

menu_list = Menu(sample_menu)
output = menu_list.convert()
print(menu_list.convert())

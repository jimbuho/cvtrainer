from pathlib import Path
from os.path import exists
import json

class JSONManager:

    def __init__(self):
        self.information = None
        self.filepath = 'userinfo.json'

    def get_info(self):
        """ 
        {
            users:[
                {id:1, nombre:diego}
            ]
        }
        """
        if not self.information:
            if exists(self.filepath):
                with open(self.filepath, 'r') as fp:
                    self.information = json.load(fp)
            else:
                myfile = Path(self.filepath)
                myfile.touch(exist_ok=True)
                self.information = {'users':[]}    

    def add_user(self, id, name):
        self.get_info()

        if self.get_user(id) == None:
            self.information["users"].append({
                "name": name,
                "id": id,
            })

            with open(self.filepath, 'w') as fp:
                json.dump(self.information, fp, indent=2)
            
            return True
        else:
            return False

    def get_user(self, id):
        self.get_info()
        
        for item in self.information['users']:
            if int(item['id']) == int(id):
                return item['name']

        return None

"""
manager = JSONManager()
print(manager.add_user(1, 'diego'))
print(manager.add_user(2, 'silvia'))
print(manager.get_user(2))
"""
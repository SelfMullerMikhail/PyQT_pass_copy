from functions.db_Helper import Db_helper



class ActiveTable():
    def get_active(self):
        return self.activeTab

    def __init__(self):
        self.helper = Db_helper("Alpha.db")
        self.activeUser = "0"
        tab_count = self.helper.get_list("SELECT COUNT(id) FROM Tables")[0][0]
        if tab_count == 0:
            self.helper.insert(f"""INSERT INTO Tables (id_client, tables_name)
                            VALUES ({1}, 'tab')""")
        self.activeTab = self.helper.get_list("SELECT MIN(id) FROM Tables")[0][0]
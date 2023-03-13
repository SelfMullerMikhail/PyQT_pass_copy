from functions.db_Helper import Db_helper



class ActiveTable():
    """Class of save and change activite table"""
    def __init__(self) -> None:
        self.helper: Db_helper = Db_helper("Alpha.db")
        self.activeUser: int = "0"
        tab_count: int = self.helper.get_list("SELECT COUNT(id) FROM Tables")[0][0]
        if tab_count == 0:
            self.helper.insert(f"""INSERT INTO Tables (id_client, tables_name)
                            VALUES ({1}, 'tab')""")
        self.activeTab: int= self.helper.get_list(f"""SELECT MIN(id) 
                                                FROM Tables""")[0][0]
        
    def createFirstMinTable(self, id_client: int) -> None:
        """Create first table"""
        self.activeTab = self.helper.get_list(f"""SELECT MIN(id) 
                                                FROM Tables 
                                                WHERE id_client = {id_client}""")[0][0]
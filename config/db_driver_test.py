from config import db_driver

class Test_Db_driver_Save_polls:
    def test_save_polls_1(self):
        db_driver.save_polls(None)


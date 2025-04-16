import pandas as pd
from pathlib import Path


class Read_excel:

    @staticmethod
    def get_user_role_authentication_data_df():
        try:
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_Excel\\Users_and_authentications_xlsx.xlsx"
            df_1 = pd.read_excel(file_path, sheet_name='User_Roles_Auth_Data_1')
            df_2 = pd.read_excel(file_path, sheet_name='User_Roles_Auth_Data_2')
            return df_1, df_2
        except Exception as ex:
            print(ex)

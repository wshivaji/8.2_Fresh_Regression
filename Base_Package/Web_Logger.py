from pathlib import Path
from datetime import datetime
import logging
import os


class web_logger:
    _logger_obj = None

    @classmethod
    def logger_obj(cls):
        if cls._logger_obj is None:
            print("creating new object")
            cls._logger_obj = cls.logger_init()
            print(cls._logger_obj)
        return cls._logger_obj

    @staticmethod
    def logger_init():
        try:
            log_folder = f"{Path(__file__).parent.parent}\\Application_Logs"
            print(log_folder)
            files_list = os.listdir(log_folder)
            print(files_list)
            list_size = len(files_list)
            print("file List : ", files_list, " file count: ", list_size)
            i = 0
            base_path = Path(log_folder)
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            # print(files_in_base_path)

            for file in files_list[:-4]:
                for file_name in files_in_base_path:
                    if file_name.name == file:
                        os.remove(file_name)

            now = datetime.now()
            # print("now =", now)
            dt = now.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = f"{Path(__file__).parent.parent}\\Application_Logs\\Application_logs_{dt}.log"
            # print("Log_file_name: ", file_name)
            formatter = logging.Formatter("%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s", datefmt='%d/%m/%Y %r')
            handler = logging.FileHandler(filename=file_name)
            handler.setFormatter(formatter)
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
            return logger
        except Exception as ex:
            print(ex.args)

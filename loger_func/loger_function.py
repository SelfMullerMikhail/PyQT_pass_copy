import datetime
import os


class Logger():
    def __init__(self) -> None:
        pass

    # @abstractmethod
    def write(info: str):
        data = str(os.getcwd()) + "\\loger\\" + str(datetime.date.today())
        """Write info in log.txt"""
        with open(f"{data}.txt", "a") as file:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(f"\n{time} {info}")
            file.close()


from lightcast_smart_dataset.lightcast_client.uk_dataset import UK
from lightcast_smart_dataset.lightcast_client.global_dataset import Global
from lightcast_smart_dataset.lightcast_client.taxonomy import Taxonomy


class LightcastSmartDataset():

    def __init__(self, username: str, password: str) -> None:
        super(LightcastSmartDataset, self).__init__()
        self.__setUsername(username)
        self.__setPassword(password)

    def __setUsername(self, username: str) -> None:
        if not isinstance(username, str):
            raise TypeError("username is not an instance of str.")

        self.__username = username

    def __setPassword(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("password is not an instance of str.")

        self.__password = password

    def ukDataset(self) -> UK:
        return UK(self.__username, self.__password)

    def globalDataset(self) -> Global:
        return Global(self.__username, self.__password)

    def taxonomy(self) -> Taxonomy:
        return Taxonomy(self.__username, self.__password)

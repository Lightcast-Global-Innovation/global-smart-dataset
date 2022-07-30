from client.client import LightcastSmartDataset

USERNAME = "*****"
PSWD = "****"
occupation = "Programmers and software development professionals"
area = "Camden and City of London"

LightcastSmartDataset().ukDataset().getSocOccupationInsight(
    "Programmers and software development professionals",
    "Camden and City of London"
)

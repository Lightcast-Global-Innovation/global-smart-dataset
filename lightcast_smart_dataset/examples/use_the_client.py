from lightcast_smart_dataset.lightcast_client.client import LightcastSmartDataset

USERNAME = "xxxx"
PSWD = "xxxx"
occupation = "Programmers and software development professionals"
area = "Camden and City of London"

# Get Soc (level 4) Occupations - UK
r = LightcastSmartDataset(USERNAME, PSWD).ukDataset().getSocOccupationInsight(
    occupation="Programmers and software development professionals",
    area="Camden and City of London"
)

occupation = "Business Development / Sales Manager"
area = "Milan (ITA)"

# Get Global Data
LightcastSmartDataset(USERNAME, PSWD).globalDataset().getOccupationInsight(
    occupation=occupation,
    area=area
)

# Get Taxonomy
LightcastSmartDataset(USERNAME, PSWD).taxonomy().getUkNuts3()

# Get Taxonomy
LightcastSmartDataset(USERNAME, PSWD).taxonomy().getOccupation()

# Get Taxonomy
LightcastSmartDataset(USERNAME, PSWD).taxonomy().getGlobalMarket()

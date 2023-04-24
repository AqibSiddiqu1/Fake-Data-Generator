from faker import Faker

import pandas as pd

fake = Faker()

data = [fake.profile() for i in range(500)]

data = pd.DataFrame(data)

print(data)
# The code runs when executed successfuly when the docker container is started

print("Container Running")

from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame(
    {'name': ['Person 1', 'Person 2', 'Person 3'], 'age': ['20', '24', '32']})
engine = create_engine(
    'postgresql://postgres:123@localhost:5432/postgres')

try:
    df.to_sql('people', engine, if_exists='replace')
    print("success")
except:
    print("unsuccesfull")
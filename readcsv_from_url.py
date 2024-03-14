import pandas as pd

list = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")

print(list)
# https://www.football-data.co.uk/data.php

list.rename(columns={"FTHG":"home_goals",
                    "FTAG":"away_goals"}, inplace=True)
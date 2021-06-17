import pandas as pd


watch_list = [
        {
            "name": "happy",
            "ott": "netflix"
        }
    ]

DF = pd.DataFrame(watch_list)
  
# save the dataframe as a csv file
DF.to_csv("data1.csv")
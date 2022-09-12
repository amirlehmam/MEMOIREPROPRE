import pandas as pd 

url_m = "https://raw.githubusercontent.com/amirlehmam/streamlit/main/fluchart.csv?token=GHSAT0AAAAAABW53GHT2N4KNKFZJKAKMRPOYY7QYZQ"
m = pd.read_csv(url_m)
print(m)
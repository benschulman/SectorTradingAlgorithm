import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

etf_path = "VanguardSectorETFs"
starting_investment = 1000
dict_of_dfs = {}
daily_returns = []

def load_data():
    for file in os.listdir(etf_path):
        df = pd.read_csv(os.path.join(etf_path,file))
        etf_name = file.split(".")[0]
        dict_of_dfs[etf_name] = df

def main():
    if not os.path.isdir(etf_path):
        exit()
    
    load_data()

    # alg: at day n determine etf with best return on prev day,
    #      at day n + 1 short that etf on market open and close the position on market close

    



  
    

        
        
            

if __name__ == "__main__":
    main()
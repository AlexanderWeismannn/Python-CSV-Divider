
import pandas as pd
import numpy as np


def main():
    # read in the csv file and decide how many "chunks" to split it into
    df = pd.read_csv("")
    df_list = np.array_split(df,2)

    # turn each "chunk" into its own unique numbered csv file
    count = 0
    for split in df_list:
        split.to_csv(f"split_{count}.csv")
        count+=1


if __name__ == '__main__':
    main()
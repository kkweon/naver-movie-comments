import os
import pandas as pd
import datetime as dt
import sqlite3

def list(current_path):
    file_path_list = []
    for dp, dn, fn in os.walk(current_path):
        for file in fn:
            if ".tsv" in file:
                file_path = os.path.join(dp, file)
                file_path_list.append(file_path)

    return file_path_list

def main(DB_NAME="data.db"):
    file_path_list = list(".")
    whole_df = pd.DataFrame(columns=['rating', 'comment', 'id', 'movie'])
    tic = dt.datetime.now()
    for idx, i in enumerate(file_path_list):
        if idx % 1000 == 0:
            print("reading: {}".format(i))
        df = read_file(i)
        whole_df = whole_df.append(df, ignore_index=True)
    toc = dt.datetime.now()
    conn = sqlite3.connect(DB_NAME)
    whole_df.to_sql("comments", conn)
    print("Time elapsed: {}".format(toc-tic))
    print("File counts: {}".format(len(file_path_list)))



def read_file(file_path):
    df = pd.read_csv(file_path, delimiter='\t', names=['rating', 'comment', 'id', 'movie'], skiprows=1)
    df['movie'] = file_path.split("/")[-1].split(".tsv")[0]
    return df


if __name__ == '__main__':
    main()

import numpy as np
import pandas as pd


def main():
    df = pd.read_csv("input", sep=" ", names=['N', 'L', 'PW'])
    #thx: https://stackoverflow.com/questions/45647199/how-to-split-strings-inside-a-numpy-array
    df['L'] = df['L'].str.split(':').str[0]
    df['NL'] = df['N'].str.split('-').str[0].astype(int)
    df['NU'] = df['N'].str.split('-').str[1].astype(int)
    
    df['OCC'] = [j.count(i) for i,j in zip(df['L'], df['PW'])]
    mask = (df['OCC'] >= df['NL']) & (df['OCC'] <= df['NU'])
    print(mask, mask.sum())


    mask = np.array([((pw[n-1]==l) ^ (pw[m-1]==l)) for pw, n, m, l in zip(df['PW'], df['NU'], df['NL'], df['L'])])
    print(mask, mask.sum())
    print(df)

if __name__ == '__main__':
    main()

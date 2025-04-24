from european import get_bs_call, get_bs_put
from scipy.optimize import brentq

def get_imvol_call(S, K, T, r, q, market_price):
    func = lambda sigma: get_bs_put(S, K, T, r, q, sigma) - market_price


    result = pd.DataFrame(index=self.df.index, columns=[f'iv_{market_col}'])
    for idx, row in self.df.iterrows():
        market_price = row[market_col]
        S, K, T, r, q = row['S'], row['K'], row['T'], row['r'], row['q']

        try:
            iv = brentq(func, 1e-8, 5.0, maxiter=1000)
            result.loc[idx, f'iv_{market_col}'] = iv
        except Exception as e:
            print(f'brentq has failed for idx {idx}: {e}')
    return result
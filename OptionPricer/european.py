import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import brentq

def get_bs_call(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def get_bs_put(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)

def get_imvol_call(S, K, T, r, q, market_price):
    price_lower_bound = get_bs_call(S, K, T, r, q, 1e-8)
    if market_price < price_lower_bound:
        return np.nan
    try:
        return brentq(lambda sigma: get_bs_call(S, K, T, r, q, sigma) - market_price, 1e-8, 5.0)
    except Exception:
        return np.nan

def get_imvol_put(S, K, T, r, q, market_price):
    price_lower_bound = get_bs_put(S, K, T, r, q, 1e-8)
    if market_price < price_lower_bound:
        return np.nan
    try:
        return brentq(lambda sigma: get_bs_put(S, K, T, r, q, sigma) - market_price, 1e-8, 5.0)
    except Exception:
        return np.nan

class BlackScholes:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def d1(self, sigma_col: str):
        return (np.log(self.df['S'] / self.df['K']) + (self.df['r'] - self.df['q'] + 0.5 * self.df[sigma_col] ** 2) *
                self.df['T']) / (
                self.df[sigma_col] * np.sqrt(self.df['T']))

    def d2(self, sigma_col: str):
        return self.d1(sigma_col) - self.df[sigma_col] * np.sqrt(self.df['T'])

    def bs_call(self, sigma_col: str):
        d1_vals = self.d1(sigma_col)
        d2_vals = self.d2(sigma_col)
        return self.df['S'] * np.exp(-self.df['q'] * self.df['T']) * norm.cdf(d1_vals) - self.df['K'] * np.exp(
            -self.df['r'] * self.df['T']) * norm.cdf(d2_vals)

    def bs_put(self, sigma_col: str):
        d1_vals = self.d1(sigma_col)
        d2_vals = self.d2(sigma_col)
        return self.df['K'] * np.exp(-self.df['r'] * self.df['T']) * norm.cdf(-d2_vals) - self.df['S'] * np.exp(
            -self.df['q'] * self.df['T']) * norm.cdf(-d1_vals)

    def find_imvol_call(self, market_col):
        result = [np.nan] * self.df.shape[0]
        for idx, row in self.df.iterrows():
            market_price = row[market_col]
            S, K, T, r, q = row['S'], row['K'], row['T'], row['r'], row['q']
            price_lower_bound = get_bs_call(S, K, T, r, q, 1e-8)
            if market_price < price_lower_bound:
                result[idx] = np.nan
                continue
            func = lambda sigma: get_bs_call(S, K, T, r, q, sigma) - market_price
            try:
                iv = brentq(func, 1e-8, 5.0, maxiter=1000)
                result[idx] = iv
            except Exception as e:
                print(f'brentq has failed for idx {idx}: {e}')
        return result

    def find_imvol_put(self, market_col):
        result = [np.nan] * self.df.shape[0]
        for idx, row in self.df.iterrows():
            market_price = row[market_col]
            S, K, T, r, q = row['S'], row['K'], row['T'], row['r'], row['q']
            price_lower_bound = get_bs_put(S, K, T, r, q, 1e-8)
            if market_price < price_lower_bound:
                result[idx] = np.nan
                continue
            func = lambda sigma: get_bs_put(S, K, T, r, q, sigma) - market_price
            try:
                iv = brentq(func, 1e-8, 5.0, maxiter=1000)
                result[idx] = iv
            except Exception as e:
                print(f'brentq has failed for idx {idx}: {e}')
        return result

    def delta(self, price_col):
        # TODO
        pass

    def gamma(self, price_col):
        # TODO
        pass

    def vega(self, price_col):
        # TODO
        pass

    def theta(self, price_col):
        # TODO
        pass

    def rho(self, price_col):
        # TODO
        pass

if __name__ == "__main__":
    call_df = pd.read_csv('../data/cleaned_data/Bloomberg/spx_call_051625_1634.csv')
    bs = BlackScholes(call_df)
    print(bs.find_imvol_call('mid'))
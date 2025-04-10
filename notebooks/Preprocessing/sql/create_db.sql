-- initialize database
DROP DATABASE IF EXISTS RRT;
CREATE DATABASE RRT;
-- create atm table
DROP TABLE IF EXISTS atm_info;
CREATE TABLE atm_info (
    dt         DATE NOT NULL, -- reference date
    ticker     TEXT NOT NULL, -- option ticker
    S          NUMERIC, -- lastly traded underlying price
    K          NUMERIC, -- strike price
    T          NUMERIC, -- time to maturity
    r          NUMERIC, -- interest rate applied
    iv         NUMERIC, -- implied volatility
    d          NUMERIC, -- dividend yield
    bid        NUMERIC, -- best bid
    ask        NUMERIC, -- best ask
    mid        NUMERIC, -- mid price
    last_price NUMERIC, -- lastly traded price
    volume     NUMERIC, -- traded volume
    hv30       NUMERIC, -- historical volatility spanning 30 days
    hv60       NUMERIC, -- historical volatility spanning 60 days
    hv90       NUMERIC, -- historical volatility spanning 90 days
    cp_flag    CHAR(1) CHECK (cp_flag IN ('C', 'P')), -- C: call, P: put
    PRIMARY KEY (dt, ticker)
);

DROP TABLE IF EXISTS spx;
CREATE TABLE spx (
    dt         DATE NOT NULL, -- reference date
    ticker     TEXT NOT NULL, -- option ticker
    K          NUMERIC NOT NULL, -- strike price
    S          NUMERIC, -- lastly traded underlying price
    M          NUMERIC, -- Moneyness
    T          NUMERIC, -- time to maturity
    r          NUMERIC, -- interest rate applied
    iv         NUMERIC, -- implied volatility
    d          NUMERIC, -- dividend yield
    bid        NUMERIC, -- best bid
    ask        NUMERIC, -- best ask
    mid        NUMERIC, -- mid price
    last_price NUMERIC, -- lastly traded price
    volume     INT, -- traded volume
    open_int   INT, -- open interest
    option_type TEXT, -- option type, European, American, Bermudan,
    thy_iv     NUMERIC, -- theoretical implied volatility
    thy_price  NUMERIC, -- theoretical price
    PRIMARY KEY (dt, ticker, )
)

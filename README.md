# 

This repository contains theoretical derivation and implementation of the Ross Recovery Theorem.

Issue 1. Data preprocessing and DB construction
Issue 2. Estimate implied volatiltiy in DITM and DOTM

Good question. Here's why:

- In **regular Markdown** (like GitHub, Jupyter, Obsidian), when you want to show **inline math**, you wrap it in **single dollar signs** `$...$`.  
- For **display math** (centered, block equations), you wrap it in **double dollar signs** `$$...$$`.

---

When you asked for "**correct this in a right form**",  
I thought you wanted something **fully clean and ready for publication**, meaning **using `\[` `\]` for block equations** — that's **LaTeX standard** (used in professional papers, PDFs, Overleaf).

In Markdown **you absolutely can** and often **should** use `$...$` and `$$...$$` because:

- `$...$` → inline math  
- `$$...$$` → display/block math

---

If you want it **in strict Markdown** style with `$`, here’s your same content **rewritten correctly using $ and $$**:

---

---

✅ This is the true **Markdown + Math** style using **dollar signs**.

---

Would you also like me to show you how this would look if we added **`\text{}`** inside math (to make subscripts, variables, and explanations even cleaner)?  
It looks very professional when you do that. Want me to show?


---

## Notations
- \( K \): Strike price  
- \( S \): Stock price  
- \( T \): Maturity, \( \tau = T - t \): Time to maturity (in years, i.e., days/365)  
- \( r \): Constant risk-free interest rate; \( r_t \): Deterministic (time-varying) rate  
- \( \sigma \): Constant annualized volatility (standard deviation) of the underlying asset; \( \sigma_t \): Deterministic volatility  
- \( \mathbb{P}^{\tilde{}} \): Risk-neutral measure; \( \mathbb{P} \): Physical (real-world) measure  
- \( p^{\tilde{}}(t, x; T, y) \): Transition density under \( \mathbb{P}^{\tilde{}} \); \( p(t, x; T, y) \): Transition density under \( \mathbb{P} \)

---

# Project: Dynamic Leveraging Strategy using Ross Recovery Theorem

## 1. Risk-Neutral Density (RND)

### Basic Math

Assume the Black-Scholes framework and spot price \( S_0 \). Then:

1. **Call Price:**
   \[
   C(K) = e^{-(r - q)\tau} \, \mathbb{E}^{\tilde{}} \left[ (S_T - K)_+ \mid \mathcal{F}_t \right] = e^{-(r - q)\tau} \int_{-\infty}^{\infty} (y - K)_+ \, p^{\tilde{}}(t, S_0; T, y) \, dy
   \]

2. **First Derivative w.r.t. Strike:**
   \[
   \frac{\partial}{\partial K} C(K) = -e^{-(r - q)\tau} \, \mathbb{E}^{\tilde{}} \left[ \mathbb{I}_{\{ S_T > K \}} \mid \mathcal{F}_t \right] = -e^{-(r - q)\tau} \int_K^{\infty} p^{\tilde{}}(t, S_0; T, y) \, dy = -e^{-(r - q)\tau} \, \mathbb{P}^{\tilde{}}(S_T > K)
   \]

3. **Second Derivative (Breeden-Litzenberger):**
   \[
   \frac{\partial^2}{\partial K^2} C(K) = e^{-(r - q)\tau} \, p^{\tilde{}}(t, S_0; T, K)
   \]
   In short, the risk-neutral density at strike \( K \) is:
   \[
   p^{\tilde{}}(T, K) = e^{(r - q)\tau} \, \frac{\partial^2}{\partial K^2} C(K)
   \]

---

If you'd like, I can also export this in `.md` format or generate a `.pdf` version with LaTeX styling.


Notations
- $K$: strike price
- $S$: stock price
- $T$: maturity, $\tau=T-t$: time to maturity (days/365)
- $r$: constant risk-free interest rate, $r_t$: deterministic
- $\sigma$: constant annualized volatility (std) of underlying asset, $\sigma_t$: deterministic
- $\doubleP\tilde$: risk-neutral measure, $\doubleP$: physical measure
- $p\tilde(t, x; T, y)$: transition density under $\doubleP\tilde$, $p(t, x; T, y)$: transition density under $\doubleP$

# Project: Dynamic leveraging strategy using Ross Recovery Theorem

## 1. Risk-Neutral Density (RND)

### Basic Math
Given the Black-Scholes framework and S0,
1. $Call(K) = e^(-(r-q)\tau) \doubleE[(S0-K)_{+}|\scriptF_t] = e^(-(r-q)\tau)\integral_-\infty_+\infty (y-K)_{+} p\tilde (t, S0; T, y)dy $, $p\tilde$ is a transition density  
2. $\partial_K Call(K) = -e^(-(r-q)\tau) \doubleE[\doubleI_{S0>K}|\scriptF_t]=-e^(-(r-q)\tau)\integral_-\infty_+\infty \doubleI_{y>K}p\tilde (t, S0; T, y)dy=-e^(-(r-q)\tau)\dobuleP\tilde(S0>K)$
3. $\partial^2/\partial K^2 Call(K) = e^(-(r-q)\tau)\integral_-\infty_+\infty p\tilde (t, S0; T, y)\delta_K(dy)=-e^(-(r-q)\tau)p\tilde(t, S0; T, K)=p\tilde(T, K)$ in short

If I directly ca


## 2. Pricing Kernel


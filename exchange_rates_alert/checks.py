from .config import CHF_EUR_THRESHOLD, CHF_USD_THRESHOLD

def check_rates(rates):

  chf_eur = float(rates['CHF']) / 1
  chf_usd = float(rates['CHF']) / float(rates['USD'])

  print(f"CHF/EUR: {chf_eur:.4f}")
  print(f"CHF/USD: {chf_usd:.4f}")

  return chf_eur < CHF_EUR_THRESHOLD, chf_usd < CHF_USD_THRESHOLD

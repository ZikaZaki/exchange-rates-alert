from .config import *
from .rates import get_rates
from .checks import check_rates
from .send_email import send_alert

def main():

  rates = get_rates()

  below_eur_threshold, below_usd_threshold = check_rates(rates)

  if (not below_eur_threshold):
    send_alert(
      subject="CHF/EUR Alert",
      body="CHF/EUR rate below threshold",
      to="za@lightupnet.de"
    )
  if below_usd_threshold:
    send_alert(
      subject="CHF/USD Alert",
      body="CHF/USD rate below threshold",
      to="za@lightupnet.de"
    )

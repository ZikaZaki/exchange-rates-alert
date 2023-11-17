import smtplib
from exchange_rates_alert.config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, PASSWORD

def send_alert(subject, body, to):

  context = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
  try:
    context.starttls()
    context.login(SENDER_EMAIL, PASSWORD)
    context.sendmail(SENDER_EMAIL, to, body)
  except Exception as e:
    print(f"Error: {e}")
  finally:
    context.quit()

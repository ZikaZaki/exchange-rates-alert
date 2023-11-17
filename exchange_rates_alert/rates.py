import requests
import csv
import zipfile
from io import BytesIO
from .config import ECB_API

def get_rates():

  r = requests.get(ECB_API)
  z = zipfile.ZipFile(BytesIO(r.content))
  csv_data = z.read('eurofxref.csv').decode('utf-8')

  reader = csv.reader(csv_data.splitlines())

  currencies = next(reader)

  rates = {}

  for row in reader:

    date = row[0].strip()

    for i, rate in enumerate(row[:]):
      currency = currencies[i].strip()
      rates[currency] = rate

  return rates
  
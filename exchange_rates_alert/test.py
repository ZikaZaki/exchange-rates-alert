import unittest
from unittest.mock import patch
from send_email import send_alert

def test_email_creation():

  msg = send_alert("Test Subject", "Test body", "za@lightupnet.de")

  # Assertions
  assert msg['Subject'] == "Test Subject"
  assert msg['To'] == "za@lightupnet.de"
  assert msg.get_content() == "Test body"

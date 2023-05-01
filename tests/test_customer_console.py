"""
Expected output:
    4 passed in 0.xx seconds
References:
    * https://realpython.com/python-testing/
    * http://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
from customer_console_assignment_14 import CustomerConsole


def test_read_pin_valid_input(monkeypatch):
    monkeypatch.setattr('getpass.getpass', lambda _: '1234')
    console = CustomerConsole()
    assert console.read_pin() == 1234


def test_read_amount_valid_input():
    console = CustomerConsole()
    input_values = ['50.57']

    def input(prompt=None):
        return input_values.pop(0)

    console.input = input
    assert console.read_amount() == 50.57


def test_display(capsys):
    console = CustomerConsole()
    statement = "Please select a choice."
    console.display(statement)
    captured = capsys.readouterr()
    assert "Please select a choice." in captured.out


def test_read_menu_choices():
    console = CustomerConsole()
    input_values = ['1']

    def input(prompt=None):
        return input_values.pop(0)

    console.input = input
    assert console.read_menu_choices() == 1

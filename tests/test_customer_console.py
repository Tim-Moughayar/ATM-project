import pytest
from source_code.customer_console import CustomerConsole


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
    options = ['Account Balance', 'Withdraw', 'Deposit']
    prompt = 'Please select an option'
    console.input = input
    assert console.read_menu_choices(prompt, options) == 1

'''Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance.Include methods to
deposit money, withdraw money,and display the account balance.Ensure that the account balance
cannot be accessed directly from outside the class.Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:

  def__init__(self,account_number, account_holder_name, initial_balance=0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance
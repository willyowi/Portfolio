#!/usr/bin/env python3.6
from password import User
from credentials import Credentials

def create_user(id_num,usr_name,pword):
    '''
    function to create a new user
    '''
    new_user = User(id_num,usr_name,pword)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user()

def find_user(id_number):
    '''
    function to find a user
    '''
    return User.find_user(id_number)

def check_existing_user(id_number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(id_number)

def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def authenticate_user(usr_name,pword):
    '''
    function that checks whether a user is a valid user
    '''
    return User.auth_user(usr_name,pword)

def create_account(acc,username,password):
    '''
    function to create a new account
    '''
    new_account = Credentials(acc,username,password)
    return new_account

def save_account(credentials):
    '''
    function to save new account
    '''
    credentials.save_acc()

def delete_acc(credentials):
    '''
    function to delete accounts
    '''
    credentials.delete_acc()
def check_existing_account(account):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credential_exists(account)

def find_account(account):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_acc(account)

def display_account():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_acc()

def display_password():
    '''
    Function that returns generated password
    '''
    return Credentials.pass_gen()

def main():
    print("Hello Welcome to your password locker. Proceed to create an account")
    print('Input a Username of your choice')
    usr_name = input()
    print('Input a password of your choice')
    pword = input()
    print('Input a random number as your account identifier')
    id_num = input()
    save_user(create_user(id_num,usr_name,pword))
    print('\n')

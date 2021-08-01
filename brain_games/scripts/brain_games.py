#!/usr/bin/env python

def welcome_user():
    import prompt
    name = prompt.string('May i have your name?')

def main():
    print("Welcome to the Brain Games!") 
    welcome_user()

if __name__=='__main__':
    main()

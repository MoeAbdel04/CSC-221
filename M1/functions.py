# M1Lab_Debug.py

from quiz_module import menu, start_program

def main():
    choice = 0

    while choice != 2:
        menu()
        choice = int(input('Enter your choice: '))

        if choice == 1:
            start_program()
        elif choice == 2:
            print('\nTerminate Program....')
        else:
            print('INVALID Entry!!!!')
            print('Enter a valid choice')

if __name__ == "__main__":
    main()

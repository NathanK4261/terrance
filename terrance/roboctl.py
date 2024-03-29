# Terminal gui to streamline configuring robot
# NOTE: Do not run on roboRio, for python configuration only
import json, subprocess, platform, os, time

def clear():
    try:
        os.system('cls') # For windows command prompt users
    except:
        subprocess.call('clear', shell=True) # For Mac/Linux users

def main_menu():
    while True:
        clear()
        print('''robothelper 2024
Make sure to run this program in cmd.exe

SELECT AN OPTION:
    [0] - Setup robotpy environment
    [1] - Remote shell into robot (still in development)
    [2] - Test robot code
    [3] - Deploy robot code
              
    ("q" to quit)
''')
        choice = input('Select option: ')

        if choice == 'q':
            clear()
            exit(0)
        elif choice == '0' or '1' or '2' or '3':
            break

    # Once finished, return the slected choice
    try:
        return int(choice)
    except:
        pass

# This function sets up a virtual environment for testing/deploying robot code
def setup_env():
    while True:
        clear()
        print(f'''Set up robotpy environment
''')
        choice = input(f'Setup virtual environment in {os.getcwd()}? [y/n] ')
        
        if choice == 'y':
            # Venv setup for windows
            if 'Windows' in platform.system():
                if os.path.exists('WPIEnv'):
                    print('Environment already exists,\nskipping build and updating dependencies...')
                    time.sleep(3)
                    pass

                else:
                    print('Setting up virtual environment...')
                    subprocess.call(f'python -m venv {os.getcwd()}\\WPIEnv', shell=True)

                while True:
                    clear()

                    # Install dependencies (or don't)
                    if choice == 'y':
                        # Install robotpy dependencies
                        subprocess.call('WPIEnv\\Scripts\\python.exe -m pip install robotpy robotpy-ctre robotpy-navx robotpy-rev numpy', shell=True)
                        subprocess.call('WPIEnv\\Scripts\\python.exe -m pip install --upgrade robotpy robotpy-ctre robotpy-navx robotpy-rev numpy', shell=True)
                        break
                    elif choice == 'n':
                        break
            break
        elif choice == 'n':
            break

def remote_shell():
    while True:
        clear()
        print('''Remote shell into robot
''')
        hostname = input('Hostname: ')
        ip = input('IP Address: ')
        port = input('Port (leve blank for default port 22): ')
        break
        # TODO: Add logic that runs a ssh client
    
def test_robot():
    clear()
    print('Running tests located in "tests/pyfrc_test.py"\n')
    subprocess.call('WPIEnv\\Scripts\\python.exe -m robotpy test')
    input('ENTER to continiue')

def deploy_robot_code():
    clear()
    try:
        subprocess.call('WPIEnv\\Scripts\\python.exe -m robotpy deploy --skip-tests --nc', shell=True)
    except Exception as e:
        print(e)
    input('ENTER to continiue')

# Main logic loop
def main():
    while True:
        main_menu_choice = main_menu()
        if main_menu_choice == 0:
            setup_env()
        elif main_menu_choice == 1:
            remote_shell()
        elif main_menu_choice == 2:
            test_robot()
        elif main_menu_choice == 3:
            deploy_robot_code()

if __name__ == '__main__':
    main()
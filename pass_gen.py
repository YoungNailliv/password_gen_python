import sys
import random
import subprocess


min_letters = "abcdefghijklmnopqrstuvwxyz"
mayus_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
especial_letters = "!@#$%^&*()_-+}={:;.,/?<>~`\|"
numbers = "1234567890"
num_of_caracters = 30
password = ""
caracters_allow = ""

try:
    if '-' in sys.argv[1]:
        arguments = sys.argv[1]
        if 'l' in arguments:
            caracters_allow += min_letters + mayus_letters
        if 'n' in arguments:
            caracters_allow += numbers
        if 'e' in arguments:
            caracters_allow += especial_letters
    else:
        is_number = sys.argv[1].isdigit()
        if is_number:
            num_of_caracters = int(sys.argv[1])
        caracters_allow = min_letters + mayus_letters + especial_letters + numbers
except:
    caracters_allow = min_letters + mayus_letters + especial_letters + numbers

try:
    if sys.argv[2]:
        try:
            num_of_caracters = int(sys.argv[2])
        except ValueError:
            pass
except:
    pass



for x in range(num_of_caracters):
    password += random.choice(caracters_allow)


match sys.platform:
    case 'linux':
        try:
            def set_clipboard_text(text):
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
            set_clipboard_text(password)
        except:
            print("Could not copy password to clipboard")
    case 'darwin':
        try:
            def set_clipboard_text(text):
                process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
            set_clipboard_text(password)
        except:
            print("Could not copy password to clipboard")
    case _:
        print("Could not copy password to clipboard")


print(password)
print("\nPassword copy to the clipboard!")



import os, colorama


def find_webdriver(driver_name):
    os.chdir('/')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == driver_name:
                results.append(os.path.join(root, driver_name))
                print(colorama.Fore.GREEN,
                        f'[*] {driver_name} Found in: {os.path.join(root, driver_name)}',
                        colorama.Style.RESET_ALL)
            else:
                continue

    if results == []:
        print(colorama.Fore.RED,
              f'{driver_name} does not exist in your system.',
              colorama.Style.RESET_ALL)


if __name__ == '__main__':
    colorama.init()
    results = []
    webdriver = input('Enter the name of the Webdriver you want to locate inside your system: ')
    find_webdriver(webdriver)


import os, colorama, platform


class Process():

    def write_into_file(self, paths):
        with open('Results.txt', 'w') as f:
            for path in paths:
                f.write(f'{path}\n')


    def local_dir(self):
        os.chdir(origin)
        return 'Returned to original working directory'


    def find_webdriver(self, driver_name):
        os.chdir('/')

        # Windows Support as well lmao
        if Process().identify_os() == 'Windows':
            driver_name = driver_name + '.exe'

        for root, dirs, files in os.walk(os.getcwd()):
            dirs = dirs
            for file in files:
                if file == driver_name:
                    results.append(os.path.join(root, driver_name))
                    print(colorama.Fore.GREEN,
                            f"[*] '{driver_name}' Found in: {os.path.join(root, driver_name)}",
                            colorama.Style.RESET_ALL)
                else:
                    continue

        if results == []:
            print(colorama.Fore.RED,
                  f"[!!] '{driver_name}' does not exist in your system.",
                colorama.Style.RESET_ALL)
        else:
            Process().local_dir()
            return Process().write_into_file(results)


    def identify_os(self):
        os = platform.system()
        return os


if __name__ == '__main__':
    origin = os.getcwd()
    colorama.init()
    results = []
    webdrivers = ['chromedriver',
                  'msedgedriver',
                  'geckodriver']
    webdriver = input('Enter the name of the Webdriver you want to locate inside your system: ')

    if webdriver == 'q':
        quit()
    elif webdriver in webdrivers:
        Process().find_webdriver(webdriver)
    else:
        raise ValueError(colorama.Fore.RED, '[!!] Invalid Option.', colorama.Style.RESET_ALL)

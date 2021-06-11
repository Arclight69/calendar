from tkinter import *
import requests
import colorama
from colorama import Fore, Back, Style
import os
from datetime import date

root = Tk()
colorama.init(autoreset=True)
actualmonth = requests.get('https://pastebin.com/raw/u7dt2G0b')
root.title('Kalender')
root.geometry("400x545")
datum = date.today()
# ***********
# VERSION 2.1
# ***********


# german version






def check_current_month():
	os.system("cls")

	if actualmonth.text == 'januar':
		januar()

	elif actualmonth.text == 'feburar':
		feburar()

	elif actualmonth.text == 'märz':
		maerz()	

	elif actualmonth.text == 'april':
		april()

	elif actualmonth.text == 'mai':
		mai()

	elif actualmonth.text == 'juni':
		juni()

	elif actualmonth.text == 'juli':
		juli()

	elif actualmonth.text == 'august':
		august()

	elif actualmonth.text == 'september':
		september()

	elif actualmonth.text == 'oktober':
		oktober()

	elif actualmonth.text == 'november':
		november()

	elif actualmonth.text == 'dezember':
		dezember()



def feiertage():
	os.system("cls")
	print('')
	print(Fore.MAGENTA + '    01.01.2021 Neujahr')
	print('')
	print(Fore.MAGENTA + '    15.02.2021 (Rosenmontag, nicht in Hessen)')
	print('')
	print(Fore.MAGENTA + '    02.04.2021 Karfreitag')
	print('')
	print(Fore.MAGENTA + '    05.04.2021 Ostermontag')
	print('')
	print(Fore.MAGENTA + '    01.05.2021 Maifeiertag (Sa)')
	print('')
	print(Fore.MAGENTA + '    13.05.2021 Christi Himmelfahrt, Vatertag in D')
	print('')
	print(Fore.MAGENTA + '    24.05.2021 Pfingstmontag')
	print('')
	print(Fore.MAGENTA + '    03.06.2021 Fronleichnam')
	print('')
	print(Fore.MAGENTA + '    03.10.2021 Tag d. Dt. Einheit')
	print('')
	print(Fore.MAGENTA + '    01.11.2021 (Allerheiligen, nicht in Hessen)')
	print('')
	print(Fore.MAGENTA + '    25.12.2021 Erster Weihnachtstag (Sa)')
	print('')
	print(Fore.MAGENTA + '    26.12.2021 Zweiter Weihnachtstag (So)')





def clearcon():
	os.system("cls")



def schliessen():
	exit()



def januar():
	os.system("cls")

	print('       _                                ___   ___ ___  __ ')
	print('      | |                              |__ \ / _ \__ \/_ |')
	print('      | | __ _ _ __  _   _  __ _ _ __     ) | | | | ) || |')
	print("  _   | |/ _` | '_ \| | | |/ _` | '__|   / /| | | |/ / | |")
	print(' | |__| | (_| | | | | |_| | (_| | |     / /_| |_| / /_ | |')
	print('  \____/ \__,_|_| |_|\__,_|\__,_|_|    |____|\___/____||_|')
	print('')
	print('')

	print(Fore.RED + '    1.     <<< Neujahr' + Fore.WHITE + '                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def februar():
	os.system("cls")

	print('  ______   _                             ___   ___ ___  __ ')
	print(' |  ____| | |                           |__ \ / _ \__ \/_ |')
	print(' | |__ ___| |__  _ __ _   _  __ _ _ __     ) | | | | ) || |')
	print(" |  __/ _ \ '_ \| '__| | | |/ _` | '__|   / /| | | |/ / | |")
	print(' | | |  __/ |_) | |  | |_| | (_| | |     / /_| |_| / /_ | |')
	print(' |_|  \___|_.__/|_|   \__,_|\__,_|_|    |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                             ')
	print('   14.                                             ')
	print(Fore.RED + '   15.     <<< Rosenmontag              ')
	print('   16.                                             ')
                        


def maerz():
	os.system("cls")

	print('  __  __ _   _            ___   ___ ___  __ ')
	print(' |  \/  (_) (_)          |__ \ / _ \__ \/_ |')
	print(' | \  / | __ _ _ __ ____    ) | | | | ) || |')
	print(" | |\/| |/ _` | '__|_  /   / /| | | |/ / | |")
	print(' | |  | | (_| | |   / /   / /_| |_| / /_ | |')
	print(' |_|  |_|\__,_|_|  /___| |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def april():
	os.system("cls")

	print('                      _ _   ___   ___ ___  __ ')
	print('     /\              (_) | |__ \ / _ \__ \/_ |')
	print('    /  \   _ __  _ __ _| |    ) | | | | ) || |')
	print("   / /\ \ | '_ \| '__| | |   / /| | | |/ / | |")
	print('  / ____ \| |_) | |  | | |  / /_| |_| / /_ | |')
	print(' /_/    \_\ .__/|_|  |_|_| |____|\___/____||_|')
	print('          | |                                 ')
	print('          |_|                                 ')
	print('')
	print('')

	print('    1.                                          17.')
	print(Fore.RED + '    2.     <<< Karfreitag' + Fore.RESET + '                       18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print(Fore.RED + '    5.     <<< Ostermontag' + Fore.RESET + '                      21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                             ')
	print('   16.                                             ')



def mai():
	os.system("cls")

	print('  __  __       _   ___   ___ ___  __ ')
	print(' |  \/  |     (_) |__ \ / _ \__ \/_ |')
	print(' | \  / | __ _ _     ) | | | | ) || |')
	print(" | |\/| |/ _` | |   / /| | | |/ / | |")
	print(' | |  | | (_| | |  / /_| |_| / /_ | |')
	print(' |_|  |_|\__,_|_| |____|\___/____||_|')
	print('')
	print('')

	print(Fore.RED + '    1.     <<< Maifeiertag ' + Fore.RESET + '                     17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print(Fore.RESET + '    6.      ' + Fore.RED + 'Ostermontag >>>                     22.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print(Fore.RED + '   13.     <<< Christi Himmelfahrt ' + Fore.RESET + '             29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def juni():
	os.system("cls")

	print('       _             _   ___   ___ ___  __ ')
	print('      | |           (_) |__ \ / _ \__ \/_ |')
	print('      | |_   _ _ __  _     ) | | | | ) || |')
	print("  _   | | | | | '_ \| |   / /| | | |/ / | |")
	print(' | |__| | |_| | | | | |  / /_| |_| / /_ | |')
	print('  \____/ \__,_|_| |_|_| |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print(Fore.RED + '    3.     <<< Fronleichnam ' + Fore.RESET + '                    19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                             ')
	print('   16.                                             ')



def juli():
	os.system("cls")

	print('       _       _ _   ___   ___ ___  __ ')
	print('      | |     | (_) |__ \ / _ \__ \/_ |')
	print('      | |_   _| |_     ) | | | | ) || |')
	print("  _   | | | | | | |   / /| | | |/ / | |")
	print(' | |__| | |_| | | |  / /_| |_| / /_ | |')
	print('  \____/ \__,_|_|_| |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def august():
	os.system("cls")

	print('                                _     ___   ___ ___  __ ')
	print('     /\                        | |   |__ \ / _ \__ \/_ |')
	print('    /  \  _   _  __ _ _   _ ___| |_     ) | | | | ) || |')
	print("   / /\ \| | | |/ _` | | | / __| __|   / /| | | |/ / | |")
	print('  / ____ \ |_| | (_| | |_| \__ \ |_   / /_| |_| / /_ | |')
	print(' /_/    \_\__,_|\__, |\__,_|___/\__| |____|\___/____||_|')
	print('                 __/ |                                  ')
	print('                |___/                                   ')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def september():
	os.system("cls")

	print('   _____            _                 _                 ___   ___ ___  __ ')
	print('  / ____|          | |               | |               |__ \ / _ \__ \/_ |')
	print(' | (___   ___ _ __ | |_ ___ _ __ ___ | |__   ___ _ __     ) | | | | ) || |')
	print("  \___ \ / _ \ '_ \| __/ _ \ '_ ` _ \| '_ \ / _ \ '__|   / /| | | |/ / | |")
	print('  ____) |  __/ |_) | ||  __/ | | | | | |_) |  __/ |     / /_| |_| / /_ | |')
	print(' |_____/ \___| .__/ \__\___|_| |_| |_|_.__/ \___|_|    |____|\___/____||_|')
	print('             | |                                                          ')
	print('             |_|                                                          ')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                             ')
	print('   16.                                             ')



def oktober():
	os.system("cls")

	print('   ____  _    _        _                 ___   ___ ___  __ ')
	print('  / __ \| |  | |      | |               |__ \ / _ \__ \/_ |')
	print(' | |  | | | _| |_ ___ | |__   ___ _ __     ) | | | | ) || |')
	print(" | |  | | |/ / __/ _ \| '_ \ / _ \ '__|   / /| | | |/ / | |")
	print(' | |__| |   <| || (_) | |_) |  __/ |     / /_| |_| / /_ | |')
	print('  \____/|_|\_\\__\___/|_.__/ \___|_|    |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print(Fore.RED + '    3.     <<< Tag d. Dt. Einheit ' + Fore.RESET + '              19')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')



def november():
	os.system("cls")

	print('  _   _                          _                 ___   ___ ___  __ ')
	print(' | \ | |                        | |               |__ \ / _ \__ \/_ |')
	print(' |  \| | _____   _____ _ __ ___ | |__   ___ _ __     ) | | | | ) || |')
	print(" | . ` |/ _ \ \ / / _ \ '_ ` _ \| '_ \ / _ \ '__|   / /| | | |/ / | |")
	print(' | |\  | (_) \ V /  __/ | | | | | |_) |  __/ |     / /_| |_| / /_ | |')
	print(' |_| \_|\___/ \_/ \___|_| |_| |_|_.__/ \___|_|    |____|\___/____||_|')
	print('')
	print('')

	#-----------------------------nicht in hessen
	print(Fore.RED + '    1.     <<< Allerheiligen ' + Fore.RESET + '                   17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print('    9.                                          25.')
	print('   10.                                          26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                             ')
	print('   16.                                             ')



def dezember():
	os.system("cls")

	print('  _____                         _                 ___   ___ ___  __ ')
	print(' |  __ \                       | |               |__ \ / _ \__ \/_ |')
	print(' | |  | | ___ _______ _ __ ___ | |__   ___ _ __     ) | | | | ) || |')
	print(" | |  | |/ _ \_  / _ \ '_ ` _ \| '_ \ / _ \ '__|   / /| | | |/ / | |")
	print(' | |__| |  __// /  __/ | | | | | |_) |  __/ |     / /_| |_| / /_ | |')
	print(' |_____/ \___/___\___|_| |_| |_|_.__/ \___|_|    |____|\___/____||_|')
	print('')
	print('')

	print('    1.                                          17.')
	print('    2.                                          18.')
	print('    3.                                          19.')
	print('    4.                                          20.')
	print('    5.                                          21.')
	print('    6.                                          22.')
	print('    7.                                          23.')
	print('    8.                                          24.')
	print(Fore.RESET + '   9.     <<< Erster Weihnachtstag ' + Fore.RED + '             25.')
	print(Fore.RESET + '   10.     <<< Zweiter Weihnachtstag ' + Fore.RED + '           26.')
	print('   11.                                          27.')
	print('   12.                                          28.')
	print('   13.                                          29.')
	print('   14.                                          30.')
	print('   15.                                          31.')
	print('   16.                                             ')












feiertage_button = Button(root, text="Feiertage Aufgelistet", fg="yellow", pady=3, padx=20, command=feiertage)
close = Button(root, text="Exit", fg="red", pady=3, padx=20, command=schliessen)
rn = Button(root, text="Aktueller Monat", fg="green", pady=3, padx=20, command=check_current_month)
clearconsole = Button(root, text="Clear Console", fg="orange", pady=3, padx=20, command=clearcon)
jan = Button(root, text="Januar 2021", fg="blue", pady=3, padx=20, command=januar)
feb = Button(root, text="Februar", fg="blue", pady=3, padx=20, command=februar)
mae = Button(root, text="März", fg="blue", pady=3, padx=20, command=maerz)
apr = Button(root, text="April", fg="blue", pady=3, padx=20, command=april)
ma = Button(root, text="Mai", fg="blue", pady=3, padx=20, command=mai)
jun = Button(root, text="Juni", fg="blue", pady=3, padx=20, command=juni)
jul = Button(root, text="Juli", fg="blue", pady=3, padx=20, command=juli)
aug = Button(root, text="August", fg="blue", pady=3, padx=20, command=august)
sep = Button(root, text="September", fg="blue", pady=3, padx=20, command=september)
okt = Button(root, text="Oktober", fg="blue", pady=3, padx=20, command=oktober)
nov = Button(root, text="November", fg="blue", pady=3, padx=20, command=november)
dez = Button(root, text="Dezember", fg="blue", pady=3, padx=20, command=dezember)
date_field = Label(root, text=datum)



rn.pack()
jan.pack()
feb.pack()
mae.pack()
apr.pack()
ma.pack()
jun.pack()
jul.pack()
aug.pack()
sep.pack()
okt.pack()
nov.pack()
dez.pack()
clearconsole.pack()
feiertage_button.pack()
close.pack()
date_field.pack()






































































































































































































root.mainloop()


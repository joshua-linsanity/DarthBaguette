from pathlib import Path 

file = Path(r"C:\Users\jlin5\AppData\Local\SumatraPDF\SumatraPDF-settings.txt")

mode = input('light or dark? --> ')
data = []

with open(file) as f:
	data = f.readlines()

if mode == 'light':
	data[2] = '	TextColor = #000000\n'
	data[3] = '	BackgroundColor = #ffffff\n'
	with open(file, 'w') as f:
		f.writelines(data)
elif mode == 'dark':
	data[2] = '	TextColor = #eeeeee\n'
	data[3] = '	BackgroundColor = #111111\n'
	with open(file, 'w') as f:
		f.writelines(data)

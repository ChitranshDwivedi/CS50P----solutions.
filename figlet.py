from pyfiglet import Figlet
import sys
import random

f = Figlet()

if len(sys.argv) == 1:
    f.setFont(font=random.choice(f.getFonts()))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font_name = sys.argv[2]
    if font_name not in f.getFonts():
       sys.exit("Invalid font")
    f.setFont(font=font_name)

else:
    sys.exit("Invalid usage")

x = input("Input: ")
print("Output: ")
print(f.renderText(x))

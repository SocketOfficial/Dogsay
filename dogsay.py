import sys
import colorama
from colorama import Fore

colorama.init()

try:
    text = " ".join(sys.argv[1:])  # Join all command line arguments to form the complete text

    print(Fore.GREEN + f"""
    
          <| {text.capitalize()} |>
               /
              /
             /
_     /)---(\      
\\   (/ . . \)     
 \\__)-\(*)/         
 \_       (_      
 (___/-(____) 

    """)

except:
    print("Usage: python3 dogsay.py <text>")

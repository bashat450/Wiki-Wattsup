import pywhatkit as kt
import getpass as gp

print("Let's Automate WattsApp!\n")

p_num = gp.getpass(prompt='PhoneNumber: ', stream=None)

msg = 'Many Many Happy Returns Of the Day '

kt.sendwhatmsg(p_num, msg, 9, 53)

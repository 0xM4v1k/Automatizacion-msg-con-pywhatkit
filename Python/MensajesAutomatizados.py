import pywhatkit

#numTel = str(input("Por favor, digame el número: "))
mensaje = str(input("Por favor, digame un mensaje: "))
horas = int(input("Por favor digame las horas: "))
minutos = int(input("Por favor digame los minutos: "))

try: 
  #pywhatkit.sendwhatmsg(f"+51 {numTel}", mensaje, horas, minutos)
  pywhatkit.sendwhatmsg_to_group("LkgKVCof2bx95URXz1XaO1", mensaje, horas, minutos)
    
  print("Mensaje enviado con éxito")

except Exception as e:
   print("Upss ocurrió un error", str(e))

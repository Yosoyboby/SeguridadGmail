import smtplib
import getpass

# Iniciar sesion en la cuenta de Gmail
username = input("Ingresa tu correo electronico:")
password = getpass.getpass("Ingresa tu contraseña:")

server = smtplib.SMTB('smtp.gmail.com',587)
server.starttls()
server.login(username,password)

# Enviar un mensaje de verificacion
to = input("Ingresa el correo electronico de verificacion:")
subject = "Verificacion de cuenta"
body = "Este es un mensaje de verificacion para tu cuenta de Gmail. Si no solicitaste esta verificacion, por favor ignora este mensaje"

msg = f"Subject:{subject}\n\n{body}"

server.sendmail(username, to, msg)
print("Mensaje de verificacion enviado.")

# Cerrar sesion
server.quit()
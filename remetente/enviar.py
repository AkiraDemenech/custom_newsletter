arq_smtp = 'arq.smtp.txt'
arq_email = 'arq.email.txt'
arq_senha = 'arq.senha.txt'

import smtplib
import ssl

#import yagmail


porta = 587 
porta = 465 # Porta SSL 

smtp = open(arq_smtp,'r').read().strip()
email = open(arq_email,'r').read().strip()
senha = open(arq_senha,'r').read().strip()




with smtplib.SMTP_SSL(smtp, porta, context=ssl.create_default_context()) as servidor:			

	servidor.login(email, senha)

				   

	servidor.quit()

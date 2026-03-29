import qrcode
  
content = "@misc{\n\t" + "name: Josué Rodríguez Ramírez\n\t" + "title: Proceso de Evaluación Automática en Problemas de Enrutamiento de Vheículos\n\t" + 'advisors:\n\t\tMSc. Fernando Rodríguez Flores,\n\t\tLic. Rodrigo García Gómez\n\t' + 'year: 2023\n\t' + "university: University of Havana\n\t" + 'type: Diploma Thesis\n' + "}"

print (content)
  
#~ # Generate QR code

url = qrcode.make(content) 

# Create and save the png file naming "myqr.png" 
# url.png('qrcode-tesis.png', scale = 6) 
f = open("qrcode-tesis.png", "wb")
url.save(f)
f.close()

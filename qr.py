import qrcode

url = input("enter url :")
image = qrcode.make(url)
image.save('1.png')

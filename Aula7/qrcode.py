# pip install qrcode[pil]

import qrcode

# criar um codigo

qr = qrcode.QRCode(version=1, box_size=10, border=5)

# adicionar dados ao código QR

data = "https://www.google.com"
qr.add_data(data)
qr.make(fit=True)

#c criar imagem do código QR
img = qr.make_image(fill_color="black", black_color="white")

# salvar imagem em um arquivo
img.save("qr_code.png")
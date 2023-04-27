import io
import qrcode

qr = qrcode.QRCode()
qr.add_data("Teste QRCode")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

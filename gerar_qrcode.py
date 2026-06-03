import sys

try:
    import qrcode
except ImportError:
    print("Instale a biblioteca qrcode antes de rodar:")
    print("pip install qrcode[pil]")
    raise SystemExit(1)

url = sys.argv[1] if len(sys.argv) > 1 else "https://seudominio.com/cartao"

img = qrcode.make(url)
img.save("qr-code.png")

print(f"QR Code gerado em qr-code.png apontando para: {url}")

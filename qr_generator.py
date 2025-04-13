import qrcode

class QRCodeGenerator:
    def generate_qr_codes(self, n):
        for i in range(1, n + 1):
            data = f"QR Code #{i}"  # You can customize this to any unique content
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"qr_code_{i}.png")
            print(f"Generated qr_code_{i}.png with data: '{data}'")

# Example usage
user_input = int(input("Enter the number of QR codes to generate: "))
qr = QRCodeGenerator()
qr.generate_qr_codes(user_input)

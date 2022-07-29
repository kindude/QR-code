import qrcode


def generate_qr(text='hello', file_name='qrcode.png'):
    qr = qrcode.make(text)
    qr.save(file_name)


def main():
    text = input('Put your text:')
    file_name = input('Put name of QR-code file:')
    file_name += '.png'
    generate_qr(text, file_name)


if __name__ == '__main__':
    main()

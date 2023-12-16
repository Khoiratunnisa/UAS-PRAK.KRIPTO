from flask import Flask, render_template, request

app = Flask(__name__)

def otp_encrypt(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_message += encrypted_char
    return encrypted_message

def otp_decrypt(encrypted_message, key):
    return otp_encrypt(encrypted_message, key)  # Dekripsi sama dengan enkripsi pada OTP

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    key = request.form['key']
    encrypted_message = otp_encrypt(message, key)
    return render_template('result.html', action='Encrypt', message=message, key=key, result=encrypted_message)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    key = request.form['key']
    decrypted_message = otp_decrypt(encrypted_message, key)
    return render_template('result.html', action='Decrypt', message=encrypted_message, key=key, result=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True)

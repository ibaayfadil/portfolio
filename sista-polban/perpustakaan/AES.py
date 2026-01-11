from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import struct
from PIL import Image

pdf = ['PDF/E', 'PDF/A', 'PDF/UA', 'PDF']
doc = ['DOCX']
png = ['JPEG', 'JPG', 'PNG']
xlsx = ['XLSX','XLS']

def GenKey():
    # generate key acak dengan panjang 128 bit (16 byte)
    key = get_random_bytes(16)
    print('Ini adalah kunci:', key)
    # with open('key.key', 'wb') as file:
    #     file.write(key)
    return key


# def EncryptTXT(txtpath, keypath):
#     with open(txtpath, 'rb') as file:
#         plaintext = file.read()
#     with open(keypath, 'rb') as file:
#         key = file.read()
#     # buat objek cipher AES dengan mode CBC
#     cipher = AES.new(key, AES.MODE_CBC)
#     # enkripsi plaintext
#     ciphertext = cipher.iv + cipher.encrypt(pad(plaintext, AES.block_size))
#     # simpan ciphertext pada file
#     fn = os.path.basename(txtpath).split(".")[0]
#     with open(f'./media/docs/{fn}_encrypted.txt', 'wb') as file:
#         file.write(ciphertext)
#     return os.path.abspath(f'./media/docs/{fn}_encrypted.txt')

# def DecryptTXT(txtpath, keypath):
#     # membaca file yang akan didekripsi
#     with open(txtpath, 'rb') as file:
#         ciphertext = file.read()
#     with open(keypath, 'rb') as file:
#         key = file.read()
#     # buat objek cipher AES dengan mode CBC
#     cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
#     # dekripsi ciphertext
#     plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
#     # simpan plaintext pada file
#     fn = os.path.basename(txtpath).split(".")[0]
#     with open(f'./media/dec/{fn}_decrypted.txt', 'wb') as file:
#         file.write(plaintext)
#     return os.path.abspath(f'./media/dec/{fn}_decrypted.txt')

def EncryptTXT(txtpath, keypath):
    with open(txtpath, 'rb') as file:
        plaintext = file.read()
    with open(keypath, 'rb') as file:
        key = file.read()
    # buat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM)
    print("ini adalah cipher txt = ", cipher)
    # enkripsi plaintext
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    print("ini adalah ciphertext txt = ", ciphertext)
    # simpan ukuran ciphertext dan tag autentikasi pada metadata
    size_bytes = struct.pack('Q', len(ciphertext))
    ciphertext_with_metadata = size_bytes + cipher.nonce + ciphertext + tag
    # simpan ciphertext pada file
    fn = os.path.basename(txtpath).split(".")[0]
    with open(f'./media/docs/{fn}_encrypted.txt', 'wb') as file:
        file.write(ciphertext_with_metadata)
    return os.path.abspath(f'./media/docs/{fn}_encrypted.txt')

def DecryptTXT(txtpath, keypath):
    # membaca file yang akan didekripsi
    with open(txtpath, 'rb') as file:
        ciphertext_with_metadata = file.read()
    with open(keypath, 'rb') as file:
        key = file.read()
    # baca ukuran ciphertext dan metadata dari file
    size = struct.unpack('Q', ciphertext_with_metadata[:8])[0]
    nonce = ciphertext_with_metadata[8:24]
    ciphertext = ciphertext_with_metadata[24:-16]
    tag = ciphertext_with_metadata[-16:]
    # buat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # dekripsi ciphertext dan verifikasi tag autentikasi
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    # simpan plaintext pada file
    fn = os.path.basename(txtpath).split(".")[0]
    with open(f'./media/dec/{fn}_decrypted.txt', 'wb') as file:
        file.write(plaintext)
    return os.path.abspath(f'./media/dec/{fn}_decrypted.txt')


# def EncryptImage(imagepath, keypath):
#     fn = os.path.basename(imagepath).split(".")[0]
#     with Image.open(imagepath) as img:
#         # konversi ke RGB jika mode RGBA
#         if img.mode == 'RGBA':
#             img = img.convert('RGB')
#         # resize gambar
#         width, height = img.size
#         size = (width, height)
#         # konversi gambar ke bytes
#         imagedata = img.tobytes()
#         # baca key dari file
#         with open(keypath, 'rb') as f:
#             key = f.read()
#         # buat objek AES
#         cipher = AES.new(key, AES.MODE_CBC)
#         # enkripsi plaintext
#         padded_data = pad(imagedata, AES.block_size)
#         encrypted_data = cipher.iv + cipher.encrypt(padded_data)
#         # simpan ukuran gambar dan ciphertext pada metadata
#         size_bytes = struct.pack('QQ', *size)
#         encrypted_data_with_metadata = size_bytes + encrypted_data + padded_data[-1].to_bytes(1, byteorder='big')
#         # simpan gambar pada file
#         with open(f'./media/docs/{fn}_encrypted.jpg', 'wb') as f:
#             f.write(encrypted_data_with_metadata)
#     return os.path.abspath(f'./media/docs/{fn}+encrypted.jpg')

# def DecryptImage(imagepath, keypath):
#     fn = os.path.basename(imagepath).split(".")[0]
#     # membaca file yang akan didekripsi
#     with open(imagepath, 'rb') as file:
#         imagedata = file.read()
#     with open(keypath, 'rb') as file:
#         key = file.read()
#     # baca ukuran gambar dari metadata
#     size = tuple(struct.unpack('QQ', imagedata[:16]))
#     # buat objek cipher AES dengan mode CBC
#     cipher = AES.new(key, AES.MODE_CBC, iv=imagedata[16:32])
#     # dekripsi ciphertext
#     decrypted_data = unpad(cipher.decrypt(imagedata[32:-1]), AES.block_size)
#     # simpan plaintext pada file
#     img = Image.frombytes('RGB', size, decrypted_data)
#     img.save(f'./media/dec/{fn}_decrypted.jpg')
#     return os.path.abspath(f'./media/dec/{fn}_decrypted.jpg')

def EncryptImage(imagepath, keypath):
    fn = os.path.basename(imagepath).split(".")[0]
    with Image.open(imagepath) as img:
        # konversi ke RGB jika mode RGBA
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # resize gambar
        width, height = img.size
        size = (width, height)
        # konversi gambar ke bytes
        imagedata = img.tobytes()
        # baca key dari file
        with open(keypath, 'rb') as f:
            key = f.read()
        # buat objek AES dengan mode GCM
        cipher = AES.new(key, AES.MODE_GCM)
        # enkripsi plaintext
        encrypted_data, tag = cipher.encrypt_and_digest(imagedata)
        # simpan ukuran gambar, nonce, ciphertext, dan tag autentikasi pada metadata
        size_bytes = struct.pack('QQ', *size)
        encrypted_data_with_metadata = size_bytes + cipher.nonce + encrypted_data + tag
        # simpan gambar pada file
        with open(f'./media/docs/{fn}_encrypted.jpg', 'wb') as f:
            f.write(encrypted_data_with_metadata)
    return os.path.abspath(f'./media/docs/{fn}_encrypted.jpg')

def DecryptImage(imagepath, keypath):
    fn = os.path.basename(imagepath).split(".")[0]
    # membaca file yang akan didekripsi
    with open(imagepath, 'rb') as file:
        imagedata = file.read()
    with open(keypath, 'rb') as file:
        key = file.read()
    # baca ukuran gambar dan metadata dari file
    size = tuple(struct.unpack('QQ', imagedata[:16]))
    nonce = imagedata[16:32]
    ciphertext = imagedata[32:-16]
    tag = imagedata[-16:]
    # buat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # dekripsi ciphertext dan verifikasi tag autentikasi
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    # simpan plaintext pada file
    img = Image.frombytes('RGB', size, decrypted_data)
    img.save(f'./media/dec/{fn}_decrypted.jpg')
    return os.path.abspath(f'./media/dec/{fn}_decrypted.jpg')


# def EncryptPdf(pdf_path, key_path):
#     fn = os.path.basename(pdf_path).split(".")[0]
#     # membaca file PDF dan membaca key AES
#     with open(pdf_path, 'rb') as file:
#         pdf_data = file.read()
#     with open(key_path, 'rb') as file:
#         key = file.read()
#     # membuat objek cipher AES dengan mode CBC
#     iv = os.urandom(16)
#     cipher = AES.new(key, AES.MODE_CBC, iv=iv)
#     # mengenkripsi isi file PDF
#     encrypted_data = iv + cipher.encrypt(pad(pdf_data, AES.block_size))
#     # menulis file PDF yang telah dienkripsi
#     with open(f'./media/docs/{fn}_encrypted.pdf', 'wb') as file:
#         file.write(encrypted_data)
#     return os.path.abspath(f'./media/docs/{fn}_encrypted.pdf')

# def DecryptPdf(pdf_path, key_path):
#     fn = os.path.basename(pdf_path).split(".")[0]
#     # membaca file PDF yang telah dienkripsi dan membaca key AES
#     with open(pdf_path, 'rb') as file:
#         encrypted_data = file.read()
#     with open(key_path, 'rb') as file:
#         key = file.read()
#     # membaca iv dari data terenkripsi
#     iv = encrypted_data[:16]
#     # membuat objek cipher AES dengan mode CBC
#     cipher = AES.new(key, AES.MODE_CBC, iv=iv)
#     # mendekripsi isi file PDF
#     decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
#     # menulis file PDF yang telah didekripsi
#     with open(f"./media/dec/{fn}_decrypted.pdf", 'wb') as file:
#         file.write(decrypted_data)
#     return os.path.abspath(f'./media/dec/{fn}_decrypted.pdf')

def EncryptPdf(pdf_path, key_path):
    fn = os.path.basename(pdf_path).split(".")[0]
    # membaca file PDF dan membaca key AES
    with open(pdf_path, 'rb') as file:
        pdf_data = file.read()
    with open(key_path, 'rb') as file:
        key = file.read()
    # membuat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM)
    # mengenkripsi isi file PDF
    encrypted_data, tag = cipher.encrypt_and_digest(pdf_data)
    # menulis file PDF yang telah dienkripsi beserta tag autentikasi
    with open(f'./media/docs/{fn}_encrypted.pdf', 'wb') as file:
        file.write(cipher.nonce + encrypted_data + tag)
    return os.path.abspath(f'./media/docs/{fn}_encrypted.pdf')

def DecryptPdf(pdf_path, key_path):
    fn = os.path.basename(pdf_path).split(".")[0]
    # membaca file PDF yang telah dienkripsi dan membaca key AES
    with open(pdf_path, 'rb') as file:
        encrypted_data = file.read()
    with open(key_path, 'rb') as file:
        key = file.read()
    # membaca nonce dan tag autentikasi dari data terenkripsi
    nonce = encrypted_data[:16]
    tag = encrypted_data[-16:]
    # membuat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # mendekripsi isi file PDF
    decrypted_data = cipher.decrypt_and_verify(encrypted_data[16:-16], tag)
    # menulis file PDF yang telah didekripsi
    with open(f"./media/dec/{fn}_decrypted.pdf", 'wb') as file:
        file.write(decrypted_data)
    return os.path.abspath(f'./media/dec/{fn}_decrypted.pdf')


# def EncryptDoc(docpath,keypath):
#     fn = os.path.basename(docpath).split(".")[0]
#     # membaca file dokumen dan membaca key AES
#     with open(keypath, 'rb') as file:
#         key = file.read()
#     with open(docpath, 'rb') as f:
#         plaintext = f.read()
#     # mengenkripsi dokumen
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext = cipher.iv + cipher.encrypt(pad(plaintext, AES.block_size))
#     # menyimpan dokumen terenkripsi pada file baru
#     with open(f'./media/docs/{fn}_encrypted.docx', 'wb') as f:
#         f.write(ciphertext)
#     return os.path.abspath(f'./media/docs/{fn}_encrypted.docx')

# def DecryptDoc(docpath,keypath):
#     fn = os.path.basename(docpath).split(".")[0]
#     # membaca file yang telah terenkripsi dan key
#     with open(keypath, 'rb') as file:
#         key = file.read()
#     with open(docpath, 'rb') as f:
#         ciphertext = f.read()
#     # mendekripsi dokumen
#     cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
#     plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
#     # menyimpan dokumen terdekripsi pada file baru
#     with open(f'./media/dec/{fn}_decrypted.docx', 'wb') as f:
#         f.write(plaintext)
#     return os.path.abspath(f'./media/dec/{fn}_decrypted.docx')

def EncryptDoc(docpath,keypath):
    fn = os.path.basename(docpath).split(".")[0]
    # membaca file dokumen dan membaca key AES
    with open(keypath, 'rb') as file:
        key = file.read()
    with open(docpath, 'rb') as f:
        plaintext = f.read()
    # mengenkripsi dokumen
    cipher = AES.new(key, AES.MODE_GCM)
    print("ini adalah cipher doc", cipher)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    # menyimpan dokumen terenkripsi pada file baru
    with open(f'./media/docs/{fn}_encrypted.docx', 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)
    return os.path.abspath(f'./media/docs/{fn}_encrypted.docx')

def DecryptDoc(docpath,keypath):
    fn = os.path.basename(docpath).split(".")[0]
    # membaca file yang telah terenkripsi dan key
    with open(keypath, 'rb') as file:
        key = file.read()
    with open(docpath, 'rb') as f:
        ciphertext = f.read()
    # mendekripsi dokumen
    nonce, tag, ciphertext = ciphertext[:16], ciphertext[16:32], ciphertext[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    # menyimpan dokumen terdekripsi pada file baru
    with open(f'./media/dec/{fn}_decrypted.docx', 'wb') as f:
        f.write(plaintext)
    return os.path.abspath(f'./media/dec/{fn}_decrypted.docx')


# Fungsi untuk menambahkan padding pada plaintext
def add_padding(plaintext):
    block_size = 32
    padding = block_size - len(plaintext) % block_size
    print("ini adalah padding = ", padding)
    return plaintext + padding * bytes([padding])

# Fungsi untuk menghapus padding dari ciphertext
def remove_padding(ciphertext):
    padding = ord(bytes([ciphertext[-1]]))
    return ciphertext[:-padding]

def EncryptExcel(file_path, key_path):
    fn = os.path.basename(file_path).split(".")[0]
    with open(file_path, 'rb') as f:
        excel_data = f.read()
    with open(key_path, 'rb') as f:
        key = f.read()
    # Tambahkan padding pada plaintext
    plaintext = add_padding(excel_data)
    # Buat objek cipher AES dengan mode GCM
    cipher = AES.new(key, AES.MODE_GCM)
    # Enkripsi plaintext dan dapatkan tag autentikasi
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    # Simpan ukuran ciphertext dan tag autentikasi pada metadata
    size_bytes = struct.pack('Q', len(ciphertext))
    ciphertext_with_metadata = size_bytes + cipher.nonce + ciphertext + tag
    # Simpan ciphertext pada file
    with open(f'./media/docs/{fn}_encrypted.xlsx', 'wb') as f:
        f.write(ciphertext_with_metadata)
    return os.path.abspath(f'./media/docs/{fn}_encrypted.xlsx')

def DecryptExcel(file_path, key_path):
    fn = os.path.basename(file_path).split(".")[0]
    # Baca file yang akan didekripsi
    with open(file_path, 'rb') as f:
        ciphertext_with_metadata = f.read()
    with open(key_path, 'rb') as f:
        key = f.read()
    # Baca ukuran ciphertext dan metadata dari file
    size = struct.unpack('Q', ciphertext_with_metadata[:8])[0]
    nonce = ciphertext_with_metadata[8:24]
    ciphertext = ciphertext_with_metadata[24:-16]
    tag = ciphertext_with_metadata[-16:]
    # Buat objek cipher AES dengan mode GCM dan nonce diambil dari metadata
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # Dekripsi ciphertext dan verifikasi tag autentikasi
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    # Hapus padding dari plaintext
    plaintext = remove_padding(plaintext)
    # Simpan data terdekripsi ke file
    with open(f'./media/dec/{fn}_decrypted.xlsx', 'wb') as f:
        f.write(plaintext)
    return os.path.abspath(f'./media/dec/{fn}_decrypted.xlsx')

# # Fungsi enkripsi file Excel
# def EncryptExcel(file_path, key_path):
#     fn = os.path.basename(file_path).split(".")[0]
#     with open(file_path, 'rb') as f:
#         excel_data = f.read()
#     with open(key_path, 'rb') as f:
#         key = f.read()
#     plaintext = add_padding(excel_data)
#     cipher = AES.new(key, AES.MODE_ECB)
#     # Enkripsi plaintext
#     ciphertext = cipher.encrypt(plaintext)
#     # Tulis ciphertext ke file
#     with open(f'./media/docs/{fn}_encrypted.xlsx', 'wb') as f:
#         f.write(ciphertext)
#     return os.path.abspath(f'./media/docs/{fn}_encrypted.xlsx')

# # Fungsi dekripsi file Excel
# def DecryptExcel(file_path, key_path):
#     fn = os.path.basename(file_path).split(".")[0]
#     # Baca file terenkripsi
#     with open(file_path, 'rb') as f:
#         encrypted_data = f.read()
#     with open(key_path, 'rb') as f:
#         key = f.read()        
#     # Buat objek cipher AES dengan mode CBC dan IV diambil dari cipher text
#     cipher = AES.new(key, AES.MODE_ECB)
#     # Dekripsi ciphertext
#     plaintext = cipher.decrypt(encrypted_data)
#     # Hapus padding dari plaintext
#     plaintext = remove_padding(plaintext)
#     # Simpan data terdekripsi ke file
#     with open(f'./media/dec/{fn}_decrypted.xlsx', 'wb') as f:
#         f.write(encrypted_data)
#     return os.path.abspath(f'./media/dec/{fn}_decrypted.xlsx')

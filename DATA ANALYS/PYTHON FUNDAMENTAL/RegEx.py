import re
teks = "hubungi kami di email1@example.com atau email2@example.net"
email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', teks)
print(email)  # Output: ['email1@example.com', 'email2@example.net']

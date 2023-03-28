from cryptographyFramework import *

initializeWrite()
user = "amigo"
password = "1926"
encryptedText = encryptMessage(user, password, "Mudei a senha!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Mudei tudo!")
saveNewLine(encryptedText)


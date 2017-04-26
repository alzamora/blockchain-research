from bitcoin import *
from blockchain import *
priv = sha256("bitcoin is awesome lets all go to the moon someday")
print("sha256 private key : "+str(priv))
print("================================================")
pub = privtopub(priv)
print("public key : "+str(pub))
print("================================================")
addr = pubtoaddr(pub)
print("bitcoin address : "+str(addr))

print("================================================")
print("================================================")


file = open("history.txt", "w")
for r in history("1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX"):
    file.write(str(r)+"\n")
file.close()



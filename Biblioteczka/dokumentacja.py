import create_table
import autor
import insert_autor_data
import check_autor_id
import insert_data
import os

if os.path.exists("biblioteczka.txt"):
    os.remove("biblioteczka.txt")

strg_ = repr(insert_data.__doc__)
print(strg_)

f = open("biblioteczka.txt","a",encoding="utf-8")
f.write(strg_ + "\n")
f.close()


tab_ = repr(create_table.__doc__)
print(tab_)

f = open("biblioteczka.txt","a",encoding="utf-8")
f.write(tab_ + "\n")
f.close()


aut = repr(autor.Autor.__doc__)
print(aut)

f = open("biblioteczka.txt","a",encoding="utf-8")
f.write(aut + "\n")

f.close()


insaut = repr(insert_autor_data.dodaj_autora.__doc__)
print(insaut)

f = open("biblioteczka.txt","a",encoding="utf-8")
f.write(insaut + "\n")

f.close()

chkaut = repr(check_autor_id.filtr.__doc__)
print(chkaut)

f = open("biblioteczka.txt","a",encoding="utf-8")
f.write(chkaut + "\n")

f.close()
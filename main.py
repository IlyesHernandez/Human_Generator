from model.Humain import Humain
from BDD import *
import random

nationality = pays[random.randint(0, 20)]
Name = names[random.randint(0, 68)]
Age = random.randint(1, 105)

humain_generate = Humain(Name, Age, nationality)

print("Bonjour, nous avons généré un humain virtuelle voici plus d'information sur lui")
print("Nom:", humain_generate.name, "\nAge:", humain_generate.age, "ans\nNationalité:", humain_generate.nationality)
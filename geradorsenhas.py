import random
import string

tamanho = int(input('Digite o tamanho de sua Senha: '))
chars = string.ascii_letters + string.digits + '!@#$%&*(),.?/+*<>'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
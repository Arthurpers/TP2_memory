import subprocess

file_sizes = [100,1024] #Mo
block_sizes =[1, 2, 4, 8, 16, 32, 64, 128, 256, 512] #Ko

times = []
througpouts = []

for file_size in file_sizes :
  for block_size in block_sizes :
    commande = "./votre_programme " + str(file_size) + " " + str(block_size)
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)
    resultat = resultat.stdout.split("\n")
    times.append(resultat[0])
    througpouts.append(resultat[1])

print(times)
print(througpouts)
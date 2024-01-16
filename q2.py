import subprocess
import matplotlib.pyplot as plt

file_sizes = [100,1024] #Mo
block_sizes =[1, 2, 4, 8, 16, 32, 64, 128, 256, 512] #Ko

times = []
througpouts = []

for file_size in file_sizes :
  for block_size in block_sizes :
    commande = "./q1 " + str(file_size) + " " + str(block_size)
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)
    resultat = resultat.stdout.split("\n")
    # print(resultat)
    times.append(resultat[0])
    througpouts.append(resultat[1])



fig, ax = plt.subplots()

ax.plot(block_sizes, times[0:9], 'o')

# Set the labels for the x and y axes
ax.set_xlabel('Block Size (Ko)')
ax.set_ylabel('Time (s)')

# Set the title of the plot
ax.set_title('100 Mo file random write ')

# Display the plot
plt.savefig("plot.png")


fig, ax = plt.subplots()
ax.plot(block_sizes, times[10:19], 'o')

# Set the labels for the x and y axes
ax.set_xlabel('Block Size (Ko)')
ax.set_ylabel('Time (s)')

# Set the title of the plot
ax.set_title('1 Go file random write')

# Display the plot
plt.savefig("plot.png")
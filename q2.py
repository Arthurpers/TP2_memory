import subprocess
import matplotlib.pyplot as plt

file_sizes = [100,1024] #Mo
block_sizes =[1, 2, 4, 8, 16, 32, 64, 128, 256, 512] #Ko

times = []
througpouts = []

for file_size in file_sizes :
  for block_size in block_sizes :
    commande = "./q1 " + str(file_size) + " " + str(block_size)
    print(commande)
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)
    resultat = resultat.stdout.split("\n")
    # print(resultat)
    times.append(resultat[0])
    througpouts.append(resultat[1])



# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot block sizes vs times on the first subplot
ax1.plot(block_sizes, times[0:10], 'o') #Temps pour le fichier de 100 Mo 
ax1.set_xlabel('Block Size (Ko)')
ax1.set_ylabel('Time (s)')
ax1.set_title('100 Mo file write ')

# Plot block sizes vs throughputs on the second subplot
ax2.plot(block_sizes, times[10:20], 'o') #Temps pour le fichier de 1 Go
ax2.set_xlabel('Block Size (Ko)')
ax2.set_ylabel('Time (s)')
ax2.set_title('1 Go file write')

# Adjust the layout so that plots do not overlap
plt.tight_layout()

# Save the figure to a file
plt.savefig("plot1-v2.png")

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot block sizes vs times on the first subplot
ax1.plot(block_sizes, througpouts[0:10], 'o')
ax1.set_xlabel('Block Size (Ko)')
ax1.set_ylabel('Throughput (Mo/s)')
ax1.set_title('100 Mo file write ')

# Plot block sizes vs throughputs on the second subplot
ax2.plot(block_sizes, througpouts[10:20], 'o')
ax2.set_xlabel('Block Size (Ko)')
ax2.set_ylabel('Throughput (Mo/s)')
ax2.set_title('1 Go file write ')

# Adjust the layout so that plots do not overlap
plt.tight_layout()

# Save the figure to a file
plt.savefig("plot2-v2.png")
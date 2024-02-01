import subprocess
import matplotlib.pyplot as plt

file_sizes = [1024] #Mo
block_sizes =[1, 2, 4, 8, 16, 32, 64, 128, 256, 512] #Ko

througpouts = []

for file_size in file_sizes :
  for block_size in block_sizes :
    commande = "./ex2 " + str(file_size) + " " + str(block_size)
    print(commande)
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)
    resultat = resultat.stdout.split("\n")
    # print(resultat)
    througpouts.append(resultat[1])

# Create a figure and two subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)

# Plot block sizes vs times on the first subplot
ax1.plot(block_sizes, througpouts[0:10], 'o')
ax1.set_xlabel('Block Size (Ko)')
ax1.set_ylabel('Throughput (Mo/s)')
ax1.set_title('1 Go file - seq write ')

# Plot block sizes vs throughputs on the second subplot
ax2.plot(block_sizes, througpouts[10:20], 'o')
ax2.set_xlabel('Block Size (Ko)')
ax2.set_ylabel('Throughput (Mo/s)')
ax2.set_title('1 Go file - random write ')

# Plot block sizes vs throughputs on the second subplot
ax3.plot(block_sizes, througpouts[20:30], 'o')
ax3.set_xlabel('Block Size (Ko)')
ax3.set_ylabel('Throughput (Mo/s)')
ax3.set_title('1 Go file - seq read ')

# Plot block sizes vs throughputs on the second subplot
ax4.plot(block_sizes, througpouts[30:40], 'o')
ax4.set_xlabel('Block Size (Ko)')
ax4.set_ylabel('Throughput (Mo/s)')
ax4.set_title('1 Go file - random read ')
# Adjust the layout so that plots do not overlap
plt.tight_layout()

# Save the figure to a file
plt.savefig("ex2.png")
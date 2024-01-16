#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/time.h>
#include <math.h>

void generate_random_data(char *buffer, size_t size)
{
  for (size_t i = 0; i < size; ++i)
  {
    buffer[i] = rand() % 256;
  }
}

int main(int argc, char *argv[])
{
  if (argc != 3)
  {
    fprintf(stderr, "usage: %s <taille_fichier> (Mo) <taille_bloc> (Ko)\n", argv[0]);
    return EXIT_FAILURE;
  }

  size_t taille_fichier = atoi(argv[1]) * 1024 * 1024;
  size_t taille_bloc = atoi(argv[2]) * 1024;

  char *buffer = (char *)malloc(taille_bloc);

  int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0666);

  if (fd == -1)
  {
    perror("Error opening file");
    free(buffer);
    return EXIT_FAILURE;
  }

  struct timeval start, end;

  gettimeofday(&start, NULL);

  for (size_t i = 0; i < taille_fichier / taille_bloc; ++i)
  {
    generate_random_data(buffer, taille_bloc);
    ssize_t written_bytes = write(fd, buffer, taille_bloc);

    if (written_bytes == -1)
    {
      perror("Error writing to file");
      free(buffer);
      close(fd);
      return EXIT_FAILURE;
    }
  }

  gettimeofday(&end, NULL);

  close(fd);
  free(buffer);

  double elapsed_time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6;
  double throughput = (double)taille_fichier / (1024 * 1024) / elapsed_time; // Mo/s

  printf("Durée d'écriture: %.6f secondes\n", elapsed_time);
  printf("Débit d'écriture: %.2f Mo/s\n", throughput);

  return EXIT_SUCCESS;
}

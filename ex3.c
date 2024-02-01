#include <fcntl.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>

void generate_random_data(char *buffer, size_t size) {
  for (size_t i = 0; i < size; ++i) {
    buffer[i] = rand() % 256;
  }
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    fprintf(stderr,
            "usage: %s <taille_fichier> (Mo) <taille_bloc> (Ko) <temps_mort> "
            "(us)\n",
            argv[0]);
    return EXIT_FAILURE;
  }

  size_t taille_fichier = atoi(argv[1]) * 1024 * 1024;
  size_t taille_bloc = atoi(argv[2]) * 1024;

  char *buffer = (char *)malloc(taille_bloc);

  int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

  if (fd == -1) {
    perror("Error opening file");
    free(buffer);
    return EXIT_FAILURE;
  }

  struct timeval start, end;
  double elapsed_time_seq_read = 0;
  double elapsed_time_seq_write = 0;
  double elapsed_time_rand_read = 0;
  double elapsed_time_rand_write = 0;

  // initialize file.
  for (size_t i = 0; i < taille_fichier / taille_bloc; ++i) {
    generate_random_data(buffer, taille_bloc);
    gettimeofday(&start, NULL);
    ssize_t written_bytes = write(fd, buffer, taille_bloc);
    gettimeofday(&end, NULL);

    elapsed_time_seq_write +=
        (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6;

    if (written_bytes == -1) {
      perror("Error writing to file");
      free(buffer);
      close(fd);
      return EXIT_FAILURE;
    }
  }

  // seq read
  for (size_t i = 0; i < taille_fichier / taille_bloc; ++i) {
    gettimeofday(&start, NULL);
    ssize_t read_bytes = read(fd, buffer, taille_bloc);
    gettimeofday(&end, NULL);

    elapsed_time_seq_read +=
        (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6;

    if (read_bytes == -1) {
      perror("Error reading from file");
      free(buffer);
      close(fd);
      return EXIT_FAILURE;
    }
    usleep(atoi(argv[3]));
  }

  // random read
  for (size_t i = 0; i < taille_fichier / taille_bloc; ++i) {
    // Modifiy fd position randomly
    off_t offset = rand() % (taille_fichier - taille_bloc);
    if (lseek(fd, offset, SEEK_SET) == -1) {
      perror("Error seeking file");
      free(buffer);
      close(fd);
      return EXIT_FAILURE;
    }
    gettimeofday(&start, NULL);
    ssize_t read_bytes = read(fd, buffer, taille_bloc);
    gettimeofday(&end, NULL);

    elapsed_time_rand_read +=
        (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1e6;

    if (read_bytes == -1) {
      perror("Error reading from file");
      free(buffer);
      close(fd);
      return EXIT_FAILURE;
    }
    usleep(atoi(argv[3]));
  }

  close(fd);
  free(buffer);

  double throughput_seq_read =
      (double)taille_fichier / (1024 * 1024) / elapsed_time_seq_read; // Mo/s
  double throughput_rand_read =
      (double)taille_fichier / (1024 * 1024) / elapsed_time_rand_read; // Mo/s

  printf("%.2f\n", throughput_seq_read);
  printf("%.2f\n", throughput_rand_read);

  return EXIT_SUCCESS;
}

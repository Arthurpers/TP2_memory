# TP2 - Performances des systèmes de stockage

L'objectif de ce TP est de mesurer les performances des accès au système de stockage sous Unix/Linux.

## Exercice 1 - Débit des écritures sur un système de stockage

### 1. Mesurer le débit des écritures sur un système de stockage

Le programme permet de mesurer la durée de l'écriture d'un fichier. Il prend en paramètre la taille de bloc et la taille du fichier à créer en octets.

(cf. fichier `q1.c` pour l'implémentation.)

### 2. Courbes de performance

On trace ensuite les performances du système pour différentes tailles de fichier (100Mo et 1Go).

L'implémentation de ce programme est réalisé dans le fichier `q2.py`.

#### Analyse des courbes

Vous pouvez trouver les courbes dans le dossier `q2/`.

<!-- TODO: rédiger l'analyse des résultats -->

### 3. Utilisation du *Page Cache* sous Linux

A présent, on souhaite utiliser le *Page cache* de Linux pour mesurer les performances et ainsi les comparer aux résultats précédents.

Pour cela, on annule les effets de cache (au niveau système) pour les écritures, en ajoutant les flags `__O_DIRECT` et `O_SYNC` à l'ouverture du fichier.

Ces drapeaux permettent:

- `O_SYNC`
  - The file is opened for synchronous I/O.  Any write(2) requests on the resulting file descriptor will block the calling process until the data has been physically written to the underlying hardware.
- `__O_DIRECT`
  - The `O_DIRECT` flag may impose alignment restrictions on the length and address of user-space buffers and the file offset of I/Os.
  - In Linux alignment restrictions vary by filesystem and kernel version and might be absent entirely.
  - However there is currently no filesystem-independent  interface  for an application to discover these restrictions for a given file or filesystem.  Some filesystems provide their own interfaces for doing so, for example the XFS_IOC_DIOINFO operation in xfsctl(3).

Pour purger le *page cache*, exécuter la commande suivante:

```bash
sync; echo 1 > /proc/sys/vm/drop_caches
```

> [!WARNING]
> Penser à purger le *page cache* avant chaque mesure.

#### Analyse

Les courbes pour cette analyse se trouve dans le dossier `q3/`.

<!-- TODO: analyser les courbes -->

## Exercice 2 - Débit des lectures et écritures

Ici, on va reprendre l'exercice précédent afin de pouvoir mesurer:

- les débits **lectures** et **écritures**
- avec un mode d'accès **séquentiel** ou **aléatoire**.

Les courbes affichent chaque opération possible:

- lecture séquentielle
- lecture aléatoire
- écriture séquentielle
- écriture aléatoire

> [!IMPORTANT]
> Chaque opération est réalisée avec un fichier de 1Go.
> Avec le *page cache* est purgé avant chaque mesure.

### Analyse
<!-- TODO: add analysis -->

## Exercice 3 - Efficacité du préchargement du *Page Cache*

### 1. Accès en lecture séquentielle

<!-- TODO -->

### 2. Accès en lecture aléatoire

<!-- TODO -->

### 3. Détection du préchargement
<!-- TODO -->

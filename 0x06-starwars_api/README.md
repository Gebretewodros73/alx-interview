# 0x06-starwars_api

This directory contains scripts that interact with the Star Wars API to retrieve information about characters from the movies.

## More Info

To run the scripts, you'll need to have Node 10 and the `semistandard` package installed. You can set it up with the following commands:

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global
```

Additionally, you'll need the request module installed. You can do this with:

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters

**Mandatory**

Write a script that prints all characters of a Star Wars movie.

* The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name per line in the same order as the "characters" list in the /films/ endpoint
* You must use the Star wars API
* You must use the request module

Usage example:

```bash
$ ./0-starwars_characters.js 3
```

Output:

```bash
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

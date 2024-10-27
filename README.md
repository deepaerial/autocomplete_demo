# T9 Autocomplete

This project is a simple T9 autocomplete system. It reads a dictionary file and generates a T9 dictionary. The user can input a sequence of numbers and the system will return a list of words that can be generated from that sequence.

[![asciicast](https://asciinema.org/a/1WrTDOXUgJeBhCxqe5NmxvGwg.svg)](https://asciinema.org/a/1WrTDOXUgJeBhCxqe5NmxvGwg)

## Requirements

* Python 3.11
* [Poetry](https://python-poetry.org/) 

## Installation
Run command below to install the project and its dependencies:
```shell
$ poetry install
```
Or use docker to run project:
```shell
$ docker build -t t9-autocomplete .
$ docker run -it t9-autocomplete
```
All of these steps can be done by running the script:
```shell
$ ./run.sh
```
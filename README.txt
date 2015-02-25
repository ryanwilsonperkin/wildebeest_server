Wildebeest Web Service
===

This web service calls out to an external move generating program for a wildebeest game.
It is expected that the external program takes a sinle command line argument (board.txt) and creates several new files in the current working directory, each representing a new board configuration.

Installation
---

- Run "pip install web.py" (or equivalent) to install the web.py python module.
- Change the PROG_NAME global variable to the canonical pathname of the wildebeest executable
- Run "python server.py" to run the web server on localhost port 8080
- See the instructions on http://webpy.org/install for details on configuring web server gateway

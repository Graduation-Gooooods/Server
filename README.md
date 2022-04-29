# Server

## repo for developing server part

### lang: python, 3.10 version
### db  : MariaDB

### now: ard req to server "previous mode", than server send to ard p-mode. (UDP)
###      - app req to server "10 recent log", than server send to app 10-log. (HTTP - GET)
###      - app req to server "chmode" using HTTP GET, than server send to ard chmode. (POST)

### future work: ard create at server ard's data(passive, automatic, training) using UDP.
### app req to server NL order, than server run NLP algorithm and send to ard NL order.


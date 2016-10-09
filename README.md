# terminal_timekeeper
a minimalistic timekeeper in your terminal
compatible with timekeeper js

###requirements  
https://github.com/Robpol86/terminaltables  
`sudo pip install terminaltables`  
`sudo pip install requests` 

##usage  
| Command                              |     Result                                                             |
| -------------------------------------|------------------------------------------------------------------------|
| `python3 main.py -p Test -t Start`   | Starts new task named `Start` in project `Test`                        |
| `python3 main.py -l p`               | Lists all projects, that have been created                             |
| `python3 main.py -l t`               | Lists a few of the last tasks                                          |
| `python3 main.py -l t -c 50`         | Lists the last 50 tasks                                                |


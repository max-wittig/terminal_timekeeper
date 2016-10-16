# terminal_timekeeper
a minimalistic timekeeper in your terminal
compatible with timekeeper js

###requirements  
https://github.com/Robpol86/terminaltables  
`sudo pip install terminaltables`  
`sudo pip install requests` 

##usage  
| Command                                                  |     Result                                                             |
| ---------------------------------------------------------|------------------------------------------------------------------------|
| `python3 __main__.py -p Test -t Start`                   | Starts new task named `Start` in project `Test`                        |
| `python3 __main__.py -l p`                               | Lists all projects, that have been created                             |
| `python3 __main__.py -l t`                               | Lists a few of the last tasks                                          |
| `python3 __main__.py -l t -c 50`                         | Lists the last 50 tasks                                                |
| `python3 __main__.py -s show_latest_month <project_name>`| Runs script "show_latest_month" from script folder with parameter        

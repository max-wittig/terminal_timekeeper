# terminal_timekeeper
a minimalistic timekeeper in your terminal
compatible with timekeeper js

### setup virtualenv & install requirements
<pre>  
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
</pre>

### setup timekeeper as softlink be to run from anywhere
<pre>
sudo ln -s `pwd`/__main__.py /usr/bin/timekeeper
sudo chmod +x /usr/bin/timekeeper
</pre>

### sycing to your timekeeperServer
* Setup this PHP server: https://github.com/max-wittig/timekeeperServer
* Create a file named `server_info.json` with the file contents:
<pre>
{
  "url": "http://127.0.0.1:3000/timekeeperServer.php",
  "username": "testing",
  "password": "123"
}
</pre>

* Replace it with your data

## usage 
 
| Command                            | Result                                                            |
|------------------------------------|-------------------------------------------------------------------|
| `timekeeper -p Test -t Start`      | Starts new task named `Start` in project `Test`                   |
| `timekeeper -l p`                  | Lists all projects, that have been created                        |
| `timekeeper -l t`                  | Lists a few of the last tasks                                     |
| `timekeeper -l t -c 50`            | Lists the last 50 tasks                                           |
| `timekeeper -s show_latest_month ` | Runs script "show_latest_month" from script folder with parameter |

# channel downloader bot
A Discord bot that can be used to download all the messages from a channel.

## Installation
Installation is very simple.<br>
Make sure you have python3.11 installed, and then copy the directory to the main.py file<br>
(full path, starting at C:/ or whatever)

Then run the following command in the terminal:
```
python3.11 -m venv venv
```
(IF that doesn't work, find the full path to your python executable and replace python3.11 with the full path)<br>

This will create a virtual environment in the directory.<br>
Then run the following command:
```
venv\Scripts\activate
```
Then run
```
pip install -r requirements.txt
```
Then finally to start the bot and run the setup script, run:
```
python main.py -O
```

## Usage
The bot has 1 command.<br>
"Download"<br>
This command downloads all the messages from the last 5 years of the channel that the command is run in.<br>
The messages are saved in 'downloaded/channel-*channel id here*'

They are saved in the format of `user id - message id - timestamp: message content`<br>
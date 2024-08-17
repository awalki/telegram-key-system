# How to install?

Install Node.js 20 LTS - https://nodejs.org/en<br/>
Install latest python version - https://www.python.org/<br/>
Install SQLiteStudio for database managment - https://sqlitestudio.pl/<br/>

## Clone Repo
```
git clone https://github.com/awalking/telegram-key-system.git
```

## Open cmd in the root dir
```npm i -g yarn
yarn install
pip install -r requirements.txt

yarn keygen
```

## Provide your BOT_TOKEN to .env<br/>You can get it here - https://t.me/BotFather
```
BOT_TOKEN = YOUR BOT_TOKEN
```

## Run setup_win.bat first, after successfull installation open run_win.bat
> You can get keys in keys.db (double click the file and SQLiteStudio should be opened)<br/>Provide that key to telegram bot

That's all. If all steps were correct your bot should be work.

## Credits:
- aiogram
- aiogram-dialog

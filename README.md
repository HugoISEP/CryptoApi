# CryptoAPI project

## Setup
> Add a config.ini file with the bot base url:
```
[DEFAULT]
bot_base_url = <YOUR_BOT_BASE_URL>
[AUTHENTICATION]
API_KEY = <YOUR_API_KEY>
API_KEY_NAME = <YOUR_API_KEY_NAME>
```

> Download the firebase config file *firebase-project-credentials.json* and put it at the root of the project

## launch the project
``` uvicorn app.main:app --reload --port 8001```

# Rest api testing GUI application written in Python tkinter framework

<img src=pic.PNG alt="Python tkinter application image">

## Architecture

```mermaid
flowchart LR
    A(client) --> B(view)
    B --> C(controller)
    C --> D(model)
    D --> |POST| E(OAuth 2.0 server)
    E --> |OK| D
    D --> |api call| F(endpoint)
    F --> |OK| D
    D --> C
    C --> B
    B --> A
```

## Execution

```bash
gh repo clone sauravdwivedi/Apps
cd Apps && cd Python && cd api-testing-gui-app
python3 -m venv venv
source venv/bin/activate
brew install python-tk
pip3 install -r requirements.txt
source env.list
python3 app.py
```

## Alias

```bash
alias apitest='source <path-to-directory>/env.list && python3 <path-to-directory>/app.py'
```
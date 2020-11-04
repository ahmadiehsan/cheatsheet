# Cheatsheet

### Prerequisites

1. `sudo apt install make` for below actions:

    - deploy
    - docker
    - elasticsearch
    - kubernetes
    - postgres
    - python

2. `sudo apt-get install wkhtmltopdf` for scrum qa action
3. `sudo apt install xclip` for scrum points action

### Usage

```
git clone <this repo>
cd leading-tools
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python runner.py help
```

# chatgpt-python-cli
Simple chat gpt cli allowing users to communicate directly in terminal via python with CHAT GPT API, 
can take 'code' output and create files for them.

Prerequisite: 

```
pip install openai
or
python -m pip install openai
```

Each time the gpt response contains code (denoted by triple backtick) the code simply finds all the code snippets
using regex and offers the user to output them to a file.

# TO SETUP:

git clone onto your machine
create some sort of executable ie. shell/batch/powershell script, making sure either you set an 'OPENAI_KEY' environment variable in the script, or globally on your machine.

Make sure the script contains (Something along the lines of:)


```
# This file would be called something like 'chatgpt.sh' or something

#!/bin/bash

# set environment variable here
/usr/bin/python3 /home/ubuntu/chatgpt-python-cli

```

Just confirm that it is executable (on linux) with

```

$ sudo chmod +x chatgpt.sh

```

simply make sure the file is in the path, then simply run chatgpt in your terminal!

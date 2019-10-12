## Introduction

CatchMail can be used to find some email addresses! 

```
(py3) λ python CatchMail.py -d example.com                  
   ______      __       __    __  ___      _ __
  / ____/___ _/ /______/ /_  /  |/  /___ _(_) /
 / /   / __ `/ __/ ___/ __ \/ /|_/ / __ `/ / /
/ /___/ /_/ / /_/ /__/ / / / /  / / /_/ / / /
\____/\__,_/\__/\___/_/ /_/_/  /_/\__,_/_/_/   
                                                        
                                                        
>>> Hello 0kee                                        
>>> Successful.                                         
>>> Your balance : 2700                                 
>>> Got 100 email:                                      
                                                        
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com
xxxx@example.com                                      
```

## Usage

1. Write Token to `0kee.token`.

2. send query. 
```                                      
(py3) CatchMail.py                   
        Usage: CatchMail.py <domain> s.types                         
        ./python3 CatchMail.py -d example.com             
        .python3 CatchMail.py -d example.com -o out.json                  
                                                                  
.python3 CatchMail.py -d example.com -l 200                                                          
  Options:           
  -h, --help show this help message and exit                                                   
  -v, --version                                      
                        -d DOMAIN, --domain-domain                           
  domain of email                                         
                        -l LIMIT, --LIMIT-LIMIT Limit number of results.   
  (default: 100)                                           
                        -o OUT, --outfile-OUT                          
output into file file

```

## Show

![img](https://raw.githubusercontent.com/0Kee-Team/CatchMail/master/cmd.gif)
## 介绍
CatchMail可用于收集邮箱地址.

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



## 使用

1. 将Token写入`0kee.token`文件.

2. 使用脚本
```
(py3) λ python CatchMail.py                                      
Usage:  CatchMail.py <domain> [type] [options]                   
        ./python3 CatchMail.py -d example.com                         
        ./python3 CatchMail.py -d example.com -o out.json             
        ./python3 CatchMail.py -d example.com -l 200                  
                                                                  
                                                                  
Options:                                                          
  -h, --help            show this help message and exit           
  -v, --version                                                   
  -d DOMAIN, --domain=DOMAIN                                      
                        domain of email                           
  -l LIMIT, --limit=LIMIT                                         
                        limit number of results. [default: 100]   
  -o OUT, --outfile=OUT                                           
                        output into file                          
```


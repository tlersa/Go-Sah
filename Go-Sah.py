from googlesearch import search
import os

try:
    from googlesearch import search
    import os
except ModuleNotFoundError:
    os.system("pip install beautifulsoup4")
    os.system("pip install googlesearch")
    os.system("pip install os")

    os.system("clear")

#--------------------------------
Black = "\033[1;30m"       #Black
Red = "\033[1;31m"         #Red
Green = "\033[1;32m"       #Green
Yellow = "\033[1;33m"      #Yellow
Blue = "\033[1;34m"        #Blue
Purple = "\033[1;35m"      #Purple
Cyan = "\033[1;36m"        #Cyan
White = "\033[1;37m"       #White
Gray = "\033[1;39m"        #Gray
DarkRed = "\033[2;31m"     #Dark Red
DarkBlue = "\033[2;34m"    #Drak Blue
DarkPink = "\033[2;35m"    #Dark Pink
DarkCyan = "\033[2;36m"    #Dark Cyan
#--------------------------------

print("""\033[1;32m
  _.--,-```-.    
 /    /      '.  
/  ../         ; 
\  ``\  .``-    '
 \ ___\/    \   :
       \    :   |
       |    ;  . 
      ;   ;   :  
     /   :   :   
     `---'.  |   
      `--..`;    
    .--,_        
    |    |`.     
    `-- -`, ;    
      '---`" """)
print("\033[1;37mThis Tool Was Programmed By : TLER AL-BISHI \nWebsite For All Accs : \033[1;34mhttps://linktr.ee/tler.sa")
print("\033[1;37m- "*25)

searchh = input("\033[1;37mWhat Do You Want To Search For? \033[1;31m")

result = input("\033[1;37mHow Many Result You Want? \033[1;31m")

for i in search(searchh, tld="co.in", num=int(result), stop=int(result)):
  print(i)
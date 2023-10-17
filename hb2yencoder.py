import base64;

greeting = """Dear Bob,

All the best to your 100th birthday! 
For the next 100 we wish you good health, prosperity and always a smile on your face.

more nice words, more nice words, some more nice words

All the best, love Alice
"""


picture = """
   ,-.
   | |
   | "--.  ,--.-.,-.--. ,-.--. ,-. ,-.
   | ,-. \/ ,-. || ,-. \| ,-. \| | | |
   | | | |\ `-' || `-' /| `-' /| `-' |
   `-' `-' `--'-'| .--' | .--'  `--. |
                 | |    | |        | |
                 `-'    `-'        `-'
,-.     _       ,-.  ,-.        ,-.
| |    (_)      | |_ | |        | |
| "--. ,-.,-.--.|  _)| "--.  ,--" | ,--.-.,-. ,-.
| ,-. \| || ,-./| |  | ,-. \/ ,-. |/ ,-. || | | |
| `-' /| || |   | |  | | | |\ `-' |\ `-' || `-' |
"-'--' `-'`-'   `-'  `-' `-' `--'-' `--'-' `--. |
                                              | |
                                              `-

"""


greetingreversed = greeting[::-1]
greetingbytes = bytearray(greetingreversed,'utf-8')
greetingbase64 =  base64.b64encode(greetingbytes)

print('Greeting message string:')
print(greetingbase64)
print()

picturebytes = bytearray(picture,'utf-8')
picturebase64 =  base64.b64encode(picturebytes)

print('Picture string:')
print(picturebase64)

def read_quotes():
    quotes=open("D:\Stages.txt")
    content=quotes.read()
    print(content)
    quotes.close()

read_quotes()

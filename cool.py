#from flask import Flask

#app = Flask (__name__)

#@app.route("/")
#def index():
#    return "Hello, world!"

fname = input("Enter file name")
file = open(fname)
tot = 0
count = 0
for line in file:
    for wrd in line.split():
        tot += wrd if isinstance(wrd, float) is True else 0
        count += 1
ans = tot/count
print("Average:",ans)
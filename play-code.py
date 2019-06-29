books=[
    {"id":1, "title":"Book A", "color": "blue", "year": 1901},
    {"id":2, "title":"Book B", "color": "red", "year": 1957},
    {"id":3, "title":"Book C", "color": "blue", "year": 1988},
    {"id":4, "title":"Book D", "color": "green", "year": 1923},
    {"id":5, "title":"Book E", "color": "yellow", "year": 2017}
]

a=[]

a = [books["color"] for books in books]

print (a)

b = []
b= [books["year"] for books in books]

c=[]
c = [i for i in b if i>1950]
breakpoint ()
#this script will test the working of HDPMSD

from HDPMSD import hdpmsd

a = hdpmsd.HDPMSD()

#filecheck

a.writeFile("myfile.txt", "Hello! World", 0)
print(a.readFile("myfile.txt", 0))
print(a.filesize("myfile.txt"))
a.deleteFile("myfile.txt")

#list

ls = "[\"Item1\", \"Item2\"]"
print(a.readList(ls, 0))
x = a.writeList(ls, "Item3")
print(x)
print(a.deleteListItem(x, 2))
print(a.listSize(x))

#json

js = "{\"Name\": \"Mayukh\"}"
print(a.readNode(js, 'Name'))
print(a.writeNode(js, {"Roll": 39}))
print(a.deleteNode(a.writeNode(js, {"Roll": 39}), 'Roll'))
print(a.json_size(js))
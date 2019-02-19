def openfile(path):
    filepath = path;
    file = open(filepath, "r+");
    a = file.readlines();
    file.close();
    print(a[0]);
openfile("a.txt")
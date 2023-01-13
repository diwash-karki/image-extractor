imgs = ''
with open("imagelist.txt", "r") as file:
    imgs =  file.read()
    file.close()

imgs = imgs.split('\n')
print(len(imgs))
cleanImgs = list(dict.fromkeys(imgs))

imgString = "".join(i+'\n' for i in cleanImgs)

print(imgString)

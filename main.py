from PIL import Image,ImageFilter
#with Image.open("Mops.jpg")as file:
    #file.show()
    #print("Розмір фото:",file.size)
    #print("Формат фото:",file.format)
    #print("Колірна модель:",file.mode)
    #gray=file.convert("L")
    #gray.save("gray.jpg")
    #blured=file.filter(ImageFilter.BLUR)
    #blured.save("blured.jpg")
    #up=file.transpose(Image.ROTATE_180)
    #up.save("up.jpg")
    #mirror=file.transpose(Image.FLIP_LEFT_RIGHT)
    #mirror.save("mirror.jpg")
    #pic_contrast = ImageEnhance.contrast(file)
    #pic_contrast=pic_contrast.enhance(1.5)
    #pic_contrast.save("pic_contrast.jpg")
class ImageEditor:
    def __init__(self,name):
        self.name=name
        self.original=""
        self.files=[]
        self.counter=1
    def open(self):
        try:
            self.original=Image.open
            self.files.append(self.original)
        except:
            print("Назва фаайлу вказана не вірно!")
    def do_left(self):
        left=self.original.transpose(Image.ROTATE_90)
        self.files.append(left)
        new=self.name.split(".")
        left.save(new[0]+str(self.counter)+"."+[1])
        self.counter+=1

    def do_croppped(self):
        box=(250,100,750,400)
        cropped=self.original.crop(box)
        self.files.append(cropped)
        new=self.name.split(".")
        cropped.save(new[0]+str(self.counter)+"."+[1])
        self.counter+=1

image=ImageEditor("Mops.jpg")
image.open()
image.do_left()
image.do_croppped()
for file in image.files:
    file.show()

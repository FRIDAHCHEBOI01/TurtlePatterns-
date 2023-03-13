from PIL import Image

img_1 = Image.open("C:/Users/user/Downloads/henryV.jpeg")
img_1.show()
print(img_1.size) #(1616, 2256)
resized_img1 = img_1.resize((500,200))
resized_img1.show()

#creates a black and white version of the image
grayscale_img_1 = img_1.convert('L')
grayscale_img_1.show()

#creates a transpose of the image
trnsImg_1 = img_1.transpose(Image.FLIP_LEFT_RIGHT)
trnsImg_1.show()

'''
#Create a thumbnail of the image
img_1.thumbnail((200,200))
img_1.show()
print(img_1.size)
'''
w, h = img_1.size

img_2 = img_1.resize((w//2,h//2))
img_2.show()

grayscale_img_1.save('C:/Users/user/OneDrive - Ashesi University/Desktop/Python files/blckhenryV.jpeg')
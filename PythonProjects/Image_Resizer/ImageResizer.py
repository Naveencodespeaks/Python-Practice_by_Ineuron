# install pillow if you haven't
# import pillow
# open up the image we want to resize using python
# print the current size we want to change it to
# save the new resized image


from PIL import Image
def resize_image(size1, side2):
    image = Image.open('krsna-the-cowheard-boys-taking-prasadam3.png')
    image1 = Image.open('krishna123.jpg')
    print(f"Current size : {image.size}")
    print(f"Current size : {image1.size}")

    resized_image = image.resize((size1,side2))
    resized_image.save('krsna-the-cowheard-boys-taking-prasadam3-500' + str(size1) +'.jpg')

size1 = int(input('Enter Width: '))
size2 = int(input('Enter length: '))
resize_image(200,300)
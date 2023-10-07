from PIL import Image, ImageDraw, ImageFont

#resim dosyası

image_path ="first.jpg"
image = Image.open(image_path)

draw = ImageDraw.Draw(image)

text ="Hello World .. "
font_path="DejaVuSans-Bold.ttf" 
font_size=32    
font = ImageFont.truetype(font_path,font_size)

position = (230,100) #kordinat değerleri

text_color =(255,255,255)
draw.text(position, text ,fill=text_color, font=font)


output_photo = "output.jpg"
image.convert('RGB').save(output_photo)
image.show()


from PIL import Image
from reportlab.pdfgen import canvas

def crop_image(input_path1,input_path2,output_path, left1, top1, right1, bottom1,left2,top2,right2,bottom2,text1,text2,text3,left3,top3,right3,bottom3):
    # Open the image file
    img1 = Image.open(input_path1)
    img2 = Image.open(input_path2)
    img3 = Image.open(input_path2)

    # Crop the image
    cropped_img1 = img1.crop((left1, top1, right1, bottom1))
    cropped_img2 = img2.crop((left2,top2,right2,bottom2))
    cropped_img3 = img3.crop((left3,top3,right3,bottom3))

    # Save the cropped image to a temporary file (PNG format)
    temp_image_path1 = 'temp.png'
    temp_image_path2 = 'temp2.png'
    temp_image_path3 = 'temp3.png'

    cropped_img1.save(temp_image_path1)
    cropped_img2.save(temp_image_path2)
    cropped_img3.save(temp_image_path3)


    # Create a PDF and add the cropped image to it
    pdf_canvas = canvas.Canvas(output_path)
    pdf_canvas.drawImage(temp_image_path1,5,350, width=600, height=400)
    pdf_canvas.drawImage(temp_image_path2,0,715,width=870, height=130)
    pdf_canvas.drawImage(temp_image_path3,0,0,width=595, height=180)

     # Add text to the PDF
    pdf_canvas.setFont("Helvetica", 16)
    pdf_canvas.drawString(9,720, text1)
    # pdf_canvas.drawString(9, 620, text2)
    # pdf_canvas.drawString(9,510, text3)

    pdf_canvas.save()

    # Remove the temporary image file
    import os
    os.remove(temp_image_path1)
    os.remove(temp_image_path2)
    os.remove(temp_image_path3)

# Example usage:
input_image_path1 = 'city.jpg'
input_image_path2 = 'logo.jpg' 
output_pdf_path ='pdf_extracted/testesttest.pdf'

text1 = "Passenger Information"
text2 = "Flight Information"
text3 = "Price"

# Define the coordinates of the area to be cropped (left, top, right, bottom)
crop_coordinates1 = (20, 220, 1250, 870)
crop_coordinates2 = (0,10,900,180)
crop_coordinates3 = (0,1000,900,1280)

crop_image(input_image_path1,input_image_path2, output_pdf_path, *crop_coordinates1,*crop_coordinates2,text1,text2,text3,*crop_coordinates3)

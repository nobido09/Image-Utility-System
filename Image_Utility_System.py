import streamlit as st
import matplotlib
from PIL import Image,ImageFilter,ImageEnhance,ImageDraw,ImageOps

def show_image(img, imgbox):
    return imgbox.image(img,use_column_width=True)

def gen_sidebar(img,imgbox):
    st.sidebar.title("Start Editing!")
    img_t=img
    options=["Resize","Tune","Filter","Rotate","Border","Flip"]
    choice=st.sidebar.radio("Choose your option",options)           
    if choice=="Resize":
        st.sidebar.header("Resize")
        st.sidebar.text(f'Size of the image: {img.width} x {img.height}')
        w=st.sidebar.text_area("Enter Width of the image: ")
        h=st.sidebar.text_area("Enter Height of the image: ")
        if w and h:
            w=type(int(w))
            h=type(int(h))
            if st.sidebar.button("Show"):
                img_t=img.resize(size=(w,h))
                show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)
    if choice=="Tune":
        st.sidebar.header("Tune")
        bright=st.sidebar.slider("Brightness",-10.0,10.0,0.0,0.5)
        contra=st.sidebar.slider("Contrast",-10.0,10.0,0.0,0.5)
        sharp=st.sidebar.slider("Sharpness",-10.0,10.0,0.0,0.5)
        col=st.sidebar.slider("Color",-10.0,10.0,0.0,0.5)
        if bright:
            img_t=ImageEnhance.Brightness(img)
            img_t=img_t.enhance(bright)
            show_image(img_t,imgbox)
        if contra:
            img_t=ImageEnhance.Contrast(img)
            img_t=img_t.enhance(contra)
            show_image(img_t,imgbox)
        if sharp:
            img_t=ImageEnhance.Sharpness(img)
            img_t=img_t.enhance(sharp)
            show_image(img_t,imgbox)
        if col:
            img_t=ImageEnhance.Color(img)
            img_t=img_t.enhance(cola)
            show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)
    if choice=="Rotate":
        st.sidebar.header("Rotate")
        val=st.sidebar.slider("Degree of Rotation",0,360,0,5)
        if st.sidebar.button("Show"):
            img_t=img.rotate(val)
            show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)
    if choice=="Filter":
        st.sidebar.header("Filter")
        filters=["Blur","Pencil Sketch","Detail","Edge Enhance","Black & White","Emboss","White Marker Sketch","Sharpen","Smooth","Sepia","Solarize","Grayscale","Negative"]
        opt=st.sidebar.radio("Choose filter",filters)
        if opt=="Blur":
            img_t=img.filter(ImageFilter.BLUR)
            show_image(img_t,imgbox)
        if opt=="Pencil Sketch":
            img_t=img.filter(ImageFilter.CONTOUR)
            show_image(img_t,imgbox)
        if opt=="Detail":
            img_t=img.filter(ImageFilter.DETAIL)
            show_image(img_t,imgbox)
        if opt=="Edge Enhance":
            img_t=img.filter(ImageFilter.EDGE_ENHANCE)
            show_image(img_t,imgbox)
        if opt=="Black & White":
            img_t=img.convert("L")
            show_image(img_t,imgbox)
        if opt=="Emboss":
            img_t=img.filter(ImageFilter.EMBOSS)
            show_image(img_t,imgbox)
        if opt=="White Marker Sketch":
            img_t=img.filter(ImageFilter.FIND_EDGES)
            show_image(img_t,imgbox)    
        if opt=="Sharpen":
            img_t=img.filter(ImageFilter.SHARPEN)
            show_image(img_t,imgbox)
        if opt=="Smooth":
            img_t=img.filter(ImageFilter.SMOOTH)
            show_image(img_t,imgbox)
        if opt=="Sepia":
            whitish = (255, 240, 192)
            sepia = make_sepia_palette(whitish)
            bw=img.convert("L")
            bw.putpalette(sepia)
            img_t=bw.convert("RGB")
            show_image(img_t,imgbox)
        if opt=="Solarize":
            img_t=ImageOps.solarize(img)
            show_image(img_t,imgbox)
        if opt=="Grayscale":
            img_t=ImageOps.grayscale(img)
            show_image(img_t,imgbox)
        if opt=="Negative":
            img_t=ImageOps.invert(img)    
            show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)
    if choice=="Border":
        st.sidebar.header("Border")
        bor=st.sidebar.text_area("Enter the width of the border(in pixels)")
        col_opt=gen_options()
        col=st.sidebar.selectbox("Choose the color for border",col_opt)
        if st.sidebar.button("Show"):
            if bor:
                bor=int(bor)
                img_t=ImageOps.expand(img,border=bor,fill=col)
                show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)       
    if choice=="Flip":
        st.sidebar.header("Flip")
        ch=st.sidebar.radio("Choose:",["Horizontally","Vertically"])
        if ch=="Horizontally":
            img_t=ImageOps.mirror(img)
            show_image(img_t,imgbox)
        if ch=="Vertically":
            img_t=ImageOps.flip(img)
            show_image(img_t,imgbox)
        if st.sidebar.button("OK"):
            img=img_t
            show_image(img,imgbox)
        if st.sidebar.button("Back"):
            show_image(img,imgbox)        
    if st.sidebar.button("Save"):
        name=st.text_area("Enter file name")
        if name:
            if img.save(f"Edited\{name}.jpg"):
                st.success("Image saved!")
            else:
                st.error("Couldn't save file!")


def gen_options():
    rgb_colors=[]
    colors=[]
    for name in matplotlib.colors.cnames.items():
        rgb_colors.append(name)
    for i in rgb_colors:
        colors.append(i[0])
    return colors

    
def make_sepia_palette(color):
    palette = []
    r, g, b = color
    for i in range(255):
        palette.extend((r*i//255, g*i//255, b*i//255))   
    return palette


st.title("IMAGE UTILITY SYSTEM")

image=st.file_uploader("Drag or Browse Image",type=["jpeg","jpg"])
if image:
    img=Image.open(image)
    imgbox = st.empty()
    imgbox.image(img,use_column_width=True)
    gen_sidebar(img, imgbox)

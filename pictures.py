





from tkinter import *
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
from tkinter.ttk import Notebook,Progressbar,Combobox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os



class Picture:

    def __init__(self,root):
        self.root=root
        self.root.title("Pictures Downloads")
        self.root.geometry("700x605")
        self.root.iconbitmap("songs.ico")
        self.root.resizable(0,0)


        pictures=StringVar()
        limits=IntVar()
        search_url=StringVar() 
        pictures_name=StringVar()
        pictures_url_single=StringVar()


#============================Hover the button===========================================



        def on_enter0(e):
            but_search['background']="black"
            but_search['foreground']="cyan"  
        def on_leave0(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"


        def on_enter1(e):
            but_scrape_pictures['background']="black"
            but_scrape_pictures['foreground']="cyan"  
        def on_leave1(e):
            but_scrape_pictures['background']="SystemButtonFace"
            but_scrape_pictures['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_clear_list['background']="black"
            but_clear_list['foreground']="cyan"  
        def on_leave2(e):
            but_clear_list['background']="SystemButtonFace"
            but_clear_list['foreground']="SystemButtonText"



        def on_enter3(e):
            but_download_pictures_all['background']="black"
            but_download_pictures_all['foreground']="cyan"  
        def on_leave3(e):
            but_download_pictures_all['background']="SystemButtonFace"
            but_download_pictures_all['foreground']="SystemButtonText"

            

        def on_enter4(e):
            but_download_pictures['background']="black"
            but_download_pictures['foreground']="cyan"  
        def on_leave4(e):
            but_download_pictures['background']="SystemButtonFace"
            but_download_pictures['foreground']="SystemButtonText"

        def on_enter5(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave5(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        def on_enter11(e):
            but_user_manual['background']="black"
            but_user_manual['foreground']="cyan"  
        def on_leave11(e):
            but_user_manual['background']="SystemButtonFace"
            but_user_manual['foreground']="SystemButtonText"

            

        def on_enter12(e):
            but_websites['background']="black"
            but_websites['foreground']="cyan"  
        def on_leave12(e):
            but_websites['background']="SystemButtonFace"
            but_websites['foreground']="SystemButtonText"
            


        def on_enter13(e):
            but_Source['background']="black"
            but_Source['foreground']="cyan"  
        def on_leave13(e):
            but_Source['background']="SystemButtonFace"
            but_Source['foreground']="SystemButtonText"



#======================================================================================

        def websites():
                root1=Toplevel(self.root)
                root1.title("Websites")
                root1.geometry("400x400")
                root1.resizable(0,0)

                frame_web=Frame(root1,width=400,height=400,relief="ridge",bd=4)
                frame_web.place(x=0,y=0)

                mess_1=Label(frame_web,text="step 1:https://stocksnap.io",anchor="w",font=('times new roman',11,'bold'))
                mess_1.place(x=10,y=25)

                mess_2=Label(frame_web,text="step 2: Enjoy the sites",anchor="w",font=('times new roman',11,'bold'))
                mess_2.place(x=10,y=45)

                root1.mainloop()


        def usermanual():

            root2=Toplevel(self.root)
            root2.title("User Manual")
            root2.geometry("400x400")
            root2.resizable(0,0)

            frame_um=Frame(root2,width=400,height=400,relief="ridge",bd=4)
            frame_um.place(x=0,y=0)

            lab_heading=Label(frame_um,text="User Manual",font=('times new roman',13,'bold'))
            lab_heading.place(x=130,y=0)

            mess_1=Label(frame_um,text="step 1: Choose any categeory from box ",anchor="w",font=('times new roman',11,'bold'))
            mess_1.place(x=10,y=25)

            mess_2=Label(frame_um,text="step 2: Select the limit of pictures you want",anchor="w",font=('times new roman',11,'bold'))
            mess_2.place(x=10,y=45)

            mess_3=Label(frame_um,text="step 3: Click the Scrape button",anchor="w",font=('times new roman',11,'bold'))
            mess_3.place(x=10,y=65)

            mess_4=Label(frame_um,text="step 4: Go to download Pictures tab ",anchor="w",font=('times new roman',11,'bold'))
            mess_4.place(x=10,y=85)

            mess_5=Label(frame_um,text="step 5: Write the folder name to save images  ",anchor="w",font=('times new roman',11,'bold'))
            mess_5.place(x=10,y=105)

            mess_6=Label(frame_um,text="step 6: Click on download button   ",anchor="w",font=('times new roman',11,'bold'))
            mess_6.place(x=10,y=125)

            mess_7=Label(frame_um,text="step 7: It will save your photo in given folder  ",anchor="w",font=('times new roman',11,'bold'))
            mess_7.place(x=10,y=145)

            mess_8=Label(frame_um,text="step 8: To download a single photo copy single url  ",anchor="w",font=('times new roman',11,'bold'))
            mess_8.place(x=10,y=165)

            mess_9=Label(frame_um,text="step 9: paste the url in download Pictures tab  ",anchor="w",font=('times new roman',11,'bold'))
            mess_9.place(x=10,y=185)

            mess_10=Label(frame_um,text="step 10: Give the name you want  ",anchor="w",font=('times new roman',11,'bold'))
            mess_10.place(x=10,y=205)

            mess_11=Label(frame_um,text="step 11: Click on download_single button  ",anchor="w",font=('times new roman',11,'bold'))
            mess_11.place(x=10,y=225)

            mess_12=Label(frame_um,text="step 12: To Search any images write into image field  ",anchor="w",font=('times new roman',11,'bold'))
            mess_12.place(x=10,y=245)

            mess_13=Label(frame_um,text="step 13: Select the limit of images   ",anchor="w",font=('times new roman',11,'bold'))
            mess_13.place(x=10,y=265)

            mess_14=Label(frame_um,text="step 14: Click on Search button   ",anchor="w",font=('times new roman',11,'bold'))
            mess_14.place(x=10,y=285)

            root2.mainloop()


        def Sourcecode():
            root3=Toplevel(self.root)
            root3.title("Source Code")
            root3.geometry("400x400")
            root3.resizable(0,0)

            frame_sc=Frame(root3,width=400,height=400,relief="ridge",bd=4)
            frame_sc.place(x=0,y=0)

            root3.mainloop()



            


#======================scrappting images from website===================================================#

            



        def scrape_pictures():
            try:
                with open("C:\\TEMP\\pictures.txt","w") as f:
                    if pictures.get()=="Nature":
                        url="https://stocksnap.io/search/nature"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    if pictures.get()=="Business":
                        url="https://stocksnap.io/search/business"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                                
                    
                    if pictures.get()=="Beach":
                        url="https://stocksnap.io/search/beach"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    if pictures.get()=="Wallpapers":
                        url="https://stocksnap.io/search/wallpaper"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Love":
                        url="https://stocksnap.io/search/love"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Flower":
                        url="https://stocksnap.io/search/flower"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="People":
                        url="https://stocksnap.io/search/people"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Girl":
                        url="https://stocksnap.io/search/girl"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Food":
                        url="https://stocksnap.io/search/food"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Sad":
                        url="https://stocksnap.io/search/sad"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Computer":
                        url="https://stocksnap.io/search/computer"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Office":
                        url="https://stocksnap.io/search/office"
                        s = requests.Session()
                        search_url.set(url)
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Happy":
                        url="https://stocksnap.io/search/happy"
                        s = requests.Session()
                        search_url.set(url)
                        response= s.get(url)                       
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Woman":
                        url="https://stocksnap.io/search/woman"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="City":
                        url="https://stocksnap.io/search/city"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Couple":
                        url="https://stocksnap.io/search/couple"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Family":
                        url="https://stocksnap.io/search/family"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Summer": 
                        url="https://stocksnap.io/search/summer"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Black and white":   
                        url="https://stocksnap.io/search/black+and+white"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Coffee":
                        url="https://stocksnap.io/search/coffee"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Design": 
                        url="https://stocksnap.io/search/design"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Travel": 
                        url="https://stocksnap.io/search/travel"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Car": 
                        url="https://stocksnap.io/search/car"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Man": 
                        url="https://stocksnap.io/search/man"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Women":
                        url="https://stocksnap.io/search/women"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Dog":
                        url="https://stocksnap.io/search/dog"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Fashion":
                        url="https://stocksnap.io/search/fashion"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Book":
                        url="https://stocksnap.io/search/book"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Fitness":
                        url="https://stocksnap.io/search/fitness"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Friends":
                        url="https://stocksnap.io/search/friends"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Music":
                        url="https://stocksnap.io/search/music"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Money":
                        url="https://stocksnap.io/search/money"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="School":
                        url="https://stocksnap.io/search/school"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="House":
                        url="https://stocksnap.io/search/house"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Water":
                        url="https://stocksnap.io/search/water"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Work":
                        url="https://stocksnap.io/search/work"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Spring":
                        url="https://stocksnap.io/search/spring"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Flowers":
                        url="https://stocksnap.io/search/flowers"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Laptop":
                        url="https://stocksnap.io/search/laptop"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Health":
                        url="https://stocksnap.io/search/health"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Meeting":
                        url="https://stocksnap.io/search/meeting"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Wedding":
                        url="https://stocksnap.io/search/wedding"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Baby":
                        url="https://stocksnap.io/search/baby"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Art":
                        url="https://stocksnap.io/search/art"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Party":
                        url="https://stocksnap.io/search/party"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Beauty":
                        url="https://stocksnap.io/search/beauty"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Sky":
                        url="https://stocksnap.io/search/sky"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Phone":
                        url="https://stocksnap.io/search/phone"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Building":
                        url="https://stocksnap.io/search/building"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Technology":
                        url="https://stocksnap.io/search/technology"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Shopping":
                        url="https://stocksnap.io/search/shopping"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Home":
                        url="https://stocksnap.io/search/home"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Team":
                        url="https://stocksnap.io/search/teame"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Background":
                        url="https://stocksnap.io/search/background"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Sunset":
                        url="https://stocksnap.io/search/sunset"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Yoga":
                        url="https://stocksnap.io/search/yoga"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Forest":
                        url="https://stocksnap.io/search/forest"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Road":
                        url="https://stocksnap.io/search/road"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Fall":
                        url="https://stocksnap.io/search/fall"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Abstract":
                        url="https://stocksnap.io/search/abstract"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Sport":
                        url="https://stocksnap.io/search/sport"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Construction":
                        url="https://stocksnap.io/search/construction"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Light":
                        url="https://stocksnap.io/search/light"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Sea":
                        url="https://stocksnap.io/search/sea"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Wine":
                        url="https://stocksnap.io/search/wine"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Child":
                        url="https://stocksnap.io/search/child"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Study":
                        url="https://stocksnap.io/search/study"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Smile":
                        url="https://stocksnap.io/search/smile"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Kids":
                        url="https://stocksnap.io/search/kids"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Mountain":
                        url="https://stocksnap.io/search/mountain"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Hand":
                        url="https://stocksnap.io/search/hand"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Tree":
                        url="https://stocksnap.io/search/tree"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Cat":
                        url="https://stocksnap.io/search/cat"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Kitchen":
                        url="https://stocksnap.io/search/kitchen"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")



                    if pictures.get()=="Wall":
                        url="https://stocksnap.io/search/wall"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")
 

                    if pictures.get()=="Space":
                        url="https://stocksnap.io/search/space"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Wood":
                        url="https://stocksnap.io/search/wood"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Writing":
                        url="https://stocksnap.io/search/writing"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Kid":
                        url="https://stocksnap.io/search/kid"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Landscape":
                        url="https://stocksnap.io/search/landscape"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Books":
                        url="https://stocksnap.io/search/books"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Green":
                        url="https://stocksnap.io/search/green"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Architecture":
                        url="https://stocksnap.io/search/architecture"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Sun":
                        url="https://stocksnap.io/search/sun"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Desk":
                        url="https://stocksnap.io/search/desk"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Mobile":
                        url="https://stocksnap.io/search/mobile"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Beer":
                        url="https://stocksnap.io/search/beer"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Restaurant":
                        url="https://stocksnap.io/search/restaurant"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Creative":
                        url="https://stocksnap.io/search/creative"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Cake":
                        url="https://stocksnap.io/search/cake"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Running":
                        url="https://stocksnap.io/search/running"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="White":
                        url="https://stocksnap.io/search/white"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Garden":
                        url="https://stocksnap.io/search/garden"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Children":
                        url="https://stocksnap.io/search/children"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                    
                    if pictures.get()=="Camera":
                        url="https://stocksnap.io/search/camera"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Student":
                        url="https://stocksnap.io/search/student"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Gym":
                        url="https://stocksnap.io/search/gym"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Social media":
                        url="https://stocksnap.io/search/social+media"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Doctor":
                        url="https://stocksnap.io/search/doctor"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")


                    if pictures.get()=="Easter":
                        url="https://stocksnap.io/search/easter"
                        search_url.set(url)
                        s = requests.Session()
                        response= s.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                        for childrens in gather:
                            child=childrens.findChildren("img",recursive=True)
                            for childs in child:
                                f.write(childs.get("src"))
                                f.write("\n")

                with open("C:\\TEMP\\pictures.txt","r") as f:
                        texttopaste.insert("end",f.read())
            except:
                pass


        def download_all():
            try:               
                parent="C:/Users/SHREYAS/Desktop/shreyas python/Picturedownloader"
                dirs=pictures_name.get()
                path=os.path.join(parent,dirs)
                os.mkdir(path)
                site=search_url.get()
                response=requests.get(site)
                Soup=BeautifulSoup(response.text,"html.parser")
                gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                for childrens in gather:
                    child=childrens.findChildren("img",recursive=True)
                    urls=[images["src"] for images in child]
                    for url in urls:
                        try:                        
                            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                            if not filename:
                                print("Regex didn't match with the url: {}".format(url))
                                continue
                            with open(path+"/"+filename.group(1), 'wb') as f:
                                if 'https' not in url:
                                    urls = url
                                response = requests.get(url)
                                f.write(response.content)
                        except Exception as e:
                            print(e)
            except Exception as e:
                tkinter.messagebox.askretrycancel("Error","Network Error/=/ Enter the folder name")




        def download_single():
            try:
                if pictures_url_single.get()=="" and pictures_name.get()=="":
                    tkinter.messagebox.askretrycancel("Error","please enter picture url and picture save name")
                elif pictures_url_single.get()=="":
                    tkinter.messagebox.askretrycancel("Error","please enter picture url")
                elif pictures_name.get()=="":
                    tkinter.messagebox.askretrycancel("Error","Please enter picture name")
                else:
                    url=pictures_url_single.get()
                    r = requests.get(url)
                    with open('C:/Users/SHREYAS/Desktop/shreyas python/Picturedownloader/{}.jpg'.format(pictures_name.get()), 'wb') as f:
                        f.write(r.content)

            except:
                pass
        
        def clear_list():
            try:
                search_url.set("")
                pictures.set("select pictures")
                limits.set("1")
                os.remove("C:\\TEMP\\pictures.txt")
                texttopaste.delete(1.0,"end")
            except:
                tkinter.messagebox.showerror("error","File not found")


        def clear():
            try:
                pictures_url_single.set("")
                pictures_name.set("")
                #os.remove("C:\\TEMP\\songs.txt")
                #texttopaste.delete(1.0,"end")
            except:
                tkinter.messagebox.showerror("error","filenotfound")


        def Search():
            try:
                with open("C:\\TEMP\\pictures.txt","w") as f:
                    searchs=search_url.get()            
                    a=searchs.lower()
                    url="https://stocksnap.io/search/"+a
                    search_url.set(url)
                    s = requests.Session()
                    response= s.get(url)
                    Soup=BeautifulSoup(response.text,"html.parser")
                    gather=Soup.findAll("a",class_="photo-grid-preview",limit=limits.get())
                    for childrens in gather:
                        child=childrens.findChildren("img",recursive=True)
                        for childs in child:
                            f.write(childs.get("src"))
                            f.write("\n")


                with open("C:\\TEMP\\pictures.txt","r") as f:
                    texttopaste.insert("end",f.read())
            except Exception as e:
                print(e)
    


#======================frame==============================================#

        mainframe=Frame(self.root,width=700,height=605,relief="ridge",bd=4)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=695,height=250,bg="grey66",bd=4,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=695,height=320,bg="grey66",bd=4,relief="ridge")
        secondframe.place(x=0,y=250)

        thirdframe=Frame(mainframe,width=695,height=30,bg="white",bd=4,relief="ridge")
        thirdframe.place(x=0,y=570)

#==============================================================================#

        tabControl = Notebook(firstframe,width=683,height=214) 
  
        scrape_pictures = Frame(tabControl,background="grey57") 
        download_pictures = Frame(tabControl,background="grey87") 
        about = Frame(tabControl,background="grey77") 
        
        tabControl.add(scrape_pictures, text ='Scrape songs') 
        tabControl.add(download_pictures, text ='Download songs')
        tabControl.add(about, text ='About') 
        tabControl.place(x=0,y=0)

#==============================firstframe================================================#

        lab_pic=Label(scrape_pictures,text="Select Pictures ",font=('times new roman',12,'bold'),background="grey57",fg="white")
        lab_pic.place(x=20,y=10)
        

        list_pictures=["Nature","Business","Beach","Wallpapers","Love","Flower","People","Girl","Food","Sad","Computer","Office"\
                      ,"Happy","Woman","City","Couple","Family","Summer","Black and white","Coffee","Design","Travel","Car","Man",\
                        "Women","Dog","Fashion","Book","Fitness","Friends","Music","Money","School","House","Water","Work","Spring",\
                       "Flowers","Laptop","Health","Meeting","Wedding","Baby","Art","Party","Beauty","Sky","Phone","Building"\
                      ,"Technology","Shopping","Home","Team","Background","Sunset","Yoga","Forest","Road","Fall","Abstract","Sport",\
                        "Construction","Light","Sea","Wine","Child","Study","Smile","Kids","Mountain",\
                       "Hand","Tree","Cat","Kitchen","Wall","Space","Wood","Writing","Kid","Landscape","Books","Green","Architecture",\
                        "Sun","Desk","Mobile","Beer","Restaurant","Creative","Cake","Running","White","Garden","Children","Camera",\
                        "Student","Gym","Social media","Doctor","Easter"]
        list_pictures_combo=Combobox(scrape_pictures,values=list_pictures,font=('arial',10),width=19,state="readonly",textvariable=pictures)
        list_pictures_combo.set("select pictures")
        list_pictures_combo.place(x=150,y=10)


        lab_pic=Label(scrape_pictures,text="Select Limits ",font=('times new roman',12,'bold'),background="grey57",fg="white")
        lab_pic.place(x=350,y=10)
        

        list_limit=list(range(1,101))
        list_limit_combo=Combobox(scrape_pictures,values=list_limit,font=('arial',10),width=19,state="readonly",textvariable=limits)
        list_limit_combo.set("1")
        list_limit_combo.place(x=480,y=10)

        lab_pictures_url=Label(scrape_pictures,text="Search Pictures",font=('times new roman',12,'bold'),background="grey57",fg="white")
        lab_pictures_url.place(x=300,y=80)

        Ent_search=Entry(scrape_pictures,width=75,font=('times new roman',12,'bold'),textvariable=search_url,bd=4,relief='ridge')
        Ent_search.place(x=35,y=120)


        but_search=Button(scrape_pictures,text="Search",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=Search)
        but_search.place(x=50,y=170)
        but_search.bind("<Enter>",on_enter0)
        but_search.bind("<Leave>",on_leave0)

        
        but_scrape_pictures=Button(scrape_pictures,text="Scrape Pictures",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=scrape_pictures)
        but_scrape_pictures.place(x=260,y=170)
        but_scrape_pictures.bind("<Enter>",on_enter1)
        but_scrape_pictures.bind("<Leave>",on_leave1)


        but_clear_list=Button(scrape_pictures,text="Clear List",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=clear_list)
        but_clear_list.place(x=490,y=170)
        but_clear_list.bind("<Enter>",on_enter2)
        but_clear_list.bind("<Leave>",on_leave2)


#===================================================================================#

        lab_pictures_url=Label(download_pictures,text="Enter Picture Url",font=('times new roman',12,'bold'),background="grey87")
        lab_pictures_url.place(x=40,y=30)
    
        Ent_pictures_url=Entry(download_pictures,textvariable=pictures_url_single,width=50,font=('times new roman',12,'bold'),bd=4,relief='ridge')
        Ent_pictures_url.place(x=230,y=30)

        lab_save_as_name=Label(download_pictures,text="Pictures/folder Saves as Name",font=('times new roman',12,'bold'),background="grey87")
        lab_save_as_name.place(x=40,y=110)

        Ent_save_as_name=Entry(download_pictures,textvariable=pictures_name,width=20,font=('times new roman',12,'bold'),bd=4,relief='ridge')
        Ent_save_as_name.place(x=290,y=105)

        but_download_pictures_all=Button(download_pictures,text="Download All",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=download_all)
        but_download_pictures_all.place(x=50,y=170)
        but_download_pictures_all.bind("<Enter>",on_enter3)
        but_download_pictures_all.bind("<Leave>",on_leave3)


        but_download_pictures=Button(download_pictures,text="Download Single",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=download_single)
        but_download_pictures.place(x=270,y=170)
        but_download_pictures.bind("<Enter>",on_enter4)
        but_download_pictures.bind("<Leave>",on_leave4)

        but_clear=Button(download_pictures,text="Clear",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=clear)
        but_clear.place(x=490,y=170)
        but_clear.bind("<Enter>",on_enter5)
        but_clear.bind("<Leave>",on_leave5)


#====================================firstframe/nootbook/about================================================#

        messages1=Message(about,text="This project is all about fun and learning this project will help you to find out how you can scrape songs in different all this project goes to the author of this project \
            shreyas mohite",font='Arial 12', anchor=W)
        messages1.place(x=4,y=4)

        messages2=Message(about,text="This project required  internet connections so please make sure   that you are connected to network  all the activities in this project    is online ,else this will display   error message   \
            ",font='Arial 12', anchor=W)
        messages2.place(x=229,y=4)


        messages3=Message(about,text="The Source code of this project is available on github  you can use it as per your requirement this will help you out.The given buttons will show you how to use this software \
            ",font='Arial 12', anchor=W)
        messages3.place(x=454,y=4)


        #==================button on About nootbook=============================================#  

        but_user_manual=Button(about,text="User Manual",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=usermanual)
        but_user_manual.place(x=35,y=170)
        but_user_manual.bind("<Enter>",on_enter11)
        but_user_manual.bind("<Leave>",on_leave11)

        but_websites=Button(about,text="Websites",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=websites)
        but_websites.place(x=260,y=170)
        but_websites.bind("<Enter>",on_enter12)
        but_websites.bind("<Leave>",on_leave12)

        but_Source=Button(about,text="Source code",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=Sourcecode)
        but_Source.place(x=490,y=170)
        but_Source.bind("<Enter>",on_enter13)
        but_Source.bind("<Leave>",on_leave13)




#==========================bottomframe=============================================#
        

        scol1=Scrollbar(secondframe,orient="vertical")
        scol1.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        texttopaste=Text(secondframe,height=16,width=83,font=('times new roman',12,'bold'),yscrollcommand=scol1.set,relief="sunken",bd=3)      
        texttopaste.place(x=0,y=0)
        scol1.config(command=texttopaste.yview)


#=============================thirdframe============================================#\
        prg=Progressbar(thirdframe,length=688,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)





if __name__ == "__main__":
    root=Tk()
    app=Picture(root)
    root.mainloop()

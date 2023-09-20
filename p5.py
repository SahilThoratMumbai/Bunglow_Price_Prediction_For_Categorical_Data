from tkinter import *
import pandas as pd
from sklearn.linear_model import LinearRegression

root=Tk()
root.title("Bunglow Price Predictor")
root.geometry("1000x600+50+50")
f=("Impact",30,"bold")

lab_header=Label(root,text="Bunglow Price Predictor",font=f)
lab_header.place(x=300,y=20)

lab_area=Label(root,text="Enter Area",font=f)
ent_area=Entry(root,font=f)

lab_area.place(x=50,y=120)
ent_area.place(x=300,y=120)

c=IntVar()
c.set(2)
lab_location=Label(root,text="Location",font=f)
rb_karjat=Radiobutton(root,text="Karjat",font=f,variable=c,value=1)
rb_khandala=Radiobutton(root,text="Khandala",font=f,variable=c,value=2)
rb_lonavala=Radiobutton(root,text="lonavala",font=f,variable=c,value=3)

lab_location.place(x=50,y=220)
rb_karjat.place(x=300,y=220)
rb_khandala.place(x=500,y=220)
rb_lonavala.place(x=750,y=220)

def find():
	data=pd.read_csv("D:/Machine Learning/D4/papsep2023.csv")	
	features=data[["place","area"]]
	target=data["price"]
	nfeatures=pd.get_dummies(features)
	model=LinearRegression()
	model.fit(nfeatures,target)
	area=float(ent_area.get())
	if c.get()==1:
		d=[[area,1,0,0]]
	elif c.get()==2:
		d=[[area,0,1,0]]
	else:
		d=[[area,0,0,1]]
	price=model.predict(d)
	msg="\u20B9"+str(round(price[0],2))
	lab_ans.configure(text=msg)	
	







btn_predict=Button(root,text="Predict Price",font=f,command=find)
lab_ans=Label(root,font=f)
btn_predict.place(x=300,y=350)
lab_ans.place(x=300,y=500)


root.mainloop()
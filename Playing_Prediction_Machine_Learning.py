from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from PIL import ImageTk,Image

dict = {
    'Outlook':['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast',
               'Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'],
    'Temperature':[85,80,83,70,68,65,64,72,69,75,75,72,81,71],
    'Humidity':[85,90,86,96,80,70,65,95,70,80,70,90,75,91],
    'Windy':['False','True','False','False','False','True','True','False',
             'False','False','True','True','False','True' ],
    'Play':['no','no','yes','yes','yes','no','yes','no',
            'yes','yes','yes','yes','yes','no']
}

data = pd.DataFrame(dict)
d = data

numeric_outlook = {'Sunny':1,'Rainy':2,'Overcast':3}
data['Outlook'] = data['Outlook'].map(numeric_outlook)


numeric_windy = {'True':1,'False':0}
data['Windy'] = data['Windy'].map(numeric_windy)

numeric_data = pd.read_csv("numeric_weather_data.csv")


window = Tk()
window.title("Playing | Prediction | Training Dataset")
window.geometry("1220x620")
window.maxsize(1220,620)

out = StringVar()
temp = StringVar()
hum = StringVar()
wind = StringVar()
result = StringVar()

def background():
    image = Image.open("w.jpg")
    image = image.resize((630, 515), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    li = Button(image=img)
    li.image = img
    li.pack(side=LEFT)

def outlook():
    Label(window, text="Playing Prediction",
          font="Courier 20 bold", background="black", foreground="white", borderwidth=5, relief=SUNKEN).place(x=4,
                                                                                                              y=6,width=632)


    ttk.Label(window, text="Select an Outlook :",
              font="Courier 13 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=100,y=100)


    monthchoosen = ttk.Combobox(window, width=27,
                                textvariable=out,font="Courier 13 bold")

    # Adding combobox drop down list
    monthchoosen['values'] = ('Sunny',
                              'Overcast',
                              'Rainy')

    monthchoosen.place(x=330,y=100)




def temperature():
    ttk.Label(window, text="Select a Temperature :",
              font="Courier 13 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=100,y=130)


    monthchoosen1 = ttk.Combobox(window, width=27,
                                textvariable=temp,font="Courier 13 bold")

    # Adding combobox drop down list
    monthchoosen1['values'] = ('85',
                              '80',
                              '83',
                              '70',
                              '68',
                              '65',
                              '64',
                              '72',
                              '69',
                              '75',
                              '75',
                              '72',
                              '81',
                              '71')

    monthchoosen1.place(x=330,y=130)

def humidity():
    ttk.Label(window, text="Select a Humidity :",
              font="Courier 14 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=100,y=160)


    monthchoosen = ttk.Combobox(window, width=27,
                                textvariable=hum,font="Courier 13 bold")

    # Adding combobox drop down list
    monthchoosen['values'] = ('85',
                              '90',
                              '86',
                              '96',
                              '80',
                              '70',
                              '65',
                              '95',
                              '70',
                              '80',
                              '70',
                              '90',
                              '75',
                              '91')

    monthchoosen.place(x=330,y=160)
def windy():
    ttk.Label(window, text="Select a Windy :",
              font="Courier 13 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=100,y=190)


    monthchoosen = ttk.Combobox(window, width=27,
                                textvariable=wind,font="Courier 13 bold")

    # Adding combobox drop down list
    monthchoosen['values'] = ('True',
                              'False')

    monthchoosen.place(x=330,y=190)

def predict_button():
    Button(window,text="Predict... You can play or not ? ", command = playing_prediction,bg="black",fg="white",borderwidth=5,relief= SUNKEN,font = "Courier 15 bold").\
        place(x=170,y=230)


def playing_prediction():
    o =  numeric_outlook[str(out.get())]
    t =  temp.get()
    h =  hum.get()
    w =  numeric_windy[str(wind.get())]

    # prdiction using decision tree from sklearn
    features = ['Outlook', 'Temperature', 'Humidity', 'Windy']
    X = numeric_data.get(features)
    Y = numeric_data.get('Play')

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, Y)
    prediction = dtree.predict([[o, t, h, w]])
    print("Prediction for Playing :", prediction)
    prediction1 = dtree.predict(X)
    print("Accuracy  :", accuracy_score(prediction1, Y) * 100, "%")

    result = "prediction you can play - "+ prediction
    for i in result:
        result = i
    Label(window, text=result,
          font="Courier 14 bold", bg="black", fg="white",padx=20,pady=20, borderwidth=4, relief=SUNKEN).place(x=170, y=300)


# TExt for dataset information
text = Text(window,bg="red",fg="white",font="courier 10 bold")
text.insert(INSERT,numeric_data.describe())
text.insert(END,numeric_data.groupby('Play').size())
text.place(x=650,y=370,width=550,height=200)



# TExt for dataset
DATA = pd.read_csv("Weather_Dataset.csv")
DATA = DATA.iloc[:,1:]
text = Text(window,bg="blue",fg="white",font="courier 10 bold")
text.insert(INSERT,DATA)
text.place(x=650,y=60,width=550,height=250)


def dataset_graph():
    x = numeric_data.get('Humidity')
    y = numeric_data.get('Temperature')
    plt.scatter(x, y,color="red")
    plt.title("Weather Plot")
    plt.xlabel("Humidity")
    plt.ylabel("Temperature")
    plt.show()

Button(window, text="Graph (Temperature VS Humidity) ", command=dataset_graph, bg="black", fg="white",
       borderwidth=5, relief=SUNKEN, font="Courier 15 bold"). \
    place(x=0, y=572,width=1220)

Label(window, text="Weather Dataset",
              font="Courier 13 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=650,y=20)

Label(window, text="Dataset Descriptive Information",
              font="Courier 13 bold",background="black",foreground="white",borderwidth=4,relief=SUNKEN).place(x=650,y=330)





background()
outlook()
temperature()
humidity()
windy()
predict_button()

window.mainloop()
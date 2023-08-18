from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd
import csv
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("exercise_recommend.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    print(request.form)
    int_features=[int(float(x)) for x in request.form.values()]
    with open('test.csv', 'w', newline='') as fp:
     a = csv.writer(fp)
     data= [['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'],int_features]
     a.writerows(data)
    #final=[np.array(int_features)]
    #print(int_features)
    #print(final)
    df = pd.read_csv('test.csv')
    test = model.predict(df)
    #prediction=model.predict_proba(final)
    output= test
    steps = (output*(4.5))
    if test<20:
        return render_template('exercise_recommend.html',pred='You are very unhealthy. Please go visit a doctor!! Go visit a doctor. \n The following exercise are recommender: Walking, Running, Small level exercises. Number of Steps to walk \n Number of Calories to be burnt is {}'.format(output))
    if test>20 and test<50:
        return render_template('exercise_recommend.html',pred='Weight Lifting should be done. Please follow these steps:1) 3kg dumbells 15 reps, 3 sets 2) 5kg dumbells 15 reps, 3 sets \n Number of Calories to be burnt is {}'.format(output))
    if test>50 and test<100:
        return render_template('exercise_recommend.html',pred='High Intensity Interval Training. \n Please continue to train every 15 minutes doing pushups and situps with breaks for 3 minutes.\n Number of Calories to be burnt is {}'.format(output),pred2='Number of steps to be taken is {}'.format(steps))
    if test>100 and test<=200:
        return render_template('exercise_recommend.html',pred='Cardio exercises are to be done. \n Please follow the following exercise. Jump Ropes, Jumping Jacks, Burpees for 1 hour with 15 minute intervals.\n Number of Calories to be burnt is {}'.format(output))
    if test>200:
        return render_template('exercise_recommend.html',pred='Walking,Low Intensity Exercise.Do jogging in the mornings or evenings. You can also do small exercises like yoga and such. Number of Calories to be burnt is {}'.format(output))    
    return render_template('exercise_recommend.html',pred2= 'Number of steps to be taken is {}'.format(steps))

if __name__ == '__main__':
    app.run(debug=True)

import joblib

cls=joblib.load(r"C:\Users\batra\Downloads\SIH-main\SIH-main\Stream_predictor_model.pkl")
print("yup")
lis=[]
lis.append(10)
lis.append(20)
lis.append(20)
lis.append(20)
lis.append(20)
lis.append(20)
print(lis)
# ans=cls.predict([lis])
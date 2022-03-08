# My2ndCar.com: The Used Car Price Prediction Service.
App is deployed on Heroku cloud.
To Visit Deployed App Click Link: https://my2ndcar.herokuapp.com/

The My2ndCar Price Prediction Service App is built using flask web application, Python(3.10) and its ML Libraries.

### About Dataset
 which predicts Selling Price Of Car which is our dependant feature) based on given independent features like Car_Name,Year,Selling_Price,	Present_Price,Kms_Driven,Fuel_Type,	Seller_Type, Transmission, and Owner. Selling Price is the Dependent variable(target variable). The dataset is available at Kaggle, and it's provided by cardekho.com  
This data can be used for a lot of purposes such as price prediction to exemplify the use of Regression in Machine Learning.
The columns in the given dataset are as follows:
1. Car_Name
2. Year
3. Selling_Price
4. Present_Price
5. Kms_Driven
6. Fuel_Type
7. Seller_Type
8. Transmission
9. Owner

Dataset Link: https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho

### Algorithm 

After applying different Machine Learning algorithms we get different model accuracies and R2 Score such as,

Linear Regression with the Accuracy: 80.40 % and R2 Score (Coefficient of determination) is 0.8517983059778264

Random Forest Regressor with the Accuracy: 83.22 % and the R2 Score is 0.8693858585024029

Decision Tree Regressor with the Accuracy: 87.10 % and R2 Score is 0.913621047690589 

Thus, Decision tree regression algorithm gave us best Accuracy and Score on the Training Dataset in comparision with other algorithms.

### Tools 

Python 3.10, Seaborn 0.11.2, Flask 2.0.3, Gunicorn 20.1.0, Sklearn 0.0, Numpy 1.22.2, Pandas 1.4.1, Scikit-learn 1.0.2, Matplotlib 3.5.1,  Seaborn 0.11.2, Juputer Notebook 

### Application Preview.

![image](https://user-images.githubusercontent.com/86619476/157186601-7f0db898-06ad-4a93-9fc6-a8ccf5d3b81f.png)



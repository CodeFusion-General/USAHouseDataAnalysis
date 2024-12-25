from flask import Flask, request, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

model_path = os.path.join("..", "app", "model", "best_rf_model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        bed = float(request.form['bed'])
        bath = float(request.form['bath'])
        acre_lot = float(request.form['acre_lot'])
        house_size = float(request.form['house_size'])
        price_per_sqft = float(request.form['price_per_sqft'])
        bed_bath_ratio = float(request.form['bed_bath_ratio'])

        input_data = pd.DataFrame({
            'bed': [bed],
            'bath': [bath],
            'acre_lot': [acre_lot],
            'house_size': [house_size],
            'price_per_sqft': [price_per_sqft],
            'bed_bath_ratio': [bed_bath_ratio]
        })

        predicted_price = model.predict(input_data)[0]

        return render_template('result.html', price=round(predicted_price, 2))
    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

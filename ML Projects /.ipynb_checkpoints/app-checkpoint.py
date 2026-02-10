{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fcf1d3b-2450-4795-80dc-afa0efd75a62",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("house_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# Inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=50)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
stories = st.slider("Stories", 1, 5, 1)
parking = st.slider("Parking spaces", 0, 5, 1)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, stories, parking]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"💰 Estimated House Price: {prediction[0]:,.2f}")

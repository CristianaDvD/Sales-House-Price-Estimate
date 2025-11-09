import streamlit as st

def predict_price(X_live, house_features, price_pipeline):
	"""
	Predicts the price of a house based on live input data.
	"""
	X_live_price = X_live.filter(house_features)

	# predict
	price_prediction = price_pipeline.predict(X_live_price)
	
	statement = (
			f"* The Sale Price of your house is: **${round(price_prediction[0])}**.\n\n"
			)
	
	st.write(statement)


def predict_inherited_house_price(X_inherited, house_features, price_pipeline):
	"""
	Predicts the price of an inherited house based on its features.
	"""
	X_inherited_price = X_inherited.filter(house_features)

	# predict

	price_prediction_inherited = price_pipeline.predict(X_inherited_price)
	
	this_price = price_prediction_inherited[0]
	
	return this_price
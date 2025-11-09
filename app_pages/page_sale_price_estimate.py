import streamlit as st
import pandas as pd
from src.data_management import load_houses_data,\
	load_inherited_data, load_pkl_file
from src.machine_learning.predictive_analysis_func\
	import predict_price, predict_inherited_house_price


def page_predict_price_body():
    """
    Loads predict price files
    """
    version = 'v1'

    regression_pipe = load_pkl_file(f"outputs/ml_pipeline\
                                /predict_price/{version}\
                                /regression_pipeline.pkl")

    house_features = (pd.read_csv(f"outputs/ml_pipeline\
                                /predict_price/{version}\
                                /X_train.csv").columns.to_list())

    st.write("### Sales Price Estimate")

    st.info(
        f"The main reason for building this app was to answer\
        our business requirement no.2:"
        f"\n* **BR2** - The client is interested in predicting\
        the house sale prices from her 4 inherited houses,"
        f" and any other house in Ames, Iowa.")

    # Predict sales prices of inherited houses
    st.write(
        f"######  Sales price estimate of inherited houses\n"
        f"* See PredictedSalePrice column in the table below.")

    X_inherited = load_inherited_data()

    total_price = 0

    predicted_sale_price = []

    for i in range(X_inherited.shape[0]):
        pprice = predict_inherited_house_price
        (X_inherited.iloc[[i, ]], house_features, regression_pipe)
        predicted_sale_price.append(round(pprice))
        total_price = total_price + pprice
        total_price = round(total_price)
        X_inherited = X_inherited.filter(house_features)
        X_inherited['PredictedSalePrice'] = predicted_sale_price
        st.write(X_inherited.head())
        st.success(
            f"* Total price: **${total_price}** \n"
            f"* Features used: **{X_inherited.columns.to_list()\
            [:-1]}**.\n"
            f"\nWe were able to determine the entire value of\
            the client's properties,thanks to the Machine\
            Learning model's good prediction of the sale prices\
            of the four inherited properties.")

    st.write("---")

    # Generate Live Data

    st.write("### House Price Estimate Interface (BR2)")
    st.write("#### Would you like to estimate another home's sale price?")
    st.write("Enter the following properties' accurate values,\
    then click on the 'Estimate Sale Price' button.")

    X_live = DrawInputsWidgets()

    # predict on live data

    if st.button("Estimate Sale Price"):
        price_prediction = predict_price(X_live,
                        house_features,
                        regression_pipe)
    if price_prediction == 1: predict_price(X_live,
									house_features,
									regression_pipe)


def check_variables_for_UI(house_features):
    st.write(f"* There are {len(house_features)} features for the UI:\
    \n\n {house_features}")


def DrawInputsWidgets():
	"""
	Displays inputs boxes for our 4 chosen variables
	for the client to fill in order to estimate price
	"""

	df = load_houses_data()

	percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 6 features
	col1, col2, col3, col4 = st.columns(4)

	# create an empty DataFrame, which will be the live data

	X_live = pd.DataFrame([], index=[0])

	with col1:
		feature = "OverallQual"
		st_widget = st.number_input(
			label=feature,
			min_value=1,
			max_value=10,
			value=5,
            step=1
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label=feature,
			min_value=int(df[feature].min()*percentageMin),
			max_value=int(df[feature].max()*percentageMax),
			value=int(df[feature].median()),
            step=50
			)
	X_live[feature] = st_widget

	with col3:
		feature = "GarageArea"
		st_widget = st.number_input(
			label=feature,
			min_value=int(df[feature].min()*percentageMin),
			max_value=int(df[feature].max()*percentageMax),
			value=int(df[feature].median()),
            step=50
			)

	X_live[feature] = st_widget

	with col4:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label=feature,
			min_value=int(df[feature].min()*percentageMin),
			max_value=int(df[feature].max()*percentageMax),
			value=int(df[feature].median()),
            step=50
			)
	X_live[feature] = st_widget

	return X_live

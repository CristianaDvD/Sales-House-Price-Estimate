import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypotheses import page_project_hypotheses_body
from app_pages.page_correlation_study import page_correlation_study_body
from app_pages.page_ml_price_estimate import page_ml_predict_price_body
from app_pages.page_sale_price_estimate import page_predict_price_body
# Create an instance of the app 
app = MultiPage(app_name= "House Sale Price Estimate")

# Add your app pages here using .add_page()
app.add_page("👀 Project Overview", page_summary_body)
app.add_page("✨ Hypotheses and Validation", page_project_hypotheses_body)
app.add_page("📊 Correlation Study", page_correlation_study_body)
app.add_page("🤖 Machine Learning Model", page_ml_predict_price_body)
app.add_page("💰 Sale Price Estimate", page_predict_price_body)

app.run()


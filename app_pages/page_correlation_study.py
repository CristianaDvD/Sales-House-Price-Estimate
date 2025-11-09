import streamlit as st
import numpy as np
import plotly.express as px
import ppscore as pps
import seaborn as sns
sns.set_style("whitegrid")


from feature_engine.discretisation import ArbitraryDiscretiser
from src.data_management import load_houses_data

def page_correlation_study_body():
    """
    Display correlated variables and a checkbox to show the show
    house price per variable.
    """
    df = load_houses_data()

    # List of variables to study in the analysis
    vars_to_study = ['OverallQual','GrLivArea','GarageArea','TotalBsmtSF','1stFlrSF','YearBuilt']

    st.write("### Correlation Study") # page title
    # Display Business req 1
    st.info(
        f"* **BR1** - The client is interested in discovering how house attributes correlate with sale prices.\
        Therefore, the client expects data visualizations of the correlated variables against the sale price."
    )

    # displays checkbox revealing houses dataset
    if st.checkbox("Inspect House Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\
            We show the first 10 rows below.\n"
            f"* SalePrice is our target variable, and we want to identify features correlated to it.")
        
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"To learn more about the relationship between the variables and a property's sale price, we performed\
        a correlation analysis in the notebook. This addresses the first business requirement (BR1) of the project.\n"
        f"\n We found that the most correlated variable are:\n\n **{vars_to_study}**"
        )
    
    # based on house market study notebook conclusions
    st.info(
        f"After inspecting and visualising variables with the Target Variable we can come up with the following hypotheses:\n"
        f"- Houses with higher overall material and finish quality **OverallQual** sell for higher prices.\n"
        f"- Houses with larger above-ground living area **GrLivArea** have higher sale prices.\n"
        f"- Houses with extra spaces get to a higher sale price, and here we can include **GarageArea, TotalBsmtSF,\
        BsmtExposure, GarageFinish**.\n"
        f"- Houses with a good kitchen quality **KitchenQual** have a good impact on the sale price."
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])
    target_var = 'SalePrice'
    st.write("#### Data Visualizations")

    # Display histogram of the target variable's distribution
    if st.checkbox("Distribution of Target Variable"):
        plot_target_hist(df_eda, target_var)

    # Display correlation and PPS (Predictive Power Score) heatmaps
    if st.checkbox("Show Correlation and PPS Heatmaps"):
        df_corr_pearson, df_corr_spearman, pps_matrix = (
            CalculateCorrAndPPS(df_eda))
        DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,
                        CorrThreshold=0.4, PPS_Threshold=0.2)

    # Function to display scatter plots or categorical distribution plots
    def scatter_plot_for_eda(df, col, target_var):
        """
        Function to create a scatter plot between a feature and the target
        variable.
        """
        fig = px.scatter(df, x=col, y=target_var,
                        title=f"Scatter Plot of {col} vs {target_var}",
                        trendline="ols", trendline_color_override="red")
        st.plotly_chart(fig)

    def plot_categorical(df, col, target_var):
        """
        Function to create a stacked histogram for categorical variables vs
        target.
        """
        fig = px.histogram(df, x=col, color=target_var,
                        title=f"Distribution of {col} vs {target_var}",
                        barmode='stack')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)

    def variables_plots(df_eda):
        """
        Function to plot either scatter plots or categorical plots for all
        selected variables.
        """
        target_var = 'SalePrice'
        # Iterate over all variables and plot according to type
        for col in df_eda.drop([target_var], axis=1).columns.to_list():
            if df_eda[col].dtype == 'object':
                plot_categorical(df_eda, col, target_var)
            else:
                scatter_plot_for_eda(df_eda, col, target_var)

    # Display visual analysis for each selected variable
    if st.checkbox("Variables Plots - Visual Analysis"):
        variables_plots(df_eda)


def plot_target_hist(df, target_var):
    """
    Function to plot a histogram for the target variable.
    """
    fig = px.histogram(df, x=target_var, marginal="box", nbins=50,
                    title=f"Distribution of {target_var}")
    st.plotly_chart(fig)


def heatmap_corr(df, threshold, title, figsize=(20, 12), font_annot=8):
    """
    Function to generate a correlation heatmap for numerical features in the
    DataFrame.
    """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        df_masked = df.mask(mask)

        # Plot heatmap using Plotly
        fig = px.imshow(
            df_masked,
            title=title,
            color_continuous_scale='viridis',
            labels={'x': 'Features', 'y': 'Features'},
            text_auto=True
        )
        st.plotly_chart(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """
    Function to generate a Predictive Power Score (PPS) heatmap.
    """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True

        df_masked = df.mask(mask)

        # Plot heatmap using Plotly
        fig = px.imshow(
            df_masked,
            title="Predictive Power Score Heatmap",
            color_continuous_scale='viridis',
            labels={'x': 'Features', 'y': 'Features'},
            text_auto=True
        )
        st.plotly_chart(fig)

# Code Institute credits
def CalculateCorrAndPPS(df):
    """
    Function to calculate both the Pearson and Spearman correlations as well as
    the Predictive Power Score (PPS) matrix for the dataset.
    """
    # Calculate correlation matrices
    df_corr_spearman = df.corr(method="spearman")
    df_corr_spearman.name = 'corr_spearman'
    df_corr_pearson = df.corr(method="pearson")
    df_corr_pearson.name = 'corr_pearson'

    # Calculate Predictive Power Score (PPS)
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')

    # Display PPS statistics for values below 1
    pps_score_stats = (pps_matrix_raw.query("ppscore < 1").filter(['ppscore'])
                    .describe().T)
    print(pps_score_stats.round(3))

    return df_corr_pearson, df_corr_spearman, pps_matrix

# Code Indtitute credits
def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,
                    CorrThreshold, PPS_Threshold,
                    figsize=(20, 12), font_annot=8):
    """
    Function to display both the correlation heatmap and the PPS heatmap.
    """
    # Display Pearson correlation heatmap
    heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold,
                title="Pearson Correlation Heatmap", figsize=figsize,
                    font_annot=font_annot)

    # Display Spearman correlation heatmap
    heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold,
                title="Spearman Correlation Heatmap", figsize=figsize,
                font_annot=font_annot)

    # Display PPS heatmap
    heatmap_pps(df=pps_matrix, threshold=PPS_Threshold, figsize=figsize,
                font_annot=font_annot)
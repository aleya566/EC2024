import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Load Data
@st.cache_data
def load_data(url):
    """Loads the dataset from a URL."""
    try:
        df = pd.read_csv(url)
        # Clean up column name for Academic Year, removing extra spaces if needed
        df.columns = [col.strip() for col in df.columns]
        return df
    except Exception as e:
        st.error(f"Error loading data from URL: {e}")
        return pd.DataFrame()

url = 'https://raw.githubusercontent.com/aleya566/EC2024/refs/heads/main/arts_faculty_data.csv'
arts_df = load_data(url)

# Set the title of the Streamlit app
st.title('🎨 Arts Faculty Data Analysis Dashboard')

if not arts_df.empty:
    st.subheader('Raw Data Preview')
    st.dataframe(arts_df.head())
    st.divider()

    # --- 2. Visualization Section ---
    st.header('📊 Faculty Survey Data Insights')

    # Helper function to generate and display bar charts
    def display_bar_chart(df, column_name, title, x_label, y_label='Count', orientation='v'):
        """Creates and displays a Plotly bar chart for a given column."""
        # Calculate value counts and rename columns for Plotly
        data = df[column_name].value_counts().reset_index()
        data.columns = [column_name, 'Count']

        if orientation == 'h':
            # Horizontal Bar Chart
            fig = px.bar(
                data,
                x='Count',
                y=column_name,
                orientation='h',
                title=title,
                labels={'Count': x_label, column_name: y_label}
            )
            # Ensure proper ordering by count
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        else:
            # Vertical Bar Chart
            fig = px.bar(
                data,
                x=column_name,
                y='Count',
                title=title,
                labels={column_name: x_label, 'Count': y_label}
            )
            # Adjust x-axis labels if too many categories
            if len(data[column_name]) > 5:
                fig.update_xaxes(tickangle=45)

        st.subheader(title)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("---")

    # --- New Visualizations (Converting Matplotlib/Seaborn to Plotly Bar Charts) ---

    # Visualization 1: Arts Program Distribution (Horizontal Bar Chart)
    display_bar_chart(
        arts_df,
        column_name='Arts Program',
        title='Distribution of Arts Programs',
        x_label='Count',
        y_label='Program',
        orientation='h'
    )

    # Visualization 2: Academic Year Distribution
    # Note: Column name is corrected to 'Bachelor Academic Year in EU' after stripping whitespace
    display_bar_chart(
        arts_df,
        column_name='Bachelor Academic Year in EU',
        title='Distribution of Academic Years in Arts Faculty',
        x_label='Academic Year'
    )

    # Visualization 3: HSC Study Medium Distribution
    display_bar_chart(
        arts_df,
        column_name='H.S.C or Equivalent study medium',
        title='Distribution of HSC Study Medium',
        x_label='Study Medium'
    )

    # Visualization 4: Coaching Center Attendance
    display_bar_chart(
        arts_df,
        column_name='Did you ever attend a Coaching center?',
        title='Did students attend a Coaching Center?',
        x_label='Attended Coaching Center'
    )

    # Visualization 5: Expectation Met Distribution (Q5)
    # Note: Column name is corrected to 'Q5 [To what extent your expectation was met?]'
    display_bar_chart(
        arts_df,
        column_name='Q5 [To what extent your expectation was met?]',
        title='To what extent was expectation met?',
        x_label='Rating'
    )

else:
    st.warning("Could not proceed with analysis because the data could not be loaded or is empty.")

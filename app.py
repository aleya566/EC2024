import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration
st.set_page_config(layout="wide", page_title="Arts Faculty Data Analysis")

# --- Data Loading ---
@st.cache_data
def load_data():
    """
    Loads data from the URL and handles potential errors.
    """
    url = 'https://raw.githubusercontent.com/aleya566/EC2024/refs/heads/main/arts_faculty_data.csv'
    try:
        # Assuming the variable name used in the original plots was arts_df
        arts_df = pd.read_csv(url)
        return arts_df
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on failure

arts_df = load_data()

# --- Streamlit App Layout ---
st.title("📊 Arts Faculty Data Visualization")
st.markdown("This dashboard presents key distributions from the Arts Faculty dataset using Plotly.")

if not arts_df.empty:
    st.subheader("Data Preview")
    st.dataframe(arts_df.head())

    # Create two columns for better layout
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, _ = st.columns(2) # Use one column for the last chart

    # --- Visualization 1: Distribution of Arts Programs (Plotly Express Bar Chart) ---
    with col1:
        st.subheader("1. Distribution of Arts Programs")
        # Calculate value counts and sort for ordered bar chart
        program_counts = arts_df['Arts Program'].value_counts().reset_index()
        program_counts.columns = ['Arts Program', 'Count']
        
        fig1 = px.bar(
            program_counts,
            y='Arts Program',
            x='Count',
            orientation='h',
            title='Distribution of Arts Programs',
            color='Arts Program', # Optional: Add color for differentiation
            template='plotly_white'
        )
        fig1.update_layout(yaxis={'title': 'Program'}, xaxis={'title': 'Count'}, showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)

    # --- Visualization 2: Academic Year Distribution (Plotly Express Bar Chart) ---
    with col2:
        st.subheader("2. Academic Year Distribution")
        fig2 = px.histogram(
            arts_df,
            x='Bachelor  Academic Year in EU',
            title='Distribution of Academic Years in Arts Faculty',
            color='Bachelor  Academic Year in EU',
            template='plotly_white'
        )
        fig2.update_layout(xaxis={'title': 'Academic Year'}, yaxis={'title': 'Count'}, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    # --- Visualization 3: HSC Study Medium Distribution (Plotly Express Bar Chart) ---
    with col3:
        st.subheader("3. HSC Study Medium Distribution")
        fig3 = px.histogram(
            arts_df,
            x='H.S.C or Equivalent study medium',
            title='Distribution of HSC Study Medium',
            color='H.S.C or Equivalent study medium',
            template='plotly_white'
        )
        fig3.update_layout(xaxis={'title': 'Study Medium', 'categoryorder':'total descending'}, yaxis={'title': 'Count'}, showlegend=False)
        fig3.update_xaxes(tickangle=45)
        st.plotly_chart(fig3, use_container_width=True)

    # --- Visualization 4: Coaching Center Attendance (Plotly Express Pie Chart) ---
    with col4:
        st.subheader("4. Coaching Center Attendance")
        # For a binary/categorical variable, a Pie Chart or simple Bar Chart works well
        coaching_counts = arts_df['Did you ever attend a Coaching center?'].value_counts().reset_index()
        coaching_counts.columns = ['Attended Coaching Center', 'Count']
        
        fig4 = px.pie(
            coaching_counts,
            values='Count',
            names='Attended Coaching Center',
            title='Did students attend a Coaching Center?',
            template='plotly_white',
            hole=.3 # Add a donut hole for style
        )
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig4, use_container_width=True)

    # --- Visualization 5: Class Modality Distribution (Plotly Express Bar Chart) ---
    with col5:
        st.subheader("5. Class Modality Distribution")
        fig5 = px.histogram(
            arts_df,
            x='Classes are mostly',
            title='Distribution of Class Modality',
            color='Classes are mostly',
            template='plotly_white'
        )
        fig5.update_layout(xaxis={'title': 'Class Modality', 'categoryorder':'total descending'}, yaxis={'title': 'Count'}, showlegend=False)
        fig5.update_xaxes(tickangle=45)
        st.plotly_chart(fig5, use_container_width=True)

else:
    st.warning("The dashboard cannot be displayed because data loading failed.")

# --- Instructions for running the app ---
st.sidebar.header("How to Run This App")
st.sidebar.info(
    "1. **Save** the code above as `streamlit_app.py`.\n"
    "2. **Open** your terminal or command prompt.\n"
    "3. **Run** the command: `streamlit run streamlit_app.py`\n"
    "4. The app will open in your default web browser."
)

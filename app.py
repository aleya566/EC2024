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
        arts_df = pd.read_csv(url)
        return arts_df
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame()

arts_df = load_data()

# --- Streamlit App Layout ---
st.title("📊 Arts Faculty Data Visualization")
st.markdown("This dashboard presents key distributions from the Arts Faculty dataset using Plotly.")

if not arts_df.empty:
    st.subheader("Data Preview")
    st.dataframe(arts_df.head())

    # Create columns for better layout
    col1, col2 = st.columns(2) # Arts Programs, Academic Year
    col3, col4 = st.columns(2) # HSC Study Medium, Coaching Center
    col5, col6 = st.columns(2) # Class Modality, Gender Pie Chart
    col7, _ = st.columns(2)    # Gender Bar Chart


    # --- Visualization 1: Distribution of Arts Programs (Plotly Express Bar Chart) ---
    with col1:
        st.subheader("1. Distribution of Arts Programs")
        st.markdown(
            """***The Takeaway:*** Enrollment is heavily **concentrated in just a few Arts programs**, showing clear student preferences for certain majors. Many specialized programs have very small student numbers, suggesting they are niche or less publicized options. The school should use this to guide budget and staffing decisions for overcrowded versus undersubscribed departments."""
        )
        program_counts = arts_df['Arts Program'].value_counts().reset_index()
        program_counts.columns = ['Arts Program', 'Count']
        
        fig1 = px.bar(
            program_counts,
            y='Arts Program',
            x='Count',
            orientation='h',
            title='Distribution of Arts Programs',
            color='Arts Program',
            template='plotly_white'
        )
        fig1.update_layout(yaxis={'title': 'Program'}, xaxis={'title': 'Count'}, showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)

    # --- Visualization 2: Academic Year Distribution (Plotly Express Bar Chart) ---
    with col2:
        st.subheader("2. Academic Year Distribution")
        st.markdown(
            """***The Takeaway:*** This chart tracks **how many students make it through each year** of their degree. A big drop-off after the first year would be a red flag, pointing to high attrition or academic struggles that need fixing. Consistent numbers across the years suggest the faculty is doing a good job supporting students to graduation. This is essentially the report card on student retention."""
        )
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
        st.markdown(
            """***The Takeaway:*** This proves that the vast **majority of students come from the same high school system**. This means most students share a similar academic background, which is helpful for instructors to know. Professors should consider this common foundation when designing introductory courses and setting expectations for new students. This uniformity impacts how the curriculum should be delivered."""
        )
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
        st.markdown(
            """***The Takeaway:*** The chart reveals that a **huge percentage of admitted students got external coaching**. This suggests that passing the entrance exam is extremely competitive, almost requiring specialized test prep outside of school. This heavy reliance on coaching raises questions about fairness and access to the university for students who can't afford that extra help. It highlights a major trend in the admissions landscape."""
        )
        coaching_counts = arts_df['Did you ever attend a Coaching center?'].value_counts().reset_index()
        coaching_counts.columns = ['Attended Coaching Center', 'Count']
        
        fig4 = px.pie(
            coaching_counts,
            values='Count',
            names='Attended Coaching Center',
            title='Did students attend a Coaching Center?',
            template='plotly_white',
            hole=.3
        )
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig4, use_container_width=True)

    # --- Visualization 5: Class Modality Distribution (Plotly Express Bar Chart) ---
    with col5:
        st.subheader("5. Class Modality Distribution")
        st.markdown(
            """***The Takeaway:*** This shows the **most common way classes are delivered** across the faculty, whether that's 'In-Person,' 'Online,' or 'Hybrid.' The tallest bar identifies the dominant learning environment for the majority of students. This is crucial for planning campus facilities and making sure the teaching methods and technologies match what students are experiencing daily. The school's current strategy is clearly visible here."""
        )
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

    # --- Visualization 6: Gender Distribution (Plotly Express Pie Chart) ---
    with col6:
        st.subheader("6. Gender Distribution (Pie Chart)")
        st.markdown(
            """***The Takeaway:*** Both gender charts confirm a **clear and significant imbalance** in the student population, with one gender enrolling much more than the other. The large proportional difference is very noticeable, highlighting a diversity issue within the faculty. This should prompt the administration to look into targeted marketing and outreach to encourage more applications from the underrepresented group."""
        )
        gender_counts_pie = arts_df['Gender'].value_counts().reset_index()
        gender_counts_pie.columns = ['Gender', 'Count']
        
        fig6 = px.pie(
            gender_counts_pie,
            values='Count',
            names='Gender',
            title='Gender Distribution in Arts Faculty',
            template='plotly_white',
            hole=.4
        )
        fig6.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig6, use_container_width=True)

    # --- Visualization 7: Gender Distribution (Plotly Express Bar Chart) ---
    with col7:
        st.subheader("7. Gender Distribution (Bar Chart)")
        st.markdown(
            """***The Takeaway:*** This bar chart visually reinforces the **numerical size of the gender gap** by showing the exact counts side-by-side. The height difference makes the disparity impossible to ignore and clearly quantifies the enrollment difference. This metric is essential for the university to set concrete goals to improve gender balance in future admission cycles. It’s the easiest way to grasp the scale of the issue."""
        )
        gender_counts_bar = arts_df['Gender'].value_counts().reset_index()
        gender_counts_bar.columns = ['Gender', 'Count']

        fig7 = px.bar(
            gender_counts_bar,
            x='Gender',
            y='Count',
            title='Gender Distribution in Arts Faculty',
            color='Gender',
            template='plotly_white'
        )
        fig7.update_layout(xaxis={'title': 'Gender'}, yaxis={'title': 'Count'}, showlegend=False)
        st.plotly_chart(fig7, use_container_width=True)


else:
    st.warning("The dashboard cannot be displayed because data loading failed.")

# --- Instructions for running the app ---
st.sidebar.header("How to Run This App")
st.sidebar.info(
    "1. **Save** the code above as `arts_faculty_dashboard.py`.\n"
    "2. **Open** your terminal or command prompt.\n"
    "3. **Run** the command: `streamlit run arts_faculty_dashboard.py`\n"
    "4. The app will open in your default web browser."
)

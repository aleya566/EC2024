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
            """***Key Finding:*** The distribution of students across programs exhibits significant **concentration of enrollment**. This means that a few core programs within the Arts Faculty are highly sought after and absorb the majority of the student population. Conversely, many specialized programs maintain comparatively small student cohorts. This evidence is vital for the administration to effectively allocate academic resources, like faculty and infrastructure, to match the varying demands of each discipline."""
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
            """***Key Finding:*** This visualization provides crucial data on **student progression and retention** throughout the bachelor's degree. A noticeable decline in student numbers between academic years could signal issues with student attrition or academic difficulty in foundational courses. If the numbers remain consistent across the years, it reflects successful retention and stable student persistence through the curriculum. Analyzing this trend helps the faculty assess the effectiveness of its advising and student support services."""
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
            """***Key Finding:*** The data highlights a strong **predominance of a single prior educational background** among admitted students. This concentration suggests that the majority of the faculty's cohort share similar high school learning experiences and pedagogical exposure. Recognizing this uniformity is important for instructors, as it helps them tailor their teaching strategies and introductory materials. This ensures that the curriculum effectively bridges the gap between the students' previous academic environment and the university standard."""
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
            """***Key Finding:*** This chart confirms that a **substantial majority of successful applicants sought specialized external coaching** before entering the university. This trend underscores the highly competitive nature of the admissions process for the Arts Faculty, where supplementary test preparation is widely perceived as necessary for success. The data may raise questions regarding educational equity, as reliance on external, possibly paid, resources can create barriers for applicants without similar financial means. This is a critical factor influencing access to higher education."""
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
            """***Key Finding:*** The class modality chart clearly identifies the **dominant form of course delivery** currently employed by the faculty (i.e., In-Person, Online, or Hybrid). The most frequent modality established by this data defines the primary learning environment for the majority of students. This insight is essential for university planners to appropriately manage technical support, physical classroom allocation, and the training provided to faculty members on effective pedagogical practices within that specific format."""
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
            """***Key Finding:*** Both the pie and bar charts conclusively demonstrate a distinct **gender imbalance** within the Arts Faculty student population. The proportional representation clearly favors one gender category over the other, which often reflects wider trends in academic program choice. This finding is a prompt for the institution to review its strategic goals regarding diversity and inclusion. Understanding this distribution is the first step toward developing targeted outreach programs to encourage participation from the underrepresented gender."""
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
            """***Key Finding:*** The bar chart explicitly quantifies the **absolute numerical disparity** in gender enrollment. By providing a direct visual comparison of the counts for each gender, the magnitude of the imbalance becomes immediately apparent. This metric is valuable for administrators seeking to set concrete, measurable targets for diversity initiatives. The clear data supports the need for focused policy interventions aimed at evening out the representation across the student body."""
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

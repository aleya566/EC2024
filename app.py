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
            """***The Takeaway:*** It's super clear that only a **handful of Arts programs are actually popular** here—most of the students are packed into just a couple of majors, making those classes feel crowded. The rest of the programs are pretty small, almost like niche options that don't get many applications. The administration really needs to see this when deciding which departments get more budget or hire more professors next year."""
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
            """***The Takeaway:*** This shows us **how many students make it through each year** of their degree. If there's a big drop in the second or third year, it signals a possible retention problem—maybe the coursework gets too tough, or students are dropping out. Seeing a stable number across all years is the best scenario, meaning most students are sticking with their program. This info helps the school figure out if their support programs are actually working to keep people enrolled."""
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
            """***The Takeaway:*** This chart is basically telling us that almost **everyone here comes from the same high school system** (one specific study medium is dominant). Because they all have a similar background, instructors need to remember that students might share the same academic strengths and weaknesses. This common background is a major factor in how lessons should be structured, making sure the curriculum fits with what students learned before coming to the university."""
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
            """***The Takeaway:*** This is shocking: a **massive majority of accepted students went to a coaching center**. This proves that getting into the Arts Faculty is extremely competitive and specialized—it seems like just a regular high school education isn't quite enough anymore. The trend suggests that specialized test prep is almost a **prerequisite for admission**, which raises questions about how fair the playing field is for applicants who can't afford that extra help."""
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
            """***The Takeaway:*** This chart simply shows us **how most classes are delivered**—is it mostly 'Online,' 'In-Person,' or a 'Hybrid' mix? The tallest bar tells the story of the current standard teaching setup for the faculty. This is crucial for students to know what kind of campus life to expect and helps the university make sure the right facilities (whether physical classrooms or robust servers) are supporting that primary method."""
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
            """***The Takeaway:*** The pie chart confirms a **clear and significant gender gap** in the Arts Faculty—one gender is definitely enrolling in much higher numbers than the other. Looking at the unequal slices, it's obvious the student body isn't balanced. This kind of imbalance is important for the school to notice, as they might need to figure out why one group is less interested and try to encourage more diversity in their programs."""
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
            """***The Takeaway:*** This bar chart clearly **shows the numbers behind the gender imbalance**. You can instantly see how much taller one bar is than the other, making the size of the gap really obvious. This visualization is great because it gives the exact counts, which is helpful when the university needs to set specific goals for outreach or change its admission marketing to try and get more applications from the underrepresented gender."""
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

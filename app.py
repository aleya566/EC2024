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
            """***Insight:*** Wow, it really jumps out how **uneven the program sizes** are here. It looks like most students are packed into just a couple of main Arts programs, which probably means those are the most popular ones people apply for. Meanwhile, a lot of the other programs are pretty small—almost like specialty groups with limited enrollment. The faculty really needs to see this when figuring out which departments need more professors or classroom space next year."""
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
            """***Insight:*** This chart is basically showing us **how many students are in each year** of their bachelor's degree right now. If we see a huge drop-off right after the first year, it might be a big problem with students leaving the program or failing classes, which the school would need to address. On the other hand, if the numbers stay pretty similar across all four years, that's a good sign that people are sticking around and graduating. This helps us know if the school is doing a good job keeping students engaged and supported over time."""
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
            """***Insight:*** Looking at where everyone came from before university, it's clear that **one specific study medium** (like the local or primary medium) is totally dominating the student body. It seems like almost all our students shared that same kind of high school background and teaching style, which means they likely have similar academic foundations. This is important because professors might need to make sure they aren't relying on knowledge that only students from other mediums would have. This concentration impacts how lessons are taught."""
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
            """***Insight:*** This pie chart is pretty eye-opening because a **huge majority of students** admitted here said they went to a coaching center beforehand. It definitely makes you wonder if it's getting too competitive to get in without paying for outside help, suggesting the entrance process requires specialized training. It seems like just graduating high school isn't enough anymore, and almost everyone feels they **have to get specialized training** to successfully pass the entrance exam for the Arts Faculty. This is a big trend in admissions."""
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
            """***Insight:*** This bar graph tells us exactly **how classes are mostly being run** in the Arts Faculty—whether they are 'Online', 'In-Person', or maybe a 'Hybrid' mix. Whatever category has the tallest bar is definitely what most students are experiencing on a day-to-day basis. This information is key for everyone, from the IT department (making sure the right tech works) to the students (knowing what kind of learning environment they should prepare for). It reflects the current standard teaching approach."""
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
            """***Insight:*** The pie chart clearly shows a big **gender gap** in the Arts Faculty, where one gender is obviously enrolling much more than the other. When you look at the proportional slices, the difference in size is hard to ignore, meaning the student body isn't very balanced right now. This kind of heavy tilt toward one gender is something the administration should look into. They need to figure out why this is happening and if the school needs to do more to get people of the underrepresented gender interested in arts programs."""
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
            """***Insight:*** This bar chart is the most straightforward way to see the **gender enrollment difference**, showing us the exact count for each gender category side-by-side. The height difference between the bars is really noticeable, confirming that the imbalance is quite large. This chart makes it really easy for the administration to see the exact scale of the disparity and decide how to address it with specific recruitment goals. It clearly quantifies the enrollment gap."""
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

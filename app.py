import streamlit as st

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Nqabakazi Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide"
)

# =================================================
# CUSTOM STYLING
# =================================================

st.markdown("""
<style>

.main{
    background-color:#FFFFFF;
}

h1{
    color:#0E4D92;
}

h2{
    color:#0E4D92;
}

h3{
    color:#1E3A5F;
}

[data-testid="stSidebar"]{
    background-color:#EAF4FF;
}

.stMetric{
    background-color:#F4FAFF;
    padding:15px;
    border-radius:12px;
}

div[data-testid="stExpander"]{
    border-radius:10px;
}

.project-box{
    background-color:#F7FBFF;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #6BB6FF;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# =================================================
# SIDEBAR
# =================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "About Me",
        "Farm Resource Allocation",
        "WineScan Research",
        "Graduate Destination Survey",
        "Institutional Reporting",
        "Science Communication",
        "Skills",
        "Contact"
    ]
)

# =================================================
# HOME PAGE
# =================================================

if page == "Home":

    col1, col2 = st.columns([1,2])

    with col1:

        # SAVE YOUR PHOTO AS profile.jpg
        st.image(
            "profile.jpg",
            width=320
        )

    with col2:

        st.title("NQABAKAZI DYANTYI")

        st.subheader(
            "Institutional Research | Data Analytics | Science Communication"
        )

        st.write(
            """
            Welcome to my Research Portfolio.

            I am a Junior Data Analyst and emerging researcher
            with interests in Institutional Research,
            Data Analytics, Optimisation Modelling,
            Survey Research, Dashboard Development,
            Executive Reporting and Science Communication.

            This portfolio showcases selected academic,
            professional and public engagement projects
            completed throughout my journey.
            """
        )

    st.divider()

    st.header("Research Areas")

    col1,col2,col3 = st.columns(3)

    with col1:

        st.info(
            """
            🌱 Operations Research

            Linear Programming

            Optimisation Models
            """
        )

    with col2:

        st.info(
            """
            🍷 Statistical Analysis

            Scientific Research

            Data Interpretation
            """
        )

    with col3:

        st.info(
            """
            📊 Institutional Analytics

            Surveys

            Dashboards

            Reporting
            """
        )

    st.divider()

    st.header("Featured Projects")

    st.markdown("""
    <div class="project-box">
    <h4>🌱 Farm Resource Allocation</h4>
    Operations Research project using Linear Programming.
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <div class="project-box">
    <h4>🍷 WineScan Research</h4>
    FTIR Spectroscopy and Statistical Analysis.
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <div class="project-box">
    <h4>📊 Graduate Destination Survey</h4>
    Survey Redesign and Power BI Dashboard Development.
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <div class="project-box">
    <h4>🏛️ Institutional Reporting</h4>
    Executive Analytics and Graduate Outcomes Reporting.
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown("""
    <div class="project-box">
    <h4>🔬 Science Communication</h4>
    Africa Scientifique & AIMS Public Engagement Project.
    </div>
    """,
    unsafe_allow_html=True)

# =================================================
# ABOUT ME
# =================================================

elif page == "About Me":

    st.title("👩🏽‍💻 About Me")

    st.image(
        "profile.jpg",
        width=250
    )

    st.write(
        """
        I am Nqabakazi Dyantyi, a Junior Data Analyst
        in the Institutional Planning Directorate
        at the Cape Peninsula University of Technology.

        My work focuses on:

        • Institutional Research

        • Data Analytics

        • Survey Design

        • Power BI Dashboard Development

        • Graduate Outcome Analysis

        • Executive Reporting

        • Science Communication

        • Public Engagement

        I am passionate about using data to support
        evidence-based decision-making while also
        communicating complex ideas in ways that are
        accessible to diverse audiences.
        """
    )

    st.subheader("Education")

    st.markdown("""
    ✅ Advanced Diploma in Mathematical Sciences

    ✅ Postgraduate Diploma in Mathematical Sciences

    ✅ Continuous Professional Development
    """) 
# =================================================
# FARM RESOURCE ALLOCATION
# =================================================

elif page == "Farm Resource Allocation":

    st.title("🌱 Farm Resource Allocation Problem")

    st.caption(
        "Undergraduate Research Project | Operations Research"
    )

    st.subheader(
        "A Case Study of a Farm in Queenstown, Eastern Cape, South Africa"
    )

    st.write(
        """
        This project investigated the use of Linear Programming
        to optimise agricultural resource allocation and support
        farm decision-making under resource constraints.
        """
    )

    st.header("📖 Project Overview")

    st.write(
        """
        Resource allocation remains one of the most important
        challenges faced by farmers. Limited land, labour
        and financial resources require effective planning
        to maximise profitability.
        """
    )

    st.header("❓ Research Problem")

    st.write(
        """
        Farm managers must maximise profit while operating
        within constraints relating to land, labour,
        fertilizer, chemicals and seed costs.

        A Linear Programming model was developed
        and implemented using MATLAB.
        """
    )

    st.header("🎯 Objectives")

    st.markdown("""
    ✅ Investigate Linear Programming in agriculture

    ✅ Identify key variables and constraints

    ✅ Determine parameters for MATLAB implementation

    ✅ Communicate optimisation results to farmers
    """)

    st.header("⚙️ Methodology")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("Land", "39 ha")

    with col2:
        st.metric("Labour", "100")

    with col3:
        st.metric("Seed Budget", "R200 000")

    st.write(
        """
        Six crops were modelled:

        • Cabbage

        • Spinach

        • Butternut

        • Tomatoes

        • Potatoes

        • Maize
        """
    )

    st.header("📈 Results")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric(
            "Income",
            "R7.42M"
        )

    with col2:
        st.metric(
            "Profit",
            "R7.16M"
        )

    with col3:
        st.metric(
            "Profit Increase",
            "46%"
        )

    st.header("💡 Skills Demonstrated")

    st.markdown("""
    ✅ Linear Programming

    ✅ MATLAB

    ✅ Operations Research

    ✅ Optimisation

    ✅ Mathematical Modelling

    ✅ Data Analysis
    """)

    st.header("📝 Reflection")

    st.write(
        """
        This project introduced me to optimisation
        modelling and demonstrated how mathematical
        techniques can support real-world decision
        making in agriculture.
        """
    )



# =================================================
# WINESCAN PROJECT
# =================================================

elif page == "WineScan Research":

    st.title("🍷 WineScan Research")

    st.caption(
        "Scientific Research Project | Statistical Analysis"
    )

    st.subheader(
        "Investigating WineScan as a Tool for Identifying Pinking in Wine"
    )

    st.write(
        """
        This study investigated the effectiveness of
        WineScan FTIR spectroscopy for identifying
        pinking susceptibility in white wine.
        """
    )

    st.header("📖 Project Overview")

    st.write(
        """
        Pinking is a wine fault that reduces product
        quality and marketability. Traditional detection
        methods are often subjective and unreliable.

        WineScan offers a rapid and non-destructive
        analytical alternative.
        """
    )

    st.header("🎯 Research Objectives")

    st.markdown("""
    ✅ Evaluate temperature effects

    ✅ Compare bag press methods

    ✅ Assess ripening stages

    ✅ Identify absorbance peaks
    """)

    st.header("⚙️ Methodology")

    st.write(
        """
        FTIR spectroscopy was used to measure
        absorbance across wine samples exposed
        to different treatments.
        """
    )

    st.header("📊 Statistical Analysis")

    col1,col2 = st.columns(2)

    with col1:
        st.metric(
            "F-value",
            "49.42"
        )

    with col2:
        st.metric(
            "p-value",
            "< 2 × 10⁻¹⁶"
        )

    st.write(
        """
        ANOVA revealed statistically significant
        differences between treatment groups.
        """
    )

    st.header("🔍 Key Findings")

    st.markdown("""
    ✅ Ripening stage significantly influenced absorbance

    ✅ 25°B showed highest absorbance

    ✅ Press method showed minimal effect

    ✅ Temperature showed limited impact
    """)

    st.header("🚀 Impact")

    st.success(
        """
        WineScan demonstrated potential as a rapid,
        reliable and non-destructive tool for assessing
        pinking susceptibility in wine.
        """
    )

    st.header("💡 Skills Demonstrated")

    st.markdown("""
    ✅ ANOVA

    ✅ Tukey HSD

    ✅ Statistical Analysis

    ✅ FTIR Spectroscopy

    ✅ Data Interpretation

    ✅ Scientific Research
    """)

    st.header("📝 Reflection")

    st.write(
        """
        This project strengthened my understanding
        of experimental design, hypothesis testing
        and statistical methods within scientific
        research.
        """
    )



# =================================================
# GDS PROJECT
# =================================================

elif page == "Graduate Destination Survey":

    st.title("📊 Graduate Destination Survey")

    st.caption(
        "Advanced Diploma Research Project"
    )

    st.subheader(
        "Improving Graduate Outcomes Reporting at CPUT"
    )

    st.header("📖 Project Overview")

    st.write(
        """
        This project focused on redesigning the
        Graduate Destination Survey and developing
        a Power BI dashboard to modernise graduate
        outcomes reporting at CPUT.
        """
    )

    st.header("❓ Research Problem")

    st.markdown("""
    Existing survey challenges included:

    • Unclear questions

    • No validation logic

    • Inconsistent responses

    • Weak data quality
    """)

    st.header("🎯 Objectives")

    st.markdown("""
    ✅ Improve survey quality

    ✅ Strengthen the data pipeline

    ✅ Enhance reporting capacity

    ✅ Develop a dashboard solution
    """)

    st.header("⚙️ Methodology")

    st.write(
        """
        Data was collected from historical
        Graduate Destination Survey records
        and a redesigned pilot survey.
        """
    )

    st.markdown("""
    **Tools Used**

    • Excel

    • Microsoft Forms

    • R

    • Power BI
    """)

    st.header("🗄️ Historical Dataset")

    col1,col2 = st.columns(2)

    with col1:
        st.metric(
            "Original Records",
            "2,491"
        )

    with col2:
        st.metric(
            "Valid Records",
            "1,736"
        )

    st.write(
        """
        Records were cleaned, verified against
        HEMIS and prepared for redesign analysis.
        """
    )

    st.header("📝 Survey Redesign")

    st.markdown("""
    New sections included:

    • Salary Bands

    • Job Relevance

    • Time to Employment

    • Unemployment Reasons

    • Further Studies

    • WIL Satisfaction
    """)

    st.header("📊 Dashboard Development")

    st.write(
        """
        A Power BI dashboard was developed to
        visualise graduate outcomes and provide
        real-time decision-support information.
        """
    )

    st.header("🚀 Project Impact")

    st.success(
        """
        Improved survey quality and modernised
        graduate outcomes reporting through
        dashboard analytics.
        """
    )

    st.header("💡 Skills Demonstrated")

    st.markdown("""
    ✅ Survey Design

    ✅ Power BI

    ✅ Data Cleaning

    ✅ Data Validation

    ✅ Institutional Research

    ✅ Dashboard Development
    """)

    st.header("📝 Reflection")

    st.write(
        """
        This project demonstrated how strong
        survey design and data quality can
        improve institutional decision making.
        """
    )
    # =================================================
# INSTITUTIONAL REPORTING
# =================================================

elif page == "Institutional Reporting":

    st.title("🏛️ Institutional Reporting & Executive Analytics")

    st.caption(
        "Institutional Planning Directorate | Executive Reporting"
    )

    st.write(
        """
        This project involved supporting graduate outcomes
        reporting for executive decision-making within
        the University environment.

        Graduate Destination Survey findings were analysed
        and prepared for inclusion in institutional reporting
        outputs used by senior management.
        """
    )

    st.header("📖 Project Overview")

    st.write(
        """
        Universities require reliable graduate outcomes
        information to support planning, accountability
        and strategic decision-making.

        This project contributed to the reporting of graduate
        employment and study outcomes through the Graduate
        Destination Survey.
        """
    )

    st.header("👩🏽‍💻 My Contributions")

    st.markdown("""
    ✅ Data Cleaning

    ✅ Graduate Record Verification

    ✅ Data Quality Checks

    ✅ Graduate Outcomes Analysis

    ✅ Reporting Indicators

    ✅ Data Visualisation

    ✅ Executive Reporting Support
    """)

    st.header("📈 Key Reporting Indicators")

    col1,col2 = st.columns(2)

    with col1:

        st.metric(
            "Response Rate",
            "22.1%"
        )

    with col2:

        st.metric(
            "Employment Rate",
            "41.7%"
        )

    st.header("🚀 Impact")

    st.success(
        """
        Contributed to evidence-based planning through
        institutional analytics and executive reporting.
        """
    )

    st.header("💡 Skills Demonstrated")

    st.markdown("""
    ✅ Institutional Research

    ✅ Data Cleaning

    ✅ Data Validation

    ✅ Executive Reporting

    ✅ Survey Analytics

    ✅ Strategic Planning Support
    """)

    st.header("📝 Reflection")

    st.write(
        """
        This project strengthened my ability to transform
        raw data into information that can support senior
        management decision-making.
        """
    )



# =================================================
# SCIENCE COMMUNICATION
# =================================================

elif page == "Science Communication":

    st.title("🔬 Science Communication & Public Engagement")

    st.caption(
        "Africa Scientifique Programme | AIMS South Africa"
    )

    st.subheader(
        "Maths Is NOT The Enemy! When Parents Change Beliefs, Children Gain Confidence"
    )

    st.write(
        """
        This project explored how parents' beliefs
        about mathematics influence children's
        confidence and attitudes toward the subject.
        """
    )

    # Save your collage as:
    # aims_collage.jpg

    st.image(
        "aims_collage.jpg",
        use_container_width=True
    )

    st.header("📖 Project Overview")

    st.write(
        """
        The project focused on communicating the idea
        that mathematical ability is not fixed and that
        beliefs can change through effort, support
        and positive experiences.
        """
    )

    st.header("🎯 Objectives")

    st.markdown("""
    ✅ Promote positive mathematical beliefs

    ✅ Engage parents and grandparents

    ✅ Translate scientific concepts into simple language

    ✅ Encourage support for learners
    """)

    st.header("👥 Target Audience")

    st.markdown("""
    • Parents

    • Grandparents

    • Security Staff

    • Cleaning Staff

    • Community Members
    """)

    st.header("📍 Community Engagement")

    st.write(
        """
        Engagements were conducted across the CPUT
        campus through individual and small-group
        conversations supported by a science
        communication poster.
        """
    )

    st.header("🌟 Outcomes")

    st.markdown("""
    ✅ Increased awareness

    ✅ Meaningful community conversations

    ✅ Requests for additional resources

    ✅ Positive engagement around mathematics
    """)

    st.header("💡 Skills Demonstrated")

    st.markdown("""
    ✅ Science Communication

    ✅ Public Engagement

    ✅ Storytelling

    ✅ Public Speaking

    ✅ Community Outreach

    ✅ Research Translation
    """)

    st.header("📝 Reflection")

    st.write(
        """
        This experience improved my confidence
        as a communicator and demonstrated the
        importance of making research meaningful
        to everyday communities.
        """
    )



# =================================================
# SKILLS PAGE
# =================================================

elif page == "Skills":

    st.title("💡 Technical Skills")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Data Analytics")

        st.markdown("""
        ✅ Excel

        ✅ Power BI

        ✅ Python

        ✅ R

        ✅ SQL (Basic)

        ✅ Dashboard Development
        """)

        st.subheader("Research")

        st.markdown("""
        ✅ Survey Design

        ✅ Data Collection

        ✅ Data Cleaning

        ✅ Statistical Analysis

        ✅ Institutional Research
        """)

    with col2:

        st.subheader("Advanced Analytics")

        st.markdown("""
        ✅ Linear Programming

        ✅ MATLAB

        ✅ Optimisation

        ✅ ANOVA

        ✅ Tukey HSD
        """)

        st.subheader("Professional")

        st.markdown("""
        ✅ Report Writing

        ✅ Executive Reporting

        ✅ Science Communication

        ✅ Public Speaking

        ✅ Stakeholder Engagement
        """)



# =================================================
# CONTACT PAGE
# =================================================

elif page == "Contact":

    st.title("📧 Contact")

    st.image(
        "profile.jpg",
        width=250
    )

    st.subheader("Nqabakazi Dyantyi")

    st.write(
        """
        Junior Data Analyst

        Institutional Planning Directorate

        Cape Peninsula University of Technology
        """
    )

    st.header("🌍 Research Interests")

    st.markdown("""
    • Institutional Research

    • Graduate Outcomes Analytics

    • Survey Methodology

    • Data Visualisation

    • Applied Statistics

    • Operations Research

    • Science Communication
    """)

    st.info(
        """
        Thank you for visiting my Research Portfolio.
        """
    )



# =================================================
# FOOTER
# =================================================

st.divider()

st.caption(
    "© Nqabakazi Dyantyi | Research Portfolio"
)
``

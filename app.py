# =================================================
# FARM RESOURCE ALLOCATION
# =================================================

elif page == "Farm Resource Allocation":

    st.title("🌱 Farm Resource Allocation Problem")

    st.caption(
        "Undergraduate Research Project | Operations Research"
    )

    st.subheader(
        "A Case Study of a Farm in Queenstown, "
        "Eastern Cape, South Africa"
    )

    st.write(
        """
        This project investigated the application of Linear Programming
        to agricultural resource allocation, with the aim of supporting
        farm decision-making under limited land, labour and financial
        resources.
        """
    )

    st.divider()

    # -------------------------------------------------
    # PROJECT OVERVIEW
    # -------------------------------------------------

    st.header("📖 Project Overview")

    st.write(
        """
        Resource allocation is an important challenge in agriculture,
        where farmers must determine how to allocate limited resources
        across different crop activities.

        This study investigated the use of Linear Programming to support
        resource allocation and profitability decisions for a farm in
        Queenstown, Eastern Cape, South Africa.
        """
    )

    # -------------------------------------------------
    # PROBLEM STATEMENT
    # -------------------------------------------------

    st.header("❓ Problem Statement")

    st.write(
        """
        Farm managers encounter resource allocation challenges while
        attempting to maximise profit margins under limitations relating
        to income, land and labour.

        To address this challenge, a Linear Programming model was
        formulated and implemented using the Simplex method in MATLAB,
        with the model adapted specifically to the agricultural context.
        """
    )

    # -------------------------------------------------
    # OBJECTIVES
    # -------------------------------------------------

    st.header("🎯 Research Objectives")

    objectives = [
        "Investigate the application of Linear Programming to enhance resource allocation in agriculture.",
        "Identify key variables and constraints for a farmer-focused Linear Programming model.",
        "Determine essential parameters and data sources for effective MATLAB implementation.",
        "Develop methods to communicate Linear Programming results to farm managers for informed decision-making."
    ]

    for objective in objectives:
        st.markdown(f"✅ {objective}")

    # -------------------------------------------------
    # METHODOLOGY
    # -------------------------------------------------

    st.header("⚙️ Methodology")

    st.write(
        """
        A Linear Programming model was developed to determine how
        available farm resources could be allocated across six crop
        activities while maximising expected income.
        """
    )

    st.subheader("Resources considered")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Land", "39 ha")
        st.metric("Labour", "100 people")

    with col2:
        st.metric("Fertilizer Budget", "R60,000")
        st.metric("Chemical Budget", "R50,000")

    with col3:
        st.metric("Seed Budget", "R200,000")
        st.metric("Crop Activities", "6")

    st.write(
        """
        The model considered cabbage, spinach, butternut, tomatoes,
        potatoes and maize.
        """
    )

    # -------------------------------------------------
    # DECISION VARIABLES
    # -------------------------------------------------

    st.header("🔢 Decision Variables")

    st.write(
        """
        Six decision variables were defined, with each variable
        representing the area allocated to a particular crop in hectares.
        """
    )

    decision_variables = {
        "Variable": [
            "x₁",
            "x₂",
            "x₃",
            "x₄",
            "x₅",
            "x₆"
        ],
        "Crop": [
            "Cabbage",
            "Spinach",
            "Butternut",
            "Tomatoes",
            "Potatoes",
            "Maize"
        ],
        "Definition": [
            "Area allocated to cabbage (ha)",
            "Area allocated to spinach (ha)",
            "Area allocated to butternut (ha)",
            "Area allocated to tomatoes (ha)",
            "Area allocated to potatoes (ha)",
            "Area allocated to maize (ha)"
        ]
    }

    st.table(decision_variables)

    # -------------------------------------------------
    # MATHEMATICAL MODEL
    # -------------------------------------------------

    st.header("📐 Mathematical Model")

    st.write(
        """
        The Linear Programming problem was formulated as a profit
        maximisation model subject to land, labour, fertilizer,
        chemical and seed constraints.
        """
    )

    with st.expander("View Mathematical Formulation"):

        st.subheader("Objective Function")

        st.latex(
            r"""
            \text{Maximise } Z =
            160000x_1 +
            56000x_2 +
            80000x_3 +
            166975.8813x_4 +
            400000x_5 +
            1200000x_6
            """
        )

        st.subheader("Land Constraint")

        st.latex(
            r"""
            x_1+x_2+x_3+x_4+x_5+x_6 \leq 39
            """
        )

        st.subheader("Labour Constraint")

        st.latex(
            r"""
            2x_1+2x_2+10x_3+
            22.08675678x_4+
            5x_5+5x_6 \leq 100
            """
        )

        st.subheader("Fertilizer Cost Constraint")

        st.latex(
            r"""
            424x_1+424x_2+1770x_3+
            11728.06785x_4+
            885x_5+1770x_6
            \leq 60000
            """
        )

        st.subheader("Chemical Cost Constraint")

        st.latex(
            r"""
            597x_1+424x_2+2985x_3+
            8790.529x_4+
            1492.5x_5+1492.5x_6
            \leq 50000
            """
        )

        st.subheader("Seed Cost Constraint")

        st.latex(
            r"""
            8000x_1+8000x_2+10000x_3+
            27829.31354x_4+
            5000x_5+40000x_6
            \leq 200000
            """
        )

        st.subheader("Minimum Allocation Requirements")

        st.latex(r"x_1 \geq 3")
        st.latex(r"x_2 \geq 3")
        st.latex(r"x_4 \geq 1")
        st.latex(r"x_5 \geq 2")

        st.latex(
            r"""
            x_1,x_2,x_3,x_4,x_5,x_6 > 0
            """
        )

    # -------------------------------------------------
    # RESULTS — COMING LATER
    # -------------------------------------------------

    st.divider()

    st.header("📊 Results & Discussion")

    st.info(
        """
        Results and discussion will be added after the original
        research report and presentation have been reviewed and
        the numerical outputs have been verified.
        """
    )

    # -------------------------------------------------
    # SKILLS
    # -------------------------------------------------

    st.header("💡 Skills Demonstrated")

    skills = [
        "Linear Programming",
        "Operations Research",
        "MATLAB",
        "Mathematical Modelling",
        "Optimisation",
        "Resource Allocation",
        "Quantitative Decision-Making"
    ]

    for skill in skills:
        st.markdown(f"✅ {skill}")

    # -------------------------------------------------
    # REFLECTION
    # -------------------------------------------------

    st.header("📝 Research Reflection")

    st.write(
        """
        This project strengthened my understanding of optimisation
        modelling and demonstrated how mathematical techniques can
        be applied to real-world resource allocation and
        decision-making problems.
        """
    )

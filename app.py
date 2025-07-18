import streamlit as st

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Ajay Arakh - Digital Resume", layout="wide")

# Sidebar
with st.sidebar:
    st.title("👨‍💻 Ajay Arakh")
    st.image("https://avatars.githubusercontent.com/u/60349361?s=400&u=3272718fca787ef98baeecdbe1dc86d1050473e0&v=4", width=150)  # optional avatar
    st.markdown("**Email:** arakhajay42@gmail.com")
    st.markdown("**Phone:** 9579852657")
    st.markdown("**Role:** Data Analyst / ML Engineer")
    st.markdown("📍 Pune, India")

    st.markdown("---")
    st.markdown("💬 [LinkedIn](https://www.linkedin.com/in/ajay-arakh-9a7a49101/)")
    st.markdown("🌐 [GitHub](https://github.com/arakhajay)")
    st.markdown("---")
    with open("AJAY ARAKH.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Download My Resume",
            data=pdf_file,
            file_name="Ajay_Arakh_Resume.pdf",
            mime="application/pdf",
        )


# Title
st.title("👋 Welcome to My Digital Resume")

# About Me
st.header("🧠 About Me")
st.markdown("""
Analytical and detail-oriented Data Analyst with strong proficiency in statistical analysis, data visualization, and machine learning. 
Eager to uncover trends and drive impactful business decisions using data.
""")

# Experience Section
st.header("💼 Experience")
exp = {
    "Unit Manager - Analytics, Bajaj Finserv (Oct 2024 – Present)": """
- Developed machine learning models to optimize personal loan collection.
- Built logistic regression models to predict repayment and default.
- Worked on LLM-powered chatbot (FinBot) using LangChain + HuggingFace.
- Monitored models using PSI/CSI metrics.
""",
    "Unit Manager - Analytics, Bajaj Finserv Ventures (Apr 2023 – Oct 2024)": """
- Built Risk of Flow models for Credit Cards.
- Delivered end-to-end ML solutions in Azure Databricks.
- Presented insights to stakeholders from collections, product, and risk.
""",
    "Data Analyst, Bajaj Finserv (Mar 2021 – Apr 2023)": """
- Developed models to predict delinquency bucket movement.
- Automated reporting; saved 2 hours of manual effort daily.
"""
}

for role, details in exp.items():
    with st.expander(role):
        st.markdown(details)

# Skills
st.header("🛠️ Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Languages & Tools**")
    st.markdown("""
- Python, SQL (T-SQL, Spark SQL)
- Databricks, Jupyter, SSMS
- Excel (Advanced)
""")

with col2:
    st.markdown("**Machine Learning**")
    st.markdown("""
- Logistic Regression, Clustering
- Model Monitoring: PSI, CSI
- LangChain, HuggingFace, Generative AI
""")

# Projects Section
st.header("🚀 Projects")

projects = [
    {
        "title": "OpenAI QnA Chatbot with File Upload",
        "description": "Created an advanced QnA chatbot using OpenAI's GPT models with support for file uploads (TXT, PDF, DOCX). Users can input questions directly or upload documents for contextual answering. Features include model selection, temperature & token control, and a dark-themed Streamlit UI for an enhanced user experience.",
        "tags": ["OpenAI", "LangChain", "LLM", "Chatbot", "FileUpload", "DocumentQA", "Streamlit", "GenerativeAI"],
        "link": "https://openai-chatbot-f.streamlit.app/"
    },
    {
        "title": "LLM QnA Chatbot using LangChain & OpenAI API",
        "description": "Developed a dynamic QnA chatbot interface using LangChain and OpenAI's GPT models. The app allows users to input their API key, select models like gpt-4o-mini, adjust temperature and max tokens, and get contextual answers to queries in real-time. Built with Streamlit for an interactive UI experience.",
        "tags": ["LangChain", "OpenAI", "LLM", "QnA", "Chatbot", "Streamlit", "PromptEngineering"],
        "link": "https://openai-qna-chatbot.streamlit.app/"
    },
    {
        "title": "LLM QnA Chatbot using LangChain & Groq API",
        "description": "Built an intelligent QnA chatbot powered by Large Language Models (LLMs) using LangChain and Groq API. The system integrates prompt templates, memory, and document loaders to enable contextual, real-time question-answering over custom data. Optimized for speed and accuracy using Groq’s ultra-fast inference API.",
        "tags": ["LangChain", "HuggingFace", "LLM", "Groq API", "QnA"],
        "link": "https://qnachatbot-groq.streamlit.app/"
    },

    {
        "title": "FinBot – LLM-Powered Financial Chatbot",
        "description": "AI chatbot for understanding financial documents and FAQs using LangChain + HuggingFace.",
        "tags": ["LangChain", "HuggingFace", "LLM"],
        "link": " "
    },
    {
        "title": "Allocation Models for PLCS and SAL",
        "description": "ML models to route delinquent customers to field or telecalling teams using logistic regression.",
        "tags": ["Logistic Regression", "Customer Segmentation"],
        "link": " "
    },
    {
        "title": "Credit Card Risk Models (PDD, PreX, Write-Off)",
        "description": "Risk of flow models to prioritize recovery strategies for ~2M accounts.",
        "tags": ["Credit Risk", "Model Monitoring"],
        "link": " "
    },
    {
        "title": "Digital Payment Propensity Model",
        "description": "Predicted customer likelihood to pay digitally; improved outreach efficiency.",
        "tags": ["Classification", "Digital Collection"],
        "link": " "
    },
    {
        "title": "Reporting Automation",
        "description": "Automated reporting from Outlook to Databricks and email delivery — saved 10+ hours weekly.",
        "tags": ["Automation", "Databricks", "Python"],
        "link": " "
    }
]

##project container with button link
for proj in projects:
    with st.container():
        st.subheader(proj["title"])
        st.markdown(proj["description"])
        st.markdown(f"**Tags:** {', '.join(proj['tags'])}")
        st.link_button("🔗 View Project", proj["link"])
        st.markdown("---")

# Education
st.header("🎓 Education")
st.markdown("""
- **BE in Electronics & Telecom** – Sanjivani College of Engineering, Pune University (2019)
- **Diploma in Electronics & Telecom** – Govt. Polytechnic, Aurangabad (2013)
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Ajay Arakh | Built with Streamlit 💚")


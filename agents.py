from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=GOOGLE_API_KEY
)

# researcher
blog_researcher = Agent(
    role='blog researcher from youtube videos',
    goal="Get relevant content for the topic {topic} from the related YouTube channel",
    verbose=True,
    memory=True,
    backstory='Expert in AI, Data Science, Machine Learning and GenAI',
    llm=llm,
    allow_delegation=True
)

# writer
blog_writer = Agent(
    role='blog writer',
    goal="Narrate compelling tech stories about the video on the topic {topic}",
    verbose=True,
    memory=True,
    backstory=(
        'With a flair for simplifying complex topics, you craft engaging '
        'narratives that captivate and educate.'
    ),
    llm=llm,
    allow_delegation=True
)


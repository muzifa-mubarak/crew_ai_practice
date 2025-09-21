from crewai import Crew,Process
from agents import blog_writer,blog_researcher
from tools import yt_tool
from tasks import research_task,writer_task
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL VS Data Science'})
print(result)
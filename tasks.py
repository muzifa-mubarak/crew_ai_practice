from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

research_task = Task(
    description=(
        "Identify the video {topic} and get detailed information about it "
        "from the channel"
    ),
    expected_output="A comprehensive 3-paragraph report on the topic {topic}",
    tools=[yt_tool],
    agent=blog_researcher
)

writer_task = Task(
    description="Write a blog on the YouTube video {topic}",
    expected_output="Summarized blog content based on the video topic {topic}",
    tools=[yt_tool],
    async_execution=False,
    output_file='blog-post.md',
    agent=blog_writer
)

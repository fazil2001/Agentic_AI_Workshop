from crewai import Agent

learning_material_agent = Agent(
    role="Learning Material Curator",
    goal="Curate learning resources (videos, articles, exercises) based on topics of interest",
    backstory="An experienced content researcher specializing in finding top-quality educational content online."
)
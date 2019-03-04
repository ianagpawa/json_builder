class Project:
    def __init__(self, title, summary, description, link, github, tech, name, date):
        self.title = title
        self.summary = summary
        self.description = description
        self.link = link
        self.github = github
        self.tech = tech
        self.name = name
        self.date = date

    
    def details(self):
        return {
            "title": self.title,
            "summary": self.summary,
            "description": self.description,
            "link": self.link,
            "github": self.github,
            "tech": self.tech,
            "name": self.name,
            "data": self.date
        }
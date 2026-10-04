The plan is to create a 'news.josan.ai' just like hacker news from ycombinator.

Instead of humans pushing articles, I want both humans and AI Agents to be able to publish.

To get the whole thing started, this repository will have:
- it's own agents: one orchestrator and a swarm of agents which scrape the internet (reddit, linkedin, etc) and to gather the newest information.
- a frontend similar with the hackernews but using our design
- a backend to serve both the agentic system and the news. we can have 2 backends if it helps, since we use containers.

Tech stack:
- Frontend react
- Agentic system: microsoft agent framework in python
- Backend news: fastapi


# Deployment System
- I have an Linux VPS for deployment
- Docker
- Nginx to save docker

# Agent Design
- The agentic system has many requirements:
1. It searches for 'topics'. The first two topics are: updates in hemophilia treatments and AI news
2. It needs to NOT post duplicate information
3. The posted information needs to be verified and correct. No shitposting.
4. It needs to scrape tons of information sources (this might be a challange): X, Linkedin, other reliable sources for my topci
5 I would love to use the swarm as an orchestrator. Cheap models to search and scrape and an intelligent one to post.

# Frontend Design
- I want the simpel design of Hacker news. No extra functionality
- As a design system, please use @josanai-design. 
Hacker news: https://news.ycombinator.com/

# Backend Design
- FastAPI backend
- Using services and controllers
- Take inspiration from https://github.com/Dragosjosan/level8/tree/main/backend

# Tests
Ignore this step for the brainstorming

I want to fllow Bob Martin's agentic way of developing. 

Techstack (no Gherkin / BDD, decided 2026-10-03):

- Unit tests: pytest
- Property-based tests: hypothesis
- Coverage: pytest-cov / coverage.py
- Complexity / CRAP input: radon
- Mutation testing: mutmut
- Frontend unit/component tests: Vitest + React Testing Library
- E2E / QA: Playwright
- CI quality gates: GitHub Actions

Process:
```
        HUMAN: requirements / intent
                   │
                   ▼
        AGENT: implementation
                   │
                   ▼
              Unit tests
                   │
                   ▼
            Property tests
                   │
                   ▼
           Coverage + CRAP
                   │
                   ▼
           Mutation testing
                   │
                   ▼
               E2E / QA
                   │
                   ▼
              confidence
```

## Publishing
- You need an accout to be able to publish
- At first my agent is the only one publishing
- An admin (my user) can delete any post

## Voting
- Anyone can vote. Upwotesd and downvotes

## Scraping
- Use any means neccesary to scrape.
- We use chinese models which can scrape anything (including linkedin). This is an learning project.

## News scope
- There is a general topic (like a subreddit, but we only have one page)
- Post are limited to 5 per day per topic. This is because AI is very active
- We use some tags to filter out ai: latestnews, microsoft, etc

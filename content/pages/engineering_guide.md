Title: Engineering Guide
Slug: engineering-guide

NOTE: This is a WIP, a rough collection of my thoughts on being a Software Engineer, Managing Software Engineers, Managing Managers of Software Engineers, etc.  I will revisit and refine this over time, but I do see value in simply the collection of resources and how I feel they are applied.

[TOC]

## Introduction

Learning to be a great Software Engineer takes experience, which takes time.  You must make mistakes, but I always prefer to make new mistakes and learn from those who have already written about theirs.

Most can expect to spend 20+ years in this field, thus, the desire to downgrade titles and grant Senior roles to individuals with less than 5 years of experience conflates the meaning of the roles.  So when I refer to a Junior engineer with 5 years of experience, it's in the course of a 20+ year career and is not indicitative of title.

Wisdom takes time and experience and mistakes.

Always strive to be the pragmatic optimist in the room.  If that failes, aim for the [Techno-Optimist](https://a16z.com/the-techno-optimist-manifesto/).

## Junior Engineering Resources

Junior engineers with about 5 years of experience would bennefit greatly from the following resources.  If you try to learn these lessons too early you may not have enough experience to understand what is being taught.  Additionally, within the first few years of entering the field, there's so much being learned about how your first 1-2 companies function that additional continueing education is lost on most.

* [Simple Made Easy](https://www.infoq.com/presentations/Simple-Made-Easy/) also [here](https://www.youtube.com/watch?v=SxdOUGdseq4) is a phenomenal video by Rich Hickey on the importance of Simple and a comparision to Easy.  Our jobs as developers is to simplify as much as possible, and this task is not always easy.  How we build and discuss software, how we layer abstractions, all should drive to simplify the development and mainteance of our systems, weighed against the cost.  This is a video I recommend being reviewed often. 

* [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition) contains great lessons is how to build software and common pitfalls.  More senior engineers can also learn a great deal from this book, but much of this will have been learned on the job over the course of your career.  I read this book with about 14 years of experience and found it enjoyable but not revolutionary.  A book like this is not as helpful for fresh graduates, where there is so much thrown at you already that the lessons most likely won't stick.  This is probably worth a re-read every few years.


## Mid-Level Engineering Resources

As you gain experience you will have larger and more difficult challenges to face, your responsibility increases and the impact you have on your organization and the others around you will grow.  Mistakes you make will cost the company more money and it is increasingly more important that you provide technical direction to those more junior and guideance to those managing you and your project.

* [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) introduces the concepts of `error budget` and taking measured risks in a pragmatic fashion.  Whether or not you are a Site Reliability Engineer, the concepts of maintaining an online system with on-call, monitoring, alerting, triaging, etc, are all relevent.  This isn't a cover-to-cover book and can be consumed over time in chunks.  I do recall reading the first 2 parts (Introduction and Principles) and skipping around when you face issues that may be relevent.

* [A Philosophy of Software Design](https://www.goodreads.com/book/show/39996759-a-philosophy-of-software-design) video [here](https://www.youtube.com/watch?v=bmSAYlu0NcY) by John Ousterhout is a sucient book of how to breakdown challenges and approach the software design process.  I propose this as a mid-level book because I feel an engineer needs enough experience having observed other design medthodologies before a more formalized methods are discussed.  We had a course like this in college, and it wasn't until years into my career did revisiting this really spark an interest.

* [Deep Work and So Good They Can't Ignore You](https://calnewport.com/writing/) are directed at helping you become more effective at minimizing the noise and working on the widley important tasks required for you to succeed.  Cal Newport is a digital minimalist and true to this self-perscribed branding, he gets hypobolic about reducing all digitial noise.  While extreme, the ideas presented in this book are great to read and help software engineers focus on the task at hand.  There are so many technologies available and the desire to become proficient at all of them will make you mediocer at all.


## Senior Engineering Resources

As you approach senior+ status you will be held to a higher standard, especially when it comes to communication.  This is where many engineers start to falter, up until this point you needed to gain deeper technical knowledge, but now you need to understand more about how organizations operate, how to communicate with stake-holders, product-management, leadership, and cross-team.  The resources presented here are to help guide you in improving communication of technical details.  Someone who isn't technical isn't less competent, they are competent in different areas, you must maintain your humility to work well with others at this level.

* [Introducing EventStorming](https://www.eventstorming.com/book/) a truly remarkable concept that once implemented, will bridge the gap between `the business` and `the tech`.  This methdology is best performed not with Product Management (representatives of stake-holders) but with actual stake-holders.  This process works by diagraming the individual steps and thought processes the stake-holders perform, and removes the idea of technology from the equation.  Perhaps there are many ways to implment this, but I have found success in removing the concept of technology and discussing the raw business processes.  This gets people thinking and naming actions and systems using common language.  Expect disagreements!  Everyone across the org has their own idea of what is happening, this process is fun and engaging!

* [The C4 Model](https://c4model.com/) is my favorite way of describing both high and low level software designs.  Simon Brown also has a couple books out that I've enjoyed that help build on the C4 model concepts, [Software Architecture for Developers](https://leanpub.com/software-architecture-for-developers), [The C4 Model](https://leanpub.com/visualising-software-architecture), and [The Software Guidebook](https://leanpub.com/documenting-software-architecture).  Standardizing on a way to represent sofware within an organization will aid in collaboration and ensuring that you have

## Data Analytics

I've done my time in the data space, and approaching this from a software engineering background has given me a whole new appreciation for the isolated world we operate in.  Data Analytics has been living in the world of pre-repository up until recently.  This is a very fast-paced world compared to software engineering, mostly due to the differences between Data and Software and the rapid pace in which the Data Professionals are catching up.

* The [DataOps Cookbook](https://datakitchen.io/the-dataops-cookbook/) is by far the most influencial book in adopting the practices of Software Engineering in the Data Analytics space.  This book covers reproducibility, testing, version-control, etc.  While this all seems table-stakes for software engineering, it's relatively new for the analytics field.

* dbt's [Analytics Engineering Guide](https://www.getdbt.com/analytics-engineering/) is the way to do Analytics Engineering in the 2020s+.  This along with the DataOps Cookbook is what will allow Data Analytics to fluorish in the same ways DevOps and Version Control scaled Software Engineering. Analytics Engineering and more notably `dbt` have been the #1 driving force in reducing the toil (see SRE above) in building data warehouses, metrics, reporting, etc.  This is a nortiously messy world and Analytics Engineering is the medthological approach to fixing this.

## Management and Leadership

I have lots to say about management and leadership topics, but for now will leave you with only my two favorite books on this topic.

* [The Manager's Path](https://www.goodreads.com/book/show/33369254-the-manager-s-path) is a guidebook for engineers as they grow into managers.  We focus so much of our attention on gaining technical skills that before we know it, we're leading a team (or two) and realize we haven't spent enough time in developing our leadership skills.  All organization issues that are interesting are communication issues, by this time in your career you probably realize that the technical issues are easy to solve, trivial in many regards (unless you're a Google, Facebook, Netflix, etc).  Take the time to understand how to be managed, how to manage individual contributors, and how to manage other managers.

* [Shape Up](https://basecamp.com/shapeup) by BaseCamp/37Signals people is a revolutionary way to estimate and work in an agile environment.  While Scrum may be very opinionated and filled with ceremony, ShapeUp is aimed at giving the team tasks to work on, time-boxing, and letting them do what they do best.  You can imagine it being a 6-week sprint, where the enginers have 6-weeks to complete a major feature.  I think the best concept here for me was the hill-climbing.  At the start of a project we know the least amount possible, but at some point we can see the end, even if we have plenty of work remaining to do.  Scrum and other agile medthdologies do not capture this nuance.

* [Team Topologies](https://teamtopologies.com/book) takes an inverse approach to how organizations should be structured.  We know from Conway's Law that our software will take on the boundaries of our engineering teams, why not specify how our software should communicate (say Event Storming) and structure our teams to achieve this goal.  Team Topologies does just this, and this is a very advanced book in regards to implementation.  I expect one would need to be executive leadership or very influencial to executive leaders to make these kind of fundamental changes in an organization.  One can take the concepts in this book though and use them to drive software organiztion better.

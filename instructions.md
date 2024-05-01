Project Overview
================

You will work towards creating an
interactive, data-driven story. To extract value from large and complex
datasets, data visuals have evolved over the past decade from static
charts and graphs to interactive and immersive visuals that tell a
story. This allows the audience to modify elements of the data being
presented and manipulate the graphical representation. Static charts and graphs cannot adjust the visual, such as hovering, sorting and scaling. Interactive visualizations allow users to
generate transformative insights, identify relationships, view trends
and create meaningful stories through data.

Data storytelling is the process of describing data through
visualizations by building a compelling narrative around datasets. This
adds meaningful context to the data and helps the audience easily
understand the information.

In your work as data scientists, in addition to doing modeling and
machine learning work, you will be responsible (either individually or
as part of a team) for providing the following as part of a project:

- **Findings:** what does the data say?
- **Conclusions:** what is your interpretation of the data?
- **Recommendations:** what can be done to address the question/problem
  at hand?

Your narrative will focus primarily on the first two above. The
narrative should allow your audience to be able to understand the topic
you are analyzing, presenting and discussing.

*We do not expect you to tackle and solve a large-scale problem, that is
not the objective. However, you are welcome to offer ideas and proposals
on the topic you present*. The objective is to find a topic of interest,
work with the data, and present it to an audience that may not know very
much about the subject using a data-driven narrative.

This is your chance to show creativity and have some fun!

## Inspiration

The following are exemplary projects from prior years:

- [Avocado Violence](https://marckvaisman.georgetown.domains/503/project/avocados/index.html)
- [What makes a great buffet restaurant in Florida?](https://marckvaisman.georgetown.domains/503/project/buffets/index.html)
- [Insights on Factors of Fatal Car Accidents](https://marckvaisman.georgetown.domains/503/project/car-crashes/index.html)
- [Data visualizations to help retail investors](https://marckvaisman.georgetown.domains/503/project/finance/index.html)
- [What ingredients are you tasting in authentic Japanese
  flavors?](https://marckvaisman.georgetown.domains/503/project/japanese-cuisine/index.html)

You can also take a look at [the Juice Analytics 20 Best Data
Storytelling
Examples](https://www.juiceanalytics.com/writing/20-best-data-storytelling-examples)
for more inspiration.

## Deliverable

The project will be delivered through an interactive self-contained
website. The website and all of your code work will be stored in your 
GitHub repository. The same repository will be used
throughout the life of the project.

Think of the entire project as several parts (for different audiences):

### The Story

- The visual narrative (a website): this is the end product and your
  audience is a general audience that wants to learn something about the
  topic you are presenting.

### The Technical Approach

- The code: this is the *how*. This includes all the code used to
  process your data, build the visualizations, and produce the website.
- The presentation: this is a summary of your efforts. The audience is interested in
  understanding *what* you did and *why* you did it to get to the end
  result.

## Overall Requirements

<div>

> **Important**
>
> Please read this section carefully. There are requirements for
> different aspects of the project.

</div>

### Visualization

Your narrative must include the following elements:

- **At least five unique views**, where a *view* is a visualization
  type. A view may also contain multiple plots. For clarification, the
  following are two examples of what can be considered *5 views*:
  - One choropleth, one bubble-plot, one box-plot, one parallel
    coordinate plot, and one linked scatter-plot/histogram. This is five
    views and six plots.
  - Two choropleths, two bubble-plots, one visualization with a 3x3
    multi-variable pairplot with histograms on the main diagonal (which
    is essentially a scatter-plot/histogram), one scatter plot, three
    linked boxplots/scatterplot, two parallel coordinate plots, and two
    histograms. This is five views and twenty-one plots.
- At least one of these views should be an attempt at an **innovative**
  view**:

<div class="columns">

<div class="column" width="50%">

#### What **is** innovative

- An extension of an existing visualization type
- A novel visualization type
- Something creative, novel, difficult, interesting, and generally
  beyond *typical*. It’s probably innovative if:
  - You are surprised that you were able to pull it off
  - You are pleasantly surprised by the insights that you’re providing
    and we learn something unexpected and novel about your data,
  - It’s something hard to get working and requires a deep understanding
    of graphic objects

</div>

<div class="column" width="50%">

#### What **is not** innovative

- An interactive visualization
- Something may not be innovative enough if:
  - Getting it to work is *trivial*
  - It’s a very common plotting method
  - It can be done with 5 or 10 lines of code
  - We can google it and quickly find a template of the code that
    generated the plot
  - It was done with plotly express
  - If it is fancy and difficult, but doesn’t tell us anything, or
    doesn’t make us think about your data, or doesn’t provide some
    insight about your data in alignment with your narrative, it might
    be innovative, but it will get penalized under the “graph for
    graph’s sake” rubric

</div>

</div>

- At least two linked views. A click/hover/selection interaction within
  one view must trigger a change in a different view.
- At least one view with Interactive tooltips that are shown when users
  hover over marks.
- A formatted and/or interactive data table that presents part of your
  data in a pleasant and interactive way.

<div>

> **Important**
>
> All views and visualizations must have a purpose! Do not create a
> views just for the sake of meeting a requirement.

</div>

### Design

You must apply best practices in design:

- You narrative should have custom theming, look and feel.
- Choose appropriate color schemes and keep them consistent.
- Add appropriate narrative, captioning, etc.
- Your website and visualizations must be as self-documenting as
  possible, with appropriate labels for panes, axes, and widgets, a
  legend documenting the meaning of visual encodings, and a meaningful
  title and description.
- Your design choices may be creative and unconventional as long as they
  are serving a purpose.

### Visual narrative file

- The narrative must:
  - Be self-contained and accessible via an `index.html` file.
  - Have navigation tools, allowing the user/visitor to explore all the
    contents and always know where they are. The navigation
    implementation will depend on how you structure your site.
  - Show the title of your visual narrative, and the team members.
- You are not required to serve or deploy your website for the project.
  You may do so at the end of the semester.

### Code and Workflow

We expect to see best practices in team development and coding. All team
members are expected to contribute to the development of the project.

- All team members must commit
- Use best practices in team workflow (branches, pull requests, merges)
- Make sure that your code is well-organized and easy to read.
- Use separate files for visualization and workflow components
- Use functions to promote code reuse.
- Don’t work with a messy repo and then try to clean it up before the
  final milestone. Comment your code early on!

### Repository

- Your repository must be well organized.
- The instructors must be able to replicate all the pieces of your work.

## Tools

### Allowed

Your efforts will be purely on the data manipulation, analysis, and
presentation using R and Python with their appropriate packages that
wrap D3 or its variants and other front-end development tools
(JavaScript, D3, HTML, CSS.)

For the website, you can choose the framework/tool to build your website
(`Rmarkdown`, `Quarto`, or editing HTML directly.)

- You may use any of the packages and *wrappers* we discussed in class
  (this is not an exhaustive list):
  - [`htmlwidgets`](https://www.htmlwidgets.org) package in R
  - [`bokeh`](https://bokeh.org)
  - [`holoviz`](https://holoviz.org) and it’s accompanying ecosystem in
    Python
  - `altair` (in both [R](https://vegawidget.github.io/altair/) and
    [Python](https://altair-viz.github.io)) as wrappers for Vega-lite
  - Specialized packages for geospatial:
    - [`leaflet`](https://rstudio.github.io/leaflet/) in R
    - [`tmap`](https://geocompr.robinlovelace.net/adv-map.html) in R
    - [`folium`](https://python-visualization.github.io/folium/index.html)
      in Python
  - [NVD3](https://nvd3.org/)
  - `plotly` (in both [R](https://plotly.com/r) and
    [Python](https://plotly.com/python)) for wrapping D3.
  - [Observable](https://observablehq.com/)
  - [`flexdashboard`](https://pkgs.rstudio.com/flexdashboard/)

<div>

> **Warning**
>
> If you intend to use a package or tool not discussed in class, you
> must get prior approval from the instructional team.

</div>

- You may choose to develop the whole narrative directly in D3 and
  JavaScript, however, in class we will be focusing on showing you R and
  Python wrappers to D3 and JavaScript that will make generating
  visualizations easier.

- You may use CSS frameworks, such as
  [Bootstrap](https://getbootstrap.com/),
  [Materialize](https://materializecss.com/), or
  [Distill](https://distill.pub/about/) and include external libraries
  (jQuery, leaflet.js, moment.js, etc.).

### Not allowed

- Any server side or custom backends (Node.js, Python, etc) and database
  systems, such as Postgres or MySQL.
- [Highcharts JS](https://www.highcharts.com/)
- [Shiny](https://shiny.rstudio.com/)

## Evaluation

The project will be holistically evaluated using the following high-level criteria:

- Visual design: effectiveness of visualizations and interactions
- Level of technical difficulty and quality of implementation
- Whether the visual narrative answers a question, tells a story, and
  addresses the goals and requirements
- Quality and clarity of your writing and overall presentation,
  including your own visual style

Your group will receive an overall final letter grade for the project and written feedback.

# Final Project Milestone

## Expectations

Review the [minimum requirements](#overall-requirements) and [what tools
are allowed.](#tools)

The visual narrative will be in it’s final form. All visualizations,
narrative, navigation and theming are complete.

## Submission

Create a repository release with a tag called `v1.0-final` and
commit/push by the **due date**. [See instructions for creating releases
on
Github.](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

# Presentation

The presentation is the walk-through of your narrative and your approach. The details of the presentation and the rubric are provided on Canvas.

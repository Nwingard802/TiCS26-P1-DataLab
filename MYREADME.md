# Project 1: DataLab: Prove Something

**Topics in Computer Science · 50 points**

## Overview

Pick a question you actually care about. Build your own dataset, use Python to investigate it, and make a case for what the evidence shows.

You might test a gaming strategy, compare snack value, investigate sports performance, measure a robot, or run a simulation. Your question and dataset should reflect your interests. Everyone uses the same tools, but everyone's project should tell a different story.

Your process: **Ask a question → build a dataset → clean it → analyze it → visualize it → defend a conclusion.**

“Prove something” does not mean forcing the data to agree with you. A surprising result—or evidence that your original claim was wrong—can make an excellent project. Your job is to make a claim that your evidence can support, explain its limits, and avoid treating a pattern as proof of cause and effect.

## Learning Goals

By the end of this project, you should be able to:

- Turn a personal interest into a focused, measurable question.
- Design a dataset with meaningful rows, columns, and units.
- Use pandas to organize, clean, and analyze data.
- Use NumPy to perform a meaningful numerical calculation or simulation.
- Use matplotlib to communicate evidence clearly.
- Defend a conclusion while acknowledging uncertainty and limitations.
- Document your work so someone else can understand and rerun it.

## Choose How to Build Your Dataset

Choose one approach or combine several:

| Approach | What you could do | What to document |
|---|---|---|
| Collect observations | Record game results, product prices, or shot accuracy. | Where, when, and how you collected each observation. |
| Run an experiment | Compare paper airplane designs, robot settings, or different strategies. | What you changed, what you measured, and what you kept consistent. |
| Build from public sources | Assemble your own comparison of LEGO sets, sports seasons, songs, or other items. | Source links, access dates, and how you selected the items. |
| Generate a simulation | Model dice games, board-game movement, queues, or strategy outcomes. | Rules, assumptions, trial count, and random seed. |

You may use public data as an ingredient, but downloading a finished CSV and making two graphs is not enough. Make a meaningful contribution by collecting records, combining sources, creating a comparison, or designing a simulation. Explain what you built yourself.

**Keep it manageable and respectful:** Use safe experiments and information you are allowed to access. Do not collect names, grades, health information, passwords, or other sensitive personal information. Ask your teacher before involving classmates in data collection; participation must be voluntary and responses anonymous.

## Project Requirements

### 1. Start with a testable question

Write a short proposal before collecting your full dataset. Include:

- Your question and why it interests you.
- Your prediction, with a brief reason.
- What one row will represent and which columns you will collect.
- Your data source or collection method.
- The comparison or measurement you will use to answer the question.

Make the question specific. Instead of “What snack is best?” try “Which snacks in our vending machine provide the most protein per dollar?” Define subjective terms such as *best*, *fair*, or *successful* before analyzing the results.

### 2. Build and document your dataset

- Aim for **at least 40 observations and 5 useful columns**. If your project needs a different structure, agree on an alternative with your teacher before full collection.
- Each row must represent a clearly defined observation or trial. Each column must represent a consistent variable.
- Include numerical data and a way to compare groups, conditions, or change over time.
- Include a data dictionary explaining every column, its units or possible values, and whether it was collected or calculated.
- Save the original data and document any cleaning or exclusions. Do not silently remove results that disagree with your prediction.
- For a simulation, use enough trials to examine variation—**at least 500 trials**—and save the generated results. Simulated data supports conclusions about your model; it does not automatically establish what happens in real life.

### 3. Analyze the evidence

Use your analysis to answer the question, rather than simply displaying everything you can calculate.

- Check for missing values, duplicates, incorrect data types, and implausible values. Explain what you found and how you handled it. If no changes were needed, say what you checked.
- Produce **at least three relevant numerical results**, including a comparison between groups, conditions, or time periods.
- Consider variation as well as averages. For example, compare spread, consistency, success rates, or the number of observations in each group.
- Explain what your results mean in plain language.

### 4. Visualize your findings

Create **at least two different types of matplotlib charts** that help answer your question. Examples include a bar chart, scatterplot, histogram, box plot, or line graph.

Every chart needs a useful title, labeled axes, units where appropriate, and a legend when needed. Choose readable scales and colors. Do not distort a graph to exaggerate your result. Add a short explanation of what each chart shows and why it matters.

### 5. Defend a conclusion

Write a **300–500 word conclusion** that includes:

- A direct answer to your question, even if the answer is “the evidence is inconclusive.”
- At least **two specific numerical findings** and a reference to your charts.
- Whether your prediction was supported and why.
- At least **two meaningful limitations**, such as a small sample, biased selection, uncontrolled variables, measurement error, or simulation assumptions.
- One realistic improvement or follow-up investigation.

Separate what your data shows from what you suspect. A relationship between two variables does not, by itself, show that one causes the other.

## Technical Requirements

Use all three libraries for a real purpose. An unused import does not count.

| Tool | Required use |
|---|---|
| **pandas** | Load or create a DataFrame; inspect and clean the data; filter or sort records; create at least one meaningful calculated column; and summarize a comparison using `groupby`, a pivot table, or an equivalent operation. |
| **NumPy** | Perform at least one useful array-based calculation or simulation, such as measuring spread, calculating percentiles, comparing errors, or generating repeated random trials. Explain how the result helps answer your question. |
| **matplotlib** | Create at least two different chart types that support your analysis. Save the charts as image files. |
| **Python organization** | Use readable variable names, comments for non-obvious decisions, and at least one function you wrote for a useful part of the workflow. |
| **Reproducibility** | Make the analysis run from beginning to end using your submitted data. Use relative file paths, list required packages, and set a random seed if you use randomness. |

Do not add complicated techniques just to look impressive. Clear, correct analysis is more valuable than code you cannot explain.

## Deliverables

Submit on CL50 your final repository, which must contain:

1. **Proposal:** Your question, prediction, and dataset plan.
2. **Data:** Original data and the cleaned analysis dataset in CSV format. If the data did not need changes, one clearly identified CSV is sufficient. Include your generation code if you used a simulation.
3. **Documentation:** A README with your collection method, source links and access dates when applicable, data dictionary, cleaning decisions, and instructions for running the project.
4. **Code:** A Python script (`.py`) containing your analysis. 
5. **Visualizations:** At least two saved chart images.
6. **Conclusion:** Your 300–500 word evidence-based explanationin a separate Markdown or PDF file (saved in youir repository.
7. **Credit and AI disclosure:** Sources, outside assistance, and any AI use, included in the README.

## Presentation Expectations

Give a **3–5 minute presentation**, followed by brief questions. Slides are optional; your notebook and charts are enough.

- Introduce your question and prediction.
- Explain how you built the dataset and what one row represents.
- Show your two strongest charts and explain the main evidence.
- State your conclusion and one important limitation.
- Be ready to explain a section of your code, a cleaning decision, and how you used each required library.

Spend most of your time explaining what you learned. Avoid reading code line by line.

## Rubric — 50 Points Total

The descriptions below show what earns full credit. Partial credit reflects the completeness, correctness, and clarity of the evidence you submit.

| Category | Points | Full-credit expectations |
|---|---:|---|
| Question and project design | 5 | Focused, measurable question; clear prediction and rationale; workable proposal that defines observations and comparisons. |
| Dataset and documentation | 10 | Student-built dataset meets the size/structure requirements or an agreed alternative; collection or generation method is clear; sources, column definitions, units, and cleaning decisions are documented. |
| Python analysis | 15 | **pandas (5):** required operations are correct and useful. **NumPy (4):** meaningful numerical calculation or simulation is correct and explained. **Analysis and code quality (6):** at least three relevant numerical results, including a comparison and attention to variation; readable code, a useful student-written function, and a reproducible workflow. |
| Visualizations | 8 | Two different, appropriate chart types support the question (4); titles, labels, units, legends when needed, readable design, and accurate interpretations make the evidence clear (4). |
| Conclusion and critical thinking | 7 | Direct answer supported by specific numerical findings and charts (4); thoughtful discussion of the prediction, at least two limitations, and a realistic next step (3). |
| Presentation and submission | 5 | Clear 3–5 minute presentation and informed responses to questions (3); complete, organized submission with run instructions and credit/AI disclosure (2). |
| **Total** | **50** | |

Your score depends on the quality of your investigation, not whether your prediction turns out to be correct.

## Suggested Project Ideas

Use these as starting points. Narrow the question and make the investigation your own.

- **Does my Mario Kart setup matter?** Compare finish positions or lap times across setups while accounting for course differences.
- **Which snack gives the best value?** Build a local price dataset and compare cost per ounce, protein per dollar, or a clearly defined rating.
- **Can I predict my phone's battery use?** Record battery change over timed activities and compare drain rates.
- **Which paper airplane is most consistent?** Compare repeated flights of several designs using distance and variation.
- **Is a board game mechanic fair?** Simulate dice rolls or movement and compare outcome frequencies.
- **Which basketball spot is my strongest?** Record repeated shooting sessions and compare success rates with sample sizes shown.
- **What makes a robot more accurate?** Compare settings across repeated trials while keeping other conditions consistent.
- **Are larger LEGO sets a better deal?** Assemble a dataset and compare price per piece across sizes or themes.
- **How do songs in my playlists differ?** Build a dataset of duration, release year, genre, or your own clearly defined ratings.
- **Which game strategy wins most often?** Write a simulation, test several strategies, and explain what your simplified rules leave out.
- **Does typing speed trade off with accuracy?** Run repeated timed trials with different text types or conditions.
- **Which sports statistic best matches success?** Define success, build a comparison dataset, and investigate relationships without claiming causation.

## Academic Integrity and AI Use

This is an individual project. You may discuss ideas and help classmates troubleshoot, but your question, dataset-building decisions, analysis, and explanation must reflect your own work. If you share any collected data, identify the contribution of each person and get teacher approval first.

Credit public datasets, websites, tutorials, and borrowed or adapted code. Label simulated or synthetic data clearly. Never invent observations and present them as measurements you collected.

You may use AI to brainstorm questions, explain library functions, suggest debugging steps, or review your work. You are responsible for checking its suggestions and understanding every line you submit. Do not submit an AI-generated project or conclusion as your own work. **YOU ARE RESPONSIBLE FOR EVERY LINE THAT YOU SUBMIT**
- If I feel as though you may have used AI without crediting, I reserve the right to print your code and have you comment by hand

In your README, name any AI tools you used, briefly describe what you used them for, and identify the code or decisions they influenced. Include the relevant prompts or a short interaction summary. If you did not use AI, write **“No AI tools used.”** Be prepared to explain or modify your code and defend your interpretation without AI assistance.

## Before You Submit

- [ ] My question is specific, and my dataset can help answer it.
- [ ] I documented how I built and checked my data.
- [ ] pandas, NumPy, and matplotlib each do meaningful work.
- [ ] I included three numerical results, a comparison, and attention to variation.
- [ ] My two chart types are readable and useful.
- [ ] My conclusion uses evidence and acknowledges limitations.
- [ ] My code runs from beginning to end using the submitted files.
- [ ] I included all deliverables, credited help, and disclosed AI use.
- [ ] I can explain my work in 3–5 minutes and answer questions about it.

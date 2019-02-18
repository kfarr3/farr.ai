Title: Measuring and Managing Information Risk
Date: 2018-02-21
Category: Blog
Tags: Book Review; DataScience;
Slug: measuring-and-managing-information-risk
Status: published

![Measuring and Managing Information Risk Book Cover]({static}/media/2018/MMIR.jpg){ width=400px }

Seldom does one read a business book with humor, and often that humor is so atrocious, it's best left out.  This is perhaps one of the most unassuming business book I've read.  To top it off, it's on Information Technology/Systems Security!  [Measuring and Managing Information Risk](https://www.amazon.com/Measuring-Managing-Information-Risk-Approach/dp/0124202314)  highlights the inner workings of the FAIR approach: Factor Analysis of Information Risk.  In complete disclosure, I picked this book up in anticipation of working with the author.  I have since accepted said job and now set forth to comprehend the workings of both this book, the FAIR standard, and my new colleague Jack Jones, said co-author of this book.

# Chapter 1: Introduction

Like any good book, this one starts at the beginning.  A brief introduction to concepts of *threat, vulenerability,* and *risk.*  Perhaps the best thought experiment consists of the following.  For each of the following risk scenarios that follow, ask yourself how much risk each have.

* A car tire so bald that you cannot discern that it ever had tread.
* Said car tire, tied to a rope hanging from a tree branch.
* Said rope, frayed halfway through
* Said branch, suspended over an 80-foot cliff with sharp rocks below

How much risk is in each scenario?  Jack presumes there is NO RISK in ANY of these scenarios.  Why would anyone care if an old tire falls off a cliff?  There's no loss, no harm, no human in these scenarios.  The point here is to help focus your thinking to the events at hand, brush aside bias and assumptions and analyze he situation as it exists.

This chapter continues with a defense of the FAIR practice.  Current risk analysis methods are often quite qualitative without answering the three basic points:

* Is it useful?
* Is it practical?
* Are the results defensible?

FAIR was designed to be **useful**, **practical**, and **defensible**.  How useful is a risk level of Medium?  Or 2.1?  How much difference is there between a risk level of 3.7 and 3.6?  FAIR quantifies risk by turning it into something practical and useful, a dollar figure.

# Chapter 2: Basic Risk Concepts

Jumping into chapter 2 the authors focus on defining terms often associated with risk assessments.  Unfortunately there is little consolation between different authors (or even some authors within the same book) regarding such terminology.  The first is probably one of of my favorite discussions since even before this book: Possibility vs Probability.  Often a scenario is possible, but with a very low probability.  Such events, struck by lightning, are not worth a terrible amount of time.

Prediction is another common concept.  Since FAIR transforms risk assessment into a annualized loss in dollars (or any currency), it's common for one to assume that FAIR is making a prediction, when in fact it is just posing a *temporally-bound probability*.  If a threat event is likely to occur once every 10 years and cost 10 million dollars, then it has an annual cost of 1 million dollars.  This does not mean that every year the threat event will cost you 1 million dollars, or that you won't go 13 years without a threat event.  A FAIR analysis cannot force a threat event, but it can provide as close approximation of expected costs, which is much better than a medium risk of something happening.

There is extensive coverage of subjectivity (not as bad as you'd expect) vs objectivity and of course precision vs accuracy.

# Chapter 3: The FAIR Risk Ontology

There are very few ways to sum this chapter up without adding more text than was found in the book.

![FAIR Ontology]({static}/media/2018/fair_ontology.jpg){.alignnone .size-full .wp-image-281 width="750"}

Essentially, Figure 1 lays out the FAIR Risk Ontology.  Risk is composed of Loss Event Frequency and Loss Magnitude.  Both of these numbers are technically a range with min, max, and expected values.  Each also gets broken down into further sub-components that are used to estimate the parent numbers.

Threat Event Frequency and Vulnerability influence the Loss Event Frequency.

Contact Frequency and Probability of Action influence the Threat Event Frequency.

Threat Capability and Resistance Strength influence Vulnerability.

On the other side of the tree, Primary Loss and Secondary Loss influence the Loss Magnitude.

And secondary Loss Event Frequency and secondary Loss Magnitude influence the Secondary Loss.

The idea here is that someone implementing FAIR can dig as deep as they need to in order to estimate the numbers correctly.  An organization with an advanced threat and loss system may be able to simply plug numbers directly into the Loss Event Frequency and Loss Magnitude inputs and have a useful result.

# Chapter 4: FAIR Terminology

I actually worked through this chapter twice.  There are a lot of subtleties that one must get correct for the rest to continue making sense.  The book asserts that the risk analysis profession is still in it's infancy and doesn't have a mature vocabulary; at least an agreed upon vocabulary.  This chapter is that vocab, and each term is represented with multiple examples and common misconceptions.  Yes, enough thought went into this chapter that it even includes ways you're probably reading it wrong.

* **Assets**: Thing we value
* **Threat**: An actor capable of causing loss
* **Threat** Community: Group of individual actors capable of causing loss, i.e. Organized Crime, Nation States, Insiders, etc
* **Threat Profile**: Collection of threat demographics, intentions, and preferred modes of attack
* **Threat Event**: Occurs when a threat actor acts in a manner that can cause loss
* **Loss Event**: a threat event that end in loss or where liability increases
* **Vulnerability Event**: An event that increases vulnerability
* **Primary Stakeholders**: Those affected by a loss event immediately
* **Secondary Stakeholders**:  Those affected after a loss event peripherally: customers, business partners, government regulators, etc
* **Loss Flow**: The order in which loss events affect stakeholders and assets
* **Forms of Loss**: Productivity, Response, Replacement, Competitive Advantage, Fines and Judgments, and Reputation

Well, there you have it, everything you need to understand the rest of this book.  Honestly though, I felt this chapter was the cementing of terminology and vocabulary, the point where one can start to appreciate the domain more thoroughly.  Since I am not a Subject Matter Expert on either Security, Information Technology, or the like, this book is helping bridge the gap and this chapter the keystone.

# Chapter 5: Measurement

How long is an inch?  About 3 centimeters?  The theme of this chapter is forethought (like most chapters).  Before you can measure anything, you need to know how precise your measurements need to be.  If you're measuring a mile, then +/- a few inches is acceptable, measuring something a foot long?   Perhaps +/- a few inches is not so acceptable.

A second concept in this chapter is estimation, since very often one does not have enough data to accurately measure an unknown event we need to estimate.  The authors persuade you to move away from a single-point estimation to a range, and in this range, one can make it large enough to be highly accurate.  Of course, too large a range and our precision plummets and the estimate is useless.

Often it's difficult to estimate something when it's so far outside of your experience.  When this happens, use an absurd value to start narrowing it down.  For instance, how far away are you from the nearest coast?  If you're unsure, perhaps you can start with 0-25,000 miles.  If you're on the coast, well, then 0 is pretty accurate, otherwise, it's impossible to be more than 25,000 miles from the coast since that's the circumference of the Earth (you are on Earth right, hello Musk!).  From here you could start to increase 0 to a positive value that you feel confident in.  We can almost immediately half the maximum value since it's so preposterous.  The point here is that in the "I don't know" event, there is always a starting point that is better than N/A.

# Chapter 6: Analysis Process

The FAIR analysis process consists of 5 steps leading to a Risk value.

* Identifying scenarios
* FAIR factors
* Expert Estimation
* PERT (Program Evaluation and Review Technique)
* Monte Carlo engine

## Identifying Scenarios

Properly scoping scenarios is the foundation of a FAIR analysis.  Fitting that it's the first step.  This involves identifying the asset at risk, threat communities, threat type, and effect.

![Identifying Assets]({static}/media/2018/identifying_assets.jpg){.size-full .wp-image-290 .aligncenter width="581" height="138"}

## Fair Factors

The book wasn't clear what Fair Factors meant.  This was less than a page that essentially listed the importance of each of the previous four items.

## Expert Estimation and PERT

These were grouped together in the book and essentially revolved around estimating Threat Event Frequency and Threat Capability for each scenario.  Then structuring a Loss table for each for each of the 7 forms of loss: Productivity, Response, Replacement, Fine and Judgement, Secondary Response, Competitive Advantage, Reputation.

![Expert Estimation]({static}/media/2018/fair_estimates.jpg){.size-full .wp-image-291 .aligncenter width="567" height="79"}

## Monte Carlo Engine

This part is pretty straightforward.  Taking the ranges of inputs from the Fair Factors and PERT section, run a Monte Carlo simulation and observe the results.

And there you have it, essentially a FAIR analysis.  Stay tuned!  There's more to come!

# Chapter 7: Interpreting Results

Now that one has their Risk Results, what do you do with them?  The output of the Monte Carlo engine is a Minimum, Average, Most Likely, and Maximum loss exposure.  Loss exposure is denoted as both an Annualized Loss Exposure and Single Loss Exposure.  Both are important and are used in conjunction by stakeholders to make planning decisions.

Often it's useful to convert the quantitative output into a qualitative scale for quick decision making.  In these cases it's important to find a loss table that maps loss ranges to qualitative enumerations, keeping in mind that the organization's risk levels should be the driving factor, not the output of the engine.

Depending on the organization, splitting the risk assessment by departments or even loss type (financial, reputation, etc) is helpful.  Some departments or organizations are more concerned about a specific loss type and that should be highlighted in a way the can quickly and correctly understand what is at risk.

It's possible that a FAIR analysis can be rather sensitive to a change in events.  For instance, a very low Threat Event Frequency with little to no Resistive  Controls is very sensitive to any increase in the Threat Event Frequency.  This is a second-level thought pattern that one should be looking for.  It's also important for the people running the analysis to make sure the numbers feel intuitively correct.  If they do not, it's best to revisit both the numbers and the intuition and discover the disconnect.  Perhaps a number was miscalculated, or perhaps a better understanding of FAIR is required, either way, intuition is there as a secondary check.

# Chapter 8: Risk Analysis Examples

Chapter eight was a very hearty chapter with 11 different examples of analyses.  This is akin to a cookbook or analysis pattern reference section.  While none of these examples will directly map to a specific circumstance, they get one started off in the correct direction.  As with any task, the more analyses performed, the quicker they become as patterns emerge.  This chapter attempts to address the most common analysis patterns.

This chapter seems tedious since each example is a full example, not building upon any previous examples.  This lends itself well to being used as a reference guide as opposed to a chapter one memorizes.  The following scenarios were analyzed.

* Inappropriate Access Privileges
    * Privileged Insider/Snooping/Confidentiality
    * Privileged Insider/Malicious/Confidentiality
    * Cyber Criminal/Malicious/Confidentiality
* Unencrypted Internal Network Traffic
    * Privileged Insider/Confidentiality
    * Non-Privileged Insider/Malicious
    * Cyber Criminal/Malicious
* Website Denial Of Service
    * Analysis
    * Basic Attacker/Availability

# Chapter 9: Thinking about Risk Scenarios Using FAIR

Thinking in a FAIR manner is the first step to a successful and useful risk analysis and mitigation approach for any organization.  Even if your organization isn't ready to take a fully quantitative approach to risk analysis, focusing on some key components of FAIR can improve whatever existing system is in place.

This chapter uses some interesting examples to approach a FAIR analysis without ever using numbers.  Strictly speaking these are qualitative analysis, however they are superior to typical qualitative approaches because at least the critical thinking and vocabulary of FAIR are used when coming up with an report.

The following examples were analyzed using a qualitative FAIR approach.

* Web Application Risk
* Contractors
* Production Data in Test Environments
* Password Security

Moving forward, a Basic Risk Analysis Guide (BRAG) offers a semi-quantitative approach to FAIR, where rough numerical ranges are used as input to a qualitative selector.  The steps in BRAG are as follows.

* Step 1: Identify the asset(s) at risk
* Step 2: Identify the threat community
* Step 3: Threat effect frequency
* Step 4: Threat capability
* Step 5: Difficulty
* Step 6: Vulnerability
* Step 7: Primary loss event frequency
* Step 8: Secondary loss event frequency
* Step 9: Estimate primary loss magnitude
* Step 10: Estimate secondary loss magnitude
* Step 11: Derive and articulate primary and secondary risk
* Step 12: Derive and articulate overall risk

# Chapter 10: Common Mistakes

FAIR brings about new terminology and a new mindset to Information Security risk analysis, with this, mistakes and problems.  The most common mistakes are categorized as follows:

* Checking results
* Scoping
* Data
* Variable confusion
* Vulnerability analysis

Sanity checking results is probably the most useful thing anyone can do in any type of functional work.  Programmers do it in the form of Unit Testing software, Scientists do it by dimensional analysis, and so on.  If a risk amount ends up being more than a company is worth, there's an obvious problem there.

Scoping analyses has one of the largest initial hurdles to overcome.  It's easy to dive too deep into the FAIR ontology, or go to wide by scoping every possible type of attack.  Adjust scope mid analysis is acceptable, especially since doing so is probably indicative of you having a better understanding of the problem.  Just make sure you go back and re-calculate any previous values once the re-scoping is finished.

Bad data in produces bad data out.  Some common forms of bad data include getting loss magnitude data from unreliable sources, not challenging your own assumptions, and not calibrating the inputs.

Some variables are easy to get confused about initially.  Mistaking contact frequency for threat effect frequency, or threat effect frequency for loss event frequency, or mistaking response losses for productivity losses.  In addition, confusing secondary loss with primary loss or confusing reputation damage with a loss in competitive advantage.

Vulnerability analysis is the last common mistake and is mostly a specific form of variable confusion.  This is where someone incorrectly enters a value into the wrong field.  Diligence and attention to detail are imperative when working with so much new vocabulary.

# Chapter 11: Controls

Controls are put in place in order to help increase threat prevention, detection, and response.  In an ideal world, 100% prevention would negate the need for any detection or response.  Contrary, 100% detection and response would negate the need for any prevention.  Unfortunately, we live in a world with neither begin perfect and a balance between the three is required.

This chapter introduces a new ontology for Loss Event Controls that help focus on the three leading inputs: Prevention, Detection, and Response.  By mapping out one's control ontology, weaknesses can be spotted and improved.

Variance Controls are also introduced in this chapter.  A Variance is the difference between an ideally secure system and the real-world system.  Based on the concept that a 100% secured system, following all best-practices, and being fully updated and patched is free from loss-events.  Thus, the variance is the amount that a system is 'off' from it's 'ideal' state.  Variance also has it's own, similar, ontology that includes Prevention, Detection, and Response, though those values are derived quite differently than the Loss Event Controls ontology.

Decision Making Controls is the last controls topic in this chapter.  Again, with it's own ontology where Prevention is replaced with Enablement.  These decisions fall into one of three categories: Strategic, Operational, and Incident management decisions.  An executive versed in the Decision Making Controls ontology should theoretically be better fitted to making risk-aware decisions.

# Chapter 12: Risk Management

Risk can be managed both implicitly and explicitly.  Implicitly managed risk happens when an organization follows a checklisted guideline provided by another organization.  Often these guidelines or standards place unneeded or useless burdens on an organization resulting in policy exceptions in the best case, or policy neglect in the worst case.  While implicit risk management is better than nothing, explicitly managing your company's risk is the most cost effective way to lower risk, and lower the right kind of risk.

Risk Management is defined as: *The combination of personnel, policies, processes, and technologies that enable an organization to cost-effectively achieve and maintain an acceptable level of loss exposure.*

The Risk Management Stack requires **Accurate Models** in order to make **Meaningful Measurements** so that one can make **Effective Comparisons** in order to mark **Well-Informed Decisions** which leads to **Effective Risk Management.**

Making well-informed decisions leads to effective risk management.  These decisions require setting expectations first.  One must know where they are going in order to plot a course to get there.  Once goals are established, they must be prioritized, every company (well, perhaps except Apple) have limited resources and focus should be given to the policies that will provide the greatest benefit to the company.  Finally, selecting the correct solution.  While your first idea is most often not your best, the first solution is probably not the best for the company.  Identify and review possible solutions and select the best fit.

Risk Management requires a feed-back loop to be effective.  Much like a PID loop (Proportional, Integral, Derivative), one must determine their variance between intended and actual risk levels and adjust accordingly.  Typically the variance is caused by lack of awareness of policies, lack of capabilities (responsibility with no authority) to implement the policies, or lack of motivation (carrot v stick).  Identifying which source is limiting the policies from going into full (or near full effect) will help minimize your variance.

# Chapter 13: Information Security Metrics

The idea of identifying Key Risk Indicators and Key Performance Indicators shouldn't come as a surprise in a quantitative risk analysis book.  When choosing metrics, keep the GQM in mind, Goal, Question, Metric.  Identify the Goal, Question how to achieve the Goal, and specify the Metric used to measure the goal.

Gaining visibility into your organizations risk landscape is important.  This requires asset visibility, how many, their location, their usage, etc.  Next threat visibility should focus on threat event frequency and threat capability.  Follow that up with control visibility, understanding what kind of controls are in place already and their variance.  Next, impact factors are organization dependent and can include items like stock price, cost of capital, compliance requirements, etc.  Finally, visibility analysis is used to gauge and manage your risk landscape.  Common areas of observation include servers, web applications, network devices, databases, etc.

# Chapter 14: Implementing Risk Management

The last chapter dives into how to implement a risk management strategy.

The FAIR-Based Risk Management Maturity Model consists of five levels:

* Level 1 - Chaotic, decision making is largely a free-for-all with no Key Risk or Performance Indicators
* Level 2 - Implicit - risk is managed by adhering to industry standards that may not fully apply
* Level 3 - Early Explicit - Analysis are performed and used, much may still be qualitative
* Level 4 - Mature Explicit - A focus is on risk management, KPI/KRI fully established and used in decision making
* Level 5 - Purely Explicit - Strategic and Operational decisions are made using based on the organizations risk appetite.

Software used to monitor Governance, Risks, and Compliance can be useful if used correctly.  Using the concepts learned in this book will help your GRC solution live up to its promise.

Root Cause Analysis is mentioned as a way to diagnose a loss-event and determine what controls were inadequate in an attempt to fix the system.  The RCA process consists of:

* Expectations - are expectations documented?
* Awareness - Is everyone aware of the policies?
* Capabilities - Does everyone have the capabilities to adhere to the policies?
* Choice - Did someone fail to choose to adhere to a policy?
* Documentation and Metrics - After determining the Root Cause, it must be documented and mediation efforts put in place.

The most useful metric the book mentions is asset level control variance.  If there were no other metrics available, knowing how far away you were from ideal controls would help gain operational insights.
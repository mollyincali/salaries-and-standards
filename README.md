# Salaries and Standards

***Do teachers who work in districts with higher salaries have students who score proficient or higher on state testing?***

**Questions to explore**
- Do districts with higher salary have higher test scores?
- Which county in California has the highest average teacher salary?
- Which county in California have the highest percentage of students meeting or exceeding standards?

**Data sources** 
- Three data sets were taken from California Department of Education from the 2018 - 19 school year.
    1. Data set on all Smarter Balanced (SBAC) scores of students in both ELA and Math for the State of California
    2. Text file identifying the codes used in SBAC data to identify County, District, and School by name
    3. Data set on teacher salary by Districts in the state of California

![title](images/infographic.png)

**Data description** 
- State testing data is in a large CSV file with over 2 million rows and over 30 columns such as: District code, School code, Grade, Percentage Standard Met, Percentage Standard Nearly Met, Area proficiency, etc.
- There is an additional District and School CSV that identifies the County, Distict, and School Names with their specific code in the SBAC file
- Students scores will fall into one of four groups: 
    - Standard exceeded
    - Standard met
    - Standard nearly met
    - Standard not Met
- For the purpose of this data exploration we are only interested in students who fall into the "exceed" or "met" category. 
- The terms "proficient" and "standards met" are interchangeable 
- Teacher salary data reports aggregated data on the lowest, average, and highest reported salary for each district in California
- Teacher salary data only matches up to the SBAC data by District Name, which can take on many forms. 

**Common Terms**
- Counties ---> Districts --> Schools
- There are 58 Counties in California with over 900 Districts. Each District has their own number of schools and serve anywhere between 596,937 (Los Angeles Unified) to 4 students (Panoche Elementary)
- Districts that education students in grades TK - 12 typically have "Unified" in their name
- Districts that educate students in grades TK - 8 can either go by "Union" or "Elementary"
- Districts that educate students in grades 9 - 12 generally have "High" in their name
- Students in grade 3 - 8 and 11 will take both the ELA and Math SBAC (Smarter Balanced Assessment Consortium)
- Some students with special needs will take a modified version, and are not accounted for in this analysis

**Data Exploration**

We will begin by looking at the money. 700 district salaries is a lot of for one bar chart, so lets look at each District in each County and find the highest average salary offered in that County. You'll find the median salary running across the middle of the graph so we can see which counties fall above or below that line.

![title](images/salary_bycounty.png)


Now let's at a look at each district's average teacher salary vs the percentage of students who met or exceeded standard in that same district.

![title](images/scatterpay_met.png)

The above graph is alot - in fact, it is over 8,000 dots! Lets group each District and look at them individually and see how that District's average salary compares to the percentage of students who met or exceeded standard for the whole county. 

![title](images/scatterpaybydistrict.png)

**Hypothesis Testing**

- After examining the graphs above we can see that as we move along the x-axis the scores do increase, but to better understand the correlation we'll take a look at some correlation heat maps.

<img src="https://github.com/mollyincali/teacher-pay/blob/master/images/corrmathpng.png" width="400" height="350"><img src="https://github.com/mollyincali/teacher-pay/blob/master/images/correla.png" width="400" height="350">

- This tells us that ...

- Great! Now that we have our student scores seperated out by ELA and Math let's get to our main question. **Do teachers who work in districts with higher salaries have students who score proficient or higher on state testing?** The title of this exploration is salaries and standards after all.

- Next thing is to seperate out both ELA and Math data frames into "top paying districts" and "bottom paying distict." We'll do that easily by having our cut off be the median. 
*image 

- Lets seperate out the top paying districts from the bottom paying districts by splitting them at the Median and see how their students perform on both ELA and Math tests. We have fairly equal data frames of about 2100 districts in each, lets run a t-test with the standard alpha level of 0.05 to test our null hypothesis that was created prior to seeing any of this data.

*Null Hypothesis: Students from top paying districts score the same as students from lower paying districts.*

*Alternate Hypothesis: Students from top paying districts score better than students from lower paying districts.*

- We will run this test for both ELA and Math
- When we perform the t-test with scipy.stats for our ELA scores we get a p value 5.484 e-64. WOW! That is significantly less than our alpha score which tells us we can reject our null hypothesis and accept the alternate.
- The results of our t-test with scipy-stats for our Math score is a little different, we receive a p-value of 1.4068 e-60. Another significat number, telling us we can reject our null hypothesis and accept the alternate.

*Students from top paying districts DO score better than students from lower paying districts.* 
- In fact, when we look at ELA scores the mean of students who score proficient or higher from top paying districts is 55% compared to 46% of students from lower paying districts. For math, the average number of students who score proficient or higher from top paying districts is 45% and those from lower paying districts is 35%.

![title](images/histbytopbottom.png)

- Lets look at just one more graph to really hit this idea home. The CDF of each test comparing the top and lower paying districts.

![title](images/cdf.png)

- Okay one last graph, saved the best for last!

<img src="https://github.com/mollyincali/teacher-pay/blob/master/images/avgsalary.png" width="400" height="350"><img src="https://github.com/mollyincali/teacher-pay/blob/master/images/percentmet.png" width="400" height="350">

**Conclusion**
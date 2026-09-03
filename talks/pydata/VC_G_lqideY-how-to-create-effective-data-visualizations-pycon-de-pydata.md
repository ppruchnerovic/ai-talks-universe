---
id: VC_G_lqideY
title: "How to create effective data visualizations [PyCon DE & PyData 2026]"
slug: how-to-create-effective-data-visualizations-pycon-de-pydata
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Dominik Haitz"]
channel: null
duration_min: 30
published_at: 2026-08-04T22:20:47Z
video_id: VC_G_lqideY
url: https://www.youtube.com/watch?v=VC_G_lqideY
youtube_url: https://www.youtube.com/watch?v=VC_G_lqideY
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# How to create effective data visualizations [PyCon DE & PyData 2026]

**Dominik Haitz**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VC_G_lqideY) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Senior Data Scientist Dominik Haitz reveal the fundamental principles and Python tools needed to transform raw data into impactful, professional visualizations.

Speakers:
Dominik Haitz

Description:
Effective data visualization requires a clear, written message to guide the audience, often integrated directly into the chart title. A robust mental model for this process is the grammar of graphics, which treats visualization as a mapping of data variables to visual properties, such as encoding a category as a color or a numerical value as a position on an axis. To improve accessibility, designers should employ a visual hierarchy, using size, boldness, and contrasting colors to highlight primary data points while graying out secondary information.

Color selection must align with the data type. Categorical data requires contrasting colors, while diverging data—such as correlation coefficients—should use a neutral center. Sequential data is best represented by monochrome or perceptually uniform color maps; rainbow color maps are discouraged because they lack intuitive ordering and create artificial edges. Cognitive science indicates that humans perceive differences in position and length more accurately than area, volume, or color. Consequently, bar charts are generally superior to pie charts, which should only be used to show simple fractions of a whole, such as 25% or 75%.

In Python, Matplotlib and Seaborn are standard for high-customization or academic scientific plots. For interactive exploration and dashboards, Altair and Plotly Express are preferred due to their adherence to the grammar of graphics and native interactivity in notebooks. For massive datasets containing millions of points, the HoloViews ecosystem, specifically Datashader, provides the necessary performance. For presenting raw values with minimal visualization, Great Tables allows for the programmatic creation of professional tables.

⭐️ About PyCon DE:
PyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for collaboration, knowledge sharing, and innovation.

The PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.

PyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.

•  Newsletter: https://2027.pycon.de/newsletter/
•  LinkedIn: https://www.linkedin.com/company/pyconde
•  X: https://www.x.com/pyconde

Links:
• Conference website: http://pycon.de
• Other sessions: https://2026.pycon.de/talks/

The conference was organized by
• Python Softwareverband e.V.: http://pysv.org
• Pioneers Hub gemeinnützige GmbH: http://pioneershub.org
in collaboration with NumFOCUS Inc.: http://numfocus.org

If you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.
Share this video with your network to spread the knowledge!

Hashtags:

Acknowledgements:
Special thanks to all the volunteers and sponsors who made this event possible.

About:
Python Softwareverband e.V.:
PySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.

Pioneers Hub gemeinnützige GmbH:
is a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.

NumFOCUS Inc.
supports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable development and collaboration.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

## Transcript

*3,812 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=VC_G_lqideY&t=5s)** Yeah, thank you. Um, welcome everyone to this talk about data visualization. It's actually one of my favorite topic and since it's very visual and colorful, it's also very accessible and lightweight. So, I hope you have a lot of fun during the talk and learn something along the way. The talk is divided into three parts. The first part will be about some general principles that will help you design better visualizations. The second part will be mostly about some practical tips and tricks like the usage of color or the advantages of different chart types. And the third part will then be about how to put all this knowledge to work with Python. So let's start with the most important

**[0:56](https://www.youtube.com/watch?v=VC_G_lqideY&t=56s)** thing that should be at the core of your visualization efforts. That is the message you want to bring across. Now I could just show you a chart like this one. Actually this one here is super interesting. It's about money and happiness. On the x- axis you have the GDP per capita of different countries and on the yaxis you have the life satisfaction self-reported from surveys and if you have a closer look there's a lots of interesting insights to take away from this so I could just leave you with this charts but in general the data visualization is more effective

**[1:46](https://www.youtube.com/watch?v=VC_G_lqideY&t=106s)** If I have a clear message I want to bring across something like uh hey the happiness increases with money but it levels off after a certain amount. So the first thing is that I'm really conscious about the message I want to bring along and structure my child or my presentation accordingly. better to be really conscious about this. Write the message down and at best write it down on the chart, maybe as a chart title. So you might think this is redundant because the message is already included in the data, but it actually helps to drive the point home, especially when your audience, as is mostly the case, is not as familiar with the data as you

**[2:33](https://www.youtube.com/watch?v=VC_G_lqideY&t=153s)** are. write it on the chart and use additional design elements like highlighting or annotations to further support the message. So now we have a clear message, but what's also super helpful is to have a clear mental model about how data visualization works. And what helps us here what I think super um useful is an approach based on the grammar of graphics. So the grammar of graphics is originally a book from by Leland Wilkinson written in 1999 very comprehensive overview of um describing a a structure or a system of data

**[3:22](https://www.youtube.com/watch?v=VC_G_lqideY&t=202s)** visualization and was famously adapted by the person on the right here in the design of its gtgplot package for R who's and the accompanying tidyiverse ecosystem which you may have heard of which also influenced later packages in other programming languages. So um what this means um very simplified and practically broken down is that if you have data like this a data set with different variables as data frame columns you can think about visualization as an mapping or encoding of the variables in your data on the data frame columns to um the visual properties of your chart.

**[4:13](https://www.youtube.com/watch?v=VC_G_lqideY&t=253s)** For example, here you have the length and depth variables in your data mapped to the X and Y positions of the scatter point. And additionally, the species category mapped to the color of the scatter point. I think this is a very simple clean approach that makes for a great mental model of data visualization and leads to clean interfaces and clean code. Like the actual code for ggplot here would be as simple as um what I just described here. You take the data frame, map or encode its columns into visual properties for the specific chart point. And there you

**[5:00](https://www.youtube.com/watch?v=VC_G_lqideY&t=300s)** have it, a very nice descriptive um way to think and think about data visualization and write the code and the interfaces accordingly. So now we have a clear message and a clear structure to describe our charts. But we still need to make it um more accessible to our readers. And what can help us here is a design principle called the visual hierarchy. So here you have two website mockups. The one on the left is really cluttered and um you don't really know where to look. Whereas the example on the right is much better

**[5:47](https://www.youtube.com/watch?v=VC_G_lqideY&t=347s)** structured with certain elements that really grab your attention first. And this is what the visual hierarchy describes. Certain visual elements are more prominent by the usage of color, larger size, boldness, and grab your attention first. whereas other elements um by using smaller size or graying them down move into the background. So instead of having all visual elements on the same layer and throwing everything at the viewer at the same time, you can influence the order in which the viewer um perceives the different elements of your chart and processes them thereby guiding them through your visualization and making it more accessible.

**[6:40](https://www.youtube.com/watch?v=VC_G_lqideY&t=400s)** So one example where these principles work quite well is this visualization here. It's from the BBC and it describes you see it already the chart title the takeaway message ocean temperatures highest on record. This was the sea surface temperatures in 2023. And you can see probably after the headline what you notice first is the prominent data point and line highlighted in red. So these are the elements that um you notice first while the other data lines representing all the previous years are grayed out and move a bit into the background. So I think quite a nice example of um the um structuring your chart, making it accessible and also adding additional

**[7:32](https://www.youtube.com/watch?v=VC_G_lqideY&t=452s)** annotations or highlighting to make the data, you know, this is scientific data here and via these um comments, it's made accessible to a broader audience. So however here in this chart we only have regarding colors we only have gray and red. Usually you have a lot more colors for your vis visualization. What's to consider regarding the usage of color and the proper color choice depends on the type of data you have at hand. So quite often you may have categorical data as you see on the left here. Best choose some contrasting use probably colors that are pleasing and not too

**[8:22](https://www.youtube.com/watch?v=VC_G_lqideY&t=502s)** bright or harsh on the eye. However, nowadays most graphics programs provide sensible defaults. Here there's diverging data like data that is centered around a middle value zero or one and diverges in both directions. Think of correlation coefficients or the visualization of a correlation matrix. So on best choose a color map here with a neutral center like white or light gray and different colors on either side. Also um very prominent um ubiquitous are of course sequential data just simply continuous values which can best be represented by using either a monochrome

**[9:11](https://www.youtube.com/watch?v=VC_G_lqideY&t=551s)** color map going from light to dark saturated color or one of the so-called perceptually uniform color maps which are also nowadays often a standard for um color maps in many graphics. fix programs. One representation of sequential data I would discourage you from is the rainbow color map. Arguably using this was a bigger problem a couple of years ago when this was the default in several graphics um programs like mattplot clip. And this color map here is bad for several reasons. So for example, there's no intuitive ordering of the colors like red, green, blue, yellow. What is the

**[9:59](https://www.youtube.com/watch?v=VC_G_lqideY&t=599s)** order here? It's not so easy to make out as for example when ordering different colors going from bright to dark. That's the perceptual effect of red alerting the eye. and the sharp color transitions like between or going from red to yellow create artificial edges which aren't there in the actual data values. So um I'll discourage you from using this better use for like heat maps or coroplith maps a simple monochrome or a perceptually uniform color map like this one here. Pro tip, um, for the orientation of the color map, use the end with the darker colors to describe higher values. This

**[10:50](https://www.youtube.com/watch?v=VC_G_lqideY&t=650s)** feels more natural, you know, um, describing a higher value, more of something with more color, like on the example on the right here. Where possible, use intuitive colors. Famous example are the climate stripes where the um levels or the change in global temperatures are presented by represented by blue for cool and red for warm. There's actually one variation of these climate stripes I really like in a very horrible way. I put this chart on the right here. The climate inaction stripes. This um puts together the change in global temperature with the

**[11:37](https://www.youtube.com/watch?v=VC_G_lqideY&t=697s)** rise in atmospheric CO2 concentration and the dates of various major climate conferences to show how useless this efforts have been in curbing greenhouse gas emissions. A very famous example of using intuitive colors is using red for bad and green for good. Um, this can be problematic for many people. So, just make sure to either use a slight variation of that like red or blue or include additional markers to make this um red green accessible. Also, regarding the choice of colors, don't use for categorical data more than say a handful of colors. You can have a look at the example here and you

**[12:26](https://www.youtube.com/watch?v=VC_G_lqideY&t=746s)** immediately notice that this is very easy, very difficult to process. It's just too many colors. If you go back to this grammar of graphics based approach of encoding a variable in your data into visual property, this means here that you've likely chosen the wrong encoding for your variable with high cardality. either encode it as some other property, use a different chart type or also just reduce the cardinality in your data. The same um goes for using color unnecessarily. If you look at the example on the left here, every bar has a different color which is unnecessarily since unnecessary since the order is already represented

**[13:15](https://www.youtube.com/watch?v=VC_G_lqideY&t=795s)** by the y position. So again with this grammar of graphics approach this means you have encoded one variable into two visual properties the y position and the color which is unnecessarily unnecessary. So best either have um every bar the same color or use the color to encode a different variable in your data like it is done on the example on the right here which reveals some additional insights regarding encoding a variable as a visual property. Um, are there recommendations which encodings are more preferable to than others?

**[14:04](https://www.youtube.com/watch?v=VC_G_lqideY&t=844s)** And indeed, we know from cognitive science or perceptual studies that we as humans are much better to assess differences in values um when they are encoded as a position or length compared to when they are encoded as area, volume or color. Have a look at the examples here. In every example is the same values. And looking at the bar charts on the left, you could roughly make out what the relation between the different items is. And this gets more difficult when looking at the areas here, the circles and the pie chart slices. And even more difficult if you look at the chart on

**[14:53](https://www.youtube.com/watch?v=VC_G_lqideY&t=893s)** the right where the values are represented by color also regarding pie charts here. So I know they're quite popular um especially with the Excel crowd I think not so much with Python listers and they are usually a bad choice. Looking at the examples here you have um three examples where the same data was represented with a bar chart and with a pie chart. And looking at the pie chart down here, um it's quite easy to see which is the lowest, which is the highest value, um how the different items are ordered. And this is much more difficult when looking at the pie chart above. So better use simpler bar charts.

**[15:42](https://www.youtube.com/watch?v=VC_G_lqideY&t=942s)** However, I think there's maybe one narrow use case where pie charts are not so bad. that is representing when something is the fraction of a whole especially when it's around 25 or 75%. So looking at the example on the right here you can easily see that the larger slice is 3/4 of the whole and the smaller slice is one quarter and here is not so straightforward to immediately see this from the bar chart. However, I think this is a really rare exception. So, um some general tips on other um chart types. If you have a chart like this where you

**[16:32](https://www.youtube.com/watch?v=VC_G_lqideY&t=992s)** have to represent aggregate values like the mean of some quantity from different observations, you will you would probably make a scatter plot with the values here. But consider using um as the example on the right, a box or a swarm plot which in not only representing the average value but also um how the values are spread out can reveal some interesting additional insights regarding bar charts which are quite often a sensible choice here. The default in most graphics programs is to use um vertical bar charts like the example on the uh left. And in many cases, especially when you have long labels, um verticals bar vertical

**[17:21](https://www.youtube.com/watch?v=VC_G_lqideY&t=1041s)** horizontal bar charts work much better and you don't have to tilt your head all the time to read the labels. And another pro tip, um, if you create a data visualization like this one with, um, lines for different categories or scatter points, most graphics software automatically creates for labeled entries a legend for with the examples of the graphical representation and the label puts them somewhere inside or outside the chart. Um, this is useful, but it creates an additional mental lookup task. Like when you look up the plot, you always have to switch between the legend to remember which um label is

**[18:11](https://www.youtube.com/watch?v=VC_G_lqideY&t=1091s)** represented by which color. And you can make this easier for your reader if you put in the extra effort to put the labels manually in the correct quarter color alongside the respective data lines. So, we've learned about the most important parts of your visualization like the the message you want to bring across, the structuring of your chart, tailoring it to your audience, and lots of practical tips. Now, how to make this work with Python? And in Python, there's vast data visualization landscape. I think this graph here has been circling in the Python community for 10 years. Originally created by I don't know Jake Vanderlas or Nicholas Rouge. And of

**[19:01](https://www.youtube.com/watch?v=VC_G_lqideY&t=1141s)** course, we're not going to focus on all of these packages here only the most important clusters which are in my opinion mattplot lib and its accompanying ecosystem and the newer javascriptbased libraries like bokeh alter and plotly. There's also the hollow this hollow views ecosystem. Honestly, I don't have a lot of in-depth experience with that, but it might be interesting to look into that, especially if you have really massive data sets you want to visualize. So, regarding the two clusters here, um first of all, there's mattplot lib. I think it's the most um well-known, most popular, well- tested graphics package

**[19:50](https://www.youtube.com/watch?v=VC_G_lqideY&t=1190s)** with an vast accompanying ecosystem. Um most notably I like Seabour which really provides a great interface for statistical highlevel plots. It has a great configurability. You can do really all sorts of customizations. Um however it suffers from its API being somewhat confusing. You know it has this dual API one um partly dates back to or was inspired by MATLAB. So not very modern and clean. Previously also had some poor stylistic defaults. However, this uh got better in more recent versions. So and then in contrast you have packages like alter or plotly express and they work for one interactively out

**[20:41](https://www.youtube.com/watch?v=VC_G_lqideY&t=1241s)** of the box. you know, metplot lilip creates static charts which I think also originates um because not only because it's older but also it originates it from um creating scientific plots um for publishing in journals but these here they work interactively out of the box. If you um create a alter or plotly chart from your data frame in a Jupiter or marimo notebook, you have direct interactivity and they are based on this grammar of graphics API like ggplot. As you can see in the example here, you specify the data set and the type of charge and then these variable to visual property encodings or mappings. And here we can see again how great it is to have such a clean and standardized approach. You know when you come from ggplot you

**[21:32](https://www.youtube.com/watch?v=VC_G_lqideY&t=1292s)** immediately feel familiar with the syntax which is different for mattplot lip which is more about like juggling with individual arrays. So when to use which my personal recommendation would be to use metroclipip for non-standard plots or if you need high customization like um special scientific plots or if you want to need to make your plot adhere to a certain um academic journal publishing standards couple of years ago I also would have told you that you can find for every possible customization examples on stack overflow. Um, of course we use uh coding agents nowadays and feel free to test this out if the coding agent works better with the customization of

**[22:19](https://www.youtube.com/watch?v=VC_G_lqideY&t=1339s)** multiple clip plot plots than other libraries for your everyday plotting or data exploration and notebooks or for creating dashboards. I think plotly express or alter are good choices. Altera is already the default plotting back end in polars. So, especially when working with dataf frame, these are really the easily usable go-to libraries. Honorable mention here goes to great tables. If you have a case that you don't need like a super fancy visualization, but you want to show the actual raw values, maybe include some um nano plot here, like these little bar plots in the cells. Um, great tables is a package to programmatically create

**[23:09](https://www.youtube.com/watch?v=VC_G_lqideY&t=1389s)** nice tables like this all in Python code. So to sum everything up, um, it's really important to be clear about the message you want to convey. best write it down on the chart and design your chart with um the choice of chart type and the inclusion of um annotations, comments, highlighting to support the message. Use the visual hierarchy to structure your chart and make it easily accessible to the viewer. Considering the grammar of graphics as a mental model makes for clean thinking and clean code accord uh in addition with adhering to

**[23:59](https://www.youtube.com/watch?v=VC_G_lqideY&t=1439s)** the best practices regarding the usage of color or different chart types. All this put together enables you to create really effective visualizations of your data. Thank you. [applause] >> [applause] >> Thank you Dominic. Um we have several questions here. The first question is are there u color maps which works best for colorblind people? >> Color bl I think I go back to the So I think this would be um here in the

**[24:49](https://www.youtube.com/watch?v=VC_G_lqideY&t=1489s)** case for example for these um either for the monochrome color maps which go from um bright to darker saturated color like if you take the color away of them you still have them going from um white to black. So they work even without color. And also you know the the ones that are below here that are those um perceptually uniform color maps. They are designed so that a change in value is reflected by a a change in the color space of the color map and make this um gradually so the change is very continuous. I think these were also designed to work for colorblind people. >> Thank you. Um the next question is um

**[25:40](https://www.youtube.com/watch?v=VC_G_lqideY&t=1540s)** there's a chart you're showing the uh line and charts in time shares. If I have more than six different lines in time shares what what I do. >> Yeah, I think then you have the same issue uh like you have with using too many colors. if you have too many lines. And I think it would depend a bit on the case. If the lines are like spread out, then it probably work, but if they're like crossing each other all the time, then it would just be too cluttered. So, it depends a bit on the actual data at hand. Um, one way to solve this would be like to aggregate your data or to use so-called um small multiples, you know, have a um different set of X's for each of your lines to not have them overlap.

**[26:31](https://www.youtube.com/watch?v=VC_G_lqideY&t=1591s)** >> Um, thank you. The next one is the blue red temperature graph commits a major plotting crime in my opinion by not starting the XY Yaxis at zero. What are the rules about accuracy in data presentations [laughter] in my opinion? >> Yeah. Um this is all >> the Yeah. >> Okay. This one here I know that it shouldn't start uh that it should start at zero. Um that's true. I think here in this uh case um it works like this because you for one you need the space to put the labels

**[27:18](https://www.youtube.com/watch?v=VC_G_lqideY&t=1638s)** into. Um I know what you mean that usually you should start the axis at at zero to make the effect less dramatic than it seems here. Um I think it it depends on of course the data if you really um if if there's like a malicious attempt behind it. um for sometime for for many types of data or the variation in the data the changes would just be too too small to um see them properly when you have the y-axis go all the way to zero but in general it's it's good practice

**[28:07](https://www.youtube.com/watch?v=VC_G_lqideY&t=1687s)** yes >> thank you um and yeah we have to there's many questions coming and this question do you have any recommendation for visualizing in large d uh large uh data sets millions of points. >> Yeah, I think in Python um I once attended I think it was at was it another Pyon a workshop by the hollow views people and one of them maybe was it HV plot or data shader was designed specifically for this purpose of visualizing massive data sets. So if that is your use case, feel free to look into this ecosystem. >> Okay, we take uh one last question. Do

**[28:58](https://www.youtube.com/watch?v=VC_G_lqideY&t=1738s)** you have one example from your experience where the plot uh really a bad misrepresented the data? Um, I don't have an example at hand, but I think it's something that you might need to look up if you Google for bad charts. Also, I think there's a lot of examples circulating online of bad visualizations. >> Okay, then thank you a lot for the questions and thank you. Give um let's give um Romanic a warm applause. [applause]

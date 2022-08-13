# ASTROTOOL.py

![astrotool](https://i.postimg.cc/K8ct0KNk/banner.png)

## Preliminary introduction to the subject

Me and my colleague being crazy about crypto-currencies and in particular about stock market prices, we have been interested in this field for more than 6 years, and very actively for more than 2 years exactly.
After having approached all the traditional methods of chart analysis, we realized that these fundamental methods were incomplete. Of course, with a good mastery of these methods we can get a decent winrate (% of gains) but these methods do not give us enough information to really understand what makes the market move as a whole... We are interested in trying to find the Causes to Effect of the stock market rather than simply the effects of a fall or a rise...

Our goal is to obtain about 70 to 80% of valid forecasts, to do this we had to explore and take a long interest in the so-called "non-traditional" methods. Therefore, we have inquired about the methods of "Astro-Finance" (for timing) as well as the methods of "Mr. William Delbert Gann" (for the forecast of resistance/support). These methods are based on geometry, numerology, astronomy (~ Astro-Finance), the study of cycles, etc... 

W.D. Gann is known to have been the best trader in the world of his time (from 1910 to 1950~, with a winrate of more than 90% - I invite you to read more about this character), he created a whole panel of methods of his own and his analysis.
This research took us more than two years (in parallel with our bachelor's degree and currently this DU) to come to our current "level" of understanding on this particular and little known subject.

We were fortunate to meet our mentor, Jim Fredrickson through an acquaintance, ([Biography of Jim](https://geometricthinking.com/about-us/)), who helped us enormously and gave us his time and knowledge to put us on the right track for learning the so-called "non-traditional" methods.

![img](https://i.postimg.cc/P54pmg5h/2022-08-07-19-26-03-Window.png)

#### We helped him to create an Excel file (containing macros) named "ASTROTOOL".

* In the course of this experience, we learned that there is a very particular way to read stock market charts in order to detect geometric supports and resistances. AND ESPECIALLY, we have discovered that there are ways to discern, well in advance (up to more than 10 years in advance), the dates at which market turns (from bullish to bearish, swing low/high, acceleration, etc) are likely to occur. We call these dates ENERGY POINTS (EPs).

* This Excel file highlights future EP dates.  It will not tell which way the market will break, but it will indicate in advance which date to pay particular attention to on a chart for a trading opportunity.

The purpose of this Excel file is to create a calendar from several weighted conditions previously established through different matrices based on Astronomical data - that is to say that each "Aspect" of each Planet has different conditions, some are more consequential than others etc., let's say that an opposition (180 degrees) will be more weighted than a Semi-Sextile (at 30 degrees) between two planets etc... to give us an overview of the next most important dates.
The Excel file contains a lot of data and different methodologies used...
 
## Final Schedule

![img](https://i.postimg.cc/qMrKcNJR/dates.png)
 
We backtested this calendar on the Bitcoin chart, over a period from 2017 to the present 2022. Indeed, the set of dates that the Excel file output to us represents more than 85% correlation with the "turning points" of the market... This does not ONLY apply to bitcoin but to all crypto-currencies and all stock indices, stocks, ETFs… 

![img](https://i.postimg.cc/XvStyvj4/ASTROTOOL-EP-DATES.png)

Example on the Bitcoin graph, since January 2021... Each vertical line represents major EPs (Energy Points date), the Astrotool file has as much success to find the "LOW" as the "HIGH" (it has indeed found the date of the "ATH" = the peak of the Bitcoin to one day - November 11, 2021)

## The Subject @ Memory Paper

The challenge of this dissertation is to find a way to link our passions and recent experiences listed above with Data and the whole world of Python (ML, algorithms etc...), to make it a real dissertation problematic in adequacy with our DU year.
Our ideal subject would be to recreate our entire Excel file "Astrotool" on the Python environment. Astronomical data being very dense and complex, it will be a challenge to process this data on Python in order to make it usable for the creation of the Astrotool calendar on a Jupyter notebook...
Then, we would like to add a Machine Learning logic to it to create an infinite learning and find new possibilities to improve Astrotool.

Finally, the goal would be to create a trading algorithm that would be based on the different methods and signals that "Astrotool" would give us and also added the same logic of Machine Learning so that this algorithm learns from these errors and develop over time.
The vision of the algorithm that we have is relatively simple, it must give at a precise date the projected trend (according to our previous research tracks) as well as issue a buy or sell position, depending on the analysis made.
This algo is rather on the category of "Swing Trade" as opposed to the high frequency algorithm which is based on the very short term. Our algo is rather interested in the "medium/long" term in order to issue buy and sell positions at the most opportune moments (Swing High/Low)...

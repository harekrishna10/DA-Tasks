
# Note: In this entire codes i had used plt.figure() to ensure that all the codes run at the same time with different output in different for that i had used plt.figure() and at last plt.show() to run the codes.


# 1. Import `matplotlib.pyplot` as `plt` and create an empty figure.
import matplotlib.pyplot as plt
empty_figure = plt.figure()
plt.figure() # using plt.figure() to write all codes in same files if i use plt.show() this will execute only first code and will leave next and other codes.
# plt.show()


# 2. Create a line plot for the values `[10, 20, 30, 40, 50]`.
v = [10,20,30,40,50]
plt.plot(v)
plt.figure()


# 3. Plot `x = [1, 2, 3, 4, 5]` and `y = [2, 4, 6, 8, 10]`.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.figure()


# 4. Add a title to a line plot.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title('Line plot using x and y.')
plt.figure()


# 5. Add labels to both axes.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.figure()


# 6. Change the line color to green.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color='green')
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.figure()


# 7. Change the line style to dashed.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color='green',linestyle='--')
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.figure()


# 8. Add circle markers to a line plot.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color='green',linestyle='--',marker='o')
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.figure()


# 9. Increase the line width to 3.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color='green',linestyle='--',marker='o',linewidth=3)
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.figure()


# 10. Display a grid on the plot.
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color='green',linestyle='--',marker='o',linewidth=3)
plt.title('Line plot using x and y.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.figure()


# 11. Plot two lines on the same graph.
fig, ax = plt.subplots(2,1)
ax[0].plot([1,2,3,4],[10,20,30,40])
ax[0].set_title('First line plot')
ax[1].plot([10,20,30,40],[100,200,300,400])
ax[1].set_title('Second line plot')
plt.subplots_adjust(hspace=1)
plt.figure()


# 12. Add a legend for multiple lines.
x = [1,2,3,4,5]
x1 = [10,20,30,40,50]
x2 = [30,50,70,90,110]

plt.plot(x,x1, label='First One')
plt.plot(x,x2, label='Second One')
plt.legend(title='Line Legends')
plt.figure()


# 13. Set the x-axis limit from 0 to 10.
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.xlim(0,10)
plt.figure()


# 14. Set the y-axis limit from 0 to 100.
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.xlim(0,100)
plt.figure()


# 15. Create a line plot showing marks obtained by a student in 5 subjects.
subject = ['Eng','Nep','Math','Sci','Comp']
marks = [86,78,98,87,75]
plt.plot(subject,marks,linestyle=':',marker='s')
plt.xlabel('Subjects')
plt.ylabel('Marks Obtained')
plt.legend()
plt.figure()


# 16. Create a bar chart for sales of five products.
product = ['Dell','Accer','Mac','Lenovo','MSI']
quantity = [47,78,35,29,69]
plt.bar(product,quantity,color='pink')
plt.title('Bar Chart of Sales Product')
plt.figure()


# 17. Change the color of all bars in a bar chart.
product = ['Dell','Accer','Mac','Lenovo','MSI']
quantity = [47,78,35,29,69]
plt.bar(product,quantity,color=['red','yellow','green','pink','blue'])
plt.title('Bar Chart of Sales Product')
plt.figure()


# 18. Create a horizontal bar chart.
product = ['Dell','Accer','Mac','Lenovo','MSI']
quantity = [47,78,35,29,69]
plt.barh(product,quantity,color=['red','yellow','green','pink','blue'])
plt.title('Bar Chart of Sales Product')
plt.figure()


# 19. Add values on top of each bar.
product = ['Dell','Accer','Mac','Lenovo','MSI']
quantity = [47,78,35,29,69]
plt.title('Bar Chart of Sales Product')
tops = plt.bar(product,quantity,color=['red','yellow','green','pink','blue'])
plt.bar_label(tops)
plt.figure()


# 20. Create a bar chart showing the number of students in different classes.
classes = [1,2,3,4,5,6,7,8,9,10]
n_studenst = [41,33,27,21,39,42,49,76,120,132]
plt.title("Bar Chart of number of Students")
top_number = plt.bar(classes,n_studenst,color=['red','yellow','green','pink','blue'])
plt.bar_label(top_number)
plt.xlabel("Classes")
plt.ylabel("Number of Students")
plt.figure()


# 21. Create a histogram using 50 random numbers.
import numpy as np
data = np.random.randint(1,51,50)
plt.hist(data,bins=5,color='green',edgecolor='white')
plt.figure()


# 22. Create a histogram with 15 bins.
weight = [10,30,42,50,55,54,53,56,60,61,64,65,68,71,75,78,80,81,82,90,91,95,96,98,101,104,108,112,118,121,125,150,180,220]
plt.hist(weight, bins=[10,30,50,60,70,80,90,100,110,120,135,165,180,200,220])
plt.figure()


# 23. Change the histogram color.
weight = [10,30,42,50,55,54,53,56,60,61,64,65,68,71,75,78,80,81,82,90,91,95,96,98,101,104,108,112,118,121,125,130,137,145,150,155,160,163,164,165,170,174,177,179,180,190,200,201,205,210,215,220]
plt.hist(weight, bins=[10,30,50,60,70,80,90,100,110,120,135,165,180,200,220], color='red')
plt.figure()


# 24. Add edge colors to histogram bars.
weight = [10,30,42,50,55,54,53,56,60,61,64,65,68,71,75,78,80,81,82,90,91,95,96,98,101,104,108,112,118,121,125,130,137,145,150,155,160,163,164,165,170,174,177,179,180,190,200,201,205,210,215,220]
plt.hist(weight, bins=[10,30,50,60,70,80,90,100,110,120,135,165,180,200,220],edgecolor='black', color='red')
plt.figure()


# 25. Plot the age distribution of 30 students using a histogram.
ages = np.random.randint(15,20,30)
plt.hist(ages,bins=5,edgecolor='white')
plt.title("Ages Distribution of Students")
plt.xlabel('Ages')
plt.ylabel('Number of Students')
plt.figure()


# 26. Create a scatter plot for height and weight data.
height = [1,2,3,4,5,6]
weight = [12,7,23,15,21,30]
plt.scatter(height,weight)
plt.title("Scatter Plotting")
plt.figure()


# 27. Change the color of scatter plot points.
height = [1,2,3,4,5,6]
weight = [12,7,23,15,21,30]
plt.scatter(height,weight,color=['red','green','blue','yellow','pink','crimson'])
plt.title("Scatter Plotting")
plt.figure()


# 28. Change the size of scatter plot points.
height = [1,2,3,4,5,6]
weight = [12,7,23,15,21,30]
plt.scatter(height,weight,color=['red','green','blue','yellow','pink','crimson'],s=[100,200,300,400,500,600])
plt.title("Scatter Plotting")
plt.figure()


# 29. Add transparency to scatter plot points.
height = [1,2,3,4,5,6]
weight = [12,7,23,15,21,30]
plt.scatter(height,weight,color=['red','green','blue','yellow','pink','crimson'],s=[100,200,300,400,500,600],alpha=0.5)
plt.title("Scatter Plotting")
plt.figure()


# 30. Create a scatter plot showing study hours and exam scores.
study_hours = [3,5,7,9,11]
exam_scores = [67,70,82,88,97]
plt.scatter(study_hours,exam_scores,color=['red','green','blue','yellow','crimson'])
plt.title("Student Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.figure ()


# 31. Create a pie chart showing monthly expenses.
month = ['Jan','Feb','Mar','Apr','May','June']
monthly_expenses = [4000,5700,6500,3000,3900,9000]
plt.pie(monthly_expenses,labels=month)
plt.title("Monthly Expenses")
plt.figure()


# 32. Display percentages on a pie chart.
month = ['Jan','Feb','Mar','Apr','May','June']
monthly_expenses = [4000,5700,6500,3000,3900,9000]
plt.pie(monthly_expenses,labels=month,autopct='%.1f%%')
plt.title("Monthly Expenses")
plt.figure()


# 33. Change the colors of pie chart slices.
month = ['Jan','Feb','Mar','Apr','May','June']
monthly_expenses = [4000,5700,6500,3000,3900,9000]
plt.pie(monthly_expenses,labels=month,autopct='%.1f%%',colors=['red','green','blue','yellow','pink','crimson'])
plt.title("Monthly Expenses")
plt.figure()


# 34. Explode one slice of a pie chart.
month = ['Jan','Feb','Mar','Apr','May','June']
monthly_expenses = [4000,5700,6500,3000,3900,9000]
plt.pie(monthly_expenses,labels=month,autopct='%.1f%%',explode=[0,0,0,0,0,0.5])
plt.title("Monthly Expenses")
plt.figure()


# 35. Create a pie chart showing market share of four companies.
companies_name = ['A','B','C','D']
market_share = [35,37,13,25]
plt.title("Companies Shares")
plt.pie(market_share,labels=companies_name,autopct='%.1f%%')
plt.figure()


# 36. Create two subplots in a single figure.
fig, ax = plt.subplots(2,1)
ax[0].plot([1,2,3,4],[10,20,30,40])
ax[1].scatter([1,3,5,7],[12,17,9,21])
plt.figure()


# 37. Display a line plot and a bar chart side by side.
fig, ax = plt.subplots(1,2)
ax[0].plot([1,2,3,4],[10,20,30,40])
ax[0].set_title("Line Plot")
ax[1].bar(['A','B','C','D'],[12,27,9,31])
ax[1].set_title("Bar Chart")
plt.subplots_adjust(hspace=0.5)
plt.figure()


# 38. Create a 2 × 2 subplot layout.
fig, ax = plt.subplots(2,2)
ax[0,0].plot([1,2,3,4],[10,20,30,40])
ax[0,1].bar([5,10,15],[50,100,150])
ax[1,0].plot(['A','B','C'],[10,20,30])
ax[1,1].hist([1,2,3,4,5,12,34,67,34,22,34,67,81,99,100],bins=[5,30,60,80,100],edgecolor='white')
plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.figure()



# 39. Add different titles to each subplot.
fig, ax = plt.subplots(2,2)
ax[0,0].plot([1,2,3,4],[10,20,30,40])
ax[0,0].set_title('Line Plot 1')
ax[0,1].bar([5,10,15],[50,100,150])
ax[0,1].set_title('Bar Chart')
ax[1,0].plot(['A','B','C'],[10,20,30])
ax[1,0].set_title('Line Plot 2')
ax[1,1].hist([1,2,3,4,5,12,34,67,34,22,34,67,81,99,100],bins=[5,30,60,80,100],edgecolor='white')
ax[1,1].set_title("Histogram")
plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.figure()


# 40. Create a dashboard containing a line plot, bar chart, histogram, and scatter plot.
fig, ax = plt.subplots(2,2)
ax[0,0].plot([1,2,3,4,5],[20,35,45,29,40],linestyle=':',marker='o')
ax[0,0].set_title('Line Plot')
ax[0,0].set_xlabel('X')
ax[0,0].set_ylabel('Y')
ax[0,1].bar([5,10,15,20,25],[20,65,79,45,59])
ax[0,1].set_title('Bar Chart')
ax[0,1].set_xlabel('Ages')
ax[0,1].set_ylabel('Number of Students')
ax[1,0].hist([1,2,3,4,5,12,34,67,34,22,34,67,81,99,100],bins=[5,30,60,80,100],edgecolor='white')
ax[1,0].set_title("Histogram")
ax[1,0].set_xlabel('Classes')
ax[1,0].set_ylabel('Students')
ax[1,1].scatter([5,10,15,20,25],[10,25,19,29,8])
ax[1,1].set_title("Scatter")
ax[1,1].set_xlabel('Weight')
ax[1,1].set_ylabel('Height')
plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.figure()


# 41. Import Seaborn and display all available themes.
import seaborn as sns
print(sns.axes_style())


# 42. Set the Seaborn theme to `darkgrid`.
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')
plt.plot([1,2,3,4],[10,20,30,40])
plt.figure()


# 43. Create a Seaborn scatter plot using a sample dataset.
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
sns.scatterplot(x=iris.sepal_length,y=iris.petal_width,)
plt.figure()


# 44. Create a Seaborn line plot.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.lineplot(x=tips.total_bill,y=tips.tip)
plt.figure()


# 45. Create a Seaborn bar plot.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.barplot(x=tips.sex,y=tips.day)
plt.figure()


# 46. Create a Seaborn count plot for a categorical variable.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.countplot(x='day', data=tips)
plt.figure()


# 47. Create a Seaborn histogram using `histplot`.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.histplot(iris.petal_length)
plt.figure()


# 48. Create a Seaborn box plot.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.boxplot(data=tips,y='tip')
plt.figure()


# 49. Create a Seaborn heatmap using a correlation matrix.
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.figure()


# 50. Load the Titanic dataset and create any three different Seaborn visualizations from it.
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
print(titanic)
sns.scatterplot(data=titanic, x='age', y='fare')
sns.histplot(data=titanic,x='age')
sns.boxplot(data=titanic,x='pclass',y='fare')
plt.show()
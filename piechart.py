import matplotlib.pyplot as plt

Tasks = [500,500,500]

labels = 'Python','Javascript','HTML'
colors = ['lightskyblue','yellow','orange']
explode = (0, 0.1, 0)
plt.pie(Tasks, labels=labels, autopct='%1.1f%%', startangle=15, shadow = True, colors=colors, explode=explode)
plt.title('Language')
plt.axis('equal')
plt.show()
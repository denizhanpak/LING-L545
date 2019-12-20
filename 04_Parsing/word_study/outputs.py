import sys
import matplotlib.pyplot as plt

Japanese = 4136/9024
English = 868/1628
SwedishSignLanguage = 17/204
Sanskrit = 43/127
Uyghur = 515/2293
Akkadian = 85/141
Armenian = 1513/3924
Tagalog = 23/23
Telugu = 49 /321
Irish = 552/1110


labels = {0:'japanese', 1:'english', 2:'swedish (sign lang)',3:'sanskrit',4:'uyghur', 5:'akkadian', 6:'armenian', 
    7:'tagalog', 8:'telugu', 9:'irish'}

y = [Japanese, English, SwedishSignLanguage, Sanskrit, Uyghur, Akkadian, Armenian, Tagalog, Telugu, Irish]  # proportion of VO
x = [1-Japanese, 1-English, 1-SwedishSignLanguage, 1-Sanskrit, 1-Uyghur, 1-Akkadian, 1-Armenian, 1-Tagalog, 1-Telugu, 1-Irish]  # proportion of OV
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.savefig(sys.argv[1])
plt.show()

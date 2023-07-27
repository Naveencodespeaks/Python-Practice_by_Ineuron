import matplotlib.pyplot as plt

left = [1,2,4,5,6]
height = [10,11,23,36,6]
tick_label = ['one', 'two', 'three', 'four', 'five']
plt.bar(left,height, tick_label= tick_label, width = 0.8, color =['blue','orange'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Customization')
plt.legend()
plt.show()
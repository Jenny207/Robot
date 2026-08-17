import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# fruits=['Franklin 723', 'Jackson 1071 ','Jefferson 1073',
#         'Marion 1093','Monroe 1099' ,'Montgomery 1101',
#         'Washington 1129' ,'Orange 1750', 'Los Angeles 6073', 'Wayne 13305' ]
counties=['Franklin', 'Jackson','Jefferson',
         'Marion','Monroe','Montgomery',
         'Washington','Orange','Los Angeles','Wayne']
counts = [471, 419, 635, 338,332,529,830,391,539,341]
bar_labels = ['red', 'blue', '_red', 'orange','red', 'blue', '_red',
              'orange','red', 'blue']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(counties, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('counties supply')
ax.set_title('counties supply by kind and color')
ax.legend(title='counties color')

plt.show()
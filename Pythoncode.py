# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd

#import dataset
office_episodes = pd.read_csv("datasets/office_episodes.csv")

#first 10 elements in dataset
office_episodes[:10]


# colours list
colors = []

# Iterate over rows of office_episodes to input color name to the colors list
for lab, row in office_episodes.iterrows():
    if row['scaled_ratings'] < 0.25:
        colors.append("red")
    elif 0.25 <= row['scaled_ratings'] < 0.50:
        colors.append("orange")
    elif 0.50 <= row['scaled_ratings'] < 0.75:
        colors.append("lightgreen")
    else:
        colors.append("darkgreen")

#the first 10 values in the list      
colors[:10]


#Sizes list
sizes = []

#condition
for lab, row in office_episodes.iterrows():
    if row['has_guests'] == True:
        sizes.append(250)
    else:
        sizes.append(25)

#the first 10 values in the list      
sizes[:10]


# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(11,7))

# Create a scatter plot
plt.scatter(office_episodes["episode_number"], office_episodes["viewership_mil"], c = colors, s = sizes)

# Create a title
plt.title('Popularity, Quality, and Guest Appearances on the Office', size = 16)

# Create an x-axis and an y-axis
plt.xlabel('Episode Number', size = 14)
plt.ylabel('Viewership (Millions)', size = 14)

# Show the plot
plt.show()



# The most view
highest_view = max(office_episodes["viewership_mil"])

#the most watched episode
most_watched_dataframe = office_episodes.loc[office_episodes["viewership_mil"] == highest_view]

# Top guest stars that were in that episode
top_stars = most_watched_dataframe[["guest_stars"]]
top_stars 


top_star = 'Jessica Alba'




get_ipython().run_cell_magic('nose', '', 'import pandas as pd\nimport numpy as np\n\ncolor_data = np.genfromtxt(\'datasets/color_data.csv\', delimiter=\',\')\nbonus_color_data = np.genfromtxt(\'datasets/bonus_color_data.csv\', delimiter=\',\')\nbonus_color_data_2 = np.genfromtxt(\'datasets/bonus_color_data_2.csv\', delimiter=\',\')\nsolution_data = pd.read_csv(\'datasets/solution_data.csv\')\n\nx_axis_data = solution_data[\'x_axis\'].values\ny_axis_data = solution_data[\'y_axis\'].values\nsize_data = solution_data[\'sizes\'].values\n\n\n# Try to retrieve student plot data, if it\'s been specified, otherwise set test values to null\ntry:\n    # Generate x and y axis containers\n    stu_yaxis_cont = []\n    stu_xaxis_cont = []\n    stu_sizes_cont = []\n    stu_colors_cont = []\n\n    # Loop through every axis in student\'s figure and grab x and y data\n    for col in fig.gca().collections:\n        stu_yaxis_cont.append(col._offsets.data[:,1])\n        stu_xaxis_cont.append(col._offsets.data[:,0])\n        stu_sizes_cont.append(np.full((1, len(col._offsets.data[:,0])), col._sizes)[0])\n        stu_colors_cont.append(col._facecolors)\n\n    # Get figure labels\n    title = fig.gca()._axes.get_title()\n    x_label = fig.gca()._axes.get_xlabel()\n    y_label = fig.gca()._axes.get_ylabel()\n\n    # Concatenate lists to compare to test plot\n    stu_yaxis = np.concatenate(stu_yaxis_cont)\n    stu_xaxis = np.concatenate(stu_xaxis_cont)\n    stu_sizes = np.concatenate(stu_sizes_cont)\n    stu_colors = np.concatenate(stu_colors_cont)\nexcept:\n    title = \'null\'\n    x_label = \'null\'\n    y_label = \'null\'\n    stu_yaxis = \'null\'\n    stu_xaxis = \'null\'\n    stu_sizes = [0, 1]\n    stu_colors = [0, 1]\n\n# Tests\ndef test_fig_exists():\n    import matplotlib\n    # Extra function to test for existence of fig to allow custom feedback\n    def test_fig():\n        try:\n            fig\n            return True\n        except:\n            return False\n    assert (test_fig() == True), \\\n    \'Did you correctly initalize a `fig` object using `fig = plt.figure()`?\'\n    assert (type(fig) == matplotlib.figure.Figure), \\\n    \'Did you correctly initalize a `fig` object using `fig = plt.figure()`?\'\n\ndef test_y_axis():\n    assert (sorted(stu_yaxis) == y_axis_data).all(), \\\n    \'Are you correctly plotting viwership in millions on the y axis? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    \ndef test_x_axis():\n    assert (sorted(stu_xaxis) == x_axis_data).all(), \\\n    \'Are you correctly plotting episode number on the x axis? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    \ndef test_colors():\n    assert (len(stu_colors) == len(color_data)), \\\n    \'Are you correctly setting the colors according to the rating scheme provided? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    assert (np.sort(color_data) == np.sort(stu_colors)).all() or \\\n    (np.sort(bonus_color_data) == np.sort(stu_colors)).all() or \\\n    (np.sort(bonus_color_data_2) == np.sort(stu_colors)).all(), \\\n    \'Are you correctly setting the colors according to the rating scheme provided? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n\ndef test_size():\n    assert (len(stu_sizes) == len(size_data)), \\\n    \'Are you correctly plotting all points as size 25, except for guest-star episodes which are sized at 250? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n    assert all(size_data == np.sort(stu_sizes)), \\\n    \'Are you correctly plotting all points as size 25, except for guest-star episodes which are sized at 250? Make sure you are calling your plot in the same cell that you initialize `fig`!\'\n\ndef test_labels():\n    assert (title.lower() == (\'Popularity, Quality, and Guest Appearances on the Office\').lower()), \\\n    \'Did you set the correct title? Make sure you are specifying your plot in the same cell that you initialize `fig`!\'\n    assert (x_label.lower() == (\'Episode Number\').lower()), \\\n    \'Did you set the correct x label? Make sure you are specifying your plot in the same cell that you initialize `fig`!\'\n    assert (y_label.lower() == (\'Viewership (Millions)\').lower()), \\\n    \'Did you set the correct x label? Make sure you are specifying your plot in the same cell that you initialize `fig`!\' \n\ndef test_stars():\n    assert (top_star == \'Cloris Leachman\' or top_star == \'Jack Black\' or top_star == \'Jessica Alba\'), \\\n    "Are you correctly assigning one of the guest stars of the most popular episode to `top_star`?"')


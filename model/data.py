## File to generate data retrieved from model
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ## EFFECT OF NUM BUSES ON NEO TIME

    # x_vals = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148]
    # y_vals = [13959, 13959, 13132, 13132, 13219, 13219, 12585, 12585, 11458, 11458, 11458, 10895, 10895, 10895, 10036, 10036, 10036,  9212, 9212, 9212, 9212, 9212, 9212, 8659, 8659, 8659, 8659, 8659, 8659, 8659, 7365, 7365, 7365, 7365, 7365, 7365, 7365, 7365, 7365, 7365, 7162, 7162, 7162, 7162]
    # point_pairs = [(i-1, i) for i in range(1, len(x_vals))]
    # for i, j in point_pairs:
    #   plt.plot([x_vals[i], x_vals[j]], [y_vals[i], y_vals[j]], color='black',linewidth=1.5)
    
    # plt.xlabel('Number of Buses')
    # plt.ylabel('Time of Bus Routing')
    # plt.title('Effect of Number of Buses on Time of Routing')
    # plt.show()

    # EFFECT OF SPHERE OF INFLUENCE OF RAIL NETWORK ON NEO TIME
    x_vals = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
    y_vals = [24127, 18022, 18022, 18022, 18022, 17084, 15428, 15428, 15428, 14051, 14314, 16424, 13202, 13202, 13202, 12019]
    point_pairs = [(i-1, i) for i in range(1, len(x_vals))]

    for i, j in point_pairs:
      plt.plot([x_vals[i], x_vals[j]], [y_vals[i], y_vals[j]], color='black',linewidth=1.5)
    
    plt.xlabel('Max. Distance for Rail to Service AP')
    plt.ylabel('Time of NEO')
    plt.title('Effect of Network Reach of Rail on NEO Time')
    plt.show()

    
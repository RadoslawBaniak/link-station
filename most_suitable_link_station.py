import math  # math module to help in calculations


def coordinate_distance(A, B):
    """
        Function that calculates distance between 2 coordinates
        A,B are coordinates
        formular is Distance^2 = x^2 + y^2
        where x and y are absolute differences in x and y coordinates of the 2 points
    """
    # get the absolute difference in coordinates
    x_diff = abs(A[0] - B[0])
    y_diff = abs(A[1] - B[1])

    # get the squared distance
    distance_squared = (x_diff ** 2) + (y_diff ** 2)

    # get the real distance using square root math module
    distance = math.sqrt(distance_squared)

    # return the distance
    return distance

# calculate the most suitable link


def most_suitable_link(point, stations):

    # loop through the stations
    for s in stations:
        # get the x,y and r
        station_x_coord = s[0]
        station_y_coord = s[1]
        station_reach = s[2]
        station_point = (station_x_coord, station_y_coord)
        # calculate distance using the function above
        distance = coordinate_distance(station_point, point)

        # calculate power for each station at that point
        power = round((station_reach - distance) ** 2, 2)
        print()  # print an empty line

        # check the most suitable link  with the given conditions and print appropriate results
        if distance > station_reach or power == 0:
            print("Best Link Station for {},{} is {},{} with power {}"
                  .format(point[0], point[1], station_x_coord, station_y_coord, power))
        else:
            print("No link Station reach within reach for point {},{}"
                  .format(point[0], point[1]))


if __name__ == "__main__":

    stations = [[0, 0, 10], [20, 20, 5], [10, 0, 12]]  # stations

    points = [(0, 0), (100, 100), (15, 10), (18, 18)]  # points

    # loop trhough all points to get the best link for the provided stations
    for p in points:
        most_suitable_link(p, stations)


"""
    Running the Program.
    Make sure you have python 3 installed and available globbally in the system
    Open a terminal/cmd and run `python3 most_suitable_link_station.py`
    That`s it.
"""

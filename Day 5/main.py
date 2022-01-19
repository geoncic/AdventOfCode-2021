def dayFive():
    allPoints = readFile()

    max_x, max_y = maxCoord(allPoints)
    map = createArray(max_x+1, max_y+1)
    map_two = createArray(max_x+1, max_y+1)
    map = partOne(allPoints, map)
    map_two = partTwo(allPoints, map_two)

    danger_points = countDanger(map, 2)
    danger_points2 = countDanger(map_two, 2)

    print(f'Part One: Number of danger points is {danger_points}')
    print(f'Part Two: Number of danger points is {danger_points2}')

def countDanger(map, x):
    count = 0
    for i in map:
        for j in i:
            if j >= x:
                count += 1
    return count

def createArray(max_x, max_y):
    # Create 2D array of zeroes
    map = [[0 for col in range(max_x)] for row in range(max_y)]
    return map

def maxCoord(allPoints):
    max_x = 0
    max_y = 0
    for coordinates in allPoints:
        x1 = int(coordinates[0][0])
        y1 = int(coordinates[0][1])
        x2 = int(coordinates[1][0])
        y2 = int(coordinates[1][1])
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        else:
            pass
    return max_x, max_y

def partTwo(allPoints, map):
    for coordinates in allPoints:
        x1 = int(coordinates[0][0])
        y1 = int(coordinates[0][1])
        x2 = int(coordinates[1][0])
        y2 = int(coordinates[1][1])

        if x1 == x2:
            map[x2][y2] += 1
            while y1 != y2:
                map[x1][y1] += 1
                if y1 <= y2:
                    y1 += 1
                elif y1 >= y2:
                    y1 -= 1
                else:
                    print('Done')

        elif y1 == y2:
            map[x2][y2] += 1
            while x1 != x2:
                map[x1][y1] += 1
                if x1 <= x2:
                    x1 += 1
                elif x1 >= x2:
                    x1 -= 1
                else:
                    print('Done')
        else:
            map[x2][y2] += 1
            while (x1 != x2) and (y1 != y2):
                map[x1][y1] += 1
                if (x1 > x2) and (y1 > y2):
                    x1 -= 1
                    y1 -= 1
                elif (x1 > x2) and (y1 < y2):
                    x1 -= 1
                    y1 += 1
                elif (x1 < x2) and (y1 < y2):
                    x1 += 1
                    y1 += 1
                elif (x1 < x2) and (y1 > y2):
                    x1 += 1
                    y1 -= 1
                else:
                    pass

    return map

def partOne(allPoints, map):
    for coordinates in allPoints:
        x1 = int(coordinates[0][0])
        y1 = int(coordinates[0][1])
        x2 = int(coordinates[1][0])
        y2 = int(coordinates[1][1])

        # Map Vertical Lines
        if x1 == x2:
            map[x2][y2] += 1
            while y1 != y2:
                map[x1][y1] += 1
                if y1 <= y2:
                    y1 += 1
                elif y1 >= y2:
                    y1 -= 1
                else:
                    print('Done')

        # Map Horizontal Lines
        elif y1 == y2:
            map[x2][y2] += 1
            while x1 != x2:
                map[x1][y1] += 1
                if x1 <= x2:
                    x1 += 1
                elif x1 >= x2:
                    x1 -= 1
                else:
                    print('Done')

        # Map Diagonal Lines
        else:
            pass
    return map



def readFile():
    with open('input.txt') as f:
        data = f.read().splitlines()
        allPoints = []
        for line in data:
            firstPoint, secondPoint = line.split(' -> ')
            x1, y1 = firstPoint.split(',')
            x2, y2 = secondPoint.split(',')
            allPoints.append([[x1, y1], [x2, y2]])
        return allPoints



if __name__ == "__main__":
    dayFive()

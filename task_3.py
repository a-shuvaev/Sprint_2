class PointsForPlace:

    @staticmethod
    def get_points_for_place(place):
        points = 0

        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place <= 100 or place >= 1:
            points = 101 - place
        else:
            print('Спортсмен не может занять нулевое или отрицательное место')
        
        return points


class PointsForMeters:
    
    @staticmethod
    def get_points_for_meters(meters):
        points = 0

        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    total = 0

    def get_total_points(self, meters, place):

        total = PointsForMeters.get_points_for_meters(meters) + PointsForPlace.get_points_for_place(place)

        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
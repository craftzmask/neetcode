class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)

        car_fleets = []
        for car in cars:
            p, s = car
            car_fleets.append((target - p) / s)
            if len(car_fleets) >= 2 and car_fleets[-1] <= car_fleets[-2]:
                car_fleets.pop()

        return len(car_fleets)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : ParkingSystem
@Software       : PyCharm
@Modify Time    : 2021/5/21 15:35
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""


# 输入：
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# 输出：
# [null, true, true, false, false]
#
# 解释：
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
# parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
# parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
# parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了
#


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.car_type = ['err', 'big', 'medium', 'small']
        self.available = {'big': big, 'medium': medium, 'small': small}

    def get_cartype_name(self, carType: int) -> str:
        return self.car_type[carType]

    def addCar(self, carType: int) -> bool:
        carType_name = self.get_cartype_name(carType)
        if self.available[carType_name] > 0:
            self.available[carType_name] -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(1))

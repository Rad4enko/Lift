import random

def get_lift(current_floors, target_floor):
    # Вычисляем расстояние до каждого лифта
    passenger_lift_distance = abs(current_floors[0] - target_floor)
    cargo_lift_distance = abs(current_floors[1] - target_floor)

    # Вызываем ближайший лифт
    if passenger_lift_distance <= cargo_lift_distance:
        return "Пассажирский"
    else:
        return "Грузовой"

# Узнаем количество этажей в доме
total_floors = int(input("Введите количество этажей в доме: "))

# Инициализируем текущие этажи лифтов
current_floors = [random.randint(1, total_floors), random.randint(1, total_floors)]
print(f'Пассажирский лифт на {current_floors[0]} этаже, Грузовой на {current_floors[1]} этаже')

# Получаем этаж, с которого вызывается лифт
target_floor = int(input("Введите этаж, с которого вызывается лифт: "))

# Вызываем ближайший лифт
lift_to_call = get_lift(current_floors, target_floor)

print(f"Вызывается {lift_to_call} лифт")
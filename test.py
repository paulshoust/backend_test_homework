def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

training_dict = {'SWM': 'Swimming', 'RUN': 'Running', 'WLK': 'SportsWalking'}
training_function = training_dict[workout_type]
print(training_function)
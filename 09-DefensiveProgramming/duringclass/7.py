def getBMI(weight, height):
    assert type(weight) == float, 'Bad format weight'
    assert type(height) == int, 'Bad format height'
    assert weight > 40.0 or weight < 150, 'Bad weight'
    assert height > 150 or height < 220, 'Bad height'
    return weight/ (height ** 2)

print(f"wzrost {182}, waga {79.6} = {getBMI(182, 79.6)}")
print(f"wzrost {182}, waga {79.6} = {getBMI(182, 79)}")
print(f"wzrost {182}, waga {79.6} = {getBMI(182.3, 79.6)}")
print(f"wzrost {182}, waga {79.6} = {getBMI(192, 170)}")
print(f"wzrost {182}, waga {79.6} = {getBMI(148, 55)}")
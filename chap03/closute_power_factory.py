def power_factory(exp):
    def pow(base):
        return base ** exp
    return pow

square = power_factory(2)
cube = power_factory(3)

print(square(4))
print(cube(2))
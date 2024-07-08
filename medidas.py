a = float(input("Media A: "))
b = float(input("Medida B: "))
c = float(input("Medida C: "))

area_quadrado = a ** 2
area_retangulo = a * b / 2
area_trapezio = (a + b) * (c / 2)

print(f"Area do quadrado: {area_quadrado:.3f}")
print(f"Area do retangulo: {area_retangulo:.3f}")
print(f"Area do trapezio: {area_trapezio:.3f}")
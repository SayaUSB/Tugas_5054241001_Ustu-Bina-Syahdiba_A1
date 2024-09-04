# Input koordinat
x1, y1, x2, y2 = map(int, input().split())

# Mencari gradien
gradien = (y1-y2)/(x1-x2)
print(f"Gradien dari koordinat ({x1}, {y1}) dan ({x2}, {y2}) adalah {gradien}")

# Mencari titik tengah
mid_x = (x1+x2)/2
mid_y = (y1+y2)/2
print(f"Absis adalah {mid_x} dan ordinat adalah {mid_y}")

# Mencari gradien tegak lurus
gradien = -1/gradien
b = mid_y-gradien*mid_x

# Output dari fungsi tegak lurus
print(f"y = {gradien:.2f}x + {b:.2f}") if b>0 else print(f"y = {gradien:.2f}x - {abs(b):.2f}")

def yigindi_hisobla(**raqamlar):
    yigindi = 0
    for qiymat in raqamlar.values():
        yigindi += qiymat
    return yigindi


raqamlar = {}
for index in range(10):
    raqam = float(input(f"{index + 1}-raqamni kiriting: "))
    raqamlar[f"raqam{index + 1}"] = raqam

print("Yig'indi:", yigindi_hisobla(**raqamlar))
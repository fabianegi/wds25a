def calc_range (kwh: int , efficiency : int) -> int:
    return kwh * efficiency

print(calc_range (kwh=0, efficiency =0))

if __name__ == "__main__":
    print(calc_range (kwh=1, efficiency =5))
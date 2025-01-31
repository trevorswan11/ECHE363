def interpolate(i, i_prop_val, f, f_prop_val, step):
    slope = (f_prop_val - i_prop_val) / (f - i)
    interpolated = i_prop_val + slope * step
    print(f"{interpolated = }")

if __name__ == "__main__":
    try:
        i = float(input( "Lower Value: "))
        i_val = float(input("Lower Property: "))
        f = float(input("Upper Value: "))
        f_val = float(input("Upper Property: "))
        step = float(input("Desired Value: ")) - i
        interpolate(i, i_val, f, f_val, step)
    except:
        print("Inputs must be numeric values!")



cup = input("Choose your cup size (small/medium/large): ").lower

if cup == "small":
    print("price is 10 rupees")
elif cup == "medium":
    print("price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("unknown cup size")
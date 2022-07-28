# "Calculator of Photographer"

from tkinter import *
import math

root = Tk()
root["bg"] = '#707070'
root.title("YouTube @ R-VideoReview")
root.geometry("480x402")
root.resizable(False, False)

# Frames:
frame = LabelFrame(root, text=" Earth Curvature Calculator Pro", font='Times 22 bold', fg="WHITE", bg="#707070")
frame.pack(padx=5, pady=5)

frame1 = LabelFrame(frame, text=" Radius = 6371.008 km!  &  Equator = 40030.174 km!",
                    font='Times 17 bold', fg="#F8C729", bg="#707070")
frame1.pack(padx=5, pady=5)


def calculate1():  # Lens Angle of View - degrees:
    """
    FOV = 2 * (arctangens * x) / (2 * f))
    x = Camera Matrix Size = 36 mm
    f = Lens Focal Length = 50 mm
    FOV = 39.5978 degrees
    """

    angle = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e2.get()))))
    result1 = round(angle, 4)

    if angle < 0:
        lens_angle_of_view["text"] = "Error"
    else:
        lens_angle_of_view["text"] = f"{result1} °"

    print(f"1. Lens Angle of View: {result1} degrees")


def calculate2():  # Distance to Horizon - kilometers:
    """
    r – Earth's radius, equal to 3959 miles or 6371 km
    h – Eyesight level above mean sea level == float(e3.get())
    a – Distance to the horizon = x = ???

    1. x = √[(r + h)² - r²]
    2. x = √[h(2r + h)]  ==  math.sqrt(h * (2 * r + h))
    3. x = √[2rh + h²] == math.sqrt((2 * r * h) + (h ** 2))
    """

    r = 6371.008
    h = float(e3.get()) / 1000  # from meters to kilometers
    d = math.sqrt((r + h)**2 - r**2)  # distance to horizon

    result2 = round(d, 4)
    distance["text"] = f"{result2} km"

    print(f"2. Distance to Horizon: {result2} km")


def calculate3():  # Width of Horizon - kilometers:

    r = 6371.008  # kilometers
    h = float(e3.get()) / 1000  # kilometers

    angle = (2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e2.get())))))  # Lens Angle of View
    d = math.sqrt((r + h) ** 2 - r ** 2)  # Distance to the horizon
    w = math.radians(angle) * d  # Width of Horizon

    result3 = round(w, 4)

    if result3 < 0:
        width["text"] = "Error"
    else:
        width["text"] = f"{result3} km"

    print(f"3. Width of Horizon: {result3} km")


def calculate4():  # Direct Drop of Horizon - degrees:
    r = 6371.008
    h = float(e3.get()) / 1000  # from meters to kilometers
    d = math.sqrt((r + h) ** 2 - r ** 2)  # distance to horizon

    ab = r
    ac = r + h
    bc = d

    drop1 = 90 - (90 - (math.degrees(math.acos((ac**2 + ab**2 - bc**2) / (2 * ac * ab)))))
    result4 = round(drop1, 4)

    if result4 < 0:
        direct["text"] = "Error"
    else:
        direct["text"] = f"{result4} °"

    print(f"4. Direct Drop of Horizon: {result4} degrees")


def calculate5():  # Lateral Drop of Horizon - degrees:
    r = 6371.008
    h = float(e3.get()) / 1000  # from meters to kilometers

    angle_of_view = 2 * math.degrees(math.atan(float(e1.get()) / (2 * float(e2.get()))))
    beta = angle_of_view / 2
    ab = math.sqrt((r + h) ** 2 - r ** 2)  # Distance to the horizon == kilometers
    ac = ab * math.tan(math.radians(beta))
    horizon_width = ac * 2

    angle1 = 2 * math.degrees(math.asin(horizon_width / (2 * r)))
    angle2 = math.degrees(horizon_width / r)
    angle = (angle1 + angle2) / 2
    height = r * (1 - (math.cos(math.radians(angle / 2))))
    chord = 2 * r * (math.sin(math.radians(angle / 2)))

    drop2 = math.degrees(math.atan(height / (chord / 2)))
    result5 = round(drop2, 4)

    if result5 < 0:
        lateral["text"] = "Error"
    else:
        lateral["text"] = f"{result5} °"

    print(f"Angle1 = {angle1} degrees")
    print(f"Angle2 = {angle2} degrees")
    print(f"Angle = {angle} degrees")
    print(f"Height = {height} km")
    print(f"Chord = {chord} km")

    print(f"5. Lateral Drop of Horizon: {result5} degrees")


def calculate6():  # Invisible Object Part - meters >> x = √(a² - 2ad + d² + r²) - r:
    r = 6371.008  # kilometers
    h = float(e3.get()) / 1000  # kilometers
    d = float(e4.get())  # kilometers

    a = math.sqrt((r + h) ** 2 - r ** 2)  # Distance to the horizon == kilometers
    x = (math.sqrt(a**2 - 2*a*d + d**2 + r**2) - r) * 1000  # invisible object's part == meters

    dx = d - a

    if d <= a:
        result6 = round(dx, 4)
        invisible["text"] = f"Visibility 100%"
    else:
        if x >= 1000:
            result6 = round(x / 1000, 3)
            invisible["text"] = f"{result6} km"
        else:
            result6 = round(x, 2)
            invisible["text"] = f"{result6} m"

    print(f"6. Invisible Object Part: {result6} m")


# Frame-1. Radius == 6371.008 km!:

l1 = Label(frame1, text="Camera Matrix Size - millimeters:", width=35, pady=5, fg="white", bg="#454545")
l1.grid(row=0, column=0)

e1 = Entry(frame1, width=12, borderwidth=4, justify=CENTER)
e1.get()
e1.insert(0, '')
e1.grid(row=0, column=1)

l2 = Label(frame1, text="Lens Focal Length - millimeters:", width=35, pady=5, fg="white", bg="#454545")
l2.grid(row=1, column=0)

e2 = Entry(frame1, width=12, borderwidth=4, justify=CENTER)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame1, text="Observer Height from Sea Level - meters:", width=35, pady=5, fg="white", bg="#454545")
l3.grid(row=2, column=0)

e3 = Entry(frame1, width=12, borderwidth=4, justify=CENTER)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

l4 = Label(frame1, text="Distance to Object - kilometers:", width=35, pady=5, fg="white", bg="#454545")
l4.grid(row=3, column=0)

e4 = Entry(frame1, width=12, borderwidth=4, justify=CENTER)
e4.get()
e4.insert(0, '')
e4.grid(row=3, column=1)

# Calculations:  Horizon Width = kilometers

c1 = Button(frame1, text="Lens Angle of View = degrees:", font='Times 16 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate1)
c1.grid(row=4, column=0)

lens_angle_of_view = Label(frame1, width=13, pady=5, bg="#F8C729")
lens_angle_of_view.grid(row=4, column=1)
lens_angle_of_view.bind("<Button>", calculate1)

c2 = Button(frame1, text="Distance to Horizon = kilometers:", font='Times 16 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate2)
c2.grid(row=5, column=0)

distance = Label(frame1, width=13, pady=5, bg="#F8C729")
distance.grid(row=5, column=1)
distance.bind("<Button>", calculate2)

c3 = Button(frame1, text="Width of Horizon = kilometers:", font='Times 15 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate3)
c3.grid(row=6, column=0)

width = Label(frame1, width=13, pady=5, bg="#F8C729")
width.grid(row=6, column=1)
width.bind("<Button>", calculate3)

c4 = Button(frame1, text="Direct Drop of Horizon = degrees:", font='Times 16 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate4)
c4.grid(row=7, column=0)

direct = Label(frame1, width=13, pady=5, bg="#F8C729")
direct.grid(row=7, column=1)
direct.bind("<Button>", calculate4)

c5 = Button(frame1, text="Lateral Drop of Horizon = degrees:", font='Times 16 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate5)
c5.grid(row=8, column=0)

lateral = Label(frame1, width=13, pady=5, bg="#F8C729")
lateral.grid(row=8, column=1)
lateral.bind("<Button>", calculate5)

c6 = Button(frame1, text="Invisible Object Part = m / km:", font='Times 15 bold', width=36, pady=1.5, borderwidth=2,
            fg="#850000", command=calculate6)
c6.grid(row=9, column=0)

invisible = Label(frame1, width=13, pady=5, bg="#F8C729")
invisible.grid(row=9, column=1)
invisible.bind("<Button>", calculate6)

root.mainloop()

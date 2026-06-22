def main():
    time = input ("What time is it ? ")
    p = convert(time)

    if 7.0 <= p <= 8.0:
        print ("breakfast time")

    elif 12.0 <= p <= 13.0 :
        print ("lunch time")

    elif 18.0 <= p <= 19.0:
        print ("dinner time")

    else:
        print ()

def convert(time):
    p,q = time.split(":")
    return int(p) + int(q) / 60

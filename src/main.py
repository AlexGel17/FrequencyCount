from src.frequent_count import FrequentCount

if __name__ == "__main__":

    with open('/home/alex/Desktop/agf/Labor/University/Karl/FrequencyCount/t8.shakespeare.txt', 'r') as file:
        inp = file.read()
        inp = inp.split()

    count = FrequentCount('frequent', inp, 10)
    a, b, c, d = count.run()

    print(a)
    print('Most frequent seq:', b)
    print('Shows on text:', c)
    print('Time:', d)

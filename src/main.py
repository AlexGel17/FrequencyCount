import sys
from src.frequent_count import FrequentCount

if __name__ == "__main__":
    count = FrequentCount(sys.argv[1], sys.argv[2], sys.argv[3])
    a, b, c, d = count.run()
    print(d)

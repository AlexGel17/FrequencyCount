import time
import re
import operator


class FrequentCount:

    def __init__(self, method, fr, k):
        self.method = method
        self.fr = re.sub(r'[^\w]', ' ', open(fr).read().lower()).split()
        self.k = int(k)

    def run(self):
        if self.method == "frequent":
            return self.frequent()
        if self.method == "lossy_counting":
            return self.lossy_counting()
        if self.method == "space_saving":
            return self.space_saving()

    def space_saving(self):
        T = {}
        start_time = time.time()

        for word in self.fr:
            if word not in T:
                if len(T) < self.k:
                    T[word]=1
                else:
                    key = min(T, key=T.get)
                    T[word] = T.pop(key)+1
            else: #its being monitored
                T[word] += 1

        elapsed_time = time.time() - start_time
        sorted_l = sorted(T.items(), key=operator.itemgetter(1))
        return sorted_l[::-1], max(T, key=T.get), T[max(T, key=T.get)], elapsed_time

    def lossy_counting(self):
        T = {}
        delta = 0
        start_time = time.time()

        for n, word in enumerate(self.fr):
            if word not in T:
                T[word] = 1+delta
            else:
                T[word] += 1
            if n/self.k != delta:
                delta = n//self.k
                T = {x:y-1 for x, y in T.items() if y != 1}

        elapsed_time = time.time() - start_time
        sorted_l = sorted(T.items(), key=operator.itemgetter(1))
        return sorted_l[::-1], max(T, key=T.get), T[max(T, key=T.get)], elapsed_time

    def frequent(self):
        T = {}
        start_time = time.time()

        for word in self.fr:
            if word not in T:
                if len(T) < self.k:
                    T[word] = 1
                else:
                    dec = True
                    for x, y in T.items():
                        if y == 0:
                            T[word] = T.pop(x)
                            dec = False
                            break
                    if dec:
                        T = {x:y-1 for x,y in T.items()}
            else: #its being monitored
                T[word] += 1

        elapsed_time = time.time() - start_time
        sorted_l = sorted(T.items(), key=operator.itemgetter(1))
        return sorted_l[::-1], max(T, key=T.get), T[max(T, key=T.get)], elapsed_time

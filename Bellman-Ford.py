def bellman_ford(word, text):
    # text dosyasını aç ve oku
    with open(text, 'r') as file:
        lines = file.readlines()

    # düğümleri ve kenarları oluştur
    node = {}
    edge = []
    for i, line in enumerate(lines):
        words = line.split()
        for j, w in enumerate(words):
            if w not in node:
                node[w] = len(node)
            if j > 0:
                edge.append((node[words[j-1]], node[w]))

    # uzaklıkları sonsuz olarak ayarla
    dist = [float('inf')] * len(node)
    dist[node[word]] = 0

    # Bellman-Ford algoritması
    for i in range(len(node) - 1):
        for u, v in edge:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1

    # kelimenin metinde kaç kez geçtiğini hesapla
    sayac = 0
    for line in lines:
        sayac += line.count(word)

    return sayac

# SONUCLAR
count_upon = bellman_ford('upon', 'alice_in_wonderland.txt')
print("upon: " + str(count_upon))

count_sight = bellman_ford('sight', 'alice_in_wonderland.txt')
print("sigh: " + str(count_sight))

count_Dormouse = bellman_ford('Dormouse', 'alice_in_wonderland.txt')
print("Dormouse: " + str(count_Dormouse))

count_jury_box = bellman_ford('jury-box', 'alice_in_wonderland.txt')
print("jury-box: " + str(count_jury_box))

count_swim = bellman_ford('swim', 'alice_in_wonderland.txt')
print("swim: " + str(count_swim))





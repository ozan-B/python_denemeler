def linear_search(dizi,target):
    for i in range(len(dizi)):
        if dizi[i] == target:
            return i
    return -1
"""        
my_list = [1,2,3,4,5,6,7,8,9,12,45,78,98,56,12,11,123]
search_item = 1

result = linear_search(my_list,search_item)

if result != -1:
    print(f"{search_item} ögesi indeks {result}'da bulundu")
else:
    print(f"{search_item} ögesi bu dizide yok.")
"""








def binary_search(arr,target):
    left = 0 #başlangıç indeksi
    right = len(arr)-1  # bitis indeksi
    
    while left <= right:
        middle = (left+right) // 2 #dizinin tam ortasindaki indeks
        
        if arr[middle] == target:
            return middle #hedef sayi middle degiskenidir
        
        elif arr[middle] < target:
            left = middle+1 #hedef öge sag yarımda olmali    

        else:
            right = middle-1 #hedef öge sol yarımda olmali
            
    return -1 #hedef oge bulanamadi

"""
sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]


search_item = 20


result = binary_search(sorted_list, search_item)

if result != -1:
    print(f"{search_item} öğesi indeks {result}'da bulundu.")
else:
    print(f"{search_item} öğesi bulunamadı.")
"""











# Örnek ağaç yapısı
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node) #düğümü ziyaret et
        visited.add(node) # düğümü ziyaret edildi olarak işaretle
    for neighbor in graph[node]:
        dfs(neighbor)  # düğümün komşularını ziyaret et
        
# A düğümünden başlayarak DFS 'i başlat

dfs('A')
        
    




"""Bu örnek, başlangıçta belirli sayıda kişinin enfekte olduğu bir popülasyonu simüle 
eder ve her gün kişiler arasında hastalığın yayılma olasılığını hesaplar. Ancak gerçek dünya senaryoları çok daha karmaşık olabilir ve daha fazla parametre ve analiz gerektirebilir. Özellikle 
gerçek bir salgını modellemek için daha karmaşık modeller ve veri kullanılması gerekir."""

import random

# Popülasyon büyüklüğü
population_size = 1000

# Başlangıçta enfekte olan kişi sayısı
initial_infected = 1

# Hastalığın bulaşma olasılığı
transmission_probability = 0.2

# Simülasyon süresi
simulation_duration = 30

# Hastalığı taşıyanlar listesi
infected = [False] * population_size
for i in range(initial_infected):
    infected[i] = True

# Simülasyon döngüsü
for day in range(simulation_duration):
    new_infections = 0
    for person in range(population_size):
        if infected[person]:
            for contact in range(population_size):
                if not infected[contact] and random.random() < transmission_probability:
                    infected[contact] = True
                    new_infections += 1
    print(f"Gün {day+1}: Yeni Enfeksiyonlar = {new_infections}")

# Bellman-Ford
Bellman Ford algoritması, en kısa yol problemi için kullanılan bir algoritmadır. Ağırlıklı yönlendirilmiş bir graf oluşturarak kendisine en kısa olan yolu hesaplar. 

Algoritmanın ortalama çalışma zamanı:
### O(EV) - (E: kenar sayısı, V: düğüm sayısı)


## İYİ DURUM
En iyi durumda ağ tamamen düzensiz olduğu ve en kısa yolun kaynak düğümden hedef düğüme doğrudan bir kenarda gittiği durum olarak varsayılır. 

En iyi durumda çalışma zamanı:
### O(E) 

## ORTALAMA DURUM
Ortalama durumda, algoritmanın çalışma zamanı O(EV) 'dir. Bu, ağın düzenlilik derecesine ve içerdiği negatif ağırlık sayısına bağlıdır.

Ortalama durumda çalışma zamanı:
### O(EV)

## EN KÖTÜ DURUM
En kötü durumda, graf negatif ağırlıklar içerdiği için algoritma tüm kenarları en az bir kez kontrol etmelidir. 

En kötü durumda çalışma zamanı:
### O(EV^2) 



# Shortest Path with A* Algorithm
> Program to perform A* search algorithm to find the shortest path from node source to destination

Tugas Kecil 3 IF2211 Strategi Algoritma
Semester II tahun 2020/2021

## Algorithm
A* (A-Star) merupakan algoritma pencarian path/lintasan terpendek dari suatu simpul start ke simpul tujuan pada suatu graf, dengan ide untuk mencari path ke simpul tujuan yang memiliki cost(jarak tempuh) seminimum mungkin dengan menghindari ekspansi path yang memiliki estimasi cost yang tidak minimum.

Cost pada algoritma A* diestimasi menggunakan fungsi f(n) = g(n) + h(n), dimana n merupakan simpul selanjutnya pada path, g(n) merupakan jarak tempuh dari simpul start ke simpul n, h(n) merupakan jarak heuristik (euclidean/ haversian/ straight-line distance) dari simpul n ke simpul tujuan, dan f(n) merupakan estimasi total cost (total jarak) yang harus diminimalisasi dalam pencarian path.

Langkah-langkah pada Algoritma A* :
1. Mula-mula tetapkan simpul start dan simpul tujuan, inisialisasi nilai f = g + h awal
2. Ekspansi simpul start (secara breadth-first/melebar)
3. Hitung nilai f(n)+g(n) = h(n) tiap simpul yang telah diekspansi
4. Ekspansi simpul yang belum dikunjungi dengan f(n) minimum
5. Ulangi langkah 3-4 hingga simpul tujuan dikunjungi (dengan f(n) minimum) atau hingga dapat disimpulkan tidak terdapat path dari simpul start ke simpul tujuan

## System requirements
1. Make sure you have python installed in your device. Download python **[here](https://www.python.org/downloads/)**.
2. Install matplotlib
```
    $ pip install matplotlib
```
3. Install networkx
```
    $ pip install networkx
```

## How to use
1. Add or customize input text file in test folder
```
Text file format:

8
BormaMargaCinta -6.9551799892199035 107.6519276693611
SimpangCiwastraRancabolang -6.959027313829701 107.65981891843917
PabrikBrowniesAmanda -6.956031773373593 107.66033921920959
SimpangRancabolangRSHB -6.955743060729726 107.66060063498446
RSHarapanBunda -6.955911807122251 107.66213210141098
SimpangCiwastraPlutoMarga -6.959656497655654 107.66113547852977
MasjidAlMuhajirin -6.955354207774072 107.66552884470308
SimpangPRayaPUtara -6.95476406184648 107.66268484090399
0 1 0 0 0 1 0 0
1 0 1 1 0 1 0 0
0 1 0 1 0 0 0 0
0 1 1 0 1 0 0 0
0 0 0 1 0 1 0 1
1 1 0 0 1 0 0 1
0 0 0 0 0 0 0 1
0 0 0 0 1 1 1 0
``` 
2. Open src folder in terminal
3. Run main.py
```
    $ python main.py
```

## Authors
- M. Sheva Almeyda Sofjan - 13519018/K01
- Alif Bhadrika Parikesit - 13519186/K04 
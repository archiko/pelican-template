Title: algoritma bubble sort dipython
Tags: fundamental,algoritma, python
Date: 24, Sep 2021
Slug: blog/algoritma-bubble-sort-dipython
Author: Hiko


membahas tentang penyotiran data (pengurutan) atau kata lainnya adalah
megurutkan data dari yang paling kecil ke yang paling besar atau sebaliknya 
(ascending / descending).

konsep dari sorting ini sederhananya adalah memanipulasi index yang ada didalam
sebuah array yang mana mungkin nantinya element yang didalamnya saling ditukar.

jadi ada tuch salah satu algoritma sorting data yaitu bubble sort (gelembung).
sebenarnya banyak banget algoritma sorting bukan cuman bubble ini ada yang rumit kek
`merge sort` atau `quick sort`.


<br><br>
#### **konsep**

<img src="https://stackabuse.s3.amazonaws.com/media/bubble-sort-in-java-1.gif" class="img-fluid">
<small style="font-size:10px;color:#80ED99">source image: stackabuse.com</small>

konsep dari bubble sort sendiri adalah pengurutan dengan cara pertukaran data 
dengan data disebelahnya secara terus menerus sampai dalam satu iterasi tertentu 
tidak ada lagi perubahan.

<br><br>
#### **implementasi**
<br>
```python

def bubble_sort(arr):

    for x in range(len(arr)):
        for i in range(len(arr - 1)):
            if arr[i] > arr[i+1]:
               arr[i],arr[i+1] = arr[i+1],arr[i]

array = [5,9,75,6,13,100]

bubble_sort(array)

print (array)

# output: [5, 6, 9, 13, 75, 100]
```

<br>
###### **penjelasan**

```python
for n in range(len(arr))
```
* kita looping buat dapetin item dari banyak isi item dari listnya

```python
for i in range(len(arr - 1)):
```
* mengubah pasangan terakhir dari item  yang berdekatan jadi (n-2,n-1).


```python
if arr[i] > arr[i+1]:
   arr[i],arr[i+1] = arr[i+1],arr[i]
```
* tukar nilainya :3


<br><br>
#### **references**
* <a style="color:#80ED99" href="https://stackabuse.com/bubble-sort-in-python/">`https://stackabuse.com/bubble-sort-in-python/`</a><br>
* <a style="color:#80ED99" href="http://buublesort.blogspot.com/?m=1">`http://buublesort.blogspot.com/?m=1`</a>







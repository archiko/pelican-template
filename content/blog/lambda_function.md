Title: Membuat fungsi dengan Lambda Expression 
Date: 12, Sep 2021
Tags: python, functions
Slug: blog/membuat-fungsi-dengan-lambda-expression
Author: Hiko


Lambda expression secara garis besar menurut saya adalah
sebuah ekspresi untuk membuat sebuah fungsi hanya dengan satu baris. 
<br><br>
#### ** perbedaan **
Ketika kita membuat sebuah fungsi dengan **def()** kita pasti membutuhkan nama untuk
fungsi tersebut berbeda dengan lambda yang tidak membutuhkan nama untuk fungsi yang kita buat
atau disebut juga dengan anonymous function. selain itu jika **def()** membutuhkan sebuah return
untuk melempar nilainya, dilambda itu tidak berlaku. dan banyak lagi perbedaan atau kelebihan dari membuat 
sebuah fungsi dengan lambda daripada dengan def function,
kalian bisa searching sendiri, karena disini bakalan ngasih tau endpointnya saja.

<br>
#### ** struktur atau format **
```
lambda args: expression
```

args: argumen-argumen <br>
expression: ekspresi / isi fungsi


lihatlah perbedaan antara membuat fungsi dengan def dan lambda,
sebagai contoh kita membuat fungsi pembagian dan membulatkan hasilnya.

* dengan def()
```python
def pembagian(a,b):
    return round(a / b)

print (pembagian(110,12))

# output: 9
```
* dengan lambda
```python
(lambda a,b: round(a/b))(110,12)

# output: 9
```

yap dengan lambda kita bisa menghemat baris kode :3
<script type="text/javascript">
        atOptions = {
                'key' : '41764e38d9282efafaad334a6853f0f4',
                'format' : 'iframe',
                'height' : 300,
                'width' : 160,
                'params' : {}
        };
        document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.highperformancedformats.com/41764e38d9282efafaad334a6853f0f4/invoke.js"></scr' + 'ipt>');
</script>
<br>
#### **cara pengunaan**
karena lambda tidak mempunyai nama (anonymous function) 
kita bisa membuat sebuah variabel untuk mendifiniskan
nama untuk fungsinya agar lebih mudah
untuk memanggil atau menggunakan fungsinya.

```
display = lambda name: print (name)

display('xHiko')
display('xKira')
```
* output:
```
xHiko
xKira
```

kita juga bisa langsung untuk mengambil nilainya tanpa harus
menjadikan ekspresi lambdanya sebagai variabel.
```
(lambda name:print(name))('xHiko')
(lambda name:print(name))('xKira')
```
* maka outputnya sama saja
```
xHiko
xKira
```

<br>
##### **Penutup**
dankee!




























Title: konstruktor init dan fungsi self - Python OOP
Date: 14, Sep 2021
Tags: python, oop
Slug: blog/konstruktor-init-dan-fungsi-self
Author: Ardho Ainullah
Status: published
Thumbnail: /images/blog/initself.jpg

##### **\__init__()**
pada python itu ada yang namanya magic keyword ciri-cirinya itu sederhana
yaitu ada double underscore **"__"** nah salah satunya adalah `__init__`ini.

saat kita membuat sebuah class kita membutuhkan method `__init__()` ini
sebagai inisialisasi (menetapkan nilai) ketika object class dibuat. ia akan dijalankan pertama kali sebelum method-method lainnya dieksekusi.

```python
class phone:

    def __init__(self):
        print ('booting proccess')

ponsel = phone()
```

ponsel ini adalah sebuah instance (wujud dari class) yang didapat dari object phone(),saat kita mengisi sebuah variabel dengan object phone() ini, maka statement print() akan dijalankan.


coba lihat output dari hasil kode diatas
```python
booting proccess
```

<br><br>
##### **jenis konstruktor**
umumnya konstruktor `__init__()` mempunyai dua jenis

* **konstruktor default**
>ia tidak diberikan argumen apapun namun mempunyai satu argumen yaitu **self**
* **konstruktor berparameter**
>konstruktor berparameter ini ia bisa menerima beberapa argumen sesudah argumen **self**
<br><br>
###### **contoh**
* **konstruktor default**
```
class phone:

    def __init__(self):
        self.brand = "xperia"

    def show_brand(self):
        print (self.brand)

ponsel = phone()
ponsel.show_brand()

# output: xperia
```

* **konstruktor berparameter**
```
class phone:

    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram

    def show_brand(self):
        print (self.brand)
        print (self.ram)

ponsel = phone('Xperia','8 Gb')
ponsel.show_brand()

# output: Xperia
#          8 Gb         
```
<br><br>

##### **Fungsi self**
untuk memahami fungsi `self` coba lihat kode dibawah ini

```
class phone:

    def __init__(self):
        self.brand = "xperia"

ponsel = phone()
```

nah jadi sebenarnya argumen `self` itu adalah si `ponsel` (instance) itu sendiri.
lebih jelas kita bisa mengubah atau menambah sebuah attribute karena mereka berdua setara.

```
class phone:

    def __init__(self):
        self.brand = "xperia"

ponsel = phone()
print(ponsel.brand)

ponsel.ram = "8 Gb"
print(ponsel.__dict__)

#\n: new line
print ('\nram: ',ponsel.ram)
```

output:
```
xperia
{'brand': 'xperia', 'ram': '8 Gb'}

ram: 8 Gb
```

nah paham kan? diatas ini sama aja kalo kita nambahin attribute
lewat si `self` nya

```
class ponsel:

    def __init__(self):
        self.brand = "xperia"
        self.ram = "8 Gb"

ponsel = phone()
print(ponsel.brand, ponsel.ram)

# output: xperia 8 Gb
```

<br>
##### **penutup**
Kalo ada salah penyebutan atau ya intinya kesalahan dalam selruh tulisan diatas
mohon maaf, hadeh kaya harus pasang fitur komen biar kalo ada yang salah bisa dikomen.
next dah. dankeee!








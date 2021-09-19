Title: instance method, class method dan static method
Date: 19, Sep 2021
Tags: python,oop
Author: Hiko
Slug: blog/instance-method-class-method-dan-static-method


sebuah method yang ada didalam class dan ia menggunakan argumen `self` maka ia
disebut instance method, paham? gudd!

disini kita bakalan lebih fokus membahas tentang static dan class method saja,
kenapa? karena saya tau kalian udah paham sama instance method.


coba lihat contoh dari instance method
```
class info:
   def __init__(self):
       self.text = "helo i'm gruutz"

   def showInfo(self):
       return self.text

```

fungsi `showInfo()` inilah yang disebut sebagai instance method, ia mengembalikan hasil
untuk siattribute text (instance variabel).
<br><br>
nah jadi gini kita tau pemanggilan method `showInfo()` itu seperti ini `info().showInfo()`
nah ini itu sebenarnya kurang bagus, kenapa? wait kita cari tau dulu
tentang static method dan class method agar kita bisa lebih mudah memahami kurang
bagusnya atau kita bilang kurang elegan..

#### **static method**
untuk membuat sebuah static method kita hanya perlu mendifinisikan methodnya
dengan decorator `@staticmethod`. static method ini berbeda dengan instance method
jika instance method perlu argumen `self` maka static sebaliknya tidak membutuhkannya,
namun kita tetap masih bisa memberinya paramater namun hanya ketiadaan `self`.


contoh
```python
class info:

    def __init__(self):
        pass

    @staticmethod
    def showInfo(text):
        return text + " gruutz"

print (info.showInfo('hello'))

#outpur: hello gruutz
```

nah kurang lebih seperti itu, lihat cara pemanggilan methodnya `info.showInfo()`
berbeda bukan dengan instance method diatas? lebih pendek tentunya dan terlihat
elegan :v

static method ini bisa dibilang tidak tahu menahu atau
bersangkut paut dengan siclass. jadi kita tidak bisa memanggil sebuah attribute
yang ada didalam class tersebut seperti si instance method, misal `self.namaAttribute`
dan kita panggil kedalam static method ya bakalan error karena emg gabisa.

waktu untuk menggunakan static method ini tergantung sih, ada waktu nya kalian ingin membuat
fungsi didalam class tanpa harus si fungsi ikut campur dengan method-method lainnya.


#### **class method**
Untuk membuat sebuah class method kita perlu mendifinisikan methodnya lagi dengan decorator
`@classmethod`. class method ini memerlukan argumen `cls` sama halnya seperti instance method
yang memerlukan `self`.

**NOTE**: Sebenarnya argumen seperi `self` atau `cls` untuk class method itu tidak harus bernama
`self` atau `cls` kalian bebas mengisinya seperti `obj` atau apapun itu. namun standarnya emg gitu.
mungkin biar lebih enak aja dimengerti. oke right?



contoh dari method class
```python
class marvel:
    hero = "deadpool"

    def __init__(self):
        self.power = "Humoris"

    @classmethod
    def heroName(cls):
        return f"name: {cls.hero}"

    @classmethod
    def heroPower(cls):
        return f"power: {cls().power}"


print (marvel.heroName())
print (marvel.heroPower())

#output: name: deadpool
#        power: Humoris
```

saya membuat sebuah class method `heroName()` yang mana ini akan mengembalikan attribute hero (static variabel) yang ada diclass marvel.

sedangkan untuk class method `heroPower()`  ini akan mengembalikan attribute si power (instance variabel) yang ada dimethod `init`

<br>
###### **pengertiaan argumen cls**
cls itu adalah si class marvel. jadi kita bisa memanggil variabel hero dengan `cls.hero`
sama seperti variabel `self.power` kita bisa mengambilnya dengan `cls().power`.

kurang lebih seperti itu.


<br>
##### **kesimpulan**
  -  `Method` atau bisa disebut juga dengan Instance method adalah method yang wajib menyertakan parameter self, dimana self merujuk pada instace kelas tersebut. Jenis method yang sangat cocok digunakan jika terdapat case yang mengharuskan kita berkomunikasi langsung dengan instance suatu class, serta masih membutuhkan attribut-atrribut lain dalam classnya.
<br><br>
  -  `Class Method` adalah jenis method yang diawali dengan decorator @classmethod dan wajib menyertakan cls pada parameternya, dimana parameter cls ini merujuk pada kelas itu sendiri. Class method sangat cocok digunakan jika terdapat case yang tidak memerlukan komunikasi langsung dengan instance suatu class, tetapi masih membutuhkan attribut-atrribut lain dalam classnya.
<br><br>
  -  `Static Method` adalah jenis method yang diawali dengan decorator @staticmethod , dia tidak butuh instance maupun attribut-attribut lain dalam class-nya dan dia juga tidak diwajibkan menyertakan parameter khusus. Jenis ini sangat cocok sebagai method yang berfungsi sebagai helper yang biasanya tidak butuh atribut-atibut apapun dari suatu class.

<br>
**conclusion source:**
<a style="color:#80ED99" href="https://medium.com/ngulicode/method-class-method-dan-static-method-pada-python-1fa5feae4333">Here<a>

<br>
#### Penutup
Idk men ngerti ga ngerti saya itu emang gada bakat buat jelasin sesuatu,
bingung nyusun materinya, bingung jelasin secara tersusun atau step by step.
but! semoga kedepannya penyampaiannya bakalan lebih mudah dimengerti.










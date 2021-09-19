Title: instance method, class method dan static method dipython
Date: 19, Sep 2021
Tags: python,oop
Author: Hiko
Slug: blog/instance-method-class-method-dan-static-method

instance method itu adalah method yang ada didalam class ia menerima argumen `self` sebagai parameter pertamanya. yang mana nantinya akan berbeda dengan static method dan class method.

**sintaks instance method**
```
def func(self, arg1, arg2, ...)
```

**contoh dari instance method**
```python
class phone:

     def __init__(self):
         self.brand = "MIUI"

     def showBrand(self):
         return self.brand

print (phone().showBrand())
#output: MIUI
```
seperti inilah bentukan dari instance method, kalian bisa lihat dibagian paramater `showBrand()` ia diisi dengan `self`, dengan adanya `self` method `showBrand()` ini leluasa untuk memanggil atau merubah attribute-attribute yang ada didalam classnya sendiri.

contoh kita bisa mengubah value dari `self.brand` melalui instance method ini.
```python
class phone:

       def __init__(self):
           self.brand = "MIUI"

       def changeBrand(self):
           self.brand = "Apple"

print (phone().changeBrand())
#OUTPUT: Apple
```
yaps udah paham kan sama instance method? next!<br><br>



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

#### **static method**
untuk membuat sebuah static method kita hanya perlu mendifinisikannya dengan decorator `@staticmethod` sebelum membuat fungsinya. static method ini berbeda dengan instance method,
jika instance method paramater utamanya `self` maka static method tidak punya paramater yang wajib diisi, namun ia masih bisa menerima argumen-argumen/paramater.

**sintaks static method**
```
@staticmethod
def func(arg1, arg2, ...)
```

**contoh dari static method**
```python
class phone:
      def __init__(self):
          self.brand = "MIUI"

      @staticmethod
      def version():
          return "11"

merek = phone().brand
versi = phone.version()

print (merek+versi)

#output: MIUI 11
```

**contoh static method dengan paramater**
```python
class phone:
       def __init__(self):
           self.brand = "MIUI"

       @staticmethod
       def version(versi):
           return versi + "stabil"

merek = phone().brand
versi = phone.version('11')

print (merek + versi)
#output: MIUI 11 stabil
```
seperti inilah static method itu, coba kalian perhatiin perbedaan sintaks untuk
menampilkan output dari instance method dengan static method.

* sintaks instance method memanggil output untuk fungsinya
```
namaClass().namaFungsi()
```

* atau jika instance method hanya memanggil suatu attribute seperti contoh kode diatas
```
namaClass().namaAttribute
```
* sintaks static method memanggil output untuk fungsinya
```
namaClass.namaFungsi()
```

tentunya static method terlihat elegan bukan? karena dia gaperlu buka, tutup kurung berulang wkwk.

instance method itu sangat leluasa untuk memanggil seluruh attribute-attribute yang ada diclassnya kan? nah distatic method itu tidak berlaku. jadi kita tidak bisa memanggil attribute yang ada diclass seperti dengan `self.NamaAttribute` jadi dia itu kaya dirinya sendiri aja gitu gada sangkut paut sama attribute-attribute atau method yang ada diclassnya.

waktu untuk menggunakan static method ini tergantung, ada waktu nya kalian ingin membuat
method didalam class tanpa harus simethod ini ikut campur dengan method-method lainnya.


#### **class method**
Untuk membuat sebuah class method kita perlu mendifinisikannya lagi dengan decorator
`@classmethod` sebelum membuat fungsinya.

Jika instance method parameter pertamanya adalah `self` maka class method juga punya, ia diberi argumen/paramater dengan nama `cls`

**NOTE**: Sebenarnya argumen seperi `self` atau `cls` untuk class method itu tidak harus bernama
`self` atau `cls` kalian bebas mengisinya seperti `obj` atau apapun itu, jadi nanti kalo mau panggil suatu attribute bisa gini `obj.nama`. tapi lebih bagusnya kita menggunakan nama standarnya aja karena didokumentasi python sendiri juga seperti itu.

<br><br>
**sintaks class method**
```
@classmethod
def func(cls, arg1, arg2, ....)
```
**contoh class method**
```python
class phone:
       brand = "MIUI"

       def __init__(self):
           pass

       @classmethod
       def showBrand(cls):
           return print( cls.brand )

phone.showBrand()
#output: MIUI
```


<br>
######  **pengertiaan argumen cls**
kalo merujuk dari contoh kode diatas maka `cls` itu bisa kita bilang adalah si class `phone`. jadi kita bisa memanggil static variabel yang ada diclassnya didalam method class itu sendiri. semisal `cls.brand` maka sama saja seperti `ponsel.brand`.

kurang lebih seperti itu.


<br><br>
#### **factory method**
ada kelebihan dari class method ini daripada static method yang mana ia bisa membuat sebuah factory method. 

factory method adalah sebuah method yang sama seperti method konstruktor init dan ia juga bisa membuat sebuah instance dari suatu class.

yang mana nanti kita bisa membuatnya menjadi lebih berbeda dengan konstruktor aslinya.

contoh factory method dengan class
```python
class phone:

    def __init__(self,brand,version):
        self.brand = brand
        self.version = version

    @classmethod
    def infoDevice(cls,brand,version):
        version = str(version) + " belum stabil"
        return cls(brand,version)

    def __str__(self):
        return f"{self.brand} {self.version}"


smartphone1 = phone('MIUI',12)
smartphone2 = phone.infoDevice('MIUI',11)

print (smartphone1)
print (smartphone2)

#output: MIUI 12
#        MIUI 11 belum stabil
```

nah seperti itulah factory method, cukup keren bukan?

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
Semoga artikel ini menambah wawasan kalian dan seperti biasa jika ada penyebutan yang salah maupun penjelasan yang kurang dapat dipahami, maklumi! yang nulis emang gada bakat buat jelasin sebuah pelajaran 😂 

danke!










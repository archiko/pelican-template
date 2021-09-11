Title: Membuat sebuah grafik data diterminal dengan python
Date: 10, sep 2021
tags: python, tools, packages
author: Ardho Ainullah


Pernah terbesit atau terpikir buat nampilin grafik data atau chart diterminal?
mungkin dari beberapa kalian pasti pernah kepikiran. apalagi yang make
termux buat belajar visualisasi data diandroid karena setau saya
tidak support buat display representasi visual dengan matplotlib.
walaupun sebenarnya bisa, jika kalian menginstall jupyter-notebook,
cuman kurang enak kalo bagi saya karena dilempar ke peramban buat aksesnya.

Oleh karena itu ada sebuah tool dan package yang bernama **termgraph** dan **plotext**
yang mana keduanya dibuat dengan bahasa pemogramman python.

#### **Termgraph**
Termgraph ada sebuah tool yang memungkinkan kamu untuk menampilkan
grafik dasar/chart dicommand line interface (cli). saya sangat suka
dengan termgraph, kenapa? karena penggunaan yang cukup mudah,
dan tampilan visual dasarnya yang sangat simple.

<script type="text/javascript">
	atOptions = {
		'key' : 'e00dc4387e6c63802d3ac0af944c2eb6',
		'format' : 'iframe',
		'height' : 250,
		'width' : 300,
		'params' : {}
	};
	document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.highperformancedformats.com/e00dc4387e6c63802d3ac0af944c2eb6/invoke.js"></scr' + 'ipt>');
</script>

###### untuk menginstallnya cukup dengan pip
<pre><code class="shell">$ pip install termgraph</code></pre>
setelah itu buat lah sebuah file dengan extensi .dat misal **post.dat**

untuk contohnya kita bisa membuat seperti dibawah ini untuk
menampilkan jumlah like, share dan comment dari postingan hari senin
sampai rabu.

<pre><code class="plaintext"># Example

@ Like, Share, Comment

senin, 1200,500,1000
selasa, 1001,550, 300
rabu, 900,1000, 500
</code></pre>

untuk menampilkan hasil tersebut kalian bisa masukan perintah
<pre><code class="shell">termgraph post.dat --color {blue,green,red}</code></pre>
maka hasilnya akan seperti dibawah ini
<br><br>
<img src="/images/blog/termgraph.jpg" class="img-fluid" alt="termgraph">
<br><br>
dibagian --color kalian bisa isi dengan warna yang sudah disediakan

full docs: <a href="https://github.com/mkaz/termgraph" style="color:#80ED99">Here</a>


<br>
#### **plotext**
Jika termgraph adalah sebuah tool berbeda dengan plotext, plotext ini adalah sebuah
package python yang sangat mirip dengan library matplotlib namun bedanya ini dikhususkan
untuk melakukan visualisasi diterminal.
<script type="text/javascript">
	atOptions = {
		'key' : 'e00dc4387e6c63802d3ac0af944c2eb6',
		'format' : 'iframe',
		'height' : 250,
		'width' : 300,
		'params' : {}
	};
	document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.highperformancedformats.com/e00dc4387e6c63802d3ac0af944c2eb6/invoke.js"></scr' + 'ipt>');
</script>

###### untuk menginstallnya cukup dengan pip
<pre><code clase="shell">$ pip install plotext</code></pre>

ada banyak pilihan untuk elemen visual data yang ada diplotext, seperti scatter plot,
line plot,log plot, stem plot dan banyak lagi. 

disini kita akan mencoba line plot saja,
buat sebuah file python dan isi seperti dibawah ini.

```python
import plotext as plt
y = [7, 5, 3, 8, 4, 9, 0, 1]
plt.plot(y)
plt.show()
```

yups sekarang kita coba jalankan programnya
```
$ python3 test.py
```
maka hasilnya akan seperti dibawah ini.
<br><br>
<img src="/images/blog/plotext.jpg" class="img-fluid">
<br><br>

ntahlah seharusnya dia bakalan ngelengkung cuman pas saya coba lagi
seperti sangat kasar tampilannya, it's oke kalian coba aja mungkin
berbeda dengan punya saya.


kalian bisa lihat dokumentasi lengkapnya 
<a href="https://pypi.org/project/plotext/" style="color:#80ED99">disini</a>


<br><br>
##### **penutup**
selain dua itu banyak sekali yang menyediakan package, module atau tool yang
bisa untuk melakukan visualisasi di cli / terminal. tapi disini hanya dua itu saja.
karena itu udah best banget buat saya, oke mungkin segini duluu, dankee.



















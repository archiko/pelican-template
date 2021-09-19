Title: Cara bikin blog digithub pages dengan pelican
Date: 6, Sep 2021.
Tags: python, pelican, ssg
Slug: blog/cara-bikin-blog-digithub-pages-dengan-pelican
Author: Hiko

Pelican adalah sebuah tool SSG (STATIC SITE GENERATOR) yang dibuat dengan bahasa python,right? oke, sebelum lebih jauh lebih baik kita mengenal apa itu ssg dulu.

jika kita translate dalam bahasa indonesia ssg adalah "penghasil website statis"
yang mana website statis ini tidak memerlukan database maupun server-side logic (backend) hanya didasari oleh html, css dan javascript. tentu ini akan membuat website kamu bakalan ngebut karena tidak terlalu banyak melakukan request ke backend. nah blog archiko ini sendiri juga dibuat dengan pelican. 


Kita masuk ke langkahnya
<br>
#### **Buat repositori baru**

Diakun github kalian buat satu repo sama dengan username kalian, diakhir dengan **.github.io**, seperti dibawah ini.
<pre><code class="plaintext">github.com/username/username.github.io</code></pre>

<br>
#### **Install pelican dan ghp-import**

karena pelican merubah sebuah konten dari markdown menjadi html, kalian juga install Markdown. kita gunakan pip python untuk install nya :D
<pre><code class="shell">$ pip install pelican ghp-import Markdown</code></pre>

<br>
#### **kloning repositori dan buat project**

<pre><code class="shell">$ git clone https://github.com/username/username.github.io blog
$ cd blog
</code></pre>

##### **Tips**
karena nanti file-file konfigurasi pelican bakalan muncul dihalaman pengguna (direpositori username.github.io) dengan cabang **master**, kita bisa memilah nya menjadi dua cabang, untuk file-file konfigruasinya kita taruh dicabang baru dengan nama **content**. sedangkan untuk hasil konten web dari pelican kita taruh dicabang **master**.

ini akan memudahkan kita nantinya jika ingin menghapus seluruh halaman/konten dalam websitenya karena hanya ada dicabang **master** dan kita bisa mengisinya lagi dari cabang **content**.


paham? semoga....

<pre><code class="shell">$ git checkout -b content
Switched to a new branch 'content'
</code></pre>

<br>
#### **Konfigurasi pelican**
Ditahap ini kita akan melakukan konfigurasi pelican.
Untuk inisialisasi gunakan perintah **pelican-quickstart**.
Nanti kalian disuruh menjawab serangkaian pertanyaan.

<pre><code class="shell">
$ pelican-quickstart
Welcome to pelican-quickstart v4.6.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.] .
> What will be the title of this web site? Anime Streaming
> Who will be the author of this web site? Hiro
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Asia/Jakarta
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /root/blog
</code></pre>


untuk bagian upload your site using github pages kalian pilih "y" karena dalam toturial ini kita bakalan hosting nya digithub.

coba sekarang kalian lihat isi foldernya.
<pre><code class="shell">$ ls
Makefile  content  output  pelicanconf.py  publishconf.py  tasks.py
</code></pre>

<br>
#### **Push!**
Setalah file-file diatas sudah ada, kita push ke repositori yang dibuat tadi dengan cabang konten.
```shell
$ git add .
$ git commit -m "-"
$ git push origin content
```
Maap jika info commitnya hanya "-" karena saya bingung mau isi dengan apa wkwk

<br>
#### **Menambahkan sebuah postingan**
Yap disini kalian sudah bisa menambahkan artikel atau postingan.
Ayo kita tambahkan 1 postingan dan 1 halaman untuk about.

<pre><code class="shell">$ cd content && mkdir pages
$ touch pages/about.md
$ touch post-1.md
</code></pre>

Buka file **post-1.md** dengan kode editor kesayangan kalian.
tambahkan judul, tanggal, author dan isi konten.

<pre><code class="plaintext">Title: Hallo Dunia!
Date: 24, sep 2027
Author: Hero

# Halo Dunia!
Ini adalah isi konten pertama saya menggunakan pelican.
</code></pre>


nah sekarang kalian coba buka file **pages/about.md** dan tambahkan seperti dibawah ini.

<pre><code class="plaintext">Title: About
Date: 24, sep 2027

## About
Hai nama gua hero dan terimakasih telah memberikan
gua kesemepatan untuk menemani malam sedih mu.
</code></pre>


Sekarang dicabang **content** kita memiliki 1 halaman dan 1 postingan. sekarang kita tinggal publish ini kehalaman github pages kita.

<br>
<script async="async" data-cfasync="false" src="//pl16575411.effectivecpmgate.com/e16ac09b2557683ec280a236f0c9e9c7/invoke.js"></script>
<div id="container-e16ac09b2557683ec280a236f0c9e9c7"></div>
<br>
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
#### **Publish**
Oke, kalian ada ditahap terakhir, waktunya untuk mempublish halaman kita.

* jalankan pelican untuk membuat file statis htmlnya dengan keluaran dipath **output**:
<pre><code class="shell">$ pelican content -o output -s publishconf.py</code></pre>
* gunakan **ghp-import** untuk menambahkan isi konten dioutput tadi kecabang **master**:
<pre><code class="shell">$ ghp-import -m "-" --no-jekyll -b master output 
</code></pre>
* sekarang tinggal kita push kecabang lokal **master**nya.
<pre><code class="shell">$ git push origin master
</code></pre>

* lakukan push dan commit lagi untuk menambahkan halaman dan post yang sudah dibuat tadi kecabang **content**
<pre><code class="shell">$ git add content
$ git commit -m "-"
$ git push origin content
</code></pre>

<br>
#### **Akhirnya ~**
Sekarang halaman github pages kalian sudah siap untuk dikunjungi!
<pre><code class="plaintext">https://username.github.io/
</code></pre>


<br>
###### **Penutup**
Ya saya bisa yakin kalian akan bosan dengan tampilan defaultnya, namun kalian bisa mengantinya dengan tema-tema yang sudah banyak tersedia, bisa disearching sendiri. selain itu ada juga untuk kustomisasi tema secara mandiri (bikin sendiri) seperti blog ini, mungkin bakalan ada dinext post untuk toturialnya, pantengin teruss ya. enjoy!




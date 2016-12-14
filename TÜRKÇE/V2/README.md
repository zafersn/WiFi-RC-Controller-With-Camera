# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING
# ----------------------------- Pi_CAR -----------------------------

[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)


## Kullanýlan Malzemeler
<br>

Malzeme Adý| Adet
----| ---- 
Arduino Nano| 1
Raspberry Pi| 1
Raspberry Pi Camera Modülü| 1
Wi-Fi Adaptör| 1
L298N,BTS7960,L293 Motor Sürücü| 1 yada 2 
DC MOTOR|  2  yada   4
12V Lipo Batarya| 1
Jumper Kablo | ~
Araç Þasi (Gövdesi)| 1
<br>

## Arduino:
### AMAÇ VE GÖREVLER:
*	Arduino motorlarý kontrol etmek amacý ile kullanýlmýþtýr.
*	Arduino ile raspberry pi usb üzerinden seri haberleþme yapmaktadýr.
*	Android telefonumuz üzerinde arduino’ya gidecek olan pwm aralýðý hesaplanýp gönderilmektedir.(Gelecek güncellemeler ve kullanýcýnýn pwm deðiþkenine daha kolay müdahale edilmesi için)
*	Aþaðýda Raspberry pi, Raspberry pi Camera, Arduino, L298N Motor Sürücü,Motorlar ve Bataryanýn devre baðlantý þemasý gösterilmiþtir. 

 
### ARDUINO KURULUMU VE PIN BAÐLANTI ÞEMASI

* Arduino 'ya gelen veri doðrudan motorlara gidecek pwm aralýðý olarak gelmektedir.PWM deðerinin yanýnda sadece aracýn yön tayini için ` + (ileri)` ve ya `- (geri)` deðerini almaktadýr.
* Yukarýdaki durum göz önüne alýnarak çeþitli modifikasyonlar yapýlabilir.
* PWM aralýðý `0-255` arasýndadýr.
* Telefon üzerinden SAÐ VE SOL motor pwmlerini ve servo motor açýsýný String bir þekilde örn:  200:200!888 þeklinde alýyoruz. Aradaki iki nokta üst üste  `:` ve ünlem iþareti `!` ' e göre bölerek 3 elemanlý bir dizi oluþturuyoruz.
*  `!` den sonraki deðer, cameranýn baðlý bulunduðu servo motor'un açý deðerleridir. Bu çalýþmada servo motor kullanýlmamýþtýr.<br><br>
**Motor Hareket PWM Geliþ Tipi ve Aracýn Durumlarý**<br>
örn:
*  0:0      //stop
* 200:200     // ileri git. ( 2 motorda 200pwm ile çalýþýr )
*  -200:-200   //geri git. (2 motorda 200pwm ile çalýþýr)
*  200:-200   // sol motor 200 pwm ileri, sag motor 200 geri döner ( araç kendi etrafýnda soldan saða doðru döner)
* -200:200   // sol motor 200 pwm geri, sag motor 200 ileri döner ( araç kendi etrafýnda saðdan sola doðru döner)
* 200:100    // araç saða dönecek þekilde hareket eder.<br><br>
 



[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/youtbeT2.png)](https://youtu.be/D4ewbO-OGLY)

<p align="center"> <b>L298 - Dual Full Bridge Driver</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/wificontrol.png"  />
</p>
<p align="center"> <b>BTS7960 - 43A MOTOR DRIVE</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/BTS7960%20fritzing2.png"  />
</p>
<br><br>
* Arduino, Raspberry pi,Raspberry pi camera modülü, L298N motor sürücü, Motorlar, Güç kaynaðýnýn baðlantýlarýný  yukarýdaki resimdeki gibi gerçekleþtiriniz.
* Yukarýdaki þekildeki gibi arduino pin baðlantýlarýný ve raspberry pi baðlantýsýný  gerçekleþtirdikten sonra yapmamýz gereken arduino kodlarýmýzý yüklemek olacaktýr.<br>
**Bunu sýra ile þu  þekilde yapabilirsiniz.<br>**

**I.** Arduino kodlarýnýn açýklamalarý ve ne iþe yaradýðý ile ilgili detaylý bilgi kodlarýn içinde mevcuttur.<br>

**II.** `androidToRaspberry.ino` adlý arduino kodumuzu bu [**linteken**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/androidToRaspberryTurkce) indirerek ve çift týklayarak açýnýz.<br>

**III.** Açýlan proje dosyasýný arduino' ya yüklemek için sýra ile  sekmelerden `Tools` => `Board`  ve buradan kullandýðýnýz arduino modelinizi seçiniz.<br><br>


![Screen Shot RA1](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/ra1.png)
<br><br>
**IV.** Tekrar `Tools` sekmesinden takmýþ olduðunuz arduino' nuzun hangi port' a takýlý olduðunu gösteriniz.  `Tools` => `port`<br>

**V.** Yukarýdaki adýmlarý gerçekleþtirdikten sonra þimdi programýmýzý arduino' muza yükleyebiliriz.Sol üst köþede `Upload` butonuna basarak yükleme iþlemini tamamlamýþ oluyoruz.<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/ra2.png)
<br><br>

## RASPBERRY PI:
### AMAÇ VE GÖREVLER:

* Raspberry pi camera modülü kullanarak görüntünün alýnmasý ve raspberry pi üzerinden telefona aktarýlmasý.
* Arduino ve Telefon arasýnda baðlantýnýn kurulmasý.

### RASPBERRY PI KURULUMU:
Raspberry pi kurulumu oldukça basittir.Öncelikle,

Win32DiskImager SD karta iþletim sistemi yazdýrmamýz için gerekli olan programdýr.
Ýndirmek için [**Týklayýnýz**](http://www.gezginler.net/indir/win32-disk-imager.html)

## 1. Raspbian Ýþletim Sistemi Ýndirme;
Raspberry pi mize kuracaðýmýz araç kontrol yazýlýmlarýnýda içinde bulunduran iþletim sistemini SD karta yazdýmamýz gerekmektedir.Burada DÝKKAT edilmesi gereken nokta, aþaðýda linkleri verilen iþletim sistemlerini seçerken elinizde bulunan Wi-Fi adaptörlere göre 
iþletim sistemini indirmeniz ve sd karta yazdýrmanýzdýr.Ýþletim sistemleri ve destekledikleri modemler aþaðýda verilmektedir.

### Raspberry Pi 3  Ýçin indirilebilir iþletim sistemi
Raspberry pi 3 için 2 alternatif yöntemimiz vardýr;<br>

1. si doðrudan raspberry pi üzerindeki dahili Wi-Fi kullanmak. <br>
2. Harici olarak USB Wi-Fi adaptör kullanmak(Mesafe ve veri hýzý bakýmýndan tavsiye edilen yöntemdir. Tabi bu kullanacaðýnýz Wi-Fi adaptöre göre deðiþebilir.)
<br>

### 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanýz.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfX1dsaVVJZThEN2c/view?usp=sharing) iþletim sistemini indirerek SD karta yazdýrýnýz.



### 2.Pi_CAR'I Raspberry pi 3 'ün  Üzerinden harici olarak taktýðýnýz Wi-Fi modüþü kullarak yönetmek istiyorsanýz.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing) iþletim sistemini indiriniz.



Bu seçenek için elimizde bulunan ve test ettiðimiz Wi-Fi cihazlarý ve çipsetleri
<br>

Test Edilen cihazlar|CHIPSET
---------- | --------
Dark WDN300A5 | RTL8192CU
Tenda UH150 | RT2870/RT3070
AWUS036NH | RT2870/RT3070
<br>

Desteklenen diðer çipsetler ve cihazlar için detaylý bilgi:http://elinux.org/RPi_USB_Wi-Fi_Adapters

## 2. Ýþletim Sistemini Micro-SD Kart’a Yazdýrma
Ýndirdiðimiz imaj dosyasýný zip içerisinden çýkarýyoruz. Ardýndan daha önce indirdiðimiz win32diskImager programýný açýyoruz. Ýmaj dosyamýzý belirtilen yerden seçiyoruz.

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/win32diskimager.jpg)

Sd kartýnýzýn bilgisayara takýlý olduðundan emin olduktan sonra Device kýsmýnda görebilirsiniz. Ardýndan Write butonuna týklayýp yazma iþlemini baþlatýyoruz. Yazma iþlemi yaklaþýk 2-3 dk sürmektedir. Yazma iþleminin bitmesini yeni açýlan pencerede "Write Succesful." yazýsýný görene kadar bekleyiniz.


![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/Write%20Succesful.png)
## 3.Baðlantýlar ve Çalýþtýrma

Yazma iþlemi tamamlandýktan sonra SD kartýnýzý bilgisayardan çýkartýp Raspberry pi'nize takabilirsiniz.
Artýk yapmanýz gereken SADECE Raspberry' nize USB üzerinde bir Arduino takýp  gerekli güç ve motor sürücüleri baðlantýlarýný yaptýktan sonra araca monte etmenizdir.
<br>
Video'lu anlatým: 
<br>
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/youtube%20play2.png)](https://youtu.be/yNLug0DhQlc)

## ANDROID:

### AMAÇ VE GÖREVLERÝ:
* Raspberry pi ve arduino ile yapýlmýþ olan rc-arabanýn kontrolünü saðlamak.
* Kullanýcý için sade ve kolay görsel arayüz.
* Raspberry pi üzerinden kamera görüntüsünü alarak kullanýcýya göstermek.

### ANDROID UYGULAMA KURULUMU:
* Uygulamanýn kurulumu son derece basittir. Sadece yapýlmasý gereken **ANDROID GOOGLE PLAY** markette giriþ yapýldýktan sonra arama kutucuðuna, uygulamaya doðrudan eriþmek için `com.stackcuriosity.tooght` ve ya uygulama ismi `RC CONTROLLER WITH CAMERA` yazmanýz yeterlidir.<br>

### UYGULAMA KULLANIMI VE ÝPUCULARI  <br>

#### Raspberry pi baðlantý bilgileri
* Android uygulamanýzý indirdikten sonra sizi aþaðýdaki gibi bir ekran karþýlayacaktýr.Artýk yapmanýz gereken þey sadece aracý kontrol etmek olacaktýr.
<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/Screenshot_20161208-155537.png)

Uygulamanýn çalýþma prensibini ve tanýtýmýný kýsaca açýklayalým.

#### UYGULAMA DETAYLARI

##### 1. GÖRSEL ARAYÜZÜN AÇIKLANMASI VE PROGRAMLAMA MANTIÐI
* **Uygulamamýz 4 temel esasa dayanmaktadýr.** Bunlar;
  1. Aracýn yön kontrolünün saðlanmasý.<br>
  2. Kullanýcýya araç üzerindeki kameradan canlý görüntünün aktarýlmasý.<br>
  3. Aracýn baðlantý sinyal seviyesi göstergesi.
  4. Fallow Me (Çok yakýnda).(Aracýn sahibini takip etmesi).<br>
* Bu dört temel esasa göre 
*  Aracýn yön kontrolünde kullanýlan mantýðýn ana detaylarýný `Arduino` bölümde anlattýk.Android tarafýna bakan kýsmý ile açýklayacak olursak.Android tarafýnda, kullanýcý için `Seek bar (Hýz ayarý)` , `Kamera Açma / Kapama` ,`Wi-Fi durum göstergesi`  ve `Yön tuþlarý` mevcuttur.<br> ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/Screenshot_description_githup.png)<br>
*  **Seek bar(Hýz ayarý)** 15 dilimden oluþmaktadýr ve hýz katsayýsý 17'dir.Yani seek bar' ýn herbir hareketi pwm'de 17'nin katlarý þeklinde bir oynama yapmaktadýr.Seek bar 5. kademede ise üretilen pwm= 5*17 = 85 'tir.
*  **Menü tuþlarý (Kamera Aç/Kapa ve WiFi Göstergesi)** Seekbar 'ýn yanýnda yer alan diðer araç kontrol fonksiyonlarý;<br> Kamera görüntüsünü araç üzerinden almamýza yarayan Kamera açma ve kapatma butonu " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/ic_eye.png) AÇ ", " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/ic_eye_off.png) KAPAT ", Ayný þekilde uygulamamýzýn Raspberry Pi üzerinde oluþturduðumuz Wi-Fi aða baðlanýp baðlanýlmadýðýný gösteren bir gösterge." ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/ic_wifi_on.png) BAÐLI DEÐÝL", " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/ic_wifi_off.png) BAÐLI "
*  **Yön tuþlarý** seek bar(Hýz ayarý)'dan alýnan verinin yönlere ayrýlmasýný saðlar. Aracýn gidiþ yönüne göre pwm deðerinin baþýna `+` ve ya `-` iþareti getirilir. **Örn;**<br><br>
 200:200     // ileri git. ( 2 motorda 200pwm ile çalýþýr )<br>
 -200:-200   //geri git. (2 motorda 200pwm ile çalýþýr)<br>
 200:-200   // sol motor 200 pwm ileri, sag motor 200 geri döner ( araç kendi etrafýnda soldan saða doðru döner)<br>
 -200:200   // sol motor 200 pwm geri, sag motor 200 ileri döner ( araç kendi etrafýnda saðdan sola doðru döner)<br>
 200:100    // araç saða dönecek þekilde hareket eder.<br><br> 
 * **Sinyal Seviye Göstergesi** Bu gösterge telefon ile araç arasýndaki  baðlantýnýn sinyal kalitesini ve uzaklýða göre deðiþen sinyal çekim seviyesinin kullanýcýya gösterilmesini saðlar.

##### 2.SAÐ'A VE SOL'A DÖNÜÞLERDE HASSASÝYET
* Aracýmýzýn sað çaðraz ve sol çapraz hareketleri yaparken dönüþ yapýlacak taraftaki motorlarýn pwm deðerleri düþürülür ve böylece motorlarýn daha yavaþ dönmesi saðlanýr.Bu sayede araç istenilen hassasiyette çarpraz dönüþleri gerçekleþtirebilir.**Bu dönüþ hareketlerinin hassasiyet ayarlamasý kullanýcýya býrakýlmýþtýr.**
* Çapraz dönüþlerin hassasiyetinin hesaplanmasýnda kullanýlan formül : **`PWM DEÐERÝ - (PWM DEÐERÝ / PWM ORANI)`** 'dýr.
* PWM ORANI varsayýlan olarak `2` gelmektedir.
* PWM ORANI ayarýný, kontrol ekranýn da sað üst köþede `Ayarlar` butonundan tekrar `Ayarlar` sekmesine basarak ulaþabilirsiniz.<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/device-2016-07-07-230804.png)<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/device-2016-07-07-230848.png)<br><br>
* Girebileceðinz PWM ORANI aralýðý **minimum ve maksimum olarak 1-4 arasýnda integer ve double tipinde** deðerlerdir.
 


### UYGULAMA ICON 'UMUZ:

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/raspi_car.png)




## TEST VÝDEO:
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/images/testvd1.png)](https://youtu.be/qbkH2KFcKqw)
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/play_video2.png)](https://youtu.be/CT-hgXIPRIk)
<br><br>



-------------------------------------------------------------------------------------
<br><br>

#KISA VE ÖZET KURULUM<br><br>
<p align="center"> <b>DETAYLI BÝLGÝ VE  VE KURULUM AYRINTILARI ÝÇÝN LÜTFEN SAYFA BAÞINDAN BAÞLAYINIZ !!</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/raw.gif" alt="DETAYLI ANLATIM VE KURULUM" align="middle" />
</p>

## **ADIM 1:**
<br>
 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanýz.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfX1dsaVVJZThEN2c/view?usp=sharing) iþletim sistemini indirerek SD karta yazdýrýnýz.
<br>


 2.Pi_CAR'I Raspberry pi 3 'ün  Üzerinden harici olarak taktýðýnýz Wi-Fi modüþü kullarak yönetmek istiyorsanýz.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing) iþletim sistemini indiriniz.
<br>

## **ADIM 2**
Arduino kontrol yazýlýmýný Bu [**linteken**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/androidToRaspberryTurkce) indirerek
Arduino' ya yükleyiniz.

## **ADIM 3**
Android kontrol yazýlýmýda  Bu [**linteken**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) indirerek
telefonunuza  yükleyiniz.
<br><br><br>
**ve  iþlem tamam arduino motor sürücüleri arasýndaki baðlantýlarý doðru yaptýysanýz artýk aracý kontrol etmeye baþlayabilirsiniz.**

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2.0/images/Google.png"/></a>
</p>


# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING
# ----------------------------- Pi_CAR -----------------------------

[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)


## Kullanılan Malzemeler
<br>

Malzeme Adı| Adet
----| ---- 
Arduino Nano / UNO / Mega| 1
Raspberry Pi| 1
Raspberry Pi Camera Modülü| 1
Wi-Fi Adaptör| 1
L298N,BTS7960,L293 Motor Sürücü| 1 yada 2 
DC MOTOR|  2  yada   4
12V Lipo Batarya| 1
Jumper Kablo | ~
Araç Şasi (Gövdesi)| 1
<br>

## Arduino:
### AMAÇ VE GÖREVLER:
*	Arduino motorları kontrol etmek amacı ile kullanılmıştır.
*	Arduino ile raspberry pi usb üzerinden seri haberleşme yapmaktadır.
*	Android telefonumuz üzerinde arduino’ya gidecek olan pwm aralığı hesaplanıp gönderilmektedir.(Gelecek güncellemeler ve kullanıcının pwm değişkenine daha kolay müdahale edilmesi için)
*	Aşağıda Raspberry pi, Raspberry pi Camera, Arduino, L298N Motor Sürücü,Motorlar ve Bataryanın devre bağlantı şeması gösterilmiştir. 

 
### ARDUINO KURULUMU VE PIN BAĞLANTI ŞEMASI

* Arduino 'ya gelen veri doğrudan motorlara gidecek pwm aralığı olarak gelmektedir.PWM değerinin yanında sadece aracın yön tayini için ` + (ileri)` ve ya `- (geri)` değerini almaktadır.
* Yukarıdaki durum göz önüne alınarak çeşitli modifikasyonlar yapılabilir.
* PWM aralığı `0-255` arasındadır.
* Telefon üzerinden SAĞ VE SOL motor pwmlerini ve servo motor açısını String bir şekilde örn:  200:200!888 şeklinde alıyoruz. Aradaki iki nokta üst üste  `:` ve ünlem işareti `!` ' e göre bölerek 3 elemanlı bir dizi oluşturuyoruz.
*  `!` den sonraki değer, cameranın bağlı bulunduğu servo motor'un açı değerleridir. Bu çalışmada servo motor kullanılmamıştır.<br><br>
**Motor Hareket PWM Geliş Tipi ve Aracın Durumları**<br>
örn:
*  0:0      //stop
* 200:200     // ileri git. ( 2 motorda 200pwm ile çalışır )
*  -200:-200   //geri git. (2 motorda 200pwm ile çalışır)
*  200:-200   // sol motor 200 pwm ileri, sag motor 200 geri döner ( araç kendi etrafında soldan sağa doğru döner)
* -200:200   // sol motor 200 pwm geri, sag motor 200 ileri döner ( araç kendi etrafında sağdan sola doğru döner)
* 200:100    // araç sağa dönecek şekilde hareket eder.<br><br>
 



[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/youtbeT2.png)](https://youtu.be/D4ewbO-OGLY)

<p align="center"> <b>L298 - Motor Sürücü</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/wificontrol.png"  />
</p>
<p align="center"> <b>BTS7960 - 43A MOTOR Sürücü</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/BTS7960%20fritzing2.png"  />
</p>
<br><br>
* Arduino, Raspberry pi,Raspberry pi camera modülü, L298N motor sürücü, Motorlar, Güç kaynağının bağlantılarını  yukarıdaki resimdeki gibi gerçekleştiriniz.
* Yukarıdaki şekildeki gibi arduino pin bağlantılarını ve raspberry pi bağlantısını  gerçekleştirdikten sonra yapmamız gereken arduino kodlarımızı yüklemek olacaktır.<br>
**Bunu sıra ile şu  şekilde yapabilirsiniz.<br>**

**I.** Arduino kodlarının açıklamaları ve ne işe yaradığı ile ilgili detaylı bilgi kodların içinde mevcuttur.<br>

**II.** `androidToRaspberry.ino` adlı arduino kodumuzu bu [**linteken**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/T%C3%9CRK%C3%87E/V2/androidToRaspberryTurkce) indirerek ve çift tıklayarak açınız.<br>

**III.** Açılan proje dosyasını arduino' ya yüklemek için sıra ile  sekmelerden `Tools` => `Board`  ve buradan kullandığınız arduino modelinizi seçiniz.<br><br>


![Screen Shot RA1](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/ra1.png)
<br><br>
**IV.** Tekrar `Tools` sekmesinden takmış olduğunuz arduino' nuzun hangi port' a takılı olduğunu gösteriniz.  `Tools` => `port`<br>

**V.** Yukarıdaki adımları gerçekleştirdikten sonra şimdi programımızı arduino' muza yükleyebiliriz.Sol üst köşede `Upload` butonuna basarak yükleme işlemini tamamlamış oluyoruz.<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/ra2.png)
<br><br>

## RASPBERRY PI:
### AMAÇ VE GÖREVLER:

* Raspberry pi camera modülü kullanarak görüntünün alınması ve raspberry pi üzerinden telefona aktarılması.
* Arduino ve Telefon arasında bağlantının kurulması.

### RASPBERRY PI KURULUMU:
Raspberry pi kurulumu oldukça basittir.Öncelikle,

Win32DiskImager SD karta işletim sistemi yazdırmamız için gerekli olan programdır.
İndirmek için [**Tıklayınız**](http://www.gezginler.net/indir/win32-disk-imager.html)

## 1. Raspbian İşletim Sistemi İndirme;
Raspberry pi mize kuracağımız araç kontrol yazılımlarınıda içinde bulunduran işletim sistemini SD karta yazdımamız gerekmektedir.Burada DİKKAT edilmesi gereken nokta, aşağıda linkleri verilen işletim sistemlerini seçerken elinizde bulunan Wi-Fi adaptörlere göre 
işletim sistemini indirmeniz ve sd karta yazdırmanızdır.İşletim sistemleri ve destekledikleri modemler aşağıda verilmektedir.

### Raspberry Pi 3  İçin indirilebilir işletim sistemi
Raspberry pi 3 için 2 alternatif yöntemimiz vardır;<br>

1. si doğrudan raspberry pi üzerindeki dahili Wi-Fi kullanmak. <br>
2. Harici olarak USB Wi-Fi adaptör kullanmak(Mesafe ve veri hızı bakımından tavsiye edilen yöntemdir. Tabi bu kullanacağınız Wi-Fi adaptöre göre değişebilir.)
<br>

### 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/open?id=0B6yjwSAqPTgfdEV1eTlfZ0lVbW8) işletim sistemini indirerek SD karta yazdırınız.



### 2.Pi_CAR'I Raspberry pi 3 'ün  Üzerinden harici olarak taktığınız Wi-Fi modüşü kullarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing) işletim sistemini indiriniz.



Bu seçenek için elimizde bulunan ve test ettiğimiz Wi-Fi cihazları ve çipsetleri
<br>

Test Edilen cihazlar|CHIPSET
---------- | --------
Dark WDN300A5 | RTL8192CU
Tenda UH150 | RT2870/RT3070
AWUS036NH | RT2870/RT3070
<br>

Desteklenen diğer çipsetler ve cihazlar için detaylı bilgi:http://elinux.org/RPi_USB_Wi-Fi_Adapters

## 2. İşletim Sistemini Micro-SD Kart’a Yazdırma
İndirdiğimiz imaj dosyasını zip içerisinden çıkarıyoruz. Ardından daha önce indirdiğimiz win32diskImager programını açıyoruz. İmaj dosyamızı belirtilen yerden seçiyoruz.

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/win32diskimager.jpg)

Sd kartınızın bilgisayara takılı olduğundan emin olduktan sonra Device kısmında görebilirsiniz. Ardından Write butonuna tıklayıp yazma işlemini başlatıyoruz. Yazma işlemi yaklaşık 2-3 dk sürmektedir. Yazma işleminin bitmesini yeni açılan pencerede "Write Succesful." yazısını görene kadar bekleyiniz.


![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Write%20Succesful.png)
## 3.Bağlantılar ve Çalıştırma

Yazma işlemi tamamlandıktan sonra SD kartınızı bilgisayardan çıkartıp Raspberry pi'nize takabilirsiniz.
Artık yapmanız gereken SADECE Raspberry' nize USB üzerinde bir Arduino takıp  gerekli güç ve motor sürücüleri bağlantılarını yaptıktan sonra araca monte etmenizdir.
<br>
Video'lu anlatım: 
<br>
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/yNLug0DhQlc)

## ANDROID:

### AMAÇ VE GÖREVLERİ:
* Raspberry pi ve arduino ile yapılmış olan rc-arabanın kontrolünü sağlamak.
* Kullanıcı için sade ve kolay görsel arayüz.
* Raspberry pi üzerinden kamera görüntüsünü alarak kullanıcıya göstermek.

### ANDROID UYGULAMA KURULUMU:
* Uygulamanın kurulumu son derece basittir. Sadece yapılması gereken **ANDROID GOOGLE PLAY** markette giriş yapıldıktan sonra arama kutucuğuna, uygulamaya doğrudan erişmek için `com.stackcuriosity.tooght` ve ya uygulama ismi `RC CONTROLLER WITH CAMERA` yazmanız yeterlidir.<br>
<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>

### UYGULAMA KULLANIMI VE İPUCULARI  <br>

#### Raspberry pi bağlantı bilgileri
* Android uygulamanızı indirdikten sonra sizi aşağıdaki gibi bir ekran karşılayacaktır.Artık yapmanız gereken şey sadece aracı kontrol etmek olacaktır.
<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_20161208-155537.png)

Uygulamanın çalışma prensibini ve tanıtımını kısaca açıklayalım.

#### UYGULAMA DETAYLARI

##### 1. GÖRSEL ARAYÜZÜN AÇIKLANMASI VE PROGRAMLAMA MANTIĞI
* **Uygulamamız 4 temel esasa dayanmaktadır.** Bunlar;
  1. Aracın yön kontrolünün sağlanması.<br>
  2. Kullanıcıya araç üzerindeki kameradan canlı görüntünün aktarılması.<br>
  3. Aracın bağlantı sinyal seviyesi göstergesi.
  4. Fallow Me (Çok yakında).(Aracın sahibini takip etmesi).<br>
* Bu dört temel esasa göre 
*  Aracın yön kontrolünde kullanılan mantığın ana detaylarını `Arduino` bölümde anlattık.Android tarafına bakan kısmı ile açıklayacak olursak.Android tarafında, kullanıcı için `Seek bar (Hız ayarı)` , `Kamera Açma / Kapama` ,`Wi-Fi durum göstergesi`  ve `Yön tuşları` mevcuttur.<br> ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_description_githup.png)<br>
*  **Seek bar(Hız ayarı)** 15 dilimden oluşmaktadır ve hız katsayısı 17'dir.Yani seek bar' ın herbir hareketi pwm'de 17'nin katları şeklinde bir oynama yapmaktadır.Seek bar 5. kademede ise üretilen pwm= 5*17 = 85 'tir.
*  **Menü tuşları (Kamera Aç/Kapa ve WiFi Göstergesi)** Seekbar 'ın yanında yer alan diğer araç kontrol fonksiyonları;<br> Kamera görüntüsünü araç üzerinden almamıza yarayan Kamera açma ve kapatma butonu "  ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_eye.png) AÇ ", " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_eye_off.png) KAPAT ", Aynı şekilde uygulamamızın Raspberry Pi üzerinde oluşturduğumuz Wi-Fi ağa bağlanıp bağlanılmadığını gösteren bir gösterge."![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_wifi_on.png) BAĞLI DEĞİL", " ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/ic_wifi_off.png) BAĞLI "
*  **Yön tuşları** seek bar(Hız ayarı)'dan alınan verinin yönlere ayrılmasını sağlar. Aracın gidiş yönüne göre pwm değerinin başına `+` ve ya `-` işareti getirilir. **Örn;**<br><br>
 200:200     // ileri git. ( 2 motorda 200pwm ile çalışır )<br>
 -200:-200   //geri git. (2 motorda 200pwm ile çalışır)<br>
 200:-200   // sol motor 200 pwm ileri, sag motor 200 geri döner ( araç kendi etrafında soldan sağa doğru döner)<br>
 -200:200   // sol motor 200 pwm geri, sag motor 200 ileri döner ( araç kendi etrafında sağdan sola doğru döner)<br>
 200:100    // araç sağa dönecek şekilde hareket eder.<br><br> 
 * **Sinyal Seviye Göstergesi** Bu gösterge telefon ile araç arasındaki  bağlantının sinyal kalitesini ve uzaklığa göre değişen sinyal çekim seviyesinin kullanıcıya gösterilmesini sağlar.

##### 2.SAĞ'A VE SOL'A DÖNÜŞLERDE HASSASİYET
* Aracımızın sağ çağraz ve sol çapraz hareketleri yaparken dönüş yapılacak taraftaki motorların pwm değerleri düşürülür ve böylece motorların daha yavaş dönmesi sağlanır.Bu sayede araç istenilen hassasiyette çarpraz dönüşleri gerçekleştirebilir.**Bu dönüş hareketlerinin hassasiyet ayarlaması kullanıcıya bırakılmıştır.**
* Çapraz dönüşlerin hassasiyetinin hesaplanmasında kullanılan formül : **`PWM DEĞERİ - (PWM DEĞERİ / PWM ORANI)`** 'dır.
* PWM ORANI varsayılan olarak `2` gelmektedir.
* PWM ORANI ayarını, kontrol ekranın da sağ üst köşede `Ayarlar` butonundan tekrar `Ayarlar` sekmesine basarak ulaşabilirsiniz.<br>!![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205757.png)<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205807.png)<br><br>
* Girebileceğinz PWM ORANI aralığı **minimum ve maksimum olarak 1-4 arasında integer ve double tipinde** değerlerdir.
 


### UYGULAMA ICON 'UMUZ:

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/raspi_car.png)




## TEST VİDEO:
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/testvd1.png)](https://youtu.be/qbkH2KFcKqw)
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/play_video2.png)](https://youtu.be/CT-hgXIPRIk)<br><br>
<br><br>



-------------------------------------------------------------------------------------
<br><br>

#KISA VE ÖZET KURULUM<br><br>
<p align="center"> <b>DETAYLI BİLGİ VE  VE KURULUM AYRINTILARI İÇİN LÜTFEN SAYFA BAŞINDAN BAŞLAYINIZ !!</b>
<img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images//images/raw.gif" alt="DETAYLI ANLATIM VE KURULUM" align="middle" />
</p>

## **ADIM 1:**
<br>
 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfX1dsaVVJZThEN2c/view?usp=sharing) işletim sistemini indirerek SD karta yazdırınız.
<br>


 2.Pi_CAR'I Raspberry pi 3 'ün  Üzerinden harici olarak taktığınız Wi-Fi modüşü kullarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/file/d/0B6yjwSAqPTgfYkhxWEN2dXBIQlU/view?usp=sharing) işletim sistemini indiriniz.
<br>

## **ADIM 2**
Arduino kontrol yazılımını Bu [**linteken**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/tree/master/T%C3%9CRK%C3%87E/V2/androidToRaspberryTurkce) indirerek
Arduino' ya yükleyiniz.

## **ADIM 3**
Android kontrol yazılımıda  Bu [**linteken**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) indirerek
telefonunuza  yükleyiniz.
<br><br><br>
**ve  işlem tamam arduino motor sürücüleri arasındaki bağlantıları doğru yaptıysanız artık aracı kontrol etmeye başlayabilirsiniz.**

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>


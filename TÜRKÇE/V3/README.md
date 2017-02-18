# RASPBERRY PI- ARDUINO ANDROID-CONTROLLED RC-CAR ROVER WITH LIVE VIDEO STREAMING
# ----------------------------- Pi_CAR -----------------------------

[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/yotubeT1.png)](https://youtu.be/J8r_bX_RNzU)
 <p align="center" ><h1>------ İÇİNDEKİLER ------</h1></p>
 
* KULLANILAN MALZEMELER
* RASPBERRY PI KURULUMU
* ÖRNEK ARAÇ SEÇİMİ VE ARACINIZA UYGUN RASPBERRY Pİ PİN BAĞLANTI ŞEMASI
* ANDROID UYGULAMA KURULUMU VE KULLANIM KILAVUZU
* WINDOWS UYGULAMA KURULUMU VE KULLANIM KILAVUZU
* TEST VİDEOSU
* HIZLI KURULUM

## Kullanılan Malzemeler
<br>

Malzeme Adı| Adet
----| ---- 
Raspberry Pi| 1
Raspberry Pi Camera Modülü| 1
Wi-Fi Adaptör| 1 (Pi 3 için isteğe bağlı)
L298N,BTS7960,L293,ESC Motor Sürücü| 1 yada 2 
DC MOTOR|  2  yada   4
12V Lipo Batarya| 1
Jumper Kablo | ~
Araç Şasi (Gövdesi)| 1
5V Güç Kaynağı [**(LM2596-ADJ)**](http://www.robotistan.com/mini-ayarlanabilir-3a-voltaj-regulator-karti-lm2596-adj) ya da [**(2A Mini)**]( http://www.robotistan.com/2a-mini-ayarlanabilir-voltaj-dusurucu-regulator-karti)|1
<br>

## ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/pibackground32x32.png)  RASPBERRY PI:
### AMAÇ VE GÖREVLER:

* Raspberry pi kamera modülü kullanarak görüntünün alınması ve raspberry pi üzerinden telefona aktarılması.
* Telefon dan ve ya bilgisayar dan gelen verileri işleyerek motor sürücülere aktarılması.

### RASPBERRY PI KURULUMU:
Raspberry pi kurulumu oldukça basittir.Öncelikle,

Win32DiskImager SD karta işletim sistemi yazdırmamız için gerekli olan programdır.
İndirmek için [**Tıklayınız**](http://www.gezginler.net/indir/win32-disk-imager.html)

## 1. Raspbian İşletim Sistemi İndirme;
Raspberry pi mize kuracağımız araç kontrol yazılımlarınıda içinde bulunduran işletim sistemini SD karta yazdımamız gerekmektedir.Burada DİKKAT edilmesi gereken nokta, **aşağıda linkleri verilen işletim sistemlerini seçerken elinizde bulunan Wi-Fi adaptörlere ve raspberry pi modelinize göre işletim sistemini indirmeniz ve sd karta yazdırmanızdır.** İşletim sistemleri ve destekledikleri modemler aşağıda verilmektedir.

### Raspberry Pi 3  İçin indirilebilir işletim sistemi
Raspberry pi 3 için 2 alternatif yöntemimiz vardır;<br>

1. si doğrudan raspberry pi üzerindeki dahili Wi-Fi kullanmak. <br>
2. Harici olarak USB Wi-Fi adaptör kullanmak(Mesafe ve veri hızı bakımından tavsiye edilen yöntemdir. Tabi bu kullanacağınız Wi-Fi adaptöre göre değişebilir.)
<br>

### 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/open?id=0B6yjwSAqPTgfcHRRLXYwMHZ6RWs) işletim sistemini indirerek SD karta yazdırınız.




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

Sd kartınızın bilgisayara takılı olduğundan emin olduktan sonra Device kısmında görebilirsiniz. Ardından Write butonuna tıklayıp yazma işlemini başlatıyoruz. Yazma işlemi yaklaşık 5-7 dk sürmektedir. Yazma işleminin bitmesini yeni açılan pencerede "Write Succesful." yazısını görene kadar bekleyiniz.


![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Write%20Succesful.png)
## 3.Bağlantılar ve Çalıştırma
<br>
# Pi_CAR Wi-Fi  Şifresi: TRaspberry
<br>
Yazma işlemi tamamlandıktan sonra SD kartınızı bilgisayardan çıkartıp Raspberry pi'nize takabilirsiniz.
Artık yapmanız gereken SADECE Raspberry' nize  gerekli güç ve motor sürücüleri bağlantılarını yaptıktan sonra araca monte etmenizdir.
<br>

## Örnek araç seçimi ve aracınıza uygun pin bağlantısı için [tıklayınız!](https://github.com/zafersn/seraotomasyon/blob/master/select_vehicle_type.md)


# Proje anlatımında anlaşılmayan bir konu, öneriniz ve ya istekleriniz için lütfen [SORUNUZ!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)

<br>
Video'lu anlatım: 
<br>
[![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/yNLug0DhQlc)

## ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/android-icon32x32.png)   ANDROID:<br>   

### AMAÇ VE GÖREVLERİ:
* Raspberry pi ile yapılmış olan rc-arabanın ve üzerindeki cameranın kontrolünü sağlamak.
* Kullanıcı için sade ve kolay görsel arayüz.
* Raspberry pi üzerinden kamera görüntüsünü alarak kullanıcıya göstermek.

### ANDROID UYGULAMA KURULUMU:
* Uygulamanın kurulumu son derece basittir. Sadece yapılması gereken **ANDROID GOOGLE PLAY** markette giriş yapıldıktan sonra arama kutucuğuna, uygulamaya doğrudan erişmek için `com.stackcuriosity.tooght` ve ya uygulama ismi `RC CONTROLLER WITH CAMERA` yazmanız yeterlidir.<br>
<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>

### UYGULAMA KULLANIMI VE İPUCULARI  <br>

# ÖNEMLİ NOT:
Android uygulamamızı yükledikten sonra normal şartlar altında araç üzerinde oluşturduğumuz Wi-Fi alan ağına otomatik olarak bağlanması gerekmektedir.Ancak Android yeni sürümlerinde (5 ve üzeri sürümler) kullanıcı deneyimini arttırmak ve tutsak ağlara bağlanmasını engellemek amacıyla Android Google servislere bağlanmaya çalışmaktadır.Bu bağlantı durumuna göre Wi-Fi ağında veri iletişimini sağlamaktadır ya da engellemektedir. Bu durumdan dolayı Android yeni sürümlerinde (5 Ve üzeri) bizim araç üzerinde oluşturduğumuz Wi-Fi alan ağına bağlantıya izin vermemektedir.Detaylı bilgi için [Buraya tıklayın!](http://android.stackexchange.com/questions/100657/how-to-disable-captive-portal-detection-how-to-remove-exclamation-mark-on-wi-fi). Bu sorunun çözümü için 2 Alternatif yöntemimiz vardır. 
* 1.**YÖNTEM (Tavsiye Edilen)** 
   * Android Studio' yu kullanarak<br>
  Bu yöntem sizin bir android geliştirici olduğunuzu varsayarak anlatılmaktadır.<br>
    * [Buradan!]( https://developer.android.com/studio/index.html) android Studio'yu indiriniz.
    * İndirdikten ve gerekli ayarlamaları yaptıktan sonra Telefonunuzun geliştirici seçeneklerini aktif etmeniz gerekmektedir.Bunun için;
      * Ayarlar ==> Telefon Hakkında ==> Derleme Numarasına 5 defa ard arda tıklayınız.Sizin artık bir geliştirici olduğunuzu söylecektir.<br>
      yine aynı şekilde 
      * Ayarlar ==> Geliştirici Seçenekleri ==> Açık konumuna getiriniz.
      * Ayarlar ==> Geliştirici Seçenekleri ==> USB hata ayıklamasını aktif hale getiriniz
  
  Şimdi telefonunuzu bilgisayara bağlı olduğuna ve telefonun bilgisayar tarafından tanındığına emin oldukdan sonra (Tanınmadıysa driverleri yükleyiniz) Android studio ortamında görüldüğünü kontrol etmelisiniz.En basit kontrol `Shift +F10` tuşuna basarak açılan ekranda sizin telefon modeliniz gözükmesi lazım.<br><br>
  ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/telefon%20algilama.PNG)
  
  Şimdi yapmamız gereken sol altta Terminal sekmesi tıklamamız yada `Alt + F12` basmanız.
  Açılan terminal ekranın da sırayla ;
  * `adb shell`
  * `settings put global captive_portal_detection_enabled 0`<br><br>
  
   ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/terminal%20detection%20enable%200.PNG)
   
  yazmalısınız. Eğer herşey yolunda gittiyse bu komutu `settings get global captive_portal_detection_enabled` yazdığınız da terminal de `0 (sıfır)` yazmalıdır.<br>
  
  Eğer `0 (sıfır)` gördüyseniz artık araca sorunsuz bir şekilde bağlanabilir ve kullanabilirsiniz.<br>
  
* **2.YÖNTEM**
   * Ayarlar ==> Kablosuz ==> Pi_CAR ==> Gelişmiş Seçenekler
   <br>
   şifreyi yazınız: **TRaspberry**<br>
   IP ayarları = **Statik**<br>
   Ip adresi = **192.168.57.57**<br>
   Ağ geçidi = **192.168.57.1**<br>
   Ağ önek uzunluğu = **24**<br>
   DNS 1 = **8.8.8.8**<br>
   DNS 2 = **8.8.4.4**<br>
   <br>
   Yukarıdaki gerekli bilgileri girdikten sonra bağlan seçeneğine tıklayınız. Ve ip adresi alıp bağlanacaktır. Sonra size **Kablosuz bağlantıda internet erişimi yok** diye bir uyarı gelirse  **Bu ağ için bir daha sorma** seçeneğini seçtikten sonra `EVET` basınız. <br><br><br>
   **VİDEOLU ANLATIM**<br>
    
   [![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/youtube%20play2.png)](https://youtu.be/qp3TYz8y5Tc)
<br>
   Ve herşey tamam artık uygulamayı kullanabilirsiniz.
   
     
  
#### Raspberry pi bağlantı bilgileri
* Android uygulamanızı indirdikten sonra sizi aşağıdaki gibi bir ekran karşılayacaktır.Artık yapmanız gereken şey sadece aracı kontrol etmek olacaktır.
<br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_20170124-151222.png)


Uygulamanın çalışma prensibini ve tanıtımını kısaca açıklayalım.

#### UYGULAMA DETAYLARI

##### 1. GÖRSEL ARAYÜZÜN AÇIKLANMASI VE PROGRAMLAMA MANTIĞI
* **Uygulamamız 3 temel esasa dayanmaktadır.** Bunlar;
  1. Aracın ve üzerindeki kameranın hareketinin sağlanması. (Joystick, Buton ve Vr(Kamera hareketi) olmak üzere 3 ayrı kontrol yöntemi mevcuttur. )<br>
  2. Kullanıcıya araç üzerindeki kameradan canlı görüntünün aktarılması.<br>
  3. Aracın bağlantı sinyal seviyesi göstergesi.  <br>
* Bu üç temel esasa göre 
*  Aracın yön kontrolünde android tarafına bakan kısmı ile açıklayacak olursak.Android tarafında, kullanıcı için 3 ayrı kontrol arayüzü mevcuttur,bunlar yön kontrol butonları, joystick ve VR ' dır. **Şimdi bu 3 kontrol arayüzünü inceleyelim**
<br>


## Buton Kontrol Arayüzü <br>

![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013621_334.jpg)
<br><br>
 ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Screenshot_description_githup.png)<br><br>
 `Seek bar (Hız ayarı)` , `Kamera Açma / Kapama` ,`Wi-Fi durum göstergesi`  ve `Yön tuşları` mevcuttur.<br>
*  **Seek bar(Hız ayarı)** 15 dilimden oluşmaktadır ve hız katsayısı 6.66'dir.Yani seek bar' ın herbir hareketi pwm'de 6.66'nin katları şeklinde bir oynama yapmaktadır.Seek bar 5. kademede ise üretilen pwm= 5*6.66 = 33.3  'tir. Ve 33 olarak yuvarlanır.
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
* PWM ORANI ayarını, kontrol ekranın da sağ üst köşede `Ayarlar` butonundan tekrar `Ayarlar` sekmesine basarak ulaşabilirsiniz.<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205757.png)<br>![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V1Images/images/Screenshot_20160713-205807.png)<br><br>
* Girebileceğinz PWM ORANI aralığı **minimum ve maksimum olarak 1-4 arasında integer ve double tipinde** değerlerdir.
 <br>
 
# Proje anlatımında anlaşılmayan bir konu, öneriniz ve ya istekleriniz için lütfen [SORUNUZ!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)
 <br>
 
##  Joystick Kontrol Arayüzü
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013536_641.jpg)<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Joysitck_aciklma.png)

Araçın ve kameranın kontrolünün sağlandığı 2 adet joystick kontrol arayüzü mevcuttur. Bu arayüzlerden soldaki araç'ın yön kontrolünü, sağdaki ise araç üzerindeki kamera' nın yön kontrolünü sağlamaktadır.<br>
  Joystick kontrol arayüzünde dikkat edilmesi gerekli nokta,maksimum hız ayarıdır.\n Burada maksimum hız ayarı, aracın maksimum çıkabileceği hızını belirtmektedir, kamera hızı sabit olarak ayarlanmıştır.Maksimum hız ayarını belirlerken raspberry pi' nin ürettiği pwm aralığı göz önüne alınmıştır. <b> Bu aralık 0-100 'dür</b>.
  Yani araç için ayarlayacağınız maksimum hız aralığı 0-100 arasında olmalıdır
    
# Proje anlatımında anlaşılmayan bir konu, öneriniz ve ya istekleriniz için lütfen [SORUNUZ!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues) 
 <br>

## VR Kontrol Arayüzü
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_vr.png)
<br> <br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Screenshot_20170122-205445.png)
<br>
VR Arayüzünde dikkat etmeniz gereken nokta, cihazın sensorlerinin kalibrasyonludur. Uygulamada 2 türlü sensor kalibrasyon yapılmaktadır. 
* **1. kalibrasyon;** uygulamanın otomatik gerçekleştirdiği, magnometre ve gyroscope verilerinin filtre edilerek yeryüzü çoğrafyasına göre referans bir değer alınarak yapılan kalibrasyon yöntemidir.
* **2. kalibrasyon;** Bizim elle yapmamız gereken kalibrasyondur. Başımızı(Kafamızı) referans (istediğimiz noktaya) noktasına getirdikten sonra menu çubuğundan pusula ikonuna tıklamamız gerekmektedir. Bu kalibrasyon bizim kafamızın yeryüzüne göre(Kalibrasyon 1'e göre) orjinini(merkez noktasını) belirtmektedir. Bu 2. kalibrasyondan sonra kafanızı nereye çevirirseniz araç kamerası o noktaya doğru hareket edecektir.
* **NOT:** VR modu seçildiğinde aracın hareket kontrolü için 2. bir cihaza ihtiyaç duyulmaktadır. Buda yine aynı şekilde isteğe bağlı olarak ikinci bir android telefon üzerinden diğer kontrol arayüzleri kullanarak kontrol edebileceğiniz gibi Windows üzerinde geliştirdiğimiz uygulamamız ile de Fly Joystick ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Retro-Games32x32.png)  yardımı ile gerçekleştirilebilmektedir.<br>
    <br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/vr_aciklama.png)<br>   

# Proje anlatımında anlaşılmayan bir konu, öneriniz ve ya istekleriniz için lütfen [SORUNUZ!](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/issues)<br>

## ![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/Microsoft-windows-8-icon32x32.png)    WINDOWS: <br>   

### AMAÇ VE GÖREVLERİ:
* Raspberry pi ile yapılmış olan rc-arabanın kontrolünü sağlamak.
* Kullanıcı için sade ve kolay görsel arayüz.


### WINDOWS "Pi_CAR" UYGULAMA KURULUMU VE KONFİGüRASYON AYARLARI:
Pi_CAR windows uygulamasında camera desteği yoktur. Kamera görüntüsünü olmadan aracı kullanmak isteyenler için ücretsiz bir şekilde kullanıma sunulmuştur.
* **Uygulamanın aktivasyonu için ilk kurulum esnasında internet bağlantınızın olması gerekmektedir.**Bunun dışında dikkat edilmesi gereken bir nokta yoktur.
* Uygulamanın kurulumu son derece basittir. Sadece yapılması gereken uygulama setup dosyasını kurmak yeterlidir.<br>

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_pi_cart.png"/></a>
</p>

### UYGULAMA KULLANIMI VE İPUCULARI  <br>

* Windows uygulaması; aracı kontrol etmek için şuanda sadece Fly joystick desteği bulunmaktadir.<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/IMG_20170123_013829_033.jpg)<br>   
* Winodws kontrol arayüzünde dikkat edilmesi gerekli nokta,maksimum hız ayarıdır. Burada maksimum hız ayarı, aracın maksimum çıkabileceği hızını belirtmektedir.Maksimum hız ayarını belirlerken raspberry pi' nin ürettiği pwm aralığı göz önüne alınmıştır. <b> Bu aralık 0-100 'dür</b>. Yani araç için belirleyeceğiniz maksimum hız aralığı <b> 0-100 </b> arasında olmalıdır.
<br><br>
![Screen Shot](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_aciklama.png)<br><br>

# ÖNEMLİ NOT:
**Bu windows uygulamasının asıl amacı Android üzerinde VR kontrol arayüzünün kullanılması sırasında android uygulamaya alternatif olarak aracın hareket ettirilmesini sağlamaktır.**



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
 1.Pi_CAR'I Raspberry pi 2 için ya da  raspberry pi 3'ün Üzerindeki dahili Wi-Fi modülü kullanarak yönetmek istiyorsanız.Bu [**linteki**](https://drive.google.com/open?id=0B6yjwSAqPTgfcHRRLXYwMHZ6RWs) işletim sistemini indirerek SD karta yazdırınız.
<br>

## **ADIM 2**
Raspbery pi  pin bağlantılarını ve yapılmış örnek araçlar için  Bu [**linteken**](https://github.com/zafersn/WiFi-RC-Controller-With-Camera/edit/master/T%C3%9CRK%C3%87E/V3/select_vehicle_type.md) bakınız!
## **ADIM 3**
Android kontrol yazılımıda  Bu [**linteken**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) indirerek
telefonunuza  yükleyiniz.

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V2Images/images/Google.png"/></a>
</p>

## **ADIM 4** 
Windows kontrol yazılımınıda  Bu [**linkten**](https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght) bilgisayarınıza indiriniz ve yükleyiniz.

<p align="center">
 <a href="https://play.google.com/store/apps/details?id=com.stackcuriosity.tooght"><img src="https://github.com/zafersn/WiFi-RC-Controller-With-Camera/blob/master/V3Images/images/windows_pi_cart.png"/></a>
</p>

<br><br><br>
**ve  işlem tamam raspberry pi bağlantıları doğru yaptıysanız artık aracı kontrol etmeye başlayabilirsiniz.**


<br><br>




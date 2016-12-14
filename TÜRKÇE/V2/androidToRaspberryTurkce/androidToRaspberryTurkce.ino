/********************************************                  WiFi-RC-Controller-With-Camera                 **************************************************************/
/*                              ##############################            ARDUINO CODE TURKCE ANLATIM                  ##########################                         */
/*
 * 
 * 
 * 
 * yonvermede motor yonleri
 * yonVer(1,2,3,4,5);
 * 1: sag motor ileri
 * 2: sag motor geri
 * 3:sol motor geri
 * 4:sol motor iler
 * 
 * Telefon üzerinden SAĞ VE SOL motor pwmlerini ve servo motor açısını String bir şekilde örn:  200:200!888 şeklinde alıyoruz. Aradaki iki nokta üst üste  ':' ve ünlem işareti '!' ' e göre bölerek 3 elemanlı bir dizi oluşturuyoruz.
 * 
 *  '!' den sonraki değer, cameranın bağlı bulunduğu servo motor'un açı değerleridir. Bu çalışmada servo motor kullanılmamıştır.
 * 
 * 
 * Motor Hareket PWM geliş tipi ve arcın durumları
 * 
 * örn:
 * 
 * 
 *  0:0      //stop
 * 200:200     // ileri git. ( 2 motorda 200pwm ile çalışır )
 *  -200:-200   //geri gir. (2 motorda 200pwm ile çalışır)
 *  200:-200   // sol motor 200 pwm ileri, sag motor 200 geri döner ( araç kendi etrafında soldan sağa doğru döner)
 * -200:200   // sol motor 200 pwm geri, sag motor 200 ileri döner ( araç kendi etrafında sağdan sola doğru döner)
 * 200:100    // araç sağa dçnecek şekilde hareket eder.
 * 
 * 
 * 
 *  9000 //yukarı servo
 *  27000 //aşağı servo
 *  0000 //sağ servo
 *  18000 //sol servo
 * 
 * 
 * 
 *   servo1 =z ekseni yani yukarı aşağı olan servo
 *   servo2 = x ekseni yani sağa sola olan servo
 *  
 *  
 *    ls /dev/tty* //raspberry usb listesi
 *    
 *    
 *    
 *       
 */


#include <Servo.h>
Servo servo1, servo2;
//sağ motor pinleri
const int SagL = 11;                 //  /*
const int SagR = 3;                  // *               L298 MOTOR SÜRÜCÜYE GİDEN ARDUİNO NANO PWM PİNLERİ
                                     // *                            (MOTOR KONTROLÜ İÇİN)
//Sol motor pinleri                  // *                
const int SolL = 6;                  // *
const int SolR = 5;                  // */


String dizi[3];                             // 3 Elemanlı bir dizi tanımladık. 



void setup() {
  pinMode(SagL, OUTPUT);                  ///*
  pinMode(SagR, OUTPUT);                  //*       Arduino pinlerini çıkış olarak ayarladık.
  pinMode(SolL, OUTPUT);                  //*
  pinMode(SolR, OUTPUT);                  //*/



  Serial.begin(115200);                       //Arduino ile Raspberry Pi Arasında USB Haberleşme hızıdır.(Baud Rate)
  Serial.setTimeout(10);                        //Seri haberleşmede veri gelmesi için beklenecek süre. (milisaniye cinsinden.Default =1000ms'dir.)
}
void loop() {
  if (Serial.available()) {
    String gelenDeger = Serial.readString();                      //serialden gelen veriyi String bir değişkene attık
    //Serial.println(gelenDeger);
    int commaIndex = gelenDeger.indexOf(':');                     //gelen veri içinde ':' 'nın index numarasını aldık (return int )
    int commaIndex2 = gelenDeger.indexOf("!");                    // aynı şekilde gelen veri için de '!' 'nın index numarasını aldık (return int)

    if (commaIndex != (-1 ) && commaIndex2 != (-1)) {             //Hataları önlemek için gelen veride  ':' ve '!' değerlerinin olup olmadığını kontrol ettik.
      gelenDeger.trim();                                          //serial'den aldığımız veri'nin başında ve sonun da boşluk varsa yok etmek için kullandık
     
      dizi[0] = gelenDeger.substring(0, commaIndex);                      //*/
      dizi[1] = gelenDeger.substring(commaIndex + 1, commaIndex2);        //*             
      dizi[2] = gelenDeger.substring(commaIndex2 + 1);                    //*     Gelen veriyi    ':' 'nın ve '!' 'nın index numaralarına göre bölerek dizilere atadık.
      dizi[0].trim();                                                     //*     Bu atanan değerlerde varsa boşluklardan kurtulduk.
      dizi[1].trim();                                                     //*
      dizi[2].trim();                                                     //*/

      int X = (dizi[0].toInt());                                        //*           Gelen ilk 2 değeri motor pwm leri bu pwmleri String tipinden int tipine dönüştürdük.
      int Y = (dizi[1].toInt());                                        //*
     
      
      
      yonVer(X, Y);                                                     //yonver Metodumuza X ve Y parametrelerimizi girdik.

    }


  }

}





void yonVer(int X, int Y)
{
  int a = 0, b = 0, c = 0, d = 0;
  if(X<0)
    b = X *-1;
  else if(X>0)
    a = X;

  if(Y<0)
    c = Y * -1;
  else if(Y > 0)
    d = Y;

  yonVer(a, b, c, d);
}

void yonVer(int a, int b, int c, int d) {

  analogWrite(SagL, a);
  analogWrite(SagR, b);

  analogWrite(SolR, c);
  analogWrite(SolL, d);
}


#  Hamming SEC-DED Simülatörü

Bu proje, Hamming SEC-DED (Single Error Correction, Double Error Detection) algoritmasını temel alan bir hata düzeltme simülatörüdür. Python ve Tkinter kullanılarak geliştirilen bu araç, kullanıcıların ikili (binary) veriler üzerinde Hamming kodu hesaplamasını, rastgele hata eklemesini ve hatalı veriyi tespit edip düzeltmesini sağlar.

##  Amaç

Veri iletiminde meydana gelebilecek tek bitlik hataların tespit edilip düzeltilebilmesi için kullanılan Hamming algoritmasının uygulamalı olarak anlaşılmasını sağlamak.  
Simülatör, öğrenciler, öğretmenler ve mühendislik öğrencileri için sezgisel bir öğrenme aracıdır.

##  Özellikler

- 8, 16 veya 32 bit uzunluğunda rastgele ikili veri üretimi
- Hamming kodu hesaplama
- Rastgele tek bitlik hata ekleme
- Hatalı kodun analiz edilerek hatanın tespiti ve düzeltilmesi
- Kullanıcı dostu grafik arayüz (Tkinter)

##  Kullanılan Teknolojiler

- Python 3.x
- Tkinter (GUI)
- Modüler yapı: `gui.py` (arayüz), `hamming.py` (algoritmalar)
- random (rasgele hata ve veri üretimi)



# Device Information

Bu belge, `Device` sınıfını kullanarak bir cihazın bilgilerini almak için Python kodu kullanımını açıklar. `Device` sınıfı, cihazın çeşitli özelliklerini (cihaz bilgileri, disk kullanımı, CPU kullanımı, RAM kullanımı, batarya bilgileri, kopyalanan metin vb.) almak için kullanılabilir.

## Gereksinimler

Bu kodu çalıştırabilmek için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

- `os`
- `ctypes`
- `socket`
- `pyperclip`
- `psutil`
- `time`
- `datetime`

## Renkli Kod Çıktıları

Bu kod, renkli çıktılar sağlamak için `ctypes` kullanır.

Disk kullanımı bilgileri aşağıdaki gibi görüntülenir:

```python
--- Disk Kullanımı ---
Toplam: 476.94 GB
Kullanılabilir: 296.63 GB
Boşta: 180.31 GB
Percent: 37.9%
```


Kodun Kullanımı
---------------

Kodun kullanımı için aşağıdaki adımları izleyin:

1.  Gereksinimleri karşılayan gerekli kütüphaneleri yükleyin.
2.  Yukarıdaki kodu bir Python dosyasına (`device_info.py`) yapıştırın.
3.  Terminali açın ve Python betiğini çalıştırın:

```
`python device_info.py --all`
```

Yukarıdaki komut, tüm cihaz bilgilerini göstermek için `--all` bayrağını kullanır. İlgili bayrağı değiştirerek veya birden fazla bayrağı birleştirerek belirli bilgileri gösterebilirsiniz.

Örnek komutlar:

*   Cihaz bilgilerini göstermek için:
        
    `python device_info.py --device-info`
    
*   Disk kullanımını göstermek için:
    
    `python device_info.py --disk-usage`
    
*   RAM kullanımını göstermek için:
    
    `python device_info.py --ram-usage`
    
*   Batarya bilgilerini göstermek için:
    
    `python device_info.py --battery-info`
    
*   Kopyalanan metni göstermek için:
    
    `python device_info.py --copied-text`
    
*   Geçerli zamanı göstermek için:
    
    `python device_info.py --current-time`
    
*   Ağ bilgilerini göstermek için:
    
    `python device_info.py --network-info`
    
*   Birden fazla bilgiyi birleştirmek için:
    
    `python device_info.py --device-info --disk-usage --ram-usage`
    

Bu şekilde, `Device` sınıfını kullanarak cihazınızın çeşitli bilgilerini kolayca alabilirsiniz. İlgili kodu kendi projelerinize dahil edebilir ve istediğiniz şekilde uyarlayabilirsiniz.

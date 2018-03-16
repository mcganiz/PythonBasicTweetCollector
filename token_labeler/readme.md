## 1.) tweets.json dosyasını oluştururken dikkatli olun, çok fazla tweet olmasın yoksa programın çalışması çok uzun sürer veya program çöker.
## 2.) tweets.json dosyasını tweets2json.py kodunu çalıştırarak oluşturabilirsiniz.
## 3.) tweettokenizer.py programındaki değişiklikler NER projeleri için geçerlidir.

# NOT: HTML,JS ve JSON dosyaları AYNI KLASÖRDE OLMASI GEREKİYOR !!!

# 4.) Label'leri değiştirmek istiyorsanız, Json2Html.js dosyasının içerisindeki ' var dropdown_menu = .. ' değişkenini değiştirmelisiniz.
# 5.) JSON dosyasının ismi tweets.json olmalı. Değiştirmek istiyorsanız yine Json2Html.js dosyasının içerisindeki ' $.getJSON("tweets.json", function (data) {  ... ' fonksyonundaki "tweets.json" ismini değiştirmelisiniz.

NER porjeleri için;
  örnek json download şu şekildedir,
  
 {"ID":"tweet",
 "Tweet":"“President Donald J. Trump Delivers Remarks at the Shamrock☘️Bowl Presentation by Prime Minister Varadkar in the East Room of the White House” 🇺🇸🇮🇪 https://t.co/ZbogpAE09g",
 "Label":"GOOD",
 "tokens":[{"ID":"0","token":"“","Label":"URL"},{"ID":"1","token":"President","Label":"URL"},{"ID":"2","token":"Donald","Label":"URL"},{"ID":"3","token":"J","Label":"URL"},{"ID":"4","token":".","Label":"URL"},{"ID":"5","token":"Trump","Label":"URL"},{"ID":"6","token":"Delivers","Label":"URL"},{"ID":"7","token":"Remarks","Label":"URL"},{"ID":"8","token":"at","Label":"URL"},{"ID":"9","token":"the","Label":"URL"},{"ID":"10","token":"Shamrock","Label":"URL"},{"ID":"11","token":"☘","Label":"URL"},{"ID":"12","token":"️","Label":"URL"},{"ID":"13","token":"Bowl","Label":"URL"},{"ID":"14","token":"Presentation","Label":"URL"},{"ID":"15","token":"by","Label":"URL"},{"ID":"16","token":"Prime","Label":"URL"},{"ID":"17","token":"Minister","Label":"URL"},{"ID":"18","token":"Varadkar","Label":"URL"},{"ID":"19","token":"in","Label":"URL"},{"ID":"20","token":"the","Label":"URL"},{"ID":"21","token":"East","Label":"URL"},{"ID":"22","token":"Room","Label":"URL"},{"ID":"23","token":"of","Label":"URL"},{"ID":"24","token":"the","Label":"URL"},{"ID":"25","token":"White","Label":"URL"},{"ID":"26","token":"House","Label":"URL"},{"ID":"27","token":"”","Label":"URL"},{"ID":"28","token":"🇺","Label":"URL"},{"ID":"29","token":"🇸","Label":"URL"},{"ID":"30","token":"🇮","Label":"URL"},{"ID":"31","token":"🇪","Label":"URL"},{"ID":"32","token":"https://t.co/ZbogpAE09g","Label":"URL"}]}

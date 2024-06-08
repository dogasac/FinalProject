from app import db, User
from app import app

def create_user(email, password, name,surname, city, country, profile_pic):
    user = User(email=email, password=password, name=name, surname=surname,city=city, country=country, profile_pic=profile_pic)
    db.session.add(user)
    db.session.commit()

def add_user():
    user2= User(
        email = "mertcol@hotmail.com",
        password = "Password123!",
        name= "Mert",
        surname = "Çol",
        city = "İstanbul",
        country = "Türkiye",
        profile_pic = "https://img-s1.onedio.com/id-569d89cc746d233b1bead1f3/rev-0/w-600/h-600/f-jpg/s-c85f74f2274a2a26407f4de7bbb1d3e46a0c153b.jpg"
    )
    db.session.add(user2)
    db.session.commit()


class News(db.Model):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}  # Allow redefinition of the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
   
    category = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)

def add_news_to_db():
    # Haberleri veritabanına eklemek için örnek haberler
    news2 = News(
        title="Milli okçu Elif Gökkır, Paris 2024 Olimpiyatları kotasi aldı.",
        content="Türkiye Okçuluk Federasyonundan yapılan açıklamaya göre, Almanya'nın Essen kentinde düzenlenen yarışmada Elif Berra Gökkır, yarı final mücadelesinde Estonyalı rakibi Reena Parnat'a 6-4 mağlup oldu. Milli sporcu, bronz madalya maçında 5-5 berabere kaldığı Hollandalı sporcu Quinty Roeffen'ı beraberlik atışında 10-9 mağlup ederek Paris 2024 Olimpiyatları kotasını aldı.Federasyonun açıklamasında, Elif Berra ve milli takımın teknik ekibi tebrik edildi.",
        image_url="https://cdnuploads.aa.com.tr/uploads/Contents/2024/05/06/thumbs_b_c_fa729ba54c7b5dbe6cde957c649e092d.jpg?v=132435",
        category="Sports",
        source="AA"
    )
    news1 =News(
        title="İngiliz futbolcu Aaaron Lennon Kayseri günlerini anlattı",
        content="",
        image_url="https://image.fanatik.com.tr/i/fanatik/75/0x0/6281a1f945d2a0515874b4d1.jpg",
        category = "Sports",
        source="İHA"
    )
    news3 =News(
        title="Okan Buruk'un listesinde iki Süper Lig yıldızı var",
        content="Okan Buruk yönetiminde üst üste ikinci şampiyonluğunu kazanan Galatasaray, yeni sezon hazırlıklarına hız kesmeden başladı.",
        image_url="https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2026000/okan-buruk-aa-2027814.jpg",
        category = "Sports",
        source="İHA"
    )
    news4 =News(
        title="Ebrar Karakurt attığı sayı ile fizik kurallarını alt üst etti",
        content="Büyük bir heyecana sahne olan karşılaşmada Ebrar Karakurt attığı sayı ile maça damga vurdu.'Ebrar Karakurt, geometriyi büktü' başlığıyla sosyal medyada paylaşılan videonun altına 'Çok güzel bir smaaç'. 'Tekrar tekrar izledim', 'Voleybolda trivela vuruşu','İç bükey vuruş' ,şeklinde yorumlar yapıldı.",
        image_url="https://medyascope.tv/wp-content/uploads/2023/09/Ebrar2.jpg",
        category = "Sports",
        source="Haberler.com"
    )
    news5 =News(
        title="Gram altın ve çeyrek altında rekor düşüş!",
        content="Gram altın bir önceki kapanışı 2 bin 409 liradan yaparken; 8 Haziran Cumartesi günü 2 bin 381 TL'ye kadar geriledi. Bir önceki kapanışı 3 bin 940 liradan tamamlayan çeyrek altın ise bugün 3 bin 810 TL'den alıcı buluyor",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQpfT.img?w=614&h=410&m=6",
        category = "Turkey",
        source="Gazetevatan"
    )
    news6 =News(
        title="Emeklilere otobüs biletlerinde yüzde 20 uygulaması",
        content="Ulaştırma ve Altyapı Bakanlığı'na bağlı ekipler, emeklilere otobüs biletlerinde uygulanan yüzde 20 indirim imkanının Esenler Otogarı'nda uygun şekilde uygulanıp uygulanmadığını denetledi. Denetim sonucunda kurala uymayan firmalara 5 uyarı cezası verileceği belirtildi. Emekliler ise yüzde 20 indirimin yeterli olmadığını ifade etti",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nOfNj.img?w=104&h=84&q=90&m=6&f=jpg&u=t",
        category = "Turkey",
        source="Haberler.com"
    )
    news7 =News(
        title="Çin'in altın alımında flaş karar",
        content=" Çin'in altın rezervlerinin değeri Nisan sonundaki 167,96 milyar dolardan Mayıs sonunda 170,96 milyar dolara yükseldi. Son iki yıldır küresel merkez bankalarının altın talebi yüksek seviyelerde seyrediyor ve bu da fiyatları destekliyor. Dünya Altın Konseyi'ne göre, 2023 yılında 7,23 milyon onsluk net alımla Çin Merkez Bankası, en büyük resmi sektör altın alıcısı oldu",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nO4D2.img?w=720&h=490&m=6",
        category = "World",
        source="CNN"
    )
    news8 =News(
        title="Danimarka Başbakanı saldırıya uğradı",
        content="Danimarka Başbakanlık Ofisi, Başbakan Frederiksen'in Kopenhag'daki Kultorvet Meydanı'nda bir kişinin saldırısına uğradığını açıkladı. Açıklamada, saldırganın gözaltına alındığı belirtildi. Frederiksen'in saldırı nedeniyle şoke olduğu aktarılan açıklamada, şüphelinin nasıl saldırdığı ve Başbakan'ın yaralanıp yaralanmadığı konusunda bilgi verilmedi.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQtcd.img?w=768&h=432&m=6&x=415&y=78&s=136&d=136",
        category = "World",
        source="T24"
    )
    news9 =News(
        title="Netanyahu 24 Temmuz’da ABD Kongresi’nde",
        content="Uzun süredir Netanyahu’yu Kongre’ye çağırmaya çalışan ABD Temsilciler Meclisi Başkanı Mike Johnson kesinleşen tarihi sosyal medyadan duyurdu.Daha önce 10 Temmuz 1996, 24 Mayıs 2011 ve 3 Mart 2015 tarihlerinde ABD Kongresi’ne hitap eden Netanyahu, dördüncü defa kürsüye çıkacak.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQvpp.img?w=750&h=422&m=6&x=253&y=51&s=291&d=214",
        category = "World",
        source="Hürriyet"
    )
    news10 =News(
        title="Gülse Birsel'den 'Aile Arasında' müjdesi",
        content="Senarist Gülse Birsel, Aile Arasında filminin ikincisi için müjdeyi verdi. Sevilen yapımın ikinci filmi için hazırlıkların başladığını duyurdu. Gülse Birsel'in senaryosunu kaleme aldığı ve 5 milyonu aşkın seyirci tarafından izlenen 'Aile Arasında' filminin ikincisi için hazırlıklar başladı.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQu1b.img?w=306&h=197&q=90&m=6&f=jpg&x=558&y=135&u=t",
        category = "Entertainment",
        source="T24"
    )
    news11 =News(
        title="Survivor'da finale adını yazdıran ilk isim belli oldu!",
        content="Dünyanın en zor yarışması Survivor’a veda eden son yarışmacı Merve Aydın oldu. Fakat yarışmada yaşananlar bununla da sınırlı kalmadı ve Batuhan Karacakaya ilk final ismi oldu.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nPzyy.img?w=306&h=197&q=90&m=6&f=jpg&x=338&y=116&u=t",
        category = "Entertainment",
        source="CNN"
    )
    news12 =News(
        title="Bu özellik Samsung Galaxy cihazlarda kullanılamayacak",
        content="u yılın sonlarında yayınlanmaya hazırlanan Android 15, Google’ın yeni özelliklerine ince ayar yapmasıyla dikkat çekiyor. Bunlardan biri Instant Hotspot olacak. Bu yenilikler arasında, Android tabletlerin ve Chromebook’ların bir telefonun erişim noktasına sorunsuz bir şekilde bağlanmasını sağlayan kullanışlı bir araç olan Instant Hotspot (Anında Erişim Noktası) da bulunuyor. Ancak, son raporlar bu özelliğin Samsung Galaxy cihazlarda kullanılamayacağını doğruluyor.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQTjy.img?w=720&h=490&m=6&x=0&y=34&s=346&d=371",
        category = "Sci/Tech",
        source="CNN"
    )
    news13 =News(
        title="Apple ve OpenAI Anlaştı",
        content="Apple ve OpenAI arasında anlaşma sağlandı. Fakat anlaşmanın ayrıntıları bilinmiyor, muhtemelen kullanıclar ChatGPT için kullanılan teknolojilere Siri aracılığıyla ulaşacak. Bununla birlikte Apple’ın yapay zeka uygulama mağazası oluşturmak istediğine dair dedikodular vardı, OpenAI bu mağazayı dolduracak birkaç şirketten biri olabilir.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nNlJI.img?w=534&h=363&m=6",
        category = "Sci/Tech",
        source="CNN"
    )
    news14 =News(
        title="Starlink’e rakip geldi",
        content="Çin, uzayda büyük bir hamle yaparak, dünya genelinde internet erişimi sağlamak için 10 bin uydu fırlatmayı planlıyor. Bu proje, Elon Musk’ın Starlink’ine ciddi bir rakip olacak. Elon Musk’ın Starlink projesi, dünya genelinde internet erişimi sağlamak için şu ana kadar 5 bin 874 uyduyu yörüngeye yerleştirdi ve toplamda 42 bin uydu fırlatmayı planlıyor. Ancak Çin de boş durmuyor. ",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nF2Jn.img?w=534&h=363&m=6&x=27&y=228&s=358&d=60",
        category = "Top stories ",
        source="CNN"
    )
    news15 =News(
        title="Aydın'da dün gece çıkan orman yangını 6 saatte söndürüldü",
        content="Aydın'ın Kuyucak ilçesinde dün gece çıkan orman yangını, karadan ve havadan müdahaleyle 6 saatte söndürüldü. Yangında, 26 hektar alanın zarar gördüğü belirtildi. Kuyucak ilçesi kırsal Çobanisa Mahallesi yakınlarındaki ormanda, dün saat 23.00 sıralarında yangın çıktı.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQLXa.img?w=534&h=363&m=6",
        category = "Top stories",
        source="CNN"
    )
    news16 =News(
        title="SpaceX Starship roketi 4'üncü test uçuşunu tamamladı",
        content="Elon Musk'ın SpaceX şirketinin Starship roketi, dördüncü test uçuşunu gerçekleştirdi. Bu uçuş, Musk'ın Mars'ı kolonileştirme planları ve NASA'nın Ay'a insan gönderme çabaları için önemli bir adım olarak görülüyor",
        image_url="data:image/webp;base64,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",
        category = "Top stories",
        source="Haberler.com"
    )
    news17 =News(
        title="Akaryakıt fiyatlarına çifte indirim geliyor!",
        content="BRENT petrol fiyatlarındaki düşüşler, benzin ve mazot fiyatlarını da etkiledi. Sektör yetkililerinden alınan bilgilere göre, akaryakıt fiyatlarında çift yönlü bir indirim bekleniyor. Brent petrol fiyatlarındaki düşüşlerin ardından akaryakıt fiyatları da gerilemeye başladı.",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nIJt3.img?w=534&h=363&m=6&x=79&y=357&s=122&d=122",
        category = "Business",
        source="Haberler.com"
    )
    news18 =News(
        title="Müzisyenler için hem iyi hem de kötü olabilir",
        content="Bu aralar Gemini veya GPT-4o gündemde, ancak Suna AI ‘ın yeni yetenekleri de hayata geçmeye hazırlanıyor. Bilmeyenler için biraz Suno’dan bahsedecek olursak, yazıyı müziğe dönüştüren bir yapay zeka. Mesela şarkı sözü yazdınız diyelim. Bu şarkı sözüyle Suno AI’da rock, rap, pop veya başka bir türde parça oluşturabilirsiniz. ",
        image_url="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nQLUs.img?w=534&h=363&m=6",
        category = "Business",
        source="Haberler.com"
    )
   
    db.session.add(news2)
    db.session.add(news1)
    db.session.add(news3)
    db.session.add(news4)
    db.session.add(news5)
    db.session.add(news6)
    db.session.add(news7)
    db.session.add(news8)
    db.session.add(news9)
    db.session.add(news10)
    db.session.add(news11)
    db.session.add(news12)
    db.session.add(news13)
    db.session.add(news14)
    db.session.add(news15)
    db.session.add(news16)
    db.session.add(news17)
    db.session.add(news18)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Caution: This will delete all data!
        db.create_all()
        add_news_to_db()
        add_user()
        print("Database and sample data created!")

# Marks
İşaretler, daha sonra donanımlar veya eklentiler tarafından erişilebilen işlevleri test etmek için (ancak donanımları değil) meta verileri uygulamak için kullanılabilir.
İşareti kullanarak, test işlevlerinizdeki meta verileri kolayca ayarlayabilirsiniz
<br><li><b>usefixtures: </b>bir test işlevinde veya sınıfta fikstürleri kullanın
<li><b>filterwarnings:</b> bir test işlevinin belirli uyarılarını filtreleyin
<li><b>skip:</b>  her zaman bir test işlevini atla
<li><b>skipif:</b> belirli bir koşul karşılanırsa bir test işlevini atlayın
<li><b>xfail: </b>belirli bir koşul karşılanırsa "beklenen bir başarısızlık" sonucu üretir
<li><b>parametrize:</b> aynı test işlevine birden çok çağrı gerçekleştirin.

<h4>@pytest.marks.filterwarnings</h4>

İşaretli test öğelerine uyarı filtreleri ekler.

<b>@pytest.mark.filterwarnings(<i>filter</i>)</b>
<br><b><u>param:</b></u> (str) action, message, category, module, lineno
<br>Örnek:
<br>@pytest.mark.filterwarnings("ignore:.*usage will be deprecated.\* : DeprecationWarning")
<br>
<h4>@pytest.marks.parametrize</h4>
<b>Parametres:</b> (argnames, argvalues, indirect=False, ids=None, scope=None, *, _param_mark=None)<br>

<h4>@pytest.mark.skip</h4>
Test fonksiyonlarını atlar. Bir test koşulunu sebepsiz atlar. <br>
<b>pytest.mark.skip(reason=None)</b><br>
reason(sebep)=None(yok)

<h4>@pytest.mark.skipif</h4>
Test koşulunu atlar. Bir test koşuluna denk gelindiğinde sebepsiz atlar. <br>
<b>pytest.mark.skipif(condition,*,reason=None)</b><br>
condition(koşul): bool veya str olabilir. Bool ise True/False<br>reason(sebep)=None(yok)

<h4>@pytest.mark.usefixtures</h4>
Bu fonksiyon ile sınıf ve modüllerde demirbaş kullanımı sağlar.<br>
<b>pytest.mark.usefixtures(*names)</b><br>

<h4>@pytest.mark.xfail</h4>
Test fonksiyonlarının başarısız olması durumunda yapılacak işlemler için koullanılan fonksiyondur.<br>
<b>pytest.mark.xfail(condition=None, *, reason=None, raises=None, run=True, strict=False)</b><br>
<li><b>koşul: (bool veya str) </b> Test işlevini xfail ( True/Falseveya bir koşul dizesi ) olarak işaretleme koşulu. Bir bool ise, ayrıca belirtmeniz gerekir reason( koşul dizesine bakın ).
<li><b>Reason: (str) </b> Test işlevinin xfail olarak işaretlenmesinin nedeni. 
<li><b>Raises-yükseltir (Tür [İstisna])</b>  Test işlevi tarafından oluşturulması beklenen istisna alt sınıfı (veya alt sınıfların demetleri); diğer istisnalar testi geçemez.
<li><b>run: (bool)</b> – Test işlevi gerçekten yürütülmeliyse. ise False, işlev her zaman xfail olur ve yürütülmez (bir işlev segfault yapıyorsa kullanışlıdır).
<li><b>katı (bool):</b>
<ul>
Eğer (varsayılan: <i>False</i>) ise, fonksiyon terminal çıkışında başarısız olmuş ve başarılı olmuş <b>False</b> gibi gösterilecektir . Her iki durumda da bu, test paketinin bir bütün olarak başarısız olmasına neden olmaz. Bu, daha sonra ele alınmak üzere lapa lapa testleri (rastgele başarısız olan testler) işaretlemek için özellikle yararlıdır .xfailedxpass
</ul><ul>
Eğer <b>True</b>, fonksiyon başarısız olmuş gibi uçbirim çıkışında gösterilecek xfailed, ancak beklenmedik bir şekilde başarılı olursa, test takımında başarısız olacaktır. Bu, özellikle her zaman başarısız olan işlevleri işaretlemek için kullanışlıdır ve beklenmedik bir şekilde geçmeye başlarlarsa açık bir gösterge olmalıdır (örneğin, bir kitaplığın yeni bir sürümü bilinen bir hatayı düzeltir).</ul>

<h3> Custom Marks </h3>
İşaretler, fabrika nesnesi kullanılarak dinamik olarak oluşturulur pytest.mark ve dekoratör olarak uygulanır.
@pytest.mark.timeout(10, "slow", method="thread")


<head><h2>MarkDecorator</h2></head>
<i><u>class</u></i> <b>MarkDecorator</b><br>
Test işlevlerine ve sınıflarına işaret uygulamak için bir dekoratör.

Mark Decorators ile oluşturulur <b>@pytest.mark:</b>

<blockquote> mark1 = pytest.mark.NAME.................# Simple MarkDecorator</blockquote>
<blockquote> mark2 = pytest.mark.NAME(name1=value)..# Parametrized MarkDecorator</blockquote>
ve daha sonra işlevleri test etmek için dekoratörler olarak uygulanabilir:

<b>@mark2<br>
def test_function():<br>
&ensp;&thinsp;&ensp;&thinsp;&ensp;pass</b><br>
<u>Çağrıldığında MarkDecorator, aşağıdakileri yapar:</u>

<ol><li>Tek konum bağımsız değişkeni olarak tek bir sınıfla çağrılırsa ve ek anahtar sözcük bağımsız değişkenleri olmadan, işareti sınıfa iliştirir, böylece o sınıfta bulunan tüm test durumlarına otomatik olarak uygulanır.

<li>Tek konum bağımsız değişkeni olarak tek bir işlevle çağrılırsa ve ek anahtar sözcük bağımsız değişkenleri olmadan, zaten dahili olarak depolanan tüm bağımsız değişkenleri içeren işlevi işaretler MarkDecorator.

<li>Başka bir durumda çağrıldığında, bu çağrıya iletilen bağımsız değişkenlerle güncellenen MarkDecorator orijinal içeriğiyle yeni bir örnek döndürür.MarkDecorator</ol>

<b>Not:</b> Yukarıdaki kurallar, MarkDecoratora'nın herhangi bir ek anahtar sözcük veya konum bağımsız değişkeni olmaksızın yalnızca tek bir işlevi veya sınıf referansını konum bağımsız değişkeni olarak depolamasını engeller. kullanarak bu sorunu çözebilirsiniz with_args().

<b>name </b>
 mark.name için takma ad.

<b>args</b>
mark.args için takma ad.

<b>kwargs</b>
mark.kwargs için takma ad.

<b>with_args</b> (* args , ** kwargs)
Ekstra bağımsız değişkenler eklenmiş bir MarkDecorator döndürün.

MarkDecorator'ı çağırmanın aksine, tek argüman çağrılabilir/sınıf olsa bile with_args() kullanılabilir.

<b>parametreler</b>
argümanlar ( nesne ) –

kwargs ( nesne ) –

Dönüş türü
_pytest.mark.structures.MarkDecorator

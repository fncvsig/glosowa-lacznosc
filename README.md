# Głosowa łączność z komputerem
Projekt trzyosobowy, dotyczący sterowania inteligentnym budynkiem za pomocą mowy

## Rozpoznawane komendy
* ciepło
* dół
* góra
* jeden
* lewo
* otwórz
* prawo
* przód
* start
* stop
* tył
* wyłącz
* włącz
* zamknij
* zero
* zimno

## Czym sterujemy i w jaki sposób?
Zastanawiałyśmy się nad wieloma rozwiązaniami, które można zaliczyc do Smart Home / Smart Building Solutions. Pod uwagę były brane m.in. ochrona przed włamaniami, monitorowanie zużycia mediów, alarmowanie np. o przeciekających rurach czy autouzupełnianie / autozamawianie produktów domowych. Stwierdziłyśmy, że kierunkiem w którym podążymy, będzie typowo dla zwiększenia komfortu we własnym domu, a konretniej w sypialni / salonie.

Nasze komendy obejmują sterowanie:

Oświetleniem: 
* `włącz` - włącza światło
* `wyłącz` - wyłącza światło

Temperaturą:
* `ciepło` - zmniejsza ogrzewanie
* `zimno` - zwiększa ogrzewanie

Budzikiem:
* `start` - nastawia budzik
* `stop` - wyłącza budzik

Oknem:
* `otwórz` - uchyla okno
* `zamknij` - zamyka okno 

Roletami:
* `góra` - unosi rolety 
* `dół` - zasłania rolety 

Telewizorem:
* `jeden` - włącza telewizor
* `zero` - wyłącza telewizor
* `prawo` - obraca ekran telewizora w prawo
* `lewo` - obraca ekran telewizora w lewo

Fotelem:
* `przód` - pochyla oparcie fotela do przodu
* `tył` - odchyla oparcie fotela do tyłu

## Typ danych
Pliki dźwiękowe (komendy) mają częstotliwość 8kHz i są zapisywane z rozszerzeniem .wav 

Każda z 16 komend była nagrywana przez trzy różne osoby pracujące nad tym projektem (Anna Straś, Martyna Szot, Kamila Chyży), o różnych porach dnia przez kilka dni, w sumie 38 razy.

## Włączenie programu na własnym komputerze
Wymagania wstępne:
* Python 3
* biblioteki `pandas`, `numpy`, `scipy`, `pickle`, `sklearn`
* środowisko do uruchamiania kodu w pythonie (np. PyCharm)

1. Pobierz zawartość tego repozytorium 
2. Uruchom `classifyTestData.py` w celu obejrzenia wyników klasyfikacji komend testowych

W razie zmiany w folderach `data` lub `tests` uruchom pliki w następującej kolejności:
* `createMFCCdata.py`  (tworzy `results.csv`, plik z cechami MFCC dla danych wejściowych)
* `createKNN.py` (tworzy `knn.sav`, model k-nn na podstawie cech MFCC)
* `classifyTestData.py`  (klasyfikuje dane testowe na podstawie modelu knn)

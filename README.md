## Приложение "Конвертер валюты"

Данное приложение может конвертировать сумму из одной валюты в другую и вывести результат.

Приложение использует взаимодействие с [Fixer API](https://fixer.io/). Он предоставляет информацию о текущем курсе нужной валюты.

### Используемые зависимости:
* django = 5.1.3
* djangorestframework = 3.15.2
* requests = 2.32.3
* python-dotenv = 1.0.1
* drf-yasg = 1.21.8
* docker



### Для работы с приложением необходимо:

1. Зайти на сайт [Fixer API](https://fixer.io/) и получить личный **API Access Key**;
2. Создать файл [.env]() и скопировать в него переменную `API_ACCESS_TOKEN `из файла [.env.sample](.env.sample) или переименовать его;
3. Скопировать полученный API Access Key  в переменную `API_ACCESS_TOKEN` находящуюся в файле [.env]();
4. Запустить программу командами `docker build . -t test_image`, `docker run -it -p 8000:8080 -d test_image`. Сервер запуститься по адресу "http://0.0.0.0:8000/";
5. Пройдя по эндпоинту `/converter/` заполните 3 обязательных поля: 
   
   `amount` - сумма необходимая для конвертации;
   
   `currency_from ` - Валюта с которой происходит конвертация. Указывается сокращение валюты тремя большими буквами "EUR" (**!!! При бесплатном API access KEY, конвертация возможна только с EUR, при установке другой валюты в это поле сервис запрос не обрабатывает. При платном API access key таких ограничений нет.!!!**);

   `currency_to` - Валюта на которую происходит конвертация. Так же указывается сокращение валюты тремя большими буквами.
6. При успешной обработке данных выводится результат в JSON-формате:


    {

       "result": 113.45

    }
7. При неправильно внесенных данных выводится:


    {

       "message": Введена некорректная валюта!

    }
8. Документация приложения находится по эндпоинту: `/redoc/`

### Список валют:

* **AED** - 	United Arab Emirates dirham	 United Arab Emirates
* **AFN** - 	Afghan afghani	 Afghanistan
* **ALL** - 	Albanian lek	 Albania
* **AMD** - 	Armenian dram	 Armenia
* **ANG** - 	Netherlands Antillean guilder	 Curaçao (CW),  Sint Maarten (SX)
* **AOA** - 	Angolan kwanza	 Angola
* **ARS** - 	Argentine peso	 Argentina
* **AUD** - 	Australian dollar	 Australia,  Christmas Island (CX),  Cocos (Keeling) Islands (CC),  Heard Island and McDonald Islands (HM),  Kiribati (KI),  Nauru (NR),  Norfolk Island (NF),  Tuvalu (TV)
* **AWG** - 	Aruban florin	 Aruba
* **AZN** - 	Azerbaijani manat	 Azerbaijan
* **BAM** - 	Bosnia and Herzegovina convertible mark	 Bosnia and Herzegovina
* **BBD** - 	Barbados dollar	 Barbados
* **BDT** - 	Bangladeshi taka	 Bangladesh
* **BGN** - 	Bulgarian lev	 Bulgaria
* **BHD** - 	Bahraini dinar	 Bahrain
* **BIF** - 	Burundian franc	 Burundi
* **BMD** - 	Bermudian dollar	 Bermuda
* **BND** - 	Brunei dollar	 Brunei Darussalam
* **BOB** - 	Boliviano	 Bolivia
* **BOV** - 	Bolivian Mvdol (funds code)	 Bolivia
* **BRL** - 	Brazilian real	 Brazil
* **BSD** - 	Bahamian dollar	 Bahamas
* **BTN** - 	Bhutanese ngultrum	 Bhutan
* **BWP** - 	Botswana pula	 Botswana
* **BYN** - 	Belarusian ruble	 Belarus
* **BZD** - 	Belize dollar	 Belize
* **CAD** - 	Canadian dollar	 Canada
* **CDF** - 	Congolese franc	 Democratic Republic of the Congo
* **CHE** - 	WIR euro (complementary currency)	  Switzerland
* **CHF** - 	Swiss franc	  Switzerland,  Liechtenstein (LI)
* **CHW** - 	WIR franc (complementary currency)	  Switzerland
* **CLF** - 	Unidad de Fomento (funds code)	 Chile
* **CLP** - 	Chilean peso	 Chile
* **CNY** - 	Renminbi[6]	 China
* **COP** - 	Colombian peso	 Colombia
* **COU** -    Unidad de Valor Real (UVR) (funds code)[7]	 Colombia
* **CRC** - 	Costa Rican colon	 Costa Rica
* **CUP** - 	Cuban peso	 Cuba
* **CVE** - 	Cape Verdean escudo	 Cabo Verde
* **CZK** - 	Czech koruna	 Czechia[8]
* **DJF** - 	Djiboutian franc	 Djibouti
* **DKK** - 	Danish krone	 Denmark,  Faroe Islands (FO),  Greenland (GL)
* **DOP** - 	Dominican peso	 Dominican Republic
* **DZD** - 	Algerian dinar	 Algeria
* **EGP** - 	Egyptian pound	 Egypt
* **ERN** - 	Eritrean nakfa	 Eritrea
* **ETB** - 	Ethiopian birr	 Ethiopia
* **EUR** - 	Euro	 Åland Islands (AX),  Andorra (AD)[c],  Austria (AT),  Belgium (BE),  Croatia (HR),  Cyprus (CY),  Estonia (EE),  European Union (EU),  Finland (FI),  France (FR),  French Guiana (GF),  French Southern and Antarctic Lands (TF),  Germany (DE),  Greece (GR),  Guadeloupe (GP),  Ireland (IE),  Italy (IT),  Kosovo (XK)[d],  Latvia (LV),  Lithuania (LT),  Luxembourg (LU),  Malta (MT),  Martinique (MQ),  Mayotte (YT),  Monaco (MC)[c],  Montenegro (ME)[d],  Netherlands (NL),  Portugal (PT),  Réunion (RE),  Saint Barthélemy (BL),  Saint Martin (MF),  Saint Pierre and Miquelon (PM),  San Marino (SM)[c],  Slovakia (SK),  Slovenia (SI),  Spain (ES),  Vatican City (VA)[c]
* **FJD** - 	Fiji dollar	 Fiji
* **FKP** - 	Falkland Islands pound	 Falkland Islands (pegged to GBP 1:1)
* **GBP** - 	Pound sterling	 United Kingdom,  Isle of Man (IM, see Manx pound),  Jersey (JE, see Jersey pound),  Guernsey (GG, see Guernsey pound),  Tristan da Cunha (SH-TA)
* **GEL** - 	Georgian lari	 Georgia
* **GHS** - 	Ghanaian cedi	 Ghana
* **GIP** - 	Gibraltar pound	 Gibraltar (pegged to GBP 1:1)
* **GMD** - 	Gambian dalasi	 Gambia
* **GNF** - 	Guinean franc	 Guinea
* **GTQ** - 	Guatemalan quetzal	 Guatemala
* **GYD** - 	Guyanese dollar	 Guyana
* **HKD** - 	Hong Kong dollar	 Hong Kong
* **HNL** - 	Honduran lempira	 Honduras
* **HTG** - 	Haitian gourde	 Haiti
* **HUF** - 	Hungarian forint	 Hungary
* **IDR** - 	Indonesian rupiah	 Indonesia
* **ILS** - 	Israeli new shekel	 Israel
* **INR** - 	Indian rupee	 India,  Bhutan
* **IQD** - 	Iraqi dinar	 Iraq
* **IRR** - 	Iranian rial	 Iran
* **ISK** - 	Icelandic króna (plural: krónur)	 Iceland
* **JMD** - 	Jamaican dollar	 Jamaica
* **JOD** - 	Jordanian dinar	 Jordan
* **JPY** - 	Japanese yen	 Japan
* **KES** - 	Kenyan shilling	 Kenya
* **KGS** - 	Kyrgyzstani som	 Kyrgyzstan
* **KHR** - 	Cambodian riel	 Cambodia
* **KMF** - 	Comoro franc	 Comoros
* **KPW** - 	North Korean won	 North Korea
* **KRW** -    South Korean won	 South Korea
* **KWD** - 	Kuwaiti dinar	 Kuwait
* **KYD** - 	Cayman Islands dollar	 Cayman Islands
* **KZT** - 	Kazakhstani tenge	 Kazakhstan
* **LAK** - 	Lao kip	 Lao People's Democratic Republic
* **LBP** - 	Lebanese pound	 Lebanon
* **LKR** - 	Sri Lankan rupee	 Sri Lanka
* **LRD** - 	Liberian dollar	 Liberia
* **LSL** - 	Lesotho loti	 Lesotho
* **LYD** - 	Libyan dinar	 Libya
* **MAD** - 	Moroccan dirham	 Morocco,  Western Sahara
* **MDL** - 	Moldovan leu	 Moldova
* **MGA** -    Malagasy ariary	 Madagascar
* **MKD** - 	Macedonian denar	 North Macedonia
* **MMK** - 	Myanmar kyat	 Myanmar
* **MNT** - 	Mongolian tögrög	 Mongolia
* **MOP** - 	Macanese pataca	 Macau
* **MRU** -    Mauritanian ouguiya	 Mauritania
* **MUR** - 	Mauritian rupee	 Mauritius
* **MVR** - 	Maldivian rufiyaa	 Maldives
* **MWK** - 	Malawian kwacha	 Malawi
* **MXN** - 	Mexican peso	 Mexico
* **MXV** - 	Mexican Unidad de Inversion (UDI) (funds code)	 Mexico
* **MYR** - 	Malaysian ringgit	 Malaysia
* **MZN** - 	Mozambican metical	 Mozambique
* **NAD** - 	Namibian dollar	 Namibia (pegged to ZAR 1:1)
* **NGN** - 	Nigerian naira	 Nigeria
* **NIO** - 	Nicaraguan córdoba	 Nicaragua
* **NOK** - 	Norwegian krone	 Norway,  Svalbard and  Jan Mayen (SJ),  Bouvet Island (BV)
* **NPR** - 	Nepalese rupee	   Nepal
* **NZD** - 	New Zealand dollar	 New Zealand,  Cook Islands (CK),  Niue (NU),  Pitcairn Islands (PN; see also Pitcairn Islands dollar),  Tokelau (TK)
* **OMR** - 	Omani rial	 Oman
* **PAB** - 	Panamanian balboa	 Panama
* **PEN** - 	Peruvian sol	 Peru
* **PGK** - 	Papua New Guinean kina	 Papua New Guinea
* **PHP** - 	Philippine peso[11]	 Philippines
* **PKR** - 	Pakistani rupee	 Pakistan
* **PLN** - 	Polish złoty	 Poland
* **PYG** - 	Paraguayan guaraní	 Paraguay
* **QAR** - 	Qatari riyal	 Qatar
* **RON** - 	Romanian leu	 Romania
* **RSD** - 	Serbian dinar	 Serbia
* **RUB** - 	Russian ruble	 Russia
* **RWF** - 	Rwandan franc	 Rwanda
* **SAR** - 	Saudi riyal	 Saudi Arabia
* **SBD** - 	Solomon Islands dollar	 Solomon Islands
* **SCR** - 	Seychelles rupee	 Seychelles
* **SDG** - 	Sudanese pound	 Sudan
* **SEK** - 	Swedish krona (plural: kronor)	 Sweden
* **SGD** - 	Singapore dollar	 Singapore
* **SHP** - 	Saint Helena pound	 Saint Helena (SH-HL),  Ascension Island (SH-AC)
* **SLE** - 	Sierra Leonean leone (new leone)[12][13][14]	 Sierra Leone
* **SOS** - 	Somalian shilling	 Somalia
* **SRD** - 	Surinamese dollar	 Suriname
* **SSP** - 	South Sudanese pound	 South Sudan
* **STN** -    São Tomé and Príncipe dobra	 São Tomé and Príncipe
* **SVC** - 	Salvadoran colón	 El Salvador
* **SYP** - 	Syrian pound	 Syria
* **SZL** - 	Swazi lilangeni	 Eswatini[11]
* **THB** - 	Thai baht	 Thailand
* **TJS** - 	Tajikistani somoni	 Tajikistan
* **TMT** - 	Turkmenistan manat	 Turkmenistan
* **TND** - 	Tunisian dinar	 Tunisia
* **TOP** - 	Tongan paʻanga	 Tonga
* **TRY** - 	Turkish lira	 Turkey
* **TTD** - 	Trinidad and Tobago dollar	 Trinidad and Tobago
* **TWD** - 	New Taiwan dollar	 Taiwan
* **TZS** - 	Tanzanian shilling	 Tanzania
* **UAH** - 	Ukrainian hryvnia	 Ukraine
* **UGX** - 	Ugandan shilling	 Uganda
* **USD** - 	United States dollar	 United States,  American Samoa (AS),  British Indian Ocean Territory (IO) (also uses GBP),  British Virgin Islands (VG),  Bonaire, Sint Eustatius and Saba (BQ - Caribbean Netherlands),  Ecuador (EC),  El Salvador (SV),  Guam (GU),  Marshall Islands (MH),  Federated States of Micronesia (FM),  Northern Mariana Islands (MP),  Palau (PW),  Panama (PA) (as well as Panamanian Balboa),  Puerto Rico (PR),  Timor-Leste (TL),  Turks and Caicos Islands (TC),  U.S. Virgin Islands (VI),  United States Minor Outlying Islands (UM)
* **USN** - 	United States dollar (next day) (funds code)	 United States
* **UYI** - 	Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)	 Uruguay
* **UYU** - 	Uruguayan peso	 Uruguay
* **UYW** - 	Unidad previsional[16]	 Uruguay
* **UZS** - 	Uzbekistani sum	 Uzbekistan
* **VED** - 	Venezuelan digital bolívar[17]	 Venezuela
* **VES** - 	Venezuelan sovereign bolívar[11]	 Venezuela
* **VND** - 	Vietnamese đồng	 Vietnam
* **VUV** - 	Vanuatu vatu	 Vanuatu
* **WST** - 	Samoan tala	 Samoa
* **XAF** - 	CFA franc BEAC	 Cameroon (CM),  Central African Republic (CF),  Republic of the Congo (CG),  Chad (TD),  Equatorial Guinea (GQ),  Gabon (GA)
* **XAG** - 	Silver (one troy ounce)
* **XAU** - 	Gold (one troy ounce)
* **XBA** - 	European Composite Unit (EURCO) (bond market unit)
* **XBB** - 	European Monetary Unit (E.M.U.-6) (bond market unit)
* **XBC** - 	European Unit of Account 9 (E.U.A.-9) (bond market unit)
* **XBD** - 	European Unit of Account 17 (E.U.A.-17) (bond market unit)
* **XCD** - 	East Caribbean dollar	 Anguilla (AI),  Antigua and Barbuda (AG),  Dominica (DM),  Grenada (GD),  Montserrat (MS),  Saint Kitts and Nevis (KN),  Saint Lucia (LC),  Saint Vincent and the Grenadines (VC)
* **XDR** - 	Special drawing rights	International Monetary Fund
* **XOF** - 	CFA franc BCEAO	 Benin (BJ),  Burkina Faso (BF),  Côte d'Ivoire (CI),  Guinea-Bissau (GW),  Mali (ML),  Niger (NE),  Senegal (SN),  Togo (TG)
* **XPD** - 	Palladium (one troy ounce)
* **XPF** - 	CFP franc (franc Pacifique)	French territories of the Pacific Ocean:  French Polynesia (PF),  New Caledonia (NC),  Wallis and Futuna (WF)
* **XPT** - 	Platinum (one troy ounce)
* **XSU** - 	SUCRE	Unified System for Regional Compensation (SUCRE)[18]
* **XTS** - 	Code reserved for testing
* **XUA** - 	ADB Unit of Account	African Development Bank[19]
* **YER** - 	Yemeni rial	 Yemen
* **ZAR** - 	South African rand	 Eswatini,  Lesotho,  Namibia,  South Africa
* **ZMW** - 	Zambian kwacha	 Zambia





import requests

quantity,initial,to = '','',''

class Conveter:
    
    def get_data():
        global quantity,initial,to
        quantity = input("Enter Quantity (default =  1):") or "1"
        initial = input("Enter From Currency code (default = USD):") or "USD"
        to = input("Enter to currency code (default = INR):") or "INR"
        Conveter.currency_convert()
    
    def print_currency_codes():
        print("\033[1m"+'\033[91m'+"Afghanistan-AFN              Albania-ALL                  Algeria-DZD               American Samoa-USD           Andorra-EUR                  Angola-AOA                   Anguilla-XCD              Antarctica-XCD\n")
        print("Antigua and Barbuda-XCD      Argentina-ARS                Armenia-AMD               Aruba-AWG                    Australia-AUD                Austria-EUR                  Azerbaijan-AZN            Bahamas-BSD\n")
        print("Bahrain-BHD                  Bangladesh-BDT               Barbados-BBD              Belarus-BYR                  Belgium-EUR                  Belize-BZD                   Benin-XOF                 Bermuda-BMD\n")
        print("Bhutan-BTN                   Bolivia-BOB                  Bosnia-Herzegovina-BAM    Botswana-BWP                 Bouvet Island-NOK            Brazil-BRL                   British Indian Ocean Territory-USD\n")
        print("Brunei Darussalam-BND        Bulgaria-BGN                 Burkina Faso-XOF          Burundi-BIF                  Cabo Verde-CVE               Cambodia-KHR                 Cameroon-XAF              Canada-CAD\n")
        print("Cayman Islands-KYD           Central African Republic-XAF Chad-XAF                  Chile-CLP                    China-CNY                    Christmas Island-AUD         Cocos (Keeling) Islands-AUD\n")
        print("Colombia-COP                 Comoros-KMF                  Congo-XAF                 Congo, Dem. Republic-CDF     Cook Islands-NZD             Costa Rica-CRC               Croatia-HRK               Cuba-CUP\n")
        print("Cyprus-EUR                   Czechia-CZK                  Denmark-DKK               Djibouti-DJF                 Dominica-XCD                 Dominican Republic-DOP       Ecuador-ECS               Egypt-EGP\n")
        print("El Salvador-SVC              Equatorial Guinea-XAF        Eritrea-ERN               Estonia-EUR                  Ethiopia-ETB                 European Union-EUR           Falkland Islands (Malvinas)-FKP\n")
        print("Faroe Islands-DKK            Fiji-FJD                     Finland-EUR               France-EUR                   French Guiana-EUR            French Southern Territories-EUR                        Gabon-XAF\n")
        print("Gambia-GMD                   Georgia-GEL                  Germany-EUR               Ghana-GHS                    Gibraltar-GIP                Great Britain-GBP            Greece-EUR                Greenland-DKK\n")
        print("Grenada-XCD                  Guadeloupe (French)-EUR      Guam (USA)-USD            Guatemala-QTQ                Guernsey-GGP                 Guinea-GNF                   Guinea Bissau-GWP         Guyana-GYD\n")
        print("Haiti-HTG                    Heard Island and McDonald Islands-AUD                  Honduras-HNL                 Hong Kong-HKD                Hungary-HUF                  Iceland-ISK               India-INR\n")
        print("Indonesia-IDR                Iran-IRR                     Iraq-IQD                  Ireland-EUR                  Isle of Man-GBP              Israel-ILS                   Italy-EUR                 Ivory Coast-XOF\n")
        print("Jamaica-JMD                  Japan-JPY                    Jersey-GBP                Jordan-JOD                   Kazakhstan-KZT               Kenya-KES                    Kiribati-AUD              Korea-North-KPW\n")
        print("Korea-South-KRW              Kuwait-KWD                   Kyrgyzstan-KGS            Laos-LAK                     Latvia-LVL                   Lebanon-LBP                  Lesotho-LSL               Liberia-LRD\n")
        print("Libya-LYD                    Liechtenstein-CHF            Lithuania-LTL             Luxembourg-EUR               Macau-MOP                    Macedonia-MKD                Madagascar-MGF            Malawi-MWK\n")
        print("Malaysia-MYR                 Maldives-MVR                 Mali-XOF                  Malta-EUR                    Marshall Islands-USD         Martinique (French)-EUR      Mauritania-MRO            Mauritius-MUR\n")
        print("Mayotte-EUR                  Mexico-MXN                   Micronesia-USD            Moldova-MDL                  Monaco-EUR                   Mongolia-MNT                 Montenegro-EUR            Montserrat-XCD\n")
        print("Morocco-MAD                  Mozambique-MZN               Myanmar-MMK               Namibia-NAD                  Nauru-AUD                    Nepal-NPR                    Netherlands-EUR           Netherlands Antilles-ANG\n")
        print("New Caledonia (French)-XPF   New Zealand-NZD              Nicaragua-NIO             Niger-XOF                    Nigeria-NGN                  Niue-NZD                     Norfolk Island-AUD        Northern Mariana Islands-USD\n")
        print("Norway-NOK                   Oman-OMR                     Pakistan-PKR              Palau-USD                    Panama-PAB                   Papua New Guinea-PGK         Paraguay-PYG              Peru-PEN\n")
        print("Philippines-PHP              Pitcairn Island-NZD          Poland-PLN                Polynesia (French)-XPF       Portugal-EUR                 Puerto Rico-USD              Qatar-QAR                 Reunion (French)-EUR\n")
        print("Romania-RON                  Russia-RUB                   Rwanda-RWF                Saint Helena-SHP             Saint Kitts & Nevis Anguilla-XCD                          Saint Lucia-XCD           Saint Pierre and Miquelon-EUR\n")
        print("Saint Vincent & Grenadines-XCD                            Samoa-WST                 San Marino-EUR               Sao Tome and Principe-STD    Saudi Arabia-SAR             Senegal-XOF               Serbia-RS\n")
        print("Seychelles-SCR               Sierra Leone-SLL             Singapore-SGD             Slovakia-EUR                 Slovenia-EUR                 Solomon Islands-SBD          Somalia-SOS               South Africa-ZAR\n")
        print("South Georgia & South Sandwich Islands-GBP                South Sudan-SSP           Spain-EUR                    Sri Lanka-LKR                Sudan-SDG                    Suriname-SRD              Svalbard and Jan Mayen Islands-NOK\n")
        print("Swaziland-SZL                Sweden-SEK                   Switzerland-CHF           Syria-SYP                    Taiwan-TWD                   Tajikistan-TJS               Tanzania-TZS              Thailand-THB\n")
        print("Togo-XOF                     Tokelau-NZD                  Tonga-TOP                 Trinidad and Tobago-TTD      Tunisia-TND                  Turkey-TRY                   Turkmenistan-TMT          Turks and Caicos Islands-USD\n")
        print("Tuvalu-AUD                   U.K.-GBP                     USA-USD                   USA Minor Outlying Islands-USD                            Uganda-UGX                   Ukraine-UAH               United Arab Emirates-AED\n")
        print("Uruguay-UYU                  Uzbekistan-UZS               Vanuatu-VUV               Vatican-EUR                  Venezuela-VEF                Vietnam-VND                  Virgin Islands (British)-USD Virgin Islands (USA)-USD\n")
        print("Wallis & Futuna Islands-XPF  Western Sahara-MAD           Yemen-YER                 Zambia-ZMW                   Zimbabwe-ZWD"+'\033[0m')
        if input("Enter 99 to covert the currency:")=='99':
            Conveter.get_data()
    
    def currency_convert():
        global quantity,initial,to
        print(quantity,initial,to)
        url = "https://currency-exchange.p.rapidapi.com/exchange"
        querystring = {"q":quantity,"from":initial,"to":to}
        headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "789d22491amsh9cf6fe5ac3b3cf8p195e80jsn0b807e6d418c"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
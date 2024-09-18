#Variables to use within questions

'''
Basic Q1
'''
sales_transactions = [
    {
        "transaction_id": "T001",
        "date": "2024-09-01",
        "customer_id": "C1001",
        "product_id": "P2001",
        "quantity": 2,
        "unit_price": 20.00,
        "payment_method": "Credit Card"
    },
    {
        "transaction_id": "T002",
        "date": "2024-09-02",
        "customer_id": "C1002",
        "product_id": "P2001",
        "quantity": 1,
        "unit_price": 20.00,
        "payment_method": "PayPal"
    },
    {
        "transaction_id": "T003",
        "date": "2024-09-03",
        "customer_id": "C1003",
        "product_id": "P2002",
        "quantity": 3,
        "unit_price": 15.00,
        "payment_method": "Debit Card"
    },
    {
        "transaction_id": "T004",
        "date": "2024-09-04",
        "customer_id": "C1004",
        "product_id": "P2003",
        "quantity": 1,
        "unit_price": 120.00,
        "payment_method": "Cash"
    },
    {
        "transaction_id": "T005",
        "date": "2024-09-05",
        "customer_id": "C1005",
        "product_id": "P2001",
        "quantity": 4,
        "unit_price": 20.00,
        "payment_method": "Credit Card"
    },
    {
        "transaction_id": "T006",
        "date": "2024-09-06",
        "customer_id": "C1006",
        "product_id": "P2004",
        "quantity": 2,
        "unit_price": 30.00,
        "payment_method": "Credit Card"
    },
    {
        "transaction_id": "T007",
        "date": "2024-09-07",
        "customer_id": "C1007",
        "product_id": "P2005",
        "quantity": 5,
        "unit_price": 8.00,
        "payment_method": "PayPal"
    },
    {
        "transaction_id": "T008",
        "date": "2024-09-08",
        "customer_id": "C1008",
        "product_id": "P2002",
        "quantity": 2,
        "unit_price": 15.00,
        "payment_method": "Debit Card"
    }
]



'''
Sustianability Q1
'''
cities_energy_usage = [{'city': 'London', 'energy_usage_GWh': 6500}, {'city': 'Edinburgh', 'energy_usage_GWh': 800}, {'city': 'Glasgow', 'energy_usage_GWh': 900}, {'city': 'Birmingham', 'energy_usage_GWh': 700}, {'city': 'Manchester', 'energy_usage_GWh': 600}, {'city': 'Berlin', 'energy_usage_GWh': 5500}, {'city': 'Munich', 'energy_usage_GWh': 4000}, {'city': 'Dusseldorf', 'energy_usage_GWh': 2300}, {'city': 'Dortmund', 'energy_usage_GWh': 2200}, {'city': 'Paris', 'energy_usage_GWh': 5000}, {'city': 'Marseille', 'energy_usage_GWh': 1800}, {'city': 'Lyon', 'energy_usage_GWh': 1600}, {'city': 'Madrid', 'energy_usage_GWh': 4500}, {'city': 'Barcelona', 'energy_usage_GWh': 3500}, {'city': 'Valencia', 'energy_usage_GWh': 2500}, {'city': 'Seville', 'energy_usage_GWh': 2200}, {'city': 'Rome', 'energy_usage_GWh': 4200}, {'city': 'Milan', 'energy_usage_GWh': 3200}, {'city': 'Naples', 'energy_usage_GWh': 2700}, {'city': 'Turin', 'energy_usage_GWh': 2400}, {'city': 'Florence', 'energy_usage_GWh': 2000}, {'city': 'Amsterdam', 'energy_usage_GWh': 3700}, {'city': 'Rotterdam', 'energy_usage_GWh': 2900}, {'city': 'Brussels', 'energy_usage_GWh': 3600}, {'city': 'Antwerp', 'energy_usage_GWh': 2400}, {'city': 'Ghent', 'energy_usage_GWh': 2100}, {'city': 'Bruges', 'energy_usage_GWh': 1700}, {'city': 'Liege', 'energy_usage_GWh': 1500}, {'city': 'Warsaw', 'energy_usage_GWh': 3400}, {'city': 'Krakow', 'energy_usage_GWh': 2800}, {'city': 'Poznan', 'energy_usage_GWh': 1800}, {'city': 'Budapest', 'energy_usage_GWh': 3200}, {'city': 'Debrecen', 'energy_usage_GWh': 1500}, {'city': 'Szeged', 'energy_usage_GWh': 1300}, {'city': 'Pecs', 'energy_usage_GWh': 1100}, {'city': 'Plzen', 'energy_usage_GWh': 2000}, {'city': 'Prague', 'energy_usage_GWh': 3100}, {'city': 'Liberec', 'energy_usage_GWh': 1700}, {'city': 'Copenhagen', 'energy_usage_GWh': 3000}, {'city': 'Aalborg', 'energy_usage_GWh': 1300}, {'city': 'Esbjerg', 'energy_usage_GWh': 1100}, {'city': 'Stockholm', 'energy_usage_GWh': 2900}, {'city': 'Gothenburg', 'energy_usage_GWh': 2200}, {'city': 'Vasteras', 'energy_usage_GWh': 1500}, {'city': 'Oslo', 'energy_usage_GWh': 2800}, {'city': 'Bergen', 'energy_usage_GWh': 2000}, {'city': 'Drammen', 'energy_usage_GWh': 1400}, {'city': 'Helsinki', 'energy_usage_GWh': 2700}, {'city': 'Espoo', 'energy_usage_GWh': 1500}, {'city': 'Tampere', 'energy_usage_GWh': 1300}, {'city': 'Vantaa', 'energy_usage_GWh': 1000}, {'city': 'Lisbon', 'energy_usage_GWh': 2600}, {'city': 'Porto', 'energy_usage_GWh': 2000}, {'city': 'Athens', 'energy_usage_GWh': 2500}, {'city': 'Thessaloniki', 'energy_usage_GWh': 1800}, {'city': 'Patras', 'energy_usage_GWh': 1400}, {'city': 'Heraklion', 'energy_usage_GWh': 1200}, {'city': 'Larissa', 'energy_usage_GWh': 1100}, {'city': 'Dublin', 'energy_usage_GWh': 2400}, {'city': 'Cork', 'energy_usage_GWh': 1500}, {'city': 'Galway', 'energy_usage_GWh': 1300}, {'city': 'Zurich', 'energy_usage_GWh': 2100}, {'city': 'Geneva', 'energy_usage_GWh': 2000}, {'city': 'Basel', 'energy_usage_GWh': 1800}, {'city': 'Bern', 'energy_usage_GWh': 1600}, {'city': 'Belgrade', 'energy_usage_GWh': 2200}, {'city': 'Novi Sad', 'energy_usage_GWh': 1800}, {'city': 'Nis', 'energy_usage_GWh': 1500}, {'city': 'Sarajevo', 'energy_usage_GWh': 2000}, {'city': 'Banja Luka', 'energy_usage_GWh': 1500}, {'city': 'Mostar', 'energy_usage_GWh': 1000}, {'city': 'Zagreb', 'energy_usage_GWh': 2300}, {'city': 'Split', 'energy_usage_GWh': 1800}, {'city': 'Ljubljana', 'energy_usage_GWh': 2000}, {'city': 'Maribor', 'energy_usage_GWh': 1500}, {'city': 'Celje', 'energy_usage_GWh': 1300}, {'city': 'Tallinn', 'energy_usage_GWh': 600}, {'city': 'Tartu', 'energy_usage_GWh': 500}, {'city': 'Kohtla-Jarve', 'energy_usage_GWh': 350}, {'city': 'Parnu', 'energy_usage_GWh': 400}, {'city': 'Riga', 'energy_usage_GWh': 550}, {'city': 'Ventspils', 'energy_usage_GWh': 250}, {'city': 'Daugavpils', 'energy_usage_GWh': 400}, {'city': 'Jelgava', 'energy_usage_GWh': 300}, {'city': 'Vilnius', 'energy_usage_GWh': 500}, {'city': 'Kaunas', 'energy_usage_GWh': 450}, {'city': 'Klaipeda', 'energy_usage_GWh': 400}, {'city': 'Kiev', 'energy_usage_GWh': 4000}, {'city': 'Lviv', 'energy_usage_GWh': 3000}, {'city': 'Minsk', 'energy_usage_GWh': 3500}, {'city': 'Gomel', 'energy_usage_GWh': 2700}, {'city': 'Vitebsk', 'energy_usage_GWh': 2300}, {'city': 'Chisinau', 'energy_usage_GWh': 900}, {'city': 'Balti', 'energy_usage_GWh': 750}, {'city': 'Bender', 'energy_usage_GWh': 700}, {'city': 'Orhei', 'energy_usage_GWh': 600}, {'city': 'Tirana', 'energy_usage_GWh': 1000}, {'city': 'Durres', 'energy_usage_GWh': 800}, {'city': 'Vlore', 'energy_usage_GWh': 600}, {'city': 'Podgorica', 'energy_usage_GWh': 800}, {'city': 'Bijelo Polje', 'energy_usage_GWh': 400}, {'city': 'Berane', 'energy_usage_GWh': 350}, {'city': 'Skopje', 'energy_usage_GWh': 1200}, {'city': 'Bitola', 'energy_usage_GWh': 800}, {'city': 'Stip', 'energy_usage_GWh': 500}, {'city': 'Valletta', 'energy_usage_GWh': 500}, {'city': 'Birkirkara', 'energy_usage_GWh': 450}, {'city': 'Qormi', 'energy_usage_GWh': 300}, {'city': 'Andorra la Vella', 'energy_usage_GWh': 150}, {'city': 'Escaldes-Engordany', 'energy_usage_GWh': 120}, {'city': 'Sant Julia de Loria', 'energy_usage_GWh': 80}, {'city': 'San Marino', 'energy_usage_GWh': 100}, {'city': 'Serravalle', 'energy_usage_GWh': 80}, {'city': 'Borgo Maggiore', 'energy_usage_GWh': 40}, {'city': 'Liechtenstein', 'energy_usage_GWh': 150}, {'city': 'Vaduz', 'energy_usage_GWh': 100}, {'city': 'Balzers', 'energy_usage_GWh': 90}]

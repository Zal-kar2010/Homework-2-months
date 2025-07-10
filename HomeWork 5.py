Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

Geeks.pop('bag')
Geeks['address'] = 'Toktogula 103'
Geeks['phone'] = '0507 052 018'
Geeks['instagram'] = '@geeks_edu'

new_courses = ['Data Science', 'Cyber Security']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])

Geeks['foundation_date'] = '24.05.2000'

print(f"Количество курсов: {len(Geeks['courses'])}")

print("\nСодержимое словаря Geeks:")
for key, value in Geeks.items():
    print(f"{key}: {value}")
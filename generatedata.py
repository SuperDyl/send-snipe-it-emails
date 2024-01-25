from dataclasses import dataclass

from pandas import DataFrame
from random import Random
from datetime import datetime, timedelta

# COUNT = 100
EMPLOYEES = 50
ASSETS = 100

rand = Random(0)  # can use a seed

first_names = [
    'Meryl',
    'Elfreda',
    'Davin',
    'Natividad',
    'Anne',
    'Abeu',
    'Elizabeth',
    'Mirelle',
    'Emilia',
    'Kimble',
    'Fanya',
    'Betta',
    'Viviana',
    'Kinnie',
    'Kath',
    'Paige',
    'Kathi',
    'Lek',
    'Mel',
    'Andonis',
    'Shara',
    'Isahella',
    'Jan',
    'Karilynn',
    'Yolande',
    'Levi',
    'Teddie',
    'Camellia',
    'Ekaterina',
    'Lawry',
    'Maje',
    'Blondelle',
    'Raye',
    'Rodney',
    'Lindie',
    'Flossi',
    'Lionel',
    'Gwennie',
    'Rosamond',
    'Bamby',
    'Nappy',
    'Tresa',
    'Celle',
    'Lishe',
    'Baily',
    'Bellina',
    'Cale',
    'Sutherlan',
    'Spence',
    'Bridie',
]

last_names = [
    'Manuely',
    'Jehaes',
    'Haill',
    'Cordrey',
    'Youtead',
    'Pock',
    'Chancellor',
    'Sutherland',
    'Baiden',
    'Boocock',
    'Ropkes',
    'Woodford',
    'Vedyasov',
    'Dalliston',
    'Danniell',
    'Angless',
    'Nellies',
    'Storres',
    'Godfroy',
    'Klesl',
    'Ropking',
    'Itzak',
    'Birmingham',
    'Tregaskis',
    'Rands',
    'Issatt',
    'Randles',
    'Petruskevich',
    'Stenners',
    'Benasik',
    'Smith',
    'Capewell',
    'Jonke',
    'Jerisch',
    'Ivanonko',
    'Tree',
    'Gemson',
    'McGeown',
    'Quarrington',
    'Colloff',
    'OLoughnan',
    'Betancourt',
    'Mossop',
    'Stitcher',
    'Dignall',
    'Sammes',
    'Braunthal',
    'Cocher',
    'McComb',
    'Sterndale',
]


@dataclass
class Name:
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def create_names(count: int = EMPLOYEES) -> list[Name]:
    return [
        Name(first_name=rand.choice(first_names), last_name=rand.choice(last_names))
        for _ in range(count)
    ]


def create_employees(names: list[Name]) -> DataFrame:
    count = len(names)

    return DataFrame({
        'id': [x for x in range(count)],
        'Company': [rand.choice(('IT', 'Math', 'Science', 'Education', 'Linguistics')) for _ in range(count)],
        'Title': [rand.choice(('Faculty', 'Student', 'Staff', 'Part Time Faculty', 'Editor', 'Adjunct')) for _ in
                  range(count)],
        'Employee Number': [rand.randint(1, 1_000_000) for _ in range(count)],
        'Name': [name.full_name for name in names],
        'Username': [f'{name.first_name[0]}{name.last_name[0]}{rand.randint(0, 99):2}' for name in names],
        'Email': [f'{name.first_name}_{name.last_name}@company.com' for name in names],
        'Manager': [names[rand.randint(0, x)].full_name for x in range(count)],
        'Location': [f'{rand.randint(0, 3) * 100:3}{rand.choice("ABCDEFGH")}' for _ in range(count)],
        'Department': ['' for _ in range(count)],
        'Assets': [rand.randint(0, 10) for _ in range(count)],
        'Licenses': [0 for _ in range(count)],
        'Accessories': [0 for _ in range(count)],
        'Consumables': [0 for _ in range(count)],
        'admin/users/table.groups': [rand.choice(('IT', '', 'No Perms')) for _ in range(count)],
        'Notes': ['' for _ in range(count)],
        'Active': [rand.choice(('Yes', 'No')) for _ in range(count)],
        'Created At': [datetime.now() for _ in range(count)],
    })


@dataclass
class Model:
    name: str
    full_id: str


def create_models(count=ASSETS) -> list[Model]:
    return [
        Model(name=f'{main}{number:3}', full_id=f'{main}{number:3}-{rand.random()}')
        for main, number in
        ((rand.choice(('NoteBook', 'Desktop', 'Printer', 'Tablet')), rand.randint(0, 999)) for _ in range(count))
    ]


def create_assets(assets: int, employees: DataFrame) -> DataFrame:
    models = create_models(assets)
    employee_tuples = [employee for employee in employees.itertuples(index=False)]
    chosen_employees = [rand.choice(employee_tuples) for _ in range(assets)]

    return DataFrame({
        'ID': [f'{rand.randint(0, 10_000):5}' for _ in range(assets)],
        'Company': ['Math' for _ in range(assets)],
        'Asset Name': [f'Math-{10_000 + x}' for x in range(assets)],
        'Asset Tag': [f'{rand.randint(0, 10_000):5}' for _ in range(assets)],
        'Model': [model.name for model in models],
        'Model No.': [model.full_id for model in models],
        'Category': [rand.choice(('Laptop', 'Desktop', 'Printer', 'Tablet', 'Other')) for _ in range(assets)],  #
        'Manufacturer': [rand.choice(('Apple', 'Dell', 'Lenovo', 'HP')) for _ in range(assets)],
        'Serial': ['' for _ in range(assets)],
        'Purchased': ['' for _ in range(assets)],
        'Cost': ['' for _ in range(assets)],
        'EOL': ['' for _ in range(assets)],
        'Order Number': ['' for _ in range(assets)],
        'Supplier': ['' for _ in range(assets)],
        'Location': [employee.Location for employee in chosen_employees],
        'Address1': ['' for _ in range(assets)],
        'Address2': ['' for _ in range(assets)],
        'City1': ['' for _ in range(assets)],
        'State1': ['' for _ in range(assets)],
        'Country1': ['' for _ in range(assets)],
        'Zip1': ['' for _ in range(assets)],
        'Default Location': ['' for _ in range(assets)],
        'Address3': ['' for _ in range(assets)],
        'Address4': ['' for _ in range(assets)],
        'City2': ['' for _ in range(assets)],
        'State2': ['' for _ in range(assets)],
        'Country2': ['' for _ in range(assets)],
        'Zip2': ['' for _ in range(assets)],
        'Checked Out': [employee.Name for employee in chosen_employees],
        'Type': ['' for _ in range(assets)],
        'Username': [employee.Username for employee in chosen_employees],
        'Employee No.': [employee.id for employee in chosen_employees],
        'Manager': [employee.Manager for employee in chosen_employees],
        'Department': [employee.Department for employee in chosen_employees],
        'Title': [employee.Title for employee in chosen_employees],
        'Status': ['' for _ in range(assets)],
        'Warranty': ['' for _ in range(assets)],
        'Warranty Expires': ['' for _ in range(assets)],
        'Current Value': ['' for _ in range(assets)],
        'Diff': ['' for _ in range(assets)],
        'Fully Depreciated': ['' for _ in range(assets)],
        'Checkout Date': ['' for _ in range(assets)],
        'Last Checkin Date': ['' for _ in range(assets)],
        'Expected Checkin Date': ['' for _ in range(assets)],
        'Created At': ['' for _ in range(assets)],
        'Updated at': ['' for _ in range(assets)],
        'Deleted': ['' for _ in range(assets)],
        'Last Audit': [datetime.now() - timedelta(days=(30 * rand.randint(0, 18))) for _ in range(assets)],
        'Next Audit Date': ['' for _ in range(assets)],
        'Notes': ['' for _ in range(assets)],
        'URL': ['' for _ in range(assets)],
        'Screen Size': ['' for _ in range(assets)],
        'RAM': ['' for _ in range(assets)],
        'Internal Storage': ['' for _ in range(assets)],
        'Encryption Capable': ['' for _ in range(assets)],
        'Wired MAC Address': ['' for _ in range(assets)],
        'Wireless MAC Address': ['' for _ in range(assets)],
        'Received from Another Unit (date)': ['' for _ in range(assets)],
        'Sent to Another Unit (date)': ['' for _ in range(assets)],
        'Sent to Surplus (date)': ['' for _ in range(assets)],
        'Owning Department': ['' for _ in range(assets)],
        'Other Disposition (date)': ['' for _ in range(assets)],
        'Date Not Found': ['' for _ in range(assets)],
        'Encryption Enabled': ['' for _ in range(assets)],
        'Hostname': ['' for _ in range(assets)],
        'IP Address': ['' for _ in range(assets)],
        'Class': ['' for _ in range(assets)],
        'Backup Service': ['' for _ in range(assets)],
        'Resolution': ['' for _ in range(assets)],
        'CPU': ['' for _ in range(assets)],
        'GPU': ['' for _ in range(assets)],
        'Touchscreen': ['' for _ in range(assets)],
        'Maintenance ID': ['' for _ in range(assets)],
        'Replacement Date': ['' for _ in range(assets)],
        'Contract Type': ['' for _ in range(assets)],
        'Manufacture Date': ['' for _ in range(assets)],
        'Security': ['' for _ in range(assets)],
        'VM Location': ['' for _ in range(assets)],
        'OS': ['' for _ in range(assets)],
        'Reason for Surplus': ['' for _ in range(assets)],
    })


if __name__ == '__main__':
    names = create_names(EMPLOYEES)
    employees = create_employees(names)
    assets = create_assets(assets=ASSETS, employees=employees)

    employees.to_csv('./employees.csv')
    assets.to_csv('./assets.csv')

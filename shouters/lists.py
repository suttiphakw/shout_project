import requests

def thailand_province():
    response = requests.get('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/')
    if response.status_code == 200:
        response_json = response.json()
        return response_json['data']

date_lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

month_lists = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

year_lists = ['<1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
              '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
              '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
              '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '>2021']

education_lists = ['ต่ำกว่ามัธยมต้น', 'มัธยมต้น', 'มัธยมปลาย', 'ปวช', 'ปวศ', 'ปริญญาตรี', 'ปริญญาโท', 'ปริญญาเอก']

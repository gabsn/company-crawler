# coding: utf-8

import re

LOGO_BASE = 'https://media.licdn.com/mpr/mpr/shrink_200_200'

RE_COMPANY_NAME = re.compile(r'"companyName":"([^"]*)"')
RE_COMPANY_TYPE = re.compile(r'"companyType":"([^"]*)"')
RE_SIZE = re.compile(r'"size":"([^"]*)"')
RE_DESCRIPTION = re.compile(r'"description":"([^"]*)"')
RE_WEBSITE = re.compile(r'"website":"([^"]*)"')
RE_SQUARE_LOGO = re.compile(r'"squareLogo":"([^"]*)"')
RE_INDUSTRY = re.compile(r'"industry":"([^"]*)"')
RE_YEAR_FOUNDED = re.compile(r'"yearFounded":(\d+),')
RE_HEADQUARTERS = re.compile(r'"headquarters":({[^}]*})')
RE_SPECIALTIES = re.compile(r'"specialties":(\[[^\]]*\])')
RE_JOB_COUNT = re.compile(r'"jobCount":(\d+),')
RE_EMPLOYEE_COUNT = re.compile(r'"employeeCount":(\d+),')

def extract(item, raw_data):
    m_company_name = RE_COMPANY_NAME.search(raw_data)
    if m_company_name:
        item['company_name'] = m_company_name.group(1)

    m_company_type = RE_COMPANY_TYPE.search(raw_data)
    if m_company_type:
        item['company_type'] = m_company_type.group(1)
    
    m_size = RE_SIZE.search(raw_data)
    if m_size:
        item['size'] = m_size.group(1)

    m_description = RE_DESCRIPTION.search(raw_data)
    if m_description:
        description = m_description.group(1)
        item['description'] = description.replace('\\n', ' ').replace('\\r', ' ')

    m_industry = RE_INDUSTRY.search(raw_data)
    if m_industry:
        item['industry'] = m_industry.group(1)
    
    m_year_founded = RE_YEAR_FOUNDED.search(raw_data)
    if m_year_founded:
        item['year_founded'] = m_year_founded.group(1)

    m_headquarters = RE_HEADQUARTERS.search(raw_data)
    if m_headquarters:
        item['headquarters'] = m_headquarters.group(1)
    
    m_specialties = RE_SPECIALTIES.search(raw_data)
    if m_specialties:
        item['specialties'] = m_specialties.group(1)

    m_website = RE_WEBSITE.search(raw_data)
    if m_website:
        item['website'] = m_website.group(1)
    
    m_square_logo = RE_SQUARE_LOGO.search(raw_data)
    if m_square_logo:
        item['square_logo'] = LOGO_BASE + m_square_logo.group(1)
    
    m_job_count = RE_JOB_COUNT.search(raw_data)
    if m_job_count:
        item['job_count'] = m_job_count.group(1)

    m_employee_count = RE_EMPLOYEE_COUNT.search(raw_data)
    if m_employee_count:
        item['employee_count'] = m_employee_count.group(1)

    return item

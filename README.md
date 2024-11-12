# Invoice Manager

---
### Setup

* `git clone https://github.com/ankitsmt211/Invoice-manager.git`

* create virtual environment `python3 -m venv venv`
* Active virtual environment `source venv/bin/activate`
* run command `pip install -r requirement.txt`
* run migration `python3 manage.py migrate`
* Start Application `python manage.py runserver`

---
### API
`http://localhost:8000/invoices/` (verify port)

Note: will be used both for create/update operation with payload in same format
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_ADMIN = 0
ROLE_MANAGER = 1
ROLE_DOCTOR = 2
ROLE_NURSE = 3
STATUS_REGISTRATION = 0
STATUS_TRIAGE = 1
STATUS_DOCTOR = 2
STATUS_PARMACY = 3
STATUS_HOLD = 4
STATUS_COMPLETE = 5


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	pwhash = db.Column(db.String(128))
	role = db.Column(db.SmallInteger, default = 3) # 0 = admin, 1 = manager, 2 = doctor, 3 = nurse

	def __init__(self, id, username, password, role):
		self.id = id
		self.username = username
		self.pwhash = generate_password_hash(password)
		self.role = role

	def check_password_hash(self, password):
		return check_password_hash(self.pwhash, password)

	def __repr__(self):
		return '<User %r>' % self.username

class Test_Patient(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	## Demographic Info ##
	last_name = db.Column(db.String(255))
	first_name = db.Column(db.String(255))
	age = db.Column(db.SmallInteger, default = 0)
	gender = db.Column(db.SmallInteger, default = 0)  # 0 = male, 1 = female


# class Patient(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)

# 	## Demographic Info ##
# 	last_name = db.Column(db.String(255))
# 	first_name = db.Column(db.String(255))
# 	age = db.Column(db.SmallInteger, default = 0)
# 	birth_date = db.Column(db.Date) # attribues: year, month, and day
# 	gender = db.Column(db.SmallInteger, default = 0)  # 0 = male, 1 = female
# 	children_count = db.Column(db.SmallInteger, default=0)
# 	address = db.Column(db.String(255))
# 	phone = db.Column(db.String(255))
# 	occupation = db.Column(db.String(255))
# 	mother_name = db.Column(db.String(255))
# 	guardian = db.Column(db.String(255))
# 	relation = db.Column(db.String(255))
# 	# PHOTO CAPTURE?

# 	## Background ##
# 	ht = db.Column(db.Boolean)
# 	diabetes = db.Column(db.Boolean)
# 	asthma = db.Column(db.Boolean)
# 	epilepsy = db.Column(db.Boolean)
# 	tb = db.Column(db.Boolean)
# 	sickle_cell = db.Column(db.Boolean)
# 	 # for the habits fields, a list of checkboxes are shown that yield boolean values
# 	tea = db.Column(db.Boolean) 
# 	coffee = db.Column(db.Boolean)
# 	alcohol = db.Column(db.Boolean)
# 	drugs = db.Column(db.Boolean)
# 	drugs_notes = db.Column(db.Text)
# 	period_age_start = db.Column(db.SmallInteger)
# 	period_last_date = db.Column(db.Date) # attribues: year, month, and day
# 	allergies = db.Column(db.Text)
# 	immunizations = db.Column(db.Text)
# 	surgeries = db.Column(db.Text)
# 	family_history = db.Column(db.Text)
# 	patient_notes = db.Column(db.Text)

# 	## Relationships ##
# 	payments = db.relationship('Payment', backref='patient', lazy='dynamic')
# 	pharmacy = db.relationship('Pharmacy', backref='patient', lazy='dynamic')
# 	visit = db.relationship('Visit', backref='patient', lazy='dynamic')
# 	status = db.relationship('Status', backref='patient', lazy='dynamic')

# 	## Flags ##
# 	# FUTURE STATE

# 	def __init__(self, last_name, first_name, age, birth_date, gender, children_count, \
# 		address, phone, occupation, mother_name, guardian, relation, ht, diabetes, asthma, \
# 		epilepsy, tb, sickle_cell, tea, coffee, alcohol, drugs, drugs_notes, period_age_start, \
# 		period_last_date, allergies, imunizations, surgeries, family_history, notes, payments, \
# 		pharmacy, visit, status):
# 		self.last_name = last_name
# 		self.first_name = first_name
# 		self.age = age
# 		self.birth_date = birth_date
# 		self.gender = gender
# 		self.children_count = children_count
# 		self.address = address
# 		self.phone = phone
# 		self.occupation = occupation
# 		self.mother_name = mother_name
# 		self.guardian = guardian
# 		self.relation = relation
# 		self.ht = ht
# 		self.diabetes = diabetes
# 		self.asthma = asthma
# 		self.epilepsy = epilepsy
# 		self.tb = tb
# 		self.sickle_cell = sickle_cell
# 		self.tea = tea
# 		self.coffee = coffee
# 		self.alcohol = alcohol
# 		self.drugs = drugs
# 		self.drugs_notes = drugs_notes
# 		self.period_age_start = period_age_start
# 		self.period_last_date = period_last_date
# 		self.allergies = allergies
# 		self.immunizations = imunizations
# 		self.surgeries = surgeries
# 		self.family_history = family_history
# 		self.notes = notes
# 		self.payments = payments
# 		self.pharmacy = pharmacy
# 		self.visit = visit
# 		self.status = status

# 	def __repr__(self):
# 		return '<Patient %r>' % self.id



# class Visit(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	timestamp = db.Column(db.Date) # attribues: year, month, and day
# 	patient_number = db.Column(db.SmallInteger) # number given to the patient at their time of visit

# 	## Vitals ##
# 	weight = db.Column(db.Float())
# 	height = db.Column(db.Float())
# 	bp_systolic = db.Column(db.SmallInteger())
# 	bp_diastolic = db.Column(db.SmallInteger())
# 	pulse = db.Column(db.SmallInteger())
# 	temperature = db.Column(db.Float())
# 	respirations = db.Column(db.Float())

# 	## Exam ##
# 	complaint = db.Column(db.Text())
# 	history = db.Column(db.Text())
# 	exam = db.Column(db.Text())
# 	diagnosis = db.Column(db.Text())
# 	treatment_1 = db.Column(db.String(255))
# 	treatment_2 = db.Column(db.String(255))
# 	treatment_3 = db.Column(db.String(255))
# 	treatment_4 = db.Column(db.String(255))
# 	treatment_5 = db.Column(db.String(255))
# 	treatment_6 = db.Column(db.String(255))
# 	follow_up = db.Column(db.Text())
# 	exam_notes = db.Column(db.Text())
# 	prescrip_given = db.Column(db.Boolean())
# 	prescrip_descrip = db.Column(db.Text())

# 	## Relationships ##
# 	patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
# 	payment = db.relationship('Payment', uselist = False, backref = 'visit', lazy='dynamic')
# 	pharmacy = db.relationship('Pharmacy', uselist = False, backref = 'visit', lazy='dynamic')
# 	# INSERT user_patient_interactions CONNECTION

# 	def __init__(self, timestamp, patient_number, weight, height, bp_systolic, bp_diastolic, \
# 		pulse, temperature, respirations, complaint, history, exam, diagnosis, treatment1, \
# 		treatment2, treatment3, treatment4, treatment5, treatment6, follow_up, exam_notes, \
# 		prescription_given, prescription_description, patient_id, payment, pharmacy):
# 		self.timestamp = timestamp
# 		self.patient_number = patient_number
# 		self.weight = weight
# 		self.height = height
# 		self.bp_systolic = bp_systolic
# 		self.bp_diastolic = bp_diastolic
# 		self.pulse = pulse
# 		self.temperature = temperature
# 		self.respirations = respirations
# 		self.complaint = complaint
# 		self.history = history
# 		self.exam = exam
# 		self.diagnosis = diagnosis
# 		self.treatment1 = treatment1
# 		self.treatment2 = treatment2
# 		self.treatment3 = treatment3
# 		self.treatment4 = treatment4
# 		self.treatment5 = treatment5
# 		self.treatment6 = treatment6
# 		self.follow_up = follow_up
# 		self.exam_notes = exam_notes
# 		self.prescription_given = prescription_given
# 		self.prescription_description = prescription_description
# 		self.patient_id = patient_id
# 		self.payment = payment
# 		self.pharmacy = pharmacy

# 	def __repr__(self):
# 		return '<Visit %r>' % self.id



# class Pharmacy(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	medication_given = db.Column(db.String(255))
# 	amount_given = db.Column(db.String(255))
# 	pharmacy_notes = db.Column(db.Text())
	
# 	## Relationships ##
# 	patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
# 	visit_id = db.Column(db.Integer, db.ForeignKey('visit.id'))
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# 	def __init__(self, medication_given, amount_given, pharmacy_notes, patient_id, visit_id, user_id):
# 		self.medication_given = medication_given
# 		self.amount_given = amount_given
# 		self.pharmacy_notes = pharmacy_notes
# 		self.patient_id = patient_id
# 		self.visit_id = visit_id
# 		self.user_id = user_id

# 	def __repr__(self):
# 		return '<Pharmacy %r>' % self.id



# class Payment(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	payment_type = db.Column(db.SmallInteger()) # 0 = $, 1 = pass, 2 = other
# 	payment_amount = db.Column(db.Float())
# 	payment_other = db.Column(db.String(255))
	
# 	## Relationships##
# 	patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
# 	visit_id = db.Column(db.Integer, db.ForeignKey('visit.id'))
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 	def __init__(self, payment_type, payment_amount, payment_other, patient_id, visit_id, user_id):
# 		self.payment_type = payment_type
# 		self.payment_amount = payment_amount
# 		self.payment_other = payment_other
# 		self.patient_id = patient_id
# 		self.visit_id = visit_id
# 		self.user_id = user_id

# 	def __repr__(self):
# 		return '<Payment %r>' % self.id



# class Status(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
	
# 	## Current Status in Clinic ##
# 	status = db.Column(db.SmallInteger())
# 	status_change_timestamp = db.Column(db.DateTime) # at what time/date did the patient change status?
# 	patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

# 	def __init__(self, status, status_change_timestamp, patient_id):
# 		self.status = status
# 		self.status_change_timestamp = status_change_timestamp
# 		self.patient_id = patient_id

# 	def __repr__(self):
# 		return '<Status %r>' % self.id


#class User_Log(db.Model):
#	id = db.Column(db.Integer, primary_key=True)

	# UserID
	# Patient_ID
	# VisitID
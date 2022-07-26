from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,NumberRange



class addproduct(FlaskForm):
    prodname = StringField('Product Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    proddept = IntegerField('Depletes', validators=[NumberRange(min=1, max=2),DataRequired()])
    prodsubmit = SubmitField('Save Changes')

class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    edittqty = IntegerField('Total Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    # editqty = IntegerField('Unallocated Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    editsubmit = SubmitField('Save Changes')

class addlocation(FlaskForm):
    locname = StringField('Person Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save Changes')

class editlocation(FlaskForm):
    editlocname = StringField('Person Name', validators=[DataRequired()])
    editlocsubmit = SubmitField('Save Changes')

class moveproduct(FlaskForm):
    mprodname = SelectField(
        'Product Name')
    src = SelectField(
        'Source')
    destination = SelectField(
        'Destination')
    mprodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    movesubmit = SubmitField('Move')

class productdepletion(FlaskForm):
    dprodname = SelectField(
        'Product Name')
    dsrc = SelectField(
        'Source')
    dprodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    deptsubmit = SubmitField('Done')

class expensesform(FlaskForm):
    eperson = StringField('Name', validators=[DataRequired()])
    eplace = StringField('Place', validators=[DataRequired()])
    ecost = IntegerField('Cost', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    equantity = IntegerField('Quantity')
    esubmit = SubmitField('Record')

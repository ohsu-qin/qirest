from nose.tools import (assert_true, assert_false, assert_equal, assert_raises)
from datetime import datetime
import pytz
from mongoengine import (connect, ValidationError)
from mongoengine.connection import get_db
from qiprofile_rest.models import *

class TestModel(object):
    def setup(self):
        connect(db='qiprofile_test')
        self.db = get_db()
    
    def tearDown(self):
        for collection in self.db.collection_names():
            if not collection.startswith('system.'):
                self.db.drop_collection(collection)

    def test_subject(self):
        subject = Subject(number=1)
        assert_equal(subject.project, 'QIN',
                     "Subject project is not set to the default -"
                     " expected %s, found %s" % ('QIN', subject.project))
        
        # The subject must have a collection.
        with assert_raises(ValidationError):
            subject.save()
        
        subject.collection='Breast'
        subject.save()

    def test_race(self):
        detail = SubjectDetail(collection='Breast', number=1)
        detail.races = ['White', 'Black', 'Asian', 'AIAN', 'NHOPI']
        detail.save()

        detail = SubjectDetail(collection='Breast', number=1)
        detail.races = ['Invalid']
        with assert_raises(ValidationError):
            detail.save()

        # Races must be a list.
        detail.races = 'White'
        with assert_raises(ValidationError):
            detail.save()

    def test_ethnicity(self):
        detail = SubjectDetail(collection='Breast', number=1)
        detail.ethnicity = 'Non-Hispanic'
        detail.save()

        detail.ethnicity = 'Invalid'
        with assert_raises(ValidationError):
            detail.save()

    def test_encounter(self):
        detail = SubjectDetail(collection='Breast', number=1)
        date = datetime(2013, 1, 4, tzinfo=pytz.utc)
        encounter = Encounter(encounter_type='Biopsy', date=date)
        detail.encounters = [encounter]
        # The encounter must have an outcome.
        with assert_raises(ValidationError):
            detail.save()
        
        # Add the outcome.
        outcome = TNM()
        encounter.outcomes = [outcome]
        # The detail is now valid.
        detail.save()

    def test_tnm_size(self):
       field = TNM.SizeField()
       for value in ['T1', 'Tx', 'cT4', 'T1b', 'cT2a']:
           assert_true(field.validate(value),
                       "Valid TNM size value not validated: %s" % value)
       for value in ['Tz', 'T', '4', 'cT4d']:
           assert_false(field.validate(value),
                        "Invalid TNM size value was validated: %s" % value)

    def test_session(self):
        detail = SubjectDetail(collection='Breast', number=1)
        date = datetime(2013, 1, 4, tzinfo=pytz.utc)
        modeling = Modeling(name='pk_test', image_container_name='scan')
        session = Session(number=1, acquisition_date=date, modeling=[modeling])
        detail.sessions = [session]
        detail.save()
        
        # Modeling must have an image container name.
        bad_modeling = Modeling(name='pk_test')
        session.modeling.append(bad_modeling)
        with assert_raises(ValidationError):
            detail.save()

    def test_series(self):
        detail = SessionDetail()
        detail.bolus_arrival_index = 4
        # The bolus arrival index must refer to a series.
        with assert_raises(ValidationError):
            detail.save()
        
        # Add the series.
        detail.series = [Series(number=7+i) for i in range(0, 32)]
        # The detail is now valid.
        detail.save()

        # The bolus arrival index does not refer to a series.
        detail.bolus_arrival_index = 32
        with assert_raises(ValidationError):
            detail.save()

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
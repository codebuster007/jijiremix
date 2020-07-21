from django.test import TestCase
from accounts.models import ORMUser
from ..models import ORMBuyer, ORMItem

class ItemModelTest(TestCase):

    def setUp(self):
        self.__create_user_dummy_data()
    
    def test_create_item_data(self):
        for y in range(1, 5):
            email = "firstn{}@gmail.com".format(y)
            owner = ORMUser.objects.get(email=email)
            n = str(y)
            item = ORMItem.objects.create(owner=owner, name='item' + n,
                                   description='clean and portable item' + n,
                                   price=35000.00 + y)
            
            self.assertEqual(item.owner, owner)
            self.assertEqual(item.name, 'item' + n)
            self.assertEqual(item.description, 'clean and portable item' + n)
            self.assertEqual(item.price, 35000.00 + y)
            self.assertFalse(item.is_sold)
            self.assertIsNone(item.sold_to)
    
    def test_sold_to_not_none_after_selling(self):
        y = 1
        email = "firstn{}@gmail.com".format(y)
        owner = ORMUser.objects.get(email=email)
        n = str(y)
        item = ORMItem.objects.create(owner=owner, name='item' + n,
                                   description='clean and portable item' + n,
                                   price=35000.00 + y)

        self.assertIsNone(item.sold_to)

        buyer = ORMBuyer.objects.create(item=item, name='buyer1',
                                        email='buyer1@hotmail.com',
                                        location='lagos')
        item = ORMItem.objects.get(item_id=item.item_id)
        item.sold_to = buyer
        item.save()

        self.assertIsNotNone(item.sold_to)

    def __create_user_dummy_data(self):
        for x in range(1, 5):
            n = str(x)
            extra_fields = {
            'first_name': 'firstn' + n,
            'last_name': 'lastn' + n,
            'residence_state': 'state' + n,
            }
            email = "{}@gmail.com".format(extra_fields['first_name'])
            ORMUser.objects.create_user(
                email=email, password='foo',
                **extra_fields
            )

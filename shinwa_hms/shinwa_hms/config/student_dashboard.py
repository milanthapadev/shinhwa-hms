def get_data(data=None):
    return {
        'fieldname': 'student',  # The link field in Student Invoice and Payment
        'transactions': [
            {
                'label': 'Finance',
                'items': ['Student Invoice', 'Payment']
            }
        ]
    }

from setuptools import setup

if __name__ == '__main__':
    setup(

        exclude_package_data = {'user_profile':
        [
            'Users/james.py'
        ]
        }

    )
# Concept: Class Methods and Static Methods
# - @classmethod takes 'cls' and is used to modify class-level variables that affect all instances.
# - @staticmethod takes neither 'self' nor 'cls'. It is a standalone utility function housed inside the class for logical organization.


class Startup:
    funding_round="Series A"
    @classmethod
    def upgrade_funding(cls,new_round):
        cls.funding_round=new_round

    @staticmethod
    def calculate_tax(revenue):
        return revenue*0.20
    
Startup.upgrade_funding("Series B")
print(Startup.funding_round)
print(Startup.calculate_tax(100000))


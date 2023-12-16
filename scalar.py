# Scalar types  such as String, Int, Float, Boolean and ID
import graphene

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
    height = graphene.Float()
    is_student = graphene.Boolean()
    id = graphene.ID()

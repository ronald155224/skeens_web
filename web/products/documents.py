from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from products.models import Product, ProductCategory, ProductImage

# The name of your index
product = Index('products')
# See Elasticsearch Indices API reference for available settings
product.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
        'name_en': fields.TextField(),
        'description': fields.TextField(),
        'description_en': fields.TextField(),
        'created': fields.DateField(),
        'modified': fields.DateField(),
        'image': fields.FileField(),
    })

    product_image_set = fields.NestedField(properties={
        'name': fields.TextField(),
        'image': fields.FileField(),
        'order': fields.IntegerField(),
    })

    class Django:
        model = Product
        # we removed the type field from here
        fields = [
            'id',   # add id field
            'name',
            'description',
            'price',
            'created',
            'modified',
        ]

    class Index:
        name = "product"

@registry.register_document
class ProductCategoryDocument(Document):

    class Django:
        model = ProductCategory
        fields = [
            'id',  # add id field
            'name',
            'name_en',
            'description',
            'description_en',
            'created',
            'modified',
            'image'
        ]

    class Index:
        name = "productcategory"

@registry.register_document
class ProductImageDocument(Document):

    class Django:
        model = ProductImage
        fields = [
            'id',
            'name',
            'image',
            'order'
        ]

    class Index:
        name = "productimage"  
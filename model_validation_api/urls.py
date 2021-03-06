from django.conf.urls import url
from .views import (ValidationTestDefinitionResource,
                    ValidationTestDefinitionListResource,
                    ValidationTestDefinitionSearchResource,
                    ValidationTestResultResource,
                    ValidationTestResultListResource,
                    ScientificModelResource,
                    ScientificModelListResource,
                    SimpleTestListView,
                    SimpleTestDetailView,
                    ValidationTestDefinitionCreate,
                    SimpleModelListView,
                    SimpleModelDetailView,
                    SimpleResultListView,
                    SimpleResultDetailView,
                    )

uuid_pattern = "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
# simplified from http://stackoverflow.com/questions/11384589/what-is-the-correct-regex-for-matching-values-generated-by-uuid-uuid4-hex
# will accept some patterns that are not strictly UUID v4

urlpatterns = (
    url(r'^tests/$',
        ValidationTestDefinitionListResource.as_view(),
        name="list-resource"),
    url(r'^tests/(?P<test_id>\d+)$',
        ValidationTestDefinitionResource.as_view(),
        name="item-resource"),
    url(r'^search',
        ValidationTestDefinitionSearchResource.as_view(),
        name="search-resource"),
    url(r'^results/$',
        ValidationTestResultListResource.as_view(),
        name="result-list-resource"),
    url(r'^results/(?P<result_id>\d+)$',
        ValidationTestResultResource.as_view(),
        name="result-item-resource"),
    url(r'^models/$',
        ScientificModelListResource.as_view(),
        name="model-list-resource"),
    url(r'^models/(?P<model_id>{})$'.format(uuid_pattern),
        ScientificModelResource.as_view(),
        name="model-item-resource"),


    url(r'^view/tests/$',
        SimpleTestListView.as_view(),
        name="simple-list-view"),
    url(r'^view/tests/(?P<pk>\d+)$',
        SimpleTestDetailView.as_view(),
        name="simple-detail-view"),
    url(r'^view/tests/create$',
        ValidationTestDefinitionCreate.as_view(),
        name="create-test-view"),



    url(r'^view/models/$',
        SimpleModelListView.as_view(),
        name="simple-model-list-view"),
    url(r'^view/models/(?P<pk>{})$'.format(uuid_pattern),
        SimpleModelDetailView.as_view(),
        name="simple-model-detail-view"),

    url(r'^view/results/$',
        SimpleResultListView.as_view(),
        name="simple-result-list-view"),
    url(r'^view/results/(?P<pk>\d+)$',
        SimpleResultDetailView.as_view(),
        name="simple-result-detail-view"),

    
)
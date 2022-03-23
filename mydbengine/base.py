from django.db.backends.postgresql import base, features

class DatabaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True

class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures
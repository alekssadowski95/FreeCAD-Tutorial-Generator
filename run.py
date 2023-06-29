import FreeCAD
import FreeCADGui


class ManualGenerator():
    def __init__(self, body, context = {}, model = 'standard') -> None:
        if body is None:
            return 0
        self.body = body
        self.context = context
        self.model = model
        if self.model == 'standard':
            self.model_url = 'models/standard.json'
    
    def get_body_features(self):
        pass

    def get_feature_snippet(self, feature_class_str):
        pass

    def get_topic_intro(self):
        pass

    def get_steps_intro(self):
        pass

    def get_steps_outro(self):
        pass

    def get_success(self):
        pass

    def get_next(self):
        pass
    
    def generate_html_str(self) -> str:
        pass

    def save_html(self) -> None:
        pass

if __name__ == '__main__':
    pass
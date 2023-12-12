general_text = {
    'title': 'Teil in FreeCAD Part Design entwerfen',
    'topic_intro': 'In dieser Anleitung werden wir ein Teil mit FreeCAD entwerfen. Das Teil wird in einem Produkt verwendet und hat die Funktion etwas zu tun. Das Produkt wird in der Industrie verwendet um etwas zu tun. Das Teil aus dieser Anleitung wird mittels eines Verfahrens hergestellt.',
    'steps_intro': 'In mehreren Schritten werden wir einige Part Design Features und Skizzen verwenden. Lasst uns mit dem ersten Schritt beginnen:',
    'success': 'Glückwunsch, du hast es geschafft!',
    'summary': 'In dieser Anleitung haben wir die Part Design Features und Skizzen angewendet.',
    'next': 'Als Nächstes entwerfe die anderen Teile des Produktes.',
    'ad_upsell': 'Mache eine Schulung um zu lernen, wie du FreeCAD in einer industriellen Umgebung zuverlässig anwenden kannst. Die FreeCAD Schulung zeigt dir, wie du mit FreeCAD in deinen Entwicklungsprozess im Maschinenbau integrieren kannst. Buche noch heute einen Termin vor Ort oder online.'
}

class ManualGenerator():
    def __init__(self, body, context = {}, model = 'standard') -> None:
        if body is None:
            return 0
        self.body = body
        self.context = context
        self.model = model
        if self.model == 'standard':
            self.model_url = 'models/standard.json'
    
    def save_html(self, abs_path) -> None:
        pass

    def generate_html_str(self) -> str:
        pass

    def get_body_features(self):
        features = self.body.Group
        return features

    '''
    text blocks
    '''
    def text_topic_intro(self):
        pass

    def text_steps_intro(self):
        pass

    def text_feature(self, feature_class_str):
        pass

    def text_summary(self):
        pass

    def text_success(self):
        pass

    def text_next(self):
        pass

    def text_ad_upsell(self):
        pass

if __name__ == '__main__':
    import sys
    import os

    #FREECAD_ABS_PATH = 'C:/PROGRA~1/FreeCAD_weekly-builds-29126-2022-06-12-conda-Windows-x86_64-py38/bin' 
    #FREECAD_ABS_PATH = 'C:/PROGRA~1/FreeCAD_weekly-builds-29126-2022-06-12-conda-Windows-x86_64-py38/bin'
    FREECAD_ABS_PATH = 'C:/PROGRA~1/FreeCAD 0.20/bin'

    # Add path to FreeCAD Python interface
    # path to your FreeCAD.so or FreeCAD.dll file
    sys.path.append(FREECAD_ABS_PATH)

    # import the FreeCAD Python interface
    try:
        import FreeCAD
        print('The FreeCAD Python interface has been loaded')
    except ValueError:
        print('FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')

    # setup project paths
    module_abs_path = os.path.abspath(__file__)
    module_abs_dir_path = os.path.dirname(module_abs_path)
    filename_no_ext = 'Elektroblech'
    path_fcstd = os.path.join(module_abs_dir_path, f'{filename_no_ext}.FCStd')
    path_html = os.path.join(module_abs_dir_path, f'{filename_no_ext}.html')
    path_pdf = os.path.join(module_abs_dir_path, f'{filename_no_ext}.pdf')

    # load the FreeCAD document
    doc = FreeCAD.openDocument(path_fcstd)

    # create a new manual generator object with a body from the loaded FreeCAD document
    mg = ManualGenerator(doc.Body)

    # get a the list of features that were used to create the body in a chronological order
    body_features = mg.get_body_features()

    steps = []

    for feature in body_features:
        steps.append(feature.TypeId)

    import jinja2

    context = {'general_text': general_text, 'steps': steps}

    env = jinja2.Environment(
        loader=jinja2.PackageLoader('fcmanualgenerator')
    )

    template = env.get_template('template.html')
    output_text = template.render(context)

    #save output_text to html file located in same folder as used freecad file
    with open(path_html, 'w') as file:
        file.write(output_text)

    #convert html file with instruction to pdf file and save it in the same folder as the html and freecad file
    import pdfkit

    path_wkhtmltopdf = r'C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdfkit.from_file(path_html, path_pdf, configuration=config)

    
    
    
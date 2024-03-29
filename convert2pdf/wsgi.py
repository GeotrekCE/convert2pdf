from flask import Flask, jsonify, request
from weasyprint import HTML

from convert2pdf.converter import Converter
from convert2pdf.utils import LibreOfficeMimeTypes, send_file_from_string


class FlaskApp(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.converter = Converter()


application = FlaskApp('convert2pdf')


@application.errorhandler(404)
def page_not_found(e):
    return jsonify(errors=['Bad url.']), 404


@application.route('/', methods=['POST'])
def to_pdf():
    if 'file' in request.files:
        f = request.files['file']
        mime_type = f.mimetype
        content = f.stream.read()

        if LibreOfficeMimeTypes.is_member(mime_type):
            pdf = application.converter.convert(content)
            return send_file_from_string(pdf, mime_type)
        elif mime_type == 'text/html':
            pdf = HTML(string=content.decode()).write_pdf()
            return send_file_from_string(pdf, mime_type)
        else:
            return (
                jsonify({'errors': ['Invalid mime type: %s is not supported.'
                                    % (mime_type, )]}),
                400
            )
    else:
        return (
            jsonify({'errors': ['No file.']}),
            400
        )

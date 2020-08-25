"""API endpoints for managing application resource."""

from http import HTTPStatus

from flask import g, jsonify, request
from flask_restx import Namespace, Resource, cors
from marshmallow import ValidationError

from ..exceptions import BusinessException
from ..schemas.aggregated_application import AggregatedApplicationReqSchema
from ..schemas.application import ApplicationListReqSchema, ApplicationSchema, ApplicationUpdateSchema
from ..services import ApplicationService, ApplicationAuditService
from ..utils.auth import auth
from ..utils.util import cors_preflight

#keeping the base path same for application history and application/
API = Namespace('Application', description='Application')

@cors_preflight('GET,OPTIONS')
@API.route('/<string:application_id>/history', methods=['GET', 'POST', 'OPTIONS'])
class ApplicationHistoryResource(Resource):
    """Resource for managing state."""

    @staticmethod
    @cors.crossdomain(origin='*')
    @auth.require
    def get(application_id):
        """Get application histry."""
        return jsonify({
            'applications': ApplicationAuditService.get_application_history(application_id)
        }), HTTPStatus.OK     

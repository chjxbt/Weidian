# *- coding:utf8 *-
import sys
import os
import uuid
from WeiDian.common.TransformToList import dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator
from WeiDian.service.SActivity import SActivity
from WeiDian.service.SActivityLike import SActivityLike
from flask import request
sys.path.append(os.path.dirname(os.getcwd()))


class CActivityLike():
    def __init__(self):
        self.sactivity = SActivity()
        self.salike = SActivityLike()

    @verify_token_decorator
    def like_or_cancel(self):
        json_data = parameter_required('acid')
        acid = json_data.get('acid')
        already_like = self.salike.is_like(request.user.id, acid)
        if not already_like:
            al_dict = dict(
                alid=str(uuid.uuid4()),
                usid=request.user.id,
                acid=acid
            )
            dict_add_models('ActivityLike', al_dict)
            alid = already_like.ALid if already_like else al_dict['alid']
            self.salike.add_like_by_acid(acid)
            data = import_status('add_activity_like_success', 'OK')
            data['data'] = {'alid': alid}
            return data
        else:
            self.salike.del_like(request.user.id, acid)
            self.salike.cancel_like_by_acid(acid)
            data = import_status('cancel_activity_like_success', 'OK')
            data['data'] = {'acid': acid}
            return data

# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# Licensed under the 【火山方舟】原型应用软件自用许可协议
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at 
#     https://www.volcengine.com/docs/82379/1433703
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
import uvicorn
from fastapi import FastAPI
from services.router import router
from common.logger import configure_logging
from common.config import get_settings
from asgi_correlation_id import CorrelationIdMiddleware
from middleware.request_id import RequestIDMiddleware
app = FastAPI(
    title="computer_use",
)
app.include_router(router)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(
    CorrelationIdMiddleware,
    header_name='X-Request-ID',
    update_request_header=True,
    generator=lambda: uuid.uuid4().hex,
    transformer=lambda a: a,
)
configure_logging()

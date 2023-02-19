from application import create_app
from app_base import FlaskDevementConfig

app = create_app(FlaskDevementConfig)

# 启动项目
if __name__ == '__main__':
    # 运行了一个flask提供的调试服务器  python application.py运行是时候生效
    app.run(host='0.0.0.0', port=8090)

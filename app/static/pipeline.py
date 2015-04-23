from flask.ext.assets import Bundle


sass = Bundle('sass/main.scss',
              output='gen/main.css')

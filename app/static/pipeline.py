from flask.ext.assets import Bundle
import sass as libsass


def __compile_sass(_in, out, **kw):
    out.write(libsass.compile(string=_in.read()))


sass = Bundle('sass/main.scss',
              filters=(__compile_sass,), output='gen/main.css')

import os, sys, re, yaml
import bottle

app_base = os.path.dirname(os.path.realpath(__file__))
app_base_join = lambda x: os.path.join(os.sep, app_base, x)

configs = yaml.load(open(app_base_join('conf' + os.sep + "application.yaml")))

bottle.TEMPLATE_PATH.append(app_base_join('views'))

control_dirs = ['controllers', 'errors', 'models']
[sys.path.append(dir) for dir in control_dirs]

[__import__(file[:-3]) 
 for cdir in control_dirs 
 for file in os.listdir(app_base_join(cdir)) 
   if re.match('.*_' + cdir[:-1] + '.py$', file)]


if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)

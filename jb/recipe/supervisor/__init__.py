import os.path
import sys

from collective.recipe.template import Recipe as Template
from zc.buildout.buildout import Options
from z3c.recipe.scripts import Scripts


class InstallSupervisor(object):
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

        b_options = buildout['buildout']
        self.cfg = options['configuration-file']

        options.setdefault('output-dir',
                           os.path.join(b_options['parts-directory'], name))

        self.output_cfg_file = os.path.join(options['output-dir'],
                                            'supervisord.conf')

    def install(self):
        buildout = self.buildout
        name = self.name
        paths = []

        def make_options(args):
            return Options(buildout, name, args)

        template_options = make_options({
            'input': self.cfg,
            'output': self.output_cfg_file,
        })
        template_options._created = []
        paths.extend(
            Template(buildout, name, template_options).install()
        )

        supervisord_options = make_options({
            'eggs': 'supervisor',
            'scripts': 'supervisord=supervisord',
            'arguments': repr(['-c', self.output_cfg_file]),
        })
        paths.extend(Scripts(buildout, name, supervisord_options).install())

        supervisorctl_options = make_options({
            'eggs': 'supervisor',
            'scripts': 'supervisorctl=supervisorctl',
            'arguments': repr(['-c', self.output_cfg_file]),
        })
        paths.extend(Scripts(buildout, name, supervisorctl_options).install())

        return paths

    def update(self):
        return []

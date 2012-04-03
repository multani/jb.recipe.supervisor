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

    def _make_options(self, args):
        return Options(self.buildout, self.name, args)

    def _install_template(self):
        template_options = self._make_options({
            'input': self.cfg,
            'output': self.output_cfg_file,
        })
        template_options._created = []

        return Template(self.buildout, self.name, template_options).install()

    def install(self):
        buildout = self.buildout
        name = self.name
        paths = []

        paths.extend(self._install_template())

        supervisord_options = self._make_options({
            'eggs': 'supervisor',
            'scripts': 'supervisord=supervisord',
            'arguments': repr(['-c', self.output_cfg_file]),
        })
        paths.extend(Scripts(buildout, name, supervisord_options).install())

        supervisorctl_options = self._make_options({
            'eggs': 'supervisor',
            'scripts': 'supervisorctl=supervisorctl',
            'arguments': repr(['-c', self.output_cfg_file]),
        })
        paths.extend(Scripts(buildout, name, supervisorctl_options).install())

        return paths

    def update(self):
        paths = []
        paths.extend(self._install_template())
        return paths

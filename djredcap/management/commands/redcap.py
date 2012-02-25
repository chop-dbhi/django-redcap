import sys
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Wrapper for REDCap subcommands"

    commands = ['inspect']
    command_prefix = 'redcap_%s'

    def print_subcommands(self, prog_name):
        usage = [
            "",
            "Available subcommands:",
        ]
        for name in sorted(self.commands):
            usage.append("    %s" % name)
        return '\n'.join(usage)

    def usage(self, subcommand):
        usage = '%%prog %s [options] subcommand [args]' % subcommand
        if self.help:
            return '%s\n\n%s' % (usage, self.help)
        else:
            return usage

    def print_help(self, prog_name, subcommand):
        super(Command, self).print_help(prog_name, subcommand)
        sys.stdout.write('%s\n' % self.print_subcommands(prog_name))

    def handle(self, *args, **options):
        if not args or args[0] not in self.commands:
            return self.print_help('./manage.py', 'redcap')
        subcommand, args = args[0], args[1:]
        return call_command(self.command_prefix % subcommand, *args, **options)


#!/usr/bin/python3


class Console:
    def do_help(self, args):
        """Display help information"""
        print(
            "Documented commands (type help <topic>):\n========================================\nEOF  help  quit"
        )

    def do_quit(self, args):
        """Exit the console"""
        return True

    def run_interactive(self):
        """Run the console in interactive mode"""
        while True:
            command = input("(hbnb) ")
            if not command:
                continue
            if self.execute_command(command):
                break

    def run_non_interactive(self, command):
        """Run the console in non-interactive mode"""
        self.execute_command(command)

    def execute_command(self, command):
        """Execute a given command"""
        cmd, *args = command.split()
        method_name = f"do_{cmd}"
        if hasattr(self, method_name):
            return getattr(self, method_name)(args)
        else:
            print(f"Invalid command: {command}")


if __name__ == "__main__":
    console = Console()

    # Check if the script is running in interactive or non-interactive mode
    import sys

    if len(sys.argv) == 1:
        console.run_interactive()
    else:
        command = " ".join(sys.argv[1:])
        console.run_non_interactive(command)

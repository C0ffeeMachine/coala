from coalib.output.Interactor import Interactor


class NullInteractor(Interactor):
    def print_result(self, result, file_dict):
        return

    def _print_actions(self, actions):
        return (None, None)

    def did_nothing(self):
        pass

    def begin_section(self, name):
        pass

    def acquire_settings(self, settings):
        # We can't get settings here, if bears need them, they better fail.
        pass

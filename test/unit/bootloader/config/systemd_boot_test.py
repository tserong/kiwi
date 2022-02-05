from mock import Mock
from kiwi.bootloader.config.systemd_boot import BootLoaderSystemdBoot


class TestBootLoaderSystemdBoot:
    def setup(self):
        self.state = Mock()
        self.bootloader = BootLoaderSystemdBoot(self.state, 'root_dir')

    def test_setup_loader(self):
        # just pass
        self.bootloader.setup_loader('target')

    def test_set_loader_entry(self):
        # just pass
        self.bootloader.set_loader_entry('target')

    def test_create_loader_image(self):
        # just pass
        self.bootloader.create_loader_image('target')

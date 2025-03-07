import logging
from pytest import fixture
from mock import patch
import mock

from kiwi.filesystem.isofs import FileSystemIsoFs


class TestFileSystemIsoFs:
    @fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    @patch('os.path.exists')
    def setup(self, mock_exists):
        mock_exists.return_value = True
        self.isofs = FileSystemIsoFs(mock.Mock(), 'root_dir')

    @patch('os.path.exists')
    def setup_method(self, cls, mock_exists):
        self.setup()

    def test_post_init(self):
        self.isofs.post_init({'some_args': 'data'})
        assert self.isofs.custom_args['meta_data'] == {}
        assert self.isofs.custom_args['mount_options'] == []
        assert self.isofs.custom_args['some_args'] == 'data'

    @patch('kiwi.filesystem.isofs.IsoTools')
    @patch('kiwi.filesystem.isofs.Iso')
    def test_create_on_file(self, mock_iso, mock_IsoTools):
        iso_tool = mock.Mock()
        iso_tool.has_iso_hybrid_capability = mock.Mock(
            return_value=True
        )
        iso_tool.get_tool_name = mock.Mock(
            return_value='/usr/bin/xorriso'
        )
        mock_IsoTools.new.return_value = iso_tool
        iso = mock.Mock()
        iso.header_end_name = 'header_end'
        mock_iso.return_value = iso
        self.isofs.create_on_file('myimage', None)

        iso.setup_isolinux_boot_path.assert_called_once_with()

        iso_tool.init_iso_creation_parameters.assert_called_once_with({})

        iso_tool.create_iso.assert_called_once_with('myimage')

    @patch('kiwi.filesystem.isofs.IsoTools')
    @patch('kiwi.filesystem.isofs.Iso')
    def test_create_on_file_EFI_enabled(self, mock_iso, mock_IsoTools):
        iso_tool = mock.Mock()
        iso_tool.has_iso_hybrid_capability = mock.Mock(
            return_value=True
        )
        iso_tool.get_tool_name = mock.Mock(
            return_value='/usr/bin/xorriso'
        )
        mock_IsoTools.new.return_value = iso_tool
        iso = mock.Mock()
        iso.header_end_name = 'header_end'
        mock_iso.return_value = iso
        self.isofs.custom_args['meta_data']['efi_mode'] = 'uefi'
        self.isofs.custom_args['meta_data']['efi_loader'] = 'esp-image-file'
        with self._caplog.at_level(logging.WARNING):
            self.isofs.create_on_file('myimage')
            iso_tool.create_iso.assert_called_once_with('myimage')
            iso_tool.add_efi_loader_parameters.assert_called_once_with(
                'esp-image-file'
            )

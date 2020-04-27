import sys
import re
from pathlib import Path, PureWindowsPath
from functools import partial
import subprocess
import fileinput
import time
import logging

from PySide2 import QtWidgets
from PySide2 import QtCore

from ui_main_qt5 import Ui_MainWindow

logging.basicConfig(
    level=logging.DEBUG, 
    filename='mk_usdcat_all.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)

_REQUIRED_BINARIES = ('hython.exe', 'usdcat')
_ALL_USD_EXTS = ('.usd', '.usdc', '.usda')
_USD_DEFAULT_EXT = '.usd'
_USD_ASCII_FORMATS = {False: 'usdc', True: 'usda'}


class USDCatAll(QtWidgets.QWidget):
    def __init__(self):
        super(USDCatAll, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def log_exec_time(func):
    '''
    Simple utility function to log execution time
    '''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        exec_time = time.time() - start_time
        logging.debug(
            '****Execution time: {:.3f} second (--in "{}").'.format(exec_time, func.__name__)
        )
        return ret
    return wrapper

def ui_launch():
    app = QtWidgets.QApplication(sys.argv)
    win = USDCatAll()

    ui_init(win.ui)
    create_connections(win.ui)

    win.show()
    sys.exit(app.exec_())

def ui_init(ui):
    houdini_latest_install_bin_folder = find_houdini_latest_install_bin_folder()
    if houdini_latest_install_bin_folder:
        ui.preq_houdini_bin_folder_lineEdit.setText(houdini_latest_install_bin_folder.as_posix())
    
    # First time run validation
    visualize_folder_input_validation(
        line_edit=ui.preq_houdini_bin_folder_lineEdit,
        validate_label=ui.preq_houdini_bin_folder_validate_status_label,
        required_files=_REQUIRED_BINARIES
    )
    enable_del_orig_option(
        ui.usdcat_change_extension_checkBox.isChecked(),
        ui.usdcat_delete_originals_checkBox
    )

    ui.usdcat_folder_to_batch_lineEdit.setFocus()

def create_connections(ui):
    ui.preq_houdini_bin_folder_lineEdit.editingFinished.connect(partial(
        visualize_folder_input_validation,
        line_edit=ui.preq_houdini_bin_folder_lineEdit,
        validate_label=ui.preq_houdini_bin_folder_validate_status_label,
        required_files=_REQUIRED_BINARIES
    ))

    ui.preq_houdini_bin_folder_browse_btn.clicked.connect(partial(
        browse_houdini_bin_folder,
        line_edit=ui.preq_houdini_bin_folder_lineEdit,
        validate_label=ui.preq_houdini_bin_folder_validate_status_label
    ))

    ui.preq_houdini_bin_folder_open_pushButton.clicked.connect(partial(
        open_explorer,
        get_folder_method=ui.preq_houdini_bin_folder_lineEdit.text
    ))

    ui.usdcat_change_extension_checkBox.toggled.connect(partial(
        enable_del_orig_option,
        del_orig_option_widget=ui.usdcat_delete_originals_checkBox
    ))

    ui.usdcat_folder_to_batch_lineEdit.returnPressed.connect(partial(
        batch_conversion,
        get_bin_folder_method=ui.preq_houdini_bin_folder_lineEdit.text,
        get_folder_to_usdcat_method=ui.usdcat_folder_to_batch_lineEdit.text,
        get_ascii_output_mode_method=ui.usdcat_output_ascii_radioButton.isChecked,
        get_change_extension_mode_method=ui.usdcat_change_extension_checkBox.isChecked,
        get_remove_orig_mode_method=ui.usdcat_delete_originals_checkBox.isChecked,
        progress_widget=ui.usdcat_batch_progressBar
    ))

    ui.usdview_file_to_run_lineEdit.returnPressed.connect(partial(
        launch_usdview,
        get_bin_folder_method=ui.preq_houdini_bin_folder_lineEdit.text,
        get_file_to_usdview_method=ui.usdview_file_to_run_lineEdit.text
    ))

def browse_houdini_bin_folder(line_edit, validate_label):
    houdini_bin_folder = QtWidgets.QFileDialog.getExistingDirectory()

    if houdini_bin_folder:
        line_edit.setText(houdini_bin_folder)

        visualize_folder_input_validation(
            line_edit=line_edit,
            validate_label=validate_label,
            required_files=_REQUIRED_BINARIES
        )
        
def find_houdini_latest_install_bin_folder(houdini_install_path='C:/Program Files/Side Effects Software'):
    '''
    Presume Houdini is installed in 'C:/'
    '''
    found_houdini_latest_install = list(Path(houdini_install_path).glob('Houdini*'))
    found_houdini_latest_install = sorted(found_houdini_latest_install)[-1] / 'bin' \
        if found_houdini_latest_install else None
    return found_houdini_latest_install \
        if found_houdini_latest_install and found_houdini_latest_install.exists() else None

def validate_folder_path(folder_path, required_files=()):
    '''
    Check if folder exists, and whether there are files of specified types within that folder
    '''
    folder_path = Path(folder_path)

    if not folder_path.exists():
        logging.warning('Folder does not exist: {}'.format(folder_path))
        return False
    else:
        # Validate all the specified files inside
        for required_file in required_files:
            required_file = (folder_path / required_file)
            if not (required_file.exists() and required_file.is_file()):
                logging.warning('File does not exist: {}'.format(required_file))
                return False

    return True

def update_validate_label(validate_label, valid):
    '''
    '''
    if valid:
        validate_label.setText('Valid')
        validate_label.setStyleSheet('color:green')
    else:
        validate_label.setText('Invalid')
        validate_label.setStyleSheet('color:red')

def visualize_folder_input_validation(line_edit, validate_label, required_files=()):
    '''
    Update QLabel to show whether the selected bin folder has required files in order to operate
    '''
    validate_result = validate_folder_path(
        line_edit.text(), 
        required_files=required_files
    )

    update_validate_label(
        validate_label,
        validate_result
    )

def enable_del_orig_option(checked, del_orig_option_widget):
    del_orig_option_widget.setEnabled(checked)

def get_usd_input_output_extensions(ascii_output_mode):
    '''
    :param int ascii_output_mode:
    '''
    infile_ext = '.' + _USD_ASCII_FORMATS[not ascii_output_mode]
    outfile_ext = '.' + _USD_ASCII_FORMATS[ascii_output_mode]

    return infile_ext, outfile_ext

@log_exec_time
def batch_usdcat(hython_path, usdcat_module_path, folder_to_usdcat, ascii_output_mode, change_extension, remove_orig, progress_widget):
    '''
    :param Path folder_to_usdcat:
    '''
    progress_widget.setValue(0)
    
    # Assuming default behavior is not changing the extension
    infile_ext = _USD_DEFAULT_EXT

    if change_extension:
        infile_ext, outfile_ext = get_usd_input_output_extensions(ascii_output_mode=ascii_output_mode)

    infiles = set()
    for usd_ext in _ALL_USD_EXTS:
        infiles.update(tuple(folder_to_usdcat.rglob('*' + usd_ext)))  # taking even .usdc or .usda

    num_jobs = len(infiles)
    logging.debug('PERFORMING {} "USDCAT CONVERSION" jobs...'.format(num_jobs))

    for i, infile in enumerate(infiles):

        logging.debug('--Converting asset: {}'.format(infile.name))

        if not change_extension:
            cmd = [
                hython_path,
                usdcat_module_path,
                infile.as_posix(),
                '--out',
                infile.as_posix(),  # retaining the .usd extension and overwriting files
                '--usdFormat',
                _USD_ASCII_FORMATS[ascii_output_mode]
            ]
            subprocess_call(cmd)
        else:
            cmd = [
                hython_path,
                usdcat_module_path,
                infile.as_posix(),
                '--out',
                infile.with_suffix(outfile_ext).as_posix()
            ]

            subprocess_call(cmd)

            if remove_orig:
                infile.unlink()

        progress_widget.setValue(round(i / num_jobs * 100))
        QtCore.QCoreApplication.processEvents()  # update the progress bar visually

@log_exec_time
def subprocess_call(cmd):
    # logging.debug(str(cmd))
    try:
        subprocess.call(cmd)
    except Exception as e:
        logging.warning('--Failed: {}'.format(e))
   
def batch_conversion(
    get_bin_folder_method, 
    get_folder_to_usdcat_method, 
    get_ascii_output_mode_method, 
    get_change_extension_mode_method, 
    get_remove_orig_mode_method, 
    progress_widget
):
    # Sanity check
    bin_path = get_bin_folder_method()
    folder_to_usdcat = get_folder_to_usdcat_method()

    bin_path_validated = validate_folder_path(bin_path, _REQUIRED_BINARIES)
    folder_to_usdcat_validated = validate_folder_path(folder_to_usdcat)

    ascii_output_mode = get_ascii_output_mode_method()
    change_extension = get_change_extension_mode_method()

    if bin_path_validated and folder_to_usdcat_validated:

        bin_path = Path(bin_path)
        hython_path = bin_path / 'hython.exe'
        usdcat_module_path = bin_path / 'usdcat'

        folder_to_usdcat = Path(folder_to_usdcat)

        do_batch_usdcat = partial(
            batch_usdcat,
            hython_path=hython_path.as_posix(),
            usdcat_module_path=usdcat_module_path.as_posix(),
            folder_to_usdcat=folder_to_usdcat, 
            ascii_output_mode=ascii_output_mode,
            change_extension=change_extension,
            remove_orig=get_remove_orig_mode_method(),
            progress_widget=progress_widget
        )

        do_edit_usd_asset_path = partial(
            edit_usd_asset_path,
            folder_to_usdcat=folder_to_usdcat,
            ascii_output_mode=ascii_output_mode
        )

        if not change_extension:
            do_batch_usdcat()  # No need for editing file content
        else:
            if ascii_output_mode:
                # Convert USD format with usdcat before editing file content
                do_batch_usdcat()
                do_edit_usd_asset_path()
            else:
                # Edit file content before converting USD format with usdcat
                do_edit_usd_asset_path()
                do_batch_usdcat()

        progress_widget.setValue(100)
    else:
        logging.error('Invalid input. Aborted')

def count_jobs(generator_obj):
    return len(tuple(generator_obj))

@log_exec_time
def edit_usd_asset_path(folder_to_usdcat, ascii_output_mode):
    '''
    :param Path folder_to_usdcat:
    '''
    infile_ext, outfile_ext = get_usd_input_output_extensions(ascii_output_mode=ascii_output_mode)

    files_to_edit = tuple(folder_to_usdcat.rglob('*' + _USD_ASCII_FORMATS[True]))  # only editing .usda is relevant
    logging.debug('PERFORMING {} "USD ASSET PATH EDIT" jobs...'.format(len(files_to_edit)))

    files_to_edit = [infile.as_posix() for infile in files_to_edit]

    # First edit if found '.usdc' or '.usda'
    with fileinput.input(files=files_to_edit, inplace=True) as usdfile:
        for line in usdfile:
            print(line.replace(infile_ext + '@', outfile_ext + '@'), end='')

    # Second edit if found '.usd'
    with fileinput.input(files=files_to_edit, inplace=True) as usdfile:
        for line in usdfile:
            print(line.replace(_USD_DEFAULT_EXT + '@', outfile_ext + '@'), end='')    


def open_explorer(get_folder_method):

    folder_path = Path(get_folder_method())

    if folder_path.exists() and folder_path.is_dir():
        subprocess.Popen(['explorer', str(PureWindowsPath(folder_path))])

def launch_usdview(get_bin_folder_method, get_file_to_usdview_method):
    bin_path = get_bin_folder_method()
    file_to_usdview = Path(get_file_to_usdview_method())

    bin_path_validated = validate_folder_path(bin_path, _REQUIRED_BINARIES)
    # file_to_usdview_validated = file_to_usdview.exists() and file_to_usdview.suffix in _USD_ASCII_FORMATS

    if bin_path_validated:

        bin_path = Path(bin_path)
        hython_path = bin_path / 'hython.exe'
        usdview_module_path = bin_path / 'usdview'

        cmd = [
                hython_path,
                usdview_module_path,
                file_to_usdview.as_posix()
            ]

        subprocess_call(cmd)


if __name__ == '__main__':
    ui_launch()
    pass

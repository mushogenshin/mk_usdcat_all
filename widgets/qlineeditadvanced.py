from PySide2 import QtWidgets
from pathlib import Path


class QLineEditAcceptUrlDrop(QtWidgets.QLineEdit):
    def __init__(self, text):
        super(QLineEditAcceptUrlDrop, self).__init__(text)
        self._path_verify_method = self.verify_path
        
    def verify_path(self, *args, **kwargs):
        raise NotImplementedError
    
    def dragEnterEvent(self, drag_event):
        if drag_event.mimeData().hasUrls():  # accept URLs only
            drag_event.acceptProposedAction()
        
    def dragMoveEvent(self, drag_event):
        '''
        Must have this for the drop to work
        '''
        pass

    def dropEvent(self, drop_event):
        mime_data = drop_event.mimeData()
        if mime_data.hasUrls():
            drop_event.accept()
            for url in mime_data.urls():
                url_path = Path(url.toLocalFile())
                if self._path_verify_method(url_path):
                    self.setText(url_path.as_posix())


class QLineEditAcceptDirectoryDrop(QLineEditAcceptUrlDrop):
    def __init__(self, text):
        super(QLineEditAcceptDirectoryDrop, self).__init__(text)
        self._path_verify_method = Path.is_dir


class QLineEditAcceptFileDrop(QLineEditAcceptUrlDrop):
    def __init__(self, text):
        super(QLineEditAcceptFileDrop, self).__init__(text)
        self._path_verify_method = Path.is_file


# if __name__ == '__main__':
#     pass

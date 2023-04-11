import sys
import fitz
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap, QImage, QAction
from PyQt6.QtCore import Qt, QRectF
from crossref.restful import Works
from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtGui import QColor, QPen

class LinkItem(QGraphicsRectItem):
    def __init__(self, link, viewer, parent=None):
        super().__init__(parent)
        self.link = link
        self.viewer = viewer
        print(self.link['kind'], self.link['from'], self.link['to'])
        if 'to' in self.link.keys():
            x1, y1, x2, y2 = self.link['from']
            # x2, y2 = self.link['to']
            self.setRect(x1, y1, x2 - x1, y2 - y1)
        else:
            x1, y1, x2, y2 = self.link['from']
            self.setRect(x1, y1, x2 - x1, y2 - y1)
        self.setAcceptHoverEvents(True)

        # Set a transparent fill color and a light blue border color
        self.setBrush(QColor(0, 0, 0, 0))
        self.setPen(QPen(QColor(0, 0, 255, 128), 1))
        
class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom PDF Viewer")
        self.init_ui()

    def extract_links(self):
        self.pdf_links = []

        for page_number in range(len(self.pdf)):
            page = self.pdf[page_number]
            links = page.get_links()
            self.pdf_links.append(links)

    def init_ui(self):
        self.create_toolbar()

        self.view = QGraphicsView(self)
        self.setCentralWidget(self.view)
        self.scene = QGraphicsScene(self.view)

    def create_toolbar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        open_action = QAction("Open PDF", self)
        open_action.triggered.connect(self.open_pdf)
        toolbar.addAction(open_action)

        copy_bibtex_action = QAction("Copy BibTeX", self)
        copy_bibtex_action.triggered.connect(self.copy_bibtex)
        toolbar.addAction(copy_bibtex_action)

    def open_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf = fitz.open(file_path)
            self.extract_links()
            self.show_page(0)

    def show_page(self, page_number):
        self.scene.clear()

        page = self.pdf[page_number]
        zoom = 2.0
        matrix = fitz.Matrix(zoom, zoom)
        pixmap = page.get_pixmap(matrix=matrix)
        qimage = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format.Format_RGB888)
        pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(qimage))
        self.scene.addItem(pixmap_item)
        self.view.setScene(self.scene)
        self.view.setSceneRect(QRectF(pixmap_item.boundingRect()))

        # Add links to the scene
        for link in self.pdf_links[page_number]:
            print(link.keys())
            link_item = LinkItem(link, viewer)
            link_item.setScale(zoom)
            x, y, _, _ = link['from']
            link_item.setPos(x * zoom, y * zoom)
            self.scene.addItem(link_item)

    def copy_bibtex(self):
        # Implement BibTeX citation copy feature here
        print('there')
        pass

    def fetch_citation_data(self, citation_marker):
        # Implement citation data fetching here
        print('here')
        pass

app = QApplication(sys.argv)
viewer = PDFViewer()
viewer.show()
sys.exit(app.exec())
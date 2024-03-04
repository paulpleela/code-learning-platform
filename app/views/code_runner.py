import sys
import subprocess
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QPlainTextEdit, QTextEdit, QSplitter
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QPainter, QTextFormat
from PySide6.QtCore import Qt, QRect, QSize

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.editor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.line_number_area = LineNumberArea(self)
        self.setViewportMargins(self.line_number_area.width(), 0, 0, 0)
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)
        self.update_line_number_area_width(0)

    def line_number_area_width(self):
        digits = len(str(self.blockCount()))
        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def highlight_current_line(self):
        extra_selections = []

        selection = QTextEdit.ExtraSelection()
        selection.format.setBackground(Qt.lightGray)
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor = self.textCursor()
        selection.cursor.clearSelection()
        extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), Qt.white)

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.line_number_area.width(), self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            cursor = self.textCursor()
            block = cursor.block()
            text = block.text()
            cursor.insertText('\n')
            # Check if the current line has indentation
            indentation = re.match(r'^\s*', text).group(0)
            if indentation:
                cursor.insertText(indentation)
            # Check if the current line ends with a colon
            index = text.rfind(':')
            if index != -1 and index == len(text) - 1:
                cursor.insertText('\t')
        else:
            super().keyPressEvent(event)


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
        ]
        self.highlighting_rules.extend([(r'\b%s\b' % w, keyword_format) for w in keywords])

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), format)


class CodeRunner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Code Editor")
        self.resize(800, 550)

        # Create text input box with syntax highlighting
        self.input_text = CodeEditor()
        self.input_text.setTabStopDistance(20)
        self.highlighter = PythonSyntaxHighlighter(self.input_text.document())

        # Create output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Create a button to run the code
        self.run_button = QPushButton("Run Code")
        self.run_button.clicked.connect(self.run_code)

        # Create a splitter to resize input and output areas
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.input_text)
        self.splitter.addWidget(self.output_text)

        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        layout.addWidget(self.run_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def run_code(self):
        code = self.input_text.toPlainText()

        # Run the Python code using subprocess
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)

        # Display output or error
        if result.returncode == 0:
            self.output_text.setText(result.stdout)
        else:
            self.output_text.setText("Error:\n" + result.stderr)


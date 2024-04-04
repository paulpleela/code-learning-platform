import sys
import subprocess
import re
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QPlainTextEdit, QTextEdit, QSplitter, QHBoxLayout
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QPainter, QTextFormat
from PySide6.QtCore import Qt, QRect, QSize

from views.navigation import NavigationBar

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


class QuizPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 550)

        font = QFont()
        font.setFamily("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.input_text = CodeEditor()
        self.input_text.setFont(font)
        self.input_text.setTabStopDistance(20)
        self.highlighter = PythonSyntaxHighlighter(self.input_text.document())

        self.output_text = QTextEdit()
        self.output_text.setFont(font)
        self.output_text.setReadOnly(True)

        self.run_button = QPushButton("Run Code")
        self.run_button.clicked.connect(self.run_code)

        instructions = QVBoxLayout()
        instruction_text = QTextEdit()
        instruction_text.setPlainText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        instruction_text.setReadOnly(True)
        instructions.addWidget(instruction_text)

        code_runner = QVBoxLayout()
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.input_text)
        splitter.addWidget(self.output_text)
        code_runner.addWidget(self.run_button)
        code_runner.addWidget(splitter)

        main_layout = QHBoxLayout()
        main_layout.addLayout(code_runner, 70)
        main_layout.addLayout(instructions, 30)

        layout = QVBoxLayout()
        layout.addLayout(main_layout)

        self.nav_bar = NavigationBar()
        layout.addWidget(self.nav_bar, alignment=Qt.AlignBottom)

        # self.nav_bar.previous_button.clicked.connect(self.previous_page)
        # self.nav_bar.next_button.clicked.connect(self.next_page)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def run_code(self):
        code = self.input_text.toPlainText()
        if "input(" in code:
            self.output_text.setTextColor(Qt.red)
            self.output_text.setText("Error:\n" + "input() function not allowed")
            return
        
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True)

        if result.returncode == 0:
            self.output_text.setTextColor(Qt.black)
            self.output_text.setText(result.stdout)
        else:
            self.output_text.setTextColor(Qt.red)
            self.output_text.setText("Error:\n" + result.stderr)

    # def previous_page(self):
    #     print("Go to previous page")

    # def next_page(self):
    #     print("Go to next page")
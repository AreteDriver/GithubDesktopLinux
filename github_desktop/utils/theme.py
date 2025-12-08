"""Theme and styling utilities."""

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt


class Theme:
    """Application theme configuration."""
    
    # Color scheme
    PRIMARY = "#0366d6"
    PRIMARY_DARK = "#0256c7"
    SECONDARY = "#586069"
    SUCCESS = "#28a745"
    DANGER = "#d73a49"
    WARNING = "#ffd33d"
    INFO = "#0366d6"
    
    # Background colors
    BG_PRIMARY = "#ffffff"
    BG_SECONDARY = "#f6f8fa"
    BG_TERTIARY = "#24292e"
    BG_DARK = "#1b1f23"
    
    # Text colors
    TEXT_PRIMARY = "#24292e"
    TEXT_SECONDARY = "#586069"
    TEXT_TERTIARY = "#6a737d"
    TEXT_LIGHT = "#ffffff"
    
    # Border colors
    BORDER_PRIMARY = "#e1e4e8"
    BORDER_SECONDARY = "#d1d5da"
    
    @staticmethod
    def apply_light_theme(app: QApplication):
        """Apply light theme to the application."""
        palette = QPalette()
        
        # Window
        palette.setColor(QPalette.ColorRole.Window, QColor(Theme.BG_PRIMARY))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(Theme.TEXT_PRIMARY))
        
        # Base
        palette.setColor(QPalette.ColorRole.Base, QColor(Theme.BG_PRIMARY))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(Theme.BG_SECONDARY))
        
        # Text
        palette.setColor(QPalette.ColorRole.Text, QColor(Theme.TEXT_PRIMARY))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(Theme.TEXT_LIGHT))
        
        # Button
        palette.setColor(QPalette.ColorRole.Button, QColor(Theme.BG_SECONDARY))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(Theme.TEXT_PRIMARY))
        
        # Highlight
        palette.setColor(QPalette.ColorRole.Highlight, QColor(Theme.PRIMARY))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Theme.TEXT_LIGHT))
        
        app.setPalette(palette)
    
    @staticmethod
    def apply_dark_theme(app: QApplication):
        """Apply dark theme to the application."""
        palette = QPalette()
        
        # Window
        palette.setColor(QPalette.ColorRole.Window, QColor(Theme.BG_DARK))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(Theme.TEXT_LIGHT))
        
        # Base
        palette.setColor(QPalette.ColorRole.Base, QColor(Theme.BG_TERTIARY))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(Theme.BG_DARK))
        
        # Text
        palette.setColor(QPalette.ColorRole.Text, QColor(Theme.TEXT_LIGHT))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(Theme.TEXT_LIGHT))
        
        # Button
        palette.setColor(QPalette.ColorRole.Button, QColor(Theme.BG_TERTIARY))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(Theme.TEXT_LIGHT))
        
        # Highlight
        palette.setColor(QPalette.ColorRole.Highlight, QColor(Theme.PRIMARY))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Theme.TEXT_LIGHT))
        
        app.setPalette(palette)
    
    @staticmethod
    def get_stylesheet() -> str:
        """Get application-wide stylesheet."""
        return """
            QMainWindow {
                background-color: #f6f8fa;
            }
            
            QPushButton {
                background-color: #0366d6;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: #0256c7;
            }
            
            QPushButton:pressed {
                background-color: #024ea4;
            }
            
            QPushButton:disabled {
                background-color: #94a3b8;
                color: #e2e8f0;
            }
            
            QPushButton.secondary {
                background-color: #f6f8fa;
                color: #24292e;
                border: 1px solid #e1e4e8;
            }
            
            QPushButton.secondary:hover {
                background-color: #e6ebf1;
            }
            
            QPushButton.danger {
                background-color: #d73a49;
            }
            
            QPushButton.danger:hover {
                background-color: #c52a3a;
            }
            
            QLineEdit, QTextEdit {
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                padding: 6px 8px;
                background-color: white;
            }
            
            QLineEdit:focus, QTextEdit:focus {
                border-color: #0366d6;
                outline: none;
            }
            
            QListWidget {
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                background-color: white;
            }
            
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #e1e4e8;
            }
            
            QListWidget::item:selected {
                background-color: #f1f8ff;
                color: #24292e;
            }
            
            QListWidget::item:hover {
                background-color: #f6f8fa;
            }
            
            QTabWidget::pane {
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                background-color: white;
            }
            
            QTabBar::tab {
                background-color: #f6f8fa;
                color: #586069;
                border: 1px solid #e1e4e8;
                border-bottom: none;
                padding: 8px 16px;
                margin-right: 2px;
            }
            
            QTabBar::tab:selected {
                background-color: white;
                color: #24292e;
                font-weight: 600;
            }
            
            QTabBar::tab:hover {
                background-color: #e6ebf1;
            }
            
            QTreeWidget {
                border: 1px solid #e1e4e8;
                border-radius: 4px;
                background-color: white;
            }
            
            QTreeWidget::item {
                padding: 4px;
            }
            
            QTreeWidget::item:selected {
                background-color: #f1f8ff;
            }
            
            QScrollBar:vertical {
                border: none;
                background-color: #f6f8fa;
                width: 12px;
                margin: 0;
            }
            
            QScrollBar::handle:vertical {
                background-color: #d1d5da;
                border-radius: 6px;
                min-height: 20px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #959da5;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            
            QStatusBar {
                background-color: #24292e;
                color: #ffffff;
            }
        """

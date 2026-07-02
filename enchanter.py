import sys
import os
import re
import json
import subprocess
import webbrowser

SETTINGS_FILE = "settings.json"
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: pass
    return {"lang": "ru"}

def save_settings(s):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(s, f)

SETTINGS = load_settings()

TRANSLATIONS = {
    "Подождите...": "Please wait...",
    "HyperOS Enchanter": "HyperOS Enchanter",
    "Создавайте идеальные обои и управляйте темами": "Create perfect wallpapers and manage themes",
    "🎨 Создание обоев": "🎨 Wallpaper Creator",
    "⚙️ Менеджер тем": "⚙️ Theme Manager",
    "Нажмите 'Выбрать фото' или перетащите сюда": "Click 'Select Photo' or drag and drop here",
    "Нейросеть (если горизонт обрезается, смените модель):": "AI Model (if horizon is cut off, change model):",
    "isnet-general-use (По умолчанию, высокая детализация)": "isnet-general-use (Default, high detail)",
    "u2net (Универсальная, лучше ловит пейзажи и горизонты)": "u2net (Universal, better for landscapes)",
    "birefnet-general (Новейшая, очень точная)": "birefnet-general (Newest, highly accurate)",
    "u2net_human_seg (Только люди)": "u2net_human_seg (Humans only)",
    " Выбрать фото": " Select Photo",
    " Своя маска": " Custom Mask",
    " ИИ Маска": " AI Mask",
    "Имя файла обоев:": "Wallpaper filename:",
    " Установить на телефон (Root)": " Install to Phone (Root)",
    "Готово к работе. Подключите телефон по USB.": "Ready. Connect your phone via USB.",
    "🔄 Поиск всех тем на телефоне (Root)": "🔄 Find all themes on phone (Root)",
    "Темы (папки):": "Themes (folders):",
    "✏️ Изменить имя папки": "✏️ Rename folder",
    "🗑️ Удалить ПАПКУ (Тему)": "🗑️ Delete FOLDER (Theme)",
    "Обои внутри темы:": "Wallpapers inside theme:",
    "✂️ Удалить только ФОТО": "✂️ Delete PHOTO only",
    "✏️ Переименовать фото": "✏️ Rename photo",
    "Предпросмотр (Оригинал + Маска):": "Preview (Original + Mask):",
    "Выберите обои\nв левом списке\nдля просмотра": "Select wallpaper\nin the left list\nto view preview",
    "Ошибка ADB": "ADB Error",
    "Телефон не подключен или выключена отладка по USB.": "Phone not connected or USB debugging disabled.",
    "Поиск тем на устройстве...": "Searching themes on device...",
    "Пусто": "Empty",
    "Папок с темами не найдено.": "No theme folders found.",
    "Чтение темы: ": "Reading theme: ",
    "ОШИБКА JSON\n": "JSON ERROR\n",
    "Загрузка миниатюр обоев...": "Loading wallpaper thumbnails...",
    "Скачивание иконки ": "Downloading icon ",
    "Слайд ": "Slide ",
    "Файл не указан\nв JSON": "File not specified\nin JSON",
    "Сборка полноформатного\nпредпросмотра с маской...": "Building full\npreview with mask...",
    "Файл не найден\nна устройстве": "File not found\non device",
    "Ошибка загрузки\nпревью": "Error loading\npreview",
    "Внимание": "Warning",
    "Сначала выберите обои в центральной колонке!": "First select a wallpaper in the middle column!",
    "Удалить файл '": "Delete file '",
    "' из этой темы?": "' from this theme?",
    "Успех": "Success",
    "Обои удалены из темы!": "Wallpaper deleted from theme!",
    "Сначала выберите тему в левом списке!": "First select a theme in the left list!",
    "Изменить имя темы": "Rename theme",
    "Введите новое отображаемое имя темы:": "Enter new display name for theme:",
    "Отображаемое имя темы успешно изменено на '": "Theme display name successfully changed to '",
    "'!": "'!",
    "Переименовать фото": "Rename photo",
    "Введите новое имя для фото (без .jpg):": "Enter new name for photo (without .jpg):",
    "Ошибка": "Error",
    "Имя не может быть пустым после конвертации!": "Name cannot be empty after conversion!",
    "Фото успешно переименовано в '": "Photo successfully renamed to '",
    "Удаление темы": "Delete theme",
    "Вы точно хотите БЕЗВОЗВРАТНО удалить папку со всеми обоями внутри:\n": "Are you sure you want to PERMANENTLY delete the folder and all wallpapers inside:\n",
    " ?": " ?",
    "Тема удалена с устройства!": "Theme deleted from device!",
    "Модель изменена. Нажмите 'ИИ Маска' для перерисовки.": "Model changed. Click 'AI Mask' to redraw.",
    "Выбрать фото": "Select photo",
    "Выбрать свою маску": "Select custom mask",
    "Кастомная маска успешно загружена! Проверьте результат.": "Custom mask loaded! Check the result.",
    "Не удалось загрузить маску: ": "Failed to load mask: ",
    "Скачивание модели... ": "Downloading model... ",
    "Подготовка модели ": "Preparing model ",
    "Генерация маски (": "Generating mask (",
    ")... Вычисляем, программа не зависла.": ")... Computing, program is not frozen.",
    "Маска готова! Проверьте результат и нажмите 'Установить'.": "Mask ready! Check result and click 'Install'.",
    "Ошибка генерации": "Generation Error",
    "Ошибка генерации маски": "Error generating mask",
    "Копирование на телефон... Подтвердите Root-доступ на экране!": "Copying to phone... Confirm Root access on screen!",
    "Ошибка подключения ADB": "ADB connection error",
    "Успех!": "Success!",
    "Обои '": "Wallpaper '",
    "' успешно установлены в HyperOS!\nПапка: ": "' successfully installed in HyperOS!\nFolder: ",
    "Успешно завершено! Можно выбрать новое фото.": "Successfully completed! You can select a new photo."
}

def _(text):
    if SETTINGS.get("lang", "ru") == "en":
        return TRANSLATIONS.get(text, text)
    return text

import sys
import os
if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)

# ВАЖНО: Импортируем rembg (onnxruntime) ДО PyQt5!
from rembg import remove, new_session
from PIL import Image

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QLineEdit, QFileDialog, QMessageBox, QGraphicsDropShadowEffect, 
                             QComboBox, QProgressBar, QTabWidget, QListWidget, QListWidgetItem, QInputDialog,
                             QDialog, QFrame)
from PyQt5.QtGui import QPixmap, QImage, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSize

class StreamInterceptor:
    def __init__(self, callback):
        self.callback = callback
        self.original = sys.stderr

    def write(self, s):
        self.callback(s)
        self.original.write(s)
        self.original.flush()
        
    def flush(self):
        self.original.flush()

class LoadingDialog(QDialog):
    def __init__(self, text=_("Подождите..."), parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        frame = QFrame(self)
        frame.setStyleSheet("background-color: #27272a; border-radius: 12px; border: 1px solid #3b82f6;")
        frame_layout = QVBoxLayout(frame)
        
        self.lbl = QLabel(text, frame)
        self.lbl.setStyleSheet("color: white; font-size: 16px; font-weight: bold; padding: 20px;")
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setWordWrap(True)
        frame_layout.addWidget(self.lbl)
        
        layout.addWidget(frame)
        self.resize(380, 120)

class MaskGeneratorThread(QThread):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, original_img, session):
        super().__init__()
        self.original_img = original_img
        self.session = session

    def run(self):
        try:
            from rembg import remove
            mask_img = remove(
                self.original_img, 
                session=self.session,
                only_mask=True, 
                alpha_matting=True,
                alpha_matting_foreground_threshold=240,
                alpha_matting_background_threshold=10,
                alpha_matting_erode_size=10
            )
            self.finished.emit(mask_img)
        except Exception as e:
            self.error.emit(str(e))

QSS = """
QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', 'Inter', Arial, sans-serif;
}

QPushButton {
    background-color: #3b82f6;
    color: white;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 14px;
    font-weight: 600;
    border: none;
}

QPushButton:hover {
    background-color: #2563eb;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

QPushButton:disabled {
    background-color: #27272a;
    color: #52525b;
}

#applyBtn {
    background-color: #10b981;
}

#applyBtn:hover {
    background-color: #059669;
}

#applyBtn:disabled {
    background-color: #27272a;
    color: #52525b;
}

#deleteBtn {
    background-color: #ef4444;
}

#deleteBtn:hover {
    background-color: #dc2626;
}

#customMaskBtn {
    background-color: #f59e0b;
}

#customMaskBtn:hover {
    background-color: #d97706;
}

QLineEdit, QComboBox {
    background-color: #18181b;
    color: white;
    border: 1px solid #3f3f46;
    border-radius: 8px;
    padding: 10px;
    font-size: 14px;
}

QLineEdit:focus, QComboBox:focus {
    border: 1px solid #3b82f6;
    background-color: #27272a;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #18181b;
    color: white;
    selection-background-color: #3b82f6;
    border: 1px solid #3f3f46;
}

QLabel {
    font-size: 14px;
}

#titleLabel {
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
    letter-spacing: 1px;
}

#subtitleLabel {
    font-size: 14px;
    color: #a1a1aa;
    margin-bottom: 20px;
}

#imageFrame {
    background-color: #18181b;
    border: 2px dashed #3f3f46;
    border-radius: 16px;
    color: #71717a;
    font-size: 16px;
}

QProgressBar {
    border: 1px solid #3f3f46;
    border-radius: 8px;
    background-color: #18181b;
    text-align: center;
    color: white;
    font-weight: bold;
    font-size: 12px;
}

QProgressBar::chunk {
    background-color: #3b82f6;
    border-radius: 6px;
}

QTabWidget::pane {
    border: 1px solid #3f3f46;
    border-radius: 8px;
    background-color: #121212;
    top: -1px;
}
QTabBar::tab {
    background-color: #18181b;
    color: #a1a1aa;
    padding: 10px 20px;
    min-width: 160px;
    border: 1px solid #3f3f46;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    margin-right: 5px;
    font-weight: bold;
}
QTabBar::tab:selected {
    background-color: #3b82f6;
    color: white;
    border-bottom-color: #3b82f6;
}

QListWidget {
    border: 1px solid #3f3f46;
    background-color: #18181b;
    color: white;
    border-radius: 8px;
    padding: 5px;
}
QListWidget::item {
    padding: 12px;
    border-bottom: 1px solid #27272a;
    font-size: 13px;
}
QListWidget::item:selected {
    background-color: #2563eb;
    border-radius: 6px;
}
"""

class EnchanterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.original_img = None
        self.mask_img = None
        self.session = None
        self.current_model_name = ""
        self.thread = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HyperOS Lock Screen Enchanter')
        self.setFixedSize(1000, 920)
        self.setStyleSheet(QSS)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 20, 30, 20)
        
        title = QLabel(_("HyperOS Enchanter"), self)
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        subtitle = QLabel(_("Создавайте идеальные обои и управляйте темами"), self)
        subtitle.setObjectName("subtitleLabel")
        subtitle.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle)
        
        # Tabs
        self.tabs = QTabWidget()
        self.tab_gen = QWidget()
        self.tab_man = QWidget()
        
        self.tabs.addTab(self.tab_gen, _("🎨 Создание обоев"))
        self.tabs.addTab(self.tab_man, _("⚙️ Менеджер тем"))
        
        self.tab_set = QWidget()
        self.tabs.addTab(self.tab_set, "🛠️ Настройки / Settings" if SETTINGS.get("lang", "ru") == "ru" else "🛠️ Settings")
        self.setup_set_tab()

        main_layout.addWidget(self.tabs)
        
        self.setup_gen_tab()
        self.setup_man_tab()
        
        self.setLayout(main_layout)
        
    def setup_gen_tab(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        self.lbl_image = QLabel(_("Нажмите 'Выбрать фото' или перетащите сюда"), self)
        self.lbl_image.setObjectName("imageFrame")
        self.lbl_image.setAlignment(Qt.AlignCenter)
        self.lbl_image.setFixedSize(400, 400)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 4)
        self.lbl_image.setGraphicsEffect(shadow)
        
        # Container to center image
        img_container = QHBoxLayout()
        img_container.addWidget(self.lbl_image, alignment=Qt.AlignCenter)
        layout.addLayout(img_container)
        
        lbl_model = QLabel("Нейросеть (если горизонт обрезается, смените модель):", self)
        lbl_model.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_model)
        
        self.combo_model = QComboBox(self)
        self.combo_model.addItems([
            _("isnet-general-use (По умолчанию, высокая детализация)"),
            _("u2net (Универсальная, лучше ловит пейзажи и горизонты)"),
            _("birefnet-general (Новейшая, очень точная)"),
            _("u2net_human_seg (Только люди)")
        ])
        self.combo_model.currentIndexChanged.connect(self.on_model_change)
        layout.addWidget(self.combo_model)
        
        btn_layout = QHBoxLayout()
        self.btn_select = QPushButton(' Выбрать фото')
        self.btn_select.setCursor(Qt.PointingHandCursor)
        self.btn_select.clicked.connect(self.select_photo)
        btn_layout.addWidget(self.btn_select)
        
        self.btn_custom_mask = QPushButton(' Своя маска')
        self.btn_custom_mask.setObjectName("customMaskBtn")
        self.btn_custom_mask.setCursor(Qt.PointingHandCursor)
        self.btn_custom_mask.clicked.connect(self.select_custom_mask)
        self.btn_custom_mask.setEnabled(False)
        btn_layout.addWidget(self.btn_custom_mask)
        
        self.btn_regen = QPushButton(' ИИ Маска')
        self.btn_regen.setCursor(Qt.PointingHandCursor)
        self.btn_regen.clicked.connect(self.generate_mask)
        self.btn_regen.setEnabled(False)
        btn_layout.addWidget(self.btn_regen)
        
        layout.addLayout(btn_layout)
        
        lbl_hint = QLabel("Имя файла обоев:", self)
        lbl_hint.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_hint)
        
        self.entry_filename = QLineEdit(self)
        self.entry_filename.setText("my_custom_wall")
        self.entry_filename.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.entry_filename)
        
        self.btn_apply = QPushButton(' Установить на телефон (Root)')
        self.btn_apply.setObjectName("applyBtn")
        self.btn_apply.setCursor(Qt.PointingHandCursor)
        self.btn_apply.clicked.connect(self.apply_to_phone)
        self.btn_apply.setEnabled(False)
        layout.addWidget(self.btn_apply)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        self.lbl_status = QLabel(_("Готово к работе. Подключите телефон по USB."), self)
        self.lbl_status.setAlignment(Qt.AlignCenter)
        self.lbl_status.setStyleSheet("color: #71717a; font-size: 13px; margin-top: 5px;")
        layout.addWidget(self.lbl_status)
        
        self.tab_gen.setLayout(layout)

    def setup_set_tab(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        lbl_lang = QLabel("Язык интерфейса / Language:")
        lbl_lang.setFont(QFont("Inter", 14, QFont.Bold))
        layout.addWidget(lbl_lang)
        
        self.combo_lang = QComboBox()
        self.combo_lang.addItems(["Русский (ru)", "English (en)"])
        if SETTINGS.get("lang", "ru") == "en":
            self.combo_lang.setCurrentIndex(1)
        self.combo_lang.currentIndexChanged.connect(self.change_language)
        layout.addWidget(self.combo_lang)
        
        lbl_social = QLabel("Мои социальные сети:")
        lbl_social.setFont(QFont("Inter", 14, QFont.Bold))
        lbl_social.setStyleSheet("margin-top: 20px;")
        layout.addWidget(lbl_social)
        
        btn_tg = QPushButton("💬 Telegram")
        btn_tg.setStyleSheet("background-color: #0088cc; font-size: 16px;")
        btn_tg.clicked.connect(lambda: webbrowser.open("https://t.me/WindyxChannel"))
        layout.addWidget(btn_tg)
        
        btn_tt = QPushButton("🎵 TikTok")
        btn_tt.setStyleSheet("background-color: #ff0050; font-size: 16px;")
        btn_tt.clicked.connect(lambda: webbrowser.open("https://tiktok.com/@windyx_edits"))
        layout.addWidget(btn_tt)
        
        layout.addStretch()
        self.tab_set.setLayout(layout)

    def change_language(self, index):
        new_lang = "en" if index == 1 else "ru"
        if SETTINGS.get("lang") != new_lang:
            SETTINGS["lang"] = new_lang
            save_settings(SETTINGS)
            QMessageBox.information(self, "Успех / Success", "Язык изменен! Перезапустите приложение. / Language changed! Restart the app.")

    def setup_man_tab(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        btn_refresh = QPushButton(_("🔄 Поиск всех тем на телефоне (Root)"))
        btn_refresh.setCursor(Qt.PointingHandCursor)
        btn_refresh.clicked.connect(self.refresh_themes)
        layout.addWidget(btn_refresh)
        
        # 3 Column Split View
        split_layout = QHBoxLayout()
        
        # Column 1 (Themes)
        left_layout = QVBoxLayout()
        lbl_themes = QLabel("Темы (папки):")
        left_layout.addWidget(lbl_themes)
        
        self.list_themes = QListWidget()
        self.list_themes.setIconSize(QSize(60, 60))
        self.list_themes.itemSelectionChanged.connect(self.on_theme_selected)
        left_layout.addWidget(self.list_themes)
        
        btn_theme_layout = QHBoxLayout()
        self.btn_rename = QPushButton(_("✏️ Изменить имя папки"))
        self.btn_rename.setCursor(Qt.PointingHandCursor)
        self.btn_rename.clicked.connect(self.rename_theme)
        btn_theme_layout.addWidget(self.btn_rename)
        
        self.btn_delete_theme = QPushButton(_("🗑️ Удалить ПАПКУ (Тему)"))
        self.btn_delete_theme.setObjectName("deleteBtn")
        self.btn_delete_theme.setCursor(Qt.PointingHandCursor)
        self.btn_delete_theme.clicked.connect(self.delete_theme)
        btn_theme_layout.addWidget(self.btn_delete_theme)
        
        left_layout.addLayout(btn_theme_layout)
        split_layout.addLayout(left_layout, 2)
        
        # Column 2 (Wallpapers)
        mid_layout = QVBoxLayout()
        lbl_walls = QLabel("Обои внутри темы:")
        mid_layout.addWidget(lbl_walls)
        
        self.list_wallpapers = QListWidget()
        self.list_wallpapers.setIconSize(QSize(60, 60))
        self.list_wallpapers.itemSelectionChanged.connect(self.on_wallpaper_selected)
        mid_layout.addWidget(self.list_wallpapers)
        
        self.btn_delete_wall = QPushButton(_("✂️ Удалить только ФОТО"))
        self.btn_delete_wall.setObjectName("customMaskBtn")
        self.btn_delete_wall.setCursor(Qt.PointingHandCursor)
        self.btn_delete_wall.clicked.connect(self.delete_wallpaper)
        mid_layout.addWidget(self.btn_delete_wall)
        
        self.btn_rename_wall = QPushButton(_("✏️ Переименовать фото"))
        self.btn_rename_wall.setCursor(Qt.PointingHandCursor)
        self.btn_rename_wall.clicked.connect(self.rename_wallpaper)
        mid_layout.addWidget(self.btn_rename_wall)
        
        split_layout.addLayout(mid_layout, 2)
        
        # Column 3 (Preview)
        right_layout = QVBoxLayout()
        lbl_preview = QLabel("Предпросмотр (Оригинал + Маска):")
        lbl_preview.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(lbl_preview)
        
        self.lbl_man_preview = QLabel(_("Выберите обои\nв левом списке\nдля просмотра"))
        self.lbl_man_preview.setObjectName("imageFrame")
        self.lbl_man_preview.setAlignment(Qt.AlignCenter)
        self.lbl_man_preview.setFixedSize(280, 280)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 2)
        self.lbl_man_preview.setGraphicsEffect(shadow)
        
        right_layout.addWidget(self.lbl_man_preview, alignment=Qt.AlignTop | Qt.AlignHCenter)
        right_layout.addStretch()
        
        split_layout.addLayout(right_layout, 2)
        
        layout.addLayout(split_layout)
        self.tab_man.setLayout(layout)

    # ===============================
    # TAB 2: MANAGER LOGIC
    # ===============================
    def refresh_themes(self):
        self.list_themes.clear()
        self.list_wallpapers.clear()
        self.lbl_man_preview.setText(_("Выберите обои\nв левом списке\nдля просмотра"))
        self.lbl_man_preview.setStyleSheet("")
        
        adb_check = self.run_adb("devices").stdout
        if "device" not in adb_check.split("\n")[1]:
            QMessageBox.critical(self, _("Ошибка ADB"), _("Телефон не подключен или выключена отладка по USB."))
            return

        loading = LoadingDialog(_("Поиск тем на устройстве..."), self)
        loading.show()
        QApplication.processEvents()

        try:
            self.run_su("mount -o remount,rw /product")
            res = self.run_su("ls /product/media/wallpaper/wallpaper_group/")
            folders = [f for f in res.stdout.split() if f.strip()]
            
            if not folders:
                loading.close()
                QMessageBox.information(self, _("Пусто"), _("Папок с темами не найдено."))
                return
                
            for folder in folders:
                loading.lbl.setText(f"Чтение темы: {folder}")
                QApplication.processEvents()
                
                res_config = self.run_su(f"cat /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
                try:
                    config = json.loads(res_config.stdout)
                    title = config.get("title", "Unknown Title")
                    count = config.get("count", 0)
                    
                    item_text = f"{title} [{count} шт.]\n{folder}"
                    item = QListWidgetItem(item_text)
                    item.setData(Qt.UserRole, folder)
                    item.setData(Qt.UserRole + 1, config)
                    
                    wallpapers = config.get("wallpapers", [])
                    if wallpapers:
                        icon_path = wallpapers[0].get("originPath", "").replace("./", "")
                        if icon_path:
                            if not os.path.exists(".cache"):
                                os.makedirs(".cache")
                            cache_name = f"theme_{folder}_thumb.jpg"
                            cache_path = os.path.join(".cache", cache_name)
                            
                            if os.path.exists(cache_path):
                                item.setIcon(QIcon(cache_path))
                            else:
                                self.run_su(f"cp /product/media/wallpaper/wallpaper_group/{folder}/{icon_path} /sdcard/Download/temp_icon.jpg")
                                self.run_adb("pull", "/sdcard/Download/temp_icon.jpg", "temp_icon.jpg")
                                self.run_su("rm /sdcard/Download/temp_icon.jpg")
                                
                                if os.path.exists("temp_icon.jpg"):
                                    try:
                                        img = Image.open("temp_icon.jpg").convert("RGB")
                                        img.thumbnail((120, 120))
                                        img.save(cache_path)
                                        item.setIcon(QIcon(cache_path))
                                    except Exception as e:
                                        print(f"Icon error: {e}")
                                    
                                    try: os.remove("temp_icon.jpg")
                                    except: pass
                                    
                    self.list_themes.addItem(item)
                except Exception as e:
                    item = QListWidgetItem(f"ОШИБКА JSON\n{folder}")
                    item.setData(Qt.UserRole, folder)
                    self.list_themes.addItem(item)
        finally:
            loading.close()

    def on_theme_selected(self):
        self.list_wallpapers.clear()
        self.lbl_man_preview.setText(_("Выберите обои\nв левом списке\nдля просмотра"))
        self.lbl_man_preview.setStyleSheet("")
        
        item = self.list_themes.currentItem()
        if not item: return
        
        folder = item.data(Qt.UserRole)
        config = item.data(Qt.UserRole + 1)
        if not config: return
        
        wallpapers = config.get("wallpapers", [])
        if not wallpapers: return
        
        loading = LoadingDialog(_("Загрузка миниатюр обоев..."), self)
        loading.show()
        QApplication.processEvents()
        
        try:
            for idx, wp in enumerate(wallpapers):
                loading.lbl.setText(f"Скачивание иконки {idx+1}/{len(wallpapers)}...")
                QApplication.processEvents()
                
                path = wp.get("originPath", "Unknown File")
                w_item = QListWidgetItem(f"Слайд {idx + 1}:\n{path}")
                w_item.setData(Qt.UserRole, idx)
                
                icon_path = path.replace("./", "")
                if icon_path and icon_path != "Unknown File":
                    if not os.path.exists(".cache"):
                        os.makedirs(".cache")
                    safe_icon = icon_path.replace("/", "_").replace("\\", "_")
                    cache_name = f"wall_{folder}_{safe_icon}_thumb.jpg"
                    cache_path = os.path.join(".cache", cache_name)
                    
                    if os.path.exists(cache_path):
                        w_item.setIcon(QIcon(cache_path))
                    else:
                        self.run_su(f"cp /product/media/wallpaper/wallpaper_group/{folder}/{icon_path} /sdcard/Download/temp_wall_icon.jpg")
                        self.run_adb("pull", "/sdcard/Download/temp_wall_icon.jpg", "temp_wall_icon.jpg")
                        self.run_su("rm /sdcard/Download/temp_wall_icon.jpg")
                        
                        if os.path.exists("temp_wall_icon.jpg"):
                            try:
                                img = Image.open("temp_wall_icon.jpg").convert("RGB")
                                img.thumbnail((120, 120))
                                img.save(cache_path)
                                w_item.setIcon(QIcon(cache_path))
                            except Exception as e:
                                print(f"Wall Icon error: {e}")
                            
                            try: os.remove("temp_wall_icon.jpg")
                            except: pass
                            
                self.list_wallpapers.addItem(w_item)
                
        finally:
            loading.close()

    def on_wallpaper_selected(self):
        item_theme = self.list_themes.currentItem()
        item_wall = self.list_wallpapers.currentItem()
        
        if not item_theme or not item_wall:
            self.lbl_man_preview.setText(_("Выберите обои\nв левом списке\nдля просмотра"))
            self.lbl_man_preview.setPixmap(QPixmap())
            self.lbl_man_preview.setStyleSheet("")
            return
            
        folder = item_theme.data(Qt.UserRole)
        config = item_theme.data(Qt.UserRole + 1)
        idx = item_wall.data(Qt.UserRole)
        
        wallpapers = config.get("wallpapers", [])
        if idx >= len(wallpapers): return
        
        wp = wallpapers[idx]
        orig_path = wp.get("originPath", "").replace("./", "")
        mask_path = wp.get("maskPath", "").replace("./", "")
        
        if not orig_path:
            self.lbl_man_preview.setText(_("Файл не указан\nв JSON"))
            return
            
        loading = LoadingDialog(_("Сборка полноформатного\nпредпросмотра с маской..."), self)
        loading.show()
        QApplication.processEvents()
        
        try:
            self.run_su(f"cp /product/media/wallpaper/wallpaper_group/{folder}/{orig_path} /sdcard/Download/temp_orig.jpg")
            self.run_adb("pull", "/sdcard/Download/temp_orig.jpg", "temp_orig.jpg")
            self.run_su("rm /sdcard/Download/temp_orig.jpg")
            
            has_mask = False
            if mask_path:
                self.run_su(f"cp /product/media/wallpaper/wallpaper_group/{folder}/{mask_path} /sdcard/Download/temp_mask.jpg")
                self.run_adb("pull", "/sdcard/Download/temp_mask.jpg", "temp_mask.jpg")
                self.run_su("rm /sdcard/Download/temp_mask.jpg")
                if os.path.exists("temp_mask.jpg"):
                    has_mask = True
                    
            if not os.path.exists("temp_orig.jpg"):
                self.lbl_man_preview.setText(_("Файл не найден\nна устройстве"))
                return
                
            try:
                orig_img = Image.open("temp_orig.jpg").convert('RGBA')
                if has_mask:
                    mask_img = Image.open("temp_mask.jpg").convert('L')
                    if mask_img.size != orig_img.size:
                        mask_img = mask_img.resize(orig_img.size, Image.Resampling.LANCZOS)
                    
                    overlay = Image.new('RGBA', orig_img.size, (239, 68, 68, 255))
                    mask_50 = mask_img.point(lambda p: int(p * 0.5))
                    orig_img.paste(overlay, (0, 0), mask=mask_50)
                    
                preview = orig_img.copy()
                preview.thumbnail((280, 280), Image.Resampling.LANCZOS)
                
                data = preview.tobytes("raw", "RGBA")
                qim = QImage(data, preview.width, preview.height, QImage.Format_RGBA8888)
                pix = QPixmap.fromImage(qim)
                
                self.lbl_man_preview.setPixmap(pix)
                self.lbl_man_preview.setStyleSheet("border: none; background-color: transparent;")
            except Exception as e:
                self.lbl_man_preview.setText(_("Ошибка загрузки\nпревью"))
                print(f"Preview error: {e}")
                
            try:
                if os.path.exists("temp_orig.jpg"): os.remove("temp_orig.jpg")
                if os.path.exists("temp_mask.jpg"): os.remove("temp_mask.jpg")
            except: pass
        finally:
            loading.close()

    def delete_wallpaper(self):
        item_theme = self.list_themes.currentItem()
        item_wall = self.list_wallpapers.currentItem()
        
        if not item_theme or not item_wall:
            QMessageBox.warning(self, _("Внимание"), _("Сначала выберите обои в центральной колонке!"))
            return
            
        folder = item_theme.data(Qt.UserRole)
        config = item_theme.data(Qt.UserRole + 1)
        idx = item_wall.data(Qt.UserRole)
        
        wallpapers = config.get("wallpapers", [])
        if idx >= len(wallpapers): return
        
        wp = wallpapers[idx]
        orig_path = wp.get("originPath", "").replace("./", "")
        mask_path = wp.get("maskPath", "").replace("./", "")
        thumb_path = wp.get("thumbPath", "").replace("./", "")
        
        reply = QMessageBox.question(self, 'Удаление', f"Удалить файл '{orig_path}' из этой темы?", QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes: return
        
        # Удаляем из конфига
        del config["wallpapers"][idx]
        config["count"] = len(config["wallpapers"])
        if "slideCount" in config:
            config["slideCount"] = config["count"]
            
        # Сохраняем и закидываем
        with open("temp_config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
            
        self.run_adb("push", "temp_config.json", "/sdcard/Download/temp_config.json")
        self.run_su(f"cp /sdcard/Download/temp_config.json /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
        self.run_su(f"chmod 644 /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
        self.run_su("rm /sdcard/Download/temp_config.json")
        try: os.remove("temp_config.json")
        except: pass
        
        # Удаляем физически
        if orig_path: self.run_su(f"rm /product/media/wallpaper/wallpaper_group/{folder}/{orig_path}")
        if mask_path: self.run_su(f"rm /product/media/wallpaper/wallpaper_group/{folder}/{mask_path}")
        if thumb_path: self.run_su(f"rm /product/media/wallpaper/wallpaper_group/{folder}/{thumb_path}")
        
        # Обновляем UI
        item_theme.setData(Qt.UserRole + 1, config)
        title = config.get("title", "Unknown")
        item_theme.setText(f"{title} [{config['count']} шт.]\n{folder}")
        self.on_theme_selected()
        
        QMessageBox.information(self, _("Успех"), _("Обои удалены из темы!"))

    def transliterate(self, text):
        cyrillic_to_latin = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
            ' ': '_'
        }
        for cyr, lat in cyrillic_to_latin.items():
            text = text.replace(cyr, lat)
        text = re.sub(r'[^a-zA-Z0-9_-]', '', text)
        return text

    def rename_theme(self):
        item = self.list_themes.currentItem()
        if not item: 
            QMessageBox.warning(self, _("Внимание"), _("Сначала выберите тему в левом списке!"))
            return
            
        folder = item.data(Qt.UserRole)
        config = item.data(Qt.UserRole + 1)
        if not config: return
        
        old_title = config.get("title", "")
        new_title, ok = QInputDialog.getText(self, _("Изменить имя темы"), "Введите новое отображаемое имя темы:", text=old_title)
        if ok and new_title.strip():
            new_title = new_title.strip()
            
            config["title"] = new_title
            config["titleResId"] = new_title
            
            with open("temp_config.json", "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
                
            self.run_adb("push", "temp_config.json", "/sdcard/Download/temp_config.json")
            self.run_su(f"cp /sdcard/Download/temp_config.json /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
            self.run_su(f"chmod 644 /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
            self.run_su("rm /sdcard/Download/temp_config.json")
            try: os.remove("temp_config.json")
            except: pass
            
            item.setData(Qt.UserRole + 1, config)
            item.setText(f"{new_title} [{config['count']} шт.]\n{folder}")
            QMessageBox.information(self, _("Успех"), f"Отображаемое имя темы успешно изменено на '{new_title}'!")

    def rename_wallpaper(self):
        item_theme = self.list_themes.currentItem()
        item_wall = self.list_wallpapers.currentItem()
        
        if not item_theme or not item_wall:
            QMessageBox.warning(self, _("Внимание"), "Сначала выберите фото в центральной колонке!")
            return
            
        folder = item_theme.data(Qt.UserRole)
        config = item_theme.data(Qt.UserRole + 1)
        idx = item_wall.data(Qt.UserRole)
        
        wallpapers = config.get("wallpapers", [])
        if idx >= len(wallpapers): return
        
        wp = wallpapers[idx]
        old_orig = wp.get("originPath", "").replace("./", "")
        old_name = old_orig.replace(".jpg", "")
        
        new_name, ok = QInputDialog.getText(self, _("Переименовать фото"), "Введите новое имя для фото (без .jpg):", text=old_name)
        if ok and new_name.strip():
            new_name = new_name.strip()
            safe_name = self.transliterate(new_name)
            
            if not safe_name:
                QMessageBox.warning(self, _("Ошибка"), _("Имя не может быть пустым после конвертации!"))
                return
                
            new_orig = f"{safe_name}.jpg"
            new_mask = f"{safe_name}_MASK.jpg"
            new_thumb = f"{safe_name}_THUMB.jpg"
            
            old_orig_path = wp.get("originPath", "").replace("./", "")
            old_mask_path = wp.get("maskPath", "").replace("./", "")
            old_thumb_path = wp.get("thumbPath", "").replace("./", "")
            
            if old_orig_path and old_orig_path != new_orig:
                self.run_su(f"mv /product/media/wallpaper/wallpaper_group/{folder}/{old_orig_path} /product/media/wallpaper/wallpaper_group/{folder}/{new_orig}")
                wp["originPath"] = f"./{new_orig}"
                
            if old_mask_path and old_mask_path != new_mask:
                self.run_su(f"mv /product/media/wallpaper/wallpaper_group/{folder}/{old_mask_path} /product/media/wallpaper/wallpaper_group/{folder}/{new_mask}")
                wp["maskPath"] = f"./{new_mask}"
                
            if old_thumb_path and old_thumb_path != new_thumb:
                self.run_su(f"mv /product/media/wallpaper/wallpaper_group/{folder}/{old_thumb_path} /product/media/wallpaper/wallpaper_group/{folder}/{new_thumb}")
                wp["thumbPath"] = f"./{new_thumb}"
                
            with open("temp_config.json", "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
                
            self.run_adb("push", "temp_config.json", "/sdcard/Download/temp_config.json")
            self.run_su(f"cp /sdcard/Download/temp_config.json /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
            self.run_su(f"chmod 644 /product/media/wallpaper/wallpaper_group/{folder}/wallpaper_config.json")
            self.run_su("rm /sdcard/Download/temp_config.json")
            try: os.remove("temp_config.json")
            except: pass
            
            self.refresh_themes()
            QMessageBox.information(self, _("Успех"), f"Фото успешно переименовано в '{safe_name}.jpg'!")

    def delete_theme(self):
        item = self.list_themes.currentItem()
        if not item: 
            QMessageBox.warning(self, _("Внимание"), _("Сначала выберите тему в левом списке!"))
            return
            
        folder = item.data(Qt.UserRole)
        reply = QMessageBox.question(self, 'Удаление темы', f"Вы точно хотите БЕЗВОЗВРАТНО удалить папку со всеми обоями внутри:\n{folder} ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.run_su(f"rm -rf /product/media/wallpaper/wallpaper_group/{folder}")
            self.refresh_themes()
            QMessageBox.information(self, _("Успех"), _("Тема удалена с устройства!"))


    # ===============================
    # TAB 1: GENERATOR LOGIC
    # ===============================
    def on_model_change(self):
        if self.image_path:
            self.lbl_status.setText(_("Модель изменена. Нажмите 'ИИ Маска' для перерисовки."))
        
    def select_photo(self):
        options = QFileDialog.Options()
        file_path, _ext = QFileDialog.getOpenFileName(self, _("Выбрать фото"), "", "Image Files (*.jpg *.jpeg *.png *.webp)", options=options)
        if not file_path:
            return
            
        self.image_path = file_path
        self.original_img = Image.open(self.image_path)
        
        # Предпросмотр оригинала сразу
        preview = self.original_img.copy()
        preview.thumbnail((400, 400))
        data = preview.tobytes("raw", "RGB" if preview.mode == "RGB" else "RGBA")
        fmt = QImage.Format_RGB888 if preview.mode == "RGB" else QImage.Format_RGBA8888
        qim = QImage(data, preview.width, preview.height, fmt)
        pix = QPixmap.fromImage(qim)
        self.lbl_image.setPixmap(pix)
        self.lbl_image.setStyleSheet("border: none; background-color: transparent;")
        
        self.btn_regen.setEnabled(True)
        self.btn_custom_mask.setEnabled(True)
        self.generate_mask()
        
    def select_custom_mask(self):
        options = QFileDialog.Options()
        file_path, _ext = QFileDialog.getOpenFileName(self, _("Выбрать свою маску"), "", "Image Files (*.jpg *.jpeg *.png)", options=options)
        if not file_path:
            return
            
        try:
            self.mask_img = Image.open(file_path).convert("L")
            self.apply_mask_preview()
            self.lbl_status.setText(_("Кастомная маска успешно загружена! Проверьте результат."))
        except Exception as e:
            QMessageBox.critical(self, _("Ошибка"), f"Не удалось загрузить маску: {str(e)}")

    def handle_stderr(self, text):
        m_percent = re.search(r'(\d+)%', text)
        if m_percent:
            val = int(m_percent.group(1))
            self.progress_bar.setValue(val)
            if not self.progress_bar.isVisible():
                self.progress_bar.setVisible(True)
                
            m_stats = re.search(r'\|\s*([\d\.]+[kMG]?/.*(?:\[.*\])?)', text)
            stats_str = f" ({m_stats.group(1).strip()})" if m_stats else ""
            
            self.lbl_status.setText(f"Скачивание модели... {val}%{stats_str}")
        QApplication.processEvents()
        
    def generate_mask(self):
        if not self.image_path:
            return
            
        model_display = self.combo_model.currentText()
        model_name = model_display.split(" ")[0]
        
        if self.session is None or self.current_model_name != model_name:
            self.lbl_status.setText(f"Подготовка модели {model_name}...")
            QApplication.processEvents()
            
            old_stderr = sys.stderr
            sys.stderr = StreamInterceptor(self.handle_stderr)
            
            try:
                from rembg import new_session
                try:
                    self.session = new_session(model_name, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
                except Exception as e:
                    print(f"[WARNING] Ошибка CUDA, переключаемся на CPU: {e}")
                    self.session = new_session(model_name, providers=["CPUExecutionProvider"])
                self.current_model_name = model_name
            finally:
                sys.stderr = old_stderr
                self.progress_bar.setVisible(False)
                self.progress_bar.setValue(0)
            
        self.lbl_status.setText(f"Генерация маски ({model_name})... Вычисляем, программа не зависла.")
        self.btn_select.setEnabled(False)
        self.btn_regen.setEnabled(False)
        self.btn_custom_mask.setEnabled(False)
        self.btn_apply.setEnabled(False)
        
        self.thread = MaskGeneratorThread(self.original_img, self.session)
        self.thread.finished.connect(self.on_mask_generated)
        self.thread.error.connect(self.on_mask_error)
        self.thread.start()
        
    def on_mask_generated(self, result):
        mask_img = result
        self.mask_img = mask_img
        
        self.apply_mask_preview()
        self.btn_select.setEnabled(True)
        self.btn_regen.setEnabled(True)
        self.btn_custom_mask.setEnabled(True)
        self.lbl_status.setText(_("Маска готова! Проверьте результат и нажмите 'Установить'."))
        
    def on_mask_error(self, err_msg):
        self.btn_select.setEnabled(True)
        self.btn_regen.setEnabled(True)
        self.btn_custom_mask.setEnabled(True)
        QMessageBox.critical(self, _("Ошибка генерации"), err_msg)
        self.lbl_status.setText(_("Ошибка генерации маски"))
        
    def apply_mask_preview(self):
        original_rgba = self.original_img.convert('RGBA')
        if self.mask_img.size != original_rgba.size:
            self.mask_img = self.mask_img.resize(original_rgba.size, Image.Resampling.LANCZOS)
            
        mask_l = self.mask_img.convert('L')
        overlay = Image.new('RGBA', original_rgba.size, (239, 68, 68, 255))
        mask_50 = mask_l.point(lambda p: int(p * 0.5))
        original_rgba.paste(overlay, (0, 0), mask=mask_50)
        
        preview = original_rgba.copy()
        preview.thumbnail((400, 400), Image.Resampling.LANCZOS)
        
        data = preview.tobytes("raw", "RGBA")
        qim = QImage(data, preview.width, preview.height, QImage.Format_RGBA8888)
        pix = QPixmap.fromImage(qim)
        
        self.lbl_image.setPixmap(pix)
        self.lbl_image.setStyleSheet("border: none; background-color: transparent;")
        
        self.btn_apply.setEnabled(True)
            
    def run_adb(self, *args):
        cmd = ["adb"] + list(args)
        print(f"[ADB EXEC] {' '.join(cmd)}")
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        if res.stdout: print(f"[ADB STDOUT] {res.stdout.strip()}")
        if res.stderr: print(f"[ADB STDERR] {res.stderr.strip()}")
        return res
        
    def run_su(self, cmd):
        full_cmd = ["adb", "shell", f"su -c '{cmd}'"]
        print(f"[SU EXEC] adb shell su -c '{cmd}'")
        res = subprocess.run(full_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        if res.stdout: print(f"[SU STDOUT] {res.stdout.strip()}")
        if res.stderr: print(f"[SU STDERR] {res.stderr.strip()}")
        return res

    def apply_to_phone(self):
        raw_name = self.entry_filename.text().strip()
        if not raw_name:
            raw_name = "custom_wall"
            
        translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch',
            'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
            ' ': '_'
        }
        
        safe_name = "".join(translit_dict.get(c, c) for c in raw_name)
        filename = re.sub(r'[^a-zA-Z0-9_-]', '_', safe_name)
        filename = re.sub(r'_+', '_', filename).strip('_')
        
        if not filename:
            filename = "custom_wall"
            
        self.entry_filename.setText(filename)
        print(f"\n=== НАЧАЛО ЗАГРУЗКИ: {filename} ===")
            
        self.lbl_status.setText(_("Копирование на телефон... Подтвердите Root-доступ на экране!"))
        QApplication.processEvents()
        
        print("[INFO] Ожидание устройства (adb wait-for-device)...")
        self.run_adb("wait-for-device")
        
        adb_check = self.run_adb("devices").stdout
        if "device" not in adb_check.split("\n")[1]:
            QMessageBox.critical(self, _("Ошибка ADB"), _("Телефон не подключен или выключена отладка по USB."))
            self.lbl_status.setText(_("Ошибка подключения ADB"))
            return

        self.run_su("mount -o remount,rw /product")
        
        res = self.run_su("ls /product/media/wallpaper/wallpaper_group/")
        folders = res.stdout.split()
        target_folder = None
        for f in folders:
            if f.endswith("_CustomWallpapers"):
                target_folder = f
                break
                
        if not target_folder:
            used = set()
            for f in folders:
                m = re.match(r"^(\d{2})_", f)
                if m: used.add(int(m.group(1)))
            num = 1
            while num in used: num += 1
            target_folder = f"{num:02d}_CustomWallpapers"
            
        target_path = f"/product/media/wallpaper/wallpaper_group/{target_folder}"
        self.run_su(f"mkdir -p {target_path}")
        
        local_orig = f"temp_{filename}.jpg"
        local_mask = f"temp_{filename}_MASK.jpg"
        
        if self.original_img.mode in ("RGBA", "P"):
            self.original_img.convert("RGB").save(local_orig, "JPEG", quality=95)
        else:
            self.original_img.save(local_orig, "JPEG", quality=95)
            
        self.mask_img.convert("RGB").save(local_mask, "JPEG", quality=95)
        
        self.run_adb("push", local_orig, f"/sdcard/Download/{filename}.jpg")
        self.run_adb("push", local_mask, f"/sdcard/Download/{filename}_MASK.jpg")
        
        self.run_su(f"cp /sdcard/Download/{filename}.jpg {target_path}/{filename}.jpg")
        self.run_su(f"cp /sdcard/Download/{filename}_MASK.jpg {target_path}/{filename}_MASK.jpg")
        self.run_su(f"chmod 644 {target_path}/{filename}.jpg")
        self.run_su(f"chmod 644 {target_path}/{filename}_MASK.jpg")
        
        self.run_su(f"cp {target_path}/wallpaper_config.json /sdcard/Download/wallpaper_config.json")
        res_pull = self.run_adb("pull", "/sdcard/Download/wallpaper_config.json", "local_config.json")
        
        config_updated = False
        if os.path.exists("local_config.json"):
            try:
                with open("local_config.json", "r", encoding="utf-8") as f:
                    config = json.load(f)
                config_updated = True
            except: pass
            
        if not config_updated:
            if os.path.exists(("scripts/assets/template.json" if os.path.exists("scripts/assets/template.json") else "template.json")):
                with open(("scripts/assets/template.json" if os.path.exists("scripts/assets/template.json") else "template.json"), "r", encoding="utf-8") as f:
                    config = json.load(f)
            else:
                config = {
                    "title": "Custom Wallpapers",
                    "titleResId": "Custom",
                    "cardType": 1,
                    "count": 0,
                    "slideCount": 0,
                    "randomOrder": False,
                    "wallpapers": []
                }
            
        config["count"] = config.get("count", 0) + 1
        if "slideCount" in config:
            config["slideCount"] = config["count"]
            
        new_wp = {
            "thumbPath": f"./{filename}.jpg",
            "originPath": f"./{filename}.jpg",
            "maskPath": f"./{filename}_MASK.jpg",
            "mattingMode": 2,
            "type": "wallpaper"
        }
        
        if "wallpapers" not in config:
            config["wallpapers"] = []
        config["wallpapers"].append(new_wp)
        
        with open("local_config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
            
        self.run_adb("push", "local_config.json", "/sdcard/Download/wallpaper_config.json")
        self.run_su(f"cp /sdcard/Download/wallpaper_config.json {target_path}/wallpaper_config.json")
        self.run_su(f"chmod 644 {target_path}/wallpaper_config.json")
        
        self.run_su("rm /sdcard/Download/wallpaper_config.json")
        self.run_su(f"rm /sdcard/Download/{filename}.jpg")
        self.run_su(f"rm /sdcard/Download/{filename}_MASK.jpg")
        try:
            os.remove(local_orig)
            os.remove(local_mask)
            if os.path.exists("local_config.json"):
                os.remove("local_config.json")
        except: pass
        
        QMessageBox.information(self, _("Успех!"), f"Обои '{filename}' успешно установлены в HyperOS!\nПапка: {target_folder}")
        self.lbl_status.setText(_("Успешно завершено! Можно выбрать новое фото."))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EnchanterApp()
    ex.show()
    sys.exit(app.exec_())

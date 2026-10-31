from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Đặt màu nền tối chủ đạo cho ứng dụng (xám đen hiện đại)
Window.clearcolor = (0.05, 0.08, 0.10, 1)

class DashboardCard(Button):
    """Tạo các ô card bo góc giống như trong ảnh mẫu"""
    def __init__(self, title, subtitle, bg_color=(0.10, 0.14, 0.18, 1), **kwargs):
        super().__init__(**kwargs)
        self.text = '' # Không dùng text mặc định của Button để tự custom giao diện
        self.background_color = (0, 0, 0, 0) # Trong suốt để dùng canvas vẽ hình nền bo góc
        self.background_normal = ''
        
        # Layout bên trong card
        self.layout = BoxLayout(orientation='vertical', padding=16, spacing=8)
        
        self.title_label = Label(
            text=title,
            font_size=18,
            bold=True,
            halign='left',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        
        self.sub_label = Label(
            text=subtitle,
            font_size=13,
            halign='left',
            valign='middle',
            color=(0.6, 0.65, 0.7, 1)
        )
        self.sub_label.bind(size=self.sub_label.setter('text_size'))
        
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.sub_label)
        self.add_widget(self.layout)
        
        # Vẽ khung card bo góc
        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[16])
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.layout.pos = self.pos
        self.layout.size = self.size

class EraserApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=16, spacing=16)
        
        # --- PHẦN HEADER (Tiêu đề ứng dụng) ---
        header_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.18), spacing=4)
        
        title = Label(
            text="AI WATERMARK ERASER",
            font_size=22,
            bold=True,
            halign='left',
            color=(0.2, 0.9, 0.6, 1) # Xanh lá điểm nhấn giống ảnh
        )
        title.bind(size=title.setter('text_size'))
        
        subtitle = Label(
            text="AI offline · không tải lên Internet",
            font_size=13,
            halign='left',
            color=(0.6, 0.7, 0.75, 1)
        )
        subtitle.bind(size=subtitle.setter('text_size'))
        
        header_layout.add_widget(title)
        header_layout.add_widget(subtitle)
        root.add_widget(header_layout)
        
        # --- PHẦN GRID (Các mảng chức năng chia đôi) ---
        grid = GridLayout(cols=2, spacing=12, size_hint=(1, 0.65))
        
        # 1. Ô Xóa ảnh
        card_img = DashboardCard(
            "Xóa ảnh", 
            "JPG, PNG, WebP\n+ Bộ lọc & Chỉnh sửa",
            bg_color=(0.10, 0.15, 0.20, 1)
        )
        card_img.bind(on_press=lambda x: self.on_card_click("Xóa & Chỉnh sửa Ảnh"))
        grid.add_widget(card_img)
        
        # 2. Ô Xóa video
        card_vid = DashboardCard(
            "Xóa video", 
            "MP4 · Watermark cố định & di chuyển",
            bg_color=(0.10, 0.15, 0.20, 1)
        )
        card_vid.bind(on_press=lambda x: self.on_card_click("Xóa & Chỉnh sửa Video"))
        grid.add_widget(card_vid)
        
        # 3. Ô Lịch sử
        card_history = DashboardCard(
            "Lịch sử", 
            "Ảnh và video đã lưu",
            bg_color=(0.10, 0.15, 0.20, 1)
        )
        card_history.bind(on_press=lambda x: self.on_card_click("Lịch sử dự án"))
        grid.add_widget(card_history)
        
        # 4. Ô Hướng dẫn
        card_guide = DashboardCard(
            "Hướng dẫn", 
            "Mẹo sử dụng offline",
            bg_color=(0.10, 0.15, 0.20, 1)
        )
        card_guide.bind(on_press=lambda x: self.on_card_click("Hướng dẫn sử dụng"))
        grid.add_widget(card_guide)
        
        root.add_widget(grid)
        
        # --- PHẦN FOOTER (Cài đặt tràn ngang bên dưới) ---
        footer_layout = BoxLayout(size_hint=(1, 0.12))
        card_settings = DashboardCard(
            "Cài đặt", 
            "Tùy chỉnh hiệu năng & lưu trữ",
            bg_color=(0.10, 0.15, 0.20, 1)
        )
        card_settings.bind(on_press=lambda x: self.on_card_click("Cài đặt hệ thống"))
        footer_layout.add_widget(card_settings)
        root.add_widget(footer_layout)
        
        return root

    def on_card_click(self, name):
        print(f"Đã chọn mở chức năng: {name}")

if __name__ == '__main__':
    EraserApp().run()


from fpdf import FPDF
class PDF(FPDF):    
    pass
    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)
    def texts(self,text):
        self.set_xy(10.0, 80.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,text)
    def titles(self, title):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)


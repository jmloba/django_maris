import subprocess
from app_task.models import TaskTable
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4,A3, landscape
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Preformatted, XPreformatted 
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle

from reportlab.lib.units import inch

def flip_image(image_path):
    img = Image.open(image_path)
    out = img.transpose(Image.FLIP_TOP_BOTTOM)
    
    return out

def logo_draw(c,x1,y1):
    #  logo print ---
    logo_image=flip_image('c:\\reportlab\\logo\\logo_red.png')
    c.drawImage(ImageReader(logo_image), x1*inch, y1*inch, width=50, height=50)
     
def draw_borderrectangle(c,x1,y1,x2,y2,stroke,hexcolor,radius):
    # draw the rectangle
    c.setLineWidth(stroke)
    c.setStrokeColor(HexColor(hexcolor))
    c.roundRect(x1 * inch, y1 * inch, x2 * inch, y2 * inch, radius=radius)     
def draw_line(c,x1,y1,x2,y2,stroke,hexcolor):
    # line
    c.setStrokeColor(HexColor(hexcolor))
    c.setLineWidth(stroke)  # line width
    c.line(x1 * inch, y1 * inch, x2 * inch, y2 * inch,)      
def print_table_header(c,y1):    
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 14)
  c.drawString( -.5  * inch, y1 * inch, 'MFO')
  c.drawString( 1.7  * inch, y1 * inch, 'MFO sub')
  
def print_template(c , pageno):
    logo_draw(c,x1=-.5,y1=-.5)
    color='#A294F9'
    draw_borderrectangle(c,x1=-.8, y1=1,x2=16.2,y2=9,stroke=1,hexcolor=color,radius=.1)
    
    
    color='#A8E6CF'
    draw_line(c, x1=0,y1=.5, x2=15,y2=.5,stroke=5,hexcolor=color,)
    # rectangle_address(c)
    # # draw_watermark(c)
    # import_date(c)
    print_table_header(c,y1=1.2)
    # print_pageno(c,7.5,pageno)
    # reference_code_print(c,invoice_no)
    pageno+=1
    return c,pageno  
def print_description(c,mdesc,y_axis):
   
  print(f'\n\ndescription to print -->> : {mdesc}')
  textobject = c.beginText(5*inch, y_axis*inch)
  for line in mdesc.splitlines(True):
      textobject.textLine(line.rstrip())
  c.drawText(textobject)
   
def print_body_data(c,row_data, y_axis,page_total):
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)

  print(f'\n\n row data : \n {row_data}')
  m_mfo = row_data['mfo__name']
  m_mfosub = row_data['mfosub__name']

  
  c.drawString(-.5*inch, y_axis * inch, m_mfo)
  c.drawString(1.7*inch, y_axis * inch, m_mfosub)
  m_desc = row_data['task_desc']

  print_description(c,m_desc,y_axis)



  return page_total

def print_pagetotal(c,page_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,9.65*inch, "Page Total :")

    c.setFillColor('#884A39')
    c.drawString(2*inch,9.65*inch, str(page_total))
def print_page_grand_total(c, g_total):
    c.setFillColor('#071952')
    c.setFont("Helvetica", 15)
    c.drawString(-.5*inch,9.9*inch, "Grand Total :")
    c.setFillColor('#fd1f1f')
    c.drawString(2*inch,9.9*inch, str(g_total))      

    
def print_tasknow(pdf_path,tasklist):
  mypath = pdf_path
  rowcount =1
  global mtotals 
  mtotals= 0.0
  y_axis = 6.0
  global  page_total 
  page_total = 0.0
  g_total = 0.0
  pageno =1
  # note : bottomup=0 x,y axis begins at the left0
  c=canvas.Canvas(pdf_path,
    pagesize=(landscape(A3)), 
    bottomup=0
                  )
  c.translate(inch, inch)  # x y position using inch  
  c,pageno = print_template(c,pageno,)  
  
  for row_number, row_data in enumerate(tasklist):
    # print_letter_heading(c)
    rowcount += 1
    page_total = print_body_data(c, row_data ,y_axis, page_total)
    y_axis += 0.3

    if rowcount > 3 :
        # print_pagetotal(c,page_total)
        g_total += page_total
        page_total = 0.0
        c.showPage()
        c.translate(inch, inch)
        c,pageno = print_template(c,pageno)  # load template
 
        y_axis = 6.0
        rowcount = 1


  g_total += page_total
  # print_pagetotal(c,page_total)
  # print_page_grand_total(c,g_total)
  c.showPage()
  c.save()
  # to open pdf
  subprocess.Popen([mypath], shell=True)

def get_data_to_print(request):
  mdata = TaskTable.objects.filter(user=request.user).values('mfo__name','mfosub__name', 'mfosub2__name', 'task_desc')
  task_list= list(mdata)   
  print(f'\n\ntasklist : \n\n {task_list}')
  return task_list

def get_task_to_print(request): 
  tasklist=get_data_to_print(request)

  
  print(f'\n\n**task to print : {tasklist}')
  pdf_path = 'c:/reportlab/task.pdf'
  print_tasknow(pdf_path,tasklist)


  
  
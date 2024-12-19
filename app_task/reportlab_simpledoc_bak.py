import subprocess
from app_task.models import TaskTable
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4,A3, landscape
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image

def get_data_to_print(request):
  mdata = TaskTable.objects.filter(user=request.user).values('mfo__name','mfosub__name', 'mfosub2__name', 'task_desc')
  task_list = list(mdata)   
  print(f'\n\ntasklist : \n\n {task_list}')
  return task_list
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
# def text_to_box(text):
   
def put_in_box(c,text,x_axis,y_axis,box_width,max_length_desc):
  new_length = max_length_desc
  n = 40
  list=[text[i:i+n] for i in range(0, len(text), n)]

  # compare max length of text
  if len(list) > new_length:
    new_length = len(list)
  else:
    new_length = max_length_desc

  print(f'split list :\n {list}')

  text_object = c.beginText()
  text_object.setTextOrigin(5*inch,y_axis*inch)
  text_object.setFillColor(colors.blue)

 #draw rectangle
  c.setLineWidth(1)
  c.setFillColor(HexColor('#EBEDC5')) #choose fill colour

  c.rect(
    (x_axis - .1)*inch,  (y_axis - 0.2)*inch,
    box_width*inch,      ((len(list)/5.3))*inch, 
          fill=1) 
  

  for i in range (len(list)):
    text_object.textLine(list[i])   
  c.drawText(text_object)    
  

  return new_length

def print_body_data(c, row_data ,y_axis):
  
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)

  print(f'\n\n row data : \n {row_data}')

  m_mfo = row_data['mfo__name']
  c.drawString(-.5*inch, y_axis * inch, m_mfo)
  m_mfosub = row_data['mfosub__name']
  
  c.drawString(1.7*inch, y_axis * inch, m_mfosub)

  m_desc = row_data['task_desc']
  x_axis=5
  box_width=3
  max_length_desc=0

  len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc)
  
  print(f'list : {len_list}')
  return len_list

def print_now(pdf_path, tasklist):
  pageno =1
  rowcount =1
  page_total =0
  c=canvas.Canvas(pdf_path, bottomup=0,  pagesize=(landscape(A3)), )
  
  c.translate(inch, inch)  # x y position using inch  
  # c.drawImage("assets/images/logo.jpg",50,50, width=100,height=100)
  c,pageno = print_template(c,pageno,)  
  y_axis = 1.5

  for row_number, row_data in enumerate(tasklist):
    rowcount += 1
    text = row_data['task_desc']

    len_mdesc=print_body_data(c, row_data ,y_axis )
    box_length = len_mdesc/6
    print(f'length of list : {len_mdesc}')
    y_axis += 0.35 + box_length
    

    if (rowcount > 5 ) or y_axis>7:
      rowcount = 1
      c.showPage()      
      c.translate(inch, inch)  # x y position using inch  
      c,pageno = print_template(c,pageno)  # load template
      y_axis = 1.5



  c.showPage()
  c.save()
  subprocess.Popen(pdf_path, shell=True)


def using_simpledoc(request):
  tasklist=get_data_to_print(request)
  print(f'tasklist: {tasklist}')
  pdf_path = 'task.pdf'
  print_now(pdf_path, tasklist)
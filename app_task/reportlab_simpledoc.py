import subprocess
from app_task.models import TaskTable
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4,A3, landscape
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.pdfbase import pdfmetrics

def get_data_to_print(request):
  mdata = TaskTable.objects.filter(user=request.user).values('mfo__name','mfosub__name', 'mfosub2__name', 'task_desc','task_ref')

  
  task_list = list(mdata)   
  print(f'\n\ntasklist  plus details ##########: \n\n {task_list}')
  return task_list
def flip_image(image_path):
    img = Image.open(image_path)
    out = img.transpose(Image.FLIP_TOP_BOTTOM)
    
    return out
def logo_draw(c,x1,y1):
    #  logo print ---
    logo_image=flip_image('c:\\reportlab\\logo\\logo_red.png')
    logo_image=flip_image('assets/images/cavite_logo.jpg')


    c.drawImage(ImageReader(logo_image), x1*inch, y1*inch, width=70, height=70)

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

def print_report_owner(request,c,  x_axis,  y_axis):
  c.setFont("Helvetica", 12)
  text=f'I, {request.user} Social Welfare Assistant of the OFFICE OF THE PROVINCIAL GOVERNOR - OFFICE OF THE PROVINCIAL PERSONS WITH DISABILITY AFFAIRS OFFICER  of the provincial government of Cavite commit to deliver and agree to be rated on the attainment of the following targets in accordance with the intended measures for the perios of ________________________' 
  # list=[text[i:i+n] for i in range(0, len(text), n)]
  list=[
    f'I, {request.user} Social Welfare Assistant of the OFFICE OF THE PROVINCIAL GOVERNOR - OFFICE OF THE PROVINCIAL PERSONS  WITH DISABILITY AFFAIRS OFFICER  ',
    f'of the provincial government of Cavite commit to deliver and agree to be rated on the attainment of the following targets in accordance with the intended measures for the period of ________',
    f'']
  n = 120
  box_width=14
  
  text_object = c.beginText()
  text_object.setTextOrigin(x_axis*inch,y_axis*inch)
  text_object.setFillColor(colors.blue)
  text_object.setFillColor(HexColor('#011E1F'))
   #draw rectangle
  c.setLineWidth(1)

  # c.setFillColor(HexColor('#ECECEC')) #choose fill colour
  # c.rect(
  #   (x_axis - .1)*inch,  (y_axis - 0.2)*inch,
  #   box_width*inch,      ((len(list)/3))*inch, 
  #         fill=1) 
  

  for i in range (len(list)):
    text_object.textLine(list[i])   
  c.drawText(text_object)    
# joven  

  
def print_template(request, c , pageno,border_color,border_box_color,fill_box_color1):
    logo_draw(c,x1=-.7,y1=-.5)
  
    draw_borderrectangle(c,x1=-.8, y1=1,x2=16.2,y2=9,stroke=1,hexcolor=border_color,radius=.1)
    
    print_report_title(c,y1=-.5)
    color='#D9D9D9'
    draw_line(c,  x1=3.5,  y1=-.3, 
                  x2=10.3, y2=-.3,
                  stroke=2,hexcolor=fill_box_color1,)
    # mfoline
    draw_line(c,  x1=1,  y1=1, 
                  x2=1, y2=10,
                  stroke=2,hexcolor=fill_box_color1,)
    # # mfosubline
    draw_line(c,  x1=3.4 ,  y1=1, 
                  x2=3.4 , y2=10,
                  stroke=2,hexcolor=fill_box_color1,)
    # mfosub2line
    draw_line(c,  x1=5.6 ,  y1=1, 
                  x2=5.6 , y2=10,
                  stroke=2,hexcolor=fill_box_color1,)

    # description
    draw_line(c,  x1=8.6 ,  y1=1, 
                  x2=8.6 , y2=10,
                  stroke=2,hexcolor=fill_box_color1,)

    print_report_owner(request,c,  x_axis=.5,  y_axis=0 )              
    # rectangle_address(c)
    # # draw_watermark(c)
    # import_date(c)
    print_table_header(c,y1=1.2)

    

    # print_pageno(c,7.5,pageno)
    # reference_code_print(c,invoice_no)
    pageno+=1
    return c,pageno  
# def text_to_box(text):
# header

def print_table_header(c,y1):    
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 14)
  c.drawString( -.5  * inch, y1 * inch, 'MFO')
  c.drawString( 1.3  * inch, y1 * inch, 'MFO sub')    
  c.drawString( 3.4  * inch, y1 * inch, 'MFO Details')    
  c.drawString( 5.8  * inch, y1 * inch, 'Description')       

def print_report_title(c,y1):
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica-Bold", 18,)
  m_title ='Individual Performance Commitment and Review (IPCR)'
  c.drawString( 3.5  * inch, y1 * inch, m_title)


def put_in_box(c,text,x_axis,y_axis,box_width,max_length_desc,char_length,border_box_color,fill_box_color1):

  new_length = max_length_desc
  n = char_length
  list=[text[i:i+n] for i in range(0, len(text), n)]

  # compare max length of text
  if len(list) > new_length:
    new_length = len(list)
  else:
    new_length = max_length_desc

  print(f'split list :\n {list}')

  text_object = c.beginText()
  text_object.setTextOrigin(x_axis*inch,y_axis*inch)
  text_object.setFillColor(colors.blue)
  text_object.setFillColor(HexColor('#265c2c'))
 #draw rectangle
  c.setLineWidth(1)
  c.setFillColor(HexColor(fill_box_color1)) #choose fill colour

  c.rect(
    (x_axis - .1)*inch,  (y_axis - 0.15)*inch,
    box_width*inch,      ((len(list)/5.9))*inch, 
          fill=1) 
  

  for i in range (len(list)):
    text_object.textLine(list[i])   


  c.drawText(text_object)    
  

  return new_length



def print_body_data(c, row_data ,y_axis,show_mfo,showsub_mfo,border_color,border_box_color,fill_box_color1):
  max_length = 0
  
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 8)

  print(f'\n\n row data : \n {row_data}')
  len_list=0
  
    #printing mfo -----------------------
  m_desc = row_data['mfo__name']
  x_axis=-.5
  box_width=1.5
  max_length_desc=0
  char_length =20
  print(f'type:{show_mfo}')
  if show_mfo:
    
    draw_line(c,  x1=-.8,  y1=y_axis-.29, 
                  x2=15.4, y2=y_axis-.29,
                  stroke=1,hexcolor=border_box_color,)    
    len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc,char_length,border_box_color, fill_box_color1)

  # test returned list              
  if len_list  >     max_length:
    max_length = len_list        


  print(f'list : {len_list}')
  # c.drawString(-.5*inch, y_axis * inch, m_mfo)

  #printing mfosub -----------------------
  m_desc = row_data['mfosub__name']
  x_axis=1.3
  box_width=2.1
  max_length_desc=0
  char_length =30
  if showsub_mfo:
    len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
  # test returned list              
  if len_list  >     max_length:
    max_length = len_list              
  print(f'list : {len_list}')

  # #printing mfosub2__name -----------------------
  m_desc = row_data['mfosub2__name']
  x_axis=3.6
  box_width=2
  max_length_desc=0
  char_length =25
  len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
  # test returned list              
  if len_list  >     max_length:
    max_length = len_list              
  print(f'list : {len_list}')

  

  #printing description -----------------------
  m_desc = row_data['task_desc']
  x_axis=5.8
  box_width=2.7
  max_length_desc=0
  char_length =40

  len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
  # test returned list              
  if len_list  >     max_length:
    max_length = len_list              
  
  print(f'list : {len_list}')



  # #printing history -----------------------
  # m_desc = row_data['task_ref']
  # x_axis=8.7
  # box_width=1.7
  # max_length_desc=0
  # char_length =20

  # len_list  = put_in_box(c,m_desc, 
  #             x_axis,y_axis,
  #             box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
  # # test returned list              
  # if len_list  >     max_length:
  #   max_length = len_list   

  # RELATED history -----------------------
  # # print(f'list : {len_list}')
  myref= row_data['task_ref']
  # # print(f'reference {myref}')
  data_related = TaskTable.objects.get(task_ref=myref).history.all()

  x_axis=9
  height_axis= print_related(c,data_related,x_axis,y_axis)
  print(f'before printing yaxs {y_axis}')
  if height_axis  >     max_length:
    max_length = height_axis  


  return max_length

def print_related(c,data_related,x_axis,y_axis):
  
  for i in data_related:
    # print(f'reference :{i.reference}, date from:  {i.date_from}, date to : {i.date_to}, description :{i.description} ')
    # c.drawString( x_axis  * inch, y_axis * inch,i.description)
    m_desc= i.description
    box_width=1.7
    max_length_desc=0
    char_length =20
    fill_box_color1= '#fce9dd'
    border_box_color='#57d4ef'

    len_list  = put_in_box(c,m_desc, 
              x_axis,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
    my_axis = y_axis+  (len_list/5.9)
    
    
 

    # DATE
    x_axis_date = x_axis + 2
    m_desc= i.date_from.strftime("%m/%d/%Y, %H:%M:%S")
    
    box_width=1
    max_length_desc=0
    char_length =20
    fill_box_color1= '#fce9dd'
    border_box_color='#57d4ef'

    len_list  = put_in_box(c,m_desc, 
              x_axis_date,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
    
    x_axis_date = x_axis + 3.5
    m_desc= i.date_to.strftime("%m/%d/%Y, %H:%M:%S")
    
    box_width=1
    max_length_desc=0
    char_length =20
    fill_box_color1= '#fce9dd'
    border_box_color='#57d4ef'

    len_list  = put_in_box(c,m_desc, 
              x_axis_date,y_axis,
              box_width,max_length_desc,char_length,border_box_color,fill_box_color1)
    
    y_axis = my_axis

    
  return y_axis +3.5 


def check_field_height(text,char_length):
   
  print (f'\n\n**** check field  ***: {text}')
  n = char_length
  list=[text[i:i+n] for i in range(0, len(text), n)]


  fontname = 'Helvetica'
  fontsize = 8

  face = pdfmetrics.getFont(fontname).face
  ascent = (face.ascent * fontsize) / 1000.0
  descent = (face.descent * fontsize) / 1000.0

  height = ascent + descent
  
  mheight=height * (len(list)/3.5)
  print(f'\n\n****height of box :{mheight}')

  return list,mheight
  

def get_next_y_axis(row_data,y_axis):
  text=row_data['mfo__name']
  char_length = 20
  returned_list, height = check_field_height(text,char_length)
  return returned_list, height
def print_now(request,pdf_path, tasklist):

  pageno =1
  c=canvas.Canvas(pdf_path, bottomup=0,  pagesize=(landscape(A3)), )
  #joven
  border_color     = '#529c5d'
  border_box_color = '#ddf4d4'
  fill_box_color1  = '#e7f2e4'
  
  c.translate(inch, inch)  
  c,pageno = print_template(request,c,pageno,border_color,border_box_color,fill_box_color1)  
  y_axis = 1.5

  show_mfo=True
  showsub_mfo=True
  mfo_compare=''
  mfosub_compare=''
  rowcount=0

  for row_number, row_data in enumerate(tasklist):
    next_y_axis =get_next_y_axis(row_data,y_axis)
    print(f'returnedlist : {next_y_axis}')

    rowcount += 1

    if mfo_compare == row_data['mfo__name']:
      show_mfo=False
    else  :
      show_mfo=True
      mfo_compare = row_data['mfo__name']

    if mfosub_compare == row_data['mfosub__name']:
      showsub_mfo=False
    else  :
      showsub_mfo=True
      mfosub_compare = row_data['mfosub__name']

    len_mdesc=print_body_data(c, row_data ,y_axis,show_mfo,showsub_mfo,border_color,border_box_color,fill_box_color1 )
    box_length = len_mdesc/6
    y_axis += 0.15 + box_length

    if (rowcount > 5 ) or y_axis>7:
      rowcount = 1
      c.showPage()      
      c.translate(inch, inch)  # x y position using inch  
      c,pageno = print_template(request,c,pageno,border_color,border_box_color,fill_box_color1)  # load template
      y_axis = 1.5

  c.showPage()
  c.save()
  subprocess.Popen(pdf_path, shell=True)


def using_simpledoc(request):
  tasklist=get_data_to_print(request)
  print(f'tasklist: {tasklist}')
  pdf_path = 'task.pdf'
  print_now(request,pdf_path, tasklist)

import datetime
def generate_posting_refno(mserial=None):
  current_datetime = datetime.datetime.now().strftime('%Y%m%d/%H:%M:%S')
  order_number = current_datetime +'/'+ str(mserial)
  return order_number
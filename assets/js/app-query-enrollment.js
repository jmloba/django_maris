
$(document).ready(function(){

// task table  
function html_record_enrollmnent(x)  {
  html_template=''
  for ( i=0; i < x.length; i++ ){
    html_template +=
    ' <tr id="task-id-'+x[i].id+'"><td data-cell="Student">'+x[i].student+'</td><td data-cell="Course">'+x[i].course+'</td><td data-cell="'+x[i].date_enrolled+'">2024-12-31</td></tr>'

  }    
  return html_template
};

$('#btn-save-add-enrollment').click(function(e){
  e.preventDefault();  
  console.log('add button task enrollment clicked save button')
  var $this = $(this);
  var valid = true;
  let student = $('#id_student :selected').text();
  let course = $('#id_course :selected').text();
  let date_enrolled = $('#id_date_enrolled').val();
  let final_grade = $('#id_final_grade').val();
  let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  let url= $(this).attr('data-url');  
  console.log('student  : ', student, 'course :', course, 'date enrolled :', date_enrolled)
  
  
  mydata = {
    'student' : student,
    'course'  : course, 
    'date_enrolled' : date_enrolled, 
    'final_grade': final_grade, 
    'csrfmiddlewaretoken': csrf_token,
  }

  
  console.log('mydata',mydata)
  $.ajax({
    url: url,
    method : 'POST',
    data : mydata,
    success: function(data){  
      if (data.status==='success'){
        console.log('its an ajax call')


      // x= data.datalist
      // console.log('** success -->> name : ', x)
      // html_template=''
      // if (data.status=='Success'){
      //   console.log('sving success')
      //   html_template=html_record_Task(x)
      //   $('#query-ManyToMany .table-body').html(html_template)
      //   $('#Enrollment-table-modal #enrollment-form')[0].reset()
      //   console.log('returned record ',x)
      //   $("#Enrollment-table-modal").modal("hide");
      //   // clear_data_entries()        
      // }


    }
  },

    error: function(data){  
      console.log ('error :',data.message  )

    }
  
  })
 
})



});
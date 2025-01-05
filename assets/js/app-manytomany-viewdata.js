
$(document).ready(function(){

  // click submit button on Task-table-edit-modal
  $('#student-dashboard main.table .table-body').on("click",".view-data",function(e){
    e.preventDefault()
    var $this = $(this);
    var valid = true;
    let id =$(this).attr('data-stuid');  
    let url= $(this).attr('data-url');  
    console.log('clicked button view  id:', id)
    console.log('url :', url)
    mydata= { 'id':id


    }
    $.ajax({
      url:url,
      data :mydata,
      type : 'GET',
      success : function(data){
        if(data.status=='success'){
          message = data.message
          swal('Successview',message,'success')

        }

      },
      error : function(data){
        if(data.status=='failed'){
          swal('Successview',data.message,'danger')

        }
      }

  })




  })

})

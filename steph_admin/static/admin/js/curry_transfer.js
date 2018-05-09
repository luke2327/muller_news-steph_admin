$('.transfer_push_send').on("click",function(){
  $('#btn_transfer_push').attr('data',$(this).attr('data'));
  $('#mod_transfer_push').modal('show');
});

$('#btn_transfer_push').on("click",function(){
  var datas=$(this).attr('data').split(',');
  console.log('datas : ' + datas[0]);// te1(0;from_team)/te2(1;to_team)
  console.log('datas : ' + datas[1]);// following
  console.log('datas : ' + datas[2]);// transfer_id
  console.log('datas : ' + datas[3]);// player_name
  console.log('datas : ' + datas[4]);// from_team_name
  console.log('datas : ' + datas[5]);// to_team_name
  console.log('datas : ' + datas[6]);// transfer_type
  console.log('datas : ' + datas[7]);// is_loan
  var push_object = new Object();
  push_object.team = datas[0];
  push_object.following = datas[1];
  push_object.transfer_id = datas[2];
  push_object.player_name = datas[3];
  push_object.from_team_name = datas[4];
  push_object.to_team_name = datas[5];
  push_object.transfer_type = datas[6];
  push_object.is_loan = datas[7];
  var json_data = JSON.stringify(push_object);

  $.ajax({
      type : "POST",
      url : "/steph_admin/push_send_transfer/",
      dataType : "text",
      data : json_data,

      error : function(){
          alert('통신실패!!');
          $('#btn_transfer_push').button('reset');
          $('#mod_transfer_push').modal('hide');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          $('#btn_transfer_push').button('reset');
          $('#mod_transfer_push').modal('hide');
      }
  });
});

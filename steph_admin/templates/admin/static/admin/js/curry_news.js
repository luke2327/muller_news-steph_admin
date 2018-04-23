var player;
var team;
var league;
var player_source = new Array();
var team_source = new Array();
var league_source = new Array();

//add following
$('#btn_following_add').click(function(){
  var tag1 = $('#tags1').val();
  var tag2 = $('#tags2').val();
  var tag3 = $('#tags3').val();
  var tag4 = $('#tags4').val();
  var tag5 = $('#tags5').val();
  var tag6 = $('#tags6').val();
  var tag7 = $('#tags7').val();
  var tag8 = $('#tags8').val();
  var tag9 = $('#tags9').val();
  var data_id = $('#add_following_modal').attr("data_id");
  console.log(parseInt(tag1.split('|')[0]));
  var pl_select = "";
  var te_select = "";
  var le_select = "";

  try{
    if(!isNaN(parseInt(tag1.split('|')[0]))){
      console.log('none');
      pl_select += parseInt(tag1.split('|')[0]);
    }
    pl_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag2.split('|')[0]))){
      pl_select += parseInt(tag2.split('|')[0]);
    }
    pl_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag3.split('|')[0]))){
      pl_select += parseInt(tag3.split('|')[0]);
    }
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag4.split('|')[0]))){
      te_select += parseInt(tag4.split('|')[0]);
    }
    te_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag5.split('|')[0]))){
      te_select += parseInt(tag5.split('|')[0]);
    }
    te_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag6.split('|')[0]))){
      te_select += parseInt(tag6.split('|')[0]);
    }
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag7.split('|')[0]))){
      le_select += parseInt(tag7.split('|')[0]);
    }
    le_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag8.split('|')[0]))){
      le_select += parseInt(tag8.split('|')[0]);
    }
    le_select += ",";
  }catch(exception){}

  try{
    if(!isNaN(parseInt(tag9.split('|')[0]))){
      le_select += parseInt(tag9.split('|')[0]);
    }
  }catch(exception){}
  console.log(pl_select)
  console.log(le_select)
  console.log(te_select)
  $.ajax({
      type : "POST",
      url : "http://127.0.0.1:8000/steph_admin/news_relation/",
      dataType : "text",
      headers: {"players" : pl_select,
                "teams" : te_select,
                "leagues" : le_select,
                "id" : data_id,
              },

      error : function(){
          //alert('통신실패!!');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          console.log(data);
          var pl = JSON.parse(data)['players'];
          var te = JSON.parse(data)['teams'];
          var le = JSON.parse(data)['leagues'];
          for(var i=0; i<pl.length; i++){
            $('#following_'+ data_id)
              .append('<li id = "f_add_'+data_id+'_'+pl[i].split('/')[1]+'"><a id = "f_del_'+data_id+'_'+pl[i].split('/')[1]+'" data-toggle="modal" data-target="#del_following"'+
                'class="following_del" following="'+pl[i]+'" data_id="'+data_id+'">'+
                pl[i]+'</a></li>');
            $('#f_del_'+data_id+'_'+pl[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');
            });
          }
          for(var i=0; i<te.length; i++){
            $('#following_'+ data_id)
              .append('<li id = "f_add_'+data_id+'_'+te[i].split('/')[1]+'"><a id = "f_del_'+data_id+'_'+te[i].split('/')[1]+'" data-toggle="modal" data-target="#del_following"'+
                'class="following_del" following="'+te[i]+'" data_id="'+data_id+'">'+
                te[i]+'</a></li>');
            $('#f_del_'+data_id+'_'+te[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');
            });
          }
          for(var i=0; i<le.length; i++){
            $('#following_'+ data_id)
              .append('<li id = "f_add_'+data_id+'_'+le[i].split('/')[1]+'"><a id = "f_del_'+data_id+'_'+le[i].split('/')[1]+'" data-toggle="modal" data-target="#del_following"'+
                'class="following_del" following="'+le[i]+'" data_id="'+data_id+'">'+
                le[i]+'</a></li>');
            $('#f_del_'+data_id+'_'+le[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');
            });
          }
      }
  });
});

$('#btn_del_following').on("click",function(){
  var data_id = $('#del_following').attr("data_id");
  var following = $('#del_following').attr("following");
  $('#btn_del_following').button('loading');
  $.ajax({
      type : "DELETE",
      url : "/steph_admin/news_relation/",
      dataType : "text",
      headers: {"following" : following,
                "id" : data_id,
              },

      error : function(){
          //alert('통신실패!!');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          console.log(data);
          $('#f_add_'+data_id+"_"+following).remove();
          $('#btn_del_following').button('reset');
          $('#del_following').modal('hide');
      }
  });
});
$('.following_add').on("click",function(){
  var data_id = $(this).attr("data_id");
  console.log('data_id : ' + data_id);
  $('#add_following_modal').attr('data_id', data_id);
  if(player && team && league && player.length>0 && team.length>0 && league.length>0){
    console.log('here!')
    initFollowingListModal();
  }else{
    getFollowingList();
  }
});
$('.following_del').on("click",function(){

  var following =  $(this).attr("following");
  var data_id = $(this).attr("data_id");
  console.log('following:' + following + ",data_id : " + data_id);
  $('#del_following').attr('data_id', data_id);
  $('#del_following').attr('following', following.split('/')[1]);

  $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');
  //post code
});
$('#add_following_modal').on('hidden.bs.modal', function () {
    $("#tags1").val("");
    $("#tags2").val("");
    $("#tags3").val("");
    $("#tags4").val("");
    $("#tags5").val("");
    $("#tags6").val("");
    $("#tags7").val("");
    $("#tags8").val("");
    $("#tags9").val("");
});
function getFollowingList(){
  $.ajax({
      type : "GET",
      url : "http://127.0.0.1:8000/steph_admin/followings/",
      dataType : "text",
      error : function(){
          //alert('통신실패!!');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          console.log(data);
          player = JSON.parse(data)['players'];
          team = JSON.parse(data)['teams'];
          league = JSON.parse(data)['leagues'];
          console.log('player:'+player);
          console.log('Tag added !');
          initFollowingListModal();
      }
  });
}
function initFollowingListModal(){
  $(function() {
    $("#tags1").autocomplete({
      source:[player]
    });
  });
  $(function() {
    $("#tags2").autocomplete({
      source:[player]
    });
  });
  $(function() {
    $("#tags3").autocomplete({
      source:[player]
    });
  });
  $(function() {
    $("#tags4").autocomplete({
      source:[team]
    });
  });
  $(function() {
    $("#tags5").autocomplete({
      source:[team]
    });
  });
  $(function() {
    $("#tags6").autocomplete({
      source:[team]
    });
  });
  $(function() {
    $("#tags7").autocomplete({
      source:[league]
    });
  });
  $(function() {
    $("#tags8").autocomplete({
      source:[league]
    });
  });
  $(function() {
    $("#tags9").autocomplete({
      source:[league]
    });
  });

  $('#add_following_modal').modal('show');
}

$('#add_following_modal').on('show.bs.modal', function (e) {
  // $('#tag1').magicsearch({
  //
  //   dataSource: player_source,
  //   fields: ['firstName', 'lastName'],
  //
  //   id: 'id',
  //   format: '%firstName% · %lastName%',
  //   focusShow: true
  // });
});


$(document).ready(function(){



  });

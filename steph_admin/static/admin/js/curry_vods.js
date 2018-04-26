var player;
var team;
var league;
var player_source = new Array();
var team_source = new Array();
var league_source = new Array();
var checked_news = new Array();
var news_id_selected;
var news_lang_selected;
var news_title_selected;
//send pushed
$('.news_push').on("click",function(){
  var news_id = $(this).attr('id').split('-')[1];
  checked_news = new Array();
  news_id_selected = news_id;
  news_lang_selected = $(this).attr('lang');
  news_title_selected = $(this).attr('title');
  datas = $(this).attr('datas').split(',');

  var check_list_default = $('#check_list').clone();
  $("#send_push_body").empty();
  check_list_default.appendTo('#send_push_body');
  check_list_default.show();
  for(var i=0; i<datas.length; i++){
    console.log('hi');
    var check_list = $('#check_list').clone();
    check_list.attr('id', 'send_push' + datas[i].split('/')[2]);
    id_checked_news = 'send_push_input-' + datas[i].split('/')[0] + "-" + datas[i].split('/')[2];
    check_list.children('.form-check-label').text(datas[i]);
    check_list.children('.form-check-input').attr('id', id_checked_news);
    check_list.children('.form-check-label').attr('for', id_checked_news);
    console.log('id_checked_newsa :' + id_checked_news);
    check_list.appendTo('#send_push_body');
    $("#" + id_checked_news).change(function(){
      console.log('id_checked_news :' + $(this).attr('id'));
      if($(this).is(':checked')){
        checked_news.push($(this).attr('id'));
      }else{
        for(var i = 0; i<checked_news.length;i++){
          if(checked_news[i]==$(this).attr('id')){
            checked_news.pop();
            break;
          }
        }
      }
      console.log(checked_news);
    });
  }
  check_list_default.hide();
  $('#send_push').modal('show');
});

$('#btn_send_push').click(function(){
  $('#btn_send_push').button('loading');
  news_push = new Object();
  news_push.news_id = news_id_selected;
  var players = new Array();
  var teams = new Array();
  var leagues = new Array();
  console.log(checked_news);
  for(var i = 0; i<checked_news.length; i++){
    console.log(checked_news[i]);
    if(checked_news[i].includes('League')){
      leagues.push(checked_news[i].split('-')[2]);
    }
    if(checked_news[i].includes('Team')){
      teams.push(checked_news[i].split('-')[2]);
    }
    if(checked_news[i].includes('Player')){
      players.push(checked_news[i].split('-')[2]);
    }
  }
  news_push.leagues = leagues;
  news_push.teams = teams;
  news_push.players = players;
  news_push.title = news_title_selected;
  news_push.lang = news_lang_selected;
  news_push.type = 'vod';
  news_push_json = JSON.stringify(news_push);
  console.log(news_push_json);
  // $('#send_push').modal('hide');

  $.ajax({
      type : "POST",
      url : "/steph_admin/push_send/",
      dataType : "text",
      data : news_push_json,

      error : function(){
          alert('통신실패!!');
          $('#btn_send_push').button('reset');
          $('#send_push').modal('hide');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          var pushed = parseInt($('#id'+news_id_selected+'pushed').text());
          $('#id'+news_id_selected+'pushed').text(pushed+checked_news.length);
          $('#btn_send_push').button('reset');
          $('#send_push').modal('hide');
      }
  });
});
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
      url : "/steph_admin/vods_relation/",
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
                'class="following_del following_pl" following="'+pl[i]+'" data_id="'+data_id+'">'+
                pl[i]+'</a></li>');

            var push_datas = $('#push-'+ data_id).attr('datas');
            push_datas = push_datas + ',Player/' + pl[i];
            $('#push-'+ data_id).attr('datas', push_datas);

            $('#f_del_'+data_id+'_'+pl[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');

              var before_datas = $('#push-'+ data_id).attr('datas').split(',');
              var data = 'Player/' + following;
              for (var i = 0 ; i<before_datas.length; i++){
                console.log(before_datas[i]);
                console.log(before_datas[i]);
                if(before_datas[i] == data){
                  before_datas.pop();
                  break;
                }
              }
              $('#push-'+ data_id).attr('datas', before_datas.join());
            });
          }
          for(var i=0; i<te.length; i++){
            $('#following_'+ data_id)
              .append('<li id = "f_add_'+data_id+'_'+te[i].split('/')[1]+'"><a id = "f_del_'+data_id+'_'+te[i].split('/')[1]+'" data-toggle="modal" data-target="#del_following"'+
                'class="following_del  following_te" following="'+te[i]+'" data_id="'+data_id+'">'+
                te[i]+'</a></li>');

            var push_datas = $('#push-'+ data_id).attr('datas');
            push_datas = push_datas + ',Team/' + te[i];
            $('#push-'+ data_id).attr('datas', push_datas);

            $('#f_del_'+data_id+'_'+te[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');

              var before_datas = $('#push-'+ data_id).attr('datas').split(',');
              var data = 'Team/' + following;
              for (var i = 0 ; i<before_datas.length; i++){
                if(before_datas[i] == data){
                  before_datas.pop();
                  break;
                }
              }
              $('#push-'+ data_id).attr('datas', before_datas.join());
            });
          }
          for(var i=0; i<le.length; i++){
            $('#following_'+ data_id)
              .append('<li id = "f_add_'+data_id+'_'+le[i].split('/')[1]+'"><a id = "f_del_'+data_id+'_'+le[i].split('/')[1]+'" data-toggle="modal" data-target="#del_following"'+
                'class="following_del following_le" following="'+le[i]+'" data_id="'+data_id+'">'+
                le[i]+'</a></li>');

            var push_datas = $('#push-'+ data_id).attr('datas');
            push_datas = push_datas + ',League/' + le[i];
            $('#push-'+ data_id).attr('datas', push_datas);

            $('#f_del_'+data_id+'_'+le[i].split('/')[1]).on("click",function(){
              var following =  $(this).attr("following");
              var data_id = $(this).attr("data_id");
              console.log('following:' + following + ",data_id : " + data_id);
              $('#del_following').attr('data_id', data_id);
              $('#del_following').attr('following', following.split('/')[1]);

              $('#del_following_body').text('news id : ' + data_id + '   ' + following + ' 을(를) 삭제합니다');

              var before_datas = $('#push-'+ data_id).attr('datas').split(',');
              var data = 'League/' + following;
              for (var i = 0 ; i<before_datas.length; i++){
                if(before_datas[i] == data){
                  before_datas.pop();
                  break;
                }
              }
              $('#push-'+ data_id).attr('datas', before_datas.join());
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
      url : "/steph_admin/vods_relation/",
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
      url : "/steph_admin/followings/",
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

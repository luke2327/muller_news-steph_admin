$('#add_lineup').click(function(){
  console.log('good');
  $('#add_all_lineup').modal('show');
});
$('#btn_add_lineup').click(function(){
  $('#btn_add_lineup').button('loading');
  console.log('hi');
  var match_id = $('#input_match_id').val();

  var team1 = new Array();
  var team2 = new Array();

  for (var i = 1; i<=20; i++){
    var team1_lineup_number = $('#ln_1_' + i).val();
    var team2_lineup_number = $('#ln_2_' + i).val();
    var team1_shirt_number = $('#sn_1_' + i).val();
    var team2_shirt_number = $('#sn_2_' + i).val();
    var team1_position = $('#p_1_' + i).val();
    var team2_position = $('#p_2_' + i).val();
    var team1_name = $('#n_1_' + i).val();
    var team2_name = $('#n_2_' + i).val();

    var pl1 = new Object();
    var pl2 = new Object();

    pl1.lineup_number = team1_lineup_number;
    pl1.shirt_number = team1_shirt_number;
    pl1.position = team1_position;
    pl1.name = team1_name;

    pl2.lineup_number = team2_lineup_number;
    pl2.shirt_number = team2_shirt_number;
    pl2.position = team2_position;
    pl2.name = team2_name;
    console.log(team1);
    console.log(pl1.name!='');
    if(typeof(pl1.name) != "undefined" && pl1.name!=''){
      team1.push(pl1);
    }
    if(typeof(pl2.name) != "undefined" && pl2.name!=''){
      team2.push(pl2);
    }
  }
  console.log(JSON.stringify(team1));
  console.log(JSON.stringify(team2));
  lineup = new Object();
  lineup.match_id = match_id;
  lineup.team1 = team1;
  lineup.team2 = team2;
  lineup_json = JSON.stringify(lineup);

  $.ajax({
      type : "POST",
      url : "/steph_admin/lineup/",
      dataType : "json",
      data : lineup_json,

      error : function(){
          console.log('error');
          alert('라인업 추가실패!!');
      },
      success : function(data){
          //alert("통신데이터 값 : " + data) ;
          // alert('라인업 추가성공!!');
          console.log(data);
          // $('#f_add_'+data_id+"_"+following).remove();
          $('#btn_add_lineup').button('reset');
          $('#add_all_lineup').modal('hide');
          location.reload();
      }
  });
});

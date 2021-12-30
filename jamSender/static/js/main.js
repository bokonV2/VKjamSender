
function erroeHand(jqXHR, exception){
  if (jqXHR.status === 0) {
    alert('НЕ подключен к интернету!');
  } else if (jqXHR.status == 404) {
    alert('НЕ найдена страница запроса [404])');
  } else if (jqXHR.status == 500) {
    alert('НЕ найден домен в запросе [500].');
  } else if (exception === 'parsererror') {
    alert("Ошибка в коде: \n"+jqXHR.responseText);
  } else if (exception === 'timeout') {
    alert('Не ответил на запрос.');
  } else if (exception === 'abort') {
    alert('Прерван запрос Ajax.');
  } else {
    alert('Неизвестная ошибка:\n' + jqXHR.responseText);
  }
};

function sendId(gname) {
  document.getElementById('spin').style.display = 'block';
  $.ajax({
      url: '/jamSender/startId',
      method: 'post',
      dataType: 'json',
      data: {'gName': gname},
      error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
      success: function(){
        console.log("Successful sendId");
        window.location.reload();
      }
  });
};

function send(){
  document.getElementById('spin').style.display = 'block';
  document.getElementById("But").disabled = true;
  $.ajax({
    url: '/jamSender/start',
    method: 'post',
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(){
      console.log("Successful send");
      window.location.reload();
    }
  });
};

function reserSt(){
  document.getElementById('spin').style.display = 'block';
  document.getElementById("But2").disabled = true;
  $.ajax({
    url: '/jamSender/reset',
    method: 'post',
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(){
      console.log("Successful send");
      window.location.reload();
    }
  });
};

function removeGroup(gname){
  document.getElementById('spin').style.display = 'block';
  $.ajax({
    url: '/jamSender/removeGroup',
    method: 'post',
    data: {'gName': gname},
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(){
      console.log("Successful delete");
      window.location.reload();
    }
  });
};

function addGroup() {
  document.getElementById('spin').style.display = 'block';
  document.getElementById("btn").disabled = true;
  $.ajax({
    url: '/jamSender/addGroup',
    type: 'post',
    dataType: "html",
    data: $("#ajax_form").serialize(),
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(response) {
      console.log("Successful send");
      window.location.reload();
    },
 });
};

function addPayDay() {
  document.getElementById('spin').style.display = 'block';
  document.getElementById("btn2").disabled = true;
  $.ajax({
    url: '/jamSender/addPayDay',
    type: 'post',
    dataType: "html",
    data: $("#ajax_form2").serialize(),
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(response) {
      console.log("Successful send");
      window.location.reload();
    },
 });
};

function getInfGroup(group_url) {
  $.ajax({
    url: '/jamSender/getInfGroup',
    type: 'post',
    dataType: "html",
    data: {group_url:group_url},
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(response) {
      var obj = JSON.parse(response);
      document.getElementById('group_url').value = obj["group_url"];
      document.getElementById('chat_url').value = obj["chat_url"];
      document.getElementById('money').value = obj["money"];
      document.getElementById('styleBg').value = obj["styleBg"];
      document.getElementById('styleFr').value = obj["styleFr"];
      document.getElementById('date_oplata').value = obj["date_oplata"];
      document.getElementById('time_send').value = obj["time_send"];
      document.getElementById('period').value = obj["period"];
      document.getElementById('type_send').value = obj["type_send"];
      document.getElementById('message').value = obj["message"];
      $('.popup-fade').fadeIn();
      // window.location.reload();
    },
 });
};

function openWin(gName, money, payDay){
  $('.popup-fade').fadeIn();
  document.getElementById("gName").value = gName;
  document.getElementById("payDay").value = payDay;
  document.getElementById("money").value = money;
};

function toggleColumn(columnClass) {
  console.log(columnClass)
	const cells = document.querySelectorAll(`.${columnClass}`);
  cells.forEach(cell => {
  	cell.classList.toggle('hidden');
  });
}

function spins() {
  document.getElementById('spin').style.display = 'block';
};

$( document ).ready(function() {
  const controls = document.getElementById('controls');
  controls.addEventListener('change', e => {
    toggleColumn(e.target.dataset.columnClass);
  });
  // popup1
  $("#btn").click(function(){addGroup();});
  $('.popup-open').click(function() {
  $('.popup-fade').fadeIn();
    return false;
  });
  $('.popup-close').click(function() {
    $(this).parents('.popup-fade').fadeOut();
    return false;
  });
  // $('.popup-fade').click(function(e) {
  //   if ($(e.target).closest('.popup').length == 0) {
  //     $(this).fadeOut();
  //  }});
  // popup2
  $("#btn2").click(function(){addPayDay();});
  $('.popup-open2').click(function() {
  $('.popup-fade2').fadeIn();
    return false;
  });
  $('.popup-close2').click(function() {
    $(this).parents('.popup-fade2').fadeOut();
    return false;
  });
  // $('.popup-fade2').click(function(e) {
  //   if ($(e.target).closest('.popup2').length == 0) {
  //     $(this).fadeOut();
  //  }});
});

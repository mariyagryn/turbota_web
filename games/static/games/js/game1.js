var em = ["💐","🌹","🌻","🏵️","🌺","🌴","🌈","🍓","🍒","🍎","🍉","🍊","🥭","🍍","🍋","🍏","🍐","🥝","🍇","🥥","🍅","🌶️","🍄","🧅","🥦","🥑","🍔","🍕","🧁","🎂","🍬","🍩","🍫","🎈"];
//Shuffling above array
var tmp, c, p = em.length;
if(p) while(--p) {
   c = Math.floor(Math.random() * (p + 1));
   tmp = em[c];
   em[c] = em[p];
   em[p] = tmp;
}

//Variables
var pre="", pID, ppID=0, turn=0, t="transform", flip="rotateY(180deg)", flipBack="rotateY(0deg)", time, mode;

//Resizing Screen
window.onresize = init;
function init() {
   W = innerWidth;
   H = innerHeight;
   $('body').height(H+"px");
   $('#ol').height(H+"px");
}

//Showing instructions
window.onload = function() {
    $("#ol").html(`<center><div id="inst"><h3>Вітаємо!</h3>Інструкції до гри<br/><br/><li>Знаходьте пари однакових карток, відкриваючи їх.</li><li>Щоб відкрити картку, натисніть на неї.</li><li>Якщо дві відкриті картки не співпадають, вони закриються.</li><p style="font-size:18px;">Оберіть рівень складності для початку гри.</p></div><button onclick="start(3, 4)">3 × 4</button> <button onclick="start(4, 4)">4 × 4</button><button onclick="start(4, 5)">4 × 5</button><button onclick="start(5, 6)">5 × 6</button><button onclick="start(6, 6)">6 × 6</button><a href="/games/" class="btn-exit-game" style="display:inline-block;margin-left:10px;margin-top:10px;padding:5px 18px;font-size:18px;border-radius:10px;border:0.1px solid #fff;background:#dc3545;color:#fff;text-decoration:none;font-weight:600;">Вийти</a></center>`);
}

//Starting the game
function start(r,l) {
    //Timer and moves
    min=0, sec=0, moves=0;
    $("#time").html("Час: 00:00");
    $("#moves").html("Ходи: 0");
    time = setInterval(function() {
      sec++;
      if(sec==60) {
          min++; sec=0;
      }
      if(sec<10) 
          $("#time").html("Час: 0"+min+":0"+sec);
      else
        $("#time").html("Час: 0"+min+":"+sec);
    }, 1000);
    rem=r*l/2, noItems=rem;
    mode = r+"x"+l;
    //Generating item array and shuffling it
    var items = [];
    for (var i=0;i<noItems;i++)
        items.push(em[i]);
    for (var i=0;i<noItems;i++)
        items.push(em[i]);
    var tmp, c, p = items.length;
    if(p) while(--p) {
        c = Math.floor(Math.random() * (p + 1));
        tmp = items[c];
        items[c] = items[p];
        items[p] = tmp;
    }
    
    //Creating table
    $("table").html("");
    var n=1;
    for (var i = 1;i<=r;i++) {
        $("table").append("<tr>");
        for (var j = 1;j<=l;j++) {
           $("table").append(`<td id='${n}' onclick="change(${n})"><div class='inner'><div class='front'></div><div class='back'><p>${items[n-1]}</p></div></div></td>`);
           n++;
         }
         $("table").append("</tr>");
    }
    
    //Hiding instructions screen
    $("#ol").fadeOut(500);
}

//Function for flipping blocks
function change(x) {
  //Variables
  let i = "#"+x+" .inner";
  let f = "#"+x+" .inner .front";
  let b = "#"+x+" .inner .back";
  
  //Dont flip for these conditions
  if (turn==2 || $(i).attr("flip")=="block" || ppID==x) {}
  
  //Flip
  else {
    $(i).css(t, flip);
    if (turn==1) {
      //This value will prevent spam clicking
      turn=2;
      
      //If both flipped blocks are not same
      if (pre!=$(b).text()) {
         setTimeout(function() {
            $(pID).css(t, flipBack);
            $(i).css(t, flipBack);
            ppID=0;
         },1000);
      }
      
      //If blocks flipped are same
      else {
          rem--;
          $(i).attr("flip", "block");
          $(pID).attr("flip", "block");
      }
      
      setTimeout(function() {
         turn=0;
         //Increase moves
         moves++;
         $("#moves").html("Ходи: "+moves);
      },1150);
      
    }
    else {
      pre = $(b).text();
      ppID = x;
      pID = "#"+x+" .inner";
      turn=1;
    }
    
    //If all pairs are matched
    if (rem==0) {
          clearInterval(time);
          let timeStr = (min==0) ? `${sec} секунд` : `${min} хвилин(и) і ${sec} секунд`;
          setTimeout(function() {
              $("#ol").html(`<center><div id="iol"><h2>Вітаємо!</h2><p style="font-size:23px;padding:10px;">Ви пройшли рівень ${mode} за ${moves} ходів. Це зайняло ${timeStr}.</p><p style="font-size:18px">Грати ще раз?</p><button onclick="start(3, 4)">3 × 4</button> <button onclick="start(4, 4)">4 × 4</button><button onclick="start(4, 5)">4 × 5</button><button onclick="start(5, 6)">5 × 6</button><button onclick="start(6, 6)">6 × 6</button><a href="/games/" class="btn-exit-game" style="display:inline-block;margin-left:10px;margin-top:10px;padding:5px 18px;font-size:18px;border-radius:10px;border:0.1px solid #fff;background:#dc3545;color:#fff;text-decoration:none;font-weight:600;">Вийти</a></div></center>`);
              $("#ol").fadeIn(750);
          }, 1500);
    }
  }
}

$(document).ready(function() {
    $("#restart-btn").on("click", function() {
        window.location.reload();
    });
});
